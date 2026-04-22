<?php
/**
 * Page Mentions legales
 */
?>
<nav class="breadcrumb" aria-label="Fil d'Ariane">
    <div class="container">
        <ol class="breadcrumb__list">
            <li><a href="/">Accueil</a></li>
            <li class="breadcrumb__current">Mentions legales</li>
        </ol>
    </div>
</nav>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">Mentions legales</h1>
    </div>
</section>

<section class="section">
    <div class="container" style="max-width:800px;">

        <h2>Editeur du site</h2>
        <p>
            <strong>BougeaParis.fr</strong><br>
            Site edite par Ludovic [NOM A COMPLETER]<br>
            Adresse : [ADRESSE A COMPLETER]<br>
            Email : <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>
        </p>

        <p><em>Directeur de la publication : Ludovic [NOM A COMPLETER]</em></p>

        <h2>Hebergement</h2>
        <p>
            <strong>o2switch</strong><br>
            SAS au capital social de 100 000 euros<br>
            RCS Clermont-Ferrand 510 909 807<br>
            Chem. des Pardiaux, 63000 Clermont-Ferrand<br>
            Telephone : 04 44 44 60 40<br>
            <a href="https://www.o2switch.fr" target="_blank" rel="noopener">www.o2switch.fr</a>
        </p>

        <h2>Propriete intellectuelle</h2>
        <p>L'ensemble des textes, illustrations et elements graphiques presents sur BougeaParis.fr sont la propriete exclusive de l'editeur, sauf mention contraire. Toute reproduction, totale ou partielle, est interdite sans autorisation prealable.</p>

        <p>Les noms de lignes (M1, RER A, T3, etc.), leurs numeros et les couleurs associees sont des elements d'information voyageur publics utilises dans un but informatif. Ils sont issus des donnees ouvertes d'Ile-de-France Mobilites et ne constituent en aucun cas une appropriation de marques ou de chartes graphiques tierces.</p>

        <h2>Independance editoriale</h2>
        <p>BougeaParis.fr est un site <strong>independant</strong>. Il n'est affilie ni a la RATP, ni a la SNCF, ni a Ile-de-France Mobilites, ni a aucun autre operateur de transport. Les informations publiees sont issues des donnees ouvertes officielles et de notre veille editoriale.</p>

        <h2>Donnees et API</h2>
        <p>Les informations de trafic, horaires et itineraires presentees sur ce site sont issues des API publiques de PRIM (Ile-de-France Mobilites) et de data.iledefrance-mobilites.fr, sous licence ODbL.</p>

        <h2>Responsabilite</h2>
        <p>Malgre tout le soin apporte a la redaction de ce site, des erreurs peuvent subsister. BougeaParis.fr ne saurait etre tenu responsable des inexactitudes qui pourraient s'y trouver ni des consequences d'une utilisation des informations qui y sont publiees. Pour toute information critique (dernier train, correspondance cruciale, etc.), nous vous invitons a verifier aupres des operateurs officiels.</p>

        <h2>Droit applicable</h2>
        <p>Les presentes mentions legales sont regies par le droit francais. En cas de litige, les tribunaux francais seront seuls competents.</p>

    </div>
</section>
