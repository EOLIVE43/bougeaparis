<?php
/**
 * Section Hero — Page ligne de métro
 *
 * Variables attendues (injectées par Template::partial via $line) :
 *   $line : array, données complètes de la ligne
 *
 * Variables dérivées localement :
 *   $lineColor, $h1, $updatedDate
 */

// Dérivation locale (pour rester découplé du template page)
$lineColor   = $line['color']      ?? '#0F6E56';
$h1          = $line['seo']['h1']  ?? ('Ligne ' . ($line['code'] ?? ''));
$updatedDate = isset($line['meta']['dates']['updated_human'])
    ? $line['meta']['dates']['updated_human']
    : dateFr(null, 'short');

$trafficStatus   = 'ok';
$trafficMessage  = 'Trafic normal sur la ligne ' . $line['code'];
$trafficUpdate   = '32 secondes';
$ridersFormatted = number_format(($line['daily_riders'] ?? 0) / 1000, 0) . 'K';

// Hero image : nouveau format hero_image (avec local_versions AVIF/WebP/JPG).
$heroImage      = $line['hero_image'] ?? null;
$hasImage       = is_array($heroImage) && !empty($heroImage['url']);
$localVersions  = $hasImage ? ($heroImage['local_versions'] ?? null) : null;
$hasPicture     = is_array($localVersions)
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

<section class="hero<?= $hasImage ? ' hero--with-image' : '' ?>" aria-labelledby="hero-title">

  <?php if ($hasImage):
    $imgAlt = $heroImage['alt'] ?? ('Ligne ' . ($line['code'] ?? '') . ' du métro de Paris');
    $imgW   = (int)($heroImage['width']  ?? 1600);
    $imgH   = (int)($heroImage['height'] ?? 1040);
    $sizes  = '(max-width: 768px) 100vw, 1200px';
  ?>
    <div class="hero__image">
      <?php if ($hasPicture): ?>
        <picture>
          <source type="image/avif"
                  srcset="<?= $buildSrcset($localVersions['avif']) ?>"
                  sizes="<?= htmlspecialchars($sizes) ?>">
          <source type="image/webp"
                  srcset="<?= $buildSrcset($localVersions['webp']) ?>"
                  sizes="<?= htmlspecialchars($sizes) ?>">
          <img src="<?= htmlspecialchars($localVersions['jpg'][1200] ?? reset($localVersions['jpg'])) ?>"
               srcset="<?= $buildSrcset($localVersions['jpg']) ?>"
               sizes="<?= htmlspecialchars($sizes) ?>"
               alt="<?= htmlspecialchars($imgAlt) ?>"
               width="<?= $imgW ?>" height="<?= $imgH ?>"
               loading="eager" fetchpriority="high">
        </picture>
      <?php else: ?>
        <img src="<?= htmlspecialchars($heroImage['url']) ?>"
             alt="<?= htmlspecialchars($imgAlt) ?>"
             width="<?= $imgW ?>" height="<?= $imgH ?>"
             loading="eager" fetchpriority="high"
             referrerpolicy="no-referrer">
      <?php endif; ?>
    </div>
  <?php endif; ?>

  <div class="hero__content">

  <div class="hero__pills">
    <span class="pill-mode">MÉTRO</span>
    <span class="pill-line" style="background: <?= htmlspecialchars($lineColor) ?>; color: <?= htmlspecialchars($line['color_text'] ?? '#1A2B26') ?>;">
      LIGNE <?= htmlspecialchars($line['code']) ?>
    </span>
  </div>

  <h1 id="hero-title" class="hero__title">
    <?= htmlspecialchars($h1) ?>
  </h1>

  <p class="hero__lead">
    <?= $line['seo']['lead'] ?>
  </p>

  <div class="traffic-banner traffic-banner--<?= $trafficStatus ?>" role="status" aria-live="polite">
    <span class="traffic-banner__dot" aria-hidden="true"></span>
    <div class="traffic-banner__main">
      <div class="traffic-banner__title"><?= htmlspecialchars($trafficMessage) ?></div>
      <div class="traffic-banner__update">
        Mis à jour il y a <?= htmlspecialchars($trafficUpdate) ?> · Source : Île-de-France Mobilités
      </div>
    </div>
    <a href="#trafic-temps-reel" class="traffic-banner__link">Voir le détail →</a>
  </div>

  <div class="hero__stats" role="list">
    <div class="stat-card" role="listitem">
      <div class="stat-card__icon" aria-hidden="true">🚉</div>
      <div class="stat-card__value"><?= htmlspecialchars($line['stations_count']) ?></div>
      <div class="stat-card__label">Stations</div>
    </div>
    <div class="stat-card" role="listitem">
      <div class="stat-card__icon" aria-hidden="true">📏</div>
      <div class="stat-card__value"><?= str_replace('.', ',', $line['length_km']) ?> km</div>
      <div class="stat-card__label">Longueur</div>
    </div>
    <div class="stat-card" role="listitem">
      <div class="stat-card__icon" aria-hidden="true">⏱️</div>
      <div class="stat-card__value">~<?= htmlspecialchars($line['duration_minutes']) ?> min</div>
      <div class="stat-card__label">Trajet complet</div>
    </div>
    <div class="stat-card" role="listitem">
      <div class="stat-card__icon" aria-hidden="true">👥</div>
      <div class="stat-card__value"><?= htmlspecialchars($ridersFormatted) ?></div>
      <div class="stat-card__label">Voyageurs / jour</div>
    </div>
  </div>

  <span class="hero__cta hero__cta--inactive" data-future-url="/itineraires/?line=<?= htmlspecialchars($line['code']) ?>" aria-disabled="true">
    <span class="hero__cta-icon" aria-hidden="true">🗺️</span>
    Calculer un itinéraire sur la ligne <?= htmlspecialchars($line['code']) ?>
  </span>

  <div class="hero__meta">
    <div class="hero__meta-item">
      <span aria-hidden="true">✍️</span>
      Par <a href="/auteur/ludo/" rel="author">Ludo</a>
    </div>
    <div class="hero__meta-item">
      <span aria-hidden="true">📅</span>
      Mis à jour le <time datetime="<?= date('Y-m-d') ?>"><?= htmlspecialchars($updatedDate) ?></time>
    </div>
    <div class="hero__meta-item">
      <span aria-hidden="true">⏰</span>
      Temps de lecture : 8 minutes
    </div>
  </div>

  </div><!-- /.hero__content -->
</section>
