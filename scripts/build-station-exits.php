<?php
declare(strict_types=1);

error_reporting(E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED);
ini_set('memory_limit', '512M');

/**
 * scripts/build-station-exits.php
 *
 * Genere/met a jour la cle "exits" dans les JSON station a partir du GTFS IDFM.
 *
 * Source GTFS : scripts/cache-gtfs/idfm-gtfs/ (telecharge par build-line-jsons.php)
 *
 * Pour chaque public_html/data/stations/{slug}.json :
 *   1. Trouve le parent_station IDFM principal (matching nom + bbox sur lat/lon).
 *   2. Elargit aux parent_stations connectes via transfers.txt (transferts <= 300s)
 *      pour fusionner les sous-hubs (ex. Chatelet metro + Les Halles + Chatelet-LH RER).
 *   3. Collecte toutes les sorties (location_type=2) des parents retenus.
 *   4. Trie par stop_code numerique (ou alphanum pour "1A", "1B", ...).
 *   5. Met a jour la cle "exits" du JSON ; preserve le reste.
 *
 * Format de chaque sortie produite :
 *   { "number": "1", "name": "pl. du Châtelet", "latitude": 48.857, "longitude": 2.347, "accessible": null }
 *
 * "accessible" est toujours null car le GTFS IDFM ne renseigne pas l'accessibilite
 * PMR au niveau sortie. Override manuel possible plus tard (true/false).
 *
 * Usage :
 *   php scripts/build-station-exits.php --preview --station=chatelet
 *   php scripts/build-station-exits.php --station=chatelet
 *   php scripts/build-station-exits.php
 *
 * @package BougeaParis\Scripts
 */

const ROOT             = __DIR__ . '/..';
const GTFS_DIR         = __DIR__ . '/cache-gtfs/idfm-gtfs';
const STATIONS_DIR     = ROOT . '/public_html/data/stations';
const STATIONS_RER_DIR = ROOT . '/public_html/data/stations-rer';
const ADDR_CACHE_FILE = __DIR__ . '/cache-gtfs/addresses-cache.json';

// API adresse.data.gouv.fr (preconnectee dans templates/layout/base.php)
const ADDR_API_URL  = 'https://api-adresse.data.gouv.fr/reverse/';
// Fair-use : 50 req/sec officiels ; on se cale a 30 pour avoir du marge
const ADDR_API_SLEEP_US = 35_000; // 35ms entre 2 requetes
// Toutes les N requetes reseau, on flush le cache sur disque
const ADDR_CACHE_FLUSH_EVERY = 50;
// Format de la cle : 6 decimales (~10cm de precision)
const ADDR_CACHE_KEY_DECIMALS = 6;

// Filtre transferts : on accepte large (jusqu'a 10 min) pour ne pas couper les
// connexions inter-hub legitimes comme Chatelet <-> Chatelet-Les Halles (480s).
// La discrimination "meme hub" se fait ensuite par overlap des mots de nom
// (Chatelet partage "chatelet" avec Chatelet-Les Halles, Les Halles partage
// "halles" avec Chatelet-Les Halles, mais Hotel de Ville n'a aucun mot commun).
const MAX_TRANSFER_SECONDS = 600;

// Stop-words a exclure quand on extrait les mots significatifs d'un nom de station.
// On garde des mots specifiques (chatelet, halles, defense, lyon...) et on rejette
// les articles + connecteurs ainsi que les mots tres courts (< 3 lettres).
const NAME_STOP_WORDS = [
    'le','la','les','l','du','de','des','d','et','en','a','au','aux',
    'sur','sous','par','pour','avec','dans','vers',
    'rer','metro','tram','bus',
];

// Distance max (en metres) entre la station JSON (lat/lon) et un parent_station
// candidat pour valider le matching primaire. 250m couvre les decalages legers.
const MAX_PRIMARY_MATCH_M = 250;

// CLI
$opts = parse_cli_args($argv);
$onlyStation = $opts['station'] ?? null;
$mode        = isset($opts['mode']) && $opts['mode'] === 'rer' ? 'rer' : 'metro';
$STATIONS_DIR_RUNTIME = ($mode === 'rer') ? STATIONS_RER_DIR : STATIONS_DIR;
$preview     = (bool)($opts['preview'] ?? false);

// ============================================================================
// HELPERS
// ============================================================================

function parse_cli_args(array $argv): array {
    $out = [];
    foreach (array_slice($argv, 1) as $arg) {
        if (str_starts_with($arg, '--')) {
            $arg = substr($arg, 2);
            if (str_contains($arg, '=')) {
                [$k, $v] = explode('=', $arg, 2);
                $out[$k] = $v;
            } else {
                $out[$arg] = true;
            }
        }
    }
    return $out;
}

function log_info(string $msg): void {
    fwrite(STDOUT, '[' . date('H:i:s') . '] ' . $msg . "\n");
}

function pretty_json(array $data): string {
    return json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
}

/** Distance haversine en metres entre 2 points lat/lon. */
function haversine_m(float $lat1, float $lon1, float $lat2, float $lon2): float {
    $R = 6371000.0;
    $dLat = deg2rad($lat2 - $lat1);
    $dLon = deg2rad($lon2 - $lon1);
    $a = sin($dLat / 2) ** 2
       + cos(deg2rad($lat1)) * cos(deg2rad($lat2)) * sin($dLon / 2) ** 2;
    return $R * 2 * atan2(sqrt($a), sqrt(1 - $a));
}

/** Normalise une chaine pour comparaison nom : minuscules + sans diacritiques + sans tirets. */
function normalize_name(string $s): string {
    $s = mb_strtolower($s, 'UTF-8');
    $s = strtr($s, [
        'à'=>'a','á'=>'a','â'=>'a','ä'=>'a','ã'=>'a',
        'è'=>'e','é'=>'e','ê'=>'e','ë'=>'e',
        'ì'=>'i','í'=>'i','î'=>'i','ï'=>'i',
        'ò'=>'o','ó'=>'o','ô'=>'o','ö'=>'o','õ'=>'o',
        'ù'=>'u','ú'=>'u','û'=>'u','ü'=>'u',
        'ç'=>'c','ñ'=>'n','ÿ'=>'y',
        '–'=>'-','—'=>'-',
    ]);
    // Supprime tout caractere non alphanumerique (sauf espace) pour neutraliser ponctuation
    $s = preg_replace('/[^a-z0-9 ]/', ' ', $s);
    $s = preg_replace('/\s+/', ' ', trim($s));
    return $s;
}

/**
 * Charge le cache d'adresses depuis le disque (cle "lat,lon" -> infos adresse).
 * Retourne un tableau vide si le fichier n'existe pas ou est invalide.
 */
function load_address_cache(): array {
    if (!is_file(ADDR_CACHE_FILE)) return [];
    $raw = @file_get_contents(ADDR_CACHE_FILE);
    if ($raw === false) return [];
    $data = json_decode($raw, true);
    return is_array($data) ? $data : [];
}

/**
 * Ecrit le cache sur disque de maniere atomique (tmpfile + rename).
 * Evite la corruption en cas de crash pendant l'ecriture.
 */
function save_address_cache(array $cache): void {
    $tmp = ADDR_CACHE_FILE . '.tmp';
    $json = json_encode($cache, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT);
    if ($json === false) return;
    file_put_contents($tmp, $json);
    rename($tmp, ADDR_CACHE_FILE);
}

/** Cle de cache adresse a partir de lat/lon. */
function addr_cache_key(float $lat, float $lon): string {
    return sprintf('%.' . ADDR_CACHE_KEY_DECIMALS . 'f,%.' . ADDR_CACHE_KEY_DECIMALS . 'f', $lat, $lon);
}

/**
 * Appelle l'API api-adresse.data.gouv.fr en reverse geocoding.
 * Tente "type=housenumber" en priorite, puis "type=street" en fallback.
 *
 * Retourne ['label', 'postcode', 'city', 'housenumber', 'street'] ou null si rien trouve.
 */
function api_reverse_geocode(float $lat, float $lon): ?array {
    foreach (['housenumber', 'street'] as $type) {
        $url = ADDR_API_URL . '?lon=' . rawurlencode((string)$lon) . '&lat=' . rawurlencode((string)$lat) . '&type=' . $type;
        $ch = curl_init($url);
        curl_setopt_array($ch, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_TIMEOUT        => 10,
            CURLOPT_CONNECTTIMEOUT => 5,
            CURLOPT_USERAGENT      => 'BougeaParis-build-station-exits/1.0 (+https://bougeaparis.fr)',
            CURLOPT_HTTPHEADER     => ['Accept: application/json'],
        ]);
        $resp = curl_exec($ch);
        $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $err  = curl_error($ch);
        curl_close($ch);

        if ($resp === false || $code !== 200) {
            log_info(sprintf('  API reverse-geocode HTTP %d (%s) lat=%.6f lon=%.6f%s',
                $code, $type, $lat, $lon, $err ? " err=$err" : ''));
            continue;
        }

        $data = json_decode($resp, true);
        $features = $data['features'] ?? [];
        if (empty($features)) continue;

        $p = $features[0]['properties'] ?? [];
        if (empty($p['label'])) continue;

        return [
            'label'       => $p['label']       ?? null,
            'postcode'    => $p['postcode']    ?? null,
            'city'        => $p['city']        ?? null,
            'housenumber' => $p['housenumber'] ?? null,
            'street'      => $p['street']      ?? ($p['name'] ?? null),
        ];
    }
    return null;
}

/**
 * Reverse-geocode avec cache. Modifie $cache et $cacheDirty in-place.
 * Le caller est responsable de flush periodiquement le cache sur disque.
 */
function reverse_geocode(float $lat, float $lon, array &$cache, int &$apiCalls): ?array {
    $key = addr_cache_key($lat, $lon);
    if (isset($cache[$key])) return $cache[$key];

    // Sleep avant l'appel pour respecter le fair-use (sauf premiere requete)
    if ($apiCalls > 0) usleep(ADDR_API_SLEEP_US);
    $apiCalls++;

    $result = api_reverse_geocode($lat, $lon);
    if ($result === null) {
        // On cache aussi les "miss" pour ne pas re-interroger l'API en boucle
        $cache[$key] = ['label' => null, 'postcode' => null, 'city' => null,
                        'housenumber' => null, 'street' => null,
                        'fetched_at' => date('c'), 'miss' => true];
        return $cache[$key];
    }
    $result['fetched_at'] = date('c');
    $cache[$key] = $result;
    return $result;
}

/** Stream un fichier CSV GTFS. */
function stream_csv(string $path, callable $callback): int {
    $fp = fopen($path, 'r');
    if (!$fp) throw new RuntimeException("Impossible d'ouvrir $path");
    $header = fgetcsv($fp);
    if (!$header) { fclose($fp); return 0; }
    $count = 0;
    while (($row = fgetcsv($fp)) !== false) {
        if (count($row) < count($header)) {
            $row = array_pad($row, count($header), '');
        }
        $callback(array_combine($header, array_slice($row, 0, count($header))));
        $count++;
    }
    fclose($fp);
    return $count;
}

/** Resout un stop_id arbitraire vers son parent_station (location_type=1). */
function resolve_parent_station(string $stopId, array &$stops): string {
    $current = $stopId;
    $hops = 0;
    while (isset($stops[$current]['parent_station']) && $stops[$current]['parent_station'] !== null && $hops < 5) {
        $current = $stops[$current]['parent_station'];
        $hops++;
    }
    return $current;
}

/**
 * Tri intelligent par numero de sortie. Numerique d'abord (1, 2, 10, 11),
 * puis "1A" < "1B" < "1bis" < "10" (extraction prefixe numerique + suffixe).
 */
function sort_exits_by_number(array $exits): array {
    usort($exits, function ($a, $b) {
        $na = $a['number'] ?? '';
        $nb = $b['number'] ?? '';
        if ($na === '' && $nb === '') return strcmp($a['name'] ?? '', $b['name'] ?? '');
        if ($na === '') return 1;  // sans numero a la fin
        if ($nb === '') return -1;

        // Extraction prefixe numerique
        $intA = (int) preg_replace('/^(\d+).*/', '$1', $na);
        $intB = (int) preg_replace('/^(\d+).*/', '$1', $nb);
        if ($intA !== $intB) return $intA <=> $intB;
        // Meme prefixe : on trie par chaine complete (ex. "1A" < "1B" < "1bis")
        return strnatcasecmp($na, $nb);
    });
    return $exits;
}

// ============================================================================
// 1. CHARGEMENT GTFS
// ============================================================================

if (!is_dir(GTFS_DIR)) {
    fwrite(STDERR, "[ERREUR] Cache GTFS introuvable : " . GTFS_DIR . "\n");
    fwrite(STDERR, "Lance d'abord build-line-jsons.php (qui telecharge le GTFS).\n");
    exit(1);
}

log_info('Phase 1: chargement stops.txt + transfers.txt');

// stops : stop_id => ['name', 'parent_station', 'lat', 'lon', 'location_type', 'wheelchair_boarding', 'stop_code']
$stops = [];
stream_csv(GTFS_DIR . '/stops.txt', function (array $r) use (&$stops) {
    $stops[$r['stop_id']] = [
        'name'                => $r['stop_name'],
        'parent_station'      => $r['parent_station'] !== '' ? $r['parent_station'] : null,
        'lat'                 => $r['stop_lat'] !== '' ? (float)$r['stop_lat'] : null,
        'lon'                 => $r['stop_lon'] !== '' ? (float)$r['stop_lon'] : null,
        'location_type'       => $r['location_type'] !== '' ? (int)$r['location_type'] : 0,
        'wheelchair_boarding' => $r['wheelchair_boarding'] !== '' ? (int)$r['wheelchair_boarding'] : null,
        'stop_code'           => $r['stop_code'] ?? '',
    ];
});
log_info(sprintf('  %d stops charges', count($stops)));

// Index : nom normalise -> [parent_station_ids]
$nameToParents = []; // normalized_name => [parent_id, ...]
$parentCount = 0;
foreach ($stops as $sid => $info) {
    if ($info['location_type'] !== 1) continue;
    $parentCount++;
    $nameToParents[normalize_name($info['name'])][] = $sid;
}
log_info(sprintf('  %d parent_stations (location_type=1) indexes par nom', $parentCount));

// Index : parent_station -> [exits (loc_type=2 children)]
$parentToExits = [];
foreach ($stops as $sid => $info) {
    if ($info['location_type'] !== 2) continue;
    $parent = $info['parent_station'];
    if (!$parent) continue;
    $parentToExits[$parent][] = $sid;
}
log_info(sprintf('  %d parent_stations avec sorties (location_type=2)', count($parentToExits)));

// Graphe transferts (1 hop, filtre <= MAX_TRANSFER_SECONDS) sur les parent_stations.
// On stocke le min_transfer_time pour pouvoir l'afficher en preview.
$transferGraph = []; // pf => [pt => time_seconds]
$skippedLong = 0;
stream_csv(GTFS_DIR . '/transfers.txt', function (array $r) use (&$transferGraph, &$stops, &$skippedLong) {
    $from = $r['from_stop_id']; $to = $r['to_stop_id'];
    if (!isset($stops[$from]) || !isset($stops[$to])) return;
    $minT = isset($r['min_transfer_time']) && $r['min_transfer_time'] !== '' ? (int)$r['min_transfer_time'] : null;
    if ($minT !== null && $minT > MAX_TRANSFER_SECONDS) { $skippedLong++; return; }
    $pf = resolve_parent_station($from, $stops);
    $pt = resolve_parent_station($to, $stops);
    if ($pf === $pt) return;
    $cur = $transferGraph[$pf][$pt] ?? PHP_INT_MAX;
    if ($minT !== null && $minT < $cur) {
        $transferGraph[$pf][$pt] = $minT;
        $transferGraph[$pt][$pf] = $minT;
    } elseif (!isset($transferGraph[$pf][$pt])) {
        $transferGraph[$pf][$pt] = $minT;
        $transferGraph[$pt][$pf] = $minT;
    }
});
log_info(sprintf('  %d parent_stations dans le graphe de transferts (%d transferts longs filtres)',
    count($transferGraph), $skippedLong));

// ============================================================================
// 2. MATCHING STATION JSON -> PARENT_STATION IDFM
// ============================================================================

/**
 * Trouve le parent_station primaire pour un JSON station.
 * Strategie :
 *  1. Match exact sur le nom normalise -> filtre par bbox (haversine <= MAX_PRIMARY_MATCH_M)
 *  2. Si plusieurs candidats : prendre le plus proche
 *  3. Sinon : pas de match (retourne null)
 *
 * Retourne un tableau ['parent' => $pid, 'distance_m' => float, 'reason' => string]
 * ou null si aucun match satisfaisant.
 */
function match_primary_parent(array $stationJson, array &$nameToParents, array &$stops): ?array {
    $name = $stationJson['name'] ?? null;
    $lat  = $stationJson['latitude']  ?? null;
    $lon  = $stationJson['longitude'] ?? null;
    if (!$name) return null;

    $normalized = normalize_name($name);
    $candidates = $nameToParents[$normalized] ?? [];

    // Si pas de match exact, essayer aussi avec nom_full ou variantes (avec parens, tirets)
    if (empty($candidates) && !empty($stationJson['name_full'])) {
        // ex. "Châtelet — Métro & RER" -> normalisation tente "chatelet metro rer"
        // peu utile -> on ignore, on prend le name simple
    }

    if (empty($candidates)) return null;

    // Si on a lat/lon, on filtre par distance et on prend le plus proche
    if ($lat !== null && $lon !== null) {
        $best = null;
        foreach ($candidates as $pid) {
            $pinfo = $stops[$pid];
            if ($pinfo['lat'] === null || $pinfo['lon'] === null) continue;
            $d = haversine_m((float)$lat, (float)$lon, $pinfo['lat'], $pinfo['lon']);
            if ($d > MAX_PRIMARY_MATCH_M) continue;
            if ($best === null || $d < $best['distance_m']) {
                $best = ['parent' => $pid, 'distance_m' => $d, 'reason' => 'name+bbox'];
            }
        }
        if ($best !== null) return $best;
    }

    // Fallback : un seul candidat homonyme dans la zone -> on l'accepte
    if (count($candidates) === 1) {
        $pid = $candidates[0];
        $d = ($lat !== null && $lon !== null && $stops[$pid]['lat'] !== null)
            ? haversine_m((float)$lat, (float)$lon, $stops[$pid]['lat'], $stops[$pid]['lon'])
            : null;
        return ['parent' => $pid, 'distance_m' => $d, 'reason' => 'name-unique'];
    }

    return null;
}

/**
 * Extrait les mots significatifs d'un nom de station (filtres : stop-words, longueur >= 3).
 */
function name_words(string $name): array {
    $norm = normalize_name($name);
    $words = explode(' ', $norm);
    $stopSet = array_flip(NAME_STOP_WORDS);
    $out = [];
    foreach ($words as $w) {
        if (mb_strlen($w) < 3) continue;
        if (isset($stopSet[$w])) continue;
        $out[$w] = true;
    }
    return $out;
}

/**
 * Etend l'ensemble des parents a partir du primary via BFS dans $transferGraph.
 * Critere d'inclusion d'un voisin : son nom doit partager au moins un mot significatif
 * avec le pool des noms deja inclus. Cela evite les faux positifs (Hotel de Ville,
 * Pont Neuf...) tout en suivant les chaines hub (Chatelet -> Chatelet-LH -> Les Halles).
 *
 * Retourne ['parents' => [pid, ...], 'edges' => [[from, to, time], ...] (debug)].
 */
function expand_hub_via_name_overlap(string $primary, array $transferGraph, array &$stops): array {
    $primaryName = $stops[$primary]['name'] ?? '';
    $pool = name_words($primaryName); // set de mots
    $visited = [$primary => true];
    $edges = [];
    $queue = [$primary];

    while (!empty($queue)) {
        $node = array_shift($queue);
        foreach ($transferGraph[$node] ?? [] as $neighbor => $time) {
            if (isset($visited[$neighbor])) continue;
            $nName = $stops[$neighbor]['name'] ?? '';
            $nWords = name_words($nName);
            if (empty(array_intersect_key($nWords, $pool))) continue; // pas d'overlap
            $visited[$neighbor] = true;
            $pool = $pool + $nWords; // union (cles)
            $edges[] = [$node, $neighbor, $time];
            $queue[] = $neighbor;
        }
    }
    return ['parents' => array_keys($visited), 'edges' => $edges];
}

// ============================================================================
// 3. CONSTRUCTION DES EXITS PAR STATION
// ============================================================================

function build_exits(array $stationJson, array &$nameToParents, array &$stops, array &$transferGraph, array &$parentToExits, array &$addrCache, int &$apiCalls, callable $maybeFlush): array {
    $primary = match_primary_parent($stationJson, $nameToParents, $stops);
    $info = ['primary_match' => $primary, 'parents_used' => [], 'edges' => [], 'exits_count' => 0, 'exits' => []];
    if (!$primary) return $info;

    $expansion = expand_hub_via_name_overlap($primary['parent'], $transferGraph, $stops);
    $parents = $expansion['parents'];
    $info['parents_used'] = $parents;
    $info['edges'] = $expansion['edges'];

    $exits = [];
    foreach ($parents as $pid) {
        foreach ($parentToExits[$pid] ?? [] as $exitStopId) {
            $e = $stops[$exitStopId];
            // Skip si pas de coordonnees
            if ($e['lat'] === null || $e['lon'] === null) continue;
            // wheelchair_boarding pour sorties est globalement vide en IDFM ;
            // on garde null par defaut (override manuel possible).
            $accessible = match ($e['wheelchair_boarding'] ?? null) {
                1 => true,
                2 => false,
                default => null,
            };

            // Reverse geocoding (api-adresse.data.gouv.fr) avec cache disque
            $apiBefore = $apiCalls;
            $addr = reverse_geocode((float)$e['lat'], (float)$e['lon'], $addrCache, $apiCalls);
            if ($apiCalls !== $apiBefore) {
                $maybeFlush(); // appel reseau effectue : peut declencher un flush si seuil atteint
            }

            $exits[] = [
                'number'       => (string)($e['stop_code'] ?? ''),
                'name'         => $e['name'],
                'address_full' => $addr['label']    ?? null,
                'postcode'     => $addr['postcode'] ?? null,
                'city'         => $addr['city']     ?? null,
                'latitude'     => round($e['lat'], 6),
                'longitude'    => round($e['lon'], 6),
                'accessible'   => $accessible,
            ];
        }
    }
    $exits = sort_exits_by_number($exits);
    $info['exits'] = $exits;
    $info['exits_count'] = count($exits);
    return $info;
}

// ============================================================================
// 4. ITERATION SUR LES JSON STATION
// ============================================================================

// ============================================================================
// 1bis. CACHE D'ADRESSES (reverse geocoding api-adresse.data.gouv.fr)
// ============================================================================

log_info('Phase 1bis: cache adresses');
$addrCache = load_address_cache();
$apiCalls  = 0; // compteur cumulatif (reset si tu veux)
$pendingFlush = 0; // nb d'appels API depuis le dernier flush

$maybeFlush = function () use (&$addrCache, &$pendingFlush, &$apiCalls): void {
    $pendingFlush++;
    if ($pendingFlush >= ADDR_CACHE_FLUSH_EVERY) {
        save_address_cache($addrCache);
        log_info(sprintf('  cache adresses flushe (%d entrees, %d appels API total)',
            count($addrCache), $apiCalls));
        $pendingFlush = 0;
    }
};
log_info(sprintf('  %d adresses deja en cache (%s)', count($addrCache),
    is_file(ADDR_CACHE_FILE) ? 'fichier present' : 'cache vide / inexistant'));

// ============================================================================
// 2. ITERATION SUR LES JSON STATION
// ============================================================================

log_info('Phase 2: iteration ' . basename($STATIONS_DIR_RUNTIME) . '/*.json (mode=' . $mode . ')');

$files = glob($STATIONS_DIR_RUNTIME . '/*.json');
if ($onlyStation) {
    $files = array_filter($files, fn($f) => basename($f, '.json') === $onlyStation);
    if (empty($files)) {
        fwrite(STDERR, "[ERREUR] Aucun fichier $STATIONS_DIR_RUNTIME/$onlyStation.json\n");
        exit(1);
    }
}

if (empty($files)) {
    fwrite(STDERR, "[ERREUR] Aucun fichier dans " . $STATIONS_DIR_RUNTIME . "\n");
    exit(1);
}

$wroteCount = 0;
$skipCount  = 0;
foreach ($files as $path) {
    $slug = basename($path, '.json');
    $json = json_decode(file_get_contents($path), true);
    if (!is_array($json)) {
        log_info("  $slug : JSON invalide, skip");
        $skipCount++; continue;
    }

    $info = build_exits($json, $nameToParents, $stops, $transferGraph, $parentToExits, $addrCache, $apiCalls, $maybeFlush);

    if ($preview) {
        echo "\n";
        echo "############################################################\n";
        echo "# PREVIEW : $slug\n";
        echo "############################################################\n";
        if (!$info['primary_match']) {
            echo "  Aucun parent_station IDFM trouve (matching nom + bbox 250m).\n";
            echo "  Nom JSON : " . ($json['name'] ?? '?') . "\n";
            echo "  lat/lon JSON : " . ($json['latitude'] ?? '?') . " / " . ($json['longitude'] ?? '?') . "\n";
            continue;
        }
        $pm = $info['primary_match'];
        echo "  Parent primaire : {$pm['parent']} (" . ($stops[$pm['parent']]['name']) . ")\n";
        echo "  Distance JSON<->parent : " . ($pm['distance_m'] !== null ? round($pm['distance_m'], 1) . ' m' : 'n/a')
             . " (raison: {$pm['reason']})\n";
        echo "  Hub fusionne via BFS+name-overlap (" . count($info['parents_used']) . " parents) :\n";
        foreach ($info['parents_used'] as $p) {
            $kind = ($p === $pm['parent']) ? '(primaire)' : '(transitif)';
            echo "    - $p $kind : " . ($stops[$p]['name'] ?? '?') . "\n";
        }
        if (!empty($info['edges'])) {
            echo "  Edges BFS retenus :\n";
            foreach ($info['edges'] as [$f, $t, $time]) {
                $fn = $stops[$f]['name'] ?? '?';
                $tn = $stops[$t]['name'] ?? '?';
                echo "    $fn -> $tn (transfer={$time}s)\n";
            }
        }
        echo "  Sorties calculees : {$info['exits_count']}\n";
        if ($info['exits_count'] > 0) {
            $existing = $json['exits'] ?? null;
            echo "  Existant dans JSON : " . (is_array($existing) ? count($existing) . ' sortie(s)' : '(aucune cle exits)') . "\n";
            echo "  --- Liste calculee ---\n";
            foreach ($info['exits'] as $e) {
                $addr = $e['address_full'] ?? '(pas d\'adresse)';
                printf("    %-5s %-32s | %-50s acc=%s\n",
                    $e['number'] ?: '-',
                    mb_strimwidth($e['name'], 0, 30, '...'),
                    mb_strimwidth($addr, 0, 48, '...'),
                    var_export($e['accessible'], true));
            }
        }
        continue;
    }

    // Mode ecriture : merge non-destructif
    if ($info['exits_count'] === 0) {
        log_info("  $slug : 0 sortie trouvee (parent introuvable ou sans sorties), skip");
        $skipCount++; continue;
    }

    // Si exits existant, preserver les valeurs editoriales saisies manuellement :
    //  - "accessible" (true/false) : override PMR par sortie
    //  - "sector"                  : regroupement editorial (forum, rivoli, seine...)
    // Tout le reste (name, address_full, postcode, city, lat, lon) est rafraichi
    // depuis le GTFS + reverse geocoding.
    $existing = $json['exits'] ?? [];
    if (is_array($existing) && !empty($existing)) {
        $byNumber = [];
        foreach ($existing as $e) {
            if (isset($e['number'])) $byNumber[(string)$e['number']] = $e;
        }
        foreach ($info['exits'] as &$newExit) {
            $key = (string)($newExit['number'] ?? '');
            if ($key !== '' && isset($byNumber[$key])) {
                $oldAcc = $byNumber[$key]['accessible'] ?? null;
                if ($oldAcc !== null) $newExit['accessible'] = $oldAcc;
                $oldSector = $byNumber[$key]['sector'] ?? null;
                if ($oldSector !== null && $oldSector !== '') $newExit['sector'] = $oldSector;
            }
        }
        unset($newExit);
    }

    $json['exits'] = $info['exits'];
    file_put_contents($path, pretty_json($json) . "\n");
    log_info("  $slug : " . count($info['exits']) . " sorties ecrites (parents: " . count($info['parents_used']) . ")");
    $wroteCount++;
}

// Flush final du cache adresses (en plus des flushes incrementaux)
save_address_cache($addrCache);
log_info(sprintf('Cache adresses sauvegarde : %d entrees totales, %d appels API effectues cette run',
    count($addrCache), $apiCalls));

if ($preview) {
    log_info("Preview terminee. Aucun fichier ecrit.");
} else {
    log_info("Termine : $wroteCount fichier(s) ecrit(s), $skipCount skip(s).");
}
