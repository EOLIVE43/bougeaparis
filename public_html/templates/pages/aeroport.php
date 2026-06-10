<?php
/**
 * Template : page détail aéroport (CDG, Orly, Beauvais).
 * Props attendues : $aeroport (array décodé depuis data/aeroports/{slug}.json).
 */
$aeroport = $aeroport ?? $props['aeroport'] ?? [];
$slug     = $aeroport['slug']      ?? 'aeroport';
$name     = $aeroport['name']      ?? 'Aéroport';
$full     = $aeroport['full_name'] ?? $name;
$iata     = $aeroport['iata']      ?? '';
$dept     = $aeroport['department']?? '';
$dist     = $aeroport['distance_paris_km'] ?? null;
$traffic  = $aeroport['annual_traffic'] ?? '';
$opened   = $aeroport['opened']    ?? '';
$operator = $aeroport['operator']  ?? '';
$terminals = $aeroport['terminals'] ?? [];
$tagline  = $aeroport['hero']['tagline'] ?? '';
$heroDesc = $aeroport['hero']['description'] ?? '';
$intros   = $aeroport['intro_paragraphs'] ?? [];
$history  = $aeroport['history'] ?? [];
$access   = $aeroport['access'] ?? [];
$terminalsDetail = $aeroport['terminals_detail'] ?? [];
$faq      = $aeroport['faq'] ?? [];
$pois     = $aeroport['nearby_pois'] ?? [];

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
?>

<?php $tpl->partial('components/breadcrumb', ['items' => [
    ['label' => 'Accueil',    'url' => '/'],
    ['label' => 'Aéroports',  'url' => '/aeroports/'],
    ['label' => $name,        'url' => $canonical],
]]); ?>

<div class="container">
<article class="aeroport-page">

  <section class="aeroport-hero">
    <div class="aeroport-hero__content">
      <h1><?= Template::e($name) ?>
        <?php if ($iata): ?><span class="aeroport-iata">(<?= Template::e($iata) ?>)</span><?php endif; ?>
      </h1>
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

  <?php if (!empty($intros)): ?>
    <section class="aeroport-intro">
      <h2>Présentation</h2>
      <?php foreach ($intros as $p): ?>
        <p><?= $p ?></p>
      <?php endforeach; ?>
    </section>
  <?php endif; ?>

  <?php if (!empty($access)): ?>
    <section class="aeroport-access" id="acces">
      <h2>Accès depuis Paris</h2>
      <p class="lead">Plusieurs modes de transport permettent de rejoindre <strong><?= Template::e($name) ?></strong> depuis Paris.</p>
      <div class="access-grid">
        <?php foreach ($access as $key => $mode): ?>
          <div class="access-card">
            <h3><?= Template::e($mode['name'] ?? $key) ?></h3>
            <?php if (!empty($mode['from'])): ?>
              <p><strong>Depuis :</strong> <?= Template::e($mode['from']) ?></p>
            <?php endif; ?>
            <?php if (!empty($mode['time_min'])): ?>
              <p><strong>Durée :</strong> ~<?= Template::e($mode['time_min']) ?> min</p>
            <?php endif; ?>
            <?php if (!empty($mode['price_eur'])): ?>
              <p><strong>Prix :</strong> <?= Template::e($mode['price_eur']) ?> €</p>
            <?php endif; ?>
            <?php if (!empty($mode['frequency_min'])): ?>
              <p><strong>Fréquence :</strong> toutes les <?= Template::e($mode['frequency_min']) ?> min</p>
            <?php endif; ?>
            <?php if (!empty($mode['note'])): ?>
              <p class="access-note"><?= Template::e($mode['note']) ?></p>
            <?php endif; ?>
          </div>
        <?php endforeach; ?>
      </div>
    </section>
  <?php endif; ?>

  <?php if (!empty($terminalsDetail)): ?>
    <section class="aeroport-terminals" id="terminaux">
      <h2>Terminaux</h2>
      <table class="aeroport-terminals-table">
        <thead>
          <tr><th>Terminal</th><th>Compagnies principales</th><th>Année</th></tr>
        </thead>
        <tbody>
          <?php foreach ($terminalsDetail as $t): ?>
            <tr>
              <td><strong><?= Template::e($t['code'] ?? '') ?></strong></td>
              <td><?= Template::e($t['compagnies'] ?? '') ?></td>
              <td><?= Template::e($t['year'] ?? '') ?></td>
            </tr>
          <?php endforeach; ?>
        </tbody>
      </table>
    </section>
  <?php endif; ?>

  <?php if (!empty($history)): ?>
    <section class="aeroport-history" id="histoire">
      <h2>Histoire</h2>
      <?php foreach ($history as $p): ?>
        <p><?= $p ?></p>
      <?php endforeach; ?>
    </section>
  <?php endif; ?>

  <?php if (!empty($pois)): ?>
    <section class="aeroport-pois" id="proximite">
      <h2>À proximité</h2>
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
    <section class="aeroport-faq" id="faq">
      <h2>Questions fréquentes</h2>
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

  <section class="aeroport-meta">
    <h2>En résumé</h2>
    <dl class="aeroport-summary">
      <dt>Nom officiel</dt><dd><?= Template::e($full) ?></dd>
      <?php if ($iata): ?><dt>Code IATA</dt><dd><?= Template::e($iata) ?></dd><?php endif; ?>
      <?php if (!empty($aeroport['icao'])): ?><dt>Code ICAO</dt><dd><?= Template::e($aeroport['icao']) ?></dd><?php endif; ?>
      <?php if ($dept): ?><dt>Département</dt><dd><?= Template::e($dept) ?></dd><?php endif; ?>
      <?php if ($operator): ?><dt>Opérateur</dt><dd><?= Template::e($operator) ?></dd><?php endif; ?>
      <?php if ($opened): ?><dt>Ouverture</dt><dd><?= Template::e($opened) ?></dd><?php endif; ?>
    </dl>
  </section>

</article>
</div>

<style>
.aeroport-page { padding: 1.5rem 0; }
.aeroport-page h2 { margin-top: 2rem; }
.aeroport-hero { background: linear-gradient(135deg, #0F6E56, #085041); color: #fff; padding: 2rem 1.5rem; border-radius: 12px; margin-bottom: 1.5rem; }
.aeroport-hero h1 { color: #fff; margin: 0 0 .5rem; font-size: clamp(1.6rem, 4vw, 2.4rem); }
.aeroport-iata { font-weight: 400; opacity: .8; font-size: .8em; }
.aeroport-tagline { font-size: 1.05rem; opacity: .95; margin: 0 0 1rem; }
.aeroport-hero-desc { line-height: 1.6; margin-bottom: 1.5rem; }
.aeroport-hero-desc strong { color: #fff; }
.aeroport-key-figures { display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 1rem; }
.key-figure { background: rgba(255,255,255,.15); padding: .75rem 1rem; border-radius: 8px; min-width: 110px; text-align: center; }
.kf-value { display: block; font-weight: 700; font-size: 1.3rem; line-height: 1; }
.kf-label { display: block; font-size: .8rem; opacity: .85; margin-top: .25rem; }
.access-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-top: 1rem; }
.access-card { background: #f4f8f6; padding: 1rem; border-radius: 8px; border-left: 4px solid #0F6E56; }
.access-card h3 { margin: 0 0 .5rem; color: #0F6E56; }
.access-card p { margin: .25rem 0; font-size: .95rem; }
.access-note { font-style: italic; font-size: .9rem; color: #555; margin-top: .5rem !important; }
.aeroport-terminals-table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
.aeroport-terminals-table th, .aeroport-terminals-table td { padding: .6rem; border-bottom: 1px solid #ddd; text-align: left; }
.aeroport-terminals-table th { background: #f4f8f6; }
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
</style>
