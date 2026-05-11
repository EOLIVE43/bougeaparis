<?php
/**
 * Configuration de la navigation du site
 *
 * Menu principal (header) refondu en 5 entrees thematiques niveau 1 :
 *   1. Se deplacer  -> hub agregant les 7 modes (metro, rer, bus, ...)
 *   2. Visiter      -> hub tourisme par categorie de POI
 *   3. Itineraires  -> placeholder (planificateur a venir)
 *   4. Trafic temps reel -> /info-trafic/ (route blog actuelle)
 *   5. Tarifs       -> cluster IDFM
 *
 * Les sous-menus (children) sont exposes au hover/focus-within desktop
 * et inline mobile (cf. templates/layout/header.php + bundle.css mega-menu).
 */
return [
    // Menu principal (header) — 5 entrees niveau 1
    'main' => [
        [
            'label' => 'Se déplacer',
            'url'   => '/se-deplacer/',
            'icon'  => 'metro',
            'children' => [
                ['label' => 'Métro',      'url' => '/metro/',     'icon' => 'metro'],
                ['label' => 'RER',        'url' => '/rer/',       'icon' => 'rer'],
                ['label' => 'Bus',        'url' => '/bus/',       'icon' => 'bus'],
                ['label' => 'Tramway',    'url' => '/tramway/',   'icon' => 'tram'],
                ['label' => 'Transilien', 'url' => '/transilien/','icon' => 'train'],
                ['label' => 'Gares',      'url' => '/gares/',     'icon' => 'train'],
                ['label' => 'Aéroports',  'url' => '/aeroports/', 'icon' => 'plane'],
            ],
        ],
        [
            'label' => 'Visiter',
            'url'   => '/visiter/',
            'icon'  => 'blog',
            'children' => [
                ['label' => 'Monuments emblématiques',  'url' => '/visiter/#monuments'],
                ['label' => 'Musées & arts',            'url' => '/visiter/#musees'],
                ['label' => 'Places & avenues',         'url' => '/visiter/#places-avenues'],
                ['label' => 'Jardins & espaces verts',  'url' => '/visiter/#jardins'],
                ['label' => 'Patrimoine religieux',     'url' => '/visiter/#patrimoine-religieux'],
                ['label' => 'Ponts & rives de Seine',   'url' => '/visiter/#ponts-seine'],
                ['label' => 'Vie parisienne',           'url' => '/visiter/#vie-parisienne'],
            ],
        ],
        [
            'label' => 'Itinéraires',
            'url'   => '/itineraires/',
            'icon'  => 'metro',
        ],
        [
            'label' => 'Trafic temps réel',
            'url'   => '/info-trafic/',
            'icon'  => 'blog',
        ],
        [
            'label' => 'Tarifs',
            'url'   => '/tarifs/',
            'icon'  => 'metro',
        ],
    ],

    // Menu footer - colonne 1 : se deplacer
    'footer_discover' => [
        ['label' => 'Se déplacer',       'url' => '/se-deplacer/'],
        ['label' => 'Métro de Paris',    'url' => '/metro/'],
        ['label' => 'Réseau RER',        'url' => '/rer/'],
        ['label' => 'Lignes de bus',     'url' => '/bus/'],
        ['label' => 'Tramways',          'url' => '/tramway/'],
        ['label' => 'Gares parisiennes', 'url' => '/gares/'],
        ['label' => 'Aéroports',         'url' => '/aeroports/'],
        ['label' => 'Transilien',        'url' => '/transilien/'],
    ],
    // Menu footer - colonne 2 : utile
    'footer_tools' => [
        ['label' => 'Visiter Paris',  'url' => '/visiter/'],
        ['label' => 'Tarifs',         'url' => '/tarifs/'],
        ['label' => 'Itinéraires',    'url' => '/itineraires/'],
        ['label' => 'Info-Trafic',    'url' => '/info-trafic/'],
    ],
    // Menu footer - colonne 3 : a propos
    'footer_about' => [
        ['label' => 'À propos',           'url' => '/a-propos/'],
        ['label' => 'Contact',            'url' => '/contact/'],
        ['label' => 'Sources et données', 'url' => '/sources/'],
        ['label' => 'Mentions légales',   'url' => '/mentions-legales/'],
        ['label' => 'Confidentialité',    'url' => '/confidentialite/'],
    ],
];
