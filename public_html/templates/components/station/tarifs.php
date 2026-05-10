<?php
/**
 * Composant : Tarifs et titres de transport (page station)
 *
 * Source unique de vérité : data/global/transit-pricing.json,
 * lu via le helper transit_pricing(). Tous les prix au format
 * FR via format_price().
 *
 * Personnalisation par station via :
 * - $stationName : nom court (intro et H2/H3)
 * - $tariffZone  : zone tarifaire IDFM (1-5), pour adapter
 *                   l'introduction et la recommandation pratique
 *
 * Variables attendues (props) :
 * - stationName : string
 * - tariffZone  : int|null (zone IDFM, défaut 1 si non spécifié
 *                  et station Paris)
 *
 * Si transit_pricing() vide → composant n'affiche rien.
 */

$stationName = $props['stationName'] ?? null;
$tariffZone  = isset($props['tariffZone']) ? (int) $props['tariffZone'] : null;
if (!$stationName) {
    return;
}

$pricing = function_exists('transit_pricing') ? transit_pricing() : [];
if (empty($pricing) || empty($pricing['tickets'])) {
    return;
}

$meta    = $pricing['_meta']  ?? [];
$tickets = $pricing['tickets'] ?? [];
$passes  = $pricing['passes']  ?? [];
$free    = $pricing['free_categories'] ?? [];
$zones   = $pricing['zones']   ?? [];

$updated  = $meta['valid_from'] ?? null;
$srcUrl   = $meta['source_url'] ?? null;
$validTo  = $meta['valid_to']   ?? null;
$expired  = $validTo && (date('Y-m-d') > $validTo);

$hubUrl    = '/tarifs/';
$hubActive = Routes::exists(rtrim($hubUrl, '/'));

// Recommandation contextuelle selon zone
$zoneIntro = '';
if ($tariffZone) {
    $zoneLabel = $zones[(string)$tariffZone] ?? null;
    if ($tariffZone === 1) {
        $zoneIntro = sprintf(
            ' La station %s est située en <strong>zone tarifaire %d</strong> (Paris intra-muros). Les tickets t+ et carnets sont valables sans supplément pour vos trajets.',
            htmlspecialchars($stationName, ENT_QUOTES, 'UTF-8'),
            $tariffZone
        );
    } else {
        $zoneIntro = sprintf(
            ' La station %s est située en <strong>zone tarifaire %d</strong>%s. Pour les trajets vers le centre de Paris (zone 1) ou au-delà, le forfait Navigo Découverte au tarif unique 1-5 est souvent plus économique qu\'un cumul de tickets t+.',
            htmlspecialchars($stationName, ENT_QUOTES, 'UTF-8'),
            $tariffZone,
            $zoneLabel ? ' (' . htmlspecialchars($zoneLabel, ENT_QUOTES, 'UTF-8') . ')' : ''
        );
    }
}

/**
 * Render commun d'une carte tarif (ticket ou pass).
 * Le format diffère légèrement entre tickets (price_eur) et passes
 * (card_price_eur + weekly/monthly), donc render unifié.
 */
$renderCard = function (string $key, array $t) {
    $name        = $t['name'] ?? $key;
    $icon        = $t['icon'] ?? '🎫';
    $primaryEur  = $t['price_eur']      ?? $t['card_price_eur']      ?? null;
    $primaryLab  = $t['type']           ?? null;
    $weeklyEur   = $t['weekly_price_eur']  ?? null;
    $monthlyEur  = $t['monthly_price_eur'] ?? null;
    $perTripEur  = $t['price_per_trip_eur'] ?? null;
    $idealFor    = $t['ideal_for']      ?? null;
    $validFor    = $t['valid_for']      ?? null;
    $transfers   = $t['transfers_note'] ?? null;
    $discount    = $t['discount_vs_unit_pct'] ?? null;
    ?>
    <article class="tarif-card">
      <div class="tarif-card__header">
        <span class="tarif-card__icon" aria-hidden="true"><?= htmlspecialchars($icon, ENT_QUOTES, 'UTF-8') ?></span>
        <h3 class="tarif-card__name"><?= htmlspecialchars($name, ENT_QUOTES, 'UTF-8') ?></h3>
      </div>
      <?php if ($primaryEur !== null): ?>
        <div class="tarif-card__price">
          <?= htmlspecialchars(format_price((float)$primaryEur), ENT_QUOTES, 'UTF-8') ?>
          <?php if ($primaryLab): ?>
            <span class="tarif-card__price-label"><?= htmlspecialchars($primaryLab, ENT_QUOTES, 'UTF-8') ?></span>
          <?php endif; ?>
        </div>
      <?php endif; ?>
      <?php if ($weeklyEur !== null || $monthlyEur !== null || $perTripEur !== null): ?>
        <ul class="tarif-card__sub">
          <?php if ($weeklyEur !== null): ?>
            <li><strong>Forfait hebdomadaire :</strong> <?= htmlspecialchars(format_price((float)$weeklyEur), ENT_QUOTES, 'UTF-8') ?></li>
          <?php endif; ?>
          <?php if ($monthlyEur !== null): ?>
            <li><strong>Forfait mensuel :</strong> <?= htmlspecialchars(format_price((float)$monthlyEur), ENT_QUOTES, 'UTF-8') ?></li>
          <?php endif; ?>
          <?php if ($perTripEur !== null): ?>
            <li><strong>Coût par trajet :</strong> <?= htmlspecialchars(format_price((float)$perTripEur), ENT_QUOTES, 'UTF-8') ?></li>
          <?php endif; ?>
        </ul>
      <?php endif; ?>
      <?php if ($validFor): ?>
        <p class="tarif-card__desc"><strong>Valable :</strong> <?= htmlspecialchars($validFor, ENT_QUOTES, 'UTF-8') ?>.</p>
      <?php endif; ?>
      <?php if ($transfers): ?>
        <p class="tarif-card__desc"><?= htmlspecialchars($transfers, ENT_QUOTES, 'UTF-8') ?>.</p>
      <?php endif; ?>
      <?php if ($discount !== null): ?>
        <p class="tarif-card__desc"><strong>Économie : −<?= (int)$discount ?> %</strong> vs ticket à l'unité.</p>
      <?php endif; ?>
      <?php if ($idealFor): ?>
        <p class="tarif-card__best"><strong>Idéal pour :</strong> <?= htmlspecialchars($idealFor, ENT_QUOTES, 'UTF-8') ?>.</p>
      <?php endif; ?>
    </article>
    <?php
};
?>

<section class="station-section section-tarifs" id="tarifs" aria-labelledby="tarifs-title">

  <h2 id="tarifs-title">Tarifs et titres de transport à <?= Template::e($stationName) ?></h2>

  <p class="section-intro">
    Les tarifs des transports en commun à <strong><?= Template::e($stationName) ?></strong> sont fixés par <strong>Île-de-France Mobilités</strong> et appliqués par la RATP et la SNCF. Voici les principaux titres en vigueur, valables sur le métro, le RER intra-Paris, le bus et le tramway.<?= $zoneIntro ?>
  </p>

  <h3 class="tarifs-subtitle">Tickets à l'unité ou en carnet à <?= Template::e($stationName) ?></h3>
  <div class="tarifs-grid">
    <?php foreach ($tickets as $key => $t) $renderCard($key, $t); ?>
  </div>

  <?php if (!empty($passes)): ?>
    <h3 class="tarifs-subtitle">Forfaits et abonnements Navigo</h3>
    <div class="tarifs-grid">
      <?php foreach ($passes as $key => $t) $renderCard($key, $t); ?>
    </div>
  <?php endif; ?>

  <?php if (!empty($free)): ?>
    <h3 class="tarifs-subtitle">Tarifs réduits et gratuités à <?= Template::e($stationName) ?></h3>
    <ul class="tarifs-reduits-list">
      <?php foreach ($free as $fc): ?>
        <li>
          <span class="tarifs-reduits-icon" aria-hidden="true"><?= Template::e($fc['icon'] ?? '🎟️') ?></span>
          <strong><?= Template::e($fc['category']) ?></strong> — <?= richText($fc['description'] ?? '') ?>
        </li>
      <?php endforeach; ?>
    </ul>
  <?php endif; ?>

  <p class="tarifs-meta">
    <?php if ($updated): ?>
      Tarifs en vigueur depuis le <?= Template::e(dateFr($updated, 'long_with_day')) ?><?= $validTo ? ', valables jusqu\'au ' . Template::e(dateFr($validTo, 'long_with_day')) : '' ?>.
    <?php endif; ?>
    Source : <?php if ($srcUrl): ?><a href="<?= Template::e($srcUrl) ?>" target="_blank" rel="noopener">Île-de-France Mobilités</a><?php else: ?>Île-de-France Mobilités<?php endif; ?>.
    <?php if ($expired): ?>
      <strong style="color:#8a570f;">⚠️ Mise à jour annuelle requise (les tarifs en cours de validité ont peut-être expiré, à recouper IDFM).</strong>
    <?php endif; ?>
    <?php if ($hubActive): ?>
      <a href="<?= Template::e($hubUrl) ?>" class="tarifs-hub-link">Voir tous les titres et abonnements →</a>
    <?php else: ?>
      <span class="tarifs-hub-link tarifs-hub-link--inactive" data-future-url="<?= Template::e($hubUrl) ?>">Voir tous les titres et abonnements (bientôt)</span>
    <?php endif; ?>
  </p>

</section>
