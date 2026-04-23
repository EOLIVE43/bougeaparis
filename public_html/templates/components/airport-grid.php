<?php
$airports = $props['airports'] ?? [];
$linkBase = $props['link_base'] ?? '/aeroports/';

if (empty($airports)) return;
?>
<div class="airport-grid" role="list" aria-label="Aeroports de Paris">
    <?php foreach ($airports as $airport):
        $slug      = $airport['slug']              ?? '';
        $name      = $airport['name']              ?? '';
        $code      = $airport['code_iata']         ?? '';
        $terminals = $airport['terminals']         ?? 0;
        $distance  = $airport['distance_paris_km'] ?? '';
    ?>
        <a href="<?= htmlspecialchars($linkBase . $slug . '/') ?>"
           class="airport-grid__item"
           role="listitem"
           aria-label="<?= htmlspecialchars($name) ?>">
            <div class="airport-grid__badge">
                <span class="airport-grid__code"><?= htmlspecialchars($code) ?></span>
            </div>
            <div class="airport-grid__info">
                <h3 class="airport-grid__name"><?= htmlspecialchars($name) ?></h3>
                <p class="airport-grid__meta">
                    <?= $terminals ?> terminaux &middot; <?= $distance ?> km de Paris
                </p>
            </div>
        </a>
    <?php endforeach; ?>
</div>
