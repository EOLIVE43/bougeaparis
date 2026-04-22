<?php
/**
 * Header commun a toutes les pages
 * Logo + slogan + menu principal
 */
$currentPath = $_SERVER['REQUEST_URI'] ?? '/';
?>
<header class="site-header" role="banner">
    <div class="container site-header__inner">

        <a href="/" class="site-logo" aria-label="<?= e($site['brand_name']) ?> - Accueil">
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
                ?>
                <li class="site-nav__item">
                    <a href="<?= e($item['url']) ?>" class="site-nav__link<?= $isActive ? ' is-active' : '' ?>">
                        <?= e($item['label']) ?>
                    </a>
                </li>
                <?php endforeach; ?>
            </ul>
        </nav>

    </div>
</header>
