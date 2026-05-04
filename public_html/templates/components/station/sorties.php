<?php
/**
 * Composant : Sorties de la station (page station)
 *
 * Affiche la liste numérotée des sorties (accès) de la station, avec adresse
 * en surface et indicateur PMR. Données issues du GTFS officiel IDFM via
 * scripts/build-station-exits.php (clé "exits" du JSON station).
 *
 * Variables attendues :
 *   $exits       : array, liste des sorties.
 *                  Chaque entrée : { number, name, latitude, longitude, accessible }
 *                  - number : string ("1", "2", "1A"...)
 *                  - name : string (adresse / repère en surface)
 *                  - latitude/longitude : float
 *                  - accessible : true (PMR), false (non PMR), null (info indispo)
 *   $stationName : string, nom de la station (pour le titre / aria-labels)
 *
 * Affichage responsive :
 *   - Mobile (<640px)  : cartes empilées 1 col
 *   - Tablet (≥640px)  : grille 2 col
 *   - Desktop (≥1024px): grille 3 col
 *
 * Si $exits est vide, le composant n'affiche rien.
 *
 * @package BougeaParis\Templates\Components\Station
 * @since Livraison 6
 */

$exits       = $props['exits']       ?? null;
$stationName = $props['stationName'] ?? null;

if (empty($exits) || !is_array($exits)) {
    return;
}

$stationName = $stationName ?? 'cette station';
$count       = count($exits);
$pmrCount    = 0;
foreach ($exits as $e) {
    if (($e['accessible'] ?? null) === true) $pmrCount++;
}
?>

<section class="station-section section-sorties" id="sorties" aria-labelledby="sorties-title">

  <h2 id="sorties-title">Sorties de la station <?= e($stationName) ?></h2>

  <p class="section-intro">
    La <strong>station <?= e($stationName) ?></strong> compte
    <strong><?= (int)$count ?> sortie<?= $count > 1 ? 's' : '' ?> numérotée<?= $count > 1 ? 's' : '' ?></strong>
    permettant d'accéder à la surface.
    <?php if ($pmrCount > 0): ?>
      <?= (int)$pmrCount ?> sortie<?= $pmrCount > 1 ? 's sont accessibles' : ' est accessible' ?>
      aux personnes à mobilité réduite.
    <?php endif; ?>
    Repérez la sortie la plus proche de votre destination en surface pour gagner du temps.
  </p>

  <ul class="sorties-list" role="list" aria-label="Liste numérotée des sorties">
    <?php foreach ($exits as $exit):
      $number    = (string)($exit['number'] ?? '');
      $name      = (string)($exit['name'] ?? '');
      $accessible = $exit['accessible'] ?? null;
      $hasNumber = $number !== '';
    ?>
      <li class="sortie-item">
        <span class="sortie-number" aria-hidden="true">
          <?= $hasNumber ? e($number) : '·' ?>
        </span>
        <div class="sortie-content">
          <?php if ($hasNumber): ?>
            <span class="visually-hidden">Sortie <?= e($number) ?> : </span>
          <?php endif; ?>
          <span class="sortie-name"><?= e($name) ?></span>
          <?php if ($accessible === true): ?>
            <span class="badge-pmr" title="Sortie accessible aux personnes à mobilité réduite">
              <span aria-hidden="true">♿</span>
              <span class="visually-hidden">Accessible PMR</span>
              <span aria-hidden="true">PMR</span>
            </span>
          <?php endif; ?>
        </div>
      </li>
    <?php endforeach; ?>
  </ul>

  <p class="sorties-note">
    <small>
      Sources : IDFM (Île-de-France Mobilités), GTFS officiel.
      Les indications PMR ne sont pas toujours renseignées dans les données ouvertes ;
      en cas de doute, consultez l'application <em>RATP Bonjour</em> ou l'agent à l'accueil.
    </small>
  </p>

</section>
