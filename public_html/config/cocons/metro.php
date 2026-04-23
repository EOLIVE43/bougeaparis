<?php
/**
 * Contenu editorial /metro/
 * Objectif : ranker top 3 sur "metro paris", "plan metro", "horaires metro", etc.
 * Volume cible : 2000 mots.
 */

return [

    'seo' => [
        'title'       => 'Metro de Paris : 16 lignes, plan, horaires et prix en 2026',
        'description' => 'Decouvrez le metro parisien : 16 lignes, 308 stations, plan, horaires, tarifs 2026 et infos pratiques. Guide complet pour se deplacer a Paris.',
        'canonical'   => 'https://bougeaparis.fr/metro/',
        'og_type'     => 'article',
    ],

    'hero' => [
        'h1'       => 'Le metro parisien',
        'subtitle' => 'Guide complet du reseau : 16 lignes, 308 stations, horaires, tarifs et plan du metro de Paris.',
        'chiffres' => [
            ['value' => '16', 'label' => 'Lignes'],
            ['value' => '308', 'label' => 'Stations'],
            ['value' => '245', 'label' => 'Km de reseau'],
            ['value' => '4,1M', 'label' => 'Voyageurs/jour'],
        ],
    ],

    'intro' => <<<'HTML'
<p class="lead">
    Le <strong>metro de Paris</strong> est l'un des reseaux les plus denses et les plus frequentes au monde.
    Avec ses <strong>16 lignes numerotees</strong>, ses <strong>308 stations</strong> et ses
    <strong>245 kilometres de voies</strong>, il transporte chaque jour plus de
    <strong>4,1 millions de voyageurs</strong> a travers Paris et sa proche banlieue.
</p>
<p>
    Inaugure le 19 juillet 1900, le metropolitain parisien est aujourd'hui un symbole de la capitale,
    aux cotes de la Tour Eiffel ou du Louvre. Il dessert l'integralite des arrondissements de Paris
    ainsi qu'une partie de la petite couronne, et s'etend progressivement vers la grande banlieue
    grace au projet du Grand Paris Express.
</p>
<p>
    Sur cette page, vous trouverez <strong>tout ce qu'il faut savoir pour utiliser le metro parisien</strong> :
    presentation des lignes avec leurs terminus, horaires d'ouverture et de fermeture, prix des tickets
    et abonnements Navigo, informations d'accessibilite, plans et conseils pratiques.
</p>
HTML,

    'section_plan' => [
        'title' => 'Plan du metro de Paris',
        'content' => <<<'HTML'
<p>
    Le plan du metro parisien represente visuellement les 16 lignes du reseau avec leurs couleurs
    officielles et leurs stations. Il permet de visualiser d'un coup d'oeil les correspondances
    entre lignes et les principaux poles d'echange tels que <em>Chatelet-Les Halles</em>,
    <em>Gare du Nord</em>, <em>Montparnasse-Bienvenue</em> ou <em>Republique</em>.
</p>
<p>
    Le plan officiel est edite par la RATP et mis a jour regulierement. Il est disponible en
    telechargement au format PDF sur le site officiel, et affiche dans toutes les stations du reseau.
</p>
<div class="cta-box">
    <p>
        <strong>Consulter le plan officiel :</strong>
        <a href="https://www.ratp.fr/plan-metro" target="_blank" rel="noopener noreferrer">
            Telecharger le plan du metro (PDF sur ratp.fr)
        </a>
    </p>
</div>
HTML,
    ],

    'section_horaires' => [
        'title' => 'Horaires du metro parisien',
        'content' => <<<'HTML'
<p>
    Le metro de Paris circule <strong>de 5h30 du matin a 1h15</strong> en semaine. Le vendredi soir,
    le samedi soir et les veilles de jour ferie, le service est <strong>prolonge jusqu'a 2h15</strong>
    pour accompagner la vie nocturne parisienne.
</p>
<p>
    Attention : ces horaires sont indicatifs. Le <strong>premier metro</strong> part de son terminus
    a 5h30, mais n'arrive dans les stations du milieu de ligne qu'a partir de 5h40 ou 5h45. De meme,
    le <strong>dernier metro</strong> quitte le terminus vers 0h40 pour une arrivee finale a 1h15
    environ.
</p>
HTML,
    ],

    'section_tarifs' => [
        'title' => 'Prix du metro : tickets et abonnements 2026',
        'content' => <<<'HTML'
<p>
    Depuis janvier 2025, l'Ile-de-France a simplifie son systeme tarifaire avec une <strong>tarification
    unique zone 1 a 5</strong> pour les titres de transport metro et RER dans Paris et sa banlieue.
</p>
<table class="data-table">
    <caption>Tarifs des titres de transport metro et RER (2026)</caption>
    <thead>
        <tr><th>Titre</th><th>Prix</th><th>Validite</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Ticket Metro-Train-RER</strong></td><td>2,50 &euro;</td><td>1 voyage zones 1-5</td></tr>
        <tr><td><strong>Carnet de 10 tickets</strong></td><td>19,10 &euro;</td><td>10 voyages (-25%)</td></tr>
        <tr><td><strong>Navigo Easy</strong></td><td>2 &euro; + chargement</td><td>Carte sans contact rechargeable</td></tr>
        <tr><td><strong>Navigo Jour</strong></td><td>des 8,65 &euro;</td><td>Illimite 1 jour</td></tr>
        <tr><td><strong>Navigo Semaine</strong></td><td>31,60 &euro;</td><td>Lundi au dimanche</td></tr>
        <tr><td><strong>Navigo Mois</strong></td><td>88,80 &euro;</td><td>Mois civil</td></tr>
    </tbody>
</table>
<p class="notice">
    <strong>Important :</strong> les tarifs sont susceptibles d'etre actualises chaque annee en janvier.
    Pour les prix en vigueur aujourd'hui, consultez
    <a href="https://www.iledefrance-mobilites.fr/titres-et-tarifs" target="_blank" rel="noopener noreferrer">iledefrance-mobilites.fr</a>.
</p>
<h3>Quel titre choisir ?</h3>
<ul>
    <li><strong>Pour un touriste (1 jour)</strong> : Navigo Jour ou tickets a l'unite.</li>
    <li><strong>Pour un sejour de 3 a 5 jours</strong> : carnet de 10 tickets.</li>
    <li><strong>Pour une semaine complete</strong> : Navigo Semaine.</li>
    <li><strong>Pour les Franciliens</strong> : Navigo Mois ou Navigo Annuel.</li>
    <li><strong>Pour les jeunes</strong> : Navigo Jeunes Week-end (tarif reduit).</li>
</ul>
HTML,
    ],

    'section_chiffres' => [
        'title' => 'Le metro parisien en chiffres',
        'content' => <<<'HTML'
<ul class="stats-list">
    <li><strong>16 lignes</strong> numerotees de 1 a 14, avec deux lignes secondaires (3bis et 7bis).</li>
    <li><strong>308 stations</strong> dans Paris et sa proche banlieue.</li>
    <li><strong>245 kilometres</strong> de voies en service.</li>
    <li><strong>4,1 millions de voyageurs</strong> par jour ouvrable (1,5 milliard/an).</li>
    <li><strong>2 lignes automatiques</strong> : ligne 1 (depuis 2012) et ligne 14.</li>
    <li><strong>Station la plus profonde</strong> : Abbesses (ligne 12), a 36 metres.</li>
    <li><strong>Station la plus haute</strong> : Bastille (ligne 1), sur un viaduc.</li>
    <li><strong>Ligne la plus frequentee</strong> : ligne 1, pres de 750 000 voyageurs/jour.</li>
    <li><strong>Ligne la plus longue</strong> : ligne 14, avec 28 km apres son extension vers Orly.</li>
</ul>
HTML,
    ],

    'section_histoire' => [
        'title' => 'Une courte histoire du metro parisien',
        'content' => <<<'HTML'
<p>
    Le metropolitain de Paris a vu le jour le <strong>19 juillet 1900</strong>, quelques jours apres
    l'ouverture de l'Exposition Universelle. La premiere ligne, inauguree entre Porte Maillot et
    Porte de Vincennes, est l'actuelle <strong>ligne 1</strong>. Son succes fut immediat : plus
    de 16 millions de voyageurs en seulement six mois.
</p>
<p>
    L'ingenieur <strong>Fulgence Bienvenue</strong>, surnomme "le pere du metro", pilota sa
    construction pendant plus de trente ans. Son nom est d'ailleurs inscrit sur une plaque a la
    station Montparnasse-Bienvenue, en son honneur.
</p>
<p>
    Au fil des decennies, le reseau s'est etendu, densifie et modernise. La <strong>ligne 14</strong>,
    ouverte en 1998, a ete la premiere ligne entierement automatique. Elle a ete prolongee en 2024
    jusqu'a l'aeroport d'Orly, devenant la ligne la plus longue du reseau.
</p>
<p>
    Le futur du metro parisien s'appelle <strong>Grand Paris Express</strong> : quatre nouvelles
    lignes automatiques (15, 16, 17 et 18) en construction pour desservir la banlieue en contournant
    Paris. Les premieres sections ouvriront progressivement entre 2025 et 2030.
</p>
HTML,
    ],

    'section_accessibilite' => [
        'title' => 'Accessibilite du metro',
        'content' => <<<'HTML'
<p>
    Le metro parisien est l'un des reseaux les plus denses au monde, mais son <strong>accessibilite
    aux personnes a mobilite reduite (PMR) reste limitee</strong>. L'age et la complexite des
    infrastructures souterraines rendent difficile l'installation d'ascenseurs partout.
</p>
<p>
    La <strong>ligne 14 est entierement accessible</strong>, avec ascenseurs systematiques et quais
    de plain-pied. C'est la seule ligne totalement adaptee aux PMR. Les autres lignes comptent
    quelques stations accessibles, principalement les plus recentes ou renovees.
</p>
HTML,
    ],

    'section_nuit' => [
        'title' => 'Le metro la nuit et le dimanche',
        'content' => <<<'HTML'
<p>
    Le metro parisien circule <strong>tous les jours de l'annee</strong>, y compris le dimanche et
    les jours feries, aux memes horaires qu'en semaine (5h30 - 1h15).
</p>
<p>
    <strong>Les vendredis, samedis et veilles de jour ferie</strong>, le service est prolonge
    jusqu'a <strong>2h15 du matin</strong>.
</p>
<p>
    <strong>Entre 1h15 (ou 2h15) et 5h30</strong>, aucun metro ne circule. Pour se deplacer la nuit,
    il faut emprunter le reseau <a href="/bus/noctilien/">Noctilien</a>.
</p>
HTML,
    ],

    'section_guide' => [
        'title' => 'Comment prendre le metro : guide pratique',
        'content' => <<<'HTML'
<ol class="steps-list">
    <li><strong>Acheter un titre de transport</strong> : distributeurs, guichets, application mobile, ou Navigo Easy.</li>
    <li><strong>Reperer votre direction</strong> : cherchez le nom du terminus dans votre direction.</li>
    <li><strong>Valider votre titre</strong> : passez votre ticket ou votre carte Navigo sur le portillon.</li>
    <li><strong>Prendre le metro</strong> : attendez la rame, laissez sortir les voyageurs avant de monter.</li>
    <li><strong>Faire une correspondance</strong> : suivez les panneaux indiquant le numero de ligne.</li>
    <li><strong>Sortir de la station</strong> : passez le portillon de sortie, reperez-vous grace aux panneaux.</li>
</ol>
HTML,
    ],

    'section_specific' => [
        'title' => 'Particularites du reseau',
        'content' => <<<'HTML'
<h3>Les lignes automatiques</h3>
<p>
    Deux lignes du metro parisien circulent <strong>sans conducteur</strong> : la <strong>ligne 14</strong>
    (depuis 1998) et la <strong>ligne 1</strong> (depuis 2012, sans interruption de service pendant
    les travaux, une prouesse technique mondiale). Ces lignes offrent une frequence accrue et une
    ponctualite quasi parfaite.
</p>
<h3>Les portes palieres</h3>
<p>
    Les lignes automatiques sont equipees de <strong>portes palieres</strong> sur les quais. La ligne
    13 est egalement equipee de portes palieres.
</p>
<h3>Les stations fantomes</h3>
<p>
    Le metro parisien compte une dizaine de <strong>stations fermees au public</strong> : Haxo (3bis),
    Porte Molitor (9 et 10), Saint-Martin (8 et 9). Certaines sont ouvertes lors des Journees du Patrimoine.
</p>
<h3>La station Arts et Metiers</h3>
<p>
    La station <strong>Arts et Metiers</strong> (ligne 11) est l'une des plus spectaculaires : habillee
    de cuivre, hublots et engrenages, elle evoque le sous-marin de Jules Verne.
</p>
HTML,
    ],

    'faq' => [
        'title' => 'Questions frequentes sur le metro parisien',
        'items' => [
            ['question' => 'Combien coute un ticket de metro a Paris en 2026 ?',
             'answer'   => '<p>Un ticket unitaire coute <strong>2,50 euros</strong>. Un carnet de 10 tickets coute <strong>19,10 euros</strong> (environ 25% de reduction). Des abonnements Navigo existent a la semaine, au mois et a l\'annee.</p>'],
            ['question' => 'A quelle heure commence et finit le metro a Paris ?',
             'answer'   => '<p>Le metro circule <strong>de 5h30 a 1h15</strong> en semaine. Les vendredis et samedis soirs, le service est prolonge jusqu\'a <strong>2h15</strong>.</p>'],
            ['question' => 'Le metro circule-t-il le dimanche et les jours feries ?',
             'answer'   => '<p>Oui, le metro circule <strong>tous les jours de l\'annee</strong>, y compris 1er janvier, 1er mai, Noel. Memes horaires qu\'un jour de semaine.</p>'],
            ['question' => 'Comment fonctionne la carte Navigo ?',
             'answer'   => '<p>La <strong>Navigo Easy</strong> (2 euros, rechargeable) sert aux voyageurs occasionnels. La <strong>Navigo Mois/Annuel</strong> (avec photo) pour les Franciliens. On la recharge en station ou via l\'application mobile.</p>'],
            ['question' => 'Y a-t-il du Wi-Fi ou de la 4G dans le metro ?',
             'answer'   => '<p>La <strong>4G/5G est disponible sur la quasi-totalite du reseau</strong> souterrain. Le Wi-Fi public est disponible dans les grandes stations via Ile-de-France Connect.</p>'],
            ['question' => 'Peut-on voyager avec un velo dans le metro ?',
             'answer'   => '<p>Les velos ne sont <strong>pas autorises</strong>, sauf les velos pliants (ranges dans une housse). Utilisez plutot le RER ou les trains Transilien (hors heures de pointe).</p>'],
            ['question' => 'Les valises sont-elles acceptees dans le metro ?',
             'answer'   => '<p>Oui, sans frais supplementaire. Attention : les stations sont rarement equipees d\'ascenseurs (sauf ligne 14). Privilegiez le RER B ou la ligne 14 pour les aeroports.</p>'],
            ['question' => 'Le metro est-il accessible aux personnes a mobilite reduite ?',
             'answer'   => '<p>L\'accessibilite est <strong>partielle</strong>. Seule la <strong>ligne 14 est entierement accessible</strong>. Pour les deplacements PMR, privilegiez le RER, les bus et les tramways.</p>'],
            ['question' => 'Quelle est la difference entre le metro et le RER ?',
             'answer'   => '<p>Le <strong>metro</strong> dessert Paris et la proche banlieue (stations tous les 500m). Le <strong>RER</strong> dessert toute l\'Ile-de-France avec des trains plus rapides. Dans Paris, meme tarif.</p>'],
            ['question' => 'Peut-on acheter un ticket en anglais ?',
             'answer'   => '<p>Oui. Les distributeurs automatiques proposent plusieurs langues (anglais, espagnol, allemand, chinois, japonais) et acceptent les cartes internationales ainsi que Apple Pay / Google Pay.</p>'],
        ],
    ],

];
