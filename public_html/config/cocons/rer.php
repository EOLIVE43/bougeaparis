<?php
return [
    'seo' => [
        'title'       => 'RER en Ile-de-France : 5 lignes, plan, horaires et tarifs 2026',
        'description' => 'Guide du RER a Paris et en Ile-de-France : lignes A, B, C, D, E, plan du reseau, horaires, tarifs, zones et conseils pratiques.',
        'canonical'   => 'https://bougeaparis.fr/rer/',
        'og_type'     => 'article',
    ],
    'hero' => [
        'h1'       => 'Le RER en Ile-de-France',
        'subtitle' => '5 lignes express reliant Paris aux aeroports, Disneyland, Versailles et toute la banlieue.',
        'chiffres' => [
            ['value' => '5', 'label' => 'Lignes'],
            ['value' => '257', 'label' => 'Gares'],
            ['value' => '587', 'label' => 'Km de reseau'],
            ['value' => '3,2M', 'label' => 'Voyageurs/jour'],
        ],
    ],
    'intro' => <<<'HTML'
<p class="lead">
    Le <strong>RER (Reseau Express Regional)</strong> est un reseau de trains rapides qui relie Paris
    a l'ensemble de l'Ile-de-France. Il complete le metro pour les trajets a longue distance, avec
    des stations plus espacees et des trains plus rapides.
</p>
<p>
    Le reseau compte <strong>5 lignes</strong> (A, B, C, D, E) exploitees conjointement par la RATP
    et la SNCF. Ensemble, elles totalisent <strong>257 gares</strong> et desservent plus de
    <strong>3,2 millions de voyageurs par jour</strong>.
</p>
<p>
    Le RER est indispensable pour rejoindre les <strong>aeroports</strong> (Roissy-CDG avec le RER B,
    Orly via la ligne B et le tramway T7), les <strong>grands sites touristiques</strong> (Versailles
    avec le RER C, Disneyland Paris avec le RER A), ou traverser Paris rapidement.
</p>
HTML,
    'section_lignes' => [
        'title' => 'Les 5 lignes du RER',
        'content' => <<<'HTML'
<ul>
    <li><strong>RER A (rouge)</strong> : la ligne la plus frequentee d'Europe, reliant l'ouest (Saint-Germain-en-Laye, Cergy) a l'est (Marne-la-Vallee pour Disneyland Paris).</li>
    <li><strong>RER B (bleu)</strong> : dessert l'aeroport Roissy-CDG au nord, le Stade de France, Chatelet, et va jusqu'au sud de Paris.</li>
    <li><strong>RER C (jaune)</strong> : traverse Paris en longeant la Seine, avec des branches vers Versailles, Massy, Pontoise.</li>
    <li><strong>RER D (vert)</strong> : la ligne la plus longue, reliant le nord (Creil) au sud-est (Melun).</li>
    <li><strong>RER E (violet)</strong> : la plus recente, prolongee vers l'ouest en 2024 (EOLE).</li>
</ul>
HTML,
    ],
    'section_tarifs' => [
        'title' => 'Tarifs et zones du RER en 2026',
        'content' => <<<'HTML'
<p>
    Depuis 2025, le tarif unique <strong>2,50 euros</strong> s'applique pour les voyages en RER dans
    toutes les zones (1 a 5) d'Ile-de-France. Les abonnements <strong>Navigo</strong> (Semaine, Mois,
    Annuel) sont valables sur l'ensemble du reseau.
</p>
<p>
    <strong>Attention pour les aeroports :</strong> un <strong>supplement</strong> peut s'appliquer
    pour les trajets vers Roissy-CDG ou Orly avec le RER B.
</p>
HTML,
    ],
    'section_horaires' => [
        'title' => 'Horaires du RER',
        'content' => <<<'HTML'
<p>
    Le RER circule generalement <strong>de 5h environ jusqu'a minuit / 00h30</strong>. Les horaires
    varient selon les lignes et les gares. Les frequences sont elevees en heure de pointe (toutes
    les 5 a 10 minutes) et plus espacees en soiree (toutes les 15 a 20 minutes).
</p>
<p>
    Le RER ne circule pas la nuit. Pour les deplacements nocturnes, utilisez le reseau Noctilien.
</p>
HTML,
    ],
    'faq' => [
        'title' => 'Questions frequentes sur le RER',
        'items' => [
            ['question' => 'Quelle est la difference entre le metro et le RER ?',
             'answer'   => '<p>Le <strong>metro</strong> dessert Paris et sa proche banlieue avec des stations tous les 500 metres. Le <strong>RER</strong> couvre toute l\'Ile-de-France avec des gares plus espacees et des trains plus rapides. Dans Paris, meme tarif unique (2,50 euros).</p>'],
            ['question' => 'Combien coute un trajet en RER depuis Roissy-CDG ?',
             'answer'   => '<p>Le billet <strong>Paris - Roissy-CDG</strong> en RER B coute environ <strong>11,80 a 13 euros</strong> en 2026. C\'est l\'option la plus rapide et economique depuis l\'aeroport.</p>'],
            ['question' => 'Le RER A passe-t-il par Disneyland Paris ?',
             'answer'   => '<p>Oui, la branche est du RER A se termine a <strong>Marne-la-Vallee - Chessy</strong>, a l\'entree du parc Disneyland. Trajet depuis Paris : environ 40 minutes.</p>'],
            ['question' => 'Le RER circule-t-il la nuit ?',
             'answer'   => '<p>Non, le RER arrete son service entre <strong>minuit environ et 5h du matin</strong>. Pour voyager la nuit, utilisez les bus Noctilien.</p>'],
            ['question' => 'Quelle est la ligne de RER la plus ponctuelle ?',
             'answer'   => '<p>Les lignes <strong>E et A</strong> sont generalement les plus ponctuelles. Les lignes B, C et D connaissent plus de retards car partagees avec les trains SNCF.</p>'],
            ['question' => 'Peut-on voyager avec un velo dans le RER ?',
             'answer'   => '<p>Oui, les velos sont autorises <strong>en dehors des heures de pointe</strong> (avant 6h30, entre 9h et 16h30, apres 19h en semaine, toute la journee le week-end).</p>'],
        ],
    ],
];
