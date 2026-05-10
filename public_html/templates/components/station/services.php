<?php
/**
 * Composant : Services et infos pratiques (page station)
 *
 * Affiche un résumé des services disponibles à la station :
 * WiFi, toilettes, distributeurs, consigne, espace voyageurs,
 * commerces. Lit le champ JSON `services` de la station.
 *
 * Variables attendues (props) :
 * - services    : array (clés : wifi, toilets, atm, consigne_bagages,
 *                  espace_voyageurs, commerces)
 * - stationName : string
 *
 * Si $services vide → le composant ne rend rien.
 */

$services    = $props['services']    ?? null;
$stationName = $props['stationName'] ?? null;

if (empty($services) || !is_array($services) || !$stationName) {
    return;
}

// Format des items : chaque clé prédéfinie a un libellé + icône.
$items = [
    'wifi'             => ['label' => 'WiFi gratuit',           'icon' => '📶'],
    'toilets'          => ['label' => 'Toilettes publiques',     'icon' => '🚻'],
    'atm'              => ['label' => 'Distributeurs',           'icon' => '💳'],
    'consigne_bagages' => ['label' => 'Consigne à bagages',      'icon' => '🧳'],
    'espace_voyageurs' => ['label' => 'Espace voyageurs RATP',   'icon' => 'ℹ️'],
    'commerces'        => ['label' => 'Commerces et restauration', 'icon' => '🛍️'],
];

$visibleCount = 0;
foreach ($items as $k => $cfg) {
    if (isset($services[$k]) && $services[$k] !== null && $services[$k] !== '') {
        $visibleCount++;
    }
}
if ($visibleCount === 0) {
    return;
}
?>

<section class="station-section section-services" id="services" aria-labelledby="services-title">

  <h2 id="services-title">Services et infos pratiques à <?= Template::e($stationName) ?></h2>

  <p class="section-intro">
    Voici les services disponibles à la station <strong><?= Template::e($stationName) ?></strong>. Les équipements peuvent évoluer ; consultez l'application <a href="https://www.bonjour-ratp.fr/" target="_blank" rel="noopener">Bonjour RATP</a> pour l'information la plus à jour avant votre voyage.
  </p>

  <ul class="services-list">
    <?php foreach ($items as $key => $cfg):
      $val = $services[$key] ?? null;
      if ($val === null || $val === '') continue;

      // Format affichage selon le type
      if ($val === true) {
          $display = 'Disponible';
          $statusClass = 'service-item--yes';
      } elseif ($val === false) {
          $display = 'Non disponible';
          $statusClass = 'service-item--no';
      } else {
          $display = (string)$val; // chaîne descriptive (ex: "Cœur Transport, niveau RER")
          $statusClass = 'service-item--detail';
      }
    ?>
      <li class="service-item <?= Template::e($statusClass) ?>">
        <span class="service-item__icon" aria-hidden="true"><?= Template::e($cfg['icon']) ?></span>
        <div class="service-item__content">
          <strong class="service-item__label"><?= Template::e($cfg['label']) ?></strong>
          <span class="service-item__detail"><?= richText($display) ?></span>
        </div>
      </li>
    <?php endforeach; ?>
  </ul>

</section>
