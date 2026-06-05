<?php
/**
 * Composant : Sorties de la station (page station)
 *
 * Affiche la liste numérotée des sorties (accès) de la station avec adresse
 * postale et indicateur PMR. Si la station a une structure officielle par
 * secteurs (signalétique RATP, ex. Châtelet : Forum / Rivoli / Seine), affiche
 * 3 blocs distincts ; sinon, liste plate. Les éventuelles sorties non assignées
 * à un secteur sont regroupées sous "Autres sorties".
 *
 * Données issues du GTFS officiel IDFM + reverse geocoding api-adresse.data.gouv.fr
 * (script scripts/build-station-exits.php).
 *
 * Variables attendues :
 *   $exits       : array, liste des sorties.
 *                  Chaque entrée : { number, name, address_full?, postcode?, city?,
 *                                    latitude, longitude, accessible, sector? }
 *                  - number       : string ("1", "2", "1A"...)
 *                  - name         : string (libellé court IDFM)
 *                  - address_full : string optionnel, adresse postale (reverse geocode)
 *                  - postcode     : string optionnel ("75001")
 *                  - city         : string optionnel ("Paris")
 *                  - accessible   : true (PMR), false (non PMR), null (info indispo)
 *                  - sector       : string optionnel, clé pointant vers $exitSectors
 *   $exitSectors : array|null, dictionnaire des secteurs.
 *                  Format : { sector_key => { title, exits_range?, description? } }
 *                  Si null ou vide → affichage en liste plate.
 *   $stationName : string, nom de la station.
 *
 * Affichage responsive :
 *   - Mobile (<640px)   : 1 col
 *   - Tablet (≥640px)   : 2 col
 *   - Desktop (≥1024px) : 3 col
 *
 * Si $exits est vide, le composant n'affiche rien.
 *
 * @package BougeaParis\Templates\Components\Station
 * @since Livraison 6 (sorties.php) ; sectorisation : Livraison 7
 */

$exits       = $props['exits']        ?? null;
$exitSectors = $props['exitSectors']  ?? null;
$stationName = $props['stationName']  ?? null;

if (empty($exits) || !is_array($exits)) {
    return;
}

$stationName = $stationName ?? 'cette station';
$count       = count($exits);
$pmrCount    = 0;
foreach ($exits as $e) {
    if (($e['accessible'] ?? null) === true) $pmrCount++;
}

// ---------------------------------------------------------------------------
// Groupage par secteur. _other = sorties sans secteur (ou avec un secteur
// inconnu de exit_sectors). En mode "secteurs", on rend les blocs dans l'ordre
// de exit_sectors puis on appendre _other en "Autres sorties" si non vide.
// ---------------------------------------------------------------------------
$useSectors = is_array($exitSectors) && !empty($exitSectors);
$bySector   = ['_other' => []];
$hasNamedSector = false;

foreach ($exits as $exit) {
    $s = $exit['sector'] ?? null;
    if ($useSectors && $s !== null && $s !== '' && isset($exitSectors[$s])) {
        if (!isset($bySector[$s])) $bySector[$s] = [];
        $bySector[$s][] = $exit;
        $hasNamedSector = true;
    } else {
        $bySector['_other'][] = $exit;
    }
}

$displayInSectors = $useSectors && $hasNamedSector;

// ---------------------------------------------------------------------------
// Rendu d'un item (carte de sortie). Closure pour reuse dans le mode
// "sectorisé" et le mode "plat".
// ---------------------------------------------------------------------------
$renderItem = function (array $exit): void {
    $number      = (string)($exit['number']       ?? '');
    $name        = (string)($exit['name']         ?? '');
    $addressFull = (string)($exit['address_full'] ?? '');
    $accessible  = $exit['accessible'] ?? null;
    $hasNumber   = $number !== '';
    $hasAddress  = $addressFull !== '' && $addressFull !== $name;
    ?>
    <li class="sortie-item">
      <span class="sortie-number" aria-hidden="true">
        <?= $hasNumber ? e($number) : '·' ?>
      </span>
      <div class="sortie-content">
        <div class="sortie-content__main">
          <?php if ($hasNumber): ?>
            <span class="visually-hidden">Sortie <?= e($number) ?> : </span>
          <?php endif; ?>
          <span class="sortie-name"><?= e(expandIdfmAbbreviations($name)) ?></span>
          <?php if ($accessible === true): ?>
            <span class="badge-pmr" title="Sortie accessible aux personnes à mobilité réduite">
              <span aria-hidden="true">♿</span>
              <span class="visually-hidden">Accessible PMR</span>
              <span aria-hidden="true">PMR</span>
            </span>
          <?php endif; ?>
        </div>
        <?php if ($hasAddress): ?>
          <span class="sortie-address" aria-label="Adresse postale">
            <?= e(expandIdfmAbbreviations($addressFull)) ?>
          </span>
        <?php endif; ?>
      </div>
    </li>
    <?php
};
?>

<section class="station-section section-sorties" id="sorties" aria-labelledby="sorties-title">

  <h2 id="sorties-title"><?= e($props['sectionTitle'] ?? ('Sorties de la station ' . $stationName)) ?></h2>

  <p class="section-intro">
    La <strong>station <?= e($stationName) ?></strong> compte
    <strong><?= (int)$count ?> sortie<?= $count > 1 ? 's' : '' ?> numérotée<?= $count > 1 ? 's' : '' ?></strong>
    permettant d'accéder à la surface.
    <?php if ($pmrCount > 0): ?>
      <?= (int)$pmrCount ?> sortie<?= $pmrCount > 1 ? 's sont accessibles' : ' est accessible' ?>
      aux personnes à mobilité réduite.
    <?php endif; ?>
    <?php if ($displayInSectors): ?>
      Elles sont organisées par la RATP en <strong><?= count(array_filter($bySector, fn($v) => !empty($v) && $v !== $bySector['_other'])) ?> secteurs</strong> distincts pour faciliter votre orientation en station.
    <?php else: ?>
      Repérez la sortie la plus proche de votre destination en surface pour gagner du temps.
    <?php endif; ?>
  </p>

  <?php if ($displayInSectors): ?>
    <?php foreach ($exitSectors as $key => $sector):
      if (empty($bySector[$key])) continue;
      $items     = $bySector[$key];
      $title     = (string)($sector['title']        ?? ucfirst($key));
      $range     = (string)($sector['exits_range']  ?? '');
      $desc      = (string)($sector['description']  ?? '');
      $sectionId = 'sortie-secteur-' . preg_replace('/[^a-z0-9]+/i', '-', strtolower($key));
    ?>
      <div class="sorties-sector" aria-labelledby="<?= e($sectionId) ?>">
        <h3 class="sorties-sector__title" id="<?= e($sectionId) ?>">
          Sorties <?= e($stationName) ?> — <?= e($title) ?>
          <?php if ($range !== ''): ?>
            <span class="sorties-sector__range"><?= e($range) ?></span>
          <?php endif; ?>
        </h3>
        <?php if ($desc !== ''): ?>
          <p class="sorties-sector__desc"><?= e($desc) ?></p>
        <?php endif; ?>
        <ul class="sorties-list" role="list">
          <?php foreach ($items as $item) $renderItem($item); ?>
        </ul>
      </div>
    <?php endforeach; ?>

    <?php if (!empty($bySector['_other'])): ?>
      <div class="sorties-sector sorties-sector--other" aria-labelledby="sortie-secteur-other">
        <h3 class="sorties-sector__title" id="sortie-secteur-other">Sorties <?= e($stationName) ?> — Autres accès</h3>
        <ul class="sorties-list" role="list">
          <?php foreach ($bySector['_other'] as $item) $renderItem($item); ?>
        </ul>
      </div>
    <?php endif; ?>

  <?php else: ?>
    <ul class="sorties-list" role="list" aria-label="Liste numérotée des sorties">
      <?php foreach ($exits as $exit) $renderItem($exit); ?>
    </ul>
  <?php endif; ?>

  <?php
  // NOTE : crédit sources retiré ici, désormais centralisé sur la page
  // dédiée /sources/ (et lien "Sources et données" dans le footer global).
  // Évite la répétition entre composants pour des sources qui sont les
  // mêmes pour toutes les pages station/ligne.
  ?>

</section>
