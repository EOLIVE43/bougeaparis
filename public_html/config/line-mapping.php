<?php
/**
 * Mapping des identifiants PRIM (IDFM) vers les slugs du site.
 * Source : https://prim.iledefrance-mobilites.fr
 * On ne stocke que la partie utile des IDs PRIM (ex : C01371)
 */

return [
    'metro' => [
        'C01371' => 'metro-1', 'C01372' => 'metro-2', 'C01373' => 'metro-3',
        'C01386' => 'metro-3bis', 'C01374' => 'metro-4', 'C01375' => 'metro-5',
        'C01376' => 'metro-6', 'C01377' => 'metro-7', 'C01387' => 'metro-7bis',
        'C01378' => 'metro-8', 'C01379' => 'metro-9', 'C01380' => 'metro-10',
        'C01381' => 'metro-11', 'C01382' => 'metro-12', 'C01383' => 'metro-13',
        'C01384' => 'metro-14',
    ],
    'rer' => [
        'C01742' => 'rer-a', 'C01743' => 'rer-b', 'C01727' => 'rer-c',
        'C01728' => 'rer-d', 'C01729' => 'rer-e',
    ],
    'tramway' => [
        'C01389' => 'tram-1', 'C01390' => 'tram-2', 'C01391' => 'tram-3a',
        'C01794' => 'tram-3b', 'C01843' => 'tram-4', 'C01684' => 'tram-5',
        'C01774' => 'tram-7', 'C01795' => 'tram-8', 'C02317' => 'tram-9',
        'C02344' => 'tram-10', 'C01999' => 'tram-11', 'C02528' => 'tram-12',
    ],
    'transilien' => [
        'C01737' => 'transilien-h', 'C01739' => 'transilien-j',
        'C01738' => 'transilien-k', 'C01740' => 'transilien-l',
        'C01736' => 'transilien-n', 'C01730' => 'transilien-p',
        'C01731' => 'transilien-r', 'C01741' => 'transilien-u',
    ],
    'bus' => [
        // A completer au fur et a mesure (350 lignes)
    ],
];
