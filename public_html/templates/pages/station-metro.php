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
$hero      = $station['hero']      ?? [];
$adjacent  = $station['adjacent_stations'] ?? [];
$image     = $station['image']     ?? null;
$intros    = $station['intro_paragraphs'] ?? [];
$faq       = $station['faq']       ?? [];
$tips      = $station['practical_tips'] ?? [];
$history   = $station['history']   ?? [];

$hasImage  = !empty($image['src']);
$canonical = '/metro/station/' . $slug . '/';

// Charger le CSS dédié
$tpl->addStylesheet('/assets/css/station.css');

// SEO de base
$lineCount = count($lines);
$rerCodes = !empty($rer) ? ' + RER ' . implode(' ', array_column($rer, 'code')) : '';
$arrLabel = $arr ? ' (Paris ' . $arr . ')' : '';

$tpl->seo
    ->setTitle('Station ' . $name . $arrLabel . ' : ' . $lineCount . ' ligne' . ($lineCount > 1 ? 's' : '') . ' métro' . $rerCodes)
    ->setDescription($hero['description'] ?? ('Tout savoir sur la station ' . $name . ' du métro parisien : lignes desservies, correspondances RER, stations adjacentes, histoire et conseils pratiques.'))
    ->setCanonical($canonical);

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
    ['label' => 'Accueil',  'url' => '/'],
    ['label' => 'Métro',    'url' => '/metro/'],
    ['label' => 'Stations', 'url' => '/metro/'],
    ['label' => $name,      'url' => $canonical],
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
    'image'              => $hasImage ? $siteUrl . $image['src'] : null,
    'isAccessibleForFree'=> true,
    'publicAccess'       => true,
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

// Assemblage @graph
$graphNodes = [
    [
        '@type'           => 'BreadcrumbList',
        '@id'             => $canonicalAbs . '#breadcrumb',
        'itemListElement' => $breadcrumbList,
    ],
    $stationNode,
];
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
        <img src="<?= Template::e($image['src']) ?>"
             alt="<?= Template::e($image['alt'] ?? $name) ?>"
             width="1200" height="675"
             loading="eager" fetchpriority="high">
      </div>
    <?php endif; ?>

    <div class="station-hero__content">
      <div class="station-hero__badges" aria-label="Lignes desservant la station">
        <?php foreach ($lines as $line):
          $lineUrl = '/metro/' . $line['slug'] . '/';
          $lineExists = Routes::exists(rtrim($lineUrl, '/'));
        ?>
          <?php if ($lineExists): ?>
            <a href="<?= Template::e($lineUrl) ?>"
               class="station-line-badge"
               style="background:<?= Template::e($line['color']) ?>;color:<?= Template::e($line['text_color']) ?>;"
               aria-label="Ligne <?= Template::e($line['code']) ?> du métro">
              <?= Template::e($line['code']) ?>
            </a>
          <?php else: ?>
            <span class="station-line-badge station-line-badge--inactive"
                  style="background:<?= Template::e($line['color']) ?>;color:<?= Template::e($line['text_color']) ?>;"
                  aria-label="Ligne <?= Template::e($line['code']) ?> du métro">
              <?= Template::e($line['code']) ?>
            </span>
          <?php endif; ?>
        <?php endforeach; ?>
      </div>

      <h1 id="station-hero-title">
        Station <?= Template::e($name) ?>
      </h1>

      <?php if (!empty($hero['tagline'])): ?>
        <p class="station-hero__tagline"><?= Template::e($hero['tagline']) ?></p>
      <?php endif; ?>

      <?php if (!empty($hero['description'])): ?>
        <p class="station-hero__description">
          <?= Template::e($hero['description']) ?>
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

  <!-- ============================================================
       1ter. TRAFIC TEMPS REEL (donnees IDFM PRIM, cache serveur 5 min)
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
       1ter. INFO TRAFIC SEO (paragraphe statique, persistent meme si
            aucune perturbation, pour ranker sur "trafic", "perturbation",
            "incident metro {station}" en permanence dans le HTML).
       ============================================================ -->
  <?php $tpl->partial('components/station/trafic-info-seo', [
      'stationName' => $name,
      'lines'       => $lines,
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
        <h3>Lignes de métro desservant la station</h3>
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
            <li>
              <div class="correspondance-line-link<?= $lineExists ? '' : ' correspondance-line-link--inactive' ?>">
                <span class="correspondance-line-badge"
                      style="background:<?= Template::e($line['color']) ?>;color:<?= Template::e($line['text_color']) ?>;">
                  <?= Template::e($line['code']) ?>
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
          <h3>Correspondances RER (via Châtelet — Les Halles)</h3>
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
              <li>
                <div class="correspondance-line-link<?= $rerExists ? '' : ' correspondance-line-link--inactive' ?>">
                  <span class="correspondance-line-badge correspondance-line-badge--rer"
                        style="background:<?= Template::e($r['color']) ?>;color:#FFFFFF;">
                    RER <?= Template::e($r['code']) ?>
                  </span>
                  <div class="correspondance-line-content">
                    <?php if ($rerExists): ?>
                      <a href="<?= Template::e($rerUrl) ?>" class="correspondance-line-name">RER <?= Template::e($r['code']) ?></a>
                    <?php else: ?>
                      <span class="correspondance-line-name">RER <?= Template::e($r['code']) ?></span>
                    <?php endif; ?>
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
          <p class="correspondances-note">
            <small>Les correspondances RER s'effectuent via les couloirs souterrains menant à la gare Châtelet — Les Halles. Comptez environ 3 à 5 minutes de marche.</small>
          </p>
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
       ============================================================ -->
  <?php if (!empty($adjacent)): ?>
    <section class="station-section section-adjacent" id="stations-adjacentes" aria-labelledby="adjacent-title">

      <h2 id="adjacent-title">Stations adjacentes à <?= Template::e($name) ?></h2>

      <p class="section-intro">
        Voici les stations directement avant et après <?= Template::e($name) ?> sur chacune des <?= count($lines) ?> lignes desservies.
      </p>

      <div class="adjacent-grid">
        <?php foreach ($lines as $line):
          $lineSlug = $line['slug'];
          $adj = $adjacent[$lineSlug] ?? null;
          if (!$adj) continue;
        ?>
          <div class="adjacent-line-block">
            <h3 class="adjacent-line-title">
              <span class="adjacent-line-badge"
                    style="background:<?= Template::e($line['color']) ?>;color:<?= Template::e($line['text_color']) ?>;">
                <?= Template::e($line['code']) ?>
              </span>
              <span>Ligne <?= Template::e($line['code']) ?></span>
            </h3>

            <div class="adjacent-stations">
              <?php
                $prev = $adj['previous'] ?? null;
                $next = $adj['next']     ?? null;
              ?>

              <?php if ($prev):
                $prevUrl = '/metro/station/' . $prev['slug'] . '/';
              ?>
                <div class="adjacent-station adjacent-station--prev">
                  <span class="adjacent-station-arrow" aria-hidden="true">←</span>
                  <div>
                    <span class="adjacent-station-direction">Direction <?= Template::e($prev['direction']) ?></span>
                    <?= conditionalLink($prevUrl, Template::e($prev['name']), 'adjacent-station-name') ?>
                  </div>
                </div>
              <?php else: ?>
                <div class="adjacent-station adjacent-station--terminus">
                  <span class="adjacent-station-name">Terminus</span>
                </div>
              <?php endif; ?>

              <?php if ($next):
                $nextUrl = '/metro/station/' . $next['slug'] . '/';
              ?>
                <div class="adjacent-station adjacent-station--next">
                  <div>
                    <span class="adjacent-station-direction">Direction <?= Template::e($next['direction']) ?></span>
                    <?= conditionalLink($nextUrl, Template::e($next['name']), 'adjacent-station-name') ?>
                  </div>
                  <span class="adjacent-station-arrow" aria-hidden="true">→</span>
                </div>
              <?php else: ?>
                <div class="adjacent-station adjacent-station--terminus">
                  <span class="adjacent-station-name">Terminus</span>
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
      'lines'       => $lines,
      'stationName' => $name,
  ]);
  ?>

  <!-- ============================================================
       4ter. SORTIES (acces numerotes, eventuellement regroupes par secteurs)
       ============================================================ -->
  <?php $tpl->partial('components/station/sorties', [
      'exits'       => $station['exits']        ?? [],
      'exitSectors' => $station['exit_sectors'] ?? null,
      'stationName' => $name,
  ]);
  ?>

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

  <!-- ============================================================
       4quinquies. POI A PROXIMITE (Wikidata + Wikipedia + Commons)
                   Place ici (et plus apres FAQ) pour grouper la
                   sequence narrative geographique :
                   sorties -> plan -> POIs -> histoire/FAQ.
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
      <h2 id="history-title"><?= Template::e($history['title'] ?? 'Histoire de la station') ?></h2>
      <?php foreach ($history['paragraphs'] as $para): ?>
        <p><?= $para ?></p>
      <?php endforeach; ?>
    </section>
  <?php endif; ?>

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
              <?= Template::e($item['question']) ?>
            </summary>
            <div class="faq-answer">
              <p><?= Template::e($item['answer']) ?></p>
            </div>
          </details>
        <?php endforeach; ?>
      </div>
    </section>
  <?php endif; ?>

  <!-- ============================================================
       7. CONSEILS PRATIQUES
       ============================================================ -->
  <?php if (!empty($tips)): ?>
    <section class="station-section section-tips" id="conseils" aria-labelledby="tips-title">
      <h2 id="tips-title">Conseils pratiques pour bien circuler à <?= Template::e($name) ?></h2>
      <ul class="tips-list">
        <?php foreach ($tips as $tip): ?>
          <li><span class="tips-icon" aria-hidden="true">💡</span> <?= Template::e($tip) ?></li>
        <?php endforeach; ?>
      </ul>
    </section>
  <?php endif; ?>

</article>
</div>
