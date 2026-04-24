<?php
/**
 * Template : info-trafic-article.php
 *
 * Page d'un article individuel dans /info-trafic/YYYY-MM-DD-slug/
 *
 * Optimise pour :
 * - Google Discover (image 1200px+, NewsArticle schema, E-E-A-T)
 * - Core Web Vitals (image hero fetchpriority=high, dimensions fixees)
 * - SEO (canonical, OG complets, breadcrumb)
 *
 * Donnees attendues :
 *   $article : instance de Article (chargee par le routing)
 */

/** @var Article $article */

// ------ SEO setup ------
$author = $article->getAuthorInfo();
$imageAbsolute = $article->getImage();
if ($imageAbsolute && !str_starts_with($imageAbsolute, 'http')) {
    $imageAbsolute = rtrim($site['url'], '/') . $imageAbsolute;
}

$tpl->seo
    ->setTitle($article->getTitle())
    ->setDescription($article->getExcerpt())
    ->setCanonical($article->getUrl())
    ->setOgType('article')
    ->setOgImage($article->getImage())
    ->setArticle([
        'published' => $article->getDateIso(),
        'modified'  => $article->getDateIso(),
        'author'    => $author['full_name'] ?? $author['name'],
        'section'   => 'Info-Trafic',
    ])
    ->setBreadcrumb([
        ['label' => 'Accueil',       'url' => '/'],
        ['label' => 'Info-Trafic',   'url' => '/info-trafic/'],
        ['label' => $article->getTitle(), 'url' => $article->getUrl()],
    ]);

// Schema NewsArticle complet (critique pour Discover)
$tpl->seo->addSchema([
    '@context' => 'https://schema.org',
    '@type'    => 'NewsArticle',
    'headline' => $article->getTitle(),
    'description' => $article->getExcerpt(),
    'image' => [$imageAbsolute],
    'datePublished' => $article->getDateIso(),
    'dateModified'  => $article->getDateIso(),
    'author' => [
        '@type' => 'Person',
        'name'  => $author['full_name'] ?? $author['name'],
        'url'   => rtrim($site['url'], '/') . ($author['url'] ?? '/'),
    ],
    'publisher' => [
        '@id' => rtrim($site['url'], '/') . '/#organization',
    ],
    'mainEntityOfPage' => [
        '@type' => 'WebPage',
        '@id'   => rtrim($site['url'], '/') . $article->getUrl(),
    ],
    'inLanguage' => 'fr-FR',
    'articleSection' => 'Info-Trafic',
]);

// URLs de partage
$shareUrl = rtrim($site['url'], '/') . $article->getUrl();
$shareTitle = rawurlencode($article->getTitle());
$shareUrlEnc = rawurlencode($shareUrl);
?>

<article class="article">

    <!-- Fil d'Ariane -->
    <nav class="breadcrumb" aria-label="Fil d'Ariane">
        <ol>
            <li><a href="/">Accueil</a></li>
            <li><a href="/info-trafic/">Info-Trafic</a></li>
            <li aria-current="page"><?= e($article->getTitle()) ?></li>
        </ol>
    </nav>

    <!-- En-tete article -->
    <header class="article__header">
        <div class="article__meta-top">
            <span class="article__category">Info-Trafic</span>
            <time class="article__date" datetime="<?= e($article->getDateIso()) ?>">
                <?= e($article->getDateFormatted()) ?>
            </time>
            <span class="article__reading-time"><?= (int) $article->getReadingTime() ?> min de lecture</span>
        </div>

        <h1 class="article__title"><?= e($article->getTitle()) ?></h1>

        <?php if ($article->getExcerpt()): ?>
            <p class="article__excerpt"><?= e($article->getExcerpt()) ?></p>
        <?php endif; ?>

        <div class="article__author-line">
            <span class="article__author-label">Par</span>
            <a href="<?= e($author['url']) ?>" class="article__author-link" rel="author">
                <?= e($author['full_name'] ?? $author['name']) ?>
            </a>
        </div>
    </header>
<!-- Bandeau statut reseau (si stats presentes dans front-matter) -->
    <?php
    $statsBloquante   = (int) ($article->getMeta('stats_bloquante') ?? 0);
    $statsPerturbee   = (int) ($article->getMeta('stats_perturbee') ?? 0);
    $statsInformation = (int) ($article->getMeta('stats_information') ?? 0);
    $statsTotal       = (int) ($article->getMeta('stats_total') ?? 0);
    if ($statsTotal > 0):
    ?>
        <section class="traffic-banner" aria-label="État du réseau aujourd'hui">
            <h2 class="traffic-banner__title">État du réseau aujourd'hui</h2>
            <div class="traffic-banner__stats">
                <div class="traffic-banner__stat traffic-banner__stat--bloquante">
                    <span class="traffic-banner__stat-number"><?= $statsBloquante ?></span>
                    <span class="traffic-banner__stat-label">Trafic interrompu</span>
                </div>
                <div class="traffic-banner__stat traffic-banner__stat--perturbee">
                    <span class="traffic-banner__stat-number"><?= $statsPerturbee ?></span>
                    <span class="traffic-banner__stat-label">Trafic perturbé</span>
                </div>
                <div class="traffic-banner__stat traffic-banner__stat--information">
                    <span class="traffic-banner__stat-number"><?= $statsInformation ?></span>
                    <span class="traffic-banner__stat-label">Information</span>
                </div>
            </div>
            <p class="traffic-banner__source">
                Source : données officielles Île-de-France Mobilités (PRIM) · <?= $statsTotal ?> perturbations recensées
            </p>
        </section>
    <?php endif; ?>
<!-- Widget de recherche de ligne -->
    <?php include __DIR__ . '/../partials/line-search-widget.php'; ?>
    <!-- Image hero (critique pour Discover) -->
    <?php if ($article->getImage()): ?>
        <figure class="article__hero">
            <img src="<?= e($article->getImage()) ?>"
                 alt="<?= e($article->getImageAlt()) ?>"
                 width="1200"
                 height="630"
                 fetchpriority="high"
                 loading="eager"
                 decoding="async">
        </figure>
    <?php endif; ?>

    <!-- Contenu principal -->
    <div class="article__content">
        <?= $article->getHtml() ?>
    </div>

    <!-- Partage social (sans JS externe) -->
    <aside class="article__share" aria-labelledby="share-title">
        <h2 id="share-title" class="article__share-title">Partager cet article</h2>
        <ul class="article__share-list">
            <li>
                <a href="https://www.facebook.com/sharer/sharer.php?u=<?= e($shareUrlEnc) ?>"
                   target="_blank"
                   rel="noopener noreferrer"
                   aria-label="Partager sur Facebook">
                    Facebook
                </a>
            </li>
            <li>
                <a href="https://twitter.com/intent/tweet?url=<?= e($shareUrlEnc) ?>&text=<?= e($shareTitle) ?>"
                   target="_blank"
                   rel="noopener noreferrer"
                   aria-label="Partager sur X (Twitter)">
                    X (Twitter)
                </a>
            </li>
            <li>
                <a href="https://www.linkedin.com/sharing/share-offsite/?url=<?= e($shareUrlEnc) ?>"
                   target="_blank"
                   rel="noopener noreferrer"
                   aria-label="Partager sur LinkedIn">
                    LinkedIn
                </a>
            </li>
            <li>
                <a href="mailto:?subject=<?= e($shareTitle) ?>&body=<?= e($shareUrlEnc) ?>"
                   aria-label="Partager par email">
                    Email
                </a>
            </li>
        </ul>
    </aside>

    <!-- Bio auteur (E-E-A-T pour Discover) -->
    <aside class="article__author-box">
        <h2 class="article__author-box-title">À propos de l'auteur</h2>
        <div class="article__author-box-content">
            <div class="article__author-box-text">
                <h3 class="article__author-box-name">
                    <a href="<?= e($author['url']) ?>" rel="author">
                        <?= e($author['full_name'] ?? $author['name']) ?>
                    </a>
                </h3>
                <p class="article__author-box-bio"><?= e($author['bio'] ?? '') ?></p>
            </div>
        </div>
    </aside>

</article>
