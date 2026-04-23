<?php
/**
 * Page Politique de confidentialité
 */
?>

<nav class="breadcrumb" aria-label="Fil d'Ariane">
    <div class="container">
        <ol class="breadcrumb__list">
            <li><a href="/">Accueil</a></li>
            <li class="breadcrumb__current">Confidentialité</li>
        </ol>
    </div>
</nav>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">Politique de confidentialité</h1>
    </div>
</section>

<section class="section">
    <div class="container" style="max-width:800px;">
        <p class="text-muted"><small>Dernière mise à jour : <?= date('d/m/Y') ?></small></p>

        <h2>Données collectées</h2>
        <p>BougeaParis.fr collecte le minimum de données nécessaires à son fonctionnement. Nous ne demandons aucune création de compte pour consulter le site.</p>

        <h3>Données collectées automatiquement</h3>
        <ul>
            <li><strong>Données techniques</strong> : adresse IP, navigateur, système d'exploitation, pages visitées. Ces données sont collectées via les logs serveur pour des raisons de sécurité et conservées 12 mois maximum.</li>
            <li><strong>Cookies</strong> : voir section dédiée ci-dessous.</li>
        </ul>

        <h3>Données que vous nous transmettez</h3>
        <ul>
            <li><strong>Contact par email</strong> : si vous nous écrivez, nous conservons votre email et votre message pour répondre à votre demande.</li>
        </ul>

        <h2>Cookies</h2>
        <p>BougeaParis.fr utilise des cookies pour améliorer votre expérience :</p>

        <h3>Cookies essentiels</h3>
        <p>Ces cookies sont nécessaires au fonctionnement du site (mémoriser vos préférences d'affichage, session technique). Ils ne peuvent pas être désactivés.</p>

        <h3>Cookies de mesure d'audience</h3>
        <p>Nous pouvons utiliser des outils de mesure d'audience (Google Analytics, Plausible, etc.) pour comprendre comment vous utilisez le site. Ces outils sont configurés de façon à respecter votre vie privée.</p>

        <h3>Cookies publicitaires</h3>
        <p>Lorsque la publicité sera activée sur le site (via Google AdSense), des cookies publicitaires pourront être déposés. Vous pouvez à tout moment gérer vos préférences publicitaires via les paramètres de Google (<a href="https://myadcenter.google.com/" target="_blank" rel="noopener">myadcenter.google.com</a>).</p>

        <h2>Vos droits (RGPD)</h2>
        <p>Conformément au Règlement Général sur la Protection des Données (RGPD) et à la loi Informatique et Libertés, vous disposez des droits suivants :</p>
        <ul>
            <li>Droit d'accès à vos données personnelles</li>
            <li>Droit de rectification</li>
            <li>Droit à l'effacement (droit à l'oubli)</li>
            <li>Droit à la portabilité</li>
            <li>Droit d'opposition au traitement</li>
            <li>Droit de limitation du traitement</li>
        </ul>
        <p>Pour exercer ces droits, contactez-nous à <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>.</p>
        <p>Vous avez également le droit d'introduire une réclamation auprès de la CNIL : <a href="https://www.cnil.fr" target="_blank" rel="noopener">www.cnil.fr</a>.</p>

        <h2>Partage de données</h2>
        <p>Nous ne vendons ni ne louons vos données personnelles. Elles peuvent être partagées uniquement avec :</p>
        <ul>
            <li>Notre hébergeur (o2switch) dans le cadre strict du fonctionnement technique du site</li>
            <li>Les autorités compétentes si la loi nous y oblige</li>
        </ul>

        <h2>Contact</h2>
        <p>Pour toute question concernant cette politique de confidentialité, écrivez à <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>.</p>
    </div>
</section>
