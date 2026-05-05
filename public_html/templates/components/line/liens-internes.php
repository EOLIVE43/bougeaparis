<?php
/**
 * Section Liens internes — Page ligne de métro
 *
 * Affiche le maillage interne pour le SEO et la navigation :
 * - Lignes en correspondance (métro, RER, tram, transilien) avec pastilles colorées
 * - Autres lignes de métro à découvrir
 * - Pages liées (parents, soeurs, ressources)
 *
 * Variables attendues :
 * - $line : array, données de la ligne (incluant 'internal_links' et 'intros.liens_internes')
 *
 * Stratégie SEO :
 * - Maillage interne fort (signal de cocon sémantique)
 * - Couleurs officielles IDFM pour identification visuelle
 * - Texte ancrage pertinent ("Ligne 4", "RER A", etc.) UNIQUEMENT sur le titre
 * - Smart linking : si la page de destination n'existe pas (cf. Routes::active),
 *   le titre devient un <span> non cliquable (--inactive). Évite les liens 404.
 *
 * Stratégie UX :
 * - Pastilles colorées (rapides à scanner)
 * - Stations en correspondance affichées sous le titre, non cliquables
 * - 3 niveaux : correspondances directes / découverte / pages liées
 */

$internalLinks = $line['internal_links'] ?? null;
if (!$internalLinks) {
    return;
}

$introText = $line['intros']['liens_internes'] ?? null;
?>

<section class="section section--liens" id="liens" aria-labelledby="liens-title">

  <h2 id="liens-title">Pour aller plus loin sur la ligne <?= htmlspecialchars($line['code']) ?> et au-delà</h2>

  <!-- Intro -->
  <div class="liens__intro">
    <?php if ($introText): ?>
      <p><?= $introText ?></p>
    <?php else: ?>
      <p>Découvrez les lignes en correspondance et les autres pages utiles pour vos déplacements.</p>
    <?php endif; ?>
  </div>

  <!-- ========================================== -->
  <!-- CORRESPONDANCES MÉTRO -->
  <!-- ========================================== -->
  <?php if (!empty($internalLinks['connections_metro'])): ?>
    <div class="liens__group">
      <h3 class="liens__subtitle">
        <span class="liens__subtitle-icon" aria-hidden="true">🚇</span>
        Lignes de métro en correspondance avec la ligne <?= htmlspecialchars($line['code']) ?>
      </h3>
      <div class="liens__cards">
        <?php foreach ($internalLinks['connections_metro'] as $conn): ?>
          <article class="line-card">
            <span class="line-card__pastille">
              <?= pastilleCorresp('M', $conn['code'], $conn['color'], 'inline') ?>
            </span>
            <span class="line-card__content">
              <span class="line-card__name">
                <?= conditionalLink($conn['url'], htmlspecialchars($conn['name']), 'line-card__name-link') ?>
              </span>
              <?php if (!empty($conn['stations'])): ?>
                <span class="line-card__stations">
                  À <?= count($conn['stations']) ?> station<?= count($conn['stations']) > 1 ? 's' : '' ?>&nbsp;:
                  <?php
                    // Smart linking sur chaque nom de station
                    $stationLinks = array_map(
                        fn($s) => stationLink($s, 'line-card__station-link'),
                        $conn['stations']
                    );
                    echo implode(', ', $stationLinks);
                  ?>
                </span>
              <?php endif; ?>
            </span>
          </article>
        <?php endforeach; ?>
      </div>
    </div>
  <?php endif; ?>

  <!-- ========================================== -->
  <!-- CORRESPONDANCES RER + AUTRES -->
  <!-- ========================================== -->
  <?php if (!empty($internalLinks['connections_rer']) || !empty($internalLinks['connections_other'])): ?>
    <div class="liens__group">
      <h3 class="liens__subtitle">
        <span class="liens__subtitle-icon" aria-hidden="true">🚆</span>
        RER, tramway et Transilien en correspondance
      </h3>
      <div class="liens__cards">
        <?php
        $merged = array_merge($internalLinks['connections_rer'] ?? [], $internalLinks['connections_other'] ?? []);
        foreach ($merged as $conn):
            // Détecter le mode (RER, T, TRANS) depuis le code de la ligne
            $code = strtoupper($conn['code'] ?? '');
            if (preg_match('/^[A-E]$/', $code)) {
                $mode = 'RER';
                $line = $code;
            } elseif (preg_match('/^T(\d+[ab]?)$/i', $code, $m)) {
                $mode = 'T';
                $line = $m[1];
            } else {
                // Transilien (J, L, U, N, P, R...) ou autre
                $mode = 'TRANS';
                $line = $code;
            }
        ?>
          <article class="line-card">
            <span class="line-card__pastille">
              <?= pastilleCorresp($mode, $line, $conn['color'], 'inline') ?>
            </span>
            <span class="line-card__content">
              <span class="line-card__name">
                <?= conditionalLink($conn['url'], htmlspecialchars($conn['name']), 'line-card__name-link') ?>
              </span>
              <?php if (!empty($conn['stations'])): ?>
                <span class="line-card__stations">
                  À <?= count($conn['stations']) ?> station<?= count($conn['stations']) > 1 ? 's' : '' ?>&nbsp;:
                  <?php
                    $stationLinks = array_map(
                        fn($s) => stationLink($s, 'line-card__station-link'),
                        $conn['stations']
                    );
                    echo implode(', ', $stationLinks);
                  ?>
                </span>
              <?php endif; ?>
            </span>
          </article>
        <?php endforeach; ?>
      </div>
    </div>
  <?php endif; ?>

  <!-- ========================================== -->
  <!-- DÉCOUVRIR D'AUTRES LIGNES -->
  <!-- ========================================== -->
  <?php if (!empty($internalLinks['discover_metro_lines'])): ?>
    <div class="liens__group">
      <h3 class="liens__subtitle">
        <span class="liens__subtitle-icon" aria-hidden="true">🔍</span>
        Découvrir d'autres lignes de métro parisien
      </h3>
      <div class="liens__discover">
        <?php foreach ($internalLinks['discover_metro_lines'] as $disc):
            $isCurrent = !empty($disc['is_current']);
            $exists = !$isCurrent && Routes::exists(rtrim($disc['url'] ?? '', '/'));
            $tagOpen  = $isCurrent ? '<span aria-current="page"' : ($exists ? '<a href="' . htmlspecialchars($disc['url']) . '"' : '<span data-future-url="' . htmlspecialchars($disc['url'] ?? '') . '"');
            $tagClose = ($exists && !$isCurrent) ? '</a>' : '</span>';
            $cssClass = 'discover-pill';
            if ($isCurrent) $cssClass .= ' discover-pill--current';
            if (!$exists && !$isCurrent) $cssClass .= ' discover-pill--inactive';
        ?>
          <?= $tagOpen ?> class="<?= $cssClass ?>">
            <span class="discover-pill__pastille">
              <?= pastilleCorresp('M', $disc['code'], $disc['color'], 'inline') ?>
            </span>
            <span class="discover-pill__name"><?= htmlspecialchars($disc['name']) ?></span>
          <?= $tagClose ?>
        <?php endforeach; ?>
      </div>
    </div>
  <?php endif; ?>

  <!-- ========================================== -->
  <!-- PAGES LIÉES -->
  <!-- ========================================== -->
  <?php if (!empty($internalLinks['related_pages'])): ?>
    <div class="liens__group">
      <h3 class="liens__subtitle">
        <span class="liens__subtitle-icon" aria-hidden="true">📍</span>
        Pages liées au métro parisien
      </h3>
      <div class="liens__related">
        <?php foreach ($internalLinks['related_pages'] as $page):
            $exists = Routes::exists(rtrim($page['url'] ?? '', '/'));
            $cssClass = 'related-card' . ($exists ? '' : ' related-card--inactive');
            $futureAttr = $exists ? '' : ' data-future-url="' . htmlspecialchars($page['url'] ?? '') . '"';
        ?>
          <div class="<?= $cssClass ?>"<?= $futureAttr ?>>
            <span class="related-card__icon" aria-hidden="true"><?= htmlspecialchars($page['icon']) ?></span>
            <span class="related-card__content">
              <?php if ($exists): ?>
                <a href="<?= htmlspecialchars($page['url']) ?>" class="related-card__title-link"><?= htmlspecialchars($page['label']) ?></a>
              <?php else: ?>
                <span class="related-card__label"><?= htmlspecialchars($page['label']) ?></span>
              <?php endif; ?>
              <span class="related-card__desc"><?= htmlspecialchars($page['description']) ?></span>
            </span>
            <?php if ($exists): ?><span class="related-card__arrow" aria-hidden="true">→</span><?php endif; ?>
          </div>
        <?php endforeach; ?>
      </div>
    </div>
  <?php endif; ?>

</section>
