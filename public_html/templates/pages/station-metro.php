<?php
/**
 * Template page station métro — station-metro.php
 *
 * Variables fournies par le router :
 * - $station : array, données chargées depuis data/stations/{slug}.json
 *
 * Variables fournies par Template (extract automatique) :
 * - $tpl     : Template instance (pour SEO + addStylesheet)
 * - $seo     : Seo instance
 * - $site    : config site
 * - $nav     : config navigation
 *
 * Sections :
 *  1. Hero (nom, badges lignes, photo, tagline, description)
 *  2. AdSense slot — header
 *  3. Correspondances (métro + RER)
 *  4. Introduction SEO
 *  5. AdSense slot — in-articlec
 *  6. Stations adjacentes (par ligne)
 *  7. Histoire de la station
 *  8. FAQ (avec schema.org)
 *  9. Conseils pratiques
 * 10. AdSense slot — footer
 *
 * @package BougeaParis\Templates\Pages
 * @since Livraison 5
 */

if (!isset($station) || !is_array($station)) {
    http_response_code(500);
    echo "Erreur : données de station manquantes.";
    return;
}

// =====================================================================
// SETUP : SEO + CSS
// =====================================================================

$slug      = $station['slug']      ?? 'unknown';
$name      = $station['name']      ?? 'Station';
$nameFull  = $station['name_full'] ?? $name;
$arr       = $station['arrondissement'] ?? '';
$address   = $station['address']   ?? '';
$lines     = $station['lines']     ?? [];
$rer       = $station['rer_correspondences'] ?? [];
$tram      = $station['tram_correspondences'] ?? [];
$transilien = $station['transilien_correspondences'] ?? [];
$bus       = $station['bus_correspondences'] ?? [];
$hero      = $station['hero']      ?? [];
$adjacent  = $station['adjacent_stations'] ?? [];
$image     = $station['image']     ?? null;
$intros    = $station['intro_paragraphs'] ?? [];
$faq       = $station['faq']       ?? [];
$tips      = $station['practical_tips'] ?? [];
$history   = $station['history']   ?? [];

// Hero image : nouveau format (hero_image avec url/alt/width/height) ou
// fallback sur l'ancien champ image. Si rien : placeholder gradient.
$heroImage = $station['hero_image'] ?? null;
if (!is_array($heroImage) || empty($heroImage['url'])) {
    if (!empty($image['src'])) {
        $heroImage = [
            'url'    => $image['src'],
            'alt'    => $image['alt'] ?? $name,
            'width'  => 1200,
            'height' => 675,
        ];
    } else {
        $heroImage = null;
    }
}
$hasImage  = $heroImage !== null;
$canonical = '/metro/station/' . $slug . '/';

// Charger le CSS dédié
$tpl->addStylesheet('/assets/css/station.css');

// SEO de base
$lineCount = count($lines);
$rerCodes = !empty($rer) ? ' + RER ' . implode(' ', array_column($rer, 'code')) : '';
$arrLabel = $arr ? ' (Paris ' . $arr . ')' : '';

// Meta description et keywords : patterns adaptatifs au mode dominant
// (metro pur / mixte / RER pur / tram pur). Voir helpers.php.
// Le helper construit la chaine deterministe a partir du nom, des codes
// lignes, de l'arrondissement et des top 3 nearby_pois. Independant du
// champ seo.description du JSON (qui reste la "lead" editoriale du hero).
$metaDesc = buildStationMetaDescription($station);
$metaKw   = buildStationMetaKeywords($station);

// Title SEO calibré sur les volumes Keyword Planner ("{nom} métro" domine).
// Voir buildStationTitle() dans core/helpers.php. Second parametre false :
// desactive le suffixe ' - BougeaParis.fr' (15 car) sur les pages station
// pour preserver la place des mots-cles SEO sous la limite 60 car SERP.
$tpl->seo
    ->setTitle(buildStationTitle($station), false)
    ->setDescription($metaDesc)
    ->setKeywords($metaKw)
    ->setCanonical($canonical);

// Hero image : og:image (partages sociaux + Discover) + preload LCP
// Si on a des local_versions, on prend l'AVIF 1200 pour og:image (taille optimale
// pour les overlays sociaux) et on preload les variantes AVIF avec imagesrcset.
$localVersions = $heroImage['local_versions'] ?? null;
if ($hasImage && !empty($heroImage['url'])) {
    $ogImg = !empty($localVersions['avif'][1200])
        ? $localVersions['avif'][1200]
        : $heroImage['url'];
    $tpl->seo->setOgImage($ogImg);
    if ($localVersions && !empty($localVersions['avif'])) {
        // Preload imagesrcset (3 tailles AVIF : 400, 800, 1200 — le 1600 est
        // pour les ecrans 4K, on l'omet du preload pour eviter d'overshoot).
        $tpl->seo->addPreloadImageSet(
            [
                400  => $localVersions['avif'][400],
                800  => $localVersions['avif'][800],
                1200 => $localVersions['avif'][1200],
            ],
            'image/avif',
            '(max-width: 768px) 100vw, 1200px'
        );
    } else {
        $tpl->seo->addPreloadImage($heroImage['url']);
    }
}

// =====================================================================
// SCHEMA.ORG : @graph unifie (BreadcrumbList + SubwayStation + FAQPage)
// =====================================================================
//
// On construit un seul bloc JSON-LD avec @graph plutot que 3 schemas
// separes : permet le cross-referencement par @id et limite les blocs
// dupliques pour les crawlers (Google, Bing, et lecteurs schemas locaux).
//
// On bypass deliberement Seo::setBreadcrumb() (qui addSchema separement)
// pour fusionner BreadcrumbList dans le @graph.

$siteUrl       = rtrim(Config::get('site.url'), '/');
$canonicalAbs  = $siteUrl . $canonical;
$breadcrumbItems = [
    ['label' => 'Accueil',     'url' => '/'],
    ['label' => 'Se déplacer', 'url' => '/se-deplacer/'],
    ['label' => 'Métro',       'url' => '/metro/'],
    ['label' => $name,         'url' => $canonical],
];

// 1. BreadcrumbList
$breadcrumbList = [];
foreach ($breadcrumbItems as $i => $crumb) {
    $breadcrumbList[] = [
        '@type'    => 'ListItem',
        'position' => $i + 1,
        'name'     => $crumb['label'],
        'item'     => $siteUrl . $crumb['url'],
    ];
}

// 2. SubwayStation (enrichi : description, lignes desservies, accessibilite,
//    contexte geographique). Schema.org n'a pas de propriete subwayLine
//    standard, on l'utilise comme extension : Google et autres parseurs
//    acceptent les proprietes inconnues sans rejeter le schema.
$subwayLines = [];
foreach ($lines as $line) {
    // L'URL publique d'une ligne est /metro/ligne-{code}/ (pas /metro/{slug}/
    // qui est le file-slug type "metro-1"). On derive depuis $line['code']
    // pour rester insensible au slug stocke dans chatelet.json.
    $lineCode    = (string)($line['code'] ?? '');
    $lineUrlSlug = 'ligne-' . strtolower($lineCode);
    $lineUrl     = '/metro/' . $lineUrlSlug . '/';
    $entry = [
        '@type'       => 'Service',
        'name'        => 'Ligne ' . $lineCode,
        'serviceType' => 'Métro Paris',
        'provider'    => [
            '@type' => 'Organization',
            'name'  => 'RATP',
        ],
    ];
    if (Routes::exists(rtrim($lineUrl, '/'))) {
        $entry['url'] = $siteUrl . $lineUrl;
    }
    $subwayLines[] = $entry;
}

$stationNode = [
    '@type'              => 'SubwayStation',
    '@id'                => $canonicalAbs . '#station',
    'name'               => $name,
    'description'        => $hero['description'] ?? null,
    'url'                => $canonicalAbs,
    'address'            => [
        '@type'           => 'PostalAddress',
        'streetAddress'   => $address ?: null,
        'addressLocality' => 'Paris',
        'addressRegion'   => 'Île-de-France',
        'addressCountry'  => 'FR',
    ],
    'geo' => [
        '@type'     => 'GeoCoordinates',
        'latitude'  => $station['latitude']  ?? null,
        'longitude' => $station['longitude'] ?? null,
    ],
    'image'              => ($hasImage && !empty($heroImage['url']))
        ? (str_starts_with($heroImage['url'], 'http') ? $heroImage['url'] : $siteUrl . $heroImage['url'])
        : null,
    'isAccessibleForFree'=> true,
    'publicAccess'       => true,
    'openingHoursSpecification' => SchemaHelpers::ratpMetroOpeningHours(),
    'amenityFeature' => array_merge(
        SchemaHelpers::stationAccessibilityFeatures($station),
        SchemaHelpers::stationServiceFeatures($station)
    ),
    'containedInPlace'   => [
        '@type' => 'City',
        'name'  => 'Paris',
        'address' => [
            '@type'           => 'PostalAddress',
            'addressLocality' => 'Paris',
            'addressRegion'   => 'Île-de-France',
            'addressCountry'  => 'FR',
        ],
    ],
    'subwayLine'         => $subwayLines,
];

// 3. FAQPage (si la station a une FAQ)
$faqNode = null;
if (!empty($faq)) {
    $faqEntities = [];
    foreach ($faq as $item) {
        $faqEntities[] = [
            '@type'          => 'Question',
            'name'           => $item['question'],
            'acceptedAnswer' => [
                '@type' => 'Answer',
                'text'  => $item['answer'],
            ],
        ];
    }
    $faqNode = [
        '@type'      => 'FAQPage',
        '@id'        => $canonicalAbs . '#faq',
        'mainEntity' => $faqEntities,
    ];
}

// 4. ItemList des POIs voisins (top 5 audités T0, si présents)
$nearbyPoisNode = SchemaHelpers::stationNearbyPoisAsItemList($station, $canonicalAbs);

// 5. ItemList des itinéraires populaires (url conditionnelle Routes::exists)
$itinerariesNode = SchemaHelpers::stationPopularItinerariesAsItemList($station, $canonicalAbs);

// Assemblage @graph
$graphNodes = [
    [
        '@type'           => 'BreadcrumbList',
        '@id'             => $canonicalAbs . '#breadcrumb',
        'itemListElement' => $breadcrumbList,
    ],
    $stationNode,
];
if ($nearbyPoisNode !== null) {
    $graphNodes[] = $nearbyPoisNode;
}
if ($itinerariesNode !== null) {
    $graphNodes[] = $itinerariesNode;
}
if ($faqNode !== null) {
    $graphNodes[] = $faqNode;
}

$tpl->seo->addSchema([
    '@context' => 'https://schema.org',
    '@graph'   => $graphNodes,
]);
?>

<?php
// Breadcrumb visible en haut de page
$tpl->partial('components/breadcrumb', [
    'items' => [
        ['label' => 'Accueil',  'url' => '/'],
        ['label' => 'Métro',    'url' => '/metro/'],
        ['label' => 'Stations', 'url' => '/metro/'],
        ['label' => 'Station ' . $name],
    ],
]);
?>

<div class="container">
<article class="station-page">

  <!-- ============================================================
       1. HERO
       ============================================================ -->
  <section class="station-hero <?= $hasImage ? 'station-hero--with-image' : 'station-hero--placeholder' ?>"
           aria-labelledby="station-hero-title">

    <?php if ($hasImage): ?>
      <div class="station-hero__image">
        <?php
        $altText = $heroImage['alt'] ?? $name;
        $imgWidth = (int)($heroImage['width']  ?? 1600);
        $imgHeight = (int)($heroImage['height'] ?? 900);
        $sizes = '(max-width: 768px) 100vw, 1200px';

        // Si on a des local_versions (AVIF/WebP/JPG), on utilise <picture> pour
        // que le navigateur choisisse le format optimal. Sinon, simple <img>.
        $hasPicture = is_array($localVersions ?? null)
            && !empty($localVersions['avif'])
            && !empty($localVersions['webp'])
            && !empty($localVersions['jpg']);

        $buildSrcset = function (array $widthMap): string {
            $parts = [];
            foreach ($widthMap as $w => $url) {
                $parts[] = htmlspecialchars($url, ENT_QUOTES, 'UTF-8') . ' ' . (int)$w . 'w';
            }
            return implode(', ', $parts);
        };
        ?>
        <?php if ($hasPicture): ?>
          <picture>
            <source type="image/avif"
                    srcset="<?= $buildSrcset($localVersions['avif']) ?>"
                    sizes="<?= e($sizes) ?>">
            <source type="image/webp"
                    srcset="<?= $buildSrcset($localVersions['webp']) ?>"
                    sizes="<?= e($sizes) ?>">
            <img src="<?= Template::e($localVersions['jpg'][1200] ?? reset($localVersions['jpg'])) ?>"
                 srcset="<?= $buildSrcset($localVersions['jpg']) ?>"
                 sizes="<?= e($sizes) ?>"
                 alt="<?= Template::e($altText) ?>"
                 width="<?= $imgWidth ?>" height="<?= $imgHeight ?>"
                 loading="eager" fetchpriority="high">
          </picture>
        <?php else: ?>
          <img src="<?= Template::e($heroImage['url']) ?>"
               alt="<?= Template::e($altText) ?>"
               width="<?= $imgWidth ?>" height="<?= $imgHeight ?>"
               loading="eager" fetchpriority="high"
               referrerpolicy="no-referrer">
        <?php endif; ?>
      </div>
    <?php endif; ?>

    <div class="station-hero__content">
      <h1 id="station-hero-title">
        <?= Template::e(buildStationH1($station)) ?>
      </h1>

      <div class="station-hero__badges" aria-label="Lignes desservant la station">
        <?php foreach ($lines as $line):
          $lineUrl    = '/metro/' . $line['slug'] . '/';
          $lineExists = Routes::exists(rtrim($lineUrl, '/'));
          // Label affiché : "M1", "M4", "M14"… (prepend "M" sur le code numérique)
          $pillLabel  = 'M' . $line['code'];
          $pillShape  = linePillShape($pillLabel);
          $pillSlug   = strtolower($pillLabel);
        ?>
          <?php if ($lineExists): ?>
            <a href="<?= Template::e($lineUrl) ?>"
               class="line-pill line-pill--<?= Template::e($pillShape) ?> line-pill--<?= Template::e($pillSlug) ?>"
               aria-label="Ligne <?= Template::e($line['code']) ?> du métro">
              <?= Template::e($pillLabel) ?>
            </a>
          <?php else: ?>
            <span class="line-pill line-pill--<?= Template::e($pillShape) ?> line-pill--<?= Template::e($pillSlug) ?>"
                  aria-label="Ligne <?= Template::e($line['code']) ?> du métro">
              <?= Template::e($pillLabel) ?>
            </span>
          <?php endif; ?>
        <?php endforeach; ?>
      </div>

      <?php if (!empty($hero['tagline'])): ?>
        <p class="station-hero__tagline"><?= Template::e($hero['tagline']) ?></p>
      <?php endif; ?>

      <?php if (!empty($hero['description'])): ?>
        <p class="station-hero__description">
          <?= richText($hero['description']) ?>
        </p>
      <?php endif; ?>

      <?php if ($address): ?>
        <p class="station-hero__address">
          <span aria-hidden="true">📍</span>
          <?= Template::e($address) ?>
        </p>
      <?php endif; ?>
    </div>

  </section>

  <!-- ============================================================
       1bis. QUICK LINKS (barre de raccourcis vers les sections)
            Place juste sous le hero pour que l'utilisateur puisse
            sauter directement à la section qu'il veut lire (trafic,
            sorties, plan, horaires, etc.). Le bouton "Trafic" porte
            un badge dynamique selon l'etat du reseau.
       ============================================================ -->
  <?php
  $traffic = function_exists('getDisruptionsForStation')
      ? getDisruptionsForStation($lines)
      : null;
  // disruptionsCount : null si API inconnue, 0 si trafic normal,
  // sinon nombre de lignes de la station impactees.
  $disruptionsCount = null;
  if (is_array($traffic)) {
      $disruptionsCount = count($traffic['lines_with_disruptions'] ?? []);
  }
  $tpl->partial('components/station/quick-links', [
      'disruptionsCount' => $disruptionsCount,
      'hasExits'         => !empty($station['exits']),
      'hasPois'          => !empty($station['nearby_pois']),
      'hasFaq'           => !empty($faq),
  ]);
  ?>

  <!-- Zone publicitaire 1 — post-hero/intro (placeholder, voir docs/MONETIZATION-STRATEGY.md) -->
  <div class="ad-zone ad-zone--post-hero" data-ad-slot="post-hero"></div>

  <?php
  ?>

  <!-- ============================================================
       1ter. INFO TRAFIC SEO (paragraphe statique, H2 PARENT du bloc dynamique
            qui suit. Toujours present pour ranker sur "trafic", "perturbation",
            "incident metro {station}" meme en l'absence de perturbation).
       ============================================================ -->
  <?php $tpl->partial('components/station/trafic-info-seo', [
      'stationName' => $name,
      'lines'       => $lines,
  ]);
  ?>

  <!-- ============================================================
       1quater. TRAFIC TEMPS REEL (donnees IDFM PRIM, cache serveur 5 min).
            Enfant semantique du H2 SEO ci-dessus : titre H3.
            Bandeau adaptatif : mince et vert si trafic normal,
            bloc complet et coloré si au moins une perturbation.
       ============================================================ -->
  <?php
  $tpl->partial('components/station/trafic-temps-reel', [
      'traffic'     => $traffic,
      'stationName' => $name,
      'allLines'    => $lines,
  ]);
  ?>

  <!-- ============================================================
       2. CORRESPONDANCES (métro + RER)
       ============================================================ -->
  <section class="station-section section-correspondances" id="correspondances" aria-labelledby="correspondances-title">

    <h2 id="correspondances-title">Correspondances à la station <?= Template::e($name) ?></h2>

    <p class="section-intro">
      La <strong>station <?= Template::e($name) ?></strong> permet de correspondre entre <?= count($lines) ?> lignes de métro<?= !empty($rer) ? ' et ' . count($rer) . ' lignes de RER' : '' ?>.
    </p>

    <div class="correspondances-grid">

      <!-- Métro -->
      <div class="correspondances-block">
        <h3>Lignes de métro à <?= Template::e($name) ?></h3>
        <ul class="correspondances-list">
          <?php foreach ($lines as $line):
            // URL publique : /metro/ligne-{code}/ (derive depuis code, pas slug).
            $lineUrl = '/metro/ligne-' . strtolower((string)($line['code'] ?? '')) . '/';
            $lineExists = Routes::exists(rtrim($lineUrl, '/'));
            $lineMeta = function_exists('getLineMeta')
                ? getLineMeta((string)($line['slug'] ?? ''))
                : null;
            $hasTerminus = $lineMeta
                && ($lineMeta['terminus_a'] !== '' || $lineMeta['terminus_b'] !== '');
          ?>
            <?php
              // Correction 16a : migration vers .line-pill (correction unifiée 2026-05-12).
              // Label "M{code}" préfixé pour cohérence avec hero badges (correction 15).
              $pillLabel = 'M' . $line['code'];
              $pillSlug  = 'm' . strtolower((string)$line['code']);
            ?>
            <li>
              <div class="correspondance-line-link<?= $lineExists ? '' : ' correspondance-line-link--inactive' ?>">
                <span class="line-pill line-pill--<?= Template::e(linePillShape($pillLabel)) ?> line-pill--<?= Template::e($pillSlug) ?>"
                      aria-label="Ligne <?= Template::e($line['code']) ?> du métro">
                  <?= Template::e($pillLabel) ?>
                </span>
                <div class="correspondance-line-content">
                  <?php if ($lineExists): ?>
                    <a href="<?= Template::e($lineUrl) ?>" class="correspondance-line-name">Ligne <?= Template::e($line['code']) ?> du métro</a>
                  <?php else: ?>
                    <span class="correspondance-line-name">Ligne <?= Template::e($line['code']) ?> du métro</span>
                  <?php endif; ?>
                  <?php if ($hasTerminus): ?>
                    <small class="correspondance-line-terminus">
                      <span aria-hidden="true">↔</span>
                      <?= Template::e($lineMeta['terminus_a']) ?>
                      <span aria-hidden="true">⇄</span>
                      <?= Template::e($lineMeta['terminus_b']) ?>
                    </small>
                  <?php endif; ?>
                </div>
              </div>
            </li>
          <?php endforeach; ?>
        </ul>
      </div>

<!-- RER -->
      <?php if (!empty($rer)): ?>
        <div class="correspondances-block">
          <h3>Correspondances RER à <?= Template::e($name) ?></h3>
          <ul class="correspondances-list">
            <?php foreach ($rer as $r):
              $rerUrl = '/rer/rer-' . strtolower($r['code']) . '/';
              $rerExists = Routes::exists(rtrim($rerUrl, '/'));
              $rerInfo = function_exists('getRerTerminus')
                  ? getRerTerminus((string)$r['code'])
                  : null;
              // Format adaptatif : compact si <=3 terminus total, hierarchique sinon
              $totalTerminus = 0;
              if ($rerInfo) {
                  foreach ($rerInfo['directions'] as $dir) {
                      $totalTerminus += count($dir['terminus']);
                  }
              }
              $useHierarchical = $totalTerminus >= 4;
            ?>
              <?php
                // Correction 16a : .line-pill--square + couleur RATP officielle via classe.
                $rerLabel = 'RER ' . $r['code'];
                $rerPillSlug = 'rer-' . strtolower($r['code']);
              ?>
              <li>
                <div class="correspondance-line-link<?= $rerExists ? '' : ' correspondance-line-link--inactive' ?>">
                  <span class="line-pill line-pill--square line-pill--<?= Template::e($rerPillSlug) ?>"
                        aria-label="<?= Template::e($rerLabel) ?>">
                    <?= Template::e($rerLabel) ?>
                  </span>
                  <div class="correspondance-line-content">
                    <div class="correspondance-line-title">
                      <?php if ($rerExists): ?>
                        <a href="<?= Template::e($rerUrl) ?>" class="correspondance-line-name">RER <?= Template::e($r['code']) ?></a>
                      <?php else: ?>
                        <span class="correspondance-line-name">RER <?= Template::e($r['code']) ?></span>
                      <?php endif; ?>
                      <?php if (!empty($r['station_name']) && $r['station_name'] !== $name):
                        // Regle T13 : affiche station_name si different du nom courant.
                        // conditionalLink prepare le futur lien vers /rer/{code}/station/{slug}/.
                        $rerStationUrl = '/rer/' . strtolower((string)$r['code']) . '/station/' . Routes::stationSlug((string)$r['station_name']) . '/';
                        echo conditionalLink($rerStationUrl, '· ' . Template::e((string)$r['station_name']), 'correspondance-line-station');
                      endif; ?>
                    </div>
                    <?php if (!empty($r['walking_minutes'])): ?>
                      <span class="correspondance-line-walking"><?= (int)$r['walking_minutes'] ?> min à pied</span>
                    <?php endif; ?>
                    <?php if ($rerInfo && !$useHierarchical):
                      $parts = [];
                      foreach ($rerInfo['directions'] as $dir) {
                          $parts[] = implode(' / ', $dir['terminus']);
                      }
                    ?>
                      <small class="correspondance-line-terminus">
                        <span aria-hidden="true">↔</span>
                        <?= Template::e($parts[0] ?? '') ?>
                        <?php if (count($parts) > 1): ?>
                          <span aria-hidden="true">⇄</span>
                          <?= Template::e($parts[1]) ?>
                        <?php endif; ?>
                      </small>
                    <?php elseif ($rerInfo && $useHierarchical): ?>
                      <small class="correspondance-line-terminus correspondance-line-terminus--multi">
                        <?php foreach ($rerInfo['directions'] as $dir):
                          $firstChar = mb_strtolower(mb_substr($dir['label'], 0, 1, 'UTF-8'), 'UTF-8');
                          $vowelStart = (bool) preg_match('/^[aeiouyhâêîôûäëïöü]/u', $firstChar);
                          $preposition = $vowelStart ? "l'" : "le ";
                        ?>
                          <span class="correspondance-line-terminus__direction">
                            <span class="correspondance-line-terminus__label">Vers <?= e($preposition) ?><?= Template::e($dir['label']) ?> :</span>
                            <span class="correspondance-line-terminus__list">
                              <?= Template::e(implode(', ', $dir['terminus'])) ?>
                            </span>
                          </span>
                        <?php endforeach; ?>
                      </small>
                    <?php endif; ?>
                  </div>
                </div>
              </li>
            <?php endforeach; ?>
          </ul>
        </div>
      <?php endif; ?>

      <!-- Tramway -->
      <?php if (!empty($tram)): ?>
        <div class="correspondances-block">
          <h3>Correspondances Tramway à <?= Template::e($name) ?></h3>
          <ul class="correspondances-list">
            <?php foreach ($tram as $t):
              $tramCode = (string)($t['code'] ?? '');
              $tramUrl  = '/tramway/t' . strtolower($tramCode) . '/';
              $tramExists = Routes::exists(rtrim($tramUrl, '/'));
            ?>
              <?php
                // Correction 16a : .line-pill--square pour tramway (couleurs officielles bundle.css)
                $tramLabel = 'T' . $tramCode;
                $tramPillSlug = 't' . strtolower($tramCode);
              ?>
              <li>
                <div class="correspondance-line-link<?= $tramExists ? '' : ' correspondance-line-link--inactive' ?>">
                  <span class="line-pill line-pill--square line-pill--<?= Template::e($tramPillSlug) ?>"
                        aria-label="Tramway <?= Template::e($tramLabel) ?>">
                    <?= Template::e($tramLabel) ?>
                  </span>
                  <div class="correspondance-line-content">
                    <?php if ($tramExists): ?>
                      <a href="<?= Template::e($tramUrl) ?>" class="correspondance-line-name">Tramway T<?= Template::e($tramCode) ?></a>
                    <?php else: ?>
                      <span class="correspondance-line-name">Tramway T<?= Template::e($tramCode) ?></span>
                    <?php endif; ?>
                    <?php if (!empty($t['walking_minutes'])): ?>
                      <span class="correspondance-line-walking"><?= (int)$t['walking_minutes'] ?> min à pied</span>
                    <?php endif; ?>
                    <?php if (!empty($t['destinations'])): ?>
                      <small class="correspondance-line-terminus">
                        <span aria-hidden="true">↔</span>
                        <?= Template::e($t['destinations']) ?>
                      </small>
                    <?php endif; ?>
                  </div>
                </div>
              </li>
            <?php endforeach; ?>
          </ul>
        </div>
      <?php endif; ?>

      <!-- Transilien (SNCF) -->
      <?php if (!empty($transilien)): ?>
        <div class="correspondances-block">
          <h3>Correspondances Transilien à <?= Template::e($name) ?></h3>
          <ul class="correspondances-list">
            <?php foreach ($transilien as $tn):
              $tnCode = (string)($tn['code'] ?? '');
              $tnUrl  = '/transilien/transilien-' . strtolower($tnCode) . '/';
              $tnExists = Routes::exists(rtrim($tnUrl, '/'));
            ?>
              <?php
                // Correction 16a : .line-pill--square pour Transilien (label = lettre seule H/J/K/...)
                $tnPillSlug = strtolower($tnCode);
              ?>
              <li>
                <div class="correspondance-line-link<?= $tnExists ? '' : ' correspondance-line-link--inactive' ?>">
                  <span class="line-pill line-pill--square line-pill--<?= Template::e($tnPillSlug) ?>"
                        aria-label="Transilien <?= Template::e($tnCode) ?>">
                    <?= Template::e($tnCode) ?>
                  </span>
                  <div class="correspondance-line-content">
                    <?php if ($tnExists): ?>
                      <a href="<?= Template::e($tnUrl) ?>" class="correspondance-line-name">Transilien <?= Template::e($tnCode) ?></a>
                    <?php else: ?>
                      <span class="correspondance-line-name">Transilien <?= Template::e($tnCode) ?></span>
                    <?php endif; ?>
                    <?php if (!empty($tn['walking_minutes'])): ?>
                      <span class="correspondance-line-walking"><?= (int)$tn['walking_minutes'] ?> min à pied</span>
                    <?php endif; ?>
                    <?php if (!empty($tn['destinations'])): ?>
                      <small class="correspondance-line-terminus">
                        <span aria-hidden="true">↔</span>
                        <?= Template::e($tn['destinations']) ?>
                      </small>
                    <?php endif; ?>
                  </div>
                </div>
              </li>
            <?php endforeach; ?>
          </ul>
        </div>
      <?php endif; ?>

      <!-- Bus (RATP + régional + Noctilien) -->
      <?php
      $busDiurnes = is_array($bus) ? ($bus['diurne'] ?? []) : [];
      $busNoct    = is_array($bus) ? ($bus['nocturne'] ?? []) : [];
      $busReg     = is_array($bus) ? ($bus['regional'] ?? []) : [];
      $hasAnyBus  = !empty($busDiurnes) || !empty($busNoct) || !empty($busReg);
      // Fallback texte neutre (regle T11/T13) quand pas de liste GTFS auditee.
      $busNote    = is_array($bus) ? (string)($bus['_note_visible'] ?? '') : '';
      ?>
      <?php
      // Helper inline : rend une pastille bus, lien actif si la page
      // /bus/ligne-{code}/ existe (Routes::exists), sinon span statique
      // avec data-future-url pour traçabilité (cocon SEO posé en avance).
      $renderBusBadge = function (string $code, string $extraClass = '') {
          $url = '/bus/ligne-' . strtolower($code) . '/';
          $cls = trim('correspondance-bus-badge ' . $extraClass);
          if (Routes::exists(rtrim($url, '/'))) {
              return '<a href="' . Template::e($url) . '" class="' . Template::e($cls) . '">'
                   . Template::e($code) . '</a>';
          }
          return '<span class="' . Template::e($cls) . '" data-future-url="' . Template::e($url) . '">'
               . Template::e($code) . '</span>';
      };
      ?>
      <?php if ($hasAnyBus): ?>
        <div class="correspondances-block">
          <h3>Lignes de bus à <?= Template::e($name) ?></h3>
          <?php if (!empty($busDiurnes)): ?>
            <div class="correspondance-bus-row">
              <p class="correspondance-bus-label"><strong>Bus diurnes</strong></p>
              <div class="correspondance-bus-list">
                <?php foreach ($busDiurnes as $b): ?>
                  <?= $renderBusBadge((string)$b) ?>
                <?php endforeach; ?>
              </div>
            </div>
          <?php endif; ?>
          <?php if (!empty($busNoct)): ?>
            <div class="correspondance-bus-row">
              <p class="correspondance-bus-label"><strong>Noctilien</strong></p>
              <div class="correspondance-bus-list">
                <?php foreach ($busNoct as $b): ?>
                  <?= $renderBusBadge((string)$b, 'correspondance-bus-badge--noct') ?>
                <?php endforeach; ?>
              </div>
            </div>
          <?php endif; ?>
          <?php if (!empty($busReg)): ?>
            <div class="correspondance-bus-row">
              <p class="correspondance-bus-label"><strong>Bus régionaux</strong></p>
              <div class="correspondance-bus-list">
                <?php foreach ($busReg as $b): ?>
                  <?= $renderBusBadge((string)$b, 'correspondance-bus-badge--reg') ?>
                <?php endforeach; ?>
              </div>
            </div>
          <?php endif; ?>
        </div>
      <?php elseif ($busNote !== ''): ?>
        <div class="correspondances-block">
          <h3>Lignes de bus à <?= Template::e($name) ?></h3>
          <p class="correspondances-bus-note"><?= Template::e($busNote) ?></p>
        </div>
      <?php endif; ?>

    </div>
  </section>

  <!-- ============================================================
       3. INTRODUCTION SEO (paragraphes longs)
       ============================================================ -->
  <?php if (!empty($intros)): ?>
    <section class="station-section section-intro-seo" aria-label="Présentation de la station">
      <?php foreach ($intros as $paragraph): ?>
        <p><?= $paragraph ?></p>
      <?php endforeach; ?>
    </section>
  <?php endif; ?>

  <!-- ============================================================
       4. STATIONS ADJACENTES (par ligne)
            Defensive : pre-filtre les lignes qui ont au moins une station
            adjacente (prev OU next). Skip toute la section si aucune ligne
            desservie n'a de data utilisable (cas station avec adjacent_stations
            absent/malforme). Pluralisation correcte 1 ligne / N lignes.
       ============================================================ -->
  <?php
  $adjacentBlocks = [];
  if (!empty($adjacent)) {
      foreach ($lines as $line) {
          $adj = $adjacent[$line['slug']] ?? null;
          if (!$adj) continue;
          $prev = $adj['previous'] ?? null;
          $next = $adj['next']     ?? null;
          if (!$prev && !$next) continue; // skip H3 vide
          $adjacentBlocks[] = ['line' => $line, 'prev' => $prev, 'next' => $next];
      }
  }
  $adjacentCount = count($adjacentBlocks);
  ?>
  <?php if ($adjacentCount > 0): ?>
    <section class="station-section section-adjacent" id="stations-adjacentes" aria-labelledby="adjacent-title">

      <h2 id="adjacent-title"><?= Template::e(buildSectionTitleAdjacent($station)) ?></h2>

      <p class="section-intro">
        <?php if ($adjacentCount === 1): ?>
          Voici les stations directement avant et après <?= Template::e($name) ?> sur la ligne desservie.
        <?php else: ?>
          Voici les stations directement avant et après <?= Template::e($name) ?> sur chacune des <?= (int)$adjacentCount ?> lignes desservies.
        <?php endif; ?>
      </p>

      <div class="adjacent-grid">
        <?php foreach ($adjacentBlocks as $block):
          $line = $block['line'];
          $prev = $block['prev'];
          $next = $block['next'];
        ?>
          <div class="adjacent-line-block">
            <?php
            // H3 enrichi avec directions selon type de station :
            // - terminus (prev XOR next) → « direction {dir unique} »
            // - centrale (prev AND next) → « directions {prev.dir} et {next.dir} »
            $dirs = [];
            if ($prev && !empty($prev['direction'])) $dirs[] = $prev['direction'];
            if ($next && !empty($next['direction'])) $dirs[] = $next['direction'];
            $dirs = array_values(array_unique($dirs));
            $dirLabel = '';
            if (count($dirs) === 1) {
                $dirLabel = ' — direction ' . $dirs[0];
            } elseif (count($dirs) >= 2) {
                $dirLabel = ' — directions ' . $dirs[0] . ' et ' . $dirs[1];
            }
            ?>
            <?php
              // Correction 16a : .line-pill--metro pour stations adjacentes métro (sur la même ligne)
              $adjPillLabel = 'M' . $line['code'];
              $adjPillSlug  = 'm' . strtolower((string)$line['code']);
            ?>
            <h3 class="adjacent-line-title">
              <span class="line-pill line-pill--<?= Template::e(linePillShape($adjPillLabel)) ?> line-pill--<?= Template::e($adjPillSlug) ?>"
                    aria-label="Ligne <?= Template::e($line['code']) ?> du métro">
                <?= Template::e($adjPillLabel) ?>
              </span>
              <span>Ligne <?= Template::e($line['code']) ?><?= Template::e($dirLabel) ?></span>
            </h3>

            <div class="adjacent-stations">
              <?php if ($prev):
                $prevUrl = '/metro/station/' . $prev['slug'] . '/';
              ?>
                <div class="adjacent-station adjacent-station--prev">
                  <span class="adjacent-station-arrow" aria-hidden="true">←</span>
                  <div>
                    <?= conditionalLink($prevUrl, Template::e($prev['name']), 'adjacent-station-name') ?>
                    <span class="adjacent-station-direction">Vers <?= Template::e($prev['direction']) ?></span>
                  </div>
                </div>
              <?php endif; ?>

              <?php if ($next):
                $nextUrl = '/metro/station/' . $next['slug'] . '/';
              ?>
                <div class="adjacent-station adjacent-station--next">
                  <div>
                    <?= conditionalLink($nextUrl, Template::e($next['name']), 'adjacent-station-name') ?>
                    <span class="adjacent-station-direction">Vers <?= Template::e($next['direction']) ?></span>
                  </div>
                  <span class="adjacent-station-arrow" aria-hidden="true">→</span>
                </div>
              <?php endif; ?>
            </div>
          </div>
        <?php endforeach; ?>
      </div>
    </section>
  <?php endif; ?>

<!-- ============================================================
       4bis. HORAIRES PAR LIGNE
       ============================================================ -->
  <?php $tpl->partial('components/station/horaires-par-ligne', [
      'lines'        => $lines,
      'stationName'  => $name,
      'sectionTitle' => buildSectionTitleHoraires($station),
  ]);
  ?>

  <!-- ============================================================
       4bis-post. TARIFS ET TITRES DE TRANSPORT
                  (source : data/global/transit-pricing.json)
       ============================================================ -->
  <?php
  // Composition d'une liste lisible des modes desservant la station
  // pour personnaliser l'intro tarifs (« la Ligne 1, le RER A et E, … »)
  $modesParts = [];
  if (!empty($lines)) {
      $codes = array_map(fn($l) => $l['code'] ?? '', $lines);
      $modesParts[] = (count($codes) === 1) ? 'la Ligne ' . $codes[0] : 'les Lignes ' . implode(', ', $codes);
  }
  if (!empty($rer)) {
      $rerCodesL = array_map(fn($r) => $r['code'] ?? '', $rer);
      $modesParts[] = (count($rerCodesL) === 1) ? 'le RER ' . $rerCodesL[0] : 'les RER ' . implode(' et ', $rerCodesL);
  }
  if (!empty($tram)) {
      $tramCodesL = array_map(fn($t) => 'T' . ($t['code'] ?? ''), $tram);
      $modesParts[] = (count($tramCodesL) === 1) ? 'le tramway ' . $tramCodesL[0] : 'les tramways ' . implode(' et ', $tramCodesL);
  }
  if (!empty($transilien)) {
      $tnCodesL = array_map(fn($tn) => $tn['code'] ?? '', $transilien);
      $modesParts[] = (count($tnCodesL) === 1) ? 'le Transilien ' . $tnCodesL[0] : 'les Transilien ' . implode(' et ', $tnCodesL);
  }
  $modesList = '';
  if (!empty($modesParts)) {
      $last = array_pop($modesParts);
      $modesList = empty($modesParts) ? $last : implode(', ', $modesParts) . ' et ' . $last;
  }
  ?>
  <?php $tpl->partial('components/station/tarifs', [
      'stationName'       => $name,
      'tariffZone'        => $station['tariff_zone'] ?? null,
      'tariffZoneContext' => $station['tariff_zone_context'] ?? null,
      'commune'           => $station['commune'] ?? null,
      'modesList'         => $modesList ?: null,
  ]); ?>

  <!-- ============================================================
       4ter. SORTIES (acces numerotes, eventuellement regroupes par secteurs)
       ============================================================ -->
  <?php $tpl->partial('components/station/sorties', [
      'exits'        => $station['exits']        ?? [],
      'exitSectors'  => $station['exit_sectors'] ?? null,
      'stationName'  => $name,
      'sectionTitle' => buildSectionTitleSorties($station),
  ]);
  ?>

  <!-- ============================================================
       4ter-post. SERVICES ET INFOS PRATIQUES (WiFi, toilettes, etc.)
       ============================================================ -->
  <?php $tpl->partial('components/station/services', [
      'services'    => $station['services'] ?? null,
      'stationName' => $name,
  ]); ?>

  <!-- ============================================================
       4quater. CARTE INTERACTIVE (Leaflet + OpenStreetMap, lazy-load)
                Affichee uniquement au clic du bouton, ne charge ni
                Leaflet JS/CSS ni les tuiles tant que l'utilisateur
                n'a pas demande explicitement le plan.
       ============================================================ -->
  <?php $tpl->partial('components/station/carte', [
      'station' => [
          'lat'  => $station['latitude']  ?? null,
          'lon'  => $station['longitude'] ?? null,
          'name' => $name,
      ],
      'exits' => $station['exits']        ?? [],
      'pois'  => $station['nearby_pois']  ?? [],
  ]);
  ?>

  <!-- Zone publicitaire 2 — mid-content (placeholder) -->
  <div class="ad-zone ad-zone--mid-content" data-ad-slot="mid-content"></div>

  <!-- ============================================================
       4quater-bis. ITINÉRAIRES POPULAIRES (V1 hub-and-spoke)
                    Zone exploratoire : transition entre la
                    sequence transactionnelle (correspondances,
                    horaires, sorties, plan) et la sequence
                    decouverte (POIs, histoire, FAQ).
       ============================================================ -->
  <?php $tpl->partial('components/station/itineraires-populaires', [
      'itineraries'  => $station['popular_itineraries'] ?? [],
      'stationName'  => $name,
      'stationSlug'  => $station['slug'] ?? null,
      'sectionTitle' => buildSectionTitleItineraires($station),
  ]); ?>

  <!-- ============================================================
       4quinquies. POI A PROXIMITE (Wikidata + Wikipedia + Commons)
                   Place ici (et plus apres FAQ) pour grouper la
                   sequence narrative geographique :
                   sorties -> plan -> itineraires -> POIs -> histoire/FAQ.
       ============================================================ -->
  <?php $tpl->partial('components/station/poi-nearby', [
      'pois'        => $station['nearby_pois'] ?? [],
      'stationName' => $name,
  ]);
  ?>

  <!-- ============================================================
       5. HISTOIRE
       ============================================================ -->
  <?php if (!empty($history['paragraphs'])): ?>
    <section class="station-section section-history" id="histoire" aria-labelledby="history-title">
      <h2 id="history-title">Histoire de la station <?= Template::e($nameFull) ?></h2>
      <?php if (!empty($history['title']) && $history['title'] !== 'Histoire de la station'): ?>
        <p class="section-subtitle"><em><?= Template::e($history['title']) ?></em></p>
      <?php endif; ?>
      <?php foreach ($history['paragraphs'] as $para): ?>
        <p><?= $para ?></p>
      <?php endforeach; ?>
    </section>
  <?php endif; ?>

  <!-- ============================================================
       5bis. LE SAVIEZ-VOUS (anecdotes verifiees sur la station)
       ============================================================ -->
  <?php $tpl->partial('components/station/trivia', [
      'trivia'      => $station['trivia'] ?? [],
      'stationName' => $name,
  ]); ?>

  <!-- ============================================================
       6. FAQ (rendu HTML — schema.org est dans le head via $seo->addSchema)
       ============================================================ -->
  <?php if (!empty($faq)): ?>
    <section class="station-section section-faq" id="faq" aria-labelledby="faq-title">

      <h2 id="faq-title">Questions fréquentes sur la station <?= Template::e($name) ?></h2>

      <div class="faq-list">
        <?php foreach ($faq as $i => $item): ?>
          <details class="faq-item" <?= $i === 0 ? 'open' : '' ?>>
            <summary class="faq-question">
              <h3 class="faq-question__heading"><?= richText($item['question']) ?></h3>
            </summary>
            <div class="faq-answer">
              <p><?= richText($item['answer']) ?></p>
            </div>
          </details>
        <?php endforeach; ?>
      </div>
    </section>
  <?php endif; ?>

  <!-- Zone publicitaire 3 — pre-footer-content (placeholder) -->
  <div class="ad-zone ad-zone--pre-footer-content" data-ad-slot="pre-footer-content"></div>

  <!-- ============================================================
       6bis. SÉCURITÉ ET CONSEILS VOYAGEUR
       ============================================================ -->
  <?php $tpl->partial('components/station/securite', [
      'safety'      => $station['safety'] ?? null,
      'stationName' => $name,
  ]); ?>

  <!-- ============================================================
       7. CONSEILS PRATIQUES
       ============================================================ -->
  <?php if (!empty($tips)): ?>
    <section class="station-section section-tips" id="conseils" aria-labelledby="tips-title">
      <h2 id="tips-title">Conseils pratiques pour bien circuler à <?= Template::e($name) ?></h2>
      <ul class="tips-list">
        <?php foreach ($tips as $tip): ?>
          <li><span class="tips-icon" aria-hidden="true">💡</span> <?= richText($tip) ?></li>
        <?php endforeach; ?>
      </ul>
    </section>
  <?php endif; ?>

  <!-- Zone publicitaire 4 — pre-maillage (placeholder) -->
  <div class="ad-zone ad-zone--pre-maillage" data-ad-slot="pre-maillage"></div>

  <!-- ============================================================
       7bis. MAILLAGE INTERNE — « Continuer votre exploration »
             4 blocs : stations voisines, hub ligne, hubs similaires
             (si major_hub), liens utilitaires.
       ============================================================ -->
  <?php $tpl->partial('components/station/maillage-interne', [
      'station'     => $station,
      'stationName' => $name,
      'stationSlug' => $slug,
      'lines'       => $lines,
  ]); ?>

  <!-- ============================================================
       8. DATE DE MISE A JOUR (signal de fraicheur Discover).
            Source : filemtime() sur le JSON station si pas de champ
            'updated_at' explicite dans data/stations/{slug}.json.
       ============================================================ -->
  <?php
  $updatedTs = null;
  if (!empty($station['updated_at'])) {
      $updatedTs = is_int($station['updated_at'])
          ? $station['updated_at']
          : (strtotime((string)$station['updated_at']) ?: null);
  }
  if ($updatedTs === null) {
      $stationFilePath = __DIR__ . '/../../data/stations/' . $slug . '.json';
      if (is_file($stationFilePath)) {
          $updatedTs = filemtime($stationFilePath);
      }
  }
  if ($updatedTs):
  ?>
    <p class="station-last-updated">
      Page mise à jour le
      <time datetime="<?= e(date('Y-m-d', $updatedTs)) ?>"><?= e(dateFr($updatedTs)) ?></time>.
    </p>
  <?php endif; ?>

</article>
</div>
