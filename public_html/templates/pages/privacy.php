<?php
/**
 * Page Politique de confidentialite
 */
?>
<nav class="breadcrumb" aria-label="Fil d'Ariane">
    <div class="container">
        <ol class="breadcrumb__list">
            <li><a href="/">Accueil</a></li>
            <li class="breadcrumb__current">Confidentialite</li>
        </ol>
    </div>
</nav>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">Politique de confidentialite</h1>
    </div>
</section>

<section class="section">
    <div class="container" style="max-width:800px;">

        <p class="text-muted"><small>Derniere mise a jour : <?= date('d/m/Y') ?></small></p>

        <h2>Donnees collectees</h2>
        <p>BougeaParis.fr collecte le minimum de donnees necessaires a son fonctionnement. Nous ne demandons aucune creation de compte pour consulter le site.</p>

        <h3>Donnees collectees automatiquement</h3>
        <ul>
            <li><strong>Donnees techniques</strong> : adresse IP, navigateur, systeme d'exploitation, pages visitees. Ces donnees sont collectees via les logs serveur pour des raisons de securite et conservees 12 mois maximum.</li>
            <li><strong>Cookies</strong> : voir section dediee ci-dessous.</li>
        </ul>

        <h3>Donnees que vous nous transmettez</h3>
        <ul>
            <li><strong>Contact par email</strong> : si vous nous ecrivez, nous conservons votre email et votre message pour repondre a votre demande.</li>
        </ul>

        <h2>Cookies</h2>
        <p>BougeaParis.fr utilise des cookies pour ameliorer votre experience :</p>

        <h3>Cookies essentiels</h3>
        <p>Ces cookies sont necessaires au fonctionnement du site (memoriser vos preferences d'affichage, session technique). Ils ne peuvent pas etre desactives.</p>

        <h3>Cookies de mesure d'audience</h3>
        <p>Nous pouvons utiliser des outils de mesure d'audience (Google Analytics, Plausible, etc.) pour comprendre comment vous utilisez le site. Ces outils sont configures de facon a respecter votre vie privee.</p>

        <h3>Cookies publicitaires</h3>
        <p>Lorsque la publicite sera activee sur le site (via Google AdSense), des cookies publicitaires pourront etre deposes. Vous pouvez a tout moment gerer vos preferences publicitaires via les parametres de Google (<a href="https://myadcenter.google.com/" target="_blank" rel="noopener">myadcenter.google.com</a>).</p>

        <h2>Vos droits (RGPD)</h2>
        <p>Conformement au Reglement General sur la Protection des Donnees (RGPD) et a la loi Informatique et Libertes, vous disposez des droits suivants :</p>
        <ul>
            <li>Droit d'acces a vos donnees personnelles</li>
            <li>Droit de rectification</li>
            <li>Droit a l'effacement (droit a l'oubli)</li>
            <li>Droit a la portabilite</li>
            <li>Droit d'opposition au traitement</li>
            <li>Droit de limitation du traitement</li>
        </ul>

        <p>Pour exercer ces droits, contactez-nous a <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>.</p>

        <p>Vous avez egalement le droit d'introduire une reclamation aupres de la CNIL : <a href="https://www.cnil.fr" target="_blank" rel="noopener">www.cnil.fr</a>.</p>

        <h2>Partage de donnees</h2>
        <p>Nous ne vendons ni ne louons vos donnees personnelles. Elles peuvent etre partagees uniquement avec :</p>
        <ul>
            <li>Notre hebergeur (o2switch) dans le cadre strict du fonctionnement technique du site</li>
            <li>Les autorites competentes si la loi nous y oblige</li>
        </ul>

        <h2>Contact</h2>
        <p>Pour toute question concernant cette politique de confidentialite, ecrivez a <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>.</p>

    </div>
</section>
