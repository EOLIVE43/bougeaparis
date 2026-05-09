<?php
/**
 * Page Mentions légales
 */
$tpl->seo
    ->setTitle('Mentions légales')
    ->setDescription("Mentions légales de BougeaParis.fr : éditeur, hébergeur, marques RATP/IDFM/SNCF citées (article L713-6 CPI), données personnelles RGPD, cookies, contact. Site indépendant non affilié.")
    ->setCanonical('/mentions-legales/')
    ->setBreadcrumb([
        ['label' => 'Accueil', 'url' => '/'],
        ['label' => 'Mentions légales', 'url' => '/mentions-legales/'],
    ]);
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
            Adresse : 43100 BRIOUDE, France<br>
            Email : <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>
        </p>
        <p><em>Directeur de la publication : Ludovic L.</em></p>
        <p style="font-size:0.85em;color:var(--color-text-muted, #5A6B66);">
            <em>Forme juridique et numéro SIRET : <span style="background:#FFF6CC;padding:2px 6px;">à compléter</span></em>
        </p>

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
        <p>Les noms et logos des lignes de transport en commun d'Île-de-France mentionnés sur ce site sont des marques déposées par la <strong>RATP</strong>, <strong>Île-de-France Mobilités (IDFM)</strong> ou la <strong>SNCF</strong> auprès de l'INPI :</p>
        <ul>
            <li><strong>Métro :</strong> lignes 1, 2, 3, 3bis, 4, 5, 6, 7, 7bis, 8, 9, 10, 11, 12, 13, 14</li>
            <li><strong>RER :</strong> A, B, C, D, E</li>
            <li><strong>Tramway :</strong> T1 à T13 (selon mises en service)</li>
            <li><strong>Bus :</strong> lignes RATP et autres réseaux franciliens</li>
            <li><strong>Transilien SNCF :</strong> H, J, K, L, N, P, R, U</li>
            <li><strong>Noctilien :</strong> N01 à N153</li>
        </ul>
        <p>Les <strong>pastilles colorées numérotées</strong>, leurs <strong>couleurs officielles</strong> (issues de la charte signalétique IDFM/RATP publique) et la <strong>signalétique associée</strong> sont des éléments protégés.</p>
        <p>Leur reproduction sur BougeaParis.fr est faite à <strong>titre informatif et éditorial</strong>, dans le cadre prévu par l'<a href="https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006279708/" target="_blank" rel="noopener">article L713-6 du Code de la propriété intellectuelle</a> (référence nécessaire à la marque pour décrire un service). Cette utilisation ne crée aucune intention de confusion avec les sites officiels et ne constitue pas une appropriation des marques concernées.</p>
        <p>La police <strong>« Parisine »</strong>, marque déposée par la RATP, <strong>n'est pas utilisée</strong> sur ce site. Le rendu des pastilles est réalisé avec une police générique sans-serif (system-ui, Segoe UI, Roboto, Helvetica, Arial).</p>
        <p>Aucune <strong>reproduction de la carte officielle</strong> du réseau RATP n'est effectuée sur ce site. Les plans de ligne affichés sont des représentations linéaires éditoriales originales générées dynamiquement à partir de nos données.</p>
        <p>BougeaParis.fr <strong>n'est pas affilié</strong> à la RATP, IDFM, SNCF ou à aucun autre opérateur de transport. Pour les services officiels, consultez :</p>
        <ul>
            <li><a href="https://www.ratp.fr/" target="_blank" rel="noopener">www.ratp.fr</a> — site officiel RATP</li>
            <li><a href="https://www.iledefrance-mobilites.fr/" target="_blank" rel="noopener">www.iledefrance-mobilites.fr</a> — Île-de-France Mobilités</li>
            <li><a href="https://www.transilien.com/" target="_blank" rel="noopener">www.transilien.com</a> — SNCF Transilien</li>
        </ul>

        <h2>Indépendance éditoriale</h2>
        <p>BougeaParis.fr est un site <strong>indépendant</strong>. Il n'est affilié ni à la RATP, ni à la SNCF, ni à Île-de-France Mobilités, ni à aucun autre opérateur de transport. Les informations publiées sont issues des données ouvertes officielles et de notre veille éditoriale.</p>

        <h2>Données et API</h2>
        <p>Les informations de trafic, horaires et itinéraires présentées sur ce site sont issues des API publiques de PRIM (Île-de-France Mobilités) et de data.iledefrance-mobilites.fr, sous licence ODbL.</p>

        <h2>Données personnelles (RGPD)</h2>
        <p>BougeaParis.fr <strong>ne collecte aucune donnée personnelle</strong> de ses visiteurs :</p>
        <ul>
            <li>Pas de formulaire utilisateur</li>
            <li>Pas de compte utilisateur</li>
            <li>Pas de newsletter</li>
            <li>Pas de tracking publicitaire</li>
        </ul>
        <p>Si vous nous contactez par email à <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>, votre adresse email sera utilisée uniquement pour répondre à votre demande, conformément au RGPD.</p>

        <h2>Cookies</h2>
        <p>Le site BougeaParis.fr <strong>n'utilise pas de cookies de tracking</strong>. Seuls les cookies strictement nécessaires au fonctionnement technique du site peuvent être déposés (préférences d'affichage, état de session). Aucun cookie publicitaire ou d'analyse comportementale n'est utilisé.</p>
        <p style="font-size:0.85em;color:var(--color-text-muted, #5A6B66);">
            <em>Si Google Analytics, Google Search Console ou un autre tracker venait à être activé : <span style="background:#FFF6CC;padding:2px 6px;">à compléter avec le détail des cookies utilisés et la procédure de consentement</span></em>
        </p>

        <h2>Responsabilité</h2>
        <p>Malgré tout le soin apporté à la rédaction de ce site, des erreurs peuvent subsister. BougeaParis.fr ne saurait être tenu responsable des inexactitudes qui pourraient s'y trouver ni des conséquences d'une utilisation des informations qui y sont publiées. Pour toute information critique (dernier train, correspondance cruciale, etc.), nous vous invitons à vérifier auprès des opérateurs officiels.</p>

        <h2>Contact</h2>
        <p>Pour toute question juridique, signalement de contenu, demande de retrait, ou question sur le traitement des données : <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a></p>

        <h2>Droit applicable</h2>
        <p>Les présentes mentions légales sont régies par le <strong>droit français</strong>. En cas de litige, les <strong>tribunaux français</strong> seront seuls compétents.</p>
    </div>
</section>
