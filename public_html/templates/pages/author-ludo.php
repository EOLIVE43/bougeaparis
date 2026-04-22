<?php
/**
 * Page auteur - Ludo
 */
$author = Config::get('authors.ludo');
?>
<nav class="breadcrumb" aria-label="Fil d'Ariane">
    <div class="container">
        <ol class="breadcrumb__list">
            <li><a href="/">Accueil</a></li>
            <li><a href="/blog/">Blog</a></li>
            <li class="breadcrumb__current"><?= e($author['name']) ?></li>
        </ol>
    </div>
</nav>

<section class="hero">
    <div class="container" style="display:flex; align-items:center; gap:1.5rem;">
        <img src="<?= e($author['avatar']) ?>" alt="<?= e($author['name']) ?>" width="96" height="96" style="border-radius:50%; flex-shrink:0;">
        <div>
            <h1 class="hero__title" style="margin-bottom:0.25rem;"><?= e($author['name']) ?></h1>
            <p class="hero__subtitle" style="margin:0;"><?= e($author['role']) ?> - <?= e($author['bio']) ?></p>
        </div>
    </div>
</section>

<section class="section">
    <div class="container" style="max-width:800px;">
        <h2>Specialites</h2>
        <p>Ludo se concentre sur les sujets suivants :</p>
        <ul>
            <?php foreach ($author['specialties'] as $specialty): ?>
            <li><?= e(ucfirst($specialty)) ?></li>
            <?php endforeach; ?>
        </ul>

        <h2>Articles recents</h2>
        <p class="text-muted">Les premiers articles signes par Ludo seront publies tres prochainement.</p>
    </div>
</section>

<?php
// Schema.org Person
$tpl->seo->addSchema([
    '@context'    => 'https://schema.org',
    '@type'       => 'Person',
    'name'        => $author['name'],
    'description' => $author['bio'],
    'url'         => url($author['url']),
    'image'       => url($author['avatar']),
    'jobTitle'    => $author['role'],
    'worksFor'    => [
        '@type' => 'Organization',
        'name'  => $site['brand_name'],
        'url'   => $site['url'],
    ],
]);
?>
