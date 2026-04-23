<?php
/**
 * Layout de base - squelette HTML de toutes les pages
 *
 * Variables disponibles :
 *   $site    : config du site
 *   $nav     : config de navigation
 *   $ads     : config AdSense
 *   $content : contenu HTML de la page
 *   $seo     : instance Seo pour rendu du <head>
 */
?><!DOCTYPE html>
<html lang="<?= e($site['language']) ?>">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <?= $seo->renderHead() ?>

    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="<?= e($site['favicon']) ?>">
    <link rel="apple-touch-icon" href="<?= e($site['favicon_png']) ?>">

    <!-- Feuilles de style -->
    <link rel="stylesheet" href="/assets/css/tokens.css">
    <link rel="stylesheet" href="/assets/css/base.css">
    <link rel="stylesheet" href="/assets/css/layout.css">
    <link rel="stylesheet" href="/assets/css/components.css">
    <link rel="stylesheet" href="/assets/css/ads.css">
    <link rel="stylesheet" href="/assets/css/cocons.css">



    <!-- RSS (blog) -->
    <link rel="alternate" type="application/rss+xml" title="<?= e($site['brand_name']) ?> - Blog" href="/blog/rss.xml">

    <!-- AdSense script global (si active) -->
    <?php if ($ads['enabled'] && !empty($ads['publisher_id'])): ?>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=<?= e($ads['publisher_id']) ?>" crossorigin="anonymous"></script>
    <?php endif; ?>

    <!-- Preconnect pour performance -->
    <link rel="preconnect" href="https://api-adresse.data.gouv.fr">
</head>
<body>

<?php $tpl->partial('layout/header'); ?>

<main class="main" id="main">
    <?= $content ?>
</main>

<?php $tpl->partial('layout/footer'); ?>

<script src="/assets/js/main.js" defer></script>

</body>
</html>
