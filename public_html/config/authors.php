<?php
/**
 * Configuration des auteurs du site
 *
 * Chaque article de blog référence un auteur par son slug.
 * Le système récupère automatiquement les infos ici.
 */
return [
    'ludo' => [
        'name'        => 'Ludo',
        'full_name'   => 'Ludovic',
        'slug'        => 'ludo',
        'url'         => '/auteur/ludo/',
        'avatar'      => '/assets/img/authors/ludo.svg',
        'role'        => 'Rédacteur',
        'bio'         => 'Passionné de Paris et de ses transports, Ludo couvre l\'actualité du réseau, les travaux, le trafic et les analyses pratiques pour les Franciliens au quotidien.',
        'specialties' => ['trafic', 'travaux', 'métro', 'infos pratiques'],
    ],
    'elodie' => [
        'name'        => 'Élodie',
        'full_name'   => 'Élodie',
        'slug'        => 'elodie',
        'url'         => '/auteur/elodie/',
        'avatar'      => '/assets/img/authors/elodie.svg',
        'role'        => 'Rédactrice',
        'bio'         => 'Amoureuse du patrimoine parisien, Élodie partage ses découvertes, ses itinéraires touristiques et l\'histoire des stations de la capitale.',
        'specialties' => ['tourisme', 'patrimoine', 'itinéraires', 'histoire'],
    ],
];
