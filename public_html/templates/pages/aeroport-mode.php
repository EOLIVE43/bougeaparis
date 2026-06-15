<?php
/**
 * Template : page détail mode-aéroport (ex: Orly + métro 14, CDG + RER B).
 * Props attendues : $mode (array décodé depuis data/aeroports/{aeroport}/{mode}.json).
 *
 * Sections SEO-driven : H1 par requête de recherche + sections H2 pratiques.
 */
$mode      = $mode ?? $props['mode'] ?? [];
$aeroSlug  = $mode['aeroport_slug'] ?? '';
$aeroName  = $mode['aeroport_name'] ?? '';
$aeroIata  = $mode['aeroport_iata'] ?? '';
$modeSlug  = $mode['mode_slug'] ?? '';
$modeLabel = $mode['mode_label'] ?? '';
$h1        = $mode['h1'] ?? "$modeLabel pour $aeroName";

$tagline   = $mode['tagline'] ?? '';
$intros    = $mode['intro_paragraphs'] ?? [];
$status    = $mode['status'] ?? null;
$altBlock  = $mode['alternatives_block'] ?? null;
$history   = $mode['history'] ?? null;

$quickFacts = $mode['quick_facts'] ?? [];
$itineraire = $mode['itineraire'] ?? [];
$horaires   = $mode['horaires'] ?? [];
$tarifs     = $mode['tarifs'] ?? [];
$itinSource = $mode['itineraires_paris'] ?? [];
$alternatives = $mode['alternatives'] ?? [];
$pois       = $mode['pois'] ?? [];
$faq        = $mode['faq'] ?? [];

$canonical = '/aeroports/' . $aeroSlug . '/' . $modeSlug . '/';

// Cards lignes (ex: bus_lines pour la page bus Orly) — affichées avant FAQ
$busLines = $mode['bus_lines'] ?? [];

// Charger le JSON parent aéroport pour récupérer access_modes[] (maillage interne)
$parentFile = __DIR__ . '/../../data/aeroports/' . $aeroSlug . '.json';
$parentAero = is_file($parentFile) ? json_decode((string)file_get_contents($parentFile), true) : null;
$allModes   = is_array($parentAero) ? ($parentAero['access_modes'] ?? []) : [];
$otherModes = array_values(array_filter($allModes, fn($m) => ($m['slug'] ?? '') !== $modeSlug));

// Title SEO via helper centralisé bp_title_aeroport_mode() / bp_title_taxi_aeroport()
// Extraction durée/prix depuis quick_facts (1er match min/€).
$_duration = null; $_price = null;
foreach ($quickFacts as $_qf) {
    $_v = $_qf['value'] ?? '';
    if ($_duration === null && preg_match('/min|h\d|→/', $_v)) $_duration = $_v;
    if ($_price === null && (str_contains($_v, '€') || stripos($_v, 'gratuit') !== false)) $_price = $_v;
}
// Priorité au seo.title défini dans le JSON s'il existe (≤ 65 chars Google,
// éditorialisé). Sinon fallback sur le helper centralisé qui auto-construit
// à partir de quick_facts.
$_seoTitleJson = trim((string)($mode['seo']['title'] ?? ''));
if ($_seoTitleJson !== '' && mb_strlen($_seoTitleJson, 'UTF-8') <= 70) {
    $_seoTitle = $_seoTitleJson;
} elseif ($modeSlug === 'taxi' && $_price && $_duration) {
    $_seoTitle = bp_title_taxi_aeroport($aeroName, $_price, $_duration);
} else {
    $_seoTitle = bp_title_aeroport_mode($modeLabel, $aeroName, $_duration, $_price);
}
$tpl->seo
    ->setTitle(bp_interpolate_fares($_seoTitle), false)
    ->setDescription(bp_interpolate_fares((string)($mode['seo']['description'] ?? '')))
    ->setCanonical($canonical)
    ->setBreadcrumb([
        ['label' => 'Accueil',    'url' => '/'],
        ['label' => 'Aéroports',  'url' => '/aeroports/'],
        ['label' => $aeroName,    'url' => '/aeroports/' . $aeroSlug . '/'],
        ['label' => $modeLabel,   'url' => $canonical],
    ]);
?>

<?php $tpl->partial('components/breadcrumb', ['items' => [
    ['label' => 'Accueil',    'url' => '/'],
    ['label' => 'Aéroports',  'url' => '/aeroports/'],
    ['label' => $aeroName,    'url' => '/aeroports/' . $aeroSlug . '/'],
    ['label' => $modeLabel,   'url' => $canonical],
]]); ?>

<div class="container">
<article class="aeroport-mode-page">

  <!-- HERO mode-colored + H1 SEO -->
  <section class="mode-hero" data-mode-slug="<?= Template::e($modeSlug) ?>">
    <div class="mode-hero__content">
      <h1><?= Template::e(bp_interpolate_fares($h1)) ?></h1>
      <?php if ($tagline): ?>
        <p class="mode-tagline"><?= Template::e(bp_interpolate_fares($tagline)) ?></p>
      <?php endif; ?>

      <?php if (!empty($quickFacts)): ?>
        <div class="mode-quick-facts">
          <?php foreach ($quickFacts as $fact): ?>
            <div class="mode-fact">
              <span class="fact-value"><?= Template::e(bp_interpolate_fares((string)($fact['value'] ?? ''))) ?></span>
              <span class="fact-label"><?= Template::e(bp_interpolate_fares((string)($fact['label'] ?? ''))) ?></span>
            </div>
          <?php endforeach; ?>
        </div>
      <?php endif; ?>
    </div>
  </section>

  <?php if (is_array($status) && !empty($status['discontinued'])): ?>
    <aside class="status-banner status-banner--discontinued" role="alert">
      <strong>Service supprimé</strong>
      <?php if (!empty($status['discontinued_date'])): ?>
        — dernier départ le <?= Template::e($status['last_service_date'] ?? '') ?>, arrêt définitif au <?= Template::e($status['discontinued_date']) ?>.
      <?php endif; ?>
      <?php if (!empty($status['replacement_label'])): ?>
        <br>Remplacé par : <strong><?= Template::e($status['replacement_label']) ?></strong>
        <?php if (!empty($status['operator_replacement'])): ?> (exploité par <?= Template::e($status['operator_replacement']) ?>)<?php endif; ?>.
      <?php endif; ?>
    </aside>
  <?php endif; ?>

  <?php $tpl->partial('ads/slot-header'); ?>

  <?php if (!empty($intros)): ?>
    <section class="mode-section">
      <?php foreach ($intros as $p): ?>
        <p><?= bp_interpolate_fares((string)$p) ?></p>
      <?php endforeach; ?>
    </section>
  <?php endif; ?>

  <?php if (is_array($altBlock) && !empty($altBlock['items'])): ?>
    <section class="mode-section" id="alternatives-block">
      <h2><?= Template::e($altBlock['h2'] ?? "Alternatives") ?></h2>
      <div class="alt-grid">
        <?php foreach ($altBlock['items'] as $alt):
          $anchor = $alt['anchor'] ?? '';
          $url    = $alt['url'] ?? '';
          $summary= $alt['summary'] ?? '';
          $future = !empty($alt['future']);
          $inner = '<span class="alt-card__anchor">' . htmlspecialchars($anchor) . '</span>'
                 . '<p class="alt-card__summary">' . htmlspecialchars($summary) . '</p>';
        ?>
          <?= conditionalLink($url, $inner, 'alt-card') ?>
        <?php endforeach; ?>
      </div>
    </section>
  <?php endif; ?>

  <?php if (is_array($history) && !empty($history['paragraphs'])): ?>
    <section class="mode-section" id="history">
      <h2><?= Template::e($history['h2'] ?? "Historique") ?></h2>
      <?php foreach ($history['paragraphs'] as $p): ?>
        <p><?= $p ?></p>
      <?php endforeach; ?>
    </section>
  <?php endif; ?>

  <?php
    // Section carte ligne tramway (T7 Orly) — CWV-safe (SVG inline + Leaflet lazy)
    // Conditionnelle : mode tramway + aéroport Paris-Orly + JSON ligne disponible.
    $_lineTramFile = __DIR__ . '/../../data/lines-tram/t7.json';
    $_showT7Map = ($modeSlug === 'tramway' && $aeroSlug === 'paris-orly' && is_file($_lineTramFile));
    if ($_showT7Map):
      $_t7Line = json_decode((string)file_get_contents($_lineTramFile), true);
      $_t7Stations = $_t7Line['stations'] ?? [];
      $_t7First = $_t7Stations[0]['name'] ?? '';
      $_t7Last  = end($_t7Stations)['name'] ?? '';
  ?>
    <section class="tramway-map-section">
      <h2>Tracé de la ligne T7 vers l'aéroport Paris-Orly</h2>
      <p>
        Le <strong>tramway T7</strong> relie <strong><?= Template::e($_t7First) ?></strong>
        à <strong><?= Template::e($_t7Last) ?></strong> en <?= count($_t7Stations) ?> stations.
        Données : <a href="https://data.iledefrance-mobilites.fr/" rel="nofollow noopener">IDFM Open Data</a>.
      </p>

      <?php $tpl->partial('components/leaflet-map-line', ['line_data' => $_t7Line]); ?>

      <div class="line-download-row">
        <a href="/assets/images/lines/t7-trace-villejuif-louis-aragon-aeroport-dorly.png"
           download="plan-t7-villejuif-orly.png"
           class="line-download-btn"
           title="Plan officiel ligne T7 entre Villejuif - Louis Aragon et aéroport Paris-Orly (PNG)">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
            <polyline points="7 10 12 15 17 10"/>
            <line x1="12" y1="15" x2="12" y2="3"/>
          </svg>
          Télécharger le plan officiel T7 (PNG)
        </a>
        <span class="line-download-meta">
          Plan officiel ligne T7 — Villejuif ↔ Aéroport Paris-Orly
        </span>
      </div>
    </section>
  <?php endif; ?>

  <?php if (!empty($busLines)): ?>
    <section class="bus-lines-section">
      <h2>Les <?= count($busLines) ?> lignes de bus vers <?= Template::e($aeroName) ?></h2>
      <div class="bus-cards-grid">
        <?php foreach ($busLines as $bl):
          $blType  = $bl['type'] ?? 'regulier';
          $blSlug  = $bl['slug'] ?? '';
          $blUrl   = '/aeroports/' . $aeroSlug . '/' . $modeSlug . '/' . $blSlug . '/';
          $isDiscontinued = (($bl['status'] ?? '') === 'discontinued');
          $cssClass = 'bus-card bus-card--' . $blType;
          // Card content (identique cliquable/non-cliquable)
          ob_start(); ?>
            <div class="bus-card__icon">
              <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <rect x="6" y="12" width="36" height="22" rx="3"/>
                <line x1="6" y1="24" x2="42" y2="24"/>
                <rect x="10" y="16" width="6" height="5" fill="currentColor"/>
                <rect x="20" y="16" width="6" height="5" fill="currentColor"/>
                <rect x="30" y="16" width="6" height="5" fill="currentColor"/>
                <circle cx="14" cy="36" r="3" fill="currentColor"/>
                <circle cx="34" cy="36" r="3" fill="currentColor"/>
              </svg>
            </div>
            <?php if ($isDiscontinued): ?>
              <span class="bus-card__status-badge">Service supprimé · <?= Template::e($bl['discontinued_date'] ?? '') ?></span>
            <?php endif; ?>
            <div class="bus-card__name"><?= Template::e($bl['name'] ?? '') ?></div>
            <p class="bus-card__route"><?= Template::e($bl['departure'] ?? '') ?> ↔ <?= Template::e($aeroName) ?></p>
            <div class="bus-card__metrics">
              <span class="bus-card__duration"><?= Template::e($bl['duration'] ?? '') ?></span>
              <span class="bus-card__separator">·</span>
              <span class="bus-card__price"><?= Template::e(bp_interpolate_fares((string)($bl['price'] ?? ''))) ?></span>
            </div>
            <?php if (!empty($bl['note'])): ?>
              <p class="bus-card__note"><?= Template::e($bl['note']) ?></p>
            <?php endif; ?>
            <span class="bus-card__cta">→ <?= Template::e($bl['cta_anchor'] ?? $bl['name'] ?? '') ?></span>
          <?php
          $cardInner = ob_get_clean();
          // conditionalLink : si route active → <a>, sinon <span data-future-url>
          echo conditionalLink($blUrl, $cardInner, $cssClass);
        endforeach; ?>
      </div>
    </section>
  <?php endif; ?>

  <?php if (!empty($itineraire)):
    // Auto-détection du badge ligne (M1-M14, T1-T13, RER A-E, Roissybus, Orlybus, Bus N).
    // Sémantique HTML <ol>/<li> préservée + texte intégral conservé pour SEO.
    $stepInfer = function(string $html): array {
        $clean = strip_tags($html);
        // Priorité 1 : ligne identifiable (badge)
        if (preg_match('/\bRoissybus\b/u', $clean))   return ['badge'=>'Bus', 'cls'=>'roissybus', 'type'=>'board'];
        if (preg_match('/\bOrlybus\b/u', $clean))     return ['badge'=>'Bus', 'cls'=>'orlybus',   'type'=>'board'];
        if (preg_match('/\bCDGVAL\b/u', $clean))      return ['badge'=>'CDGVAL', 'cls'=>'cdgval', 'type'=>'board'];
        if (preg_match('/\bOrlyval\b/u', $clean))     return ['badge'=>'Orlyval','cls'=>'orlyval','type'=>'board'];
        if (preg_match('/\bTGV\b/u', $clean))         return ['badge'=>'TGV',    'cls'=>'tgv',    'type'=>'board'];
        if (preg_match('/\bRER\s+([A-E])\b/u', $clean, $m))  return ['badge'=>'RER '.$m[1], 'cls'=>'rer-'.strtolower($m[1]), 'type'=>'board'];
        if (preg_match('/\bM(\d{1,2}\w?)\b/u', $clean, $m))  return ['badge'=>'M'.$m[1], 'cls'=>'m'.strtolower($m[1]), 'type'=>'board'];
        if (preg_match('/\b(?:métro|m[ée]tro)\s+(?:ligne\s+)?(\d{1,2})\b/iu', $clean, $m)) return ['badge'=>'M'.$m[1], 'cls'=>'m'.$m[1], 'type'=>'board'];
        if (preg_match('/\bT(\d{1,2})\b/u', $clean, $m))     return ['badge'=>'T'.$m[1], 'cls'=>'t'.$m[1], 'type'=>'board'];
        if (preg_match('/\b[Tt]ramway\s+T?(\d{1,2})\b/u', $clean, $m)) return ['badge'=>'T'.$m[1], 'cls'=>'t'.$m[1], 'type'=>'board'];
        if (preg_match('/\bBus\s+(\d{2,3}|N\d+)\b/u', $clean, $m))    return ['badge'=>'Bus', 'cls'=>'bus-'.strtolower($m[1]), 'type'=>'board'];
        if (preg_match('/\b(?:bus|car|navette)\b/iu', $clean))        return ['badge'=>'Bus', 'cls'=>'bus',  'type'=>'board'];
        if (preg_match('/\bTaxi\b/iu', $clean))                       return ['badge'=>'Taxi','cls'=>'taxi', 'type'=>'taxi'];
        // Priorité 2 : type d'action (sans badge ligne)
        if (preg_match('/^\s*(?:Descendre|Arriver|Arrivée|Sortir|Sortie)/iu', $clean))     return ['badge'=>'', 'cls'=>'alight',   'type'=>'alight'];
        if (preg_match('/^\s*(?:Suivre|Marcher|à pied|Continuer)/iu', $clean))             return ['badge'=>'', 'cls'=>'walk',     'type'=>'walk'];
        if (preg_match('/^\s*(?:Changer|Correspondance|Prendre la correspondance)/iu', $clean)) return ['badge'=>'', 'cls'=>'transfer', 'type'=>'transfer'];
        return ['badge'=>'', 'cls'=>'default', 'type'=>'default'];
    };
  ?>
    <section class="mode-section" id="itineraire">
      <h2><?= Template::e($itineraire['h2'] ?? "Itinéraire détaillé") ?></h2>
      <?php foreach (($itineraire['paragraphs'] ?? []) as $p): ?>
        <p><?= $p ?></p>
      <?php endforeach; ?>
      <?php if (!empty($itineraire['steps'])): ?>
        <ol class="itinerary-steps">
          <?php foreach ($itineraire['steps'] as $idx => $step):
            $meta = $stepInfer((string)$step);
            $badge = $meta['badge']; $cls = $meta['cls']; $type = $meta['type'];
          ?>
            <li class="step-card" data-step-type="<?= htmlspecialchars($type) ?>">
              <div class="step-card__number" aria-hidden="true"><?= $idx + 1 ?></div>
              <div class="step-card__icon">
                <?php if ($badge): ?>
                  <span class="line-badge line-badge--<?= htmlspecialchars($cls) ?>"><?= htmlspecialchars($badge) ?></span>
                <?php else: ?>
                  <span class="step-icon step-icon--<?= htmlspecialchars($cls) ?>" aria-hidden="true">
                    <?php switch ($cls):
                      case 'alight': ?>
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2v18M5 13l7 7 7-7"/></svg>
                      <?php break; case 'walk': ?>
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="4" r="2"/><path d="M14 6l-2 4 4 4M8 18l3-3 2 3 3 4M10 10l-5 2"/></svg>
                      <?php break; case 'transfer': ?>
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>
                      <?php break; default: ?>
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/></svg>
                    <?php endswitch; ?>
                  </span>
                <?php endif; ?>
              </div>
              <div class="step-card__content"><?= bp_interpolate_fares((string)$step) ?></div>
            </li>
          <?php endforeach; ?>
        </ol>
      <?php endif; ?>
    </section>
  <?php endif; ?>

  <?php $tpl->partial('ads/slot-in-article'); ?>

  <?php if (!empty($horaires)): ?>
    <section class="mode-section" id="horaires">
      <h2><?= Template::e($horaires['h2'] ?? "Horaires") ?></h2>
      <?php foreach (($horaires['paragraphs'] ?? []) as $p): ?>
        <p><?= $p ?></p>
      <?php endforeach; ?>
      <?php if (!empty($horaires['table'])): ?>
        <div class="mode-table-wrap">
          <table class="mode-table">
            <thead>
              <tr>
                <?php foreach ($horaires['table']['headers'] as $h): ?>
                  <th><?= Template::e($h) ?></th>
                <?php endforeach; ?>
              </tr>
            </thead>
            <tbody>
              <?php foreach ($horaires['table']['rows'] as $row): ?>
                <tr>
                  <?php foreach ($row as $cell): ?>
                    <td><?= Template::e($cell) ?></td>
                  <?php endforeach; ?>
                </tr>
              <?php endforeach; ?>
            </tbody>
          </table>
        </div>
      <?php endif; ?>
    </section>
  <?php endif; ?>

  <?php if (!empty($tarifs)):
    // Map mode-slug → SVG icon (icons dispo : metro, bus, rer, tramway, taxi, navette, train)
    $iconMap = ['rer-b' => 'rer', 'tgv' => 'train', 'cdgval' => 'navette'];
    $iconKey = $iconMap[$modeSlug] ?? $modeSlug;
    $iconFp  = __DIR__ . '/../../assets/icons/transport-modes/' . $iconKey . '.svg';
    $iconSvg = is_file($iconFp) ? file_get_contents($iconFp) : '';
  ?>
    <section class="mode-section" id="tarifs">
      <h2><?= Template::e($tarifs['h2'] ?? "Tarifs") ?></h2>
      <?php foreach (($tarifs['paragraphs'] ?? []) as $p): ?>
        <p><?= bp_interpolate_fares((string)$p) ?></p>
      <?php endforeach; ?>
      <?php if (!empty($tarifs['table']['rows'])): ?>
        <div class="info-cards-grid">
          <?php foreach ($tarifs['table']['rows'] as $row):
            $title   = bp_interpolate_fares((string)($row[0] ?? ''));
            $price   = bp_interpolate_fares((string)($row[1] ?? ''));
            $details = bp_interpolate_fares((string)($row[2] ?? ''));
          ?>
            <div class="info-card info-card--<?= Template::e($iconKey) ?>">
              <div class="info-card__icon"><?= $iconSvg ?></div>
              <div class="info-card__content">
                <div class="info-card__title"><?= Template::e($title) ?></div>
                <div class="info-card__body">
                  <?php if ($price !== ''): ?>
                    <span class="info-card__price"><?= Template::e($price) ?></span>
                  <?php endif; ?>
                  <?php if ($details !== ''): ?>
                    <span class="info-card__details"><?= Template::e($details) ?></span>
                  <?php endif; ?>
                </div>
              </div>
            </div>
          <?php endforeach; ?>
        </div>
      <?php endif; ?>
      <?php if (!empty($tarifs['table_note'])):
        // Rendu note sous table : interpole les liens [[link:URL|label]] via
        // conditionalLink (route active → <a>, sinon texte seul).
        $_noteHtml = preg_replace_callback(
          '/\[\[link:([^|\]]+)\|([^\]]+)\]\]/u',
          fn($m) => conditionalLink($m[1], htmlspecialchars($m[2], ENT_QUOTES, 'UTF-8'), 'tarifs-table-note__link'),
          (string)$tarifs['table_note']
        );
      ?>
        <p class="tarifs-table-note"><?= $_noteHtml ?></p>
      <?php endif; ?>
    </section>
  <?php endif; ?>

  <?php if (!empty($itinSource)): ?>
    <section class="mode-section" id="depuis-paris">
      <h2>Itinéraires depuis Paris</h2>
      <div class="mode-table-wrap">
        <table class="mode-table">
          <thead>
            <tr><th>Depuis</th><th>Durée</th><th>Trajet</th></tr>
          </thead>
          <tbody>
            <?php foreach ($itinSource as $i): ?>
              <tr>
                <td>
                  <?php if (!empty($i['station_slug'])): ?>
                    <a href="/metro/station/<?= Template::e($i['station_slug']) ?>/"><strong><?= Template::e($i['depart']) ?></strong></a>
                  <?php else: ?>
                    <strong><?= Template::e($i['depart']) ?></strong>
                  <?php endif; ?>
                </td>
                <td><?= Template::e($i['duration']) ?></td>
                <td><?= bp_interpolate_fares((string)($i['trajet'] ?? '')) ?></td>
              </tr>
            <?php endforeach; ?>
          </tbody>
        </table>
      </div>
    </section>
  <?php endif; ?>

  <?php if (!empty($pois)): ?>
    <section class="mode-section" id="pois">
      <h2>Stations / arrêts / terminaux</h2>
      <ul class="pois-list">
        <?php foreach ($pois as $poi): ?>
          <li>
            <strong><?= Template::e($poi['name']) ?></strong>
            <?php if (!empty($poi['description'])): ?>
              <p><?= $poi['description'] ?></p>
            <?php endif; ?>
          </li>
        <?php endforeach; ?>
      </ul>
    </section>
  <?php endif; ?>

  <?php if (!empty($faq)): ?>
    <section class="mode-section" id="faq">
      <h2>FAQ — <?= Template::e($modeLabel) ?> <?= Template::e($aeroName) ?></h2>
      <div class="faq-list">
        <?php foreach ($faq as $q): ?>
          <details class="faq-item">
            <summary><h3 class="faq-question__title"><?= Template::e($q['question'] ?? '') ?></h3></summary>
            <div class="faq-answer"><?= bp_interpolate_fares((string)($q['answer'] ?? '')) ?></div>
          </details>
        <?php endforeach; ?>
      </div>
    </section>
    <script type="application/ld+json">
    <?php
    $_faqMain = [];
    foreach ($faq as $q) {
      $_faqMain[] = [
        '@type' => 'Question',
        'name'  => $q['question'] ?? '',
        'acceptedAnswer' => [
          '@type' => 'Answer',
          'text'  => trim(strip_tags(bp_interpolate_fares((string)($q['answer'] ?? '')))),
        ],
      ];
    }
    echo json_encode([
      '@context' => 'https://schema.org',
      '@type'    => 'FAQPage',
      'mainEntity' => $_faqMain,
    ], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT);
    ?>
    </script>
  <?php endif; ?>

  <?php
    // JSON-LD Article — éligible Discover. dateModified = filemtime du JSON
    // source (fraîcheur Discover-compatible, mis à jour automatiquement à
    // chaque modification du contenu).
    $_modeFile = __DIR__ . '/../../data/aeroports/' . $aeroSlug . '/' . $modeSlug . '.json';
    if (!is_file($_modeFile)) {
        $_modeFile = __DIR__ . '/../../data/aeroports/' . $aeroSlug . '/bus/' . $modeSlug . '.json';
    }
    $_modeMtime = is_file($_modeFile) ? (int)filemtime($_modeFile) : time();
    $_dateModified = date('c', $_modeMtime);
    $_datePublished = $mode['date_published'] ?? $_dateModified;
    $_articleSchema = [
      '@context'      => 'https://schema.org',
      '@type'         => 'Article',
      'headline'      => bp_interpolate_fares($mode['h1'] ?? ($modeLabel . ' aéroport ' . $aeroName)),
      'description'   => bp_interpolate_fares((string)($mode['seo']['description'] ?? '')),
      'url'           => 'https://bougeaparis.fr' . $canonical,
      'datePublished' => $_datePublished,
      'dateModified'  => $_dateModified,
      'author'        => ['@type' => 'Organization', 'name' => 'BougeaParis.fr'],
      'publisher'     => ['@type' => 'Organization', 'name' => 'BougeaParis.fr', 'url' => 'https://bougeaparis.fr'],
    ];
  ?>
  <script type="application/ld+json"><?= json_encode($_articleSchema, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT) ?></script>

  <?php if (!empty($otherModes)):
    $modeIconDir = __DIR__ . '/../../assets/icons/transport-modes/';
  ?>
    <section class="aeroport-mode-other-modes" id="autres-modes">
      <h2>Aller à l'aéroport <?= Template::e($aeroName) ?> autrement</h2>
      <div class="modes-grid">
        <?php foreach ($otherModes as $m):
          $mSlug  = $m['slug'] ?? '';
          $mType  = $m['type'] ?? 'metro';
          $mUrl   = '/aeroports/' . $aeroSlug . '/' . $mSlug . '/';
          $icoFp  = $modeIconDir . $mType . '.svg';
          $icoSvg = is_file($icoFp) ? file_get_contents($icoFp) : '';
        ?>
          <a href="<?= Template::e($mUrl) ?>" class="mode-card mode-card--<?= Template::e($mType) ?>">
            <div class="mode-card__icon"><?= $icoSvg ?></div>
            <div class="mode-card__title"><?= Template::e($m['name'] ?? '') ?></div>
            <div class="mode-card__details">
              <span class="mode-card__time"><?= Template::e($m['duration'] ?? '') ?></span>
              <span class="mode-card__price"><?= Template::e($m['price'] ?? '') ?></span>
            </div>
            <?php if (!empty($m['note'])): ?>
              <p class="mode-card__note"><?= Template::e($m['note']) ?></p>
            <?php endif; ?>
            <span class="mode-card__cta">Voir le guide →</span>
          </a>
        <?php endforeach; ?>
      </div>
      <p class="back-to-hub">
        <a href="/aeroports/<?= Template::e($aeroSlug) ?>/">
          ← Retour au guide complet <?= Template::e($aeroName) ?>
        </a>
      </p>
    </section>
  <?php endif; ?>

  <?php $tpl->partial('ads/slot-footer'); ?>

</article>
</div>

<style>
.aeroport-mode-page { padding: 1.5rem 0; }
.aeroport-mode-page h2 { margin-top: 2rem; color: #0F6E56; }

/*
 * Mode hero — palette éditoriale BougeaParis, non identique aux chartes
 * officielles IDFM/RATP/SNCF (à l'exception du T7 jaune #FFCD00 qui est la
 * couleur officielle Tramway IDFM).
 * Pour les pastilles de correspondance officielles : voir .line-badge--*
 * (helper pastilleCorresp dans helpers.php).
 *
 * Couleurs sélectionnées via data-mode-slug. Voile sombre uniforme 30%
 * pour garantir le contraste WCAG AA sur tous les fonds, sauf T7 (jaune
 * trop clair) qui bascule en texte sombre.
 */
.mode-hero {
  background-color: #0F6E56; /* fallback BougeaParis */
  background-image: linear-gradient(rgba(0,0,0,.30), rgba(0,0,0,.30));
  color: #fff;
  padding: 2rem 1.5rem;
  border-radius: 12px;
  margin-bottom: 1.5rem;
}
.mode-hero h1 {
  color: #fff;
  margin: 0 0 .5rem;
  font-size: clamp(1.5rem, 3.5vw, 2rem);
  line-height: 1.25;
  text-shadow: 0 1px 2px rgba(0,0,0,.25);
}
.mode-tagline {
  font-size: 1.05rem;
  margin: 0 0 1rem;
  font-weight: 600;
  color: #fff;
}
.mode-quick-facts {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 1rem;
}
.mode-fact {
  background: rgba(0,0,0,.5);   /* fond assombri → contraste AA garanti */
  padding: .75rem 1rem;
  border-radius: 8px;
  min-width: 110px;
  text-align: center;
}
.fact-value { display: block; font-weight: 700; font-size: 1.3rem; line-height: 1; color: #fff; }
.fact-label { display: block; font-size: .8rem; margin-top: .25rem; color: #fff; font-weight: 500; }

/* Mapping data-mode-slug → couleur (palette éditoriale BougeaParis) */
.mode-hero[data-mode-slug="rer-b"]      { background-color: #0064B0; }
.mode-hero[data-mode-slug="rer"]        { background-color: #0064B0; }
.mode-hero[data-mode-slug="metro"]      { background-color: #7C4E9B; }
.mode-hero[data-mode-slug="tramway"]    { background-color: #FFCD00; } /* T7 jaune officiel IDFM */
.mode-hero[data-mode-slug="bus"]        { background-color: #E5B100; }
.mode-hero[data-mode-slug="bus-183"]    { background-color: #2980B9; }
.mode-hero[data-mode-slug="bus-285"]    { background-color: #2980B9; }
.mode-hero[data-mode-slug="orlybus"]    { background-color: #E67E22; }
.mode-hero[data-mode-slug="roissybus"]  { background-color: #9A9A9A; }
.mode-hero[data-mode-slug="tgv"]        { background-color: #C61E4D; }
.mode-hero[data-mode-slug="cdgval"]     { background-color: #007AB7; }
.mode-hero[data-mode-slug="navette"]    { background-color: #9A4DD0; }
.mode-hero[data-mode-slug="train"]      { background-color: #D02D2D; }
.mode-hero[data-mode-slug="taxi"]       { background-color: #222222; }

/* Cas particulier T7 : jaune officiel trop clair pour texte blanc.
   H1 et tagline en sombre, ratio AA 5.70 sur fond jaune+voile 30%.
   Les fact-cards (fond rgba(0,0,0,.5)) gardent leur texte blanc. */
.mode-hero[data-mode-slug="tramway"] h1 {
  color: #1a1a1a;
  text-shadow: none;
}
.mode-hero[data-mode-slug="tramway"] .mode-tagline {
  color: #1a1a1a;
}
.mode-section { margin: 2rem 0; }
.mode-section p { line-height: 1.65; }
.mode-table-wrap { overflow-x: auto; margin-top: 1rem; }
.mode-table { width: 100%; border-collapse: collapse; }
.mode-table th, .mode-table td { padding: .6rem .8rem; border-bottom: 1px solid #ddd; text-align: left; }
.mode-table th { background: #f4f8f6; color: #0F6E56; font-weight: 600; }
.mode-steps { padding-left: 1.5rem; }
.mode-steps li { margin-bottom: .5rem; line-height: 1.6; }
.pois-list, .alt-list { list-style: none; padding: 0; }
.pois-list li, .alt-list li { background: #f4f8f6; padding: .75rem 1rem; border-radius: 8px; margin-bottom: .5rem; }
.faq-list { margin-top: 1rem; }
.faq-item { background: #f4f8f6; padding: .75rem 1rem; border-radius: 8px; margin-bottom: .5rem; }
.faq-item summary { cursor: pointer; list-style: none; }
.faq-item summary::-webkit-details-marker { display: none; }
.faq-question__title { display: inline; margin: 0; font-size: 1rem; font-weight: 600; color: #1a1a1a; }
.faq-answer { margin-top: .5rem; line-height: 1.6; color: #444; }
.faq-answer p:first-child { margin-top: 0; }
.back-link { font-weight: 600; color: #0F6E56; }

/* Section "Aller à l'aéroport X autrement" — maillage interne */
.aeroport-mode-other-modes { margin: 3rem 0 2rem; padding-top: 2rem; border-top: 2px solid #E1F5EE; }
.aeroport-mode-other-modes h2 { color: #0F6E56; margin: 0 0 1.5rem; font-size: clamp(1.3rem, 2.5vw, 1.6rem); }
.modes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}
.mode-card {
  display: flex; flex-direction: column;
  background: #fff;
  border: 2px solid transparent;
  border-radius: 12px;
  padding: 1.25rem;
  text-decoration: none;
  color: inherit;
  transition: transform .2s ease, border-color .2s ease, box-shadow .2s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,.05);
}
.mode-card:hover { border-color: var(--card-color, #0F6E56); transform: translateY(-2px); box-shadow: 0 6px 16px rgba(0,0,0,.1); }
.mode-card__icon { width: 48px; height: 48px; color: var(--card-color, #0F6E56); margin-bottom: .75rem; }
.mode-card__icon svg { width: 100%; height: 100%; display: block; }
.mode-card--metro   { --card-color: #0F6E56; }
.mode-card--bus     { --card-color: #E67E22; }
.mode-card--rer     { --card-color: #2980B9; }
.mode-card--tramway { --card-color: #27AE60; }
.mode-card--taxi    { --card-color: #C9A227; }
.mode-card--navette { --card-color: #8E44AD; }
.mode-card--train   { --card-color: #C0392B; }
.mode-card__title { margin: 0 0 .5rem; font-size: 1.1rem; color: var(--card-color); }
.mode-card__details { display: flex; flex-direction: column; gap: .15rem; margin-bottom: .5rem; }
.mode-card__time { font-weight: 700; font-size: 1.05rem; }
.mode-card__price { color: #555; font-size: .95rem; }
.mode-card__note { font-size: .85rem; color: #777; margin: .25rem 0 .75rem; flex: 1; }
.mode-card__cta { display: inline-block; font-weight: 600; color: var(--card-color); font-size: .9rem; margin-top: auto; }
.back-to-hub { text-align: center; margin-top: 2rem; }
.back-to-hub a {
  display: inline-block;
  color: #0F6E56;
  text-decoration: none;
  font-weight: 600;
  padding: .6rem 1.2rem;
  border: 1px solid #0F6E56;
  border-radius: 8px;
  transition: background .2s, color .2s;
}
.back-to-hub a:hover { background: #0F6E56; color: #fff; }
@media (max-width: 768px) {
  .modes-grid { grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: .75rem; }
  .mode-card { padding: 1rem; }
  .mode-card__icon { width: 40px; height: 40px; }
}

/* Info-cards Tarifs — refactor table → cards horizontales */
.info-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: .75rem;
  margin: 1rem 0;
}
.info-card {
  display: flex; gap: 1rem; align-items: center;
  background: #f4f8f6;
  border-left: 4px solid var(--info-color, #0F6E56);
  border-radius: 8px;
  padding: 1rem 1.25rem;
}
.info-card__icon {
  flex-shrink: 0; width: 48px; height: 48px;
  color: var(--info-color, #0F6E56);
}
.info-card__icon svg { width: 100%; height: 100%; display: block; }
.info-card__content { flex: 1; min-width: 0; }
.info-card__title {
  margin: 0 0 .25rem;
  font-size: 1rem;
  color: var(--info-color, #0F6E56);
  font-weight: 600;
}
.info-card__body { display: flex; flex-wrap: wrap; gap: .25rem 1rem; align-items: baseline; }
.info-card__price {
  font-size: 1.25rem; font-weight: 700;
  color: var(--info-color, #0F6E56);
}
.info-card__details { color: #555; font-size: .92rem; }
.info-card--metro   { --info-color: #0F6E56; }
.info-card--bus     { --info-color: #E67E22; }
.info-card--rer     { --info-color: #2980B9; }
.info-card--tramway { --info-color: #27AE60; }
.info-card--taxi    { --info-color: #C9A227; }
.info-card--navette { --info-color: #8E44AD; }
.info-card--train   { --info-color: #C0392B; }
@media (max-width: 768px) {
  .info-card {
    flex-direction: column; text-align: center; align-items: stretch;
    padding: 1rem;
  }
  .info-card__icon { width: 40px; height: 40px; margin: 0 auto; }
  .info-card__body { justify-content: center; }
}

/* Cards bus_lines — anchor text SEO direct */
.bus-lines-section { margin: 3rem 0; }
.bus-lines-section h2 { color: #0F6E56; margin: 0 0 1rem; }
.bus-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.25rem;
  margin: 1.5rem 0;
}
.bus-card {
  display: flex; flex-direction: column;
  background: #fff;
  border: 2px solid #E1F5EE;
  border-radius: 12px;
  padding: 1.5rem;
  text-decoration: none;
  color: inherit;
  transition: transform .3s ease, border-color .3s ease, box-shadow .3s ease;
}
.bus-card--express { border-color: #E67E22; }
.bus-card--express:hover { border-color: #ba6519; transform: translateY(-3px); box-shadow: 0 10px 20px rgba(230,126,34,.15); }
.bus-card--regulier { border-color: #2980B9; }
.bus-card--regulier:hover { border-color: #1f618d; transform: translateY(-3px); box-shadow: 0 10px 20px rgba(41,128,185,.15); }
.bus-card__icon { width: 48px; height: 48px; margin-bottom: .75rem; }
.bus-card--express .bus-card__icon { color: #E67E22; }
.bus-card--regulier .bus-card__icon { color: #2980B9; }
.bus-card__icon svg { width: 100%; height: 100%; display: block; }
.bus-card__name { margin: 0 0 .5rem; color: #1a1a1a; font-size: 1.25rem; font-weight: 700; }
.bus-card__route { margin: 0 0 1rem; color: #555; font-size: .95rem; line-height: 1.4; }
.bus-card__metrics { margin: 0 0 .75rem; font-size: 1rem; font-weight: 600; }
.bus-card__duration { color: #1a1a1a; }
.bus-card__separator { margin: 0 .5rem; color: #999; }
.bus-card__price { color: #0F6E56; font-weight: 700; }
.bus-card__note { margin: 0 0 1rem; color: #777; font-size: .85rem; flex-grow: 1; }
.bus-card__cta {
  margin-top: auto; font-weight: 600; font-size: 1rem;
  padding-top: .5rem; border-top: 1px solid #f0f0f0;
}
.bus-card--express .bus-card__cta { color: #E67E22; }
.bus-card--regulier .bus-card__cta { color: #2980B9; }
.bus-card--noctilien { border-color: #6A4F9C; }
.bus-card--noctilien:hover { border-color: #4f3a78; transform: translateY(-3px); box-shadow: 0 10px 20px rgba(106,79,156,.15); }
.bus-card--noctilien .bus-card__icon { color: #6A4F9C; }
.bus-card--noctilien .bus-card__cta { color: #6A4F9C; }

/* Variant historique (service supprimé) — visuellement grisé mais cliquable */
.bus-card--historique {
  border-color: #B0B0B0;
  background: #f8f8f8;
  position: relative;
  padding-top: 2.5rem;
}
.bus-card--historique:hover { border-color: #7a7a7a; transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,.08); }
.bus-card--historique .bus-card__icon { color: #7a7a7a; }
.bus-card--historique .bus-card__name { color: #555; text-decoration: line-through; text-decoration-color: #B0B0B0; text-decoration-thickness: 1.5px; }
.bus-card--historique .bus-card__cta { color: #555; }
.bus-card__status-badge {
  position: absolute; top: .85rem; left: .85rem;
  background: #C0392B; color: #fff;
  padding: .25rem .6rem;
  border-radius: 4px;
  font-size: .72rem; font-weight: 700;
  letter-spacing: .3px;
  text-transform: uppercase;
}

/* État inactive (conditionalLink : URL future) */
.bus-card--inactive { cursor: default; opacity: .82; }
.bus-card--inactive:hover { transform: none; box-shadow: none; }
.bus-card--inactive .bus-card__cta::after { content: " (à venir)"; color: #999; font-weight: 400; font-size: .85rem; }

/* Status banner (Discover-eligible alerte service supprimé) */
.status-banner {
  margin: 1rem 0 1.5rem;
  padding: 1rem 1.25rem;
  border-radius: 8px;
  font-size: .95rem;
  line-height: 1.55;
}
.status-banner--discontinued {
  background: #fdecea;
  border-left: 4px solid #C0392B;
  color: #6a1c14;
}
.status-banner--discontinued strong { color: #C0392B; }

/* Bloc alternatives mis en avant (avant historique) */
.alt-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}
.alt-card {
  display: block;
  background: #fff;
  border: 2px solid #E1F5EE;
  border-radius: 10px;
  padding: 1.1rem 1.25rem;
  text-decoration: none;
  color: inherit;
  transition: border-color .2s, box-shadow .2s, transform .2s;
}
.alt-card:hover {
  border-color: #0F6E56;
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(15,110,86,.1);
}
.alt-card--inactive { opacity: .85; cursor: default; }
.alt-card--inactive:hover { transform: none; box-shadow: none; border-color: #c8d6cf; }
.alt-card__anchor {
  display: inline-block;
  font-weight: 700;
  color: #0F6E56;
  font-size: 1.05rem;
  margin-bottom: .35rem;
}
.alt-card--inactive .alt-card__anchor::after {
  content: " (à venir)"; color: #999; font-weight: 400; font-size: .85rem;
}
.alt-card__summary { margin: 0; color: #444; font-size: .92rem; line-height: 1.5; }

/* Note tarifs sous la table (lien interne optionnel via conditionalLink) */
.tarifs-table-note {
  margin: 1rem 0 .5rem;
  padding: .75rem 1rem;
  background: #f4f8f6;
  border-left: 3px solid #0F6E56;
  border-radius: 4px;
  font-size: .9rem;
  color: #444;
}
.tarifs-table-note__link { color: #0F6E56; font-weight: 600; }
.tarifs-table-note__link--inactive { color: #777; }

/* Bouton de téléchargement plan ligne (sous carte Leaflet) */
.line-download-row {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: .5rem;
  margin: 1rem 0 2rem;
  padding: 1rem;
  background: #F8FBFA;
  border: 1px solid #E1F5EE;
  border-radius: 8px;
}
.line-download-btn {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  padding: .6rem 1rem;
  background: #fff;
  color: #0F6E56;
  border: 1px solid #0F6E56;
  border-radius: 6px;
  text-decoration: none;
  font-size: .95rem;
  font-weight: 600;
  transition: background .2s, color .2s;
}
.line-download-btn:hover { background: #0F6E56; color: #fff; }
.line-download-meta { color: #777; font-size: .85rem; }

/* Itinerary steps — cards visuelles préservant sémantique <ol>/<li> */
.itinerary-steps { list-style: none; padding: 0; margin: 1rem 0 0; }
.step-card {
  display: grid;
  grid-template-columns: 48px 56px 1fr;
  gap: 1rem;
  align-items: center;
  padding: 1rem 1.25rem;
  background: #fff;
  border: 1px solid #E1F5EE;
  border-radius: 10px;
  margin-bottom: 1.25rem;
  position: relative;
  transition: border-color .2s, box-shadow .2s;
}
.step-card:hover { border-color: #0F6E56; box-shadow: 0 4px 12px rgba(15,110,86,.08); }
/* Connecteur flèche entre étapes */
.step-card:not(:last-child)::after {
  content: '';
  position: absolute;
  bottom: -.85rem;
  left: 24px;
  width: 0; height: 0;
  border-left: 7px solid transparent;
  border-right: 7px solid transparent;
  border-top: 10px solid #C8E5DA;
  z-index: 1;
}
.step-card__number {
  width: 44px; height: 44px; border-radius: 50%;
  background: #0F6E56; color: #fff;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.15rem; font-weight: 700;
  flex-shrink: 0;
}
.step-card__icon {
  display: flex; align-items: center; justify-content: center;
}
.line-badge {
  display: inline-flex; align-items: center; justify-content: center;
  min-width: 48px; height: 44px; padding: 0 .5rem;
  border-radius: 22px;
  font-weight: 700; font-size: .9rem;
  color: #fff; background: #0F6E56;
  white-space: nowrap;
}
.step-icon {
  width: 44px; height: 44px; border-radius: 50%;
  background: #F4F8F6; color: #0F6E56;
  display: flex; align-items: center; justify-content: center;
}
.step-icon svg { width: 22px; height: 22px; }
.step-icon--alight   { background: #E1F5EE; color: #0F6E56; }
.step-icon--walk     { background: #FEF5E1; color: #C9A227; }
.step-icon--transfer { background: #D6EAF8; color: #2980B9; }
.step-card__content { font-size: .95rem; line-height: 1.55; color: #1a1a1a; }
.step-card__content strong { font-weight: 700; color: #0F6E56; }

/* Couleurs officielles RATP/SNCF */
.line-badge--m1  { background: #FFCD00; color: #1a1a1a; }
.line-badge--m2  { background: #003CA6; }
.line-badge--m3  { background: #837902; }
.line-badge--m3bis,.line-badge--m3b { background: #6EC4E8; }
.line-badge--m4  { background: #CF009E; }
.line-badge--m5  { background: #FF7E2E; }
.line-badge--m6  { background: #6ECA97; }
.line-badge--m7  { background: #FA9ABA; color: #1a1a1a; }
.line-badge--m7bis,.line-badge--m7b { background: #6ECA97; }
.line-badge--m8  { background: #E19BDF; color: #1a1a1a; }
.line-badge--m9  { background: #B6BD00; color: #1a1a1a; }
.line-badge--m10 { background: #C9910D; }
.line-badge--m11 { background: #704B1C; }
.line-badge--m12 { background: #007852; }
.line-badge--m13 { background: #6EC4E8; }
.line-badge--m14 { background: #62259D; }
.line-badge--rer-a { background: #E2231A; }
.line-badge--rer-b { background: #5291CE; }
.line-badge--rer-c { background: #F3D006; color: #1a1a1a; }
.line-badge--rer-d { background: #007E49; }
.line-badge--rer-e { background: #C28FC4; }
.line-badge--t1,.line-badge--t2,.line-badge--t3,.line-badge--t4,.line-badge--t5,.line-badge--t6,
.line-badge--t7,.line-badge--t8,.line-badge--t9,.line-badge--t10,.line-badge--t11,.line-badge--t12,.line-badge--t13 { background: #00643C; }
.line-badge--t7  { background: #FFCD00; color: #1a1a1a; }
.line-badge--orlybus,.line-badge--roissybus { background: #E67E22; }
.line-badge--orlyval,.line-badge--cdgval { background: #007AB7; }
.line-badge--tgv { background: #C61E4D; }
.line-badge--taxi { background: #2C2C2C; }
.line-badge--bus,
.line-badge--bus-183,.line-badge--bus-285,.line-badge--bus-350,.line-badge--bus-351 { background: #E5B100; color: #1a1a1a; }

@media (max-width: 640px) {
  .step-card { grid-template-columns: 38px 48px 1fr; gap: .75rem; padding: .85rem 1rem; }
  .step-card__number { width: 36px; height: 36px; font-size: 1rem; }
  .line-badge, .step-icon { min-width: 40px; width: 40px; height: 40px; font-size: .85rem; }
  .step-card__content { font-size: .9rem; }
}
</style>
