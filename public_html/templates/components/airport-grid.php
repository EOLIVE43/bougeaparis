<?php
/**
 * Composant airport-grid : grille des 3 aeroports parisiens.
 *
 * Props :
 *   - airports     : data/lines.json aeroports
 *   - link_base    : base URL (defaut '/aeroports/')
 *   - enable_links : activer les liens vers pages dediees (defaut false)
 */

$airports     = $props['airports']     ?? [];
$link_base    = $props['link_base']    ?? '/aeroports/';
$enable_links = $props['enable_links'] ?? false;

if (empty($airports)) return;
?>
<ul class="airport-grid" role="list">
    <?php foreach ($airports as $airport):
        $slug    = $airport['slug']    ?? '';
        $code    = $airport['code']    ?? '';
        $name    = $airport['name']    ?? '';
        $city    = $airport['city']    ?? '';
        $distance= $airport['distance_from_paris_km'] ?? null;
        $href    = $link_base . $slug . '/';
    ?>
        <li class="airport-grid__item">
            <span class="airport-grid__badge" aria-hidden="true">
                <span class="airport-grid__code"><?= htmlspecialchars($code) ?></span>
            </span>
            <span class="airport-grid__info">
                <?php if ($enable_links): ?>
                    <a href="<?= htmlspecialchars($href) ?>" class="airport-grid__name airport-grid__name--link"><?= htmlspecialchars($name) ?></a>
                <?php else: ?>
                    <span class="airport-grid__name"><?= htmlspecialchars($name) ?></span>
                <?php endif; ?>
                <?php if ($distance): ?>
                    <p class="airport-grid__meta"><?= $distance ?> km de Paris</p>
                <?php endif; ?>
            </span>
        </li>
    <?php endforeach; ?>
</ul>
