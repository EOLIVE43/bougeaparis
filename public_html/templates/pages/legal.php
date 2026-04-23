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
        <p>L'ensemble des textes, illustrations et éléments graphiques présents sur BougeaParis.fr sont la propriété exclusive de l'éditeur, sauf mention contraire. Toute reproduction, totale ou partielle, est interdite sans autorisation préalable.</p>
        <p>Les noms de lignes (M1, RER A, T3, etc.), leurs numéros et les couleurs associées sont des éléments d'information voyageur publics utilisés dans un but informatif. Ils sont issus des données ouvertes d'Île-de-France Mobilités et ne constituent en aucun cas une appropriation de marques ou de chartes graphiques tierces.</p>

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
