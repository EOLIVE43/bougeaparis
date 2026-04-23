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
            'label' => 'Blog',
            'url'   => '/blog/',
            'icon'  => 'blog',
        ],
    ],
    // Menu footer - colonne 1 : découvrir
    'footer_discover' => [
        ['label' => 'Métro de Paris',    'url' => '/metro/'],
        ['label' => 'Réseau RER',        'url' => '/rer/'],
        ['label' => 'Lignes de bus',     'url' => '/bus/'],
        ['label' => 'Tramways',          'url' => '/tramway/'],
        ['label' => 'Aéroports',         'url' => '/aeroports/'],
        ['label' => 'Transilien',        'url' => '/transilien/'],
    ],
    // Menu footer - colonne 2 : utile
    // Les pages /itineraires/, /tarifs/, /plans/ arriveront en Livraison 5+
    // En attendant, seul /blog/ est actif
    'footer_tools' => [
        ['label' => 'Blog',              'url' => '/blog/'],
    ],
    // Menu footer - colonne 3 : à propos
    'footer_about' => [
        ['label' => 'À propos',          'url' => '/a-propos/'],
        ['label' => 'Contact',           'url' => '/contact/'],
        ['label' => 'Mentions légales',  'url' => '/mentions-legales/'],
        ['label' => 'Confidentialité',   'url' => '/confidentialite/'],
    ],
];
