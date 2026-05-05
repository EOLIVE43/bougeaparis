<?php
/**
 * Composant : Trafic temps réel (page station)
 *
 * Affiche un bandeau adaptatif selon l'état du trafic sur les lignes desservant
 * la station :
 *   - SI aucune perturbation : mini-bandeau vert discret "Trafic normal sur..."
 *   - SI au moins une perturbation : bloc complet avec sévérité, ligne(s)
 *     impactée(s), titre + résumé, badge couleur de chaque ligne
 *   - SI helper retourne null (clé absente, API down sans cache) : return early
 *
 * Données issues de l'API IDFM PRIM (cache 5 min) via getDisruptionsForStation()
 * dans core/helpers.php.
 *
 * Variables attendues :
 *   $traffic     : array|null retourné par getDisruptionsForStation()
 *                  Format : { has_disruption, max_severity, lines_with_disruptions,
 *                            lines_normal, fetched_at }
 *   $stationName : string, nom de la station (pour aria-labels)
 *   $allLines    : array, $station['lines'] (pour afficher les codes en mode normal)
 *
 * @package BougeaParis\Templates\Components\Station
 * @since Livraison 8 (trafic temps réel)
 */

$traffic     = $props['traffic']     ?? null;
$stationName = $props['stationName'] ?? null;
$allLines    = $props['allLines']    ?? [];

// Si helper a retourné null : graceful degradation (pas de bloc trafic du tout)
if ($traffic === null || !is_array($traffic)) {
    return;
}

$stationName = $stationName ?? 'cette station';
$hasDisruption = !empty($traffic['has_disruption']);
$linesWith    = $traffic['lines_with_disruptions'] ?? [];
$linesNormal  = $traffic['lines_normal'] ?? [];
$maxSeverity  = $traffic['max_severity'] ?? null;
$fetchedAt    = $traffic['fetched_at'] ?? null;

// Heure de mise à jour (HH:MM, locale Paris)
$updatedLabel = null;
if ($fetchedAt) {
    try {
        $dt = new DateTimeImmutable($fetchedAt);
        $dt = $dt->setTimezone(new DateTimeZone('Europe/Paris'));
        $updatedLabel = $dt->format('H\hi');
    } catch (\Throwable $e) {}
}

// Mapping sévérité -> classe CSS variant + label
$severityClass = match ($maxSeverity) {
    'BLOQUANTE'   => 'trafic--bloquante',
    'PERTURBEE'   => 'trafic--perturbee',
    'INFORMATION' => 'trafic--info',
    default       => 'trafic--normal',
};
$severityLabel = match ($maxSeverity) {
    'BLOQUANTE'   => 'Trafic interrompu',
    'PERTURBEE'   => 'Trafic perturbé',
    'INFORMATION' => 'Information trafic',
    default       => 'Trafic normal',
};
?>

<?php if (!$hasDisruption): ?>
  <!-- Cas 1 : trafic normal sur toutes les lignes desservies -->
  <section class="trafic-banner trafic--normal" id="trafic" aria-label="État du trafic">
    <div class="trafic-banner__inner">
      <span class="trafic-banner__icon" aria-hidden="true">✓</span>
      <span class="trafic-banner__message">
        <strong>Trafic normal</strong>
        <?php if (!empty($linesNormal)): ?>
          sur les lignes
          <?= e(implode(', ', $linesNormal)) ?>
          desservant la station
        <?php endif; ?>
        <?= e($stationName) ?>.
      </span>
      <?php if ($updatedLabel): ?>
        <span class="trafic-banner__time">
          Mis à jour à <?= e($updatedLabel) ?>
        </span>
      <?php endif; ?>
    </div>
  </section>

<?php else: ?>
  <!-- Cas 2 : au moins une perturbation -->
  <section class="trafic-block <?= e($severityClass) ?>" id="trafic" aria-labelledby="trafic-title">

    <header class="trafic-block__header">
      <div class="trafic-block__heading">
        <span class="trafic-block__icon" aria-hidden="true">
          <?= $maxSeverity === 'BLOQUANTE' ? '🚫' : '⚠️' ?>
        </span>
        <h2 class="trafic-block__title" id="trafic-title">
          <?= e($severityLabel) ?> à la station <?= e($stationName) ?>
        </h2>
      </div>
      <?php if ($updatedLabel): ?>
        <span class="trafic-block__time">
          Mis à jour à <?= e($updatedLabel) ?>
        </span>
      <?php endif; ?>
    </header>

    <p class="trafic-block__lead">
      <?= count($linesWith) ?>
      ligne<?= count($linesWith) > 1 ? 's' : '' ?>
      desservant <?= e($stationName) ?>
      <?= count($linesWith) > 1 ? 'sont impactées' : 'est impactée' ?>
      par une perturbation actuelle.
    </p>

    <ul class="trafic-block__list" role="list">
      <?php foreach ($linesWith as $line): ?>
        <li class="trafic-line">
          <div class="trafic-line__head">
            <span class="trafic-line__badge"
                  style="background:<?= e($line['color']) ?>;color:<?= e($line['text_color']) ?>;"
                  aria-label="Ligne <?= e($line['code']) ?> du métro">
              <?= e($line['code']) ?>
            </span>
            <span class="trafic-line__name">Ligne <?= e($line['code']) ?> du métro</span>
          </div>
          <ul class="trafic-line__disruptions" role="list">
            <?php foreach ($line['disruptions'] as $d):
              $sev = (string)($d['severity'] ?? '');
              $sevLabel = match ($sev) {
                  'BLOQUANTE'   => 'Trafic interrompu',
                  'PERTURBEE'   => 'Trafic perturbé',
                  'INFORMATION' => 'Information',
                  default       => $sev,
              };
              $sevDotClass = match ($sev) {
                  'BLOQUANTE'   => 'trafic-dot--bloquante',
                  'PERTURBEE'   => 'trafic-dot--perturbee',
                  default       => 'trafic-dot--info',
              };
              $title = trim((string)($d['title'] ?? ''));
              $message = trim((string)($d['message'] ?? ''));
              // Le message est deja nettoye par DisruptionFormatter::cleanHtml
              if ($title !== '' && stripos($message, $title) === 0) {
                  $message = trim(substr($message, strlen($title)));
              }
              $shortMsg = mb_strimwidth($message, 0, 240, '…');
            ?>
              <li class="trafic-disruption">
                <span class="trafic-disruption__sev">
                  <span class="trafic-dot <?= e($sevDotClass) ?>" aria-hidden="true"></span>
                  <strong><?= e($sevLabel) ?></strong>
                </span>
                <?php if ($title !== ''): ?>
                  <p class="trafic-disruption__title"><?= e($title) ?></p>
                <?php endif; ?>
                <?php if ($shortMsg !== ''): ?>
                  <p class="trafic-disruption__msg"><?= e($shortMsg) ?></p>
                <?php endif; ?>
              </li>
            <?php endforeach; ?>
          </ul>
        </li>
      <?php endforeach; ?>
    </ul>

    <?php if (!empty($linesNormal)): ?>
      <p class="trafic-block__footer">
        <span class="trafic-block__footer-icon" aria-hidden="true">✓</span>
        Trafic normal sur les lignes <?= e(implode(', ', $linesNormal)) ?>.
      </p>
    <?php endif; ?>

  </section>
<?php endif; ?>
