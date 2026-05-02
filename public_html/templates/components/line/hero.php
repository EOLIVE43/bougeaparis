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
    : date('j F Y');

$trafficStatus   = 'ok';
$trafficMessage  = 'Trafic normal sur la ligne ' . $line['code'];
$trafficUpdate   = '32 secondes';
$ridersFormatted = number_format(($line['daily_riders'] ?? 0) / 1000, 0) . 'K';
?>

<section class="hero" aria-labelledby="hero-title">
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

  <a href="/itineraires/?line=<?= htmlspecialchars($line['code']) ?>" class="hero__cta">
    <span class="hero__cta-icon" aria-hidden="true">🗺️</span>
    Calculer un itinéraire sur la ligne <?= htmlspecialchars($line['code']) ?>
  </a>

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
</section>
