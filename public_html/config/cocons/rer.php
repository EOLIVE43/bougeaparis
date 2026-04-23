<?php
return [
    'seo' => [
        'title'       => 'RER en Île-de-France : 5 lignes, plan, horaires et tarifs 2026',
        'description' => 'Guide du RER à Paris et en Île-de-France : lignes A, B, C, D, E, plan du réseau, horaires, tarifs, zones et conseils pratiques.',
        'canonical'   => 'https://bougeaparis.fr/rer/',
        'og_type'     => 'article',
    ],
    'hero' => [
        'h1'       => 'Le RER en Île-de-France',
        'subtitle' => '5 lignes express reliant Paris aux aéroports, Disneyland, Versailles et toute la banlieue.',
        'chiffres' => [
            ['value' => '5', 'label' => 'Lignes'],
            ['value' => '257', 'label' => 'Gares'],
            ['value' => '587', 'label' => 'Km de réseau'],
            ['value' => '3,2M', 'label' => 'Voyageurs/jour'],
        ],
    ],
    'intro' => <<<'HTML'
<p class="lead">
    Le <strong>RER (Réseau Express Régional)</strong> est un réseau de trains rapides qui relie Paris
    à l'ensemble de l'Île-de-France. Il complète le métro pour les trajets à longue distance, avec
    des stations plus espacées et des trains plus rapides.
</p>
<p>
    Le réseau compte <strong>5 lignes</strong> (A, B, C, D, E) exploitées conjointement par la RATP
    et la SNCF. Ensemble, elles totalisent <strong>257 gares</strong> et desservent plus de
    <strong>3,2 millions de voyageurs par jour</strong>.
</p>
<p>
    Le RER est indispensable pour rejoindre les <strong>aéroports</strong> (Roissy-CDG avec le RER B,
    Orly via la ligne B et le tramway T7), les <strong>grands sites touristiques</strong> (Versailles
    avec le RER C, Disneyland Paris avec le RER A), ou traverser Paris rapidement.
</p>
HTML,
    'section_lignes' => [
        'title' => 'Les 5 lignes du RER',
        'content' => <<<'HTML'
<ul>
    <li><strong>RER A (rouge)</strong> : la ligne la plus fréquentée d'Europe, reliant l'ouest (Saint-Germain-en-Laye, Cergy) à l'est (Marne-la-Vallée pour Disneyland Paris).</li>
    <li><strong>RER B (bleu)</strong> : dessert l'aéroport Roissy-CDG au nord, le Stade de France, Châtelet, et va jusqu'au sud de Paris.</li>
    <li><strong>RER C (jaune)</strong> : traverse Paris en longeant la Seine, avec des branches vers Versailles, Massy, Pontoise.</li>
    <li><strong>RER D (vert)</strong> : la ligne la plus longue, reliant le nord (Creil) au sud-est (Melun).</li>
    <li><strong>RER E (violet)</strong> : la plus récente, prolongée vers l'ouest en 2024 (EOLE).</li>
</ul>
HTML,
    ],
    'section_tarifs' => [
        'title' => 'Tarifs et zones du RER en 2026',
        'content' => <<<'HTML'
<p>
    Depuis 2025, le tarif unique <strong>2,50 euros</strong> s'applique pour les voyages en RER dans
    toutes les zones (1 à 5) d'Île-de-France. Les abonnements <strong>Navigo</strong> (Semaine, Mois,
    Annuel) sont valables sur l'ensemble du réseau.
</p>
<p>
    <strong>Attention pour les aéroports :</strong> un <strong>supplément</strong> peut s'appliquer
    pour les trajets vers Roissy-CDG ou Orly avec le RER B.
</p>
HTML,
    ],
    'section_horaires' => [
        'title' => 'Horaires du RER',
        'content' => <<<'HTML'
<p>
    Le RER circule généralement <strong>de 5h environ jusqu'à minuit / 00h30</strong>. Les horaires
    varient selon les lignes et les gares. Les fréquences sont élevées en heure de pointe (toutes
    les 5 à 10 minutes) et plus espacées en soirée (toutes les 15 à 20 minutes).
</p>
<p>
    Le RER ne circule pas la nuit. Pour les déplacements nocturnes, utilisez le réseau Noctilien.
</p>
HTML,
    ],
    'faq' => [
        'title' => 'Questions fréquentes sur le RER',
        'items' => [
            ['question' => 'Quelle est la différence entre le métro et le RER ?',
             'answer'   => '<p>Le <strong>métro</strong> dessert Paris et sa proche banlieue avec des stations tous les 500 mètres. Le <strong>RER</strong> couvre toute l\'Île-de-France avec des gares plus espacées et des trains plus rapides. Dans Paris, même tarif unique (2,50 euros).</p>'],
            ['question' => 'Combien coûte un trajet en RER depuis Roissy-CDG ?',
             'answer'   => '<p>Le billet <strong>Paris - Roissy-CDG</strong> en RER B coûte environ <strong>11,80 à 13 euros</strong> en 2026. C\'est l\'option la plus rapide et économique depuis l\'aéroport.</p>'],
            ['question' => 'Le RER A passe-t-il par Disneyland Paris ?',
             'answer'   => '<p>Oui, la branche est du RER A se termine à <strong>Marne-la-Vallée - Chessy</strong>, à l\'entrée du parc Disneyland. Trajet depuis Paris : environ 40 minutes.</p>'],
            ['question' => 'Le RER circule-t-il la nuit ?',
             'answer'   => '<p>Non, le RER arrête son service entre <strong>minuit environ et 5h du matin</strong>. Pour voyager la nuit, utilisez les bus Noctilien.</p>'],
            ['question' => 'Quelle est la ligne de RER la plus ponctuelle ?',
             'answer'   => '<p>Les lignes <strong>E et A</strong> sont généralement les plus ponctuelles. Les lignes B, C et D connaissent plus de retards car partagées avec les trains SNCF.</p>'],
            ['question' => 'Peut-on voyager avec un vélo dans le RER ?',
             'answer'   => '<p>Oui, les vélos sont autorisés <strong>en dehors des heures de pointe</strong> (avant 6h30, entre 9h et 16h30, après 19h en semaine, toute la journée le week-end).</p>'],
        ],
    ],
];
