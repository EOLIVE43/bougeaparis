<?php
return [
    'seo' => [
        'title'       => 'Tramway en Île-de-France : 13 lignes, plan et horaires 2026',
        'description' => 'Le tramway à Paris et en Île-de-France : 13 lignes (T1 à T13), plan du réseau, horaires, tarifs et conseils pratiques pour voyager.',
        'canonical'   => 'https://bougeaparis.fr/tramway/',
        'og_type'     => 'article',
    ],
    'hero' => [
        'h1'       => 'Le tramway en Île-de-France',
        'subtitle' => 'Un réseau moderne et écologique de 13 lignes qui ceinture Paris et dessert la petite couronne.',
        'chiffres' => [
            ['value' => '13', 'label' => 'Lignes'],
            ['value' => '260+', 'label' => 'Stations'],
            ['value' => '180', 'label' => 'Km de réseau'],
            ['value' => '100%', 'label' => 'Accessible PMR'],
        ],
    ],
    'intro' => <<<'HTML'
<p class="lead">
    Le <strong>tramway francilien</strong> est un réseau moderne, récent et en pleine expansion.
    Inauguré en 1992 avec la ligne T1, il compte aujourd'hui <strong>13 lignes (T1 à T13)</strong>
    qui desservent majoritairement la petite couronne et les limites de Paris.
</p>
<p>
    Le tramway est apprécié pour son <strong>confort</strong> (rames spacieuses, climatisation),
    sa <strong>ponctualité</strong> (site propre) et son <strong>accessibilité totale</strong>
    aux personnes à mobilité réduite.
</p>
<p>
    C'est aussi une solution écologique : 100% électrique, silencieux, et intégré dans des
    aménagements urbains soignés.
</p>
HTML,
    'section_lignes' => [
        'title' => 'Les 13 lignes de tramway',
        'content' => <<<'HTML'
<ul>
    <li><strong>Tramways de ceinture de Paris</strong> : T3a et T3b, sur les boulevards des Maréchaux.</li>
    <li><strong>Tramways de petite couronne</strong> : T1, T2, T5, T6, T7, T8, T9, T10, T11.</li>
    <li><strong>Tramways de grande couronne</strong> : T4, T12, T13.</li>
</ul>
<p>
    Chaque ligne a sa propre couleur officielle et un numéro unique commençant par "T".
</p>
HTML,
    ],
    'section_tarifs' => [
        'title' => 'Tarifs du tramway',
        'content' => <<<'HTML'
<p>
    Le <strong>ticket bus-tram coûte 2 euros</strong> à l'unité, valable 1h30 avec correspondances
    illimitées entre bus et tramways. Les cartes Navigo sont valables sur l'ensemble du réseau.
</p>
HTML,
    ],
    'faq' => [
        'title' => 'Questions fréquentes sur le tramway',
        'items' => [
            ['question' => 'Combien coûte un trajet en tramway ?',
             'answer'   => '<p>Un ticket bus-tram coûte <strong>2 euros</strong> à l\'unité en 2026, valable 1h30 avec correspondances illimitées.</p>'],
            ['question' => 'Les tramways sont-ils accessibles PMR ?',
             'answer'   => '<p>Oui, <strong>100% du réseau tramway est accessible</strong> : quais de plain-pied, rames avec plancher bas, information sonore et visuelle.</p>'],
            ['question' => 'Quels sont les horaires des tramways ?',
             'answer'   => '<p>Les tramways circulent généralement de <strong>5h à 0h30</strong>. Certaines lignes prolongent jusqu\'à 1h30 le week-end. Fréquence : 4 à 6 minutes en pointe.</p>'],
            ['question' => 'Y a-t-il des tramways qui traversent Paris ?',
             'answer'   => '<p>Non, aucun tramway ne traverse Paris intramuros. Les lignes <strong>T3a et T3b</strong> circulent sur les boulevards des Maréchaux autour de Paris.</p>'],
            ['question' => 'Quelle est la ligne de tram la plus longue ?',
             'answer'   => '<p>La <strong>T4</strong> (Bondy - Arboretum / Hôpital de Montfermeil) est l\'une des plus longues avec ses 20 stations et son parcours en tram-train.</p>'],
        ],
    ],
];
