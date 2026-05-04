<?php
/**
 * Composant : Horaires par ligne (page station)
 *
 * Affiche un tableau récapitulatif des horaires (premier/dernier métro,
 * service prolongé vendredi-samedi, fréquence en heures de pointe) pour
 * chaque ligne desservant la station.
 *
 * Les données sont mutualisées depuis les JSON des lignes
 * (data/lines/{slug}.json) via getLineSchedule(). Aucune donnée
 * dupliquée dans le JSON station.
 *
 * Variables attendues :
 *   $lines : array des lignes desservant la station (issu de $station['lines'])
 *            Chaque ligne doit avoir : code, slug, color, text_color
 *   $stationName : string, nom de la station (pour le titre / aria-labels)
 *
 * Affichage responsive :
 *   - Mobile (<768px)  : cartes empilées verticalement
 *   - Desktop (≥768px) : tableau comparatif
 *
 * Si aucune ligne n'a de schedule disponible, le composant n'affiche rien.
 *
 * @package BougeaParis\Templates\Components\Station
 * @since Livraison 5
 */

echo '<div style="background:#FFE5A0;padding:1rem;margin:1rem 0;border:2px solid orange;font-family:monospace;font-size:13px">';
echo '<strong>🐛 DEBUG horaires-par-ligne</strong><br>';
echo 'function getLineSchedule exists: ' . (function_exists('getLineSchedule') ? '✅ YES' : '❌ NO') . '<br>';
echo 'lines passé au composant: ' . (is_array($lines ?? null) ? count($lines) . ' lignes' : 'PAS UN ARRAY') . '<br>';
if (is_array($lines ?? null)) {
    foreach ($lines as $i => $line) {
        $slug = $line['slug'] ?? '(pas de slug)';
        $sched = function_exists('getLineSchedule') ? getLineSchedule($slug) : null;
        echo "&nbsp;&nbsp;[$i] slug=<strong>$slug</strong> → schedule: " . ($sched ? '✅ trouvé (' . count($sched) . ' clés)' : '❌ null') . '<br>';
    }
}
echo '</div>';
$lines       = $props['lines']       ?? null;
$stationName = $props['stationName'] ?? null;
if (empty($lines) || !is_array($lines)) {
    return;
}

// Pré-charger les schedules pour ne garder que les lignes avec données
$linesWithSchedule = [];
foreach ($lines as $line) {
    $slug = $line['slug'] ?? null;
    if (!$slug) continue;

    $schedule = getLineSchedule($slug);
    if ($schedule === null) continue;

    $linesWithSchedule[] = [
        'line'     => $line,
        'schedule' => $schedule,
    ];
}

// Si aucune ligne n'a d'horaires disponibles, on n'affiche pas la section
if (empty($linesWithSchedule)) {
    return;
}

$stationName = $stationName ?? 'cette station';
?>

<section class="station-section section-horaires" id="horaires" aria-labelledby="horaires-title">

  <h2 id="horaires-title">Horaires des lignes à <?= e($stationName) ?></h2>

  <p class="section-intro">
    Premier et dernier métro, service prolongé du vendredi et samedi soir,
    fréquence aux heures de pointe : retrouvez les horaires pratiques de chaque ligne
    desservant la <strong>station <?= e($stationName) ?></strong>.
  </p>

  <!-- Version mobile : cartes empilées -->
  <div class="horaires-cards" role="presentation">
    <?php foreach ($linesWithSchedule as $item):
      $line = $item['line'];
      $sched = $item['schedule'];
      $first = $sched['first_departure']['weekday'] ?? '—';
      $lastWeek = $sched['last_departure']['weekday'] ?? '—';
      $lastFri = $sched['last_departure']['friday']  ?? null;
      $lastSat = $sched['last_departure']['saturday'] ?? null;
      $lastExtended = $lastFri ?? $lastSat;
      $peakInterval = $sched['frequency']['peak_hours']['interval'] ?? null;
      $lineUrl = '/metro/' . $line['slug'] . '/';
      $lineExists = class_exists('Routes') && Routes::exists(rtrim($lineUrl, '/'));
    ?>
      <div class="horaires-card">
        <div class="horaires-card__header">
          <?php if ($lineExists): ?>
            <a href="<?= e($lineUrl) ?>" class="horaires-card__badge"
               style="background:<?= e($line['color']) ?>;color:<?= e($line['text_color']) ?>;">
              <?= e($line['code']) ?>
            </a>
          <?php else: ?>
            <span class="horaires-card__badge"
                  style="background:<?= e($line['color']) ?>;color:<?= e($line['text_color']) ?>;">
              <?= e($line['code']) ?>
            </span>
          <?php endif; ?>
          <span class="horaires-card__line-label">Ligne <?= e($line['code']) ?> du métro</span>
        </div>

        <dl class="horaires-card__list">
          <div class="horaires-card__row">
            <dt>Premier métro</dt>
            <dd><?= e($first) ?></dd>
          </div>
          <div class="horaires-card__row">
            <dt>Dernier métro</dt>
            <dd><?= e($lastWeek) ?></dd>
          </div>
          <?php if ($lastExtended && $lastExtended !== $lastWeek): ?>
            <div class="horaires-card__row horaires-card__row--extended">
              <dt>Vendredi &amp; samedi <span class="badge-extended">PROLONGÉ</span></dt>
              <dd><?= e($lastExtended) ?></dd>
            </div>
          <?php endif; ?>
          <?php if ($peakInterval): ?>
            <div class="horaires-card__row">
              <dt>Fréquence (heures de pointe)</dt>
              <dd><?= e($peakInterval) ?></dd>
            </div>
          <?php endif; ?>
        </dl>
      </div>
    <?php endforeach; ?>
  </div>

  <!-- Version desktop : tableau comparatif -->
  <div class="horaires-table-wrapper" role="presentation">
    <table class="horaires-table">
      <caption class="visually-hidden">
        Tableau des horaires des lignes de métro à la station <?= e($stationName) ?>
      </caption>
      <thead>
        <tr>
          <th scope="col">Ligne</th>
          <th scope="col">Premier métro</th>
          <th scope="col">Dernier métro</th>
          <th scope="col">Vendredi &amp; samedi</th>
          <th scope="col">Fréquence (heures de pointe)</th>
        </tr>
      </thead>
      <tbody>
        <?php foreach ($linesWithSchedule as $item):
          $line = $item['line'];
          $sched = $item['schedule'];
          $first = $sched['first_departure']['weekday'] ?? '—';
          $lastWeek = $sched['last_departure']['weekday'] ?? '—';
          $lastFri = $sched['last_departure']['friday']  ?? null;
          $lastSat = $sched['last_departure']['saturday'] ?? null;
          $lastExtended = $lastFri ?? $lastSat;
          $peakInterval = $sched['frequency']['peak_hours']['interval'] ?? '—';
          $lineUrl = '/metro/' . $line['slug'] . '/';
          $lineExists = class_exists('Routes') && Routes::exists(rtrim($lineUrl, '/'));
        ?>
          <tr>
            <th scope="row" class="horaires-table__line-cell">
              <?php if ($lineExists): ?>
                <a href="<?= e($lineUrl) ?>" class="horaires-table__badge"
                   style="background:<?= e($line['color']) ?>;color:<?= e($line['text_color']) ?>;"
                   aria-label="Voir la page de la ligne <?= e($line['code']) ?>">
                  <?= e($line['code']) ?>
                </a>
              <?php else: ?>
                <span class="horaires-table__badge"
                      style="background:<?= e($line['color']) ?>;color:<?= e($line['text_color']) ?>;">
                  <?= e($line['code']) ?>
                </span>
              <?php endif; ?>
            </th>
            <td><?= e($first) ?></td>
            <td><?= e($lastWeek) ?></td>
            <td>
              <?php if ($lastExtended && $lastExtended !== $lastWeek): ?>
                <strong><?= e($lastExtended) ?></strong>
                <span class="badge-extended">PROLONGÉ</span>
              <?php else: ?>
                <span class="text-muted">—</span>
              <?php endif; ?>
            </td>
            <td><?= e($peakInterval) ?></td>
          </tr>
        <?php endforeach; ?>
      </tbody>
    </table>
  </div>

  <p class="horaires-note">
    <small>
      Les horaires sont indicatifs et peuvent varier en cas de travaux ou perturbations.
      Pour le détail jour par jour de chaque ligne, consultez la page dédiée à la ligne concernée.
    </small>
  </p>

</section>
