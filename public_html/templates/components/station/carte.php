<?php
/**
 * Composant : Carte interactive (page station)
 *
 * Affiche un bouton "Afficher le plan interactif" qui, au clic, déclenche
 * le chargement lazy de Leaflet (CSS + JS) puis l'initialisation de la carte
 * avec tuiles OpenStreetMap, marqueur central station, marqueurs numérotés
 * pour les sorties, marqueurs catégorie pour les POIs.
 *
 * Lazy loading TOTAL : Leaflet n'est PAS chargé tant que l'utilisateur ne
 * clique pas. Préserve les Core Web Vitals (LCP, FID, CLS) sur la page
 * station qui charge déjà beaucoup de contenu (12 POIs avec images, 19
 * cartes sortie, etc.).
 *
 * Variables attendues :
 *   $station : array { lat: float, lon: float, name: string }
 *   $exits   : array exits[] avec latitude/longitude/number/name/address_full
 *   $pois    : array nearby_pois[] avec latitude/longitude/name/category/nearest_exit
 *
 * Si $station['lat'] ou $station['lon'] manquant, le composant ne s'affiche
 * pas (graceful degradation).
 *
 * @package BougeaParis\Templates\Components\Station
 * @since Livraison 9 (carte interactive)
 */

$station = $props['station'] ?? null;
$exits   = $props['exits']   ?? [];
$pois    = $props['pois']    ?? [];

if (!is_array($station)) return;
$stationLat  = $station['lat']  ?? null;
$stationLon  = $station['lon']  ?? null;
$stationName = $station['name'] ?? null;
if ($stationLat === null || $stationLon === null) return;

// Filtrage + projection des sorties (ne garder que celles avec coords)
$exitsForJs = [];
foreach ($exits as $e) {
    if (!isset($e['latitude'], $e['longitude'])) continue;
    $exitsForJs[] = [
        'number'  => (string)($e['number']       ?? ''),
        'name'    => (string)($e['name']         ?? ''),
        'address' => (string)($e['address_full'] ?? ''),
        'lat'     => (float)$e['latitude'],
        'lon'     => (float)$e['longitude'],
    ];
}

// Filtrage + projection des POIs
$poisForJs = [];
foreach ($pois as $p) {
    if (!empty($p['is_hidden'])) continue;
    if (!isset($p['latitude'], $p['longitude'])) continue;
    $ne = $p['nearest_exit'] ?? null;
    $poisForJs[] = [
        'name'         => (string)($p['name']     ?? ''),
        'category'     => (string)($p['category'] ?? ''),
        'lat'          => (float)$p['latitude'],
        'lon'          => (float)$p['longitude'],
        'nearest_exit' => is_array($ne) ? [
            'number'       => (string)($ne['number']       ?? ''),
            'walk_minutes' => (int)   ($ne['walk_minutes'] ?? 0),
        ] : null,
    ];
}

// JSON encode + escape pour data-attribute (XSS-safe)
$jsonOpts  = JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES;
$exitsJson = htmlspecialchars(json_encode($exitsForJs, $jsonOpts), ENT_QUOTES, 'UTF-8');
$poisJson  = htmlspecialchars(json_encode($poisForJs,  $jsonOpts), ENT_QUOTES, 'UTF-8');
$nbExits   = count($exitsForJs);
$nbPois    = count($poisForJs);

// Si pas de point à afficher (pas d'exits ni POIs), pas la peine d'afficher la carte
if ($nbExits === 0 && $nbPois === 0) return;
?>

<section class="station-section section-carte" id="plan" aria-labelledby="carte-title">

  <h2 id="carte-title">Plan de la station <?= e($stationName) ?></h2>

  <p class="section-intro">
    Visualisez d'un coup d'œil
    <?php if ($nbExits > 0): ?>
      les <strong><?= (int)$nbExits ?> sorties</strong>
    <?php endif; ?>
    <?php if ($nbExits > 0 && $nbPois > 0): ?>
      et
    <?php endif; ?>
    <?php if ($nbPois > 0): ?>
      les <strong><?= (int)$nbPois ?> monuments à proximité</strong>
    <?php endif; ?>
    de la station <strong><?= e($stationName) ?></strong>.
    Le plan est interactif : zoom, déplacement, et clic sur un marqueur pour
    afficher les détails.
  </p>

  <button class="carte-trigger" type="button"
          data-loaded="false"
          data-station-lat="<?= e((string)$stationLat) ?>"
          data-station-lon="<?= e((string)$stationLon) ?>"
          data-station-name="<?= e((string)$stationName) ?>"
          data-exits="<?= $exitsJson ?>"
          data-pois="<?= $poisJson ?>"
          aria-controls="carte-container"
          aria-expanded="false">
    <span aria-hidden="true">📍</span>
    Afficher le plan interactif
  </button>

  <div id="carte-container" class="carte-container" hidden></div>

</section>

<script src="/assets/js/carte-station.js" defer></script>
