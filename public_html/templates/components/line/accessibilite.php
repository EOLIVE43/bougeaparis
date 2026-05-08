<?php
/**
 * Section Accessibilité PMR — Page ligne de métro
 *
 * Informations sur l'accessibilité aux personnes à mobilité réduite :
 * - Stats du taux d'accessibilité
 * - Équipements disponibles
 * - Liste des stations accessibles
 * - Conseils pratiques
 * - Liens vers ressources externes
 *
 * Variables attendues :
 * - $line : array, données de la ligne (incluant 'accessibility' et 'intros.accessibilite')
 *
 * Stratégie SEO :
 * - H2 unique avec "ligne X" + "PMR"
 * - Densité mots-clés : "accessibilité ligne X", "stations PMR", "métro fauteuil roulant"
 * - Schema.org : utilité pour les Google Rich Results
 */

$accessibility = $line['accessibility'] ?? null;
if (!$accessibility) {
    return;
}

$introText = $line['intros']['accessibilite'] ?? null;
$stats = $accessibility['stats'];
?>

<section class="section section--accessibilite" id="accessibilite" aria-labelledby="accessibilite-title">

  <h2 id="accessibilite-title">Accessibilité PMR de la ligne <?= htmlspecialchars($line['code']) ?> du métro</h2>

  <!-- Intro -->
  <div class="accessibilite__intro">
    <?php if ($introText): ?>
      <p><?= $introText ?></p>
    <?php else: ?>
      <p>L'<strong>accessibilité de la ligne <?= htmlspecialchars($line['code']) ?></strong> aux personnes à mobilité réduite (PMR) varie selon les stations.</p>
    <?php endif; ?>
  </div>

  <!-- Stats visuelles -->
  <div class="accessibilite__stats">

    <div class="access-stat">
      <div class="access-stat__circle">
        <svg viewBox="0 0 100 100" class="access-stat__progress" aria-hidden="true">
          <circle cx="50" cy="50" r="42" fill="none" stroke-width="10"/>
          <circle cx="50" cy="50" r="42" fill="none" stroke-width="10"
                  stroke-dasharray="<?= round($stats['accessibility_rate'] * 2.64) ?> 264"
                  stroke-dashoffset="0"
                  transform="rotate(-90 50 50)"
                  stroke-linecap="round"/>
        </svg>
        <div class="access-stat__circle-value"><?= htmlspecialchars($stats['accessibility_rate']) ?>%</div>
      </div>
      <div class="access-stat__label">Taux d'accessibilité</div>
      <div class="access-stat__detail"><?= htmlspecialchars($stats['accessible_count']) ?> stations sur <?= htmlspecialchars($stats['total_count']) ?></div>
    </div>

    <div class="access-stat-card">
      <div class="access-stat-card__icon" aria-hidden="true">♿</div>
      <div class="access-stat-card__value"><?= htmlspecialchars($stats['accessible_count']) ?></div>
      <div class="access-stat-card__label">Stations accessibles<br>aux fauteuils roulants</div>
    </div>

    <div class="access-stat-card">
      <div class="access-stat-card__icon" aria-hidden="true">🛗</div>
      <div class="access-stat-card__value"><?= htmlspecialchars($stats['elevators_count']) ?></div>
      <div class="access-stat-card__label">Ascenseurs<br>en service sur la ligne</div>
    </div>

    <div class="access-stat-card">
      <div class="access-stat-card__icon" aria-hidden="true">🚪</div>
      <div class="access-stat-card__value">100%</div>
      <div class="access-stat-card__label">Stations équipées<br>de portes palières</div>
    </div>

  </div>

  <!-- Équipements -->
  <h3 class="accessibilite__subtitle">Équipements PMR sur la ligne <?= htmlspecialchars($line['code']) ?></h3>
  <div class="accessibilite__equipment">
    <?php foreach ($accessibility['equipment'] as $eq): ?>
      <div class="equipment-card">
        <div class="equipment-card__icon" aria-hidden="true"><?= htmlspecialchars($eq['icon']) ?></div>
        <div class="equipment-card__content">
          <div class="equipment-card__label"><?= htmlspecialchars($eq['label']) ?></div>
          <div class="equipment-card__desc"><?= richText($eq['description'] ?? '') ?></div>
        </div>
      </div>
    <?php endforeach; ?>
  </div>

  <!-- Liste des stations accessibles -->
  <?php if (!empty($accessibility['accessible_stations'])): ?>
    <h3 class="accessibilite__subtitle">Stations accessibles aux PMR sur la ligne <?= htmlspecialchars($line['code']) ?></h3>
    <div class="accessibilite__stations-list">
      <?php foreach ($accessibility['accessible_stations'] as $station): ?>
        <div class="access-station <?= ($station['is_major'] ?? false) ? 'access-station--major' : '' ?>">
          <span class="access-station__icon" aria-label="Station accessible PMR">✓</span>
          <span class="access-station__name"><?= htmlspecialchars($station['name']) ?></span>
          <?php if (!empty($station['subtitle'])): ?>
            <span class="access-station__subtitle"><?= htmlspecialchars($station['subtitle']) ?></span>
          <?php endif; ?>
        </div>
      <?php endforeach; ?>
    </div>
    <p class="accessibilite__note">
      Liste basée sur les données officielles d'<strong>Île-de-France Mobilités</strong>. Vérifiez le fonctionnement des ascenseurs en temps réel avant votre voyage, des pannes ponctuelles peuvent survenir.
    </p>
  <?php endif; ?>

  <!-- Conseils pratiques -->
  <h3 class="accessibilite__subtitle">Conseils pratiques pour voyager PMR sur la ligne <?= htmlspecialchars($line['code']) ?></h3>
  <div class="accessibilite__tips">
    <?php foreach ($accessibility['tips'] as $tip): ?>
      <div class="access-tip">
        <div class="access-tip__title"><?= htmlspecialchars($tip['title']) ?></div>
        <p class="access-tip__desc"><?= richText($tip['description'] ?? '') ?></p>
      </div>
    <?php endforeach; ?>
  </div>

  <!-- Ressources externes -->
  <?php if (!empty($accessibility['external_resources'])): ?>
    <div class="accessibilite__resources">
      <div class="accessibilite__resources-title">Ressources officielles</div>
      <div class="accessibilite__resources-list">
        <?php foreach ($accessibility['external_resources'] as $res): ?>
          <a href="<?= htmlspecialchars($res['url']) ?>" rel="noopener noreferrer" target="_blank" class="access-resource">
            <div class="access-resource__label"><?= htmlspecialchars($res['label']) ?> <span aria-hidden="true">↗</span></div>
            <div class="access-resource__desc"><?= richText($res['description'] ?? '') ?></div>
          </a>
        <?php endforeach; ?>
      </div>
    </div>
  <?php endif; ?>

</section>
