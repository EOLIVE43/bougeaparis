<?php
/**
 * Configuration de la navigation du site
 *
 * Menu principal (header) et menus secondaires (footer).
 * Modifier ce fichier pour changer les liens de navigation partout.
 */

return [
    // Menu principal (header)
    'main' => [
        [
            'label' => 'Metro',
            'url'   => '/metro/',
            'icon'  => 'metro',
        ],
        [
            'label' => 'RER',
            'url'   => '/rer/',
            'icon'  => 'rer',
        ],
        [
            'label' => 'Bus',
            'url'   => '/bus/',
            'icon'  => 'bus',
        ],
        [
            'label' => 'Tramway',
            'url'   => '/tramway/',
            'icon'  => 'tram',
        ],
        [
            'label' => 'Aeroports',
            'url'   => '/aeroports/',
            'icon'  => 'plane',
        ],
        [
            'label' => 'Transilien',
            'url'   => '/transilien/',
            'icon'  => 'train',
        ],
        [
            'label' => 'Blog',
            'url'   => '/blog/',
            'icon'  => 'blog',
        ],
    ],

    // Menu footer - colonne 1 : decouvrir
    'footer_discover' => [
        ['label' => 'Metro de Paris',    'url' => '/metro/'],
        ['label' => 'Reseau RER',        'url' => '/rer/'],
        ['label' => 'Lignes de bus',     'url' => '/bus/'],
        ['label' => 'Tramways',          'url' => '/tramway/'],
        ['label' => 'Aeroports',         'url' => '/aeroports/'],
        ['label' => 'Transilien',        'url' => '/transilien/'],
    ],

    // Menu footer - colonne 2 : utile
    'footer_tools' => [
        ['label' => 'Blog',              'url' => '/blog/'],
        ['label' => 'Itineraires',       'url' => '/itineraires/'],
        ['label' => 'Tarifs',            'url' => '/tarifs/'],
        ['label' => 'Plans',             'url' => '/plans/'],
    ],

    // Menu footer - colonne 3 : a propos
    'footer_about' => [
        ['label' => 'A propos',          'url' => '/a-propos/'],
        ['label' => 'Contact',           'url' => '/contact/'],
        ['label' => 'Mentions legales',  'url' => '/mentions-legales/'],
        ['label' => 'Confidentialite',   'url' => '/confidentialite/'],
    ],
];
