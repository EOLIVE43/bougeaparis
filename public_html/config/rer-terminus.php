<?php
/**
 * Mapping curatorial : terminus officiels des 5 lignes RER d'Île-de-France.
 *
 * Source : audit GTFS IDFM (cf. scripts/cache-gtfs/idfm-gtfs/) + croisement
 * avec les schémas RATP/SNCF officiels. Libellés alignés sur les noms GTFS
 * pour cohérence avec le reste du site.
 *
 * Note RER E : l'extension Eole (mai 2024) prolonge la ligne ouest jusqu'à
 * Nanterre-La-Folie. Le terminus historique Magenta-Saint-Lazare apparaît
 * encore résiduellement dans le GTFS (~5% des trips, sans doute service
 * partiel) mais n'est plus le terminus opérationnel principal. La phase 2
 * vers Mantes-la-Jolie est prévue pour 2027 — pas dans le GTFS courant.
 *
 * Note RER B : Massy-Palaiseau apparaît parfois comme terminus partiel
 * mais les terminus opérationnels officiels sont Robinson et
 * Saint-Rémy-lès-Chevreuse (sud).
 *
 * Note RER C : ligne très ramifiée (5+ branches). On regroupe les
 * directions en deux blocs principaux pour rester lisible.
 *
 * Format : pour chaque code RER (A/B/C/D/E), une liste de "directions"
 * géographiques (label + tableau de noms). Le format d'affichage
 * (compact / hiérarchique) est décidé côté composant selon le total.
 *
 * @return array<string, array{directions: array<int, array{label:string, terminus:array<int,string>}>}>
 * @package BougeaParis\Config
 */

return [
    'A' => [
        'directions' => [
            ['label' => 'ouest', 'terminus' => [
                'Saint-Germain-en-Laye',
                'Cergy le Haut',
                'Poissy',
            ]],
            ['label' => 'est', 'terminus' => [
                'Marne-la-Vallée Chessy',
                'Boissy-Saint-Léger',
            ]],
        ],
    ],
    'B' => [
        'directions' => [
            ['label' => 'nord', 'terminus' => [
                'Aéroport Charles de Gaulle 2 (Terminal 2)',
                'Mitry - Claye',
            ]],
            ['label' => 'sud', 'terminus' => [
                'Robinson',
                'Saint-Rémy-lès-Chevreuse',
            ]],
        ],
    ],
    'C' => [
        'directions' => [
            ['label' => 'nord/ouest', 'terminus' => [
                'Pontoise',
                'Versailles Château Rive Gauche',
                'Saint-Quentin en Yvelines - Montigny-le-Bretonneux',
            ]],
            ['label' => 'sud', 'terminus' => [
                'Massy - Palaiseau',
                'Saint-Martin d\'Étampes',
                'Dourdan',
            ]],
        ],
    ],
    'D' => [
        'directions' => [
            ['label' => 'nord', 'terminus' => [
                'Creil',
                'Orry-la-Ville - Coye',
            ]],
            ['label' => 'sud', 'terminus' => [
                'Melun',
                'Malesherbes',
                'Corbeil-Essonnes',
            ]],
        ],
    ],
    'E' => [
        'directions' => [
            ['label' => 'ouest', 'terminus' => [
                'Nanterre-La-Folie',
            ]],
            ['label' => 'est', 'terminus' => [
                'Chelles - Gournay',
                'Tournan',
                'Villiers-sur-Marne - Le Plessis-Trévise',
            ]],
        ],
    ],
];
