<?php
/**
 * Template : page détail aéroport (CDG, Orly, Beauvais).
 * Props attendues : $aeroport (array décodé depuis data/aeroports/{slug}.json).
 *
 * Sections SEO-driven : H1 explicite + H2 par mode de transport
 * (alignés sur les intentions de recherche GKP).
 */
$aeroport = $aeroport ?? $props['aeroport'] ?? [];
$slug      = $aeroport['slug']      ?? 'aeroport';
$name      = $aeroport['name']      ?? 'Aéroport';
$full      = $aeroport['full_name'] ?? $name;
$iata      = $aeroport['iata']      ?? '';
$dept      = $aeroport['department']?? '';
$dist      = $aeroport['distance_paris_km'] ?? null;
$traffic   = $aeroport['annual_traffic'] ?? '';
$opened    = $aeroport['opened']    ?? '';
$operator  = $aeroport['operator']  ?? '';
$terminals = $aeroport['terminals'] ?? [];
$h1        = $aeroport['h1'] ?? ("Aéroport " . $name . ($iata ? " (" . $iata . ")" : "") . " : guide d'accès complet");
$tagline   = $aeroport['hero']['tagline'] ?? '';
$heroDesc  = $aeroport['hero']['description'] ?? '';
$intros    = $aeroport['intro_paragraphs'] ?? [];
$sections  = $aeroport['sections'] ?? [];
$history   = $aeroport['history'] ?? [];
$faq       = $aeroport['faq'] ?? [];
$pois      = $aeroport['nearby_pois'] ?? [];
$heroImg   = $aeroport['hero_image'] ?? null;
$accessModes = $aeroport['access_modes'] ?? [];

$canonical = '/aeroports/' . $slug . '/';

$tpl->seo
    ->setTitle(bp_title_aeroport_hub($name, $iata), false)
    ->setDescription($aeroport['seo']['description'] ?? '')
    ->setCanonical($canonical)
    ->setBreadcrumb([
        ['label' => 'Accueil',    'url' => '/'],
        ['label' => 'Aéroports',  'url' => '/aeroports/'],
        ['label' => $name,        'url' => $canonical],
    ]);

// Build picture sources for hero
$localVersions = $heroImg['local_versions'] ?? null;
$buildSrcset = function(array $map): string {
    $parts = [];
    foreach ($map as $w => $url) {
        $parts[] = htmlspecialchars($url, ENT_QUOTES, 'UTF-8') . ' ' . (int)$w . 'w';
    }
    return implode(', ', $parts);
};
?>

<?php $tpl->partial('components/breadcrumb', ['items' => [
    ['label' => 'Accueil',    'url' => '/'],
    ['label' => 'Aéroports',  'url' => '/aeroports/'],
    ['label' => $name,        'url' => $canonical],
]]); ?>

<div class="container">
<article class="aeroport-page">

  <!-- HERO avec image Wikimedia + H1 SEO -->
  <section class="aeroport-hero">
    <?php if ($heroImg && !empty($heroImg['url'])): ?>
      <div class="aeroport-hero__image">
        <?php if (is_array($localVersions) && !empty($localVersions['avif'])): ?>
          <picture>
            <source type="image/avif" srcset="<?= $buildSrcset($localVersions['avif']) ?>" sizes="(max-width: 768px) 100vw, 1200px">
            <source type="image/webp" srcset="<?= $buildSrcset($localVersions['webp']) ?>" sizes="(max-width: 768px) 100vw, 1200px">
            <img src="<?= Template::e($localVersions['jpg'][1200] ?? reset($localVersions['jpg'])) ?>"
                 srcset="<?= $buildSrcset($localVersions['jpg']) ?>"
                 sizes="(max-width: 768px) 100vw, 1200px"
                 alt="<?= Template::e($heroImg['alt'] ?? $name) ?>"
                 width="1200" height="675"
                 loading="eager" fetchpriority="high">
          </picture>
        <?php else: ?>
          <img src="<?= Template::e($heroImg['url']) ?>"
               alt="<?= Template::e($heroImg['alt'] ?? $name) ?>"
               width="1200" height="675"
               loading="eager" fetchpriority="high">
        <?php endif; ?>
      </div>
    <?php endif; ?>

    <div class="aeroport-hero__content">
      <h1><?= Template::e($h1) ?></h1>
      <?php if ($tagline): ?>
        <p class="aeroport-tagline"><?= Template::e($tagline) ?></p>
      <?php endif; ?>
      <p class="aeroport-hero-desc"><?= $heroDesc ?></p>

      <div class="aeroport-key-figures">
        <?php if ($dist): ?>
          <div class="key-figure"><span class="kf-value"><?= (int)$dist ?> km</span><span class="kf-label">de Paris</span></div>
        <?php endif; ?>
        <?php if ($traffic): ?>
          <div class="key-figure"><span class="kf-value"><?= Template::e($traffic) ?></span><span class="kf-label">passagers/an</span></div>
        <?php endif; ?>
        <?php if (!empty($terminals)): ?>
          <div class="key-figure"><span class="kf-value"><?= count($terminals) ?></span><span class="kf-label">terminaux</span></div>
        <?php endif; ?>
        <?php if ($opened): ?>
          <div class="key-figure"><span class="kf-value"><?= Template::e($opened) ?></span><span class="kf-label">ouverture</span></div>
        <?php endif; ?>
      </div>
    </div>
  </section>

  <?php $tpl->partial('ads/slot-header'); ?>

  <?php if (!empty($intros)): ?>
    <section class="aeroport-intro">
      <?php foreach ($intros as $p): ?>
        <p><?= $p ?></p>
      <?php endforeach; ?>
    </section>
  <?php endif; ?>

  <?php
    // Cards modes d'accès — refonte UX : grille visuelle cliquable
    $modeIconDir = __DIR__ . '/../../assets/icons/transport-modes/';
  ?>
  <?php if (!empty($accessModes)): ?>
    <section class="aeroport-modes-grid">
      <h2>Tous les modes d'accès à <?= Template::e($name) ?></h2>
      <div class="modes-grid">
        <?php foreach ($accessModes as $mode):
          $modeSlug = $mode['slug'] ?? '';
          $modeType = $mode['type'] ?? 'metro';
          $modeUrl  = '/aeroports/' . $slug . '/' . $modeSlug . '/';
          // Mapping vers SVG existants (bus-express réutilise bus.svg)
          $iconMap  = ['bus-express' => 'bus'];
          $iconKey  = $iconMap[$modeType] ?? $modeType;
          $iconPath = $modeIconDir . $iconKey . '.svg';
          $iconSvg  = is_file($iconPath) ? file_get_contents($iconPath) : '';
        ?>
          <a href="<?= Template::e($modeUrl) ?>" class="mode-card mode-card--<?= Template::e($modeType) ?>">
            <div class="mode-card__icon"><?= $iconSvg ?></div>
            <div class="mode-card__title"><?= Template::e($mode['name'] ?? '') ?></div>
            <div class="mode-card__details">
              <span class="mode-card__time"><?= Template::e($mode['duration'] ?? '') ?></span>
              <span class="mode-card__price"><?= Template::e($mode['price'] ?? '') ?></span>
            </div>
            <?php if (!empty($mode['note'])): ?>
              <p class="mode-card__note"><?= Template::e($mode['note']) ?></p>
            <?php endif; ?>
            <span class="mode-card__cta">→ <?= Template::e($mode['cta_anchor'] ?? $mode['name'] ?? 'Voir le guide') ?></span>
          </a>
        <?php endforeach; ?>
      </div>
    </section>
  <?php endif; ?>

  <?php $tpl->partial('ads/slot-in-article'); ?>

  <!-- Sections H2 SEO-driven (modes de transport) -->
  <?php foreach ($sections as $section): ?>
    <section class="aeroport-section" <?php if (!empty($section['anchor'])): ?>id="<?= Template::e($section['anchor']) ?>"<?php endif; ?>>
      <h2><?= Template::e($section['h2'] ?? '') ?></h2>

      <?php if (!empty($section['paragraphs'])): ?>
        <?php foreach ($section['paragraphs'] as $p): ?>
          <p><?= $p ?></p>
        <?php endforeach; ?>
      <?php endif; ?>

      <?php if (!empty($section['table'])): ?>
        <div class="aeroport-table-wrap">
          <table class="aeroport-table">
            <thead>
              <tr>
                <?php foreach ($section['table']['headers'] as $h): ?>
                  <th><?= Template::e($h) ?></th>
                <?php endforeach; ?>
              </tr>
            </thead>
            <tbody>
              <?php foreach ($section['table']['rows'] as $row): ?>
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
  <?php endforeach; ?>

  <?php if (!empty($history)): ?>
    <section class="aeroport-section" id="histoire">
      <h2>Histoire de <?= Template::e($full) ?></h2>
      <?php foreach ($history as $p): ?>
        <p><?= $p ?></p>
      <?php endforeach; ?>
    </section>
  <?php endif; ?>

  <?php if (!empty($pois)): ?>
    <section class="aeroport-section" id="proximite">
      <h2>À proximité de <?= Template::e($name) ?></h2>
      <ul class="pois-list">
        <?php foreach ($pois as $poi): ?>
          <li>
            <strong><?= Template::e($poi['name'] ?? '') ?></strong>
            <?php if (!empty($poi['distance_km'])): ?>
              <span class="poi-distance">(~<?= (int)$poi['distance_km'] ?> km)</span>
            <?php endif; ?>
            <p><?= $poi['description'] ?? '' ?></p>
          </li>
        <?php endforeach; ?>
      </ul>
    </section>
  <?php endif; ?>

  <?php if (!empty($faq)): ?>
    <section class="aeroport-section" id="faq">
      <h2>FAQ — <?= Template::e($name) ?></h2>
      <div class="faq-list">
        <?php foreach ($faq as $q): ?>
          <details class="faq-item">
            <summary><h3 class="faq-question__title"><?= Template::e($q['question'] ?? '') ?></h3></summary>
            <div class="faq-answer"><?= $q['answer'] ?? '' ?></div>
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
          'text'  => trim(strip_tags($q['answer'] ?? '')),
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

  <section class="aeroport-section aeroport-meta">
    <dl class="aeroport-summary">
      <dt>Nom officiel</dt><dd><?= Template::e($full) ?></dd>
      <?php if ($iata): ?><dt>Code IATA</dt><dd><?= Template::e($iata) ?></dd><?php endif; ?>
      <?php if (!empty($aeroport['icao'])): ?><dt>Code ICAO</dt><dd><?= Template::e($aeroport['icao']) ?></dd><?php endif; ?>
      <?php if ($dept): ?><dt>Département</dt><dd><?= Template::e($dept) ?></dd><?php endif; ?>
      <?php if ($operator): ?><dt>Opérateur</dt><dd><?= Template::e($operator) ?></dd><?php endif; ?>
      <?php if ($opened): ?><dt>Ouverture</dt><dd><?= Template::e($opened) ?></dd><?php endif; ?>
    </dl>
    <?php if (!empty($heroImg['credit'])): ?>
      <p class="aeroport-credit-link">
        Crédits photo et sources des données : <a href="/sources/#credits-photos">voir la page Sources</a>.
      </p>
    <?php endif; ?>
  </section>

  <?php $tpl->partial('ads/slot-footer'); ?>

</article>
</div>

<style>
.aeroport-page { padding: 1.5rem 0; }
.aeroport-page h2 { margin-top: 2rem; color: #0F6E56; }
.aeroport-hero { margin-bottom: 1.5rem; border-radius: 12px; overflow: hidden; background: #0F6E56; color: #fff; }
.aeroport-hero__image img,
.aeroport-hero__image picture img { display: block; width: 100%; height: auto; max-height: 400px; aspect-ratio: 16/9; object-fit: cover; }
@media (max-width: 768px) {
  .aeroport-hero__image img,
  .aeroport-hero__image picture img { max-height: 250px; }
}
.aeroport-hero__content { padding: 1.5rem; }
.aeroport-hero h1 { color: #fff; margin: 0 0 .5rem; font-size: clamp(1.5rem, 3.5vw, 2rem); line-height: 1.25; }
.aeroport-tagline { font-size: 1.05rem; opacity: .95; margin: 0 0 1rem; font-weight: 600; }
.aeroport-hero-desc { line-height: 1.6; margin-bottom: 1.5rem; }
.aeroport-hero-desc strong { color: #fff; }
.aeroport-key-figures { display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 1rem; }
.key-figure { background: rgba(255,255,255,.15); padding: .75rem 1rem; border-radius: 8px; min-width: 110px; text-align: center; }
.kf-value { display: block; font-weight: 700; font-size: 1.3rem; line-height: 1; }
.kf-label { display: block; font-size: .8rem; opacity: .85; margin-top: .25rem; }
.aeroport-section { margin: 2rem 0; }
.aeroport-section p { line-height: 1.65; }
.aeroport-table-wrap { overflow-x: auto; margin-top: 1rem; }
.aeroport-table { width: 100%; border-collapse: collapse; }
.aeroport-table th, .aeroport-table td { padding: .6rem .8rem; border-bottom: 1px solid #ddd; text-align: left; }
.aeroport-table th { background: #f4f8f6; color: #0F6E56; font-weight: 600; }
.pois-list { list-style: none; padding: 0; }
.pois-list li { background: #f4f8f6; padding: 1rem; border-radius: 8px; margin-bottom: .75rem; }
.poi-distance { font-size: .85rem; color: #777; margin-left: .5rem; }
.faq-list { margin-top: 1rem; }
.faq-item { background: #f4f8f6; padding: .75rem 1rem; border-radius: 8px; margin-bottom: .5rem; }
.faq-item summary { cursor: pointer; list-style: none; }
.faq-item summary::-webkit-details-marker { display: none; }
.faq-question__title { display: inline; margin: 0; font-size: 1rem; font-weight: 600; color: #1a1a1a; }
.faq-answer { margin-top: .5rem; line-height: 1.6; color: #444; }
.faq-answer p:first-child { margin-top: 0; }
.aeroport-summary { display: grid; grid-template-columns: max-content 1fr; gap: .5rem 1rem; margin-top: 1rem; }
.aeroport-summary dt { font-weight: 600; color: #0F6E56; }
.aeroport-summary dd { margin: 0; }
.aeroport-credit-link { margin-top: 1rem; font-size: .85rem; color: #777; }
.aeroport-credit-link a { color: #0F6E56; }

/* Cards modes d'accès — refonte UX P3 */
.aeroport-modes-grid { margin: 2rem 0; }
.modes-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin: 1.5rem 0;
}
@media (max-width: 900px) {
  .modes-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
  .modes-grid { grid-template-columns: 1fr; }
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
.mode-card:hover {
  border-color: var(--card-color, #0F6E56);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(0,0,0,.1);
}
.mode-card__icon { width: 48px; height: 48px; color: var(--card-color, #0F6E56); margin-bottom: .75rem; }
.mode-card__icon svg { width: 100%; height: 100%; display: block; }
.mode-card--metro       { --card-color: #0F6E56; }
.mode-card--bus         { --card-color: #E67E22; }
.mode-card--bus-express { --card-color: #E67E22; position: relative; border-color: #E67E22; }
.mode-card--bus-express::before {
  content: "★ Populaire";
  position: absolute;
  top: -10px; right: 12px;
  background: #E67E22; color: #fff;
  font-size: .72rem; font-weight: 700;
  padding: .25rem .65rem;
  border-radius: 12px;
  letter-spacing: .5px;
  text-transform: uppercase;
}
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
@media (max-width: 768px) {
  .modes-grid { gap: .75rem; }
  .mode-card { padding: 1rem; }
  .mode-card__icon { width: 40px; height: 40px; }
}
</style>
