<?php
/**
 * Header commun a toutes les pages — refonte nav niveau 1 (5 entrees).
 *
 * Mega-menu desktop : :hover/:focus-within sur les items avec children.
 * Mobile : <details>/<summary> natif (zero JS, a11y clavier gratuit).
 *
 * Le markup utilise <details> pour les items avec children. Sur desktop
 * (>=768px), le hover/focus-within revele le sous-menu en position
 * absolute (overlay, zero CLS). Sur mobile (<768px), le <details>
 * fonctionne en accordeon natif via summary click.
 *
 * Styles : bundle.css section "Mega-menu" (above-the-fold -> inline dans
 * critical CSS automatiquement via critical@7 lors du deploy).
 */
$currentPath = $_SERVER['REQUEST_URI'] ?? '/';
?>
<header class="site-header" role="banner">
    <div class="container site-header__inner">
        <a href="/" class="site-logo">
            <span class="site-logo__mark" aria-hidden="true">B</span>
            <span class="site-logo__text">
                <span class="site-logo__name">Bougea<span class="site-logo__name-accent">Paris</span><span class="site-logo__tld">.fr</span></span>
                <span class="site-logo__tagline"><?= e($site['slogan']) ?></span>
            </span>
        </a>

        <button class="site-header__menu-toggle" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="site-nav">
            <span></span><span></span><span></span>
        </button>

        <nav class="site-nav" id="site-nav" aria-label="Navigation principale">
            <ul class="site-nav__list">
                <?php foreach ($nav['main'] as $item):
                    $isActive = $currentPath === $item['url']
                        || ($item['url'] !== '/' && str_starts_with($currentPath, $item['url']));
                    $hasChildren = !empty($item['children']);
                ?>
                <li class="site-nav__item<?= $hasChildren ? ' site-nav__item--has-children' : '' ?>">
                <?php if ($hasChildren): ?>
                    <details class="site-nav__details">
                        <summary class="site-nav__summary<?= $isActive ? ' is-active' : '' ?>"<?= $isActive ? ' aria-current="page"' : '' ?>>
                            <a href="<?= e($item['url']) ?>" class="site-nav__link">
                                <?php $tpl->partial('components/icon-menu', [
                                    'icon' => $item['icon'] ?? 'metro',
                                    'size' => 'md',
                                ]); ?>
                                <span class="site-nav__label"><?= e($item['label']) ?></span>
                            </a>
                            <span class="site-nav__chevron" aria-hidden="true">▾</span>
                        </summary>
                        <ul class="site-nav__submenu" aria-label="Sous-menu <?= e($item['label']) ?>">
                            <?php foreach ($item['children'] as $child): ?>
                            <li class="site-nav__submenu-item">
                                <a href="<?= e($child['url']) ?>" class="site-nav__submenu-link">
                                    <?php if (!empty($child['icon'])): ?>
                                    <?php $tpl->partial('components/icon-menu', [
                                        'icon' => $child['icon'],
                                        'size' => 'md',
                                    ]); ?>
                                    <?php endif; ?>
                                    <span><?= e($child['label']) ?></span>
                                </a>
                            </li>
                            <?php endforeach; ?>
                        </ul>
                    </details>
                <?php else: ?>
                    <a href="<?= e($item['url']) ?>" class="site-nav__link<?= $isActive ? ' is-active' : '' ?>"<?= $isActive ? ' aria-current="page"' : '' ?>>
                        <?php $tpl->partial('components/icon-menu', [
                            'icon' => $item['icon'] ?? 'metro',
                            'size' => 'md',
                        ]); ?>
                        <span class="site-nav__label"><?= e($item['label']) ?></span>
                    </a>
                <?php endif; ?>
                </li>
                <?php endforeach; ?>
            </ul>
        </nav>
    </div>
</header>
