<?php
/**
 * Page Mentions légales
 */
?>

<nav class="breadcrumb" aria-label="Fil d'Ariane">
    <div class="container">
        <ol class="breadcrumb__list">
            <li><a href="/">Accueil</a></li>
            <li class="breadcrumb__current">Mentions légales</li>
        </ol>
    </div>
</nav>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">Mentions légales</h1>
    </div>
</section>

<section class="section">
    <div class="container" style="max-width:800px;">
        <h2>Éditeur du site</h2>
        <p>
            <strong>BougeaParis.fr</strong><br>
            Site édité par Ludovic L.<br>
            Adresse : 43100 BRIOUDE<br>
            Email : <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>
        </p>
        <p><em>Directeur de la publication : Ludovic L.</em></p>

        <h2>Hébergement</h2>
        <p>
            <strong>o2switch</strong><br>
            SAS au capital social de 100 000 euros<br>
            RCS Clermont-Ferrand 510 909 807<br>
            Chem. des Pardiaux, 63000 Clermont-Ferrand<br>
            Téléphone : 04 44 44 60 40<br>
            <a href="https://www.o2switch.fr" target="_blank" rel="noopener">www.o2switch.fr</a>
        </p>

        <h2>Propriété intellectuelle</h2>
        <p>L'ensemble des textes originaux et éléments graphiques propres à BougeaParis.fr sont la propriété exclusive de l'éditeur, sauf mention contraire. Toute reproduction, totale ou partielle, est interdite sans autorisation préalable.</p>

        <h2>Marques et signalétique des transports</h2>
        <p>Les noms et logos des lignes de métro, RER, tramway, bus et Transilien mentionnés sur ce site sont des marques déposées par la <strong>RATP</strong>, <strong>Île-de-France Mobilités (IDFM)</strong> ou la <strong>SNCF</strong>. Les pastilles numérotées des lignes (M1, M4, RER A, T3a, etc.), leurs couleurs officielles et leur charte signalétique sont des éléments protégés.</p>
        <p>Leur reproduction sur BougeaParis.fr est faite à <strong>titre informatif et éditorial</strong>, dans le cadre prévu par l'<a href="https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006279708/" target="_blank" rel="noopener">article L713-6 du Code de la propriété intellectuelle</a> (référence nécessaire à la marque pour décrire un service). Cette utilisation ne crée aucune intention de confusion avec les sites officiels et ne constitue pas une appropriation des marques concernées.</p>
        <p>BougeaParis.fr <strong>n'est pas affilié</strong> à la RATP, IDFM, SNCF ou à aucun autre opérateur de transport.</p>

        <h2>Indépendance éditoriale</h2>
        <p>BougeaParis.fr est un site <strong>indépendant</strong>. Il n'est affilié ni à la RATP, ni à la SNCF, ni à Île-de-France Mobilités, ni à aucun autre opérateur de transport. Les informations publiées sont issues des données ouvertes officielles et de notre veille éditoriale.</p>

        <h2>Données et API</h2>
        <p>Les informations de trafic, horaires et itinéraires présentées sur ce site sont issues des API publiques de PRIM (Île-de-France Mobilités) et de data.iledefrance-mobilites.fr, sous licence ODbL.</p>

        <h2>Responsabilité</h2>
        <p>Malgré tout le soin apporté à la rédaction de ce site, des erreurs peuvent subsister. BougeaParis.fr ne saurait être tenu responsable des inexactitudes qui pourraient s'y trouver ni des conséquences d'une utilisation des informations qui y sont publiées. Pour toute information critique (dernier train, correspondance cruciale, etc.), nous vous invitons à vérifier auprès des opérateurs officiels.</p>

        <h2>Droit applicable</h2>
        <p>Les présentes mentions légales sont régies par le droit français. En cas de litige, les tribunaux français seront seuls compétents.</p>
    </div>
</section>
