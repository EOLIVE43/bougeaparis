<?php
/**
 * Composant traffic-widget
 *
 * Affiche l'état du trafic du jour pour un cocon, une ligne ou une station.
 * Lit /data/traffic/YYYY-MM-DD.json et filtre selon le contexte.
 */

$mode         = $props['mode']          ?? 'cocon';
$cocon        = $props['cocon']         ?? null;
$lineSlug     = $props['line_slug']     ?? null;
$stationLines = $props['station_lines'] ?? [];
$compact      = $props['compact']       ?? false;

$today = date('Y-m-d');
$jsonPath = __DIR__ . '/../../data/traffic/' . $today . '.json';

if (!file_exists($jsonPath)) {
    $files = glob(__DIR__ . '/../../data/traffic/*.json');
    if (!empty($files)) {
        rsort($files);
        $jsonPath = $files[0];
    } else {
        return;
    }
}

$data = json_decode(file_get_contents($jsonPath), true);
if (!$data || empty($data['lines'])) {
    return;
}

$allLines   = $data['lines'];
$articleUrl = $data['article_url'] ?? '/blog/';
$dateData   = $data['date'] ?? $today;
$lastUpdate = $data['last_update'] ?? '';
$isToday    = ($dateData === $today);

$relevantLines = [];

if ($mode === 'cocon' && $cocon) {
    $prefix = ($cocon === 'tramway') ? 'tram-' : $cocon . '-';
    foreach ($allLines as $slug => $info) {
        if (str_starts_with($slug, $prefix)) {
            $relevantLines[$slug] = $info;
        }
    }
} elseif ($mode === 'line' && $lineSlug) {
    if (isset($allLines[$lineSlug])) {
        $relevantLines[$lineSlug] = $allLines[$lineSlug];
    }
} elseif ($mode === 'station' && !empty($stationLines)) {
    foreach ($stationLines as $slug) {
        if (isset($allLines[$slug])) {
            $relevantLines[$slug] = $allLines[$slug];
        }
    }
}

if (empty($relevantLines)) {
    return;
}

$disruptedCount   = 0;
$interruptedCount = 0;
$normalCount      = 0;

foreach ($relevantLines as $info) {
    switch ($info['status'] ?? 'normal') {
        case 'disrupted':    $disruptedCount++;   break;
        case 'interrupted':  $interruptedCount++; break;
        default:             $normalCount++;
    }
}

$totalCount = count($relevantLines);
$allNormal  = ($normalCount === $totalCount);

if ($interruptedCount > 0) {
    $globalStatus = 'interrupted';
} elseif ($disruptedCount > 0) {
    $globalStatus = 'disrupted';
} else {
    $globalStatus = 'normal';
}

$updateTime = '';
if ($lastUpdate) {
    $ts = strtotime($lastUpdate);
    if ($ts) { $updateTime = date('H\hi', $ts); }
}

$title = 'Trafic du jour';
if ($mode === 'cocon') {
    $cocons = [
        'metro'      => 'du métro',
        'rer'        => 'du RER',
        'bus'        => 'des bus',
        'tramway'    => 'des tramways',
        'transilien' => 'des Transilien',
    ];
    $title = 'Trafic ' . ($cocons[$cocon] ?? '') . ' aujourd\'hui';
} elseif ($mode === 'line' && !empty($lineSlug)) {
    $title = 'Aujourd\'hui sur la ligne';
}
?>

<aside class="traffic-widget traffic-widget--<?= $globalStatus ?><?= $compact ? ' traffic-widget--compact' : '' ?>" aria-label="<?= htmlspecialchars($title) ?>">
    <header class="traffic-widget__header">
        <span class="traffic-widget__dot traffic-widget__dot--<?= $globalStatus ?>" aria-hidden="true"></span>
        <h2 class="traffic-widget__title"><?= htmlspecialchars($title) ?></h2>
        <?php if ($updateTime): ?>
            <span class="traffic-widget__update">Mis à jour à <?= $updateTime ?></span>
        <?php endif; ?>
    </header>

    <?php if ($allNormal): ?>
        <p class="traffic-widget__summary traffic-widget__summary--normal">
            <strong>Trafic normal</strong> sur l'ensemble des lignes.
            <span class="traffic-widget__count"><?= $totalCount ?> ligne<?= $totalCount > 1 ? 's' : '' ?> en service.</span>
        </p>
    <?php else: ?>
        <p class="traffic-widget__summary traffic-widget__summary--disrupted">
            <strong><?= ($disruptedCount + $interruptedCount) ?> ligne<?= ($disruptedCount + $interruptedCount) > 1 ? 's' : '' ?> perturbée<?= ($disruptedCount + $interruptedCount) > 1 ? 's' : '' ?></strong>
            <?php if ($normalCount > 0): ?>
                sur <?= $totalCount ?>. Les autres lignes circulent normalement.
            <?php endif; ?>
        </p>

        <ul class="traffic-widget__lines">
            <?php foreach ($relevantLines as $slug => $info):
                $status = $info['status'] ?? 'normal';
                if ($status === 'normal') continue;
                $label = strtoupper(str_replace('-', ' ', $slug));
            ?>
                <li class="traffic-widget__line traffic-widget__line--<?= $status ?>">
                    <span class="traffic-widget__line-dot traffic-widget__line-dot--<?= $status ?>" aria-hidden="true"></span>
                    <div class="traffic-widget__line-body">
                        <strong class="traffic-widget__line-name"><?= htmlspecialchars($label) ?></strong>
                        <?php if (!empty($info['message'])): ?>
                            <p class="traffic-widget__line-message"><?= htmlspecialchars($info['message']) ?></p>
                        <?php endif; ?>
                    </div>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>

    <footer class="traffic-widget__footer">
        <a href="<?= htmlspecialchars($articleUrl) ?>" class="traffic-widget__link">
            Voir l'article complet du jour
            <span aria-hidden="true">&rarr;</span>
        </a>
        <?php if (!$isToday): ?>
            <span class="traffic-widget__warning">Données du <?= date('d/m/Y', strtotime($dateData)) ?></span>
        <?php endif; ?>
    </footer>
</aside>
