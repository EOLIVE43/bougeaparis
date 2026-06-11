<?php
/**
 * Hub /aeroports/ — structure Hn refondue (spec user 2026-06-11).
 *
 * Plan :
 *   H1 : "Les aéroports de Paris : guide d'accès"
 *   DIV "Les 3 aéroports parisiens" (pas H2) + 3 cards visuelles
 *   H2 × 3 (CDG / Orly / Beauvais) avec description + lien guide
 *   H2 "Comparatif rapide des 3 aéroports" + table
 *   H2 "Quel aéroport choisir selon votre destination ?" + 3 H3
 *   H2 "Questions fréquentes sur les aéroports de Paris" + 4 H3
 *   H2 "Explorer les autres transports parisiens" + nav
 *
 * Ne délègue plus à hub-transport.php pour contrôler totalement la Hn structure.
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
$order = ['paris-charles-de-gaulle' => 1, 'paris-orly' => 2, 'paris-beauvais-tille' => 3];
usort($aeroports, fn($a, $b) => ($order[$a['slug']] ?? 99) <=> ($order[$b['slug']] ?? 99));

// SEO
$tpl->seo
    ->setTitle($cocon['seo']['title'] ?? 'Aéroports de Paris : guide d\'accès — CDG, Orly, Beauvais')
    ->setDescription($cocon['seo']['description'] ?? 'Les 3 aéroports parisiens : guides complets d\'accès Paris-CDG, Paris-Orly et Paris-Beauvais. Modes de transport, tarifs, durées, terminaux 2026.')
    ->setCanonical('/aeroports/')
    ->setBreadcrumb([
        ['label' => 'Accueil', 'url' => '/'],
        ['label' => 'Aéroports', 'url' => '/aeroports/'],
    ]);
?>

<?php $tpl->partial('components/breadcrumb', ['items' => [
    ['label' => 'Accueil', 'url' => '/'],
    ['label' => 'Aéroports', 'url' => '/aeroports/'],
]]); ?>

<div class="container">
<article class="hub-aeroports">

  <header class="hub-hero">
    <h1>Les aéroports de Paris : guide d'accès</h1>
    <p class="hub-intro">
      Trois aéroports desservent Paris et l'Île-de-France : <strong>Paris-Charles de Gaulle (CDG)</strong>, <strong>Paris-Orly (ORY)</strong> et <strong>Paris-Beauvais-Tillé (BVA)</strong>. Découvrez les guides complets d'accès, modes de transport, tarifs et terminaux pour chaque aéroport parisien.
    </p>
  </header>

  <?php $tpl->partial('ads/slot-header'); ?>

  <?php if (!empty($aeroports)): ?>
  <section class="aeroports-presentation">
    <div class="aeroports-intro-label">Les 3 aéroports parisiens</div>

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
        <a href="/aeroports/<?= Template::e($aSlug) ?>/" class="aeroport-card" aria-label="Guide complet <?= Template::e($aName) ?>">
          <div class="aeroport-card__image">
            <?php if ($aImgSrc): ?>
              <img src="<?= Template::e($aImgSrc) ?>" alt="<?= Template::e($aAlt) ?>" loading="lazy" width="600" height="338">
            <?php endif; ?>
            <?php if ($aIata): ?>
              <span class="aeroport-card__iata"><?= Template::e($aIata) ?></span>
            <?php endif; ?>
          </div>
          <div class="aeroport-card__content">
            <div class="aeroport-card__title"><?= Template::e($aName) ?></div>
            <?php if ($aCity): ?>
              <p class="aeroport-card__location">📍 <?= Template::e($aCity) ?></p>
            <?php endif; ?>
            <?php if ($aTraf): ?>
              <p class="aeroport-card__traffic">
                <strong><?= Template::e($aTraf) ?> passagers/an</strong>
                <?php if (is_int($aRank)): ?> · <?= (int)$aRank ?>e en Europe<?php endif; ?>
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
  <?php endif; ?>

  <section class="aeroport-detail">
    <h2>Aéroport Paris-Charles de Gaulle (CDG)</h2>
    <p>
      Le <strong>plus grand aéroport parisien</strong>, situé à <strong>Roissy-en-France (95)</strong> à 25 km au nord-est de Paris. <strong>2e en Europe</strong> avec <strong>~67 millions de passagers/an</strong>. <strong>Hub principal d'Air France</strong> et de nombreuses compagnies internationales. Accessible depuis Paris en <strong>RER B (35 min, 11,80 €)</strong>, <strong>Roissybus (60 min, 16,60 €)</strong> ou taxi.
    </p>
    <p><a href="/aeroports/paris-charles-de-gaulle/" class="aeroport-link">Voir le guide complet de CDG →</a></p>
  </section>

  <?php $tpl->partial('ads/slot-in-article'); ?>

  <section class="aeroport-detail">
    <h2>Aéroport Paris-Orly (ORY)</h2>
    <p>
      <strong>2e aéroport parisien</strong>, situé dans le <strong>Val-de-Marne (94)</strong> à 14 km au sud de Paris. <strong>~33 millions de passagers/an</strong>. Hub majeur des compagnies low-cost et des vols européens. Accessible depuis Paris par le <strong>métro 14 depuis juin 2024 (25 min, 2,15 €)</strong>, l'<strong>Orlybus (35 min, 11,50 €)</strong>, le tramway T7 ou taxi.
    </p>
    <p><a href="/aeroports/paris-orly/" class="aeroport-link">Voir le guide complet d'Orly →</a></p>
  </section>

  <section class="aeroport-detail">
    <h2>Aéroport Paris-Beauvais (BVA)</h2>
    <p>
      Aéroport low-cost situé à <strong>85 km au nord de Paris (Oise 60)</strong>. <strong>~5,7 millions de passagers/an</strong>. Principalement desservi par <strong>Ryanair</strong> et <strong>Wizz Air</strong>. Accès depuis Paris par <strong>navette officielle depuis Porte Maillot (75 min, 17 €)</strong> ou train + bus.
    </p>
    <p><a href="/aeroports/paris-beauvais-tille/" class="aeroport-link">Voir le guide complet de Beauvais →</a></p>
  </section>

  <section class="aeroport-comparatif">
    <h2>Comparatif rapide des 3 aéroports</h2>
    <div class="aeroport-table-wrap">
      <table class="aeroports-comparatif">
        <thead>
          <tr>
            <th>Aéroport</th>
            <th>Code IATA</th>
            <th>Distance Paris</th>
            <th>Passagers/an</th>
            <th>Mode principal</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Paris-Charles de Gaulle</strong></td>
            <td>CDG</td>
            <td>~25 km nord-est</td>
            <td>~67 M</td>
            <td>RER B (35 min)</td>
          </tr>
          <tr>
            <td><strong>Paris-Orly</strong></td>
            <td>ORY</td>
            <td>~14 km sud</td>
            <td>~33 M</td>
            <td>Métro 14 (25 min)</td>
          </tr>
          <tr>
            <td><strong>Paris-Beauvais</strong></td>
            <td>BVA</td>
            <td>~85 km nord</td>
            <td>~5,7 M</td>
            <td>Navette (75 min)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="aeroport-guide-choisir">
    <h2>Quel aéroport choisir selon votre destination ?</h2>

    <h3>Vols long-courriers et internationaux : Paris-CDG</h3>
    <p>
      Si vous voyagez en <strong>long-courrier</strong> (Amérique, Asie, Afrique), l'aéroport <strong>Paris-Charles de Gaulle</strong> est votre choix principal. Hub d'Air France avec plus de <strong>300 destinations</strong> et la majorité des compagnies internationales (Delta, KLM, Lufthansa, Emirates, Cathay Pacific, ANA…).
    </p>

    <h3>Vols européens et compagnies traditionnelles : Paris-Orly</h3>
    <p>
      <strong>Paris-Orly</strong> dessert principalement l'<strong>Europe et le bassin méditerranéen</strong>. Hub de <strong>Transavia, easyJet</strong>, French Bee et de compagnies régulières (Vueling, Iberia, Air Corsica). Accès rapide depuis Paris via le <strong>métro 14 en 25 min</strong>.
    </p>

    <h3>Vols low-cost Ryanair et Wizz Air : Paris-Beauvais</h3>
    <p>
      <strong>Paris-Beauvais-Tillé</strong> est l'aéroport principal des compagnies <strong>low-cost européennes</strong> (Ryanair, Wizz Air, Volotea). Distance plus importante (85 km) mais billets souvent très compétitifs. Réserver la navette officielle Porte Maillot recommandée.
    </p>
  </section>

  <section class="aeroport-faq">
    <h2>Questions fréquentes sur les aéroports de Paris</h2>

    <h3>Combien y a-t-il d'aéroports à Paris ?</h3>
    <p>
      Paris compte <strong>3 aéroports principaux</strong> : <strong>Paris-Charles de Gaulle (CDG)</strong>, <strong>Paris-Orly (ORY)</strong> et <strong>Paris-Beauvais-Tillé (BVA)</strong>.
    </p>

    <h3>Quel est le plus grand aéroport parisien ?</h3>
    <p>
      <strong>Paris-Charles de Gaulle (CDG)</strong> est le plus grand, avec environ <strong>67 millions de passagers/an</strong>. C'est le <strong>2e aéroport européen</strong> après Londres-Heathrow.
    </p>

    <h3>Quel aéroport pour Ryanair ?</h3>
    <p>
      <strong>Ryanair</strong> opère principalement depuis <strong>Paris-Beauvais-Tillé (BVA)</strong>, situé à 85 km au nord de Paris. Quelques vols depuis Paris-Charles de Gaulle.
    </p>

    <h3>Quel aéroport est le plus proche du centre de Paris ?</h3>
    <p>
      <strong>Paris-Orly</strong> est l'aéroport le plus proche du centre, à environ <strong>14 km au sud</strong>. Accessible en <strong>25 minutes en métro 14</strong> (depuis juin 2024).
    </p>
  </section>

  <?php $tpl->partial('ads/slot-footer'); ?>

  <section class="related-transports">
    <h2>Explorer les autres transports parisiens</h2>
    <nav class="related-nav" aria-label="Autres transports">
      <?php
      $others = [
          'metro'      => 'Métro',
          'rer'        => 'RER',
          'bus'        => 'Bus',
          'tramway'    => 'Tramway',
          'transilien' => 'Transilien',
      ];
      foreach ($others as $slug => $label): ?>
        <a href="/<?= $slug ?>/" class="related-nav__item">
          <span class="related-nav__label"><?= htmlspecialchars($label) ?></span>
        </a>
      <?php endforeach; ?>
    </nav>
  </section>

</article>
</div>

<style>
.hub-aeroports { padding: 1.5rem 0; }
.hub-aeroports h2 { color: #0F6E56; margin-top: 2.5rem; font-size: clamp(1.3rem, 2.5vw, 1.7rem); }
.hub-aeroports h3 { color: #0F6E56; margin-top: 1.5rem; font-size: 1.1rem; }
.hub-aeroports p { line-height: 1.65; }
.hub-hero { margin: 1rem 0 2rem; }
.hub-hero h1 { color: #0F6E56; margin: 0 0 .75rem; font-size: clamp(1.6rem, 4vw, 2.2rem); line-height: 1.25; }
.hub-intro { font-size: 1.05rem; color: #333; max-width: 760px; margin: 0; line-height: 1.6; }

.aeroports-intro-label {
  font-size: .95rem;
  font-weight: 700;
  color: #0F6E56;
  margin: 1.5rem 0 1rem;
  text-transform: uppercase;
  letter-spacing: .5px;
}

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
.aeroport-card__title { margin: 0 0 .5rem; color: #0F6E56; font-size: 1.25rem; line-height: 1.3; font-weight: 700; }
.aeroport-card__location { margin: 0 0 .75rem; font-size: .95rem; color: #555; }
.aeroport-card__traffic { margin: 0 0 .75rem; font-size: .95rem; color: #333; }
.aeroport-card__traffic strong { color: #0F6E56; }
.aeroport-card__modes { margin: 0 0 1rem; font-size: .85rem; color: #777; line-height: 1.5; }
.aeroport-card__cta { display: inline-block; color: #0F6E56; font-weight: 600; font-size: .95rem; transition: transform .2s; }
.aeroport-card:hover .aeroport-card__cta { transform: translateX(4px); }

.aeroport-detail { margin: 2rem 0; }
.aeroport-link {
  display: inline-block;
  color: #0F6E56;
  font-weight: 600;
  text-decoration: none;
  padding: .5rem 1rem;
  border: 1px solid #0F6E56;
  border-radius: 8px;
  transition: background .2s, color .2s;
}
.aeroport-link:hover { background: #0F6E56; color: #fff; }

.aeroport-table-wrap { overflow-x: auto; margin-top: 1rem; }
.aeroports-comparatif { width: 100%; border-collapse: collapse; }
.aeroports-comparatif th, .aeroports-comparatif td { padding: .7rem .9rem; border-bottom: 1px solid #ddd; text-align: left; }
.aeroports-comparatif th { background: #f4f8f6; color: #0F6E56; font-weight: 600; }

.related-nav {
  display: flex; flex-wrap: wrap; gap: .75rem;
  margin-top: 1rem;
}
.related-nav__item {
  background: #f4f8f6;
  border: 1px solid #E1F5EE;
  padding: .6rem 1.1rem;
  border-radius: 8px;
  text-decoration: none;
  color: #0F6E56;
  font-weight: 600;
}
.related-nav__item:hover { background: #0F6E56; color: #fff; }

@media (max-width: 768px) {
  .aeroports-grid { grid-template-columns: 1fr; gap: 1rem; }
  .aeroport-card__content { padding: 1rem 1.25rem 1.25rem; }
  .aeroport-card__title { font-size: 1.15rem; }
}
</style>
