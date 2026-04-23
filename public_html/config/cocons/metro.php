<?php
/**
 * Contenu editorial /metro/ AVEC ACCENTS FRANCAIS
 * Objectif : ranker top 3 sur "métro paris", "plan métro", etc.
 */

return [

    'seo' => [
        'title'       => 'Métro de Paris : 16 lignes, plan, horaires et prix en 2026',
        'description' => 'Découvrez le métro parisien : 16 lignes, 308 stations, plan, horaires, tarifs 2026 et infos pratiques. Guide complet pour se déplacer à Paris.',
        'canonical'   => 'https://bougeaparis.fr/metro/',
        'og_type'     => 'article',
    ],

    'hero' => [
        'h1'       => 'Le métro parisien',
        'subtitle' => 'Guide complet du réseau : 16 lignes, 308 stations, horaires, tarifs et plan du métro de Paris.',
        'chiffres' => [
            ['value' => '16', 'label' => 'Lignes'],
            ['value' => '308', 'label' => 'Stations'],
            ['value' => '245', 'label' => 'Km de réseau'],
            ['value' => '4,1M', 'label' => 'Voyageurs/jour'],
        ],
    ],

    'intro' => <<<'HTML'
<p class="lead">
    Le <strong>métro de Paris</strong> est l'un des réseaux les plus denses et les plus fréquentés au monde.
    Avec ses <strong>16 lignes numérotées</strong>, ses <strong>308 stations</strong> et ses
    <strong>245 kilomètres de voies</strong>, il transporte chaque jour plus de
    <strong>4,1 millions de voyageurs</strong> à travers Paris et sa proche banlieue.
</p>
<p>
    Inauguré le 19 juillet 1900, le métropolitain parisien est aujourd'hui un symbole de la capitale,
    aux côtés de la Tour Eiffel ou du Louvre. Il dessert l'intégralité des arrondissements de Paris
    ainsi qu'une partie de la petite couronne, et s'étend progressivement vers la grande banlieue
    grâce au projet du Grand Paris Express.
</p>
<p>
    Sur cette page, vous trouverez <strong>tout ce qu'il faut savoir pour utiliser le métro parisien</strong> :
    présentation des lignes avec leurs terminus, horaires d'ouverture et de fermeture, prix des tickets
    et abonnements Navigo, informations d'accessibilité, plans et conseils pratiques.
</p>
HTML,

    'section_plan' => [
        'title' => 'Plan du métro de Paris',
        'content' => <<<'HTML'
<p>
    Le plan du métro parisien représente visuellement les 16 lignes du réseau avec leurs couleurs
    officielles et leurs stations. Il permet de visualiser d'un coup d'œil les correspondances
    entre lignes et les principaux pôles d'échange tels que <em>Châtelet-Les Halles</em>,
    <em>Gare du Nord</em>, <em>Montparnasse-Bienvenüe</em> ou <em>République</em>.
</p>
<p>
    Le plan officiel est édité par la RATP et mis à jour régulièrement. Il est disponible en
    téléchargement au format PDF sur le site officiel, et affiché dans toutes les stations du réseau.
</p>
<div class="cta-box">
    <p>
        <strong>Consulter le plan officiel :</strong>
        <a href="https://www.ratp.fr/plan-metro" target="_blank" rel="noopener noreferrer">
            Télécharger le plan du métro (PDF sur ratp.fr)
        </a>
    </p>
</div>
HTML,
    ],

    'section_horaires' => [
        'title' => 'Horaires du métro parisien',
        'content' => <<<'HTML'
<p>
    Le métro de Paris circule <strong>de 5h30 du matin à 1h15</strong> en semaine. Le vendredi soir,
    le samedi soir et les veilles de jour férié, le service est <strong>prolongé jusqu'à 2h15</strong>
    pour accompagner la vie nocturne parisienne.
</p>
<p>
    Attention : ces horaires sont indicatifs. Le <strong>premier métro</strong> part de son terminus
    à 5h30, mais n'arrive dans les stations du milieu de ligne qu'à partir de 5h40 ou 5h45. De même,
    le <strong>dernier métro</strong> quitte le terminus vers 0h40 pour une arrivée finale à 1h15
    environ.
</p>
HTML,
    ],

    'section_tarifs' => [
        'title' => 'Prix du métro : tickets et abonnements 2026',
        'content' => <<<'HTML'
<p>
    Depuis janvier 2025, l'Île-de-France a simplifié son système tarifaire avec une <strong>tarification
    unique zone 1 à 5</strong> pour les titres de transport métro et RER dans Paris et sa banlieue.
</p>
<table class="data-table">
    <caption>Tarifs des titres de transport métro et RER (2026)</caption>
    <thead>
        <tr><th>Titre</th><th>Prix</th><th>Validité</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Ticket Métro-Train-RER</strong></td><td>2,50 &euro;</td><td>1 voyage zones 1-5</td></tr>
        <tr><td><strong>Carnet de 10 tickets</strong></td><td>19,10 &euro;</td><td>10 voyages (-25%)</td></tr>
        <tr><td><strong>Navigo Easy</strong></td><td>2 &euro; + chargement</td><td>Carte sans contact rechargeable</td></tr>
        <tr><td><strong>Navigo Jour</strong></td><td>dès 8,65 &euro;</td><td>Illimité 1 jour</td></tr>
        <tr><td><strong>Navigo Semaine</strong></td><td>31,60 &euro;</td><td>Lundi au dimanche</td></tr>
        <tr><td><strong>Navigo Mois</strong></td><td>88,80 &euro;</td><td>Mois civil</td></tr>
    </tbody>
</table>
<p class="notice">
    <strong>Important :</strong> les tarifs sont susceptibles d'être actualisés chaque année en janvier.
    Pour les prix en vigueur aujourd'hui, consultez
    <a href="https://www.iledefrance-mobilites.fr/titres-et-tarifs" target="_blank" rel="noopener noreferrer">iledefrance-mobilites.fr</a>.
</p>
<h3>Quel titre choisir ?</h3>
<ul>
    <li><strong>Pour un touriste (1 jour)</strong> : Navigo Jour ou tickets à l'unité.</li>
    <li><strong>Pour un séjour de 3 à 5 jours</strong> : carnet de 10 tickets.</li>
    <li><strong>Pour une semaine complète</strong> : Navigo Semaine.</li>
    <li><strong>Pour les Franciliens</strong> : Navigo Mois ou Navigo Annuel.</li>
    <li><strong>Pour les jeunes</strong> : Navigo Jeunes Week-end (tarif réduit).</li>
</ul>
HTML,
    ],

    'section_chiffres' => [
        'title' => 'Le métro parisien en chiffres',
        'content' => <<<'HTML'
<ul class="stats-list">
    <li><strong>16 lignes</strong> numérotées de 1 à 14, avec deux lignes secondaires (3bis et 7bis).</li>
    <li><strong>308 stations</strong> dans Paris et sa proche banlieue.</li>
    <li><strong>245 kilomètres</strong> de voies en service.</li>
    <li><strong>4,1 millions de voyageurs</strong> par jour ouvrable (1,5 milliard/an).</li>
    <li><strong>2 lignes automatiques</strong> : ligne 1 (depuis 2012) et ligne 14.</li>
    <li><strong>Station la plus profonde</strong> : Abbesses (ligne 12), à 36 mètres.</li>
    <li><strong>Station la plus haute</strong> : Bastille (ligne 1), sur un viaduc.</li>
    <li><strong>Ligne la plus fréquentée</strong> : ligne 1, près de 750 000 voyageurs/jour.</li>
    <li><strong>Ligne la plus longue</strong> : ligne 14, avec 28 km après son extension vers Orly.</li>
</ul>
HTML,
    ],

    'section_histoire' => [
        'title' => 'Une courte histoire du métro parisien',
        'content' => <<<'HTML'
<p>
    Le métropolitain de Paris a vu le jour le <strong>19 juillet 1900</strong>, quelques jours après
    l'ouverture de l'Exposition Universelle. La première ligne, inaugurée entre Porte Maillot et
    Porte de Vincennes, est l'actuelle <strong>ligne 1</strong>. Son succès fut immédiat : plus
    de 16 millions de voyageurs en seulement six mois.
</p>
<p>
    L'ingénieur <strong>Fulgence Bienvenüe</strong>, surnommé "le père du métro", pilota sa
    construction pendant plus de trente ans. Son nom est d'ailleurs inscrit sur une plaque à la
    station Montparnasse-Bienvenüe, en son honneur.
</p>
<p>
    Au fil des décennies, le réseau s'est étendu, densifié et modernisé. La <strong>ligne 14</strong>,
    ouverte en 1998, a été la première ligne entièrement automatique. Elle a été prolongée en 2024
    jusqu'à l'aéroport d'Orly, devenant la ligne la plus longue du réseau.
</p>
<p>
    Le futur du métro parisien s'appelle <strong>Grand Paris Express</strong> : quatre nouvelles
    lignes automatiques (15, 16, 17 et 18) en construction pour desservir la banlieue en contournant
    Paris. Les premières sections ouvriront progressivement entre 2025 et 2030.
</p>
HTML,
    ],

    'section_accessibilite' => [
        'title' => 'Accessibilité du métro',
        'content' => <<<'HTML'
<p>
    Le métro parisien est l'un des réseaux les plus denses au monde, mais son <strong>accessibilité
    aux personnes à mobilité réduite (PMR) reste limitée</strong>. L'âge et la complexité des
    infrastructures souterraines rendent difficile l'installation d'ascenseurs partout.
</p>
<p>
    La <strong>ligne 14 est entièrement accessible</strong>, avec ascenseurs systématiques et quais
    de plain-pied. C'est la seule ligne totalement adaptée aux PMR. Les autres lignes comptent
    quelques stations accessibles, principalement les plus récentes ou rénovées.
</p>
HTML,
    ],

    'section_nuit' => [
        'title' => 'Le métro la nuit et le dimanche',
        'content' => <<<'HTML'
<p>
    Le métro parisien circule <strong>tous les jours de l'année</strong>, y compris le dimanche et
    les jours fériés, aux mêmes horaires qu'en semaine (5h30 - 1h15).
</p>
<p>
    <strong>Les vendredis, samedis et veilles de jour férié</strong>, le service est prolongé
    jusqu'à <strong>2h15 du matin</strong>.
</p>
<p>
    <strong>Entre 1h15 (ou 2h15) et 5h30</strong>, aucun métro ne circule. Pour se déplacer la nuit,
    il faut emprunter le réseau <a href="/bus/noctilien/">Noctilien</a>.
</p>
HTML,
    ],

    'section_guide' => [
        'title' => 'Comment prendre le métro : guide pratique',
        'content' => <<<'HTML'
<ol class="steps-list">
    <li><strong>Acheter un titre de transport</strong> : distributeurs, guichets, application mobile, ou Navigo Easy.</li>
    <li><strong>Repérer votre direction</strong> : cherchez le nom du terminus dans votre direction.</li>
    <li><strong>Valider votre titre</strong> : passez votre ticket ou votre carte Navigo sur le portillon.</li>
    <li><strong>Prendre le métro</strong> : attendez la rame, laissez sortir les voyageurs avant de monter.</li>
    <li><strong>Faire une correspondance</strong> : suivez les panneaux indiquant le numéro de ligne.</li>
    <li><strong>Sortir de la station</strong> : passez le portillon de sortie, repérez-vous grâce aux panneaux.</li>
</ol>
HTML,
    ],

    'section_specific' => [
        'title' => 'Particularités du réseau',
        'content' => <<<'HTML'
<h3>Les lignes automatiques</h3>
<p>
    Deux lignes du métro parisien circulent <strong>sans conducteur</strong> : la <strong>ligne 14</strong>
    (depuis 1998) et la <strong>ligne 1</strong> (depuis 2012, sans interruption de service pendant
    les travaux, une prouesse technique mondiale). Ces lignes offrent une fréquence accrue et une
    ponctualité quasi parfaite.
</p>
<h3>Les portes palières</h3>
<p>
    Les lignes automatiques sont équipées de <strong>portes palières</strong> sur les quais. La ligne
    13 est également équipée de portes palières.
</p>
<h3>Les stations fantômes</h3>
<p>
    Le métro parisien compte une dizaine de <strong>stations fermées au public</strong> : Haxo (3bis),
    Porte Molitor (9 et 10), Saint-Martin (8 et 9). Certaines sont ouvertes lors des Journées du Patrimoine.
</p>
<h3>La station Arts et Métiers</h3>
<p>
    La station <strong>Arts et Métiers</strong> (ligne 11) est l'une des plus spectaculaires : habillée
    de cuivre, hublots et engrenages, elle évoque le sous-marin de Jules Verne.
</p>
HTML,
    ],

    'faq' => [
        'title' => 'Questions fréquentes sur le métro parisien',
        'items' => [
            ['question' => 'Combien coûte un ticket de métro à Paris en 2026 ?',
             'answer'   => '<p>Un ticket unitaire coûte <strong>2,50 euros</strong>. Un carnet de 10 tickets coûte <strong>19,10 euros</strong> (environ 25% de réduction). Des abonnements Navigo existent à la semaine, au mois et à l\'année.</p>'],
            ['question' => 'À quelle heure commence et finit le métro à Paris ?',
             'answer'   => '<p>Le métro circule <strong>de 5h30 à 1h15</strong> en semaine. Les vendredis et samedis soirs, le service est prolongé jusqu\'à <strong>2h15</strong>.</p>'],
            ['question' => 'Le métro circule-t-il le dimanche et les jours fériés ?',
             'answer'   => '<p>Oui, le métro circule <strong>tous les jours de l\'année</strong>, y compris 1er janvier, 1er mai, Noël. Mêmes horaires qu\'un jour de semaine.</p>'],
            ['question' => 'Comment fonctionne la carte Navigo ?',
             'answer'   => '<p>La <strong>Navigo Easy</strong> (2 euros, rechargeable) sert aux voyageurs occasionnels. La <strong>Navigo Mois/Annuel</strong> (avec photo) pour les Franciliens. On la recharge en station ou via l\'application mobile.</p>'],
            ['question' => 'Y a-t-il du Wi-Fi ou de la 4G dans le métro ?',
             'answer'   => '<p>La <strong>4G/5G est disponible sur la quasi-totalité du réseau</strong> souterrain. Le Wi-Fi public est disponible dans les grandes stations via Île-de-France Connect.</p>'],
            ['question' => 'Peut-on voyager avec un vélo dans le métro ?',
             'answer'   => '<p>Les vélos ne sont <strong>pas autorisés</strong>, sauf les vélos pliants (rangés dans une housse). Utilisez plutôt le RER ou les trains Transilien (hors heures de pointe).</p>'],
            ['question' => 'Les valises sont-elles acceptées dans le métro ?',
             'answer'   => '<p>Oui, sans frais supplémentaire. Attention : les stations sont rarement équipées d\'ascenseurs (sauf ligne 14). Privilégiez le RER B ou la ligne 14 pour les aéroports.</p>'],
            ['question' => 'Le métro est-il accessible aux personnes à mobilité réduite ?',
             'answer'   => '<p>L\'accessibilité est <strong>partielle</strong>. Seule la <strong>ligne 14 est entièrement accessible</strong>. Pour les déplacements PMR, privilégiez le RER, les bus et les tramways.</p>'],
            ['question' => 'Quelle est la différence entre le métro et le RER ?',
             'answer'   => '<p>Le <strong>métro</strong> dessert Paris et la proche banlieue (stations tous les 500m). Le <strong>RER</strong> dessert toute l\'Île-de-France avec des trains plus rapides. Dans Paris, même tarif.</p>'],
            ['question' => 'Peut-on acheter un ticket en anglais ?',
             'answer'   => '<p>Oui. Les distributeurs automatiques proposent plusieurs langues (anglais, espagnol, allemand, chinois, japonais) et acceptent les cartes internationales ainsi que Apple Pay / Google Pay.</p>'],
        ],
    ],

];
