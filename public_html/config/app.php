<?php
/**
 * Configuration applicative
 *
 * Parametres techniques : cache, API, chemins internes.
 * La cle API PRIM est chargee depuis un fichier secrets.php
 * (non versionne sur Git, present uniquement sur le serveur).
 */

// Chargement des secrets depuis un fichier externe non versionne
$secretsFile = __DIR__ . '/secrets.php';
$secrets = file_exists($secretsFile) ? require $secretsFile : [];

return [
    // Cles API
    'prim_api_key'    => $secrets['prim_api_key'] ?? '',
    'navitia_api_key' => $secrets['navitia_api_key'] ?? '',

    // Endpoints API
    'prim_base_url'    => 'https://prim.iledefrance-mobilites.fr/marketplace',
    'navitia_base_url' => 'https://api.navitia.io/v1',
    'adresse_api_url'  => 'https://api-adresse.data.gouv.fr/search/',

    // Cache (en secondes)
    'cache_static'      => 30 * 24 * 3600, // 30 jours : stations, lignes, referentiels
    'cache_schedules'   => 3600,           // 1h : horaires theoriques
    'cache_realtime'    => 30,             // 30s : prochains passages
    'cache_disruptions' => 300,            // 5min : incidents et travaux
    'cache_itinerary'   => 3600,           // 1h : resultats d'itineraires (memoires par couple A-B)

    // Dossier cache (chmod 755 requis sur le serveur)
    'cache_dir'         => __DIR__ . '/../api/cache',

    // User-Agent pour les appels API
    'user_agent'        => 'BougeaParis/1.0 (+https://bougeaparis.fr)',

    // Timeout des requetes externes (secondes)
    'api_timeout'       => 10,
];
