<?php
/**
 * config/networks.php
 *
 * Mapping des labels techniques de l'API PRIM vers des labels editoriaux
 * utilisables dans les articles.
 *
 * Utilise par : DisruptionFilter.php, DisruptionFormatter.php, ClaudeClient.php
 *
 * Sources :
 * - Modes PRIM : Metro, RapidTransit, Tramway, LocalTrain, Bus
 * - Networks : cf analyse API PRIM du 24 avril 2026
 */

declare(strict_types=1);

return [

    /**
     * Mapping mode technique -> label editorial.
     * Utilise pour generer les articles et les affichages.
     */
    'modes' => [
        'Metro'         => 'Métro',
        'RapidTransit'  => 'RER',
        'Tramway'       => 'Tramway',
        'LocalTrain'    => 'Transilien',
        'Bus'           => 'Bus',
    ],

    /**
     * Modes inclus dans le scope editorial (Option B).
     * Toute ligne hors de ces modes est ignoree par defaut.
     */
    'scope_modes' => [
        'Metro',
        'RapidTransit',
        'Tramway',
        'LocalTrain',
    ],

    /**
     * Priorite d'affichage des modes (dans l'article).
     * Les modes en haut de liste sont presentes en premier.
     */
    'mode_priority' => [
        'Metro'        => 1,
        'RapidTransit' => 2,
        'Tramway'      => 3,
        'LocalTrain'   => 4,
        'Bus'          => 5,
    ],

    /**
     * Networks inclus dans le scope BUS (Option B).
     * Seuls les bus de ces reseaux sont pris en compte,
     * et SEULEMENT s'ils sont en severite BLOQUANTE.
     *
     * Note : Operator_100 = RATP Paris (130 lignes intra-muros + proche banlieue)
     */
    'scope_bus_networks' => [
        'network:IDFM:Operator_100', // RATP Paris
    ],

    /**
     * Mapping networkId -> nom lisible du reseau.
     * Pour affichage dans les articles et les widgets.
     */
    'network_names' => [
        'network:IDFM:Operator_100' => 'RATP Paris',
        // A completer au fil des decouvertes :
        // 'network:IDFM:1051' => '...',
        // 'network:IDFM:1070' => 'Pays Briard',
        // 'network:IDFM:1071' => '...',
    ],

    /**
     * Mapping severity -> poids numerique (plus haut = plus grave).
     * Utilise pour trier les perturbations.
     */
    'severity_weight' => [
        'BLOQUANTE'   => 100,
        'PERTURBEE'   => 50,
        'INFORMATION' => 10,
    ],

    /**
     * Mapping severity -> label editorial.
     */
    'severity_labels' => [
        'BLOQUANTE'   => 'Trafic interrompu',
        'PERTURBEE'   => 'Trafic perturbé',
        'INFORMATION' => 'Information',
    ],

    /**
     * Mapping cause -> label editorial.
     */
    'cause_labels' => [
        'TRAVAUX'       => 'Travaux',
        'PERTURBATION'  => 'Incident',
        'INFORMATION'   => 'Information',
    ],

    /**
     * Slug d'URL pour chaque ligne majeure.
     * Utilise pour les liens internes dans les articles vers les pages ligne.
     *
     * Format : "{mode}:{shortName}" => "slug-url"
     */
    'line_slugs' => [
        // Metro
        'Metro:1'   => 'metro/ligne-1',
        'Metro:2'   => 'metro/ligne-2',
        'Metro:3'   => 'metro/ligne-3',
        'Metro:3B'  => 'metro/ligne-3bis',
        'Metro:4'   => 'metro/ligne-4',
        'Metro:5'   => 'metro/ligne-5',
        'Metro:6'   => 'metro/ligne-6',
        'Metro:7'   => 'metro/ligne-7',
        'Metro:7B'  => 'metro/ligne-7bis',
        'Metro:8'   => 'metro/ligne-8',
        'Metro:9'   => 'metro/ligne-9',
        'Metro:10'  => 'metro/ligne-10',
        'Metro:11'  => 'metro/ligne-11',
        'Metro:12'  => 'metro/ligne-12',
        'Metro:13'  => 'metro/ligne-13',
        'Metro:14'  => 'metro/ligne-14',
        // RER
        'RapidTransit:A' => 'rer/ligne-a',
        'RapidTransit:B' => 'rer/ligne-b',
        'RapidTransit:C' => 'rer/ligne-c',
        'RapidTransit:D' => 'rer/ligne-d',
        'RapidTransit:E' => 'rer/ligne-e',
        // Tramway
        'Tramway:T1'  => 'tramway/ligne-t1',
        'Tramway:T2'  => 'tramway/ligne-t2',
        'Tramway:T3a' => 'tramway/ligne-t3a',
        'Tramway:T3b' => 'tramway/ligne-t3b',
        'Tramway:T4'  => 'tramway/ligne-t4',
        'Tramway:T5'  => 'tramway/ligne-t5',
        'Tramway:T6'  => 'tramway/ligne-t6',
        'Tramway:T7'  => 'tramway/ligne-t7',
        'Tramway:T8'  => 'tramway/ligne-t8',
        'Tramway:T9'  => 'tramway/ligne-t9',
        'Tramway:T11' => 'tramway/ligne-t11',
        'Tramway:T12' => 'tramway/ligne-t12',
        'Tramway:T13' => 'tramway/ligne-t13',
        // Transilien
        'LocalTrain:H' => 'transilien/ligne-h',
        'LocalTrain:J' => 'transilien/ligne-j',
        'LocalTrain:K' => 'transilien/ligne-k',
        'LocalTrain:L' => 'transilien/ligne-l',
        'LocalTrain:N' => 'transilien/ligne-n',
        'LocalTrain:P' => 'transilien/ligne-p',
        'LocalTrain:R' => 'transilien/ligne-r',
        'LocalTrain:U' => 'transilien/ligne-u',
    ],
];
