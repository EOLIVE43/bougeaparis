<?php
/**
 * Layout de base - squelette HTML de toutes les pages
 *
 * Variables disponibles :
 *   $site      : config du site
 *   $nav       : config de navigation
 *   $ads       : config AdSense
 *   $analytics : config analytics (GSC + GA4)
 *   $content   : contenu HTML de la page
 *   $seo       : instance Seo pour rendu du <head>
 */
?><!DOCTYPE html>
<html lang="<?= e($site['language']) ?>">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <?= $seo->renderHead() ?>
<?php if (!empty($analytics['gsc_enabled']) && !empty($analytics['gsc_verification_code'])): ?>
    <meta name="google-site-verification" content="<?= e($analytics['gsc_verification_code']) ?>">
<?php endif; ?>

<?php if (!empty($analytics['ga4_enabled']) && !empty($analytics['ga4_measurement_id'])): ?>
    <!-- Google Consent Mode v2 (initialise AVANT le chargement de gtag.js) -->
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('consent', 'default', {
            'ad_storage': 'denied',
            'ad_user_data': 'denied',
            'ad_personalization': 'denied',
            'analytics_storage': 'denied',
            'functionality_storage': 'granted',
            'security_storage': 'granted',
            'wait_for_update': 500
        });
        var bpConsent = localStorage.getItem('bp_consent');
        if (bpConsent === 'granted') {
            gtag('consent', 'update', {
                'ad_storage': 'granted',
                'ad_user_data': 'granted',
                'ad_personalization': 'granted',
                'analytics_storage': 'granted'
            });
        }
    </script>
    <!-- Google Analytics 4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=<?= e($analytics['ga4_measurement_id']) ?>"></script>
    <script>
        gtag('js', new Date());
        gtag('config', '<?= e($analytics['ga4_measurement_id']) ?>', {
            'anonymize_ip': true
        });
    </script>
<?php endif; ?>

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
    <link rel="stylesheet" href="/assets/css/icons.css">
<?php if (!empty($analytics['cookie_banner_enabled'])): ?>
    <link rel="stylesheet" href="/assets/css/cookie-banner.css">
<?php endif; ?>
    <!-- RSS (blog) -->
    <link rel="alternate" type="application/rss+xml" title="<?= e($site['brand_name']) ?> - Blog" href="/blog/rss.xml">
    <!-- AdSense script global (si active) -->
    <?php if ($ads['enabled'] && !empty($ads['publisher_id'])): ?>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=<?= e($ads['publisher_id']) ?>" crossorigin="anonymous"></script>
    <?php endif; ?>
    <!-- Preconnect pour performance -->
    <link rel="preconnect" href="https://api-adresse.data.gouv.fr">
<?php if (!empty($analytics['ga4_enabled'])): ?>
    <link rel="preconnect" href="https://www.googletagmanager.com">
    <link rel="preconnect" href="https://www.google-analytics.com">
<?php endif; ?>
</head>
<body>
<?php $tpl->partial('layout/header'); ?>
<main class="main" id="main">
    <?= $content ?>
</main>
<?php $tpl->partial('layout/footer'); ?>

<?php if (!empty($analytics['cookie_banner_enabled'])): ?>
<?php $tpl->partial('components/cookie-banner'); ?>
<?php endif; ?>

<script src="/assets/js/main.js" defer></script>
</body>
</html>
