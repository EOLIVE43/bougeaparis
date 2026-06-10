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
$color     = $mode['color'] ?? '#0F6E56';
$h1        = $mode['h1'] ?? "$modeLabel pour $aeroName";

$tagline   = $mode['tagline'] ?? '';
$intros    = $mode['intro_paragraphs'] ?? [];

$quickFacts = $mode['quick_facts'] ?? [];
$itineraire = $mode['itineraire'] ?? [];
$horaires   = $mode['horaires'] ?? [];
$tarifs     = $mode['tarifs'] ?? [];
$itinSource = $mode['itineraires_paris'] ?? [];
$alternatives = $mode['alternatives'] ?? [];
$pois       = $mode['pois'] ?? [];
$faq        = $mode['faq'] ?? [];

$canonical = '/aeroports/' . $aeroSlug . '/' . $modeSlug . '/';

$tpl->seo
    ->setTitle($mode['seo']['title'] ?? $h1)
    ->setDescription($mode['seo']['description'] ?? '')
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
  <section class="mode-hero" style="background: <?= Template::e($color) ?>;">
    <div class="mode-hero__content">
      <h1><?= Template::e($h1) ?></h1>
      <?php if ($tagline): ?>
        <p class="mode-tagline"><?= Template::e($tagline) ?></p>
      <?php endif; ?>

      <?php if (!empty($quickFacts)): ?>
        <div class="mode-quick-facts">
          <?php foreach ($quickFacts as $fact): ?>
            <div class="mode-fact">
              <span class="fact-value"><?= Template::e($fact['value']) ?></span>
              <span class="fact-label"><?= Template::e($fact['label']) ?></span>
            </div>
          <?php endforeach; ?>
        </div>
      <?php endif; ?>
    </div>
  </section>

  <?php $tpl->partial('ads/slot-header'); ?>

  <?php if (!empty($intros)): ?>
    <section class="mode-section">
      <?php foreach ($intros as $p): ?>
        <p><?= $p ?></p>
      <?php endforeach; ?>
    </section>
  <?php endif; ?>

  <?php if (!empty($itineraire)): ?>
    <section class="mode-section" id="itineraire">
      <h2><?= Template::e($itineraire['h2'] ?? "Itinéraire détaillé") ?></h2>
      <?php foreach (($itineraire['paragraphs'] ?? []) as $p): ?>
        <p><?= $p ?></p>
      <?php endforeach; ?>
      <?php if (!empty($itineraire['steps'])): ?>
        <ol class="mode-steps">
          <?php foreach ($itineraire['steps'] as $step): ?>
            <li><?= $step ?></li>
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

  <?php if (!empty($tarifs)): ?>
    <section class="mode-section" id="tarifs">
      <h2><?= Template::e($tarifs['h2'] ?? "Tarifs") ?></h2>
      <?php foreach (($tarifs['paragraphs'] ?? []) as $p): ?>
        <p><?= $p ?></p>
      <?php endforeach; ?>
      <?php if (!empty($tarifs['table'])): ?>
        <div class="mode-table-wrap">
          <table class="mode-table">
            <thead>
              <tr>
                <?php foreach ($tarifs['table']['headers'] as $h): ?>
                  <th><?= Template::e($h) ?></th>
                <?php endforeach; ?>
              </tr>
            </thead>
            <tbody>
              <?php foreach ($tarifs['table']['rows'] as $row): ?>
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
                <td><?= $i['trajet'] ?? '' ?></td>
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

  <?php if (!empty($alternatives)): ?>
    <section class="mode-section" id="alternatives">
      <h2>Alternatives pour rejoindre <?= Template::e($aeroName) ?></h2>
      <p>D'autres modes de transport relient Paris à <?= Template::e($aeroName) ?> :</p>
      <ul class="alt-list">
        <?php foreach ($alternatives as $alt): ?>
          <li>
            <a href="<?= Template::e($alt['url']) ?>">
              <strong><?= Template::e($alt['label']) ?></strong>
            </a>
            <?php if (!empty($alt['note'])): ?>
              — <?= Template::e($alt['note']) ?>
            <?php endif; ?>
          </li>
        <?php endforeach; ?>
      </ul>
      <p>
        <a href="/aeroports/<?= Template::e($aeroSlug) ?>/" class="back-link">
          ← Retour au guide complet <?= Template::e($aeroName) ?>
        </a>
      </p>
    </section>
  <?php endif; ?>

  <?php if (!empty($faq)): ?>
    <section class="mode-section" id="faq">
      <h2>FAQ — <?= Template::e($modeLabel) ?> <?= Template::e($aeroName) ?></h2>
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

  <?php $tpl->partial('ads/slot-footer'); ?>

</article>
</div>

<style>
.aeroport-mode-page { padding: 1.5rem 0; }
.aeroport-mode-page h2 { margin-top: 2rem; color: #0F6E56; }
.mode-hero { color: #fff; padding: 2rem 1.5rem; border-radius: 12px; margin-bottom: 1.5rem; }
.mode-hero h1 { color: #fff; margin: 0 0 .5rem; font-size: clamp(1.5rem, 3.5vw, 2rem); line-height: 1.25; }
.mode-tagline { font-size: 1.05rem; opacity: .95; margin: 0 0 1rem; font-weight: 600; }
.mode-quick-facts { display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 1rem; }
.mode-fact { background: rgba(255,255,255,.15); padding: .75rem 1rem; border-radius: 8px; min-width: 110px; text-align: center; }
.fact-value { display: block; font-weight: 700; font-size: 1.3rem; line-height: 1; }
.fact-label { display: block; font-size: .8rem; opacity: .85; margin-top: .25rem; }
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
.faq-item summary { cursor: pointer; font-weight: 600; }
.faq-item p { margin-top: .5rem; }
.back-link { font-weight: 600; color: #0F6E56; }
</style>
