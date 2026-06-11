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

// Descriptions riches par aéroport (mutualisation : source unique pour les cards)
$descriptions = [
    'paris-charles-de-gaulle' => [
        'h2'   => 'Aéroport Paris-Charles de Gaulle (CDG)',
        'desc' => 'Le <strong>plus grand aéroport parisien</strong>, situé à <strong>Roissy-en-France (95)</strong> à 25 km au nord-est de Paris. <strong>2e en Europe</strong> avec ~67 millions de passagers/an. <strong>Hub principal d\'Air France</strong> et de nombreuses compagnies internationales. Accessible depuis Paris en <strong>RER B (35 min, 11,80 €)</strong>, <strong>Roissybus (60 min, 16,60 €)</strong> ou taxi.',
        'cta'  => 'Voir le guide complet de CDG',
    ],
    'paris-orly' => [
        'h2'   => 'Aéroport Paris-Orly (ORY)',
        'desc' => '<strong>2e aéroport parisien</strong>, situé dans le <strong>Val-de-Marne (94)</strong> à 14 km au sud de Paris. <strong>~33 millions de passagers/an</strong>. Hub majeur des compagnies low-cost et des vols européens. Accessible depuis Paris par le <strong>métro 14 depuis juin 2024 (25 min, 2,15 €)</strong>, l\'<strong>Orlybus (35 min, 11,50 €)</strong>, le tramway T7 ou taxi.',
        'cta'  => 'Voir le guide complet d\'Orly',
    ],
    'paris-beauvais-tille' => [
        'h2'   => 'Aéroport Paris-Beauvais (BVA)',
        'desc' => 'Aéroport low-cost situé à <strong>85 km au nord de Paris (Oise 60)</strong>. <strong>~5,7 millions de passagers/an</strong>. Principalement desservi par <strong>Ryanair</strong> et <strong>Wizz Air</strong>. Accès depuis Paris par <strong>navette officielle depuis Porte Maillot (75 min, 17 €)</strong> ou train + bus.',
        'cta'  => 'Voir le guide complet de Beauvais',
    ],
];

// SEO
$tpl->seo
    ->setTitle(bp_title_aeroports_hub(), false)
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
        <?php
          $aDescr = $descriptions[$aSlug] ?? null;
          $aUrl   = '/aeroports/' . $aSlug . '/';
        ?>
        <article class="aeroport-card">
          <a href="<?= Template::e($aUrl) ?>" class="aeroport-card__image" aria-label="Guide <?= Template::e($aName) ?>">
            <?php if ($aImgSrc): ?>
              <img src="<?= Template::e($aImgSrc) ?>" alt="<?= Template::e($aAlt) ?>" loading="lazy" width="600" height="338">
            <?php endif; ?>
            <?php if ($aIata): ?>
              <span class="aeroport-card__iata"><?= Template::e($aIata) ?></span>
            <?php endif; ?>
          </a>
          <div class="aeroport-card__content">
            <h2 class="aeroport-card__title">
              <a href="<?= Template::e($aUrl) ?>"><?= Template::e($aDescr['h2'] ?? $aName) ?></a>
            </h2>
            <?php if ($aCity): ?>
              <p class="aeroport-card__location">📍 <?= Template::e($aCity) ?></p>
            <?php endif; ?>
            <?php if ($aTraf): ?>
              <p class="aeroport-card__stats">
                <strong><?= Template::e($aTraf) ?> passagers/an</strong>
                <?php if (is_int($aRank)): ?> · <?= (int)$aRank ?>e en Europe<?php endif; ?>
              </p>
            <?php endif; ?>
            <?php if (!empty($modeNames)): ?>
              <p class="aeroport-card__modes"><?= Template::e(implode(' · ', $modeNames)) ?></p>
            <?php endif; ?>
            <?php if (!empty($aDescr['desc'])): ?>
              <p class="aeroport-card__description"><?= $aDescr['desc'] ?></p>
            <?php endif; ?>
            <a href="<?= Template::e($aUrl) ?>" class="aeroport-card__cta">
              <?= Template::e($aDescr['cta'] ?? ('Voir le guide ' . $aName)) ?> →
            </a>
          </div>
        </article>
      <?php endforeach; ?>
    </div>
  </section>
  <?php endif; ?>

  <?php $tpl->partial('ads/slot-in-article'); ?>

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

  <section class="aeroports-choix-section">
    <h2>Quel aéroport choisir selon votre destination ?</h2>
    <p class="aeroports-choix-intro">
      Le choix de votre aéroport dépend de votre destination, du type de vol et de votre budget. Voici nos recommandations selon votre profil de voyageur.
    </p>

    <div class="choix-grid">

      <a href="/aeroports/paris-charles-de-gaulle/" class="choix-card choix-card--longcourrier">
        <div class="choix-card__icon">
          <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <circle cx="24" cy="24" r="20"/>
            <line x1="4" y1="24" x2="44" y2="24"/>
            <path d="M24 4 Q14 14 24 24 Q34 34 24 44"/>
            <path d="M24 4 Q34 14 24 24 Q14 34 24 44"/>
          </svg>
        </div>
        <h3 class="choix-card__title">Vols long-courriers et internationaux</h3>
        <div class="choix-card__aeroport">Paris-CDG</div>
        <p class="choix-card__description">
          <strong>Hub d'Air France</strong> avec plus de <strong>300 destinations</strong> et la majorité des compagnies internationales (Delta, KLM, Lufthansa, Emirates, Cathay Pacific, ANA…). Idéal pour l'Amérique, l'Asie et l'Afrique.
        </p>
        <span class="choix-card__cta">Voir le guide CDG →</span>
      </a>

      <a href="/aeroports/paris-orly/" class="choix-card choix-card--europe">
        <div class="choix-card__icon">
          <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <circle cx="14" cy="20" r="5"/>
            <circle cx="34" cy="20" r="5"/>
            <circle cx="24" cy="36" r="5"/>
            <line x1="19" y1="20" x2="29" y2="20"/>
            <line x1="16" y1="24" x2="22" y2="33"/>
            <line x1="32" y1="24" x2="26" y2="33"/>
          </svg>
        </div>
        <h3 class="choix-card__title">Vols européens et compagnies traditionnelles</h3>
        <div class="choix-card__aeroport">Paris-Orly</div>
        <p class="choix-card__description">
          <strong>Europe et bassin méditerranéen</strong>. Hub de Transavia, easyJet, French Bee et compagnies régulières (Vueling, Iberia, Air Corsica). Accès rapide depuis Paris via le <strong>métro 14 en 25 min</strong>.
        </p>
        <span class="choix-card__cta">Voir le guide Orly →</span>
      </a>

      <a href="/aeroports/paris-beauvais-tille/" class="choix-card choix-card--lowcost">
        <div class="choix-card__icon">
          <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M4 28 L42 18 L26 32 L20 24 Z"/>
            <line x1="20" y1="24" x2="14" y2="34"/>
            <line x1="4" y1="40" x2="44" y2="40"/>
          </svg>
        </div>
        <h3 class="choix-card__title">Vols low-cost Ryanair et Wizz Air</h3>
        <div class="choix-card__aeroport">Paris-Beauvais</div>
        <p class="choix-card__description">
          <strong>Compagnies low-cost européennes</strong> (Ryanair, Wizz Air, Volotea). Distance plus importante (85 km au nord) mais billets souvent très compétitifs. <strong>Navette officielle Porte Maillot</strong> recommandée.
        </p>
        <span class="choix-card__cta">Voir le guide Beauvais →</span>
      </a>

    </div>
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
  <script type="application/ld+json">
  <?php
  $_hubFaq = [
    ["Combien y a-t-il d'aéroports à Paris ?", "Paris compte 3 aéroports principaux : Paris-Charles de Gaulle (CDG), Paris-Orly (ORY) et Paris-Beauvais-Tillé (BVA)."],
    ["Quel est le plus grand aéroport parisien ?", "Paris-Charles de Gaulle (CDG) est le plus grand, avec environ 67 millions de passagers/an. C'est le 2e aéroport européen après Londres-Heathrow."],
    ["Quel aéroport pour Ryanair ?", "Ryanair opère principalement depuis Paris-Beauvais-Tillé (BVA), situé à 85 km au nord de Paris. Quelques vols depuis Paris-Charles de Gaulle."],
    ["Quel aéroport est le plus proche du centre de Paris ?", "Paris-Orly est l'aéroport le plus proche du centre, à environ 14 km au sud. Accessible en 25 minutes en métro 14 (depuis juin 2024)."],
  ];
  $_main = [];
  foreach ($_hubFaq as [$q, $a]) {
    $_main[] = ['@type' => 'Question', 'name' => $q, 'acceptedAnswer' => ['@type' => 'Answer', 'text' => $a]];
  }
  echo json_encode([
    '@context' => 'https://schema.org',
    '@type'    => 'FAQPage',
    'mainEntity' => $_main,
  ], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT);
  ?>
  </script>

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
  display: flex; flex-direction: column;
  background: #fff;
  border: 2px solid #E1F5EE; border-radius: 12px; overflow: hidden;
  transition: transform .3s ease, border-color .3s ease, box-shadow .3s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,.05);
}
.aeroport-card:hover {
  border-color: #0F6E56;
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(15,110,86,.12);
}
.aeroport-card__image { display: block; position: relative; width: 100%; aspect-ratio: 16/9; overflow: hidden; background: #f4f8f6; }
.aeroport-card__image img { width: 100%; height: 100%; object-fit: cover; display: block; }
.aeroport-card__iata {
  position: absolute; top: 12px; right: 12px;
  background: rgba(15,110,86,.95); color: #fff;
  padding: .4rem .75rem; border-radius: 6px;
  font-weight: 700; font-size: .95rem; letter-spacing: .5px;
}
.aeroport-card__content { padding: 1.25rem 1.5rem 1.5rem; display: flex; flex-direction: column; flex: 1; }
.aeroport-card__title { margin: 0 0 .5rem; font-size: 1.2rem; line-height: 1.3; font-weight: 700; }
.aeroport-card__title a { color: #0F6E56; text-decoration: none; }
.aeroport-card__title a:hover { text-decoration: underline; }
.aeroport-card__location { margin: 0 0 .5rem; font-size: .95rem; color: #555; }
.aeroport-card__stats { margin: .25rem 0; font-size: .95rem; color: #333; }
.aeroport-card__stats strong { color: #0F6E56; }
.aeroport-card__modes { margin: .25rem 0 .75rem; font-size: .9rem; color: #777; letter-spacing: .3px; }
.aeroport-card__description { margin: .75rem 0; line-height: 1.55; font-size: .95rem; color: #333; flex: 1; }
.aeroport-card__description strong { color: #0F6E56; }
.aeroport-card__cta {
  display: inline-block; align-self: flex-start;
  margin-top: 1rem;
  padding: .6rem 1.25rem;
  background: #fff;
  color: #0F6E56;
  border: 2px solid #0F6E56;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  font-size: .95rem;
  transition: background .2s, color .2s, transform .2s;
}
.aeroport-card__cta:hover {
  background: #0F6E56; color: #fff;
  transform: translateX(2px);
}

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

/* Section "Quel aéroport choisir ?" — 3 cards visuelles décisionnelles */
.aeroports-choix-section { margin: 3rem 0; }
.aeroports-choix-intro { font-size: 1rem; color: #555; margin-bottom: 1.5rem; max-width: 720px; line-height: 1.6; }
.choix-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.25rem;
  margin: 2rem 0;
}
.choix-card {
  display: flex; flex-direction: column;
  background: #fff;
  border: 2px solid #E1F5EE;
  border-radius: 12px;
  padding: 1.5rem;
  text-decoration: none;
  color: inherit;
  transition: transform .3s ease, border-color .3s ease, box-shadow .3s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,.05);
}
.choix-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(15,110,86,.15);
}
.choix-card--longcourrier { border-color: #0F6E56; }
.choix-card--longcourrier:hover { border-color: #085041; }
.choix-card--europe { border-color: #2980B9; }
.choix-card--europe:hover { border-color: #1f618d; }
.choix-card--lowcost { border-color: #E67E22; }
.choix-card--lowcost:hover { border-color: #ba6519; }
.choix-card__icon { width: 56px; height: 56px; margin-bottom: 1rem; }
.choix-card__icon svg { width: 100%; height: 100%; display: block; }
.choix-card--longcourrier .choix-card__icon { color: #0F6E56; }
.choix-card--europe .choix-card__icon       { color: #2980B9; }
.choix-card--lowcost .choix-card__icon      { color: #E67E22; }
.choix-card__title {
  margin: 0 0 .5rem;
  font-size: 1.05rem;
  color: #1a1a1a;
  font-weight: 600;
  line-height: 1.3;
}
.choix-card__aeroport {
  display: inline-block; align-self: flex-start;
  margin-bottom: 1rem;
  padding: .35rem .85rem;
  font-weight: 700; font-size: 1.05rem;
  border-radius: 6px;
}
.choix-card--longcourrier .choix-card__aeroport { background: #E1F5EE; color: #0F6E56; }
.choix-card--europe .choix-card__aeroport       { background: #D6EAF8; color: #2980B9; }
.choix-card--lowcost .choix-card__aeroport      { background: #FDEAA7; color: #E67E22; }
.choix-card__description {
  margin: .5rem 0 1rem;
  font-size: .93rem;
  line-height: 1.55;
  color: #444;
  flex-grow: 1;
}
.choix-card__description strong { color: #1a1a1a; }
.choix-card__cta {
  display: inline-block;
  margin-top: auto;
  font-weight: 600;
  font-size: .95rem;
  padding-top: .5rem;
  border-top: 1px solid #E1F5EE;
  transition: transform .2s;
}
.choix-card--longcourrier .choix-card__cta { color: #0F6E56; }
.choix-card--europe .choix-card__cta       { color: #2980B9; }
.choix-card--lowcost .choix-card__cta      { color: #E67E22; }
.choix-card:hover .choix-card__cta { transform: translateX(4px); }
@media (max-width: 768px) {
  .choix-grid { grid-template-columns: 1fr; gap: 1rem; }
  .choix-card { padding: 1.25rem; }
  .choix-card__icon { width: 48px; height: 48px; }
}
</style>
