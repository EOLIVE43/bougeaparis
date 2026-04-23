<?php
/**
 * Layout de base - version optimisee perf (bundle CSS + lazy gtag)
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
    <!-- Google Consent Mode v2 (initialise AVANT gtag.js, non bloquant) -->
    <script>
    window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
    gtag('consent','default',{'ad_storage':'denied','ad_user_data':'denied','ad_personalization':'denied','analytics_storage':'denied','functionality_storage':'granted','security_storage':'granted','wait_for_update':500});
    try{if(localStorage.getItem('bp_consent')==='granted'){gtag('consent','update',{'ad_storage':'granted','ad_user_data':'granted','ad_personalization':'granted','analytics_storage':'granted'});}}catch(e){}
    </script>
<?php endif; ?>

    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="<?= e($site['favicon']) ?>">
    <link rel="apple-touch-icon" href="<?= e($site['favicon_png']) ?>">

    <!-- Bundle CSS unique (fusion des 8 CSS) -->
    <link rel="stylesheet" href="/assets/css/bundle.css">

    <!-- RSS (blog) -->
    <link rel="alternate" type="application/rss+xml" title="<?= e($site['brand_name']) ?> - Blog" href="/blog/rss.xml">

    <!-- AdSense script global (si active) -->
    <?php if ($ads['enabled'] && !empty($ads['publisher_id'])): ?>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=<?= e($ads['publisher_id']) ?>" crossorigin="anonymous"></script>
    <?php endif; ?>

    <!-- Preconnect pour performance -->
    <link rel="preconnect" href="https://api-adresse.data.gouv.fr">
<?php if (!empty($analytics['ga4_enabled'])): ?>
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
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

<?php if (!empty($analytics['ga4_enabled']) && !empty($analytics['ga4_measurement_id'])): ?>
<!-- Lazy loading GA4 : charge apres interaction ou au bout de 5 secondes -->
<script>
(function(){
    var loaded=false;
    function loadGA(){
        if(loaded)return;loaded=true;
        var s=document.createElement('script');
        s.async=true;
        s.src='https://www.googletagmanager.com/gtag/js?id=<?= e($analytics['ga4_measurement_id']) ?>';
        document.head.appendChild(s);
        s.onload=function(){
            gtag('js',new Date());
            gtag('config','<?= e($analytics['ga4_measurement_id']) ?>',{'anonymize_ip':true});
        };
    }
    var events=['scroll','mousemove','touchstart','click','keydown'];
    var trigger=function(){events.forEach(function(e){window.removeEventListener(e,trigger,{passive:true});});loadGA();};
    events.forEach(function(e){window.addEventListener(e,trigger,{passive:true,once:true});});
    setTimeout(loadGA,5000);
})();
</script>
<?php endif; ?>

</body>
</html>
