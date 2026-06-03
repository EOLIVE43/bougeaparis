<?php
declare(strict_types=1);

error_reporting(E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED);
ini_set('memory_limit', '512M');

/**
 * scripts/bootstrap-station.php
 *
 * Générateur de squelette JSON station métro pour l'industrialisation 300 stations.
 *
 * À partir d'un slug (ou nom) de station, produit automatiquement les sections A+B
 * (auto-générables) du JSON station en réutilisant les scripts existants + GTFS
 * IDFM. Les sections C (éditoriales) restent en stubs vides avec marker _todo.
 * Flag racine "published": false par défaut → garde-fou Routes auto-activation.
 *
 * Sections A auto-générées :
 *   - slug, name, name_full, latitude, longitude
 *   - lines[] (via GTFS routes + line-mapping)
 *   - adjacent_stations (via GTFS stop_times séquences)
 *   - is_major_hub (heuristique : ≥3 lignes OU RER présent)
 *   - tariff_zone (1 par défaut, Paris intra-muros)
 *   - i18n stubs (en/es)
 *   - Q-ID Wikidata via SPARQL search (sameAs URLs)
 *
 * Sections B auto-générées via sous-process :
 *   - exits[] via scripts/build-station-exits.php (GTFS parent_station + transfers)
 *   - nearby_pois[] via scripts/build-station-pois.php (SPARQL Wikidata 800m)
 *
 * Sections C laissées en stubs (à compléter par humain/LLM) :
 *   - seo.description, hero (tagline + description)
 *   - intro_paragraphs (3 stubs), history (title + 3 stubs)
 *   - faq (8 stubs), trivia (5 stubs), practical_tips (6 stubs)
 *   - services, safety, accessibility (stubs avec defaults)
 *
 * Usage :
 *   php scripts/bootstrap-station.php --slug=opera
 *   php scripts/bootstrap-station.php --name="Opéra"
 *   php scripts/bootstrap-station.php --slug=opera --force
 *   php scripts/bootstrap-station.php --slug=opera --dry-run
 *   php scripts/bootstrap-station.php --slug=opera --skip-pois
 *   php scripts/bootstrap-station.php --slug=opera --skip-exits
 *   php scripts/bootstrap-station.php --slug=opera --skip-wikidata
 *
 * Exit codes : 0=succès, 1=warnings sections partielles, 2=erreur bloquante.
 *
 * Pré-requis : GTFS IDFM téléchargé dans scripts/cache-gtfs/idfm-gtfs/
 * (sinon lancer d'abord scripts/build-line-jsons.php).
 */

const GTFS_DIR = __DIR__ . '/cache-gtfs/idfm-gtfs';
const STATIONS_DIR = __DIR__ . '/../public_html/data/stations';
const LINE_MAPPING_PATH = __DIR__ . '/../public_html/config/line-mapping.php';

// ─────────────────────────────────────────────────────────────
// CLI parsing
// ─────────────────────────────────────────────────────────────

$opts = ['slug' => '', 'name' => '', 'force' => false, 'dry-run' => false,
         'skip-pois' => false, 'skip-exits' => false, 'skip-wikidata' => false];
foreach (array_slice($argv, 1) as $arg) {
    if (preg_match('/^--slug=(.+)$/', $arg, $m)) $opts['slug'] = $m[1];
    elseif (preg_match('/^--name=(.+)$/', $arg, $m)) $opts['name'] = $m[1];
    elseif ($arg === '--force') $opts['force'] = true;
    elseif ($arg === '--dry-run') $opts['dry-run'] = true;
    elseif ($arg === '--skip-pois') $opts['skip-pois'] = true;
    elseif ($arg === '--skip-exits') $opts['skip-exits'] = true;
    elseif ($arg === '--skip-wikidata') $opts['skip-wikidata'] = true;
    else { fwrite(STDERR, "Argument inconnu : $arg\n"); exit(2); }
}
if ($opts['slug'] === '' && $opts['name'] === '') {
    fwrite(STDERR, "Usage: php bootstrap-station.php (--slug=<slug>|--name=\"<name>\") [--force] [--dry-run] [--skip-pois] [--skip-exits] [--skip-wikidata]\n");
    exit(2);
}

// Calcul slug si pas donné
if ($opts['slug'] === '') $opts['slug'] = slugify($opts['name']);
if ($opts['name'] === '') $opts['name'] = null;  // sera dérivé du GTFS

$slug = $opts['slug'];
$jsonPath = STATIONS_DIR . '/' . $slug . '.json';

logStep("Bootstrap station : $slug");

// ─────────────────────────────────────────────────────────────
// Garde-fou existing file
// ─────────────────────────────────────────────────────────────

if (file_exists($jsonPath) && !$opts['force'] && !$opts['dry-run']) {
    fwrite(STDERR, "Erreur : $jsonPath existe déjà. Utilise --force pour merger (préserve champs non-vides) ou --dry-run pour visualiser.\n");
    exit(2);
}

// Pré-requis GTFS
if (!is_file(GTFS_DIR . '/stops.txt')) {
    fwrite(STDERR, "Erreur : GTFS IDFM absent (scripts/cache-gtfs/idfm-gtfs/stops.txt). Lance d'abord scripts/build-line-jsons.php pour télécharger le GTFS.\n");
    exit(2);
}

// ─────────────────────────────────────────────────────────────
// Étape 1 : Charger stops.txt + résoudre le parent_station
// ─────────────────────────────────────────────────────────────

logStep("Chargement stops.txt...");
$stops = loadStops(GTFS_DIR . '/stops.txt');
logInfo("  " . count($stops) . " stops chargés");

logStep("Résolution parent_station pour '$slug'...");
$searchName = $opts['name'] ?? humanizeSlug($slug);
$parent = findParentStation($stops, $searchName, $slug);
if (!$parent) {
    fwrite(STDERR, "Erreur : aucun parent_station (location_type=1) trouvé pour '$searchName' / '$slug'. Vérifie le slug ou le nom.\n");
    exit(2);
}
logInfo("  Parent trouvé : {$parent['stop_id']} « {$parent['stop_name']} » (lat={$parent['stop_lat']}, lon={$parent['stop_lon']})");

// ─────────────────────────────────────────────────────────────
// Étape 2 : Identifier les lignes desservies
// ─────────────────────────────────────────────────────────────

logStep("Identification des lignes métro/RER desservies...");
$childStops = findChildStops($stops, $parent['stop_id']);
logInfo("  " . count($childStops) . " quais/sorties enfants");

$lines = identifyLines($childStops, $parent['stop_id']);
logInfo("  " . count($lines) . " ligne(s) métro/RER identifiée(s) : " .
        implode(', ', array_column($lines, 'code')));

if (empty($lines)) {
    logWarn("Aucune ligne métro/RER trouvée pour cette station. Bootstrap interrompu (rien à générer).");
    exit(2);
}

// ─────────────────────────────────────────────────────────────
// Étape 3 : Adjacent stations par ligne (via stop_times)
// ─────────────────────────────────────────────────────────────

logStep("Calcul adjacent_stations par ligne...");
$adjacents = buildAdjacentStations($stops, $childStops, $lines);
foreach ($adjacents as $lineSlug => $adj) {
    $prev = $adj['previous']['name'] ?? '(début ligne)';
    $next = $adj['next']['name'] ?? '(fin ligne)';
    logInfo("  $lineSlug : $prev ← X → $next");
}

// ─────────────────────────────────────────────────────────────
// Étape 4 : Wikidata Q-ID (sameAs SEO)
// ─────────────────────────────────────────────────────────────

$wikidata = null;
if (!$opts['skip-wikidata']) {
    logStep("Recherche Q-ID Wikidata pour la station...");
    $wikidata = fetchWikidataInfo($parent['stop_name']);
    if ($wikidata && !empty($wikidata['qid'])) {
        logInfo("  Q-ID trouvé : {$wikidata['qid']} (wikipedia: " . ($wikidata['wikipedia_url'] ?? '?') . ")");
    } else {
        logInfo("  Aucun Q-ID trouvé (ou SPARQL timeout). Section sameAs vide.");
    }
} else {
    logInfo("  Skip Wikidata (--skip-wikidata)");
}

// ─────────────────────────────────────────────────────────────
// Étape 5 : Métadonnées dérivées
// ─────────────────────────────────────────────────────────────

$isMajorHub = computeIsMajorHub($lines);
$nameFull = buildNameFull($parent['stop_name'], $lines);
$tariffZone = computeTariffZone($parent);

logInfo("  is_major_hub = " . ($isMajorHub ? 'true' : 'false') . " (heuristique : " .
        count($lines) . " lignes" . (hasRer($lines) ? ' + RER' : '') . ")");

// ─────────────────────────────────────────────────────────────
// Étape 6 : Charger JSON existant (--force merge) ou stubs
// ─────────────────────────────────────────────────────────────

$existing = [];
if ($opts['force'] && file_exists($jsonPath)) {
    $existing = json_decode((string)file_get_contents($jsonPath), true) ?? [];
    logInfo("  --force : JSON existant chargé pour merge (préservation des champs non-vides)");
}

// ─────────────────────────────────────────────────────────────
// Étape 7 : Construire JSON squelette
// ─────────────────────────────────────────────────────────────

logStep("Construction du squelette JSON...");
$json = buildSkeleton(
    $slug, $parent, $nameFull, $lines, $adjacents, $isMajorHub, $tariffZone, $wikidata, $existing
);

// ─────────────────────────────────────────────────────────────
// Étape 8 : Écriture
// ─────────────────────────────────────────────────────────────

if ($opts['dry-run']) {
    echo json_encode($json, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    echo "\n";
    logInfo("  --dry-run : aucune écriture disque");
    exit(0);
}

@mkdir(STATIONS_DIR, 0755, true);
file_put_contents($jsonPath, json_encode($json, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n");
logInfo("  Écrit : $jsonPath (" . number_format(strlen(json_encode($json))) . " bytes)");

// ─────────────────────────────────────────────────────────────
// Étape 9 : Sous-process (exits + pois)
// ─────────────────────────────────────────────────────────────

$warnings = [];

if (!$opts['skip-exits']) {
    logStep("Enrichissement exits[] via build-station-exits.php...");
    if (!runSubprocess($slug, 'build-station-exits.php', 60)) {
        $warnings[] = 'exits non générés';
    }
}

if (!$opts['skip-pois']) {
    logStep("Enrichissement nearby_pois[] via build-station-pois.php...");
    if (!runSubprocess($slug, 'build-station-pois.php', 60)) {
        $warnings[] = 'POIs non générés';
    }
}

// ─────────────────────────────────────────────────────────────
// Étape 10 : Validation finale
// ─────────────────────────────────────────────────────────────

logStep("Validation via validate-station.php...");
$validateOk = runSubprocess($slug, 'validate-station.php', 30, ['--check-wikidata']);
if (!$validateOk) $warnings[] = 'validate-station a signalé des erreurs (voir logs)';

// ─────────────────────────────────────────────────────────────
// Récap final
// ─────────────────────────────────────────────────────────────

// Recharger le JSON depuis le disque : les sous-process exits/pois
// l'ont modifié hors de la portée PHP en mémoire. Sans ce reload,
// printSummary affichait 0 exits / 0 pois (friction documentée
// dans docs/TEMPLATE_GUIDE.md).
$json = json_decode((string)file_get_contents($jsonPath), true) ?? $json;

printSummary($jsonPath, $json, $warnings);
exit(count($warnings) > 0 ? 1 : 0);


// ═══════════════════════════════════════════════════════════════════════════
// Fonctions
// ═══════════════════════════════════════════════════════════════════════════

function logStep(string $msg): void { fwrite(STDERR, "\n▶ $msg\n"); }
function logInfo(string $msg): void { fwrite(STDERR, "  $msg\n"); }
function logWarn(string $msg): void { fwrite(STDERR, "⚠️  $msg\n"); }

function slugify(string $name): string
{
    // Translittération identique à Routes::stationSlug() côté PHP
    $name = preg_replace('/\s*\([^)]*\)\s*/', '', $name);
    $name = strtr($name, [
        'à'=>'a','á'=>'a','â'=>'a','ä'=>'a','ã'=>'a','å'=>'a',
        'è'=>'e','é'=>'e','ê'=>'e','ë'=>'e',
        'ì'=>'i','í'=>'i','î'=>'i','ï'=>'i',
        'ò'=>'o','ó'=>'o','ô'=>'o','ö'=>'o','õ'=>'o',
        'ù'=>'u','ú'=>'u','û'=>'u','ü'=>'u',
        'ç'=>'c','ñ'=>'n',
        'À'=>'a','É'=>'e','È'=>'e','Ê'=>'e','Ô'=>'o','Î'=>'i',
        'Ç'=>'c','Ñ'=>'n','Œ'=>'oe','œ'=>'oe',
    ]);
    $slug = strtolower($name);
    $slug = preg_replace('/[^a-z0-9]+/', '-', $slug);
    return trim(preg_replace('/-+/', '-', $slug), '-');
}

function humanizeSlug(string $slug): string
{
    // Capitalise pour un match approximatif avec stops.txt
    $words = explode('-', $slug);
    $words = array_map('ucfirst', $words);
    return implode(' ', $words);
}

function normalizeForMatch(string $s): string
{
    $s = mb_strtolower($s, 'UTF-8');
    $s = strtr($s, [
        'à'=>'a','á'=>'a','â'=>'a','ä'=>'a','é'=>'e','è'=>'e','ê'=>'e','ë'=>'e',
        'ì'=>'i','í'=>'i','î'=>'i','ï'=>'i','ò'=>'o','ó'=>'o','ô'=>'o','ö'=>'o',
        'ù'=>'u','ú'=>'u','û'=>'u','ü'=>'u','ç'=>'c','ñ'=>'n','œ'=>'oe',
    ]);
    return preg_replace('/[^a-z0-9]+/u', '', $s);
}

function loadStops(string $path): array
{
    $stops = [];
    $fp = fopen($path, 'r');
    if (!$fp) throw new RuntimeException("Cannot open $path");
    $header = fgetcsv($fp);
    while (($row = fgetcsv($fp)) !== false) {
        if (count($row) < count($header)) $row = array_pad($row, count($header), '');
        $r = array_combine($header, array_slice($row, 0, count($header)));
        $stops[$r['stop_id']] = $r;
    }
    fclose($fp);
    return $stops;
}

function findParentStation(array $stops, string $searchName, string $slug): ?array
{
    // 1. Match exact sur stop_name (location_type=1)
    $needleN = normalizeForMatch($searchName);
    $slugN = normalizeForMatch($slug);
    $candidates = [];

    foreach ($stops as $s) {
        if (($s['location_type'] ?? '') !== '1') continue;
        $nameN = normalizeForMatch($s['stop_name']);
        if ($nameN === $needleN || $nameN === $slugN) {
            $candidates[] = $s;
        }
    }

    // 2. Si rien : match approximatif (contains)
    if (empty($candidates)) {
        foreach ($stops as $s) {
            if (($s['location_type'] ?? '') !== '1') continue;
            $nameN = normalizeForMatch($s['stop_name']);
            if (mb_strlen($needleN) >= 5 && str_contains($nameN, $needleN)) {
                $candidates[] = $s;
            }
        }
    }

    if (empty($candidates)) return null;

    // Privilégier celui qui a le plus d'enfants (proxy de "vraie station métro" vs arrêt isolé)
    $best = null; $maxChildren = -1;
    foreach ($candidates as $c) {
        $childCount = 0;
        foreach ($stops as $s) if (($s['parent_station'] ?? '') === $c['stop_id']) $childCount++;
        if ($childCount > $maxChildren) { $maxChildren = $childCount; $best = $c; }
    }
    return $best;
}

function findChildStops(array $stops, string $parentId): array
{
    $children = [];
    foreach ($stops as $s) {
        if (($s['parent_station'] ?? '') === $parentId) $children[$s['stop_id']] = $s;
    }
    return $children;
}

function identifyLines(array $childStops, string $parentId): array
{
    // Pour chaque quai enfant : grep stop_times → trip_id → route_id → route metadata
    // Optimisation : on collecte les stop_ids enfants, puis on grep stop_times.txt
    $childIds = array_keys($childStops);
    if (empty($childIds)) return [];

    // Récupérer trips via stop_times en streaming (file grep style)
    $tripIds = [];
    $fp = fopen(GTFS_DIR . '/stop_times.txt', 'r');
    fgetcsv($fp); // skip header
    $childIdSet = array_flip($childIds);
    while (($row = fgetcsv($fp)) !== false) {
        if (count($row) >= 7 && isset($childIdSet[$row[5]])) {
            $tripIds[$row[0]] = true;
        }
    }
    fclose($fp);

    // Récupérer route_id via trips.txt
    $routeIds = [];
    $fp = fopen(GTFS_DIR . '/trips.txt', 'r');
    fgetcsv($fp);
    while (($row = fgetcsv($fp)) !== false) {
        if (count($row) >= 3 && isset($tripIds[$row[2]])) {
            $routeIds[$row[0]] = true;
        }
    }
    fclose($fp);

    // Charger routes.txt + line-mapping pour identifier les routes métro/RER
    $lineMapping = require LINE_MAPPING_PATH;
    $lines = [];

    $fp = fopen(GTFS_DIR . '/routes.txt', 'r');
    fgetcsv($fp);
    while (($row = fgetcsv($fp)) !== false) {
        if (count($row) < 6) continue;
        $routeId = $row[0]; // ex IDFM:C01371
        if (!isset($routeIds[$routeId])) continue;
        $routeType = (int)$row[5];
        // route_type : 1=métro, 2=train (RER), 0=tram, 3=bus (selon GTFS)
        if (!in_array($routeType, [0, 1, 2], true)) continue; // skip bus

        $type = match($routeType) { 0 => 'tram', 1 => 'metro', 2 => 'rer', default => 'other' };

        // Extraire le code court PRIM (ex C01371) du route_id complet (IDFM:C01371)
        $primCode = '';
        if (preg_match('/C\d+/', $routeId, $m)) $primCode = $m[0];

        $internalSlug = $lineMapping[$type][$primCode] ?? null;
        if (!$internalSlug) continue; // route_id pas dans mapping → skip

        $lines[] = [
            'type' => $type,
            'code' => $row[2],
            'slug' => $internalSlug,
            'color' => '#' . strtoupper($row[7]),
            'text_color' => '#' . strtoupper($row[8] ?: '000000'),
            '_route_id' => $routeId, // private, pour adjacent_stations
        ];
    }
    fclose($fp);

    // Dedup par slug (au cas où plusieurs route_id pointent vers la même ligne)
    $unique = [];
    foreach ($lines as $l) $unique[$l['slug']] = $l;
    // Tri par type (metro > rer > tram) puis code
    usort($unique, function ($a, $b) {
        $order = ['metro' => 1, 'rer' => 2, 'tram' => 3];
        $ta = $order[$a['type']] ?? 9;
        $tb = $order[$b['type']] ?? 9;
        return $ta <=> $tb ?: strnatcmp($a['code'], $b['code']);
    });
    return array_values($unique);
}

function buildAdjacentStations(array $stops, array $childStops, array $lines): array
{
    // Pour chaque ligne, prendre un trip représentatif (le plus long en stop_count
    // qui passe par un de nos quais enfants), et lire le stop précédent/suivant.
    $childIds = array_keys($childStops);
    $childIdSet = array_flip($childIds);

    $adjacents = [];
    foreach ($lines as $line) {
        $routeId = $line['_route_id'];
        $adjacents[$line['slug']] = ['previous' => null, 'next' => null];

        // 1. Récupérer un trip représentatif sur cette route
        $tripId = null; $maxSeq = 0;
        $fp = fopen(GTFS_DIR . '/trips.txt', 'r');
        fgetcsv($fp);
        $tripsForRoute = [];
        while (($row = fgetcsv($fp)) !== false) {
            if (count($row) >= 3 && $row[0] === $routeId) $tripsForRoute[$row[2]] = true;
        }
        fclose($fp);

        if (empty($tripsForRoute)) continue;

        // 2. Trouver le premier trip qui contient un de nos childIds, et collecter sa séquence
        // Pour rapidité, on lit stop_times en streaming et on note la séquence des trips qu'on rencontre
        $candidateTrips = []; // trip_id => [['stop_id', 'stop_sequence']]
        $found = 0;
        $fp = fopen(GTFS_DIR . '/stop_times.txt', 'r');
        fgetcsv($fp);
        while (($row = fgetcsv($fp)) !== false) {
            if (count($row) < 7) continue;
            $tid = $row[0]; $sid = $row[5]; $seq = (int)$row[6];
            if (!isset($tripsForRoute[$tid])) continue;
            if (!isset($candidateTrips[$tid])) $candidateTrips[$tid] = [];
            $candidateTrips[$tid][] = ['stop_id' => $sid, 'stop_sequence' => $seq];
            // Si ce trip contient notre child, on flag
            if (isset($childIdSet[$sid])) $found++;
            // Early break : si on a 3 trips contenant nos children, c'est suffisant
            if ($found >= 30) break;
        }
        fclose($fp);

        // 3. Choisir le trip qui contient un child + a le plus de stops (terminus complet)
        $bestTrip = null; $bestLen = 0;
        foreach ($candidateTrips as $tid => $seq) {
            $hasChild = false;
            foreach ($seq as $st) if (isset($childIdSet[$st['stop_id']])) { $hasChild = true; break; }
            if (!$hasChild) continue;
            if (count($seq) > $bestLen) { $bestLen = count($seq); $bestTrip = $seq; }
        }
        if (!$bestTrip) continue;

        // 4. Trier par stop_sequence
        usort($bestTrip, fn($a, $b) => $a['stop_sequence'] <=> $b['stop_sequence']);

        // 5. Trouver l'index de notre child dans la séquence
        $idx = -1;
        foreach ($bestTrip as $i => $st) if (isset($childIdSet[$st['stop_id']])) { $idx = $i; break; }
        if ($idx < 0) continue;

        // 6. previous + next (résolu en parent_station + name)
        if ($idx > 0) {
            $prevStop = $stops[$bestTrip[$idx - 1]['stop_id']] ?? null;
            if ($prevStop) {
                $prevParent = resolveParent($stops, $prevStop['stop_id']);
                $adjacents[$line['slug']]['previous'] = [
                    'name' => $stops[$prevParent]['stop_name'] ?? $prevStop['stop_name'],
                    'slug' => slugify($stops[$prevParent]['stop_name'] ?? $prevStop['stop_name']),
                    'direction' => $stops[$bestTrip[0]['stop_id']]['stop_name'] ?? '?',
                ];
            }
        }
        if ($idx < count($bestTrip) - 1) {
            $nextStop = $stops[$bestTrip[$idx + 1]['stop_id']] ?? null;
            if ($nextStop) {
                $nextParent = resolveParent($stops, $nextStop['stop_id']);
                $adjacents[$line['slug']]['next'] = [
                    'name' => $stops[$nextParent]['stop_name'] ?? $nextStop['stop_name'],
                    'slug' => slugify($stops[$nextParent]['stop_name'] ?? $nextStop['stop_name']),
                    'direction' => $stops[end($bestTrip)['stop_id']]['stop_name'] ?? '?',
                ];
            }
        }
    }
    return $adjacents;
}

function resolveParent(array $stops, string $stopId): string
{
    $current = $stopId; $hops = 0;
    while (isset($stops[$current]['parent_station']) && $stops[$current]['parent_station'] !== '' && $hops < 5) {
        $current = $stops[$current]['parent_station'];
        $hops++;
    }
    return $current;
}

function computeIsMajorHub(array $lines): bool
{
    // Heuristique : ≥3 lignes au total OU au moins 1 RER présent
    return count($lines) >= 3 || hasRer($lines);
}

function hasRer(array $lines): bool
{
    foreach ($lines as $l) if ($l['type'] === 'rer') return true;
    return false;
}

function buildNameFull(string $name, array $lines): string
{
    $metroLines = array_filter($lines, fn($l) => $l['type'] === 'metro');
    $rerLines   = array_filter($lines, fn($l) => $l['type'] === 'rer');
    $parts = [];
    if (!empty($metroLines)) $parts[] = 'Métro ' . implode(', ', array_column($metroLines, 'code'));
    if (!empty($rerLines))   $parts[] = 'RER ' . implode(', ', array_column($rerLines, 'code'));
    return $name . (empty($parts) ? '' : ' (' . implode(' + ', $parts) . ')');
}

function computeTariffZone(array $parent): int
{
    // V1 simple : zone 1 par défaut (Paris intra-muros couvre tous les terminus métro
    // sauf La Défense en zone 3 — détection bbox Paris ~48.815-48.902, 2.224-2.470)
    $lat = (float)$parent['stop_lat'];
    $lon = (float)$parent['stop_lon'];
    if ($lat >= 48.815 && $lat <= 48.902 && $lon >= 2.224 && $lon <= 2.470) return 1;
    return 3; // hors Paris intra-muros (La Défense, terminus banlieue)
}

function fetchWikidataInfo(string $stationName): ?array
{
    // SPARQL : item de type Q928830 (station métro Paris) avec label fr matching
    $query = '
        SELECT ?item ?itemLabel ?wikipediaUrl ?osm WHERE {
          ?item wdt:P31/wdt:P279* wd:Q928830 .
          ?item rdfs:label "' . addcslashes($stationName, '"\\') . '"@fr .
          OPTIONAL { ?wikipediaUrl schema:about ?item ; schema:inLanguage "fr" ;
                                   schema:isPartOf <https://fr.wikipedia.org/> . }
          OPTIONAL { ?item wdt:P402 ?osm . }
          SERVICE wikibase:label { bd:serviceParam wikibase:language "fr". }
        }
        LIMIT 1
    ';
    $url = 'https://query.wikidata.org/sparql?format=json&query=' . rawurlencode($query);

    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 15,
        CURLOPT_HTTPHEADER => ['User-Agent: BougeaParis-Bootstrap/1.0 (https://bougeaparis.fr; ludovic@eoliz.fr)'],
    ]);
    $body = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    if ($code !== 200 || !$body) return null;
    $data = json_decode($body, true);
    $bindings = $data['results']['bindings'][0] ?? null;
    if (!$bindings) return null;

    $qid = '';
    if (!empty($bindings['item']['value']) && preg_match('~/(Q\d+)$~', $bindings['item']['value'], $m)) {
        $qid = $m[1];
    }
    return [
        'qid' => $qid,
        'wikidata_url' => $qid ? "https://www.wikidata.org/wiki/$qid" : null,
        'wikipedia_url' => $bindings['wikipediaUrl']['value'] ?? null,
        'osm_id' => $bindings['osm']['value'] ?? null,
    ];
}

function buildSkeleton(string $slug, array $parent, string $nameFull, array $lines,
                       array $adjacents, bool $isMajorHub, int $tariffZone,
                       ?array $wikidata, array $existing): array
{
    // Garde-fou merge : préserve les champs non-vides de $existing
    $today = date('Y-m-d');
    $skel = [
        '_doc' => $existing['_doc'] ?? "Squelette généré par bootstrap-station.php le $today. Sections A+B auto, sections C en stubs à compléter (humain/LLM).",
        '_todo' => $existing['_todo'] ?? ['seo.description', 'hero', 'intro_paragraphs', 'history', 'faq', 'practical_tips', 'trivia', 'popular_itineraries', 'safety', 'accessibility'],
        'published' => $existing['published'] ?? false,
        'slug' => $slug,
        'name' => $existing['name'] ?? $parent['stop_name'],
        'name_full' => !empty($existing['name_full']) ? $existing['name_full'] : $nameFull,
        'arrondissement' => $existing['arrondissement'] ?? '',
        'address' => $existing['address'] ?? '',
        'latitude' => (float)$parent['stop_lat'],
        'longitude' => (float)$parent['stop_lon'],
        'tariff_zone' => $existing['tariff_zone'] ?? $tariffZone,
        'tariff_zone_context' => $existing['tariff_zone_context'] ?? ($tariffZone === 1 ? 'Paris intra-muros' : 'Hors Paris intra-muros'),
        'commune' => $existing['commune'] ?? ($tariffZone === 1 ? 'Paris' : ''),
        'is_major_hub' => $isMajorHub,
        'i18n' => $existing['i18n'] ?? ['en' => '', 'es' => ''],
        'lines' => $lines,
        'bus_correspondences' => $existing['bus_correspondences'] ?? [
            'diurne' => [], 'nocturne' => [], 'regional' => [],
            '_note' => 'auto: à compléter via RATP SIRI API en V2',
        ],
        'seo' => $existing['seo'] ?? ['description' => ''],
        'hero' => $existing['hero'] ?? ['tagline' => '', 'description' => ''],
        'adjacent_stations' => $adjacents,
        'intro_paragraphs' => mergeStubArray($existing['intro_paragraphs'] ?? null, ['', '', '']),
        'history' => $existing['history'] ?? ['title' => '', 'paragraphs' => ['', '', '']],
        'faq' => mergeStubFaq($existing['faq'] ?? null, 8),
        'practical_tips' => mergeStubArray($existing['practical_tips'] ?? null, ['', '', '', '', '', '']),
        'trivia' => mergeStubTrivia($existing['trivia'] ?? null, 5),
        'popular_itineraries' => $existing['popular_itineraries'] ?? [],
        'nearby_pois' => $existing['nearby_pois'] ?? [],
        'exits' => $existing['exits'] ?? [],
        'services' => $existing['services'] ?? buildServicesStub(),
        'safety' => $existing['safety'] ?? buildSafetyStub(),
        'hero_image' => $existing['hero_image'] ?? null,
        'accessibility' => $existing['accessibility'] ?? buildAccessibilityStub(count($lines)),
    ];

    // Strip private keys
    foreach ($skel['lines'] as &$l) unset($l['_route_id']);

    // Wikidata sameAs (si trouvé)
    if ($wikidata && !empty($wikidata['qid'])) {
        $skel['wikidata'] = [
            'qid' => $wikidata['qid'],
            'wikidata_url' => $wikidata['wikidata_url'],
            'wikipedia_url' => $wikidata['wikipedia_url'],
            'osm_relation_id' => $wikidata['osm_id'],
        ];
    }

    return $skel;
}

function mergeStubArray($existing, array $defaultStub): array
{
    if (!is_array($existing) || empty($existing)) return $defaultStub;
    // Si existant est plus long, on le garde tel quel
    return $existing;
}

function mergeStubFaq($existing, int $count): array
{
    if (is_array($existing) && !empty($existing)) return $existing;
    $faq = [];
    for ($i = 0; $i < $count; $i++) $faq[] = ['question' => '', 'answer' => ''];
    return $faq;
}

function mergeStubTrivia($existing, int $count): array
{
    if (is_array($existing) && !empty($existing)) return $existing;
    $trivia = [];
    for ($i = 0; $i < $count; $i++) $trivia[] = ['icon' => '', 'title' => '', 'content' => ''];
    return $trivia;
}

function buildServicesStub(): array
{
    return [
        'wifi' => ['available' => false, 'location_detail' => '', 'coverage_detail' => ''],
        'toilets' => ['public_paid' => ['available' => false], 'public_free' => ['available' => false, 'location' => '', 'access' => '']],
        'atm' => ['available' => false, 'banks_count_estimate' => '', 'locations' => []],
        'ratp_office' => ['available' => false, 'location' => '', 'services' => ''],
        'left_luggage' => ['ratp_available' => false, 'third_party' => []],
        'shopping_dining' => ['main_location' => '', 'details' => '', 'secondary' => ''],
    ];
}

function buildSafetyStub(): array
{
    return [
        'audit_status' => 'pending',
        'audit_date' => null,
        'level' => '',
        'agents' => null,
        'police' => null,
        'tips' => [],
        'notes' => '',
    ];
}

function buildAccessibilityStub(int $totalLines): array
{
    return [
        'audit_status' => 'pending',
        'audit_date' => null,
        'level' => '',
        'stats' => ['elevators_count' => 0, 'accessible_lines' => 0, 'total_lines' => $totalLines],
        'details' => '',
    ];
}

function timeoutAvailable(): bool
{
    static $checked = null;
    if ($checked !== null) return $checked;
    exec('command -v timeout 2>/dev/null', $out, $code);
    return $checked = ($code === 0 && !empty($out));
}

function runSubprocess(string $slug, string $script, int $timeoutSec, array $extraArgs = []): bool
{
    // build-station-* utilise --station= (pas --slug=). validate-station utilise --slug=.
    $arg = ($script === 'validate-station.php') ? "--slug=$slug" : "--station=$slug";
    $argString = $arg;
    foreach ($extraArgs as $a) $argString .= ' ' . escapeshellarg($a);

    // Le timeout GNU coreutils n'est pas présent par défaut sur macOS dev.
    // Sur CI Ubuntu il est dispo → on l'utilise. Sinon → exécution sans cap
    // (les scripts existants ont leurs propres protections internes).
    $prefix = timeoutAvailable() ? "timeout {$timeoutSec}s " : '';
    $cmd = $prefix . 'php ' . escapeshellarg(__DIR__ . '/' . $script) . ' ' . $argString . ' 2>&1';
    logInfo("  $ $cmd");
    $out = shell_exec($cmd);
    if ($out !== null) {
        // Show condensed output (last 8 lines)
        $lines = array_slice(explode("\n", trim($out)), -8);
        foreach ($lines as $l) if (trim($l) !== '') logInfo("    | $l");
    }
    return $out !== null && !str_contains((string)$out, 'Fatal') && !str_contains((string)$out, 'command not found');
}

function printSummary(string $path, array $json, array $warnings): void
{
    $linesCount = count($json['lines'] ?? []);
    $exitsCount = count($json['exits'] ?? []);
    $poisCount  = count($json['nearby_pois'] ?? []);
    $hasWikidata = !empty($json['wikidata']['qid']);

    echo "\n\n";
    echo "═══════════════════════════════════════════════════════════════\n";
    echo "  ✅ Bootstrap squelette terminé : {$json['slug']}\n";
    echo "═══════════════════════════════════════════════════════════════\n";
    echo "\n";
    echo "Fichier      : $path\n";
    echo "published    : " . ($json['published'] ? 'true (page servable)' : 'false (squelette en review, route 404)') . "\n";
    echo "\n";
    echo "─── Sections A (auto-générées) ───\n";
    echo "  ✓ slug, name, name_full : « {$json['name_full']} »\n";
    echo "  ✓ lat/lon : {$json['latitude']}, {$json['longitude']}\n";
    echo "  ✓ tariff_zone : {$json['tariff_zone']} ({$json['tariff_zone_context']})\n";
    echo "  ✓ is_major_hub : " . ($json['is_major_hub'] ? 'true' : 'false') . "\n";
    echo "  ✓ lines : $linesCount (" . implode(', ', array_column($json['lines'] ?? [], 'code')) . ")\n";
    echo "  ✓ adjacent_stations : " . count($json['adjacent_stations'] ?? []) . " lignes\n";
    if ($hasWikidata) {
        echo "  ✓ wikidata.qid : {$json['wikidata']['qid']} (sameAs SEO)\n";
    } else {
        echo "  ⏳ wikidata.qid : non trouvé (à compléter manuellement si nécessaire)\n";
    }
    echo "\n";
    echo "─── Sections B (sous-process) ───\n";
    echo "  " . ($exitsCount > 0 ? '✓' : '⏳') . " exits : $exitsCount\n";
    echo "  " . ($poisCount > 0 ? '✓' : '⏳') . " nearby_pois : $poisCount\n";
    echo "\n";
    echo "─── Sections C (à compléter) ───\n";
    echo "  ⏳ seo.description, hero (tagline + description)\n";
    echo "  ⏳ intro_paragraphs (3 paragraphes), history (title + 3 paragraphes)\n";
    echo "  ⏳ faq (8 Q/R), trivia (5), practical_tips (6)\n";
    echo "  ⏳ services, safety, accessibility (audits manuels)\n";
    echo "  ⏳ popular_itineraries (à générer en V2 via cross-itineraries script)\n";
    echo "\n";

    if (!empty($warnings)) {
        echo "─── Warnings ───\n";
        foreach ($warnings as $w) echo "  ⚠️  $w\n";
        echo "\n";
    }

    echo "Prochaine étape : compléter sections C (LLM ou manuel), puis :\n";
    echo "  php scripts/diff-station-wikipedia.php --slug={$json['slug']}\n";
    echo "  # Si verdict pass, flipper \"published\": true et git push.\n\n";
}
