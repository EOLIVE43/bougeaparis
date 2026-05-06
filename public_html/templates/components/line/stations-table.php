<?php
/**
 * Section Tableau des stations — Page ligne de métro
 *
 * Liste complète des stations avec correspondances et PMR.
 *
 * v1.3 — Refactor :
 * - URL canonique stations : /metro/station/{slug}/ (au lieu de /metro/ligne-1/{slug}/)
 *   → évite duplicate content (Châtelet est sur 5 lignes mais a 1 seule URL)
 * - Smart linking via Routes::exists() : noms inactifs/gris si page pas créée
 * - Pastilles correspondances en SVG (pastilleCorresp()) pour cohérence avec le plan
 *
 * Variables attendues :
 * - $line : array, données de la ligne
 */

$stations = $line['stations'];
$totalStations = count($stations);
?>

<section class="section section--stations-table" id="stations-table" aria-labelledby="stations-title">

  <h2 id="stations-title">Liste des <?= $totalStations ?> stations de la ligne <?= htmlspecialchars($line['code']) ?></h2>

  <div class="stations-table__intro">
    <?php if (!empty($line['intros']['stations'])): ?>
      <p><?= $line['intros']['stations'] ?></p>
    <?php else: ?>
      <p>Voici la <strong>liste complète des <?= $totalStations ?> stations de la ligne <?= htmlspecialchars($line['code']) ?></strong> du métro parisien, dans l'ordre de circulation entre <strong><?= htmlspecialchars($line['terminus_a']) ?></strong> et <strong><?= htmlspecialchars($line['terminus_b']) ?></strong>. Pour chaque station, retrouvez les correspondances et l'accessibilité PMR.</p>
    <?php endif; ?>
  </div>

  <!-- Schema.org : ItemList des stations (E-E-A-T + données structurées) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Stations de la ligne <?= htmlspecialchars($line['code']) ?>",
    "numberOfItems": <?= $totalStations ?>,
    "itemListElement": [
      <?php foreach ($stations as $i => $station): ?>
      {
        "@type": "ListItem",
        "position": <?= $i + 1 ?>,
        "name": <?= json_encode($station['name'] . (!empty($station['subtitle']) ? ' (' . $station['subtitle'] . ')' : '')) ?>,
        "url": "https://bougeaparis.fr<?= Routes::stationUrl($station['name']) ?>"
      }<?= $i < $totalStations - 1 ? ',' : '' ?>
      <?php endforeach; ?>
    ]
  }
  </script>

  <!-- Tableau des stations -->
  <div class="stations-table__wrapper">
    <table class="stations-table">
      <caption class="sr-only">Liste des stations de la ligne <?= htmlspecialchars($line['code']) ?> du métro avec correspondances et accessibilité PMR.</caption>
      <thead>
        <tr>
          <th class="stations-table__col-num" scope="col">#</th>
          <th class="stations-table__col-name" scope="col">Station</th>
          <th class="stations-table__col-corresp" scope="col">Correspondances</th>
          <th class="stations-table__col-pmr" scope="col">
            <span aria-label="Accessibilité PMR" title="Accessibilité PMR">♿</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <?php foreach ($stations as $i => $station):
          $isMajor = $station['is_major'] ?? false;
          $stationUrl = Routes::stationUrl($station['name']);
          $stationActive = Routes::exists(rtrim($stationUrl, '/'));
        ?>
          <tr class="<?= $isMajor ? 'stations-table__row--major' : '' ?>">

            <!-- Numéro de la station -->
            <td class="stations-table__col-num">
              <span class="stations-table__num"><?= $i + 1 ?></span>
            </td>

            <!-- Nom de la station + sous-titre + label culturel -->
            <td class="stations-table__col-name">
              <?php if ($stationActive): ?>
                <a href="<?= htmlspecialchars($stationUrl) ?>" class="stations-table__name-link">
              <?php else: ?>
                <span class="stations-table__name-link stations-table__name-link--inactive" data-future-url="<?= htmlspecialchars($stationUrl) ?>">
              <?php endif; ?>
                <span class="stations-table__name <?= $isMajor ? 'stations-table__name--major' : '' ?>">
                  <?= htmlspecialchars($station['name']) ?>
                </span>
                <?php if (!empty($station['subtitle'])): ?>
                  <span class="stations-table__subtitle"><?= htmlspecialchars($station['subtitle']) ?></span>
                <?php endif; ?>
                <?php if (!empty($station['cultural_label'])): ?>
                  <span class="stations-table__label">
                    <?= str_replace("\n", ' · ', htmlspecialchars($station['cultural_label'])) ?>
                  </span>
                <?php endif; ?>
              <?= $stationActive ? '</a>' : '</span>' ?>
            </td>

            <!-- Correspondances (pastilles SVG style "plan visuel") -->
            <td class="stations-table__col-corresp">
              <?php if (!empty($station['correspondences'])): ?>
                <div class="stations-table__corresp">
                  <?php foreach ($station['correspondences'] as $corresp): ?>
                    <?= pastilleCorresp(
                        $corresp['mode'],
                        $corresp['line'],
                        $corresp['color'],
                        'small'
                    ) ?>
                  <?php endforeach; ?>
                </div>
              <?php else: ?>
                <span class="stations-table__no-corresp" aria-label="Aucune correspondance">—</span>
              <?php endif; ?>
            </td>

            <!-- Accessibilité PMR -->
            <td class="stations-table__col-pmr">
              <?php if ($station['accessible']): ?>
                <span class="stations-table__pmr stations-table__pmr--yes" title="Station accessible PMR" aria-label="Station accessible PMR">
                  ✓
                </span>
              <?php else: ?>
                <span class="stations-table__pmr stations-table__pmr--no" title="Station non accessible PMR" aria-label="Station non accessible PMR">
                  —
                </span>
              <?php endif; ?>
            </td>

          </tr>
        <?php endforeach; ?>
      </tbody>
    </table>
  </div>

</section>
