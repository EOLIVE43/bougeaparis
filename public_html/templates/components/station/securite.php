<?php
/**
 * Composant : Sécurité et conseils voyageur (page station)
 *
 * Affiche les informations sécurité de la station : niveau,
 * présence agents/police, conseils anti-pickpockets, numéro
 * d'urgence RATP.
 *
 * Variables attendues (props) :
 * - safety      : array (clés : level, agents, police, tips,
 *                  notes)
 * - stationName : string
 *
 * Si $safety vide → le composant ne rend rien.
 */

$safety      = $props['safety']      ?? null;
$stationName = $props['stationName'] ?? null;

if (empty($safety) || !is_array($safety) || !$stationName) {
    return;
}

$tips  = $safety['tips']  ?? [];
$notes = $safety['notes'] ?? '';
$level = $safety['level'] ?? null; // 'standard', 'high', 'low'
$agents = isset($safety['agents']) ? (bool)$safety['agents'] : null;
$police = isset($safety['police']) ? (bool)$safety['police'] : null;

$levelLabels = [
    'standard' => ['label' => 'Niveau standard',       'icon' => '🛡️', 'class' => 'safety-level--standard'],
    'high'     => ['label' => 'Vigilance recommandée', 'icon' => '⚠️',  'class' => 'safety-level--high'],
    'low'      => ['label' => 'Station calme',          'icon' => '✓',  'class' => 'safety-level--low'],
];
?>

<section class="station-section section-securite" id="securite" aria-labelledby="securite-title">

  <h2 id="securite-title">Sécurité à la station <?= Template::e($stationName) ?></h2>

  <p class="section-intro">
    Voici les informations sécurité disponibles pour la station <strong><?= Template::e($stationName) ?></strong>. En cas d'incident ou de comportement suspect, prévenez immédiatement un agent RATP ou composez le numéro d'urgence RATP.
  </p>

  <?php if ($level && isset($levelLabels[$level])): ?>
    <p class="safety-level <?= Template::e($levelLabels[$level]['class']) ?>">
      <span class="safety-level__icon" aria-hidden="true"><?= Template::e($levelLabels[$level]['icon']) ?></span>
      <strong><?= Template::e($levelLabels[$level]['label']) ?></strong>
    </p>
  <?php endif; ?>

  <?php if ($agents !== null || $police !== null): ?>
    <ul class="safety-presence">
      <?php if ($agents !== null): ?>
        <li>
          <span class="safety-presence__icon" aria-hidden="true">👤</span>
          <strong>Agents RATP :</strong> <?= $agents ? 'Présence régulière' : 'Présence ponctuelle' ?>
        </li>
      <?php endif; ?>
      <?php if ($police !== null): ?>
        <li>
          <span class="safety-presence__icon" aria-hidden="true">👮</span>
          <strong>Police / GPSR :</strong> <?= $police ? 'Patrouilles régulières' : 'Pas de présence permanente' ?>
        </li>
      <?php endif; ?>
    </ul>
  <?php endif; ?>

  <?php if (!empty($tips)): ?>
    <h3 class="safety-subtitle">Conseils de sécurité à <?= Template::e($stationName) ?></h3>
    <ul class="safety-tips">
      <?php foreach ($tips as $tip): ?>
        <li><span class="safety-tips__icon" aria-hidden="true">💡</span> <?= richText($tip) ?></li>
      <?php endforeach; ?>
    </ul>
  <?php endif; ?>

  <?php if ($notes !== ''): ?>
    <p class="safety-notes"><?= richText($notes) ?></p>
  <?php endif; ?>

  <div class="safety-emergency">
    <p>
      <strong>En cas d'urgence :</strong>
      RATP <strong>3424</strong> (24h/24) — Police-secours <strong>17</strong> — SAMU <strong>15</strong>
    </p>
  </div>

</section>
