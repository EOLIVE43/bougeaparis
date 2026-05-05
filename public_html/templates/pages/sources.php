<?php
/**
 * Page « Sources et données »
 *
 * Centralise la transparence sur les bases ouvertes utilisees pour
 * alimenter le site (transports, adresses, monuments, methodologie).
 *
 * @package BougeaParis\Templates\Pages
 */

// SEO explicite pour cette page (les autres pages legal/about utilisent
// les defaults du Template ; ici on cible un title + description optimises).
$tpl->seo
    ->setTitle('Sources et données')
    ->setDescription("Découvrez les sources officielles utilisées par Bouge à Paris : Île-de-France Mobilités, Base Adresse Nationale, Wikipédia, Wikidata. Toutes nos données sont issues de bases ouvertes sous licences libres.")
    ->setCanonical('/sources/')
    ->setBreadcrumb([
        ['label' => 'Accueil', 'url' => '/'],
        ['label' => 'Sources et données', 'url' => '/sources/'],
    ]);

// Date de derniere maj : on prend filemtime du present template (proxy fiable
// puisque cette page est mise a jour quand on edite ce fichier).
$lastUpdate = @filemtime(__FILE__);
$lastUpdateLabel = $lastUpdate ? dateFr($lastUpdate, 'long_with_day') : null;
?>

<nav class="breadcrumb" aria-label="Fil d'Ariane">
    <div class="container">
        <ol class="breadcrumb__list">
            <li><a href="/">Accueil</a></li>
            <li class="breadcrumb__current">Sources et données</li>
        </ol>
    </div>
</nav>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">Sources et données utilisées sur Bouge à Paris</h1>
        <p class="hero__subtitle">
            Bouge à Paris s'engage sur la transparence des informations qu'il publie.
            Toutes nos données proviennent de bases ouvertes officielles, sous licences
            libres et reconnues, citées et liées ci-dessous.
        </p>
    </div>
</section>

<section class="section">
    <div class="container" style="max-width:800px;">

        <h2>Données de transport</h2>
        <p>
            <strong>Source principale : Île-de-France Mobilités (IDFM).</strong>
            Toutes les informations sur les lignes, stations, horaires, sorties et
            correspondances proviennent du fichier GTFS officiel produit par IDFM
            et exposé en open data.
        </p>
        <ul>
            <li>Plateforme PRIM :
                <a href="https://prim.iledefrance-mobilites.fr/" target="_blank" rel="noopener noreferrer">prim.iledefrance-mobilites.fr</a>
            </li>
            <li>Catalogue national :
                <a href="https://transport.data.gouv.fr/datasets/reseau-urbain-et-interurbain-dile-de-france-mobilites" target="_blank" rel="noopener noreferrer">transport.data.gouv.fr</a>
            </li>
            <li><strong>Licence</strong> : Open Database License (ODbL) — réutilisation libre avec partage à l'identique.</li>
            <li><strong>Format</strong> : GTFS officiel, mis à jour 3 fois par jour (8h, 13h, 17h), validé par IDFM.</li>
        </ul>

        <h2>Adresses postales</h2>
        <p>
            <strong>Source : Base Adresse Nationale (BAN).</strong>
            Pour chaque sortie de station, nous calculons l'adresse postale réelle
            en surface (voie + numéro + code postal) via du <em>reverse geocoding</em>
            sur l'API officielle.
        </p>
        <ul>
            <li>Site officiel :
                <a href="https://adresse.data.gouv.fr/" target="_blank" rel="noopener noreferrer">adresse.data.gouv.fr</a>
            </li>
            <li>API utilisée :
                <a href="https://api-adresse.data.gouv.fr/" target="_blank" rel="noopener noreferrer">api-adresse.data.gouv.fr</a>
            </li>
            <li><strong>Licence</strong> : Etalab 2.0 (équivalent CC-BY) — réutilisation libre avec attribution.</li>
        </ul>

        <h2>Monuments et sites notables</h2>
        <p>
            <strong>Sources : Wikidata, Wikipédia (FR), Wikimedia Commons.</strong>
            Pour chaque station métro, nous sélectionnons les 12 monuments les plus
            notables dans un rayon de 800 mètres. Les descriptions courtes proviennent
            de Wikipédia, les photos de Wikimedia Commons.
        </p>
        <ul>
            <li>Wikidata :
                <a href="https://www.wikidata.org/" target="_blank" rel="noopener noreferrer">wikidata.org</a>
                (identifiants, coordonnées, types, classements)
            </li>
            <li>Wikipédia FR :
                <a href="https://fr.wikipedia.org/" target="_blank" rel="noopener noreferrer">fr.wikipedia.org</a>
                (textes courts via l'API REST <code>/page/summary/</code>)
            </li>
            <li>Wikimedia Commons :
                <a href="https://commons.wikimedia.org/" target="_blank" rel="noopener noreferrer">commons.wikimedia.org</a>
                (photos via <code>Special:FilePath</code>)
            </li>
            <li><strong>Licences</strong> : CC0 (Wikidata), CC-BY-SA (textes Wikipédia, photos Commons sauf mention contraire).</li>
        </ul>

        <h2>Méthodologie</h2>
        <p>
            Quelques choix techniques que nous documentons en toute transparence :
        </p>
        <ul>
            <li>
                <strong>Sortie de station la plus proche d'un monument</strong> :
                pour chaque POI, nous calculons la distance vers chacune des sorties
                numérotées de la station via la
                <a href="https://fr.wikipedia.org/wiki/Formule_de_haversine" target="_blank" rel="noopener noreferrer">formule de Haversine</a>
                (distance orthodromique sur sphère terrestre), puis retenons la sortie
                avec la plus petite distance.
            </li>
            <li>
                <strong>Temps à pied</strong> : estimé à <strong>80 mètres par minute</strong>,
                soit la vitesse moyenne d'un piéton parisien sur surface plane.
                Le résultat est arrondi à la minute, avec un minimum de 1 minute pour
                éviter d'afficher « 0 min ». Les ascenseurs, escaliers et passages
                piétons ne sont pas modélisés : la valeur est indicative.
            </li>
            <li>
                <strong>Filtrage des monuments par notoriété</strong> : sur les 30-40
                items renvoyés par Wikidata pour le rayon donné, nous classons par
                <em>nombre de sitelinks Wikipedia tous langages confondus</em> (proxy
                robuste de notoriété internationale), puis dédupliquons les doublons
                thématiques (ex. un musée et le bâtiment qui l'abrite peuvent être
                deux entrées Wikidata distinctes mais à la même adresse) avec un seuil
                de proximité géographique de 50 m.
            </li>
            <li>
                <strong>Pourquoi parfois moins de 12 POIs ?</strong> Les stations
                périphériques traversent des zones moins denses en monuments notables.
                Si Wikidata renvoie moins de 6 entrées valides après filtrage, nous
                préférons ne pas afficher la section plutôt que d'ajouter des entrées
                de faible intérêt.
            </li>
            <li>
                <strong>Accessibilité PMR</strong> : la donnée
                <code>wheelchair_boarding</code> du GTFS IDFM est utilisée telle quelle
                pour chaque quai de métro. Note : la ligne 1 est marquée non accessible
                par IDFM (gap quai/train) malgré l'automatisation, alors que la
                ligne 14 est totalement accessible.
            </li>
        </ul>

        <h2>Mentions légales et indépendance</h2>
        <p>
            Bouge à Paris est un site éditorial <strong>indépendant</strong>.
            Il n'est affilié ni à la RATP, ni à la SNCF, ni à Île-de-France Mobilités,
            ni à aucun autre opérateur de transport. Les informations sont issues
            des données ouvertes officielles ci-dessus et de notre veille éditoriale.
        </p>
        <p>
            Pour le détail de l'éditeur du site, l'hébergement et la responsabilité
            éditoriale, consultez la page
            <a href="/mentions-legales/">Mentions légales</a>.
            Pour les questions sur le traitement des données personnelles, voir la
            <a href="/confidentialite/">Politique de confidentialité</a>.
            Pour toute remarque ou signalement d'erreur sur ces sources :
            <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>.
        </p>

        <?php if ($lastUpdateLabel): ?>
            <p class="page-meta-update" style="margin-top:2.5rem; color:var(--color-text-muted, #5A6B66); font-size:0.875rem; font-style:italic;">
                Page mise à jour le <?= e($lastUpdateLabel) ?>.
            </p>
        <?php endif; ?>
    </div>
</section>
