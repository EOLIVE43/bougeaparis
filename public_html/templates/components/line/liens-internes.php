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
 * - Texte ancrage pertinent ("Ligne 4", "RER A", etc.)
 *
 * Stratégie UX :
 * - Pastilles colorées (rapides à scanner)
 * - Stations en correspondance affichées
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
          <a href="<?= htmlspecialchars($conn['url']) ?>" class="line-card">
            <span class="line-card__pill" style="background:<?= htmlspecialchars($conn['color']) ?>;color:<?= htmlspecialchars($conn['color_text']) ?>;">
              <?= htmlspecialchars($conn['code']) ?>
            </span>
            <span class="line-card__content">
              <span class="line-card__name"><?= htmlspecialchars($conn['name']) ?></span>
              <?php if (!empty($conn['stations'])): ?>
                <span class="line-card__stations">
                  À <?= count($conn['stations']) ?> station<?= count($conn['stations']) > 1 ? 's' : '' ?>&nbsp;:
                  <?= htmlspecialchars(implode(', ', $conn['stations'])) ?>
                </span>
              <?php endif; ?>
            </span>
          </a>
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
        ?>
          <a href="<?= htmlspecialchars($conn['url']) ?>" class="line-card">
            <span class="line-card__pill" style="background:<?= htmlspecialchars($conn['color']) ?>;color:<?= htmlspecialchars($conn['color_text']) ?>;">
              <?= htmlspecialchars($conn['code']) ?>
            </span>
            <span class="line-card__content">
              <span class="line-card__name"><?= htmlspecialchars($conn['name']) ?></span>
              <?php if (!empty($conn['stations'])): ?>
                <span class="line-card__stations">
                  À <?= count($conn['stations']) ?> station<?= count($conn['stations']) > 1 ? 's' : '' ?>&nbsp;:
                  <?= htmlspecialchars(implode(', ', $conn['stations'])) ?>
                </span>
              <?php endif; ?>
            </span>
          </a>
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
        <?php foreach ($internalLinks['discover_metro_lines'] as $disc): ?>
          <a href="<?= htmlspecialchars($disc['url']) ?>" class="discover-pill <?= !empty($disc['is_current']) ? 'discover-pill--current' : '' ?>" <?= !empty($disc['is_current']) ? 'aria-current="page"' : '' ?>>
            <span class="discover-pill__pill" style="background:<?= htmlspecialchars($disc['color']) ?>;color:<?= htmlspecialchars($disc['color_text']) ?>;">
              <?= htmlspecialchars($disc['code']) ?>
            </span>
            <span class="discover-pill__name"><?= htmlspecialchars($disc['name']) ?></span>
          </a>
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
        <?php foreach ($internalLinks['related_pages'] as $page): ?>
          <a href="<?= htmlspecialchars($page['url']) ?>" class="related-card">
            <span class="related-card__icon" aria-hidden="true"><?= htmlspecialchars($page['icon']) ?></span>
            <span class="related-card__content">
              <span class="related-card__label"><?= htmlspecialchars($page['label']) ?></span>
              <span class="related-card__desc"><?= htmlspecialchars($page['description']) ?></span>
            </span>
            <span class="related-card__arrow" aria-hidden="true">→</span>
          </a>
        <?php endforeach; ?>
      </div>
    </div>
  <?php endif; ?>

</section>
