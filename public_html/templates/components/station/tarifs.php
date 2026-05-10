<?php
/**
 * Composant : Tarifs et titres de transport (page station)
 *
 * Rend un résumé des principaux titres IDFM/RATP en vigueur,
 * lus depuis data/tarifs.json (source unique mutualisée).
 *
 * Le contenu est identique pour toutes les stations IDF, mais la
 * formulation H2/H3 inclut le nom de la station pour le SEO local
 * (« Tarifs métro à La Défense », etc.).
 *
 * Variables attendues (props) :
 * - stationName : string, nom de la station (pour les H2/H3)
 *
 * Si tarifs.json absent → composant n'affiche rien.
 */

$stationName = $props['stationName'] ?? null;
if (!$stationName) {
    return;
}

$tarifsFile = __DIR__ . '/../../../data/tarifs.json';
if (!file_exists($tarifsFile)) {
    return;
}
$tarifs = json_decode(file_get_contents($tarifsFile), true);
if (!is_array($tarifs)) {
    return;
}

$updated = $tarifs['_meta']['last_updated'] ?? null;
$srcUrl  = $tarifs['_meta']['source_url']  ?? null;

// Liste compacte des principaux titres affichés sur la page station
$mainTitles = [];
foreach (['ticket_unique', 'carnet', 'navigo_easy', 'navigo_decouverte', 'navigo_liberte_plus'] as $k) {
    if (!empty($tarifs[$k])) {
        $mainTitles[$k] = $tarifs[$k];
    }
}

if (empty($mainTitles)) {
    return;
}

$hubUrl    = '/tarifs/';
$hubActive = Routes::exists(rtrim($hubUrl, '/'));
?>

<section class="station-section section-tarifs" id="tarifs" aria-labelledby="tarifs-title">

  <h2 id="tarifs-title">Tarifs et titres de transport à <?= Template::e($stationName) ?></h2>

  <p class="section-intro">
    Les tarifs des transports en commun à <strong><?= Template::e($stationName) ?></strong> sont fixés par <strong>Île-de-France Mobilités</strong> et appliqués par la RATP et la SNCF. Voici les principaux titres en vigueur, valables sur le métro, le RER intra-Paris, le bus et le tramway.
  </p>

  <div class="tarifs-grid" role="list">
    <?php foreach ($mainTitles as $key => $t): ?>
      <article class="tarif-card" role="listitem">
        <div class="tarif-card__header">
          <span class="tarif-card__icon" aria-hidden="true"><?= Template::e($t['icon'] ?? '🎫') ?></span>
          <h3 class="tarif-card__name"><?= Template::e($t['name']) ?></h3>
        </div>
        <div class="tarif-card__price"><?= Template::e($t['price']) ?>
          <?php if (!empty($t['price_label'])): ?>
            <span class="tarif-card__price-label"><?= Template::e($t['price_label']) ?></span>
          <?php endif; ?>
        </div>
        <?php if (!empty($t['weekly_price']) || !empty($t['monthly_price'])): ?>
          <ul class="tarif-card__sub">
            <?php if (!empty($t['weekly_price'])): ?>
              <li><strong><?= Template::e($t['weekly_label'] ?? 'Hebdo') ?> :</strong> <?= Template::e($t['weekly_price']) ?></li>
            <?php endif; ?>
            <?php if (!empty($t['monthly_price'])): ?>
              <li><strong><?= Template::e($t['monthly_label'] ?? 'Mensuel') ?> :</strong> <?= Template::e($t['monthly_price']) ?></li>
            <?php endif; ?>
          </ul>
        <?php endif; ?>
        <p class="tarif-card__desc"><?= richText($t['description'] ?? '') ?></p>
        <?php if (!empty($t['best_for'])): ?>
          <p class="tarif-card__best"><strong>Idéal pour :</strong> <?= Template::e($t['best_for']) ?></p>
        <?php endif; ?>
      </article>
    <?php endforeach; ?>
  </div>

  <?php if (!empty($tarifs['free_categories'])): ?>
    <h3 class="tarifs-subtitle">Tarifs réduits et gratuités à <?= Template::e($stationName) ?></h3>
    <ul class="tarifs-reduits-list">
      <?php foreach ($tarifs['free_categories'] as $fc): ?>
        <li>
          <span class="tarifs-reduits-icon" aria-hidden="true"><?= Template::e($fc['icon'] ?? '🎟️') ?></span>
          <strong><?= Template::e($fc['category']) ?></strong> — <?= richText($fc['description'] ?? '') ?>
        </li>
      <?php endforeach; ?>
    </ul>
  <?php endif; ?>

  <p class="tarifs-meta">
    <?php if ($updated): ?>
      Tarifs en vigueur au <?= Template::e(dateFr($updated, 'long_with_day')) ?>.
    <?php endif; ?>
    Source : <?php if ($srcUrl): ?><a href="<?= Template::e($srcUrl) ?>" target="_blank" rel="noopener">Île-de-France Mobilités</a><?php else: ?>Île-de-France Mobilités<?php endif; ?>.
    <?php if ($hubActive): ?>
      <a href="<?= Template::e($hubUrl) ?>" class="tarifs-hub-link">Voir tous les titres et abonnements →</a>
    <?php else: ?>
      <span class="tarifs-hub-link tarifs-hub-link--inactive" data-future-url="<?= Template::e($hubUrl) ?>">Voir tous les titres et abonnements (bientôt)</span>
    <?php endif; ?>
  </p>

</section>
