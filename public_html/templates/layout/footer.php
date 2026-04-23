<?php
/**
 * Footer commun à toutes les pages
 * 3 colonnes de liens + mention non-officiel obligatoire + copyright
 */
$year = date('Y');
?>
<footer class="site-footer" role="contentinfo">
    <div class="container">
        <div class="site-footer__cols">
            <div class="site-footer__col site-footer__col--brand">
                <div class="site-footer__logo">
                    <span class="site-logo__mark site-logo__mark--sm" aria-hidden="true">B</span>
                    <span class="site-logo__name site-logo__name--sm">Bougea<span class="site-logo__name-accent">Paris</span><span class="site-logo__tld">.fr</span></span>
                </div>
                <p class="site-footer__baseline"><?= e($site['description']) ?></p>
            </div>
            <div class="site-footer__col">
                <h2 class="site-footer__heading">Découvrir</h2>
                <ul class="site-footer__list">
                    <?php foreach ($nav['footer_discover'] as $link): ?>
                    <li><a href="<?= e($link['url']) ?>"><?= e($link['label']) ?></a></li>
                    <?php endforeach; ?>
                </ul>
            </div>
            <div class="site-footer__col">
                <h2 class="site-footer__heading">Outils</h2>
                <ul class="site-footer__list">
                    <?php foreach ($nav['footer_tools'] as $link): ?>
                    <li><a href="<?= e($link['url']) ?>"><?= e($link['label']) ?></a></li>
                    <?php endforeach; ?>
                </ul>
            </div>
            <div class="site-footer__col">
                <h2 class="site-footer__heading">À propos</h2>
                <ul class="site-footer__list">
                    <?php foreach ($nav['footer_about'] as $link): ?>
                    <li><a href="<?= e($link['url']) ?>"><?= e($link['label']) ?></a></li>
                    <?php endforeach; ?>
                </ul>
                <p class="site-footer__contact">
                    <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>
                </p>
            </div>
        </div>
        <div class="site-footer__legal">
            <p class="site-footer__notice"><?= e($site['non_official_notice']) ?></p>
            <p class="site-footer__copy">&copy; <?= $year ?> <?= e($site['brand_name']) ?> &mdash; Tous droits réservés.</p>
        </div>
    </div>
</footer>
