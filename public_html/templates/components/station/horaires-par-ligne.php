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

/**
 * Convertit "5h30" ou "1h15" en minutes depuis 00h00. Les heures
 * post-minuit (1h15, 2h15) sont décalées de +1440 pour comparaison
 * monotone avec un service nocturne qui chevauche minuit.
 */
$timeToMinutes = function (?string $hhmm) {
    if (!$hhmm) return null;
    if (preg_match('/^(\d{1,2})h(\d{0,2})$/', trim($hhmm), $m)) {
        $h = (int)$m[1]; $mn = $m[2] !== '' ? (int)$m[2] : 0;
        $base = $h * 60 + $mn;
        // 0h00-4h00 → service nocturne, ajoute 1440 min pour ordonnancement
        if ($h < 4) $base += 1440;
        return $base;
    }
    return null;
};

// Agrégation premier / dernier métro toutes lignes
$earliest = null; $earliestLine = null; $earliestDir = null;
$latestWeek = null; $latestWeekLine = null; $latestWeekDir = null;
$latestExt = null;
foreach ($linesWithSchedule as $item) {
    $line = $item['line']; $sched = $item['schedule'];
    $slug = $line['slug'] ?? '';
    $meta = function_exists('getLineMeta') ? getLineMeta($slug) : null;
    $direction = $meta['terminus_b'] ?? $meta['terminus_a'] ?? null;

    $first = $sched['first_departure']['weekday'] ?? null;
    $lastW = $sched['last_departure']['weekday'] ?? null;
    $ext   = $sched['last_departure']['friday'] ?? $sched['last_departure']['saturday'] ?? null;

    $firstMin = $timeToMinutes($first);
    $lastMin  = $timeToMinutes($lastW);
    $extMin   = $timeToMinutes($ext);

    if ($firstMin !== null && ($earliest === null || $firstMin < $timeToMinutes($earliest))) {
        $earliest = $first;
        $earliestLine = $line['code'] ?? null;
        $earliestDir = $direction;
    }
    if ($lastMin !== null && ($latestWeek === null || $lastMin > $timeToMinutes($latestWeek))) {
        $latestWeek = $lastW;
        $latestWeekLine = $line['code'] ?? null;
        $latestWeekDir = $direction;
    }
    if ($extMin !== null && $lastMin !== null && $extMin > $lastMin) {
        if ($latestExt === null || $extMin > $timeToMinutes($latestExt)) {
            $latestExt = $ext;
        }
    }
}

$lineCount = count($linesWithSchedule);
$lineCodes = array_map(fn($i) => $i['line']['code'] ?? '', $linesWithSchedule);
$lineCodesLabel = $lineCount === 1
    ? 'la Ligne ' . $lineCodes[0]
    : ($lineCount === 2
        ? 'les Lignes ' . $lineCodes[0] . ' et ' . $lineCodes[1]
        : 'les Lignes ' . implode(', ', array_slice($lineCodes, 0, -1)) . ' et ' . end($lineCodes));
?>

<section class="station-section section-horaires" id="horaires" aria-labelledby="horaires-title">

  <h2 id="horaires-title"><?= e($props['sectionTitle'] ?? ('Horaires des lignes à ' . $stationName)) ?></h2>

  <p class="section-intro">
    La station <strong><?= e($stationName) ?></strong> est desservie par <?= e($lineCodesLabel) ?> du métro, du lundi au dimanche.
  </p>

  <?php if ($earliest && $latestWeek): ?>
    <p>
      Le <strong>premier métro à <?= e($stationName) ?></strong> circule à partir de <strong><?= e($earliest) ?></strong><?php if ($earliestLine && $earliestDir): ?> (Ligne <?= e($earliestLine) ?> direction <?= e($earliestDir) ?>)<?php endif; ?>, et le <strong>dernier métro à <?= e($stationName) ?></strong> quitte la station à <strong><?= e($latestWeek) ?></strong><?php if ($latestWeekLine && $latestWeekDir): ?> (Ligne <?= e($latestWeekLine) ?> direction <?= e($latestWeekDir) ?>)<?php endif; ?> en semaine.
      <?php if ($latestExt): ?>
        Le <strong>vendredi soir, le samedi soir et les veilles de fêtes</strong>, le service est prolongé jusqu'à <strong><?= e($latestExt) ?></strong> sur l'ensemble des lignes.
      <?php endif; ?>
    </p>
    <p>
      Pour des correspondances précises et adaptées à votre itinéraire depuis ou vers <?= e($stationName) ?>, consultez les horaires détaillés ci-dessous selon la ligne de votre choix.
    </p>
  <?php else: ?>
    <p class="section-intro">
      Premier et dernier métro, service prolongé du vendredi et samedi soir, fréquence aux heures de pointe : retrouvez les horaires pratiques de chaque ligne desservant la <strong>station <?= e($stationName) ?></strong>.
    </p>
  <?php endif; ?>

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
      <?php
        // Correction 18A : migration vers .line-pill (cohérence avec hero badges,
        // correspondances et adjacents stations — corrections 15/16a).
        $pillLabel = 'M' . $line['code'];
        $pillSlug  = 'm' . strtolower((string)$line['code']);
        $pillShape = linePillShape($pillLabel);
      ?>
      <div class="horaires-card">
        <div class="horaires-card__header">
          <?php if ($lineExists): ?>
            <a href="<?= e($lineUrl) ?>" class="line-pill line-pill--<?= e($pillShape) ?> line-pill--<?= e($pillSlug) ?>"
               aria-label="Ligne <?= e($line['code']) ?> du métro">
              <?= e($pillLabel) ?>
            </a>
          <?php else: ?>
            <span class="line-pill line-pill--<?= e($pillShape) ?> line-pill--<?= e($pillSlug) ?>"
                  aria-label="Ligne <?= e($line['code']) ?> du métro">
              <?= e($pillLabel) ?>
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
          <?php
            // Correction 18A : .line-pill dans la version desktop du tableau
            $pillLabel = 'M' . $line['code'];
            $pillSlug  = 'm' . strtolower((string)$line['code']);
            $pillShape = linePillShape($pillLabel);
          ?>
          <tr>
            <th scope="row" class="horaires-table__line-cell">
              <?php if ($lineExists): ?>
                <a href="<?= e($lineUrl) ?>" class="line-pill line-pill--<?= e($pillShape) ?> line-pill--<?= e($pillSlug) ?>"
                   aria-label="Voir la page de la ligne <?= e($line['code']) ?>">
                  <?= e($pillLabel) ?>
                </a>
              <?php else: ?>
                <span class="line-pill line-pill--<?= e($pillShape) ?> line-pill--<?= e($pillSlug) ?>"
                      aria-label="Ligne <?= e($line['code']) ?> du métro">
                  <?= e($pillLabel) ?>
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
