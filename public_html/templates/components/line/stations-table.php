<?php
/**
 * Section Tableau des stations — Page ligne de métro
 *
 * Liste complète des stations avec correspondances et PMR.
 * Schema.org : ItemList contenant des Place pour rich snippets.
 *
 * Variables attendues :
 * - $line : array, données de la ligne
 */

$stations = $line['stations'];
$totalStations = count($stations);

// Helper : transforme un slug à partir d'un nom
function stationToSlug($name) {
  $slug = mb_strtolower($name);
  $slug = strtr($slug, [
    'à'=>'a','á'=>'a','â'=>'a','ä'=>'a','ã'=>'a',
    'é'=>'e','è'=>'e','ê'=>'e','ë'=>'e',
    'í'=>'i','ì'=>'i','î'=>'i','ï'=>'i',
    'ó'=>'o','ò'=>'o','ô'=>'o','ö'=>'o','õ'=>'o',
    'ú'=>'u','ù'=>'u','û'=>'u','ü'=>'u',
    'ç'=>'c','ñ'=>'n', "'"=>'-', ' '=>'-'
  ]);
  $slug = preg_replace('/[^a-z0-9\-]/', '', $slug);
  $slug = preg_replace('/-+/', '-', $slug);
  return trim($slug, '-');
}
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

  <!-- Schema.org ItemList -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Stations de la ligne <?= htmlspecialchars($line['code']) ?> du métro parisien",
    "numberOfItems": <?= $totalStations ?>,
    "itemListElement": [
      <?php foreach ($stations as $i => $station): ?>
      {
        "@type": "ListItem",
        "position": <?= $i + 1 ?>,
        "item": {
          "@type": "Place",
          "name": <?= json_encode($station['name'] . (!empty($station['subtitle']) ? ' (' . $station['subtitle'] . ')' : '')) ?>,
          "url": "https://bougeaparis.fr/metro/ligne-<?= $line['code'] ?>/<?= stationToSlug($station['name']) ?>/"
        }
      }<?= $i < $totalStations - 1 ? ',' : '' ?>
      <?php endforeach; ?>
    ]
  }
  </script>

  <!-- Tableau des stations -->
  <div class="stations-table__wrapper">
    <table class="stations-table">
      <thead>
        <tr>
          <th class="stations-table__col-num" scope="col">#</th>
          <th class="stations-table__col-name" scope="col">Station</th>
          <th class="stations-table__col-corresp" scope="col">Correspondances</th>
          <th class="stations-table__col-pmr" scope="col" title="Personnes à mobilité réduite">
            <span class="visually-hidden">Accessibilité PMR</span>
            <span aria-hidden="true">♿</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <?php foreach ($stations as $i => $station):
          $isMajor = $station['is_major'];
          $stationSlug = stationToSlug($station['name']);
          $stationUrl = '/metro/ligne-' . $line['code'] . '/' . $stationSlug . '/';
        ?>
          <tr class="<?= $isMajor ? 'stations-table__row--major' : '' ?>">

            <!-- Numéro de la station -->
            <td class="stations-table__col-num">
              <span class="stations-table__num"><?= $i + 1 ?></span>
            </td>

            <!-- Nom de la station -->
            <td class="stations-table__col-name">
              <a href="<?= htmlspecialchars($stationUrl) ?>" class="stations-table__name-link">
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
              </a>
            </td>

            <!-- Correspondances -->
            <td class="stations-table__col-corresp">
              <?php if (!empty($station['correspondences'])): ?>
                <div class="stations-table__corresp">
                  <?php foreach ($station['correspondences'] as $corresp): ?>
                    <span class="pastille-corresp pastille-corresp--inline" style="border-color: <?= htmlspecialchars($corresp['color']) ?>;">
                      <span class="pastille-corresp__mode" style="color: <?= htmlspecialchars($corresp['color']) ?>;"><?= htmlspecialchars($corresp['mode']) ?></span><span class="pastille-corresp__line" style="color: <?= htmlspecialchars($corresp['color']) ?>;"><?= htmlspecialchars($corresp['line']) ?></span>
                    </span>
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

  <!-- Note légale et lien PMR -->
  <p class="stations-table__note">
    <span class="stations-table__pmr stations-table__pmr--yes" aria-hidden="true">✓</span>
    Stations <strong>accessibles aux personnes à mobilité réduite (PMR)</strong>.
    <a href="#accessibilite">Voir le détail de l'accessibilité sur la ligne <?= htmlspecialchars($line['code']) ?></a>.
  </p>

</section>
