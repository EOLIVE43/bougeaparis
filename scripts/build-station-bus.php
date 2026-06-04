<?php
declare(strict_types=1);

error_reporting(E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED);
ini_set('memory_limit', '1024M');

/**
 * scripts/build-station-bus.php
 *
 * Genere/met a jour la cle "bus_correspondences" dans les JSON station
 * a partir des donnees GTFS IDFM locales (scripts/cache-gtfs/idfm-gtfs/).
 *
 * Pipeline :
 *   1. Charge JSON station, lit lat/lon
 *   2. Stream stops.txt et identifie les stops dans buffer 300m (haversine)
 *      avec marquage same_node (<= 50m) ou nearby_300m (50-300m)
 *   3. Stream stop_times.txt (962 MB) -> trip_ids desservant ces stops
 *   4. Stream trips.txt -> route_ids pour ces trips
 *   5. Charge routes.txt + agency.txt en memoire
 *   6. Classifie chaque route_id selon route_type :
 *      - 1 (metro), 2 (rail RER/Transilien), 0 (tram) -> SKIP
 *      - 3 (bus) -> sous-classifie :
 *        * route_short_name commence par 'N' -> nocturne[]
 *        * agency_id == "IDFM:Operator_100" (RATP) -> diurne[]
 *        * autres operateurs -> regional[]
 *   7. Dedup + sort + ecrit dans station.json avec metadata _audit
 *
 * Usage :
 *   php scripts/build-station-bus.php --slug=bir-hakeim --dry-run --verbose
 *   php scripts/build-station-bus.php --slug=bir-hakeim --force
 *   php scripts/build-station-bus.php --slug=bir-hakeim
 *
 * Backlog A du TEMPLATE_GUIDE (BLOQUANT batch T2), implementation 2026-06.
 *
 * @package BougeaParis\Scripts
 */

const ROOT          = __DIR__ . '/..';
const STATIONS_DIR  = ROOT . '/public_html/data/stations';
const GTFS_DIR      = __DIR__ . '/cache-gtfs/idfm-gtfs';

const BUFFER_RADIUS_M = 300;
const SAME_NODE_M     = 50;

const AGENCY_RATP     = 'IDFM:Operator_100'; // RATP "pur" intra-Paris

// CLI
$opts = parse_cli_args($argv);
$slug    = $opts['slug']    ?? null;
$dryRun  = (bool)($opts['dry-run'] ?? false);
$verbose = (bool)($opts['verbose'] ?? false);
$force   = (bool)($opts['force']   ?? false);

if (!$slug) {
    fwrite(STDERR, "Usage: php scripts/build-station-bus.php --slug=<slug> [--dry-run] [--verbose] [--force]\n");
    exit(1);
}

$startTime = microtime(true);

// ---------------------------------------------------------------------------
// 1. Charger JSON station
// ---------------------------------------------------------------------------
$jsonPath = STATIONS_DIR . "/$slug.json";
if (!file_exists($jsonPath)) {
    fwrite(STDERR, "ERREUR : station JSON not found at $jsonPath\n");
    exit(1);
}
$station = json_decode((string)file_get_contents($jsonPath), true);
if (!is_array($station)) {
    fwrite(STDERR, "ERREUR : JSON station invalide\n");
    exit(1);
}

$lat = (float)($station['latitude'] ?? 0);
$lon = (float)($station['longitude'] ?? 0);
if ($lat === 0.0 || $lon === 0.0) {
    fwrite(STDERR, "ERREUR : lat/lon manquants dans $slug.json\n");
    exit(1);
}

log_info("Station « {$station['name']} » ($lat, $lon)");

// Garde-fou --force (evite ecrasement accidentel)
$existingDiurne = $station['bus_correspondences']['diurne'] ?? [];
if (!$force && !$dryRun && is_array($existingDiurne) && count($existingDiurne) > 0) {
    log_info("bus_correspondences.diurne deja rempli (" . count($existingDiurne) . " entrees).");
    log_info("Utilise --force pour ecraser, ou --dry-run pour comparer.");
    exit(0);
}

// ---------------------------------------------------------------------------
// 2. Identifier stops candidats dans le buffer 300m
// ---------------------------------------------------------------------------
log_info("Lecture stops.txt + identification candidats <= " . BUFFER_RADIUS_M . "m...");
$candidates = []; // stop_id => [stop_id, name, distance_m, tier]
$stopsFh = fopen(GTFS_DIR . '/stops.txt', 'r');
if ($stopsFh === false) {
    fwrite(STDERR, "ERREUR : impossible d'ouvrir stops.txt\n");
    exit(1);
}
$header = fgetcsv($stopsFh);
$idIdx   = array_search('stop_id',   $header, true);
$lonIdx  = array_search('stop_lon',  $header, true);
$latIdx  = array_search('stop_lat',  $header, true);
$nameIdx = array_search('stop_name', $header, true);

while (($row = fgetcsv($stopsFh)) !== false) {
    if (!isset($row[$latIdx], $row[$lonIdx])) continue;
    $sLat = (float)$row[$latIdx];
    $sLon = (float)$row[$lonIdx];
    if ($sLat === 0.0 || $sLon === 0.0) continue;
    // Pre-filter rapide bounding box (~300m = ~0.003 deg) pour eviter haversine
    if (abs($sLat - $lat) > 0.005 || abs($sLon - $lon) > 0.005) continue;
    $dist = haversine($lat, $lon, $sLat, $sLon);
    if ($dist <= BUFFER_RADIUS_M) {
        $candidates[$row[$idIdx]] = [
            'stop_id'    => $row[$idIdx],
            'name'       => $row[$nameIdx],
            'distance_m' => (int)round($dist),
            'tier'       => $dist <= SAME_NODE_M ? 'same_node' : 'nearby_300m',
        ];
    }
}
fclose($stopsFh);
log_info("Stops candidats : " . count($candidates));
if ($verbose) {
    foreach ($candidates as $c) {
        log_info("  - {$c['stop_id']} ({$c['name']}) @ {$c['distance_m']}m [{$c['tier']}]");
    }
}

if (empty($candidates)) {
    fwrite(STDERR, "ERREUR : 0 stops candidats dans le buffer 300m.\n");
    exit(1);
}

// ---------------------------------------------------------------------------
// 3. Stream stop_times.txt -> trip_ids desservant ces stops
// ---------------------------------------------------------------------------
log_info("Stream stop_times.txt (~960 MB, attendre ~30-60s)...");
$tripIds = [];
$stopTimeFh = fopen(GTFS_DIR . '/stop_times.txt', 'r');
if ($stopTimeFh === false) {
    fwrite(STDERR, "ERREUR : impossible d'ouvrir stop_times.txt\n");
    exit(1);
}
$stHeader = fgetcsv($stopTimeFh);
$stStopIdx = array_search('stop_id', $stHeader, true);
$stTripIdx = array_search('trip_id', $stHeader, true);
$rowsScanned = 0;
while (($row = fgetcsv($stopTimeFh)) !== false) {
    $rowsScanned++;
    $sid = $row[$stStopIdx] ?? '';
    if (isset($candidates[$sid])) {
        $tripIds[$row[$stTripIdx]] = true;
    }
}
fclose($stopTimeFh);
log_info("stop_times.txt scanne ($rowsScanned lignes). Trips uniques : " . count($tripIds));

// ---------------------------------------------------------------------------
// 4. Stream trips.txt -> route_ids pour ces trips
// ---------------------------------------------------------------------------
log_info("Stream trips.txt...");
$routeIds = [];
$tripsFh = fopen(GTFS_DIR . '/trips.txt', 'r');
$tHeader = fgetcsv($tripsFh);
$tTripIdx  = array_search('trip_id',  $tHeader, true);
$tRouteIdx = array_search('route_id', $tHeader, true);
while (($row = fgetcsv($tripsFh)) !== false) {
    $tid = $row[$tTripIdx] ?? '';
    if (isset($tripIds[$tid])) {
        $routeIds[$row[$tRouteIdx]] = true;
    }
}
fclose($tripsFh);
log_info("Route_ids uniques : " . count($routeIds));

// ---------------------------------------------------------------------------
// 5. Charger routes.txt + agency.txt en memoire (petits fichiers)
// ---------------------------------------------------------------------------
log_info("Lecture routes.txt + agency.txt...");
$routes = [];
$routesFh = fopen(GTFS_DIR . '/routes.txt', 'r');
$rHeader = fgetcsv($routesFh);
$rIdIdx     = array_search('route_id',         $rHeader, true);
$rAgencyIdx = array_search('agency_id',        $rHeader, true);
$rNameIdx   = array_search('route_short_name', $rHeader, true);
$rTypeIdx   = array_search('route_type',       $rHeader, true);
while (($row = fgetcsv($routesFh)) !== false) {
    $rid = $row[$rIdIdx] ?? '';
    if (isset($routeIds[$rid])) {
        $routes[$rid] = [
            'route_id'         => $rid,
            'route_short_name' => $row[$rNameIdx],
            'agency_id'        => $row[$rAgencyIdx],
            'route_type'       => (int)$row[$rTypeIdx],
        ];
    }
}
fclose($routesFh);

$agencies = [];
$agencyFh = fopen(GTFS_DIR . '/agency.txt', 'r');
$aHeader = fgetcsv($agencyFh);
$aIdIdx   = array_search('agency_id',   $aHeader, true);
$aNameIdx = array_search('agency_name', $aHeader, true);
while (($row = fgetcsv($agencyFh)) !== false) {
    $agencies[$row[$aIdIdx]] = $row[$aNameIdx];
}
fclose($agencyFh);

// ---------------------------------------------------------------------------
// 6. Classifier
// ---------------------------------------------------------------------------
$diurne = [];
$nocturne = [];
$regional = [];
$mappingDebug = [];

foreach ($routes as $r) {
    $name       = (string)$r['route_short_name'];
    $agencyId   = (string)$r['agency_id'];
    $agencyName = $agencies[$agencyId] ?? '?';
    $type       = $r['route_type'];

    // Skip non-bus (metro 1, rail 2, tram 0, ferry 4, funiculaire 7, ...)
    if ($type !== 3) {
        $mappingDebug[] = "SKIP $name (route_type=$type, $agencyName)";
        continue;
    }

    // Noctilien = route_short_name commence par 'N' suivi d'un chiffre
    if (preg_match('/^N\d/', $name) === 1) {
        $nocturne[] = $name;
        $mappingDebug[] = "NOCT $name ($agencyName)";
        continue;
    }

    // RATP pur Paris intra-muros -> diurne
    if ($agencyId === AGENCY_RATP) {
        $diurne[] = $name;
        $mappingDebug[] = "DIURNE $name (RATP)";
    } else {
        $regional[] = $name;
        $mappingDebug[] = "REGIONAL $name ($agencyName)";
    }
}

// Dedup + sort naturel (pour que "22" < "100")
$diurne   = array_values(array_unique($diurne));
$nocturne = array_values(array_unique($nocturne));
$regional = array_values(array_unique($regional));
sort($diurne,   SORT_NATURAL);
sort($nocturne, SORT_NATURAL);
sort($regional, SORT_NATURAL);

if ($verbose) {
    log_info("Mapping detail :");
    foreach ($mappingDebug as $m) log_info("  $m");
}

// ---------------------------------------------------------------------------
// 7. Compose bus_correspondences
// ---------------------------------------------------------------------------
$sameNodeCount = count(array_filter($candidates, fn($c) => $c['tier'] === 'same_node'));
$nearbyCount   = count($candidates) - $sameNodeCount;

$busCorr = [
    'diurne'   => $diurne,
    'nocturne' => $nocturne,
    'regional' => $regional,
    '_audit'   => [
        'source'           => 'gtfs-idfm',
        'buffer_radius_m'  => BUFFER_RADIUS_M,
        'audit_date'       => date('Y-m-d'),
        'same_node_count'  => $sameNodeCount,
        'nearby_count'     => $nearbyCount,
    ],
];

$elapsed = round(microtime(true) - $startTime, 1);
log_info("=== RECAP ===");
log_info("Diurne   (RATP Operator_100) : " . count($diurne)   . " — " . implode(', ', $diurne));
log_info("Nocturne (N* RATP)           : " . count($nocturne) . " — " . implode(', ', $nocturne));
log_info("Regional (autres operateurs) : " . count($regional) . " — " . implode(', ', $regional));
log_info("Stops same_node / nearby     : $sameNodeCount / $nearbyCount");
log_info("Temps execution              : {$elapsed}s");

if ($dryRun) {
    log_info("DRY RUN — JSON station non modifie.");
    log_info("Output prevu pour bus_correspondences :");
    echo pretty_json($busCorr) . "\n";
    exit(0);
}

// ---------------------------------------------------------------------------
// 8. Ecrire dans JSON station (preserver l'ordre des cles existantes)
// ---------------------------------------------------------------------------
$station['bus_correspondences'] = $busCorr;
$written = file_put_contents($jsonPath, pretty_json($station) . "\n");
if ($written === false) {
    fwrite(STDERR, "ERREUR : impossible d'ecrire $jsonPath\n");
    exit(1);
}
log_info("JSON $slug.json mis a jour ({$written} octets).");
exit(0);

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

/**
 * Distance haversine en metres entre 2 paires lat/lon (WGS84).
 */
function haversine(float $lat1, float $lon1, float $lat2, float $lon2): float {
    $earthRadius = 6371000.0;
    $dLat = deg2rad($lat2 - $lat1);
    $dLon = deg2rad($lon2 - $lon1);
    $a = sin($dLat / 2) ** 2 +
         cos(deg2rad($lat1)) * cos(deg2rad($lat2)) *
         sin($dLon / 2) ** 2;
    $c = 2 * atan2(sqrt($a), sqrt(1 - $a));
    return $earthRadius * $c;
}
