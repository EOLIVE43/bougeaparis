<?php
return [
    'seo' => [
        'title'       => 'Bus a Paris et en Ile-de-France : reseau, horaires et tarifs 2026',
        'description' => 'Guide complet des bus en Ile-de-France : lignes Mobilien, bus parisiens, Noctilien pour la nuit, tarifs, horaires et conseils pratiques.',
        'canonical'   => 'https://bougeaparis.fr/bus/',
        'og_type'     => 'article',
    ],
    'hero' => [
        'h1'       => 'Les bus en Ile-de-France',
        'subtitle' => 'Plus de 1 500 lignes de bus couvrent Paris et sa region : Mobilien, reseau parisien, banlieue et Noctilien la nuit.',
        'chiffres' => [
            ['value' => '1500+', 'label' => 'Lignes'],
            ['value' => '10 000+', 'label' => 'Arrets'],
            ['value' => '47', 'label' => 'Lignes Noctilien'],
            ['value' => '24h/24', 'label' => 'Avec Noctilien'],
        ],
    ],
    'intro' => <<<'HTML'
<p class="lead">
    Le reseau de <strong>bus en Ile-de-France</strong> est l'un des plus denses au monde. Avec plus
    de <strong>1 500 lignes</strong> et <strong>10 000 arrets</strong>, il dessert l'integralite du
    territoire : Paris intramuros, petite couronne et grande couronne.
</p>
<p>
    Le reseau bus complete efficacement le metro et le RER, en desservant les zones peu accessibles
    par rail, et en circulant <strong>la nuit</strong> grace au reseau <a href="/bus/noctilien/">Noctilien</a>.
</p>
<p>
    Les bus d'Ile-de-France sont accessibles aux personnes a mobilite reduite sur la quasi-totalite
    du reseau, et desservent des lieux emblematiques souvent mal desservis par le metro (Montmartre,
    certaines parties du 16e arrondissement).
</p>
HTML,
    'section_reseaux' => [
        'title' => 'Les differents reseaux de bus',
        'content' => <<<'HTML'
<ul>
    <li><strong>Bus Mobilien</strong> : lignes a haut niveau de service (frequence elevee, amplitude horaire large).</li>
    <li><strong>Bus parisiens (20 a 96)</strong> : lignes historiques de Paris et proche banlieue.</li>
    <li><strong>Bus de banlieue (100 a 799)</strong> : lignes reliant les villes de petite et grande couronne.</li>
    <li><strong>Bus Express</strong> : liaisons rapides inter-banlieues avec peu d'arrets.</li>
    <li><strong>Petite Ceinture (PC1, PC2, PC3)</strong> : lignes historiques contournant Paris.</li>
    <li><strong>Noctilien</strong> : 47 lignes de bus de nuit (0h30 a 5h30).</li>
</ul>
HTML,
    ],
    'section_tarifs' => [
        'title' => 'Tarifs des bus en 2026',
        'content' => <<<'HTML'
<p>
    Depuis 2025, le <strong>ticket bus-tram</strong> coute <strong>2 euros</strong> a l'unite. Il est
    valable 1h30 apres validation, avec correspondance illimitee entre bus et tramways (mais pas
    avec le metro/RER).
</p>
<p>
    Les cartes <strong>Navigo</strong> (Jour, Semaine, Mois, Annuel) sont valables sur tous les bus
    d'Ile-de-France, sans supplement.
</p>
HTML,
    ],
    'faq' => [
        'title' => 'Questions frequentes sur les bus',
        'items' => [
            ['question' => 'Combien coute un ticket de bus a Paris ?',
             'answer'   => '<p>Un ticket unitaire bus-tram coute <strong>2 euros</strong> en 2026, valable 1h30 avec correspondances illimitees bus/tram.</p>'],
            ['question' => 'Peut-on acheter son ticket directement dans le bus ?',
             'answer'   => '<p>Oui, au tarif majore de <strong>2,50 euros</strong>. Privilegiez l\'achat avant le voyage pour economiser.</p>'],
            ['question' => 'Les bus circulent-ils la nuit ?',
             'answer'   => '<p>Oui, le reseau <strong>Noctilien</strong> assure le service entre 0h30 et 5h30 avec 47 lignes couvrant Paris et sa banlieue.</p>'],
            ['question' => 'Les bus sont-ils accessibles PMR ?',
             'answer'   => '<p>Oui, <strong>la quasi-totalite des bus</strong> sont accessibles PMR : plancher bas, palette retractable, emplacement dedie.</p>'],
            ['question' => 'Comment fonctionnent les bus Mobilien ?',
             'answer'   => '<p>Les lignes <strong>Mobilien</strong> offrent un bus toutes les 5-10 minutes en journee, une amplitude horaire large et des arrets amenages. Recommandees pour les trajets quotidiens.</p>'],
        ],
    ],
];
