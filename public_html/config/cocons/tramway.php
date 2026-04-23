<?php
return [
    'seo' => [
        'title'       => 'Tramway en Ile-de-France : 13 lignes, plan et horaires 2026',
        'description' => 'Le tramway a Paris et en Ile-de-France : 13 lignes (T1 a T13), plan du reseau, horaires, tarifs et conseils pratiques pour voyager.',
        'canonical'   => 'https://bougeaparis.fr/tramway/',
        'og_type'     => 'article',
    ],
    'hero' => [
        'h1'       => 'Le tramway en Ile-de-France',
        'subtitle' => 'Un reseau moderne et ecologique de 13 lignes qui ceinture Paris et dessert la petite couronne.',
        'chiffres' => [
            ['value' => '13', 'label' => 'Lignes'],
            ['value' => '260+', 'label' => 'Stations'],
            ['value' => '180', 'label' => 'Km de reseau'],
            ['value' => '100%', 'label' => 'Accessible PMR'],
        ],
    ],
    'intro' => <<<'HTML'
<p class="lead">
    Le <strong>tramway francilien</strong> est un reseau moderne, recent et en pleine expansion.
    Inaugure en 1992 avec la ligne T1, il compte aujourd'hui <strong>13 lignes (T1 a T13)</strong>
    qui desservent majoritairement la petite couronne et les limites de Paris.
</p>
<p>
    Le tramway est apprecie pour son <strong>confort</strong> (rames spacieuses, climatisation),
    sa <strong>ponctualite</strong> (site propre) et son <strong>accessibilite totale</strong>
    aux personnes a mobilite reduite.
</p>
<p>
    C'est aussi une solution ecologique : 100% electrique, silencieux, et integre dans des
    amenagements urbains soignes.
</p>
HTML,
    'section_lignes' => [
        'title' => 'Les 13 lignes de tramway',
        'content' => <<<'HTML'
<ul>
    <li><strong>Tramways de ceinture de Paris</strong> : T3a et T3b, sur les boulevards des Marechaux.</li>
    <li><strong>Tramways de petite couronne</strong> : T1, T2, T5, T6, T7, T8, T9, T10, T11.</li>
    <li><strong>Tramways de grande couronne</strong> : T4, T12, T13.</li>
</ul>
<p>
    Chaque ligne a sa propre couleur officielle et un numero unique commencant par "T".
</p>
HTML,
    ],
    'section_tarifs' => [
        'title' => 'Tarifs du tramway',
        'content' => <<<'HTML'
<p>
    Le <strong>ticket bus-tram coute 2 euros</strong> a l'unite, valable 1h30 avec correspondances
    illimitees entre bus et tramways. Les cartes Navigo sont valables sur l'ensemble du reseau.
</p>
HTML,
    ],
    'faq' => [
        'title' => 'Questions frequentes sur le tramway',
        'items' => [
            ['question' => 'Combien coute un trajet en tramway ?',
             'answer'   => '<p>Un ticket bus-tram coute <strong>2 euros</strong> a l\'unite en 2026, valable 1h30 avec correspondances illimitees.</p>'],
            ['question' => 'Les tramways sont-ils accessibles PMR ?',
             'answer'   => '<p>Oui, <strong>100% du reseau tramway est accessible</strong> : quais de plain-pied, rames avec plancher bas, information sonore et visuelle.</p>'],
            ['question' => 'Quels sont les horaires des tramways ?',
             'answer'   => '<p>Les tramways circulent generalement de <strong>5h a 0h30</strong>. Certaines lignes prolongent jusqu\'a 1h30 le week-end. Frequence : 4 a 6 minutes en pointe.</p>'],
            ['question' => 'Y a-t-il des tramways qui traversent Paris ?',
             'answer'   => '<p>Non, aucun tramway ne traverse Paris intramuros. Les lignes <strong>T3a et T3b</strong> circulent sur les boulevards des Marechaux autour de Paris.</p>'],
            ['question' => 'Quelle est la ligne de tram la plus longue ?',
             'answer'   => '<p>La <strong>T4</strong> (Bondy - Arboretum / Hopital de Montfermeil) est l\'une des plus longues avec ses 20 stations et son parcours en tram-train.</p>'],
        ],
    ],
];
