<?php
/**
 * Page d'accueil
 *
 * Version Livraison 1 : structure minimale propre.
 * La home enrichie (widget itineraire, trafic live, blog) viendra en Livraison 3.
 */
?>
<section class="hero">
    <div class="container">
        <h1 class="hero__title">Tous les transports de Paris et d'Ile-de-France</h1>
        <p class="hero__subtitle">Metro, RER, bus, tramway, aeroports : horaires, itineraires et trafic en temps reel. Pour les Parisiens qui se deplacent comme pour les visiteurs qui decouvrent.</p>
    </div>
</section>

<?php include __DIR__ . '/../ads/slot-header.php'; ?>

<section class="section">
    <div class="container">
        <h2 class="section__title">Les transports franciliens</h2>
        <p class="section__intro">Choisissez votre mode de transport pour acceder au guide detaille : lignes, stations, horaires et infos pratiques.</p>

        <div class="mode-grid">
            <?php foreach ($nav['main'] as $item): if ($item['url'] === '/blog/') continue; ?>
            <a href="<?= e($item['url']) ?>" class="mode-card mode-card--<?= e($item['icon']) ?>">
                <span class="mode-card__label"><?= e($item['label']) ?></span>
                <span class="mode-card__arrow" aria-hidden="true">&rarr;</span>
            </a>
            <?php endforeach; ?>
        </div>
    </div>
</section>

<?php include __DIR__ . '/../ads/slot-in-article.php'; ?>

<section class="section section--alt">
    <div class="container">
        <h2 class="section__title">Le blog BougeaParis</h2>
        <p class="section__intro">Actualite des transports parisiens, trafic, travaux, nouveautes du reseau et conseils pratiques mis a jour quotidiennement.</p>
        <p class="section__cta">
            <a href="/blog/" class="btn btn--primary">Decouvrir le blog</a>
        </p>
    </div>
</section>

<?php include __DIR__ . '/../ads/slot-footer.php'; ?>
