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

<?php $tpl->partial('ads/slot-header'); ?>

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
        <p>BougeaParis.fr <strong>ne collecte aucune donnée personnelle directement</strong> via formulaire, compte utilisateur ou abonnement. Le site fait toutefois appel à des services tiers pour la mesure d'audience et l'analyse de référencement (voir section Cookies). Aucune donnée personnelle identifiante n'est conservée ou exploitée par BougeaParis.fr en propre.</p>
        <p>L'utilisateur dispose d'un droit d'accès, de rectification et d'opposition concernant les données traitées par les services tiers (Google Analytics notamment), à exercer directement auprès de Google ou via les outils de désactivation mentionnés dans la section Cookies.</p>
        <p>Si vous nous contactez par email à <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>, votre adresse email sera utilisée uniquement pour répondre à votre demande, conformément au RGPD.</p>

        <h2>Cookies</h2>
        <p>Le site bougeaparis.fr utilise les services suivants à des fins de mesure d'audience et d'optimisation SEO :</p>

        <h3>Google Analytics (mesure d'audience)</h3>
        <p>Le site utilise Google Analytics pour mesurer la fréquentation du site, identifier les pages les plus consultées et améliorer l'expérience utilisateur. Google Analytics dépose des cookies tiers (notamment <code>_ga</code>, <code>_ga_*</code>) sur le terminal de l'utilisateur. Ces cookies collectent des informations de manière anonyme (adresse IP anonymisée, type de navigateur, pages visitées, durée de visite, source de trafic).</p>
        <p>Pour consulter la politique de confidentialité de Google : <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">policies.google.com/privacy</a></p>
        <p>Pour refuser le suivi par Google Analytics, l'utilisateur peut installer le module complémentaire de désactivation officiel : <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener">tools.google.com/dlpage/gaoptout</a></p>

        <h3>Google Search Console (analyse référencement)</h3>
        <p>Le site utilise Google Search Console pour analyser sa performance dans les résultats de recherche Google. Cet outil <strong>ne dépose pas de cookies</strong> sur le terminal des visiteurs : il fonctionne via une vérification de propriété du domaine et collecte uniquement les données de recherche agrégées côté Google.</p>
        <p>Pour plus d'informations sur Search Console : <a href="https://support.google.com/webmasters" target="_blank" rel="noopener">support.google.com/webmasters</a></p>

        <h3>Consentement</h3>
        <p>Conformément au RGPD et à la directive ePrivacy, l'utilisateur peut à tout moment refuser ces cookies via les paramètres de son navigateur ou les outils de désactivation mentionnés ci-dessus.</p>
        <p>Pour toute question concernant la collecte de données, contacter <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>.</p>

        <h2>Responsabilité</h2>
        <p>Malgré tout le soin apporté à la rédaction de ce site, des erreurs peuvent subsister. BougeaParis.fr ne saurait être tenu responsable des inexactitudes qui pourraient s'y trouver ni des conséquences d'une utilisation des informations qui y sont publiées. Pour toute information critique (dernier train, correspondance cruciale, etc.), nous vous invitons à vérifier auprès des opérateurs officiels.</p>

        <h2>Contact</h2>
        <p>Pour toute question juridique, signalement de contenu, demande de retrait, ou question sur le traitement des données : <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a></p>

        <h2>Droit applicable</h2>
        <p>Les présentes mentions légales sont régies par le <strong>droit français</strong>. En cas de litige, les <strong>tribunaux français</strong> seront seuls compétents.</p>
    </div>
</section>

<?php $tpl->partial('ads/slot-in-article'); ?>

<?php $tpl->partial('ads/slot-footer'); ?>
