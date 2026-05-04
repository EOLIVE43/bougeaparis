<?php
declare(strict_types=1);

error_reporting(E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED);
ini_set('memory_limit', '2G'); // stream stop_times.txt (~917 MB) + index trips metro

/**
 * scripts/build-line-jsons.php
 *
 * Generateur des JSON factuels pour les 16 lignes du metro parisien
 * a partir du GTFS officiel d'Ile-de-France Mobilites.
 *
 * Source GTFS : https://eu.ftp.opendatasoft.com/stif/GTFS/IDFM-gtfs.zip
 * Cache local : scripts/cache-gtfs/idfm-gtfs/
 *
 * Donnees factuelles produites :
 *   - identite ligne : id, mode, code, name, color, color_text, terminus_a/b
 *   - stations_count, length_km (haversine via shapes.txt), duration_minutes
 *   - schedule { first_departure, last_departure, frequency }
 *   - stations[] avec correspondences (M/RER/T/TRANS) + accessible PMR
 *
 * Pour metro-1 (existant) : ecrase UNIQUEMENT les cles factuelles,
 *                           preserve le contenu editorial deja saisi.
 * Pour les 15 autres lignes : ecrit un JSON minimal contenant uniquement
 *                             les cles factuelles ci-dessus. Aucun placeholder
 *                             ni TODO. Le contenu editorial sera ajoute
 *                             plus tard par d'autres scripts.
 *
 * Usage :
 *   php scripts/build-line-jsons.php --preview --line=1   # preview diff metro-1
 *   php scripts/build-line-jsons.php --line=1             # ecrit metro-1
 *   php scripts/build-line-jsons.php                      # ecrit les 16 lignes
 *
 * @package BougeaParis\Scripts
 */

// ============================================================================
// 0. CONSTANTES, CLI, CONFIG
// ============================================================================

const ROOT          = __DIR__ . '/..';
const GTFS_DIR      = __DIR__ . '/cache-gtfs/idfm-gtfs';
const LINES_DIR     = ROOT . '/public_html/data/lines';
const LINES_SUMMARY = ROOT . '/public_html/data/lines.json';
const LINE_MAPPING  = ROOT . '/public_html/config/line-mapping.php';

// Dates representatives (semaine de validite GTFS 2026-04-27 -> 2026-05-29).
// On evite jeudi 14 mai (Ascension) et vendredi 8 mai (Victoire 1945).
const REP_DATE_WEEKDAY  = '20260512'; // mardi
const REP_DATE_FRIDAY   = '20260515'; // vendredi (service prolonge)
const REP_DATE_SATURDAY = '20260516';
const REP_DATE_SUNDAY   = '20260517';

// Plages horaires pour le calcul des frequences (en secondes depuis minuit).
// On utilise le sequence=0 (depart de chaque trip a son terminus de depart),
// direction_id=0, et on prend la mediane des intervalles consecutifs.
const PEAK_WINDOW     = [8 * 3600,  9 * 3600];
const OFF_PEAK_WINDOW = [10 * 3600, 16 * 3600];
const EVENING_WINDOW  = [22 * 3600, 26 * 3600]; // GTFS extended-time (>24h ok)

// Override des couleurs pour tram/transilien (lines.json a des erreurs upstream :
// p.ex. T2 a #A0006E qui est en realite la couleur metro 4, TRANS U a #E2231A qui
// est la couleur RER A). Sources : RATP / SNCF Transilien officiels + metro-1.json
// existant (qui contient les bonnes valeurs pour les correspondances visibles).
const COLOR_OVERRIDES = [
    'tramway' => [
        'T1'  => ['color' => '#0055C8', 'text' => '#FFFFFF'],
        'T2'  => ['color' => '#cead2c', 'text' => '#000000'],
        'T3a' => ['color' => '#FF7E2E', 'text' => '#FFFFFF'],
        'T3b' => ['color' => '#86BE13', 'text' => '#FFFFFF'],
        'T4'  => ['color' => '#B89D58', 'text' => '#FFFFFF'],
        'T5'  => ['color' => '#5E2D8E', 'text' => '#FFFFFF'],
        'T6'  => ['color' => '#E5007D', 'text' => '#FFFFFF'],
        'T7'  => ['color' => '#F28E42', 'text' => '#FFFFFF'],
        'T8'  => ['color' => '#5291CE', 'text' => '#FFFFFF'],
        'T9'  => ['color' => '#C04191', 'text' => '#FFFFFF'],
        'T10' => ['color' => '#8D5E2A', 'text' => '#FFFFFF'],
        'T11' => ['color' => '#0064B0', 'text' => '#FFFFFF'],
        'T12' => ['color' => '#00814F', 'text' => '#FFFFFF'],
        'T13' => ['color' => '#98D4E2', 'text' => '#000000'],
    ],
    'transilien' => [
        'H' => ['color' => '#98D4E2', 'text' => '#000000'],
        'J' => ['color' => '#D5C900', 'text' => '#000000'],
        'K' => ['color' => '#8D5E2A', 'text' => '#FFFFFF'],
        'L' => ['color' => '#7A99C9', 'text' => '#FFFFFF'], // existant metro-1.json
        'N' => ['color' => '#00814F', 'text' => '#FFFFFF'],
        'P' => ['color' => '#F3A4BA', 'text' => '#000000'],
        'R' => ['color' => '#F28E42', 'text' => '#FFFFFF'],
        'U' => ['color' => '#D41367', 'text' => '#FFFFFF'], // existant metro-1.json
    ],
];

// Filtrer les transferts a longues distances (faux positifs : ex. Argentine -> Etoile
// est marque comme un "transfert" alors que c'est un trajet pieton de 600+ s).
const MAX_TRANSFER_SECONDS = 300; // 5 min

// CLI arguments.
$opts = parse_cli_args($argv);
$onlyLines  = $opts['lines'] ?? null;       // ex. ['1', '3B'] ou null pour toutes
$preview    = (bool)($opts['preview'] ?? false);
$verbose    = (bool)($opts['verbose'] ?? true);

if ($preview && empty($onlyLines)) {
    fwrite(STDERR, "[ERREUR] --preview requiert --line=N\n");
    exit(1);
}

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
                if ($k === 'line')   $out['lines']   = [strtoupper($v)];
                elseif ($k === 'lines') $out['lines'] = array_map('strtoupper', explode(',', $v));
                else                 $out[$k]        = $v;
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

function fmt_bytes(int $b): string {
    foreach (['B', 'KB', 'MB', 'GB'] as $u) {
        if ($b < 1024) return number_format($b, 1) . $u;
        $b = (int)($b / 1024);
    }
    return $b . 'TB';
}

/** Convertit "HH:MM:SS" GTFS (24h+ possible) -> secondes depuis minuit. */
function gtfs_time_to_seconds(string $t): ?int {
    if (!preg_match('/^(\d{1,3}):(\d{2}):(\d{2})$/', $t, $m)) return null;
    return (int)$m[1] * 3600 + (int)$m[2] * 60 + (int)$m[3];
}

/** Formate des secondes en "5h30" (modulo 24h, accepte 25h15 -> "1h15"). */
function fmt_clock(int $secs): string {
    $h = intdiv($secs, 3600) % 24;
    $m = intdiv($secs % 3600, 60);
    return $h . 'h' . str_pad((string)$m, 2, '0', STR_PAD_LEFT);
}

/** Formate un intervalle (secondes) en chaine lisible "85 secondes" / "3 minutes". */
function fmt_interval(?float $secs): ?string {
    if ($secs === null || $secs <= 0) return null;
    $secs = (int) round($secs);
    if ($secs < 120) return $secs . ' secondes';
    return (int) round($secs / 60) . ' minutes';
}

/** Distance haversine en km entre 2 points lat/lon. */
function haversine_km(float $lat1, float $lon1, float $lat2, float $lon2): float {
    $R = 6371.0; // rayon Terre km
    $dLat = deg2rad($lat2 - $lat1);
    $dLon = deg2rad($lon2 - $lon1);
    $a = sin($dLat / 2) ** 2
       + cos(deg2rad($lat1)) * cos(deg2rad($lat2)) * sin($dLon / 2) ** 2;
    return $R * 2 * atan2(sqrt($a), sqrt(1 - $a));
}

/** Stream un .txt GTFS (CSV) ; appelle $callback($row_assoc) pour chaque ligne. */
function stream_csv(string $path, callable $callback, int $progressEvery = 1_000_000): int {
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
        if ($progressEvery > 0 && $count % $progressEvery === 0) {
            log_info(sprintf('  ... %s lignes traitees (%s)', number_format($count), basename($path)));
        }
    }
    fclose($fp);
    return $count;
}

// ============================================================================
// 1. PRE-CHARGEMENT DES CONFIGS
// ============================================================================

log_info('Pre-chargement des configs et lines.json...');

if (!is_dir(GTFS_DIR)) {
    fwrite(STDERR, "[ERREUR] Cache GTFS introuvable : " . GTFS_DIR . "\n");
    fwrite(STDERR, "Lance d'abord le telechargement (curl + unzip).\n");
    exit(1);
}

$lineMapping = require LINE_MAPPING; // ['metro' => ['C01371'=>'metro-1', ...], 'rer'=>..., ...]
$linesSummary = json_decode(file_get_contents(LINES_SUMMARY), true);

// route_id GTFS -> info correspondance (mode, code, color, slug)
// Mode : M / RER / T / TRANS
$routeIdToInfo = []; // 'IDFM:C01371' => ['mode'=>'M', 'code'=>'1', 'color'=>'#FFCE00', 'slug'=>'metro-1']

foreach ($lineMapping as $modeKey => $entries) {
    $modeLetter = match ($modeKey) {
        'metro'      => 'M',
        'rer'        => 'RER',
        'tramway'    => 'T',
        'transilien' => 'TRANS',
        default      => null,
    };
    if (!$modeLetter) continue;

    $summarySection = $linesSummary[$modeKey === 'tramway' ? 'tramway' : $modeKey] ?? [];

    foreach ($entries as $idfmShort => $fileSlug) {
        $routeId = 'IDFM:' . $idfmShort;
        $code    = null;
        $color   = null;

        // Recuperer code + color depuis lines.json en croisant le slug
        // file slug "metro-1" -> on cherche label "1" dans summary metro
        // file slug "rer-a"   -> label "A" dans summary rer
        // file slug "tram-2"  -> label "2" dans summary tramway (si "2" stocke; sinon "T2")
        // file slug "transilien-l" -> label "L" dans summary transilien
        $codeFromSlug = preg_replace('/^(metro|rer|tram|transilien)-/i', '', $fileSlug);

        foreach ($summarySection as $row) {
            if (strcasecmp((string)$row['label'], $codeFromSlug) === 0
             || strcasecmp((string)$row['label'], 'T' . $codeFromSlug) === 0
             || strcasecmp((string)($row['short'] ?? ''), $codeFromSlug) === 0) {
                $code  = (string)$row['label'];
                $color = (string)$row['color'];
                break;
            }
        }

        // Fallback : reconstituer depuis le slug
        if ($code === null) $code = strtoupper($codeFromSlug);

        // Couleur : appliquer override si dispo (lines.json contient des erreurs
        // upstream pour tram/transilien ; metro-1.json a les bonnes valeurs RATP/SNCF)
        if (isset(COLOR_OVERRIDES[$modeKey][$code]['color'])) {
            $color = COLOR_OVERRIDES[$modeKey][$code]['color'];
        }

        // Convention metro-1.json : pour le mode T (tram), le champ "line" est sans
        // prefixe T (ex : "2", "3a", "13"). On strippe pour les correspondances.
        $displayCode = $code;
        if ($modeLetter === 'T' && strlen($code) > 1 && (str_starts_with($code, 'T') || str_starts_with($code, 't'))) {
            $displayCode = substr($code, 1);
        }

        $routeIdToInfo[$routeId] = [
            'mode'  => $modeLetter,
            'code'  => $displayCode,
            'color' => $color,
            'slug'  => $fileSlug,
        ];
    }
}

// metro_route_id => file_slug, et l'inverse
$metroRouteIds = [];
foreach ($lineMapping['metro'] as $idfmShort => $fileSlug) {
    $metroRouteIds['IDFM:' . $idfmShort] = $fileSlug;
}

// metro short_name (ex "1", "3B") -> route_id
$metroCodeToRouteId = [];
$metroFileSlugToCode = []; // "metro-1" => "1", "metro-3bis" => "3B"

// ============================================================================
// 2. ROUTES.TXT
// ============================================================================

log_info('Phase 2: routes.txt');

$gtfsRoutes = []; // route_id => ['short_name', 'color', 'route_type', 'agency_id']

stream_csv(GTFS_DIR . '/routes.txt', function (array $r) use (&$gtfsRoutes, &$metroCodeToRouteId, &$metroFileSlugToCode, $metroRouteIds) {
    $rid = $r['route_id'];
    $gtfsRoutes[$rid] = [
        'short_name' => $r['route_short_name'],
        'color'      => $r['route_color'],
        'route_type' => (int)$r['route_type'],
        'agency_id'  => $r['agency_id'],
    ];
    if (isset($metroRouteIds[$rid])) {
        $code = $r['route_short_name']; // "1", "3B", etc.
        $metroCodeToRouteId[$code] = $rid;
        $metroFileSlugToCode[$metroRouteIds[$rid]] = $code;
    }
}, 0);

log_info(sprintf('  routes.txt: %d entrees, %d metros mappees', count($gtfsRoutes), count($metroCodeToRouteId)));
unset($gtfsRoutes); // plus utilise par la suite

// Si --line=N, on filtre la liste des metros a traiter
if ($onlyLines !== null) {
    $allowed = array_flip($onlyLines);
    $metroRouteIdsFiltered = [];
    foreach ($metroCodeToRouteId as $code => $rid) {
        if (isset($allowed[strtoupper((string)$code)])) {
            $metroRouteIdsFiltered[$rid] = $metroRouteIds[$rid];
        }
    }
    if (empty($metroRouteIdsFiltered)) {
        fwrite(STDERR, "[ERREUR] Aucune ligne metro ne correspond a --line=" . implode(',', $onlyLines) . "\n");
        fwrite(STDERR, "  Codes valides : " . implode(', ', array_keys($metroCodeToRouteId)) . "\n");
        exit(1);
    }
    $metroRouteIdsToProcess = $metroRouteIdsFiltered;
} else {
    $metroRouteIdsToProcess = $metroRouteIds;
}

log_info(sprintf('  -> %d ligne(s) metro a traiter : %s',
    count($metroRouteIdsToProcess),
    implode(', ', array_map(fn($rid) => (string)($metroFileSlugToCode[$metroRouteIds[$rid]] ?? '?'), array_keys($metroRouteIdsToProcess)))
));

// Tous les routes interessantes (metro + rer + tram + transilien) pour les correspondances
$interestingRouteIds = array_keys($routeIdToInfo);
$interestingRouteSet = array_flip($interestingRouteIds);

// ============================================================================
// 3. CALENDAR.TXT + CALENDAR_DATES.TXT
// ============================================================================

log_info('Phase 3: calendar.txt + calendar_dates.txt');

$repDates = [
    'weekday'  => REP_DATE_WEEKDAY,
    'friday'   => REP_DATE_FRIDAY,
    'saturday' => REP_DATE_SATURDAY,
    'sunday'   => REP_DATE_SUNDAY,
];
$repDow = [ // jour de semaine 0=lun .. 6=dim, mappe sur les colonnes calendar.txt
    'weekday'  => 'tuesday',   // 12 mai 2026 = mardi
    'friday'   => 'friday',
    'saturday' => 'saturday',
    'sunday'   => 'sunday',
];

// service_id => set de dates ('weekday','friday','saturday','sunday') ou il est actif
$serviceActive = [];

stream_csv(GTFS_DIR . '/calendar.txt', function (array $r) use (&$serviceActive, $repDates, $repDow) {
    $sid   = $r['service_id'];
    $start = $r['start_date'];
    $end   = $r['end_date'];
    foreach ($repDates as $key => $date) {
        if ($date < $start || $date > $end) continue;
        if ((int)$r[$repDow[$key]] === 1) {
            $serviceActive[$sid][$key] = true;
        }
    }
}, 0);

// Exceptions : type=1 ajoute, type=2 retire
stream_csv(GTFS_DIR . '/calendar_dates.txt', function (array $r) use (&$serviceActive, $repDates) {
    $sid  = $r['service_id'];
    $date = $r['date'];
    $type = (int)$r['exception_type'];
    foreach ($repDates as $key => $repDate) {
        if ($date !== $repDate) continue;
        if ($type === 1) {
            $serviceActive[$sid][$key] = true;
        } elseif ($type === 2) {
            unset($serviceActive[$sid][$key]);
        }
    }
}, 0);

log_info(sprintf('  %d service_ids actifs sur au moins un jour-type', count($serviceActive)));

// ============================================================================
// 4. STOPS.TXT
// ============================================================================

log_info('Phase 4: stops.txt');

$stops = []; // stop_id => ['name', 'parent_station', 'wheelchair_boarding', 'lat', 'lon', 'location_type']
stream_csv(GTFS_DIR . '/stops.txt', function (array $r) use (&$stops) {
    $stops[$r['stop_id']] = [
        'name'                => $r['stop_name'],
        'parent_station'      => $r['parent_station'] ?: null,
        'wheelchair_boarding' => $r['wheelchair_boarding'] !== '' ? (int)$r['wheelchair_boarding'] : null,
        'lat'                 => $r['stop_lat'] !== '' ? (float)$r['stop_lat'] : null,
        'lon'                 => $r['stop_lon'] !== '' ? (float)$r['stop_lon'] : null,
        'location_type'       => $r['location_type'] !== '' ? (int)$r['location_type'] : 0,
    ];
}, 0);
log_info(sprintf('  %d stops charges', count($stops)));

/**
 * Resout un stop_id arbitraire vers son parent_station (location_type=1).
 * Remonte la hierarchie tant que parent_station est defini.
 */
function resolve_parent_station(string $stopId, array &$stops): string {
    $current = $stopId;
    $hops = 0;
    while (isset($stops[$current]['parent_station']) && $stops[$current]['parent_station'] !== null && $hops < 5) {
        $current = $stops[$current]['parent_station'];
        $hops++;
    }
    return $current;
}

// ============================================================================
// 5. TRANSFERS.TXT
// ============================================================================

log_info('Phase 5: transfers.txt');

// Graphe de correspondance physique (1 hop) : parent_station => set(parent_stations)
// Filtre : on ne garde que les transferts <= MAX_TRANSFER_SECONDS pour eviter les
// faux positifs (ex. Argentine -> Etoile a 600+ s, qui n'est pas une correspondance).
$transferGraph = [];
$skippedLongTransfers = 0;
stream_csv(GTFS_DIR . '/transfers.txt', function (array $r) use (&$transferGraph, &$stops, &$skippedLongTransfers) {
    $from = $r['from_stop_id'];
    $to   = $r['to_stop_id'];
    if (!isset($stops[$from]) || !isset($stops[$to])) return;
    $minT = isset($r['min_transfer_time']) && $r['min_transfer_time'] !== ''
        ? (int)$r['min_transfer_time']
        : null;
    if ($minT !== null && $minT > MAX_TRANSFER_SECONDS) {
        $skippedLongTransfers++;
        return;
    }
    $pf = resolve_parent_station($from, $stops);
    $pt = resolve_parent_station($to, $stops);
    if ($pf === $pt) return;
    $transferGraph[$pf][$pt] = true;
    $transferGraph[$pt][$pf] = true;
}, 0);
log_info(sprintf('  %d parent_stations avec correspondances physiques (%d transferts longs filtres)',
    count($transferGraph), $skippedLongTransfers));

// ============================================================================
// 6. TRIPS.TXT
// ============================================================================

log_info('Phase 6: trips.txt (filtrage routes interessantes)');

// trip_id => ['route_id','service_id','direction_id','headsign','shape_id']
$trips = [];
stream_csv(GTFS_DIR . '/trips.txt', function (array $r) use (&$trips, $interestingRouteSet) {
    if (!isset($interestingRouteSet[$r['route_id']])) return;
    $trips[$r['trip_id']] = [
        'route_id'     => $r['route_id'],
        'service_id'   => $r['service_id'],
        'direction_id' => (int)$r['direction_id'],
        'headsign'     => $r['trip_headsign'],
        'shape_id'     => $r['shape_id'] ?: null,
    ];
}, 200_000);
log_info(sprintf('  %d trips conserves (metro/rer/tram/transilien)', count($trips)));

// ============================================================================
// 7. STOP_TIMES.TXT (le gros morceau, ~962 MB)
// ============================================================================

log_info('Phase 7: stop_times.txt (single pass, ~5 min sur disque normal)');

// Pour chaque metro route, on garde :
//   - departures[date_key][direction_id] = [departure_time_secs, ...]  (sequence=0)
//   - lastDeparture[date_key]            = max(arrival_time_secs)      (toutes seqs)
//   - tripStops[trip_id]                 = [parent_station, ...]       (en sequence)
//   - tripDuration[trip_id]              = (last_arrival - first_departure)
$metroData = []; // route_id => [...]

// Pour les correspondances : route_id => set(parent_station)
$routeServesStation = []; // route_id => [parent_station => true]

// Accessibilite (3 etats) :
//   true  : au moins un platform-stop metro a wheelchair_boarding=1
//   false : tous les platform-stops sont a wheelchair_boarding=2 (ou aucun wb=1, et au moins un wb=2)
//   null  : aucune info (wb=0 ou vide)
// Le wheelchair_boarding est rempli au niveau platform-stop, pas au parent_station.
$stationAccessibleVotes = []; // parent_station => ['has1' => bool, 'has2' => bool]

// Index inverse : trip_id appartenant au metro -> route_id (pour shapes plus tard)
$metroTripToRoute = [];
foreach ($trips as $tid => $info) {
    if (isset($metroRouteIds[$info['route_id']])) {
        $metroTripToRoute[$tid] = $info['route_id'];
    }
}
log_info(sprintf('  trips metro: %d (sur %d trips interessants)', count($metroTripToRoute), count($trips)));

$stopTimesFile = GTFS_DIR . '/stop_times.txt';
$fileSize = filesize($stopTimesFile);
log_info('  taille: ' . fmt_bytes($fileSize));

$fp = fopen($stopTimesFile, 'r');
$header = fgetcsv($fp);
$colMap = array_flip($header);
$idxTrip = $colMap['trip_id'];
$idxArr  = $colMap['arrival_time'];
$idxDep  = $colMap['departure_time'];
$idxStop = $colMap['stop_id'];
$idxSeq  = $colMap['stop_sequence'];

$count = 0;
$matched = 0;
$metroMatched = 0;
$start = microtime(true);

while (($row = fgetcsv($fp)) !== false) {
    $count++;
    if (($count % 2_000_000) === 0) {
        $pct = ftell($fp) / max(1, $fileSize) * 100;
        log_info(sprintf('  ... %s lignes (%.1f%%, %s metro matched)', number_format($count), $pct, number_format($metroMatched)));
    }

    $tid = $row[$idxTrip];
    if (!isset($trips[$tid])) continue;
    $matched++;

    $tripInfo = $trips[$tid];
    $rid      = $tripInfo['route_id'];
    $stopId   = $row[$idxStop];
    $parent   = resolve_parent_station($stopId, $stops);

    // (1) correspondances : on enregistre pour TOUTES les routes interessantes
    $routeServesStation[$rid][$parent] = true;

    // (2) suite reservee aux routes metro
    if (!isset($metroRouteIds[$rid])) continue;
    $metroMatched++;

    // (2b) accessibilite : votes par platform-stop desservi par metro
    $wb = $stops[$stopId]['wheelchair_boarding'] ?? null;
    if ($wb === 1) {
        $stationAccessibleVotes[$parent]['has1'] = true;
    } elseif ($wb === 2) {
        $stationAccessibleVotes[$parent]['has2'] = true;
    }

    $depSec = gtfs_time_to_seconds($row[$idxDep]);
    $arrSec = gtfs_time_to_seconds($row[$idxArr]);
    $seq    = (int)$row[$idxSeq];

    // Stations en sequence pour le trip (servira a choisir le longest)
    $metroData[$rid]['tripStops'][$tid][$seq] = $parent;

    // Premieres / dernieres heures par jour-type
    $svc = $tripInfo['service_id'];
    if (isset($serviceActive[$svc])) {
        foreach ($serviceActive[$svc] as $dateKey => $_) {
            $dir = $tripInfo['direction_id'];
            // sequence 0 = depart depuis terminus
            if ($seq === 0 && $depSec !== null) {
                $metroData[$rid]['departures'][$dateKey][$dir][] = $depSec;
            }
            // arrival_time partout pour calculer le "dernier metro" (max sur toutes seq)
            if ($arrSec !== null) {
                $cur = $metroData[$rid]['lastArrival'][$dateKey] ?? -1;
                if ($arrSec > $cur) $metroData[$rid]['lastArrival'][$dateKey] = $arrSec;
            }
            if ($seq === 0 && $depSec !== null) {
                $cur = $metroData[$rid]['firstDeparture'][$dateKey] ?? PHP_INT_MAX;
                if ($depSec < $cur) $metroData[$rid]['firstDeparture'][$dateKey] = $depSec;
            }
        }
    }

    // Duree par trip (premiere et derniere arrival_time / departure_time)
    if ($depSec !== null) {
        $cur = $metroData[$rid]['tripFirstDep'][$tid] ?? PHP_INT_MAX;
        if ($depSec < $cur) $metroData[$rid]['tripFirstDep'][$tid] = $depSec;
    }
    if ($arrSec !== null) {
        $cur = $metroData[$rid]['tripLastArr'][$tid] ?? -1;
        if ($arrSec > $cur) $metroData[$rid]['tripLastArr'][$tid] = $arrSec;
    }
}
fclose($fp);
$elapsed = microtime(true) - $start;
log_info(sprintf('  termine: %s lignes traitees en %.1fs (%s metro matched, %s interesting)',
    number_format($count), $elapsed, number_format($metroMatched), number_format($matched)));

// ============================================================================
// 8. SHAPES.TXT (longueur des lignes)
// ============================================================================

log_info('Phase 8: shapes.txt (calcul longueurs metro via haversine)');

// On a besoin d'UNE shape_id representative par route metro (la plus longue parmi
// les trips de la route). On va la determiner via $trips + $metroData['tripStops'].
// Choix : pour chaque route metro, on prend le shape_id du trip qui a le plus
// grand nombre de stops (tous services confondus).
$bestShapePerRoute = []; // route_id => shape_id
foreach ($metroRouteIds as $rid => $_slug) {
    $bestTid = null; $bestStops = -1;
    foreach ($metroData[$rid]['tripStops'] ?? [] as $tid => $stopsByseq) {
        $n = count($stopsByseq);
        if ($n > $bestStops && isset($trips[$tid]['shape_id']) && $trips[$tid]['shape_id']) {
            $bestStops = $n; $bestTid = $tid;
        }
    }
    if ($bestTid !== null) {
        $bestShapePerRoute[$rid] = $trips[$bestTid]['shape_id'];
    }
}
$shapesNeeded = array_flip(array_values($bestShapePerRoute));
log_info(sprintf('  shapes a calculer: %d (1 par metro)', count($shapesNeeded)));

// shape_id => liste de [lat,lon,seq] -> on la garde en RAM pour les shapes choisies uniquement
$shapePoints = [];
$count = 0;
stream_csv(GTFS_DIR . '/shapes.txt', function (array $r) use (&$shapePoints, $shapesNeeded, &$count) {
    $count++;
    if (!isset($shapesNeeded[$r['shape_id']])) return;
    $shapePoints[$r['shape_id']][] = [
        (float)$r['shape_pt_lat'],
        (float)$r['shape_pt_lon'],
        (int)$r['shape_pt_sequence'],
    ];
}, 1_000_000);
log_info(sprintf('  shapes.txt: %d lignes scannees', $count));

// Calcul des longueurs
$routeLengthKm = []; // route_id => float
foreach ($bestShapePerRoute as $rid => $shapeId) {
    if (!isset($shapePoints[$shapeId])) continue;
    $pts = $shapePoints[$shapeId];
    usort($pts, fn($a, $b) => $a[2] <=> $b[2]);
    $total = 0.0;
    for ($i = 1; $i < count($pts); $i++) {
        $total += haversine_km($pts[$i-1][0], $pts[$i-1][1], $pts[$i][0], $pts[$i][1]);
    }
    $routeLengthKm[$rid] = round($total, 1);
}

// ============================================================================
// 9. CALCULS PAR LIGNE METRO
// ============================================================================

log_info('Phase 9: calcul des donnees factuelles par ligne');

/**
 * Mediane d'un tableau (interpolation lineaire si pair).
 */
function median(array $values): ?float {
    if (empty($values)) return null;
    sort($values);
    $n = count($values);
    if ($n % 2 === 1) return (float)$values[intdiv($n, 2)];
    return ($values[$n/2 - 1] + $values[$n/2]) / 2;
}

/**
 * A partir des departures (liste de timestamps en secondes a sequence=0),
 * calcule la mediane des intervalles consecutifs dans une fenetre [from, to].
 */
function compute_headway(array $departures, array $window): ?float {
    [$from, $to] = $window;
    sort($departures);
    $diffs = [];
    for ($i = 1; $i < count($departures); $i++) {
        $a = $departures[$i-1]; $b = $departures[$i];
        // l'intervalle est dans la fenetre si le second depart est dans la fenetre
        if ($b < $from || $b > $to) continue;
        $d = $b - $a;
        if ($d > 0 && $d < 30 * 60) $diffs[] = $d; // ignore les "pauses" > 30min
    }
    return median($diffs);
}

/**
 * Construit la liste ordonnee des stations (parent_station) pour la ligne :
 * on prend, sur le jour-type 'weekday', le trip direction_id=0 le plus long.
 * Si direction 0 a moins de stops que direction 1, on inverse.
 */
function pick_canonical_stops(string $rid, array $metroData, array $trips, array $serviceActive): array {
    $byDir = [0 => null, 1 => null]; // dir => [tripId, count]
    foreach ($metroData[$rid]['tripStops'] ?? [] as $tid => $stopsByseq) {
        $info = $trips[$tid] ?? null;
        if (!$info) continue;
        if (!isset($serviceActive[$info['service_id']]['weekday'])) continue;
        $n = count($stopsByseq);
        $dir = $info['direction_id'];
        if ($byDir[$dir] === null || $n > $byDir[$dir][1]) $byDir[$dir] = [$tid, $n];
    }
    // On retient le trip avec le plus de stops, tout en preferant direction_id=0 a egalite
    $best = null;
    if ($byDir[0] && (!$byDir[1] || $byDir[0][1] >= $byDir[1][1])) {
        $best = ['dir' => 0, 'tid' => $byDir[0][0]];
    } elseif ($byDir[1]) {
        $best = ['dir' => 1, 'tid' => $byDir[1][0]];
    }
    if (!$best) return ['stops' => [], 'direction' => null];

    $stopsByseq = $metroData[$rid]['tripStops'][$best['tid']];
    ksort($stopsByseq);
    return ['stops' => array_values($stopsByseq), 'direction' => $best['dir'], 'tid' => $best['tid']];
}

/**
 * Pour un parent_station, calcule les correspondances (autres lignes du reseau).
 */
function compute_correspondences(string $parentStation, string $currentRouteId, array $transferGraph, array $routeServesStation, array $routeIdToInfo): array {
    // Stations physiques liees (incluant le station meme)
    $linked = [$parentStation => true] + ($transferGraph[$parentStation] ?? []);

    $correspondences = [];
    $seenKey = [];
    foreach ($routeIdToInfo as $rid => $info) {
        if ($rid === $currentRouteId) continue;
        $served = $routeServesStation[$rid] ?? [];
        foreach ($linked as $st => $_) {
            if (isset($served[$st])) {
                $key = $info['mode'] . '|' . $info['code'];
                if (!isset($seenKey[$key])) {
                    $seenKey[$key] = true;
                    $correspondences[] = [
                        'mode'  => $info['mode'],
                        'line'  => $info['code'],
                        'color' => $info['color'] ?? '#999999',
                    ];
                }
                break;
            }
        }
    }
    // Tri pour determinisme : M(asc num/3B) > RER > T > TRANS
    usort($correspondences, function ($a, $b) {
        $order = ['M' => 0, 'RER' => 1, 'T' => 2, 'TRANS' => 3];
        if ($a['mode'] !== $b['mode']) return $order[$a['mode']] <=> $order[$b['mode']];
        return strnatcmp($a['line'], $b['line']);
    });
    return $correspondences;
}

// Pour chaque metro a traiter, on assemble le bloc factuel
$lineFactual = []; // file_slug => array

foreach ($metroRouteIdsToProcess as $rid => $fileSlug) {
    $code = $metroFileSlugToCode[$fileSlug] ?? null;
    if ($code === null) continue;

    log_info(sprintf('  ligne %s (%s)...', $code, $fileSlug));

    // Lookup couleurs/termini canoniques depuis lines.json.
    // Tolere les variantes 3B/3bis et 7B/7bis : on derive aussi le label a partir
    // du file_slug (ex. "metro-3bis" -> "3bis").
    $codeFromFileSlug = preg_replace('/^metro-/', '', $fileSlug); // "1", "3bis", etc.
    $summaryRow = null;
    foreach ($linesSummary['metro'] as $row) {
        if (strcasecmp($row['label'], $code) === 0
         || strcasecmp($row['label'], $codeFromFileSlug) === 0
         || strcasecmp($row['slug'] ?? '', $fileSlug) === 0
         || strcasecmp(($row['slug'] ?? ''), 'ligne-' . $codeFromFileSlug) === 0) {
            $summaryRow = $row;
            break;
        }
    }

    // Schedule
    $schedule = [
        'first_departure' => [],
        'last_departure'  => [],
        'frequency'       => [],
    ];
    foreach (['weekday','saturday','sunday'] as $key) {
        if (isset($metroData[$rid]['firstDeparture'][$key])) {
            $schedule['first_departure'][$key] = fmt_clock($metroData[$rid]['firstDeparture'][$key]);
        }
    }
    foreach (['weekday','friday','saturday','sunday'] as $key) {
        if (isset($metroData[$rid]['lastArrival'][$key])) {
            $schedule['last_departure'][$key] = fmt_clock($metroData[$rid]['lastArrival'][$key]);
        }
    }

    // Frequencies (mediane des intervalles a sequence=0, direction_id=0)
    $weekdayDeps = $metroData[$rid]['departures']['weekday'][0] ?? [];
    $satDeps     = $metroData[$rid]['departures']['saturday'][0] ?? [];
    $sunDeps     = $metroData[$rid]['departures']['sunday'][0]   ?? [];
    $allDay      = [0, 30 * 3600];

    $peak    = compute_headway($weekdayDeps, PEAK_WINDOW);
    $offPeak = compute_headway($weekdayDeps, OFF_PEAK_WINDOW);
    $evening = compute_headway($weekdayDeps, EVENING_WINDOW);
    $weekend = median(array_filter([
        compute_headway($satDeps, $allDay),
        compute_headway($sunDeps, $allDay),
    ], fn($v) => $v !== null));

    if ($peak !== null) {
        $schedule['frequency']['peak_hours'] = [
            'label'    => 'Heures de pointe',
            'times'    => '7h-9h30 et 17h-20h',
            'interval' => fmt_interval($peak),
        ];
    }
    if ($offPeak !== null) {
        $schedule['frequency']['off_peak'] = [
            'label'    => 'Heures creuses',
            'times'    => '9h30-17h et 20h-23h',
            'interval' => fmt_interval($offPeak),
        ];
    }
    if ($evening !== null) {
        $schedule['frequency']['evening'] = [
            'label'    => 'Soiree',
            'times'    => '23h-1h',
            'interval' => fmt_interval($evening),
        ];
    }
    if ($weekend !== null) {
        $schedule['frequency']['weekend'] = [
            'label'    => 'Week-end',
            'times'    => 'Toute la journee',
            'interval' => fmt_interval($weekend),
        ];
    }

    // Stations canoniques (longest trip dir=0 ou 1 sur jour-type weekday)
    $canon = pick_canonical_stops($rid, $metroData, $trips, $serviceActive);
    $canonicalStops = $canon['stops'];

    // Cas des lignes en Y/branche (3bis, 7bis) : aucun trip ne visite toutes les
    // stations en une seule fois. On complete avec la difference de l'ensemble
    // des parent_stations effectivement desservis par la ligne (toutes services).
    $allServed = array_keys($routeServesStation[$rid] ?? []);
    $canonSet = array_flip($canonicalStops);
    foreach ($allServed as $ps) {
        if (!isset($canonSet[$ps])) {
            $canonicalStops[] = $ps; // append (position approximative pour les bis)
            $canonSet[$ps] = true;
        }
    }

    $stationsList = [];
    foreach ($canonicalStops as $parentStop) {
        $stopInfo = $stops[$parentStop] ?? null;
        if (!$stopInfo) continue;
        $entry = [
            'name'            => $stopInfo['name'],
            'correspondences' => compute_correspondences($parentStop, $rid, $transferGraph, $routeServesStation, $routeIdToInfo),
        ];
        // accessible : 3 etats. true si has1, false si has2 sans has1, sinon absent.
        $votes = $stationAccessibleVotes[$parentStop] ?? [];
        if (!empty($votes['has1'])) {
            $entry['accessible'] = true;
        } elseif (!empty($votes['has2'])) {
            $entry['accessible'] = false;
        }
        $stationsList[] = $entry;
    }

    // Inversion eventuelle pour matcher terminus_a -> terminus_b de lines.json
    if (!empty($stationsList) && $summaryRow) {
        $first = $stationsList[0]['name'] ?? '';
        $expectedFirst = $summaryRow['termini'][0] ?? '';
        // Comparaison souple (le terminus dans lines.json peut differer en parens etc.)
        $similarity = 0;
        similar_text(mb_strtolower($first), mb_strtolower($expectedFirst), $similarity);
        if ($similarity < 50) {
            $stationsList = array_reverse($stationsList);
        }
    }

    // Duree moyenne terminus-a-terminus
    $durations = [];
    foreach ($metroData[$rid]['tripStops'] ?? [] as $tid => $byseq) {
        // Garde-fou : >= 3 stops (M3bis = 4 stations, pas de trip plus court).
        if (count($byseq) < 3) continue;
        $first = $metroData[$rid]['tripFirstDep'][$tid] ?? null;
        $last  = $metroData[$rid]['tripLastArr'][$tid] ?? null;
        if ($first === null || $last === null) continue;
        $d = $last - $first;
        // >= 60s (lignes navette), < 90 min (eviter trips qui chevauchent minuit).
        if ($d >= 60 && $d < 90 * 60) $durations[] = $d;
    }
    $durationMin = !empty($durations) ? (int) round(array_sum($durations) / count($durations) / 60) : null;

    // Statistiques d'accessibilite recalculees depuis stations[]
    $accessibleCount = 0;
    foreach ($stationsList as $s) {
        if (($s['accessible'] ?? null) === true) $accessibleCount++;
    }
    $totalCount = count($stationsList);
    $accessibilityRate = $totalCount > 0 ? (int) round($accessibleCount / $totalCount * 100) : 0;

    // Liste des stations accessibles (pour accessibility.accessible_stations)
    $accessibleStations = [];
    foreach ($stationsList as $s) {
        if (($s['accessible'] ?? null) === true) {
            $entry = ['name' => $s['name']];
            // subtitle / is_major non disponibles dans le calcul GTFS — preserves par le merge si existants
            $accessibleStations[] = $entry;
        }
    }

    // Assemblage
    $factual = [
        'id'               => $fileSlug,
        'mode'             => 'metro',
        'code'             => $code,
        'name'             => 'Ligne ' . $code,
        'color'            => $summaryRow['color']      ?? null,
        'color_text'       => $summaryRow['text_color'] ?? null,
        'terminus_a'       => $summaryRow['termini'][0] ?? null,
        'terminus_b'       => $summaryRow['termini'][1] ?? null,
        'stations_count'   => count($stationsList),
        'length_km'        => $routeLengthKm[$rid] ?? ($summaryRow['length_km'] ?? null),
        'duration_minutes' => $durationMin,
        'automated'        => $summaryRow['automatic'] ?? null,
        'opened_year'      => $summaryRow['opened']    ?? null,
        'schedule'         => $schedule,
        'stations'         => $stationsList,
        '_accessibility_recompute' => [
            'accessible_count'   => $accessibleCount,
            'total_count'        => $totalCount,
            'accessibility_rate' => $accessibilityRate,
            'accessible_stations' => $accessibleStations,
        ],
    ];

    $lineFactual[$fileSlug] = $factual;
}

// ============================================================================
// 10. PREVIEW DIFF OU ECRITURE
// ============================================================================

/**
 * Cles factuelles ecrasables. Le reste (editorial) est preserve si le fichier existe.
 */
const FACTUAL_KEYS = [
    'id','mode','code','name','color','color_text','terminus_a','terminus_b',
    'stations_count','length_km','duration_minutes','automated','opened_year',
    'schedule','stations',
];

/**
 * Pour les fichiers existants, recalcule accessibility.stats.{accessible_count,
 * total_count, accessibility_rate} et accessibility.accessible_stations a partir
 * du bloc stations[] qu'on vient de regenerer. Les autres cles editoriales
 * (equipment, tips, external_resources, stats.elevators_count, etc.) sont preservees.
 *
 * Pour accessibility.accessible_stations : on regenere la liste mais on tente
 * de preserver les champs editoriaux (subtitle, is_major) presents dans l'ancien.
 */
/**
 * Construit le JSON final pour une ligne :
 *  - si existing != null : merge non-destructif (preserve editorial)
 *  - sinon : JSON minimal (uniquement les cles factuelles non-null)
 *
 * Retourne ['output' => array, 'log' => string|null].
 */
function build_output(string $fileSlug, array $factual, ?array $existing, ?array $accessibilityRecompute): array {
    $log = null;
    if (is_array($existing)) {
        $merged = $existing;
        foreach (FACTUAL_KEYS as $k) {
            if ($k === 'stations') continue;
            if (array_key_exists($k, $factual) && $factual[$k] !== null) {
                $merged[$k] = $factual[$k];
            }
        }
        if (isset($factual['stations']) && isset($existing['stations'])
         && count($factual['stations']) === count($existing['stations'])) {
            $mergedStations = [];
            foreach ($factual['stations'] as $i => $newS) {
                $oldS = $existing['stations'][$i];
                $entry = $oldS;
                $entry['correspondences'] = $newS['correspondences'];
                if (array_key_exists('accessible', $newS)) {
                    $entry['accessible'] = $newS['accessible'];
                } else {
                    unset($entry['accessible']);
                }
                $mergedStations[] = $entry;
            }
            $merged['stations'] = $mergedStations;
        } elseif (isset($factual['stations'])) {
            $log = sprintf('ATTENTION: stations_count differe (%d new vs %d old) pour %s, remplacement complet',
                count($factual['stations']), count($existing['stations'] ?? []), $fileSlug);
            $merged['stations'] = $factual['stations'];
        }
        if ($accessibilityRecompute) {
            apply_accessibility_recompute($merged, $accessibilityRecompute, $existing['accessibility']['accessible_stations'] ?? null);
        }
        return ['output' => $merged, 'log' => $log];
    }
    // Nouveau fichier : JSON minimal (uniquement les cles factuelles non-null)
    $output = [];
    foreach (FACTUAL_KEYS as $k) {
        if (array_key_exists($k, $factual) && $factual[$k] !== null) {
            $output[$k] = $factual[$k];
        }
    }
    return ['output' => $output, 'log' => null];
}

function apply_accessibility_recompute(array &$merged, array $recompute, ?array $existingStations = null): void {
    if (!isset($merged['accessibility'])) return;
    if (isset($merged['accessibility']['stats'])) {
        $merged['accessibility']['stats']['accessible_count']   = $recompute['accessible_count'];
        $merged['accessibility']['stats']['total_count']        = $recompute['total_count'];
        $merged['accessibility']['stats']['accessibility_rate'] = $recompute['accessibility_rate'];
    }
    // accessible_stations : on construit a partir du nouveau, en preservant les
    // champs editoriaux (subtitle, is_major) trouves dans l'ancienne liste si meme nom.
    $oldByName = [];
    if (is_array($existingStations)) {
        foreach ($existingStations as $s) {
            if (!empty($s['name'])) $oldByName[$s['name']] = $s;
        }
    }
    $newAccessibleStations = [];
    foreach ($recompute['accessible_stations'] as $s) {
        $entry = ['name' => $s['name']];
        if (isset($oldByName[$s['name']]['subtitle']))  $entry['subtitle']  = $oldByName[$s['name']]['subtitle'];
        if (isset($oldByName[$s['name']]['is_major']))  $entry['is_major']  = $oldByName[$s['name']]['is_major'];
        $newAccessibleStations[] = $entry;
    }
    $merged['accessibility']['accessible_stations'] = $newAccessibleStations;
}

function pretty_json(array $data): string {
    return json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
}

function diff_block(string $label, $existing, $computed): string {
    $out = "\n=== $label ===\n";
    $oldS = pretty_json(['_' => $existing]);
    $newS = pretty_json(['_' => $computed]);
    if ($oldS === $newS) {
        $out .= "(identique)\n";
        return $out;
    }
    $out .= "--- ANCIEN (existant) ---\n" . $oldS . "\n";
    $out .= "+++ NOUVEAU (calcule) +++\n" . $newS . "\n";
    return $out;
}

if ($preview) {
    log_info('Phase 10: PREVIEW (aucune ecriture)');
    foreach ($lineFactual as $fileSlug => $factual) {
        $existingPath = LINES_DIR . '/' . $fileSlug . '.json';
        $existing = is_file($existingPath) ? json_decode(file_get_contents($existingPath), true) : null;

        $accRecompute = $factual['_accessibility_recompute'] ?? null;
        unset($factual['_accessibility_recompute']);

        $built = build_output($fileSlug, $factual, $existing, $accRecompute);
        $merged = $built['output'];
        if ($built['log']) log_info('  ' . $built['log']);

        echo "\n";
        echo "############################################################\n";
        echo "# PREVIEW : $fileSlug" . ($existing ? " (merge avec existant)" : " (nouveau fichier)") . "\n";
        echo "############################################################\n";

        // Metadata sommaire
        echo "Identite (apres merge):\n";
        foreach (['code','name','terminus_a','terminus_b','stations_count','length_km','duration_minutes'] as $k) {
            $newV = $merged[$k] ?? null;
            $oldV = $existing[$k] ?? null;
            $tag = ($newV === $oldV) ? '   ' : ' * ';
            echo sprintf("  %s %-18s : %s    (existant: %s)\n", $tag, $k, var_export($newV, true), var_export($oldV, true));
        }

        echo diff_block('schedule', $existing['schedule'] ?? null, $merged['schedule'] ?? null);
        echo diff_block('stations (apres merge per-station)', $existing['stations'] ?? null, $merged['stations'] ?? null);

        if ($accRecompute && isset($merged['accessibility'])) {
            echo diff_block('accessibility.stats (recalcule)', $existing['accessibility']['stats'] ?? null, $merged['accessibility']['stats'] ?? null);
            $oldList = $existing['accessibility']['accessible_stations'] ?? [];
            $newList = $merged['accessibility']['accessible_stations'] ?? [];
            echo "\n=== accessibility.accessible_stations (recalcule) ===\n";
            echo "  ANCIEN: " . count($oldList) . " stations\n";
            echo "  NOUVEAU: " . count($newList) . " stations";
            if (!empty($newList)) {
                echo " (" . implode(', ', array_column($newList, 'name')) . ")";
            }
            echo "\n";
        }
    }
    log_info('Preview terminee. Aucun fichier ecrit.');
    exit(0);
}

log_info('Phase 10: ecriture des fichiers');

foreach ($lineFactual as $fileSlug => $factual) {
    $path = LINES_DIR . '/' . $fileSlug . '.json';
    $existing = is_file($path) ? json_decode(file_get_contents($path), true) : null;

    $accRecompute = $factual['_accessibility_recompute'] ?? null;
    unset($factual['_accessibility_recompute']);

    $built = build_output($fileSlug, $factual, $existing, $accRecompute);
    if ($built['log']) log_info('  ' . $built['log']);

    file_put_contents($path, pretty_json($built['output']) . "\n");
    log_info('  ecrit: ' . $path);
}

log_info('Termine.');
