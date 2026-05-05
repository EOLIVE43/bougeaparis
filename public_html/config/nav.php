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
            'label' => 'Métro',
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
            'label' => 'Gares',
            'url'   => '/gares/',
            'icon'  => 'train',
        ],
        [
            'label' => 'Aéroports',
            'url'   => '/aeroports/',
            'icon'  => 'plane',
        ],
        [
            'label' => 'Transilien',
            'url'   => '/transilien/',
            'icon'  => 'train',
        ],
        [
            'label' => 'Info-Trafic',
            'url'   => '/info-trafic/',
            'icon'  => 'blog',
        ],
    ],
    // Menu footer - colonne 1 : découvrir
    'footer_discover' => [
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
        ['label' => 'Info-Trafic',       'url' => '/info-trafic/'],
    ],
    // Menu footer - colonne 3 : à propos
    'footer_about' => [
        ['label' => 'À propos',          'url' => '/a-propos/'],
        ['label' => 'Contact',           'url' => '/contact/'],
        ['label' => 'Sources et données', 'url' => '/sources/'],
        ['label' => 'Mentions légales',  'url' => '/mentions-legales/'],
        ['label' => 'Confidentialité',   'url' => '/confidentialite/'],
    ],
];
