<?php
return [
    'seo' => [
        'title'       => 'Bus à Paris et en Île-de-France : réseau, horaires et tarifs 2026',
        'description' => 'Guide complet des bus en Île-de-France : lignes Mobilien, bus parisiens, Noctilien pour la nuit, tarifs, horaires et conseils pratiques.',
        'canonical'   => 'https://bougeaparis.fr/bus/',
        'og_type'     => 'article',
    ],
    'hero' => [
        'h1'       => 'Les bus en Île-de-France',
        'subtitle' => 'Plus de 1 500 lignes de bus couvrent Paris et sa région : Mobilien, réseau parisien, banlieue et Noctilien la nuit.',
        'chiffres' => [
            ['value' => '1500+', 'label' => 'Lignes'],
            ['value' => '10 000+', 'label' => 'Arrêts'],
            ['value' => '47', 'label' => 'Lignes Noctilien'],
            ['value' => '24h/24', 'label' => 'Avec Noctilien'],
        ],
    ],
    'intro' => <<<'HTML'
<p class="lead">
    Le réseau de <strong>bus en Île-de-France</strong> est l'un des plus denses au monde. Avec plus
    de <strong>1 500 lignes</strong> et <strong>10 000 arrêts</strong>, il dessert l'intégralité du
    territoire : Paris intramuros, petite couronne et grande couronne.
</p>
<p>
    Le réseau bus complète efficacement le métro et le RER, en desservant les zones peu accessibles
    par rail, et en circulant <strong>la nuit</strong> grâce au réseau <a href="/bus/noctilien/">Noctilien</a>.
</p>
<p>
    Les bus d'Île-de-France sont accessibles aux personnes à mobilité réduite sur la quasi-totalité
    du réseau, et desservent des lieux emblématiques souvent mal desservis par le métro (Montmartre,
    certaines parties du 16e arrondissement).
</p>
HTML,
    'section_reseaux' => [
        'title' => 'Les différents réseaux de bus',
        'content' => <<<'HTML'
<ul>
    <li><strong>Bus Mobilien</strong> : lignes à haut niveau de service (fréquence élevée, amplitude horaire large).</li>
    <li><strong>Bus parisiens (20 à 96)</strong> : lignes historiques de Paris et proche banlieue.</li>
    <li><strong>Bus de banlieue (100 à 799)</strong> : lignes reliant les villes de petite et grande couronne.</li>
    <li><strong>Bus Express</strong> : liaisons rapides inter-banlieues avec peu d'arrêts.</li>
    <li><strong>Petite Ceinture (PC1, PC2, PC3)</strong> : lignes historiques contournant Paris.</li>
    <li><strong>Noctilien</strong> : 47 lignes de bus de nuit (0h30 à 5h30).</li>
</ul>
HTML,
    ],
    'section_tarifs' => [
        'title' => 'Tarifs des bus en 2026',
        'content' => <<<'HTML'
<p>
    Depuis 2025, le <strong>ticket bus-tram</strong> coûte <strong>2 euros</strong> à l'unité. Il est
    valable 1h30 après validation, avec correspondance illimitée entre bus et tramways (mais pas
    avec le métro/RER).
</p>
<p>
    Les cartes <strong>Navigo</strong> (Jour, Semaine, Mois, Annuel) sont valables sur tous les bus
    d'Île-de-France, sans supplément.
</p>
HTML,
    ],
    'faq' => [
        'title' => 'Questions fréquentes sur les bus',
        'items' => [
            ['question' => 'Combien coûte un ticket de bus à Paris ?',
             'answer'   => '<p>Un ticket unitaire bus-tram coûte <strong>2 euros</strong> en 2026, valable 1h30 avec correspondances illimitées bus/tram.</p>'],
            ['question' => 'Peut-on acheter son ticket directement dans le bus ?',
             'answer'   => '<p>Oui, au tarif majoré de <strong>2,50 euros</strong>. Privilégiez l\'achat avant le voyage pour économiser.</p>'],
            ['question' => 'Les bus circulent-ils la nuit ?',
             'answer'   => '<p>Oui, le réseau <strong>Noctilien</strong> assure le service entre 0h30 et 5h30 avec 47 lignes couvrant Paris et sa banlieue.</p>'],
            ['question' => 'Les bus sont-ils accessibles PMR ?',
             'answer'   => '<p>Oui, <strong>la quasi-totalité des bus</strong> sont accessibles PMR : plancher bas, palette rétractable, emplacement dédié.</p>'],
            ['question' => 'Comment fonctionnent les bus Mobilien ?',
             'answer'   => '<p>Les lignes <strong>Mobilien</strong> offrent un bus toutes les 5-10 minutes en journée, une amplitude horaire large et des arrêts aménagés. Recommandées pour les trajets quotidiens.</p>'],
        ],
    ],
];
