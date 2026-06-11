<?php
/**
 * Hub /aeroports/ : dispatcher hub-transport + cards visuelles 3 aéroports.
 * Les cards sont rendues AVANT la section airport-grid classique pour
 * occuper le haut de page (entrée SEO touristique forte).
 */

// Charger les 3 JSON aéroports published=true (CDG, Orly, Beauvais)
$aeroportsDir = __DIR__ . '/../../data/aeroports';
$aeroports = [];
foreach (glob($aeroportsDir . '/*.json') ?: [] as $f) {
    $data = json_decode((string)file_get_contents($f), true);
    if (is_array($data) && !empty($data['published'])) {
        $aeroports[] = $data;
    }
}
// Ordre : CDG (vitrine), Orly, Beauvais
$order = ['paris-charles-de-gaulle' => 1, 'paris-orly' => 2, 'paris-beauvais-tille' => 3];
usort($aeroports, fn($a, $b) => ($order[$a['slug']] ?? 99) <=> ($order[$b['slug']] ?? 99));
?>

<?php if (!empty($aeroports)): ?>
<section class="aeroports-grid-section container">
  <h2>Nos guides des 3 aéroports parisiens</h2>
  <p class="aeroports-grid-intro">
    Découvrez les guides complets d'accès aux trois aéroports desservant Paris et l'Île-de-France.
  </p>

  <div class="aeroports-grid">
    <?php foreach ($aeroports as $aero):
      $aSlug   = $aero['slug'] ?? '';
      $aName   = $aero['name'] ?? '';
      $aIata   = $aero['iata'] ?? '';
      $aCity   = $aero['city'] ?? '';
      $aTraf   = $aero['annual_traffic'] ?? '';
      $aRank   = $aero['rank_europe'] ?? '';
      $aHero   = $aero['hero_image'] ?? [];
      $aImgSrc = $aHero['local_versions']['jpg'][1200] ?? ($aHero['url'] ?? '');
      $aAlt    = $aHero['alt'] ?? ('Aéroport ' . $aName);
      $modes   = $aero['access_modes'] ?? [];
      $modeNames = array_slice(array_column($modes, 'name'), 0, 4);
    ?>
      <a href="/aeroports/<?= Template::e($aSlug) ?>/" class="aeroport-card">
        <div class="aeroport-card__image">
          <?php if ($aImgSrc): ?>
            <img src="<?= Template::e($aImgSrc) ?>"
                 alt="<?= Template::e($aAlt) ?>"
                 loading="lazy" width="600" height="338">
          <?php endif; ?>
          <?php if ($aIata): ?>
            <span class="aeroport-card__iata"><?= Template::e($aIata) ?></span>
          <?php endif; ?>
        </div>

        <div class="aeroport-card__content">
          <h3 class="aeroport-card__title"><?= Template::e($aName) ?></h3>

          <?php if ($aCity): ?>
            <p class="aeroport-card__location">📍 <?= Template::e($aCity) ?></p>
          <?php endif; ?>

          <?php if ($aTraf): ?>
            <p class="aeroport-card__traffic">
              <strong><?= Template::e($aTraf) ?> passagers/an</strong>
              <?php if (is_int($aRank)): ?>
                · <?= (int)$aRank ?>e en Europe
              <?php endif; ?>
            </p>
          <?php endif; ?>

          <?php if (!empty($modeNames)): ?>
            <p class="aeroport-card__modes"><?= Template::e(implode(' · ', $modeNames)) ?></p>
          <?php endif; ?>

          <span class="aeroport-card__cta">Voir le guide complet →</span>
        </div>
      </a>
    <?php endforeach; ?>
  </div>
</section>

<style>
.aeroports-grid-section { margin: 2.5rem auto; }
.aeroports-grid-section h2 { color: #0F6E56; margin-bottom: .75rem; }
.aeroports-grid-intro { font-size: 1.05rem; color: #555; margin: 0 0 1.5rem; max-width: 720px; line-height: 1.6; }
.aeroports-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}
.aeroport-card {
  display: block; background: #fff;
  border: 2px solid #E1F5EE; border-radius: 12px; overflow: hidden;
  text-decoration: none; color: inherit;
  transition: transform .3s ease, border-color .3s ease, box-shadow .3s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,.05);
}
.aeroport-card:hover {
  border-color: #0F6E56;
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(15,110,86,.15);
}
.aeroport-card__image { position: relative; width: 100%; aspect-ratio: 16/9; overflow: hidden; background: #f4f8f6; }
.aeroport-card__image img { width: 100%; height: 100%; object-fit: cover; display: block; }
.aeroport-card__iata {
  position: absolute; top: 12px; right: 12px;
  background: rgba(15,110,86,.95); color: #fff;
  padding: .4rem .75rem; border-radius: 6px;
  font-weight: 700; font-size: .95rem; letter-spacing: .5px;
}
.aeroport-card__content { padding: 1.25rem 1.5rem 1.5rem; }
.aeroport-card__title { margin: 0 0 .5rem; color: #0F6E56; font-size: 1.25rem; line-height: 1.3; }
.aeroport-card__location { margin: 0 0 .75rem; font-size: .95rem; color: #555; }
.aeroport-card__traffic { margin: 0 0 .75rem; font-size: .95rem; color: #333; }
.aeroport-card__traffic strong { color: #0F6E56; }
.aeroport-card__modes { margin: 0 0 1rem; font-size: .85rem; color: #777; line-height: 1.5; }
.aeroport-card__cta { display: inline-block; color: #0F6E56; font-weight: 600; font-size: .95rem; transition: transform .2s; }
.aeroport-card:hover .aeroport-card__cta { transform: translateX(4px); }
@media (max-width: 768px) {
  .aeroports-grid { grid-template-columns: 1fr; gap: 1rem; }
  .aeroport-card__content { padding: 1rem 1.25rem 1.25rem; }
  .aeroport-card__title { font-size: 1.15rem; }
}
</style>
<?php endif; ?>

<?php
$cocon_slug     = 'aeroports';
$cocon_label    = 'Aeroports';
$grid_component = 'airport-grid';
$data_key       = 'aeroports';

$tpl->partial('pages/hub-transport', [
    'cocon'          => $cocon,
    'lines'          => $lines,
    'cocon_slug'     => $cocon_slug,
    'cocon_label'    => $cocon_label,
    'grid_component' => $grid_component,
    'data_key'       => $data_key,
]);
