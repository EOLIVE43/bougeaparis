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
$tariffZoneContext = $props['tariffZoneContext'] ?? null;
$commune     = $props['commune'] ?? null;
$modesList   = $props['modesList'] ?? null; // ex: "Ligne 1, RER A et E, tramway T2 et Transilien L et U"
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

$stationE = htmlspecialchars($stationName, ENT_QUOTES, 'UTF-8');
$communeE = $commune ? htmlspecialchars($commune, ENT_QUOTES, 'UTF-8') : null;
$modesE   = $modesList ? htmlspecialchars($modesList, ENT_QUOTES, 'UTF-8') : null;

// Composition de l'intro personnalisée par station :
// 1) Zone + commune + modes desservis
// 2) Recommandation contextuelle selon zone (1 = Paris centre, >1 = banlieue)
// 3) Mention IDFM/RATP/SNCF
$introParts = [];
if ($tariffZone) {
    $ctxStr = $tariffZoneContext ? ' (' . htmlspecialchars($tariffZoneContext, ENT_QUOTES, 'UTF-8') . ')' : (
        !empty($zones[(string)$tariffZone]) ? ' (' . htmlspecialchars($zones[(string)$tariffZone], ENT_QUOTES, 'UTF-8') . ')' : ''
    );
    $loc = "Située en <strong>zone tarifaire {$tariffZone}</strong>{$ctxStr}";
    if ($communeE) $loc .= " — {$communeE}";
    $loc .= ", la station {$stationE}";
    if ($modesE) {
        $loc .= " est desservie par {$modesE}.";
    } else {
        $loc .= ".";
    }
    $introParts[] = $loc;

    if ($tariffZone === 1) {
        $introParts[] = "Tous les titres de transport classiques (Ticket t+, Carnet de 10, Navigo Easy, Navigo Découverte) sont valables pour entrer ou sortir à {$stationE} sans supplément. Le tarif unique francilien de 2,15 € s'applique quelle que soit la distance parcourue dans le réseau.";
    } else {
        $introParts[] = "Pour les déplacements vers le centre de Paris (zone 1), le tarif unique francilien de 2,15 € pour le ticket t+ et le forfait Navigo Découverte (toutes zones 1-5 au même prix) restent les options les plus économiques. Le carnet de 10 tickets t+ offre une réduction de 19 % pour les voyages occasionnels depuis {$stationE}.";
    }
} else {
    // Fallback générique si zone inconnue
    $intro_loc = "La station {$stationE}";
    if ($modesE) $intro_loc .= " est desservie par {$modesE}";
    $intro_loc .= ".";
    $introParts[] = $intro_loc;
}
$introParts[] = "Les tarifs sont fixés par <strong>Île-de-France Mobilités</strong> et appliqués par la RATP, la SNCF et les opérateurs Transilien. Voici les principaux titres en vigueur, valables sur le métro, le RER intra-Paris, le bus et le tramway.";

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

  <?php foreach ($introParts as $i => $part): ?>
    <p<?= $i === 0 ? ' class="section-intro"' : '' ?>><?= $part ?></p>
  <?php endforeach; ?>

  <h3 class="tarifs-subtitle">Tickets à l'unité ou en carnet à <?= Template::e($stationName) ?></h3>
  <div class="tarifs-grid">
    <?php foreach ($tickets as $key => $t) $renderCard($key, $t); ?>
  </div>

  <?php if (!empty($passes)): ?>
    <h3 class="tarifs-subtitle">Forfaits et abonnements Navigo à <?= Template::e($stationName) ?></h3>
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
