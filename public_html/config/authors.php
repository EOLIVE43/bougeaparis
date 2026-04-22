<?php
/**
 * Configuration des auteurs du site
 *
 * Chaque article de blog reference un auteur par son slug.
 * Le systeme recupere automatiquement les infos ici.
 */

return [
    'ludo' => [
        'name'        => 'Ludo',
        'full_name'   => 'Ludovic',
        'slug'        => 'ludo',
        'url'         => '/auteur/ludo/',
        'avatar'      => '/assets/img/authors/ludo.svg',
        'role'        => 'Redacteur',
        'bio'         => 'Passionne de Paris et de ses transports, Ludo couvre l\'actualite du reseau, les travaux, le trafic et les analyses pratiques pour les Franciliens au quotidien.',
        'specialties' => ['trafic', 'travaux', 'metro', 'infos pratiques'],
    ],

    'elodie' => [
        'name'        => 'Elodie',
        'full_name'   => 'Elodie',
        'slug'        => 'elodie',
        'url'         => '/auteur/elodie/',
        'avatar'      => '/assets/img/authors/elodie.svg',
        'role'        => 'Redactrice',
        'bio'         => 'Amoureuse du patrimoine parisien, Elodie partage ses decouvertes, ses itineraires touristiques et l\'histoire des stations de la capitale.',
        'specialties' => ['tourisme', 'patrimoine', 'itineraires', 'histoire'],
    ],
];
