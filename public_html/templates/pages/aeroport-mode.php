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

// Charger le JSON parent aéroport pour récupérer access_modes[] (maillage interne)
$parentFile = __DIR__ . '/../../data/aeroports/' . $aeroSlug . '.json';
$parentAero = is_file($parentFile) ? json_decode((string)file_get_contents($parentFile), true) : null;
$allModes   = is_array($parentAero) ? ($parentAero['access_modes'] ?? []) : [];
$otherModes = array_values(array_filter($allModes, fn($m) => ($m['slug'] ?? '') !== $modeSlug));

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
        <p><?= $p ?></p>
      <?php endforeach; ?>
      <?php if (!empty($tarifs['table']['rows'])): ?>
        <div class="info-cards-grid">
          <?php foreach ($tarifs['table']['rows'] as $row):
            $title   = $row[0] ?? '';
            $price   = $row[1] ?? '';
            $details = $row[2] ?? '';
          ?>
            <div class="info-card info-card--<?= Template::e($iconKey) ?>">
              <div class="info-card__icon"><?= $iconSvg ?></div>
              <div class="info-card__content">
                <h3 class="info-card__title"><?= Template::e($title) ?></h3>
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
            <h3 class="mode-card__title"><?= Template::e($m['name'] ?? '') ?></h3>
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
</style>
