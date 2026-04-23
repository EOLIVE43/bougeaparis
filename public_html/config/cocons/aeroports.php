<?php
return [
    'seo' => [
        'title'       => 'Aéroports de Paris : CDG, Orly, Beauvais - Accès et transports 2026',
        'description' => 'Guide complet des aéroports parisiens : Charles de Gaulle, Orly, Beauvais. Comment y aller depuis Paris en RER, métro, bus, taxi.',
        'canonical'   => 'https://bougeaparis.fr/aeroports/',
        'og_type'     => 'article',
    ],
    'hero' => [
        'h1'       => 'Les aéroports de Paris',
        'subtitle' => 'Trois aéroports desservent la région parisienne : Roissy-CDG, Paris-Orly et Paris-Beauvais.',
        'chiffres' => [
            ['value' => '3', 'label' => 'Aéroports'],
            ['value' => '108M', 'label' => 'Passagers/an'],
            ['value' => '25', 'label' => 'Km CDG-Paris'],
            ['value' => '14', 'label' => 'Km Orly-Paris'],
        ],
    ],
    'intro' => <<<'HTML'
<p class="lead">
    La région parisienne compte <strong>trois aéroports</strong> majeurs qui accueillent chaque année
    plus de 108 millions de passagers : <strong>Paris-Charles de Gaulle</strong> (CDG), le plus grand,
    <strong>Paris-Orly</strong> (ORY) historiquement le premier de la région, et
    <strong>Paris-Beauvais</strong> (BVA), dédié aux compagnies low-cost.
</p>
<p>
    Chaque aéroport dispose de plusieurs options de transport pour rejoindre Paris :
    <strong>RER, métro, tramway, bus</strong>, navettes spécifiques, taxis ou VTC. Le choix dépend
    de votre budget, de votre horaire d'arrivée et du volume de bagages.
</p>
<p>
    Depuis 2024, l'extension de la <strong>ligne 14 du métro jusqu'à Orly</strong> a révolutionné
    l'accès à cet aéroport depuis le centre de Paris.
</p>
HTML,
    'section_cdg' => [
        'title' => 'Aéroport Paris-Charles de Gaulle (CDG)',
        'content' => <<<'HTML'
<p>
    L'aéroport <strong>Paris-Charles de Gaulle (Roissy)</strong>, situé à <strong>25 km au nord-est
    de Paris</strong>, est le plus grand aéroport de France et le 2e d'Europe. Il compte 3 terminaux
    (1, 2, 3) et accueille plus de 70 millions de passagers par an.
</p>
<h3>Comment aller de Paris à CDG ?</h3>
<ul>
    <li><strong>RER B</strong> : option la plus rapide (30 min depuis Châtelet). Prix : 11,80 à 13 euros.</li>
    <li><strong>Roissybus</strong> : depuis Opéra, environ 60 min. Prix : 16,60 euros.</li>
    <li><strong>Bus 350 ou 351</strong> : plus économique (2 euros) mais plus lent (1h15).</li>
    <li><strong>Taxi</strong> : forfait fixe de <strong>56 euros</strong> (Rive Droite) ou <strong>65 euros</strong> (Rive Gauche).</li>
    <li><strong>CDGVAL</strong> : navette gratuite qui relie les terminaux entre eux.</li>
</ul>
HTML,
    ],
    'section_orly' => [
        'title' => 'Aéroport Paris-Orly (ORY)',
        'content' => <<<'HTML'
<p>
    L'aéroport <strong>Paris-Orly</strong>, situé à seulement <strong>14 km au sud de Paris</strong>,
    accueille environ 33 millions de passagers par an. Il dispose de 4 terminaux (Orly 1, 2, 3, 4).
</p>
<h3>Comment aller de Paris à Orly ?</h3>
<ul>
    <li><strong>Métro ligne 14</strong> : depuis 2024, liaison directe depuis Châtelet en 30 minutes. Prix : 2,50 euros.</li>
    <li><strong>Tramway T7</strong> : depuis Villejuif (métro 7). Prix : 2 euros.</li>
    <li><strong>RER B + Orlyval</strong> : via Antony. Prix : environ 12 euros.</li>
    <li><strong>Orlybus</strong> : depuis Denfert-Rochereau. Prix : 11,50 euros.</li>
    <li><strong>Taxi</strong> : forfait fixe de <strong>41 euros</strong> (Rive Gauche) ou <strong>50 euros</strong> (Rive Droite).</li>
</ul>
HTML,
    ],
    'section_beauvais' => [
        'title' => 'Aéroport Paris-Beauvais (BVA)',
        'content' => <<<'HTML'
<p>
    L'aéroport <strong>Paris-Beauvais</strong>, à <strong>85 km au nord de Paris</strong>, est
    principalement utilisé par les compagnies low-cost (Ryanair, Wizz Air). Il accueille environ
    5 millions de passagers par an.
</p>
<h3>Comment aller de Paris à Beauvais ?</h3>
<ul>
    <li><strong>Navette officielle</strong> depuis Porte Maillot (métro 1) : trajet 1h15, environ 17 euros.</li>
    <li><strong>Train SNCF</strong> depuis Gare du Nord jusqu'à Beauvais + navette locale.</li>
    <li><strong>Taxi</strong> : environ 160 euros (tarif libre, non réglementé).</li>
</ul>
<p class="notice">
    <strong>Attention :</strong> en raison de la distance, prévoyez toujours une marge confortable
    pour rejoindre Beauvais (minimum 3h avant votre vol).
</p>
HTML,
    ],
    'faq' => [
        'title' => 'Questions fréquentes sur les aéroports de Paris',
        'items' => [
            ['question' => 'Quel est le moyen le plus rapide pour aller à Roissy-CDG depuis Paris ?',
             'answer'   => '<p>Le <strong>RER B</strong> est le plus rapide : 30 minutes depuis Châtelet, pour 11,80 à 13 euros.</p>'],
            ['question' => 'Comment aller à Orly depuis Paris en 2026 ?',
             'answer'   => '<p>Depuis l\'ouverture de la ligne 14 en 2024, le <strong>métro 14</strong> est la solution la plus rapide et économique : 30 min pour 2,50 euros.</p>'],
            ['question' => 'Combien coûte un taxi de Paris vers CDG ou Orly ?',
             'answer'   => '<p>Les taxis parisiens pratiquent un <strong>forfait fixe</strong> : 56-65 euros pour CDG, 41-50 euros pour Orly, selon la rive.</p>'],
            ['question' => 'Les transports vers les aéroports circulent-ils la nuit ?',
             'answer'   => '<p>Le RER B fonctionne environ de 5h à minuit. La nuit, utilisez les bus Noctilien N140 (CDG) et N31/N144 (Orly), ou un taxi.</p>'],
            ['question' => 'Peut-on utiliser son Pass Navigo pour aller à CDG ?',
             'answer'   => '<p>Oui, depuis 2025 le <strong>Navigo Semaine et Mois</strong> inclut les trajets vers les aéroports, sans supplément.</p>'],
        ],
    ],
];
