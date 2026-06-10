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

$canonical = '/aeroports/' . $slug . '/';

$tpl->seo
    ->setTitle($aeroport['seo']['title'] ?? $name)
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
      <h2>Présentation de l'<?= Template::e($full) ?></h2>
      <?php foreach ($intros as $p): ?>
        <p><?= $p ?></p>
      <?php endforeach; ?>
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
      <h2>Histoire de l'<?= Template::e($full) ?></h2>
      <?php foreach ($history as $p): ?>
        <p><?= $p ?></p>
      <?php endforeach; ?>
    </section>
  <?php endif; ?>

  <?php if (!empty($pois)): ?>
    <section class="aeroport-section" id="proximite">
      <h2>À proximité de l'<?= Template::e($name) ?></h2>
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
            <summary><?= Template::e($q['question'] ?? '') ?></summary>
            <p><?= $q['answer'] ?? '' ?></p>
          </details>
        <?php endforeach; ?>
      </div>
    </section>
  <?php endif; ?>

  <section class="aeroport-section aeroport-meta">
    <h2>En résumé — <?= Template::e($name) ?></h2>
    <dl class="aeroport-summary">
      <dt>Nom officiel</dt><dd><?= Template::e($full) ?></dd>
      <?php if ($iata): ?><dt>Code IATA</dt><dd><?= Template::e($iata) ?></dd><?php endif; ?>
      <?php if (!empty($aeroport['icao'])): ?><dt>Code ICAO</dt><dd><?= Template::e($aeroport['icao']) ?></dd><?php endif; ?>
      <?php if ($dept): ?><dt>Département</dt><dd><?= Template::e($dept) ?></dd><?php endif; ?>
      <?php if ($operator): ?><dt>Opérateur</dt><dd><?= Template::e($operator) ?></dd><?php endif; ?>
      <?php if ($opened): ?><dt>Ouverture</dt><dd><?= Template::e($opened) ?></dd><?php endif; ?>
    </dl>
    <?php if (!empty($heroImg['credit'])): ?>
      <p class="aeroport-credit">
        Photo : <?= Template::e($heroImg['credit']['author'] ?? '') ?> —
        <?= Template::e($heroImg['credit']['license'] ?? '') ?> —
        <?php if (!empty($heroImg['credit']['source_url'])): ?>
          <a href="<?= Template::e($heroImg['credit']['source_url']) ?>" rel="nofollow noopener" target="_blank">source Wikimedia</a>
        <?php endif; ?>
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
.aeroport-hero__image picture img { display: block; width: 100%; height: auto; aspect-ratio: 16/9; object-fit: cover; }
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
.faq-item summary { cursor: pointer; font-weight: 600; }
.faq-item p { margin-top: .5rem; }
.aeroport-summary { display: grid; grid-template-columns: max-content 1fr; gap: .5rem 1rem; margin-top: 1rem; }
.aeroport-summary dt { font-weight: 600; color: #0F6E56; }
.aeroport-summary dd { margin: 0; }
.aeroport-credit { margin-top: 1rem; font-size: .85rem; color: #777; }
</style>
