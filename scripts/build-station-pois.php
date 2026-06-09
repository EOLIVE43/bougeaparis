<?php
declare(strict_types=1);

error_reporting(E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED);
ini_set('memory_limit', '512M');

/**
 * scripts/build-station-pois.php
 *
 * Genere/met a jour la cle "nearby_pois" dans les JSON station avec un top 10
 * de monuments / sites notables a proximite (rayon 800m).
 *
 * Pipeline :
 *   1. SPARQL Wikidata Query Service : items dans 800m + filtres types + tri
 *      par sitelinks (proxy de notoriete).
 *   2. Dedup par wikidata_id + filter descriptions transport en commun
 *      + dedup par proximite geographique (50m) pour eliminer les doublons
 *      thematiques (ex. "Lutece" colle a "Ile de la Cite", MNAM colle au
 *      Centre Pompidou).
 *   3. Top 10 enrichi avec : Wikipedia summary FR (extract court via REST API),
 *      image Commons (URL Special:FilePath?width=400), categorie heuristique.
 *   4. Pour chaque POI : haversine vers chaque sortie de la station, identifie
 *      la plus proche, calcule walk_minutes (m / 80 m-min, mini 1 min, arrondi).
 *   5. Cache disque scripts/cache-gtfs/wikidata-pois-cache.json par wikidata_id.
 *
 * Format ecrit dans data/stations/{slug}.json sous "nearby_pois" :
 *   [{ wikidata_id, name, category, description, image_url, wikipedia_url,
 *      latitude, longitude, nearest_exit:{number, name, distance_m, walk_minutes} }]
 *
 * Usage :
 *   php scripts/build-station-pois.php --preview --station=chatelet
 *   php scripts/build-station-pois.php --station=chatelet
 *   php scripts/build-station-pois.php
 *
 * @package BougeaParis\Scripts
 */

const ROOT          = __DIR__ . '/..';
const STATIONS_DIR  = ROOT . '/public_html/data/stations';
const POI_CACHE     = __DIR__ . '/cache-gtfs/wikidata-pois-cache.json';
const SECRETS_PHP   = ROOT . '/public_html/config/secrets.php';

const SPARQL_URL    = 'https://query.wikidata.org/sparql';
const WP_SUMMARY_URL = 'https://fr.wikipedia.org/api/rest_v1/page/summary/';
const COMMONS_FILE   = 'https://commons.wikimedia.org/wiki/Special:FilePath/';
const WD_ENTITY_URL  = 'https://www.wikidata.org/wiki/Special:EntityData/';
const ANTHROPIC_URL  = 'https://api.anthropic.com/v1/messages';
const ANTHROPIC_MODEL = 'claude-haiku-4-5-20251001';

const SEARCH_RADIUS_KM    = 0.8;        // rayon SPARQL
const TOP_N               = 12;         // top retenu par station
const MIN_POIS            = 6;          // si moins, on n'ecrit pas (section pas affichee)
const SPARQL_LIMIT        = 40;         // marge pour absorber les dedup
const PROXIMITY_DEDUP_M   = 50;         // 2 POIs a < N m = doublon thematique
const WALK_M_PER_MIN      = 80;         // vitesse pieton parisien
const SPARQL_SLEEP_US     = 250_000;    // 250 ms entre 2 SPARQL (~4 req/s)
const WP_SLEEP_US         = 50_000;     // 50 ms entre 2 wikipedia (~20 req/s)

const USER_AGENT = 'BougeaParis-build-station-pois/1.0 (https://bougeaparis.fr; contact@bougeaparis.fr)';

// Bruit a exclure dans les descriptions Wikidata (transport en commun, etc.)
const NOISE_DESC_REGEX = '/(station du m[ée]tro|ligne du m[ée]tro|station de m[ée]tro|gare RER|station RER|ligne de tramway|arr[êe]t de bus)/iu';

// CLI
$opts = parse_cli_args($argv);
$onlyStation = $opts['station'] ?? null;
$preview     = (bool)($opts['preview'] ?? false);
// v2 : --paraphrase active le post-traitement Claude API sur les descriptions POI
$paraphrase  = (bool)($opts['paraphrase'] ?? false) || in_array('--paraphrase', $argv, true);

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

function haversine_m(float $lat1, float $lon1, float $lat2, float $lon2): float {
    $R = 6371000.0;
    $dLat = deg2rad($lat2 - $lat1);
    $dLon = deg2rad($lon2 - $lon1);
    $a = sin($dLat / 2) ** 2
       + cos(deg2rad($lat1)) * cos(deg2rad($lat2)) * sin($dLon / 2) ** 2;
    return $R * 2 * atan2(sqrt($a), sqrt(1 - $a));
}

function load_cache(): array {
    if (!is_file(POI_CACHE)) return [];
    $raw = @file_get_contents(POI_CACHE);
    $data = $raw !== false ? json_decode($raw, true) : null;
    return is_array($data) ? $data : [];
}

function save_cache(array $cache): void {
    $tmp = POI_CACHE . '.tmp';
    file_put_contents($tmp, pretty_json($cache));
    rename($tmp, POI_CACHE);
}

/** Heuristique de categorisation depuis label + description. */
function categorize(string $label, string $desc): string {
    $s = mb_strtolower($label . ' ' . $desc, 'UTF-8');
    // Ordre IMPORTANT : les regles plus specifiques d'abord pour eviter
    // qu'un mot generique (ex. "ile " dans "ile de la Cite" qui apparait
    // dans la description d'un hopital) capture en premier.
    $rules = [
        'cathédrale'                 => 'cathédrale',
        'basilique'                  => 'basilique',
        'chapelle'                   => 'chapelle',
        'église'                     => 'église',
        'mosquée'                    => 'mosquée',
        'synagogue'                  => 'synagogue',
        'hôpital|hôtel-dieu'         => 'hôpital',
        'mairie|hôtel de ville'      => 'mairie',
        'palais|château'             => 'palais',
        'musée|centre.+art|centre culturel' => 'musée',
        'théâtre|opéra'              => 'théâtre',
        'gare '                      => 'gare',
        'pont|passerelle'            => 'pont',
        'tour '                      => 'tour',
        'place '                     => 'place',
        'jardin|parc '               => 'jardin',
        'magasin|grand magasin'      => 'commerce',
        'librairie'                  => 'librairie',
        'café '                      => 'café',
        'fontaine'                   => 'fontaine',
        'statue'                     => 'statue',
        'île '                       => 'île',
        'cité|cite'                  => 'quartier',
        'monument'                   => 'monument',
    ];
    foreach ($rules as $pattern => $cat) {
        if (preg_match('/' . $pattern . '/u', $s)) return $cat;
    }
    return 'site notable';
}

// ============================================================================
// HTTP / API HELPERS
// ============================================================================

function http_get(string $url, int $timeout = 20): ?string {
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT        => $timeout,
        CURLOPT_CONNECTTIMEOUT => 5,
        CURLOPT_USERAGENT      => USER_AGENT,
        CURLOPT_HTTPHEADER     => ['Accept: application/json'],
        CURLOPT_FOLLOWLOCATION => true,
    ]);
    $resp = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    return ($resp !== false && $code === 200) ? $resp : null;
}

/** Lance la requete SPARQL Wikidata centree sur (lat, lon). */
function sparql_query_around(float $lat, float $lon): array {
    $radius = SEARCH_RADIUS_KM;
    $limit  = SPARQL_LIMIT;
    $q = <<<SPARQL
SELECT DISTINCT ?item ?itemLabel ?itemDescription ?coord ?image ?wparticle ?sitelinks
WHERE {
  SERVICE wikibase:around {
    ?item wdt:P625 ?coord .
    bd:serviceParam wikibase:center "Point($lon $lat)"^^geo:wktLiteral .
    bd:serviceParam wikibase:radius "$radius" .
  }
  VALUES ?type {
    wd:Q33506 wd:Q24354 wd:Q16970 wd:Q174782 wd:Q12280
    wd:Q23413 wd:Q4989906 wd:Q570116 wd:Q1248784 wd:Q839954
    wd:Q1370598 wd:Q41176 wd:Q11303 wd:Q22698 wd:Q3947
  }
  ?item wdt:P31/wdt:P279* ?type .
  ?wparticle schema:about ?item ; schema:isPartOf <https://fr.wikipedia.org/> .
  ?item wikibase:sitelinks ?sitelinks .
  OPTIONAL { ?item wdt:P18 ?image . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "fr,en" . }
}
ORDER BY DESC(?sitelinks)
LIMIT $limit
SPARQL;

    $ch = curl_init(SPARQL_URL . '?query=' . urlencode($q));
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT        => 30,
        CURLOPT_CONNECTTIMEOUT => 5,
        CURLOPT_USERAGENT      => USER_AGENT,
        CURLOPT_HTTPHEADER     => ['Accept: application/sparql-results+json'],
    ]);
    $resp = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    usleep(SPARQL_SLEEP_US);
    if ($resp === false || $code !== 200) {
        log_info("  SPARQL HTTP $code, abandon pour cette station");
        return [];
    }
    $data = json_decode($resp, true);
    return $data['results']['bindings'] ?? [];
}

/** Fetch summary FR depuis Wikipedia REST API par titre. */
/** Charge la cle ANTHROPIC_API_KEY depuis secrets.php. */
function load_anthropic_key(): string {
    if (!is_file(SECRETS_PHP)) {
        fwrite(STDERR, "[ERREUR] secrets.php absent : " . SECRETS_PHP . "\n");
        exit(2);
    }
    $secrets = require SECRETS_PHP;
    $key = $secrets['ANTHROPIC_API_KEY'] ?? null;
    if (!$key || str_starts_with($key, 'sk-ant-api03-COLLER')) {
        fwrite(STDERR, "[ERREUR] ANTHROPIC_API_KEY manquant dans secrets.php\n");
        exit(2);
    }
    return $key;
}

/**
 * Wikidata Entities API : recupere quelques claims utiles pour enrichir
 * la description d'un POI (architect P84, inception P571, instance of P31,
 * heritage status P1435, height P2048, area P2046).
 * Retourne un tableau text-friendly de faits.
 */
function fetch_wikidata_facts(string $qid): array {
    $url = WD_ENTITY_URL . $qid . '.json';
    $resp = http_get($url, 10);
    if ($resp === null) return [];
    $d = json_decode($resp, true);
    $entity = $d['entities'][$qid] ?? null;
    if (!$entity) return [];
    $claims = $entity['claims'] ?? [];
    $facts = [];

    // P31 instance of (label si dispo en FR)
    $p31_labels = wd_resolve_qids_to_labels(wd_claim_qids($claims, 'P31'));
    if ($p31_labels) $facts['type'] = implode(', ', array_slice($p31_labels, 0, 3));

    // P571 inception (date de creation)
    $p571 = wd_claim_time($claims, 'P571');
    if ($p571) $facts['inception'] = $p571;

    // P84 architect (label)
    $p84_labels = wd_resolve_qids_to_labels(wd_claim_qids($claims, 'P84'));
    if ($p84_labels) $facts['architect'] = implode(', ', array_slice($p84_labels, 0, 3));

    // P170 creator
    $p170_labels = wd_resolve_qids_to_labels(wd_claim_qids($claims, 'P170'));
    if ($p170_labels) $facts['creator'] = implode(', ', array_slice($p170_labels, 0, 2));

    // P1435 heritage status (Monument Historique etc.)
    $p1435_labels = wd_resolve_qids_to_labels(wd_claim_qids($claims, 'P1435'));
    if ($p1435_labels) $facts['heritage'] = implode(', ', array_slice($p1435_labels, 0, 2));

    // P2048 height (Q-units, on garde l'amount)
    $p2048 = wd_claim_quantity($claims, 'P2048');
    if ($p2048) $facts['height'] = $p2048;

    // P2046 area
    $p2046 = wd_claim_quantity($claims, 'P2046');
    if ($p2046) $facts['area'] = $p2046;

    return $facts;
}

/** Extrait les QIDs d'une claim donnee (ex P84 -> [Q123, Q456]). */
function wd_claim_qids(array $claims, string $prop): array {
    $qids = [];
    foreach ($claims[$prop] ?? [] as $c) {
        $id = $c['mainsnak']['datavalue']['value']['id'] ?? null;
        if ($id) $qids[] = $id;
    }
    return $qids;
}

/** Extrait une date d'une claim (P571 inception, time format Wikidata). */
function wd_claim_time(array $claims, string $prop): ?string {
    foreach ($claims[$prop] ?? [] as $c) {
        $time = $c['mainsnak']['datavalue']['value']['time'] ?? null;
        if ($time) {
            // Format +YYYY-MM-DDTHH:MM:SSZ -> on garde l'annee
            if (preg_match('/^[+\-](\d{1,4})/', $time, $m)) {
                return $m[1];
            }
        }
    }
    return null;
}

/** Extrait une quantite (P2048 height, P2046 area). */
function wd_claim_quantity(array $claims, string $prop): ?string {
    foreach ($claims[$prop] ?? [] as $c) {
        $val = $c['mainsnak']['datavalue']['value'] ?? null;
        if (isset($val['amount'])) {
            $amount = ltrim($val['amount'], '+');
            return $amount;
        }
    }
    return null;
}

/** Resout des QIDs en labels FR via SPARQL (batch jusqu'a 20 QIDs). */
function wd_resolve_qids_to_labels(array $qids): array {
    if (empty($qids)) return [];
    $qids = array_slice(array_unique($qids), 0, 20);
    $values = implode(' ', array_map(fn($q) => "wd:$q", $qids));
    $query = "SELECT ?id ?label WHERE { VALUES ?id { $values } ?id rdfs:label ?label . FILTER(LANG(?label) = \"fr\") }";
    $url = SPARQL_URL . '?query=' . urlencode($query) . '&format=json';
    $resp = http_get($url, 10);
    usleep(SPARQL_SLEEP_US);
    if ($resp === null) return [];
    $d = json_decode($resp, true);
    $out = [];
    foreach ($d['results']['bindings'] ?? [] as $b) {
        $label = $b['label']['value'] ?? null;
        if ($label) $out[] = $label;
    }
    return $out;
}

/**
 * Appelle l'API Anthropic Messages pour paraphraser un POI.
 * Retourne la description originale (50-80 mots) ou null si erreur.
 */
function call_anthropic_paraphrase(string $apiKey, string $poiName, ?string $wikipediaExtract, array $wdFacts, string $stationName, ?int $distanceM): ?string {
    $factsLines = [];
    foreach ($wdFacts as $k => $v) $factsLines[] = "- $k : $v";
    $factsBlock = $factsLines ? implode("\n", $factsLines) : "(aucun fait Wikidata structuré disponible)";
    $extractBlock = $wikipediaExtract ?: '(pas d\'extrait Wikipedia disponible)';
    $distanceTxt = $distanceM ? "Distance station : ~{$distanceM} m" : "";

    $prompt = <<<PROMPT
Tu rédiges des descriptions de POI pour un guide transport parisien (bougeaparis.fr).

POI à décrire : **{$poiName}**
Station de référence : {$stationName}
{$distanceTxt}

EXTRAIT WIKIPEDIA FR (source factuelle — NE PAS RECOPIER) :
{$extractBlock}

FAITS WIKIDATA STRUCTURÉS :
{$factsBlock}

CONSIGNES STRICTES :
1. Rédige 2 phrases originales, 40-70 mots au total.
2. INTERDIT : reprendre verbatim plus de 4 mots consécutifs de l'extrait Wikipedia.
3. Zéro invention : tout fait doit être sourcé ci-dessus.
4. Croiser au moins 2 angles (date + créateur, type + dimensions, etc.) si possible.
5. Ton informatif sobre, pas de superlatif gratuit ("incroyable", "magnifique").
6. Ne commence PAS par "C'est un/une X" (formule scolaire).
7. Pas de référence explicite à Wikipedia ni à la station ("à proximité de la station…" interdit).

RÉPONDS UNIQUEMENT avec le texte de la description, sans préambule, sans guillemets.
PROMPT;

    $payload = [
        'model'      => ANTHROPIC_MODEL,
        'max_tokens' => 300,
        'messages'   => [
            ['role' => 'user', 'content' => $prompt],
        ],
    ];

    $ch = curl_init(ANTHROPIC_URL);
    curl_setopt_array($ch, [
        CURLOPT_POST           => true,
        CURLOPT_POSTFIELDS     => json_encode($payload),
        CURLOPT_HTTPHEADER     => [
            'Content-Type: application/json',
            'x-api-key: ' . $apiKey,
            'anthropic-version: 2023-06-01',
        ],
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT        => 30,
        CURLOPT_USERAGENT      => USER_AGENT,
    ]);
    $resp = curl_exec($ch);
    $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($code !== 200) {
        log_info("    Anthropic HTTP $code");
        return null;
    }
    $d = json_decode($resp, true);
    $content = $d['content'][0]['text'] ?? null;
    if (!$content) return null;
    $content = trim($content);
    // Nettoyage : retirer eventuels guillemets autour
    $content = trim($content, "\"'« »");
    // Trace usage tokens si dispo
    $usage = $d['usage'] ?? null;
    if ($usage) {
        $GLOBALS['CLAUDE_INPUT_TOKENS']  = ($GLOBALS['CLAUDE_INPUT_TOKENS']  ?? 0) + ($usage['input_tokens']  ?? 0);
        $GLOBALS['CLAUDE_OUTPUT_TOKENS'] = ($GLOBALS['CLAUDE_OUTPUT_TOKENS'] ?? 0) + ($usage['output_tokens'] ?? 0);
        $GLOBALS['CLAUDE_CALLS']         = ($GLOBALS['CLAUDE_CALLS']         ?? 0) + 1;
    }
    return $content;
}

function wikipedia_summary(string $title): ?array {
    $url = WP_SUMMARY_URL . rawurlencode($title);
    $resp = http_get($url, 10);
    usleep(WP_SLEEP_US);
    if ($resp === null) return null;
    $d = json_decode($resp, true);
    return [
        'extract'   => $d['extract']  ?? null,
        'thumbnail' => $d['thumbnail']['source'] ?? null,
    ];
}

/** Construit l'URL Commons dimensionnee a 400px depuis l'URL P18 brute. */
function commons_thumb_url(?string $rawImage): ?string {
    if (!$rawImage) return null;
    // Format brut : http://commons.wikimedia.org/wiki/Special:FilePath/<filename>
    if (preg_match('#Special:FilePath/(.+)$#', $rawImage, $m)) {
        $filename = rawurldecode($m[1]);
        return COMMONS_FILE . rawurlencode($filename) . '?width=400';
    }
    return $rawImage;
}

/** Convertit un wparticle URL (https://fr.wikipedia.org/wiki/Title) en titre decode. */
function wikipedia_title_from_url(string $url): ?string {
    if (preg_match('#fr\.wikipedia\.org/wiki/(.+)$#', $url, $m)) {
        return rawurldecode(str_replace('_', ' ', $m[1]));
    }
    return null;
}

// ============================================================================
// SELECTION TOP N (dedup id + filter desc + dedup proximite)
// ============================================================================

function select_top_pois(array $bindings, int $topN): array {
    $seen = [];
    $rows = [];
    foreach ($bindings as $b) {
        if (!isset($b['item'], $b['coord'])) continue;
        $id = basename($b['item']['value']);
        if (isset($seen[$id])) continue;
        $seen[$id] = true;
        if (!preg_match('/Point\(([\d.\-]+) ([\d.\-]+)\)/', $b['coord']['value'], $m)) continue;
        $b['_lat'] = (float)$m[2];
        $b['_lon'] = (float)$m[1];
        $rows[] = $b;
    }
    // Filter noise descriptions
    $rows = array_values(array_filter($rows, function ($b) {
        $desc = $b['itemDescription']['value'] ?? '';
        return !preg_match(NOISE_DESC_REGEX, $desc);
    }));
    // Proximity dedup : ordre actuel = sitelinks DESC (du SPARQL), garder le 1er
    $kept = [];
    foreach ($rows as $r) {
        $isDup = false;
        foreach ($kept as $k) {
            if (haversine_m($r['_lat'], $r['_lon'], $k['_lat'], $k['_lon']) < PROXIMITY_DEDUP_M) {
                $isDup = true;
                break;
            }
        }
        if (!$isDup) $kept[] = $r;
        if (count($kept) >= $topN) break;
    }
    return $kept;
}

// ============================================================================
// MATCHING SORTIE LA PLUS PROCHE
// ============================================================================

function find_nearest_exit(float $poiLat, float $poiLon, array $exits): ?array {
    $best = null;
    foreach ($exits as $exit) {
        $eLat = $exit['latitude']  ?? null;
        $eLon = $exit['longitude'] ?? null;
        if ($eLat === null || $eLon === null) continue;
        $d = haversine_m((float)$eLat, (float)$eLon, $poiLat, $poiLon);
        if ($best === null || $d < $best['distance_m']) {
            $best = [
                'number'        => (string)($exit['number'] ?? ''),
                'name'          => (string)($exit['name'] ?? ''),
                'distance_m'    => (int) round($d),
                'walk_minutes'  => max(1, (int) round($d / WALK_M_PER_MIN)),
            ];
        }
    }
    return $best;
}

// ============================================================================
// ENRICHISSEMENT POI (Wikipedia summary + image)
// ============================================================================

function enrich_poi(array $b, array &$cache, int &$apiCalls): array {
    $id   = basename($b['item']['value']);
    $name = $b['itemLabel']['value']      ?? '';
    $desc = $b['itemDescription']['value'] ?? '';
    $sl   = (int)($b['sitelinks']['value'] ?? 0);
    $rawImage = $b['image']['value'] ?? null;
    $wpurl    = $b['wparticle']['value'] ?? null;
    $wpTitle  = $wpurl ? wikipedia_title_from_url($wpurl) : null;

    // Cache hit : on retourne mais on RECALCULE la category dynamiquement
    // (les regles heuristiques peuvent evoluer entre 2 versions du script,
    // on ne veut pas un cache stale sur ce champ).
    if (isset($cache[$id]) && !empty($cache[$id]['wikipedia_extract'])) {
        $entry = $cache[$id];
        $entry['category'] = categorize($entry['name'] ?? '', $entry['description'] ?? '');
        $cache[$id] = $entry; // re-persist la nouvelle category
        return $entry;
    }

    $extract = null; $thumbUrl = null;
    if ($wpTitle) {
        $apiCalls++;
        $sum = wikipedia_summary($wpTitle);
        if ($sum) {
            $extract = $sum['extract']  ?? null;
            $thumbUrl = $sum['thumbnail'] ?? null;
        }
    }

    $entry = [
        'wikidata_id'       => $id,
        'name'              => $name,
        'description'       => $desc,
        'category'          => categorize($name, $desc),
        'latitude'          => round($b['_lat'], 6),
        'longitude'         => round($b['_lon'], 6),
        'image_url'         => commons_thumb_url($rawImage) ?? $thumbUrl,
        'wikipedia_url'     => $wpurl,
        'wikipedia_title'   => $wpTitle,
        'wikipedia_extract' => $extract,
        'sitelinks'         => $sl,
        'fetched_at'        => date('c'),
    ];
    $cache[$id] = $entry;
    return $entry;
}

/**
 * v2 : pour un POI (entry cache), appelle Claude pour paraphraser le wikipedia_extract.
 * Stocke le resultat dans $entry['description_paraphrased'] + cache.
 * Si deja fait, retourne tel quel (idempotent).
 * Retourne $entry mis a jour.
 */
function paraphrase_poi(array $entry, string $apiKey, string $stationName, ?int $distanceM, array &$cache): array {
    $id = $entry['wikidata_id'] ?? null;
    if (!$id) return $entry;

    // Cache hit
    if (!empty($entry['description_paraphrased'])) return $entry;

    $extract = $entry['wikipedia_extract'] ?? null;
    if (!$extract) return $entry; // pas d'extract = on garde la description Wikidata courte (deja non verbatim)

    // Fetch Wikidata facts (P31, P571, P84, etc.)
    $wdFacts = fetch_wikidata_facts($id);
    usleep(SPARQL_SLEEP_US);

    // Appel Claude
    $name = $entry['name'] ?? '?';
    $paraphrase = call_anthropic_paraphrase($apiKey, $name, $extract, $wdFacts, $stationName, $distanceM);
    if (!$paraphrase) {
        log_info("    Claude paraphrase failed pour $name ($id) — skip");
        return $entry;
    }

    $entry['description_paraphrased'] = $paraphrase;
    $entry['wikidata_facts']          = $wdFacts;
    $entry['paraphrased_at']          = date('c');
    $cache[$id] = $entry;
    return $entry;
}

/** Tronque un extract Wikipedia a ~150 chars sur une frontiere de phrase si possible. */
function truncate_extract(?string $extract, int $maxChars = 200): ?string {
    if ($extract === null) return null;
    $extract = trim($extract);
    if (mb_strlen($extract) <= $maxChars) return $extract;
    $cut = mb_substr($extract, 0, $maxChars);
    // Coupe a la derniere phrase complete si presente
    if (preg_match('/^(.+?[\.\!\?])\s/u', $cut, $m)) {
        return $m[1];
    }
    // Sinon coupe au dernier espace
    $lastSpace = mb_strrpos($cut, ' ');
    if ($lastSpace !== false) {
        return mb_substr($cut, 0, $lastSpace) . '…';
    }
    return $cut . '…';
}

// ============================================================================
// CONSTRUCTION DU NEARBY_POIS POUR UNE STATION
// ============================================================================

function build_nearby_pois(array $stationJson, array &$cache, int &$apiCalls, ?string $apiKey = null, bool $paraphrase = false): array {
    $info = ['count' => 0, 'pois' => []];
    $lat = $stationJson['latitude']  ?? null;
    $lon = $stationJson['longitude'] ?? null;
    $exits = $stationJson['exits']    ?? [];
    $stationName = $stationJson['name_full'] ?? $stationJson['name'] ?? '?';
    if ($lat === null || $lon === null) {
        log_info("  station sans lat/lon, skip");
        return $info;
    }

    $bindings = sparql_query_around((float)$lat, (float)$lon);
    if (empty($bindings)) {
        log_info("  SPARQL retourne 0 resultats");
        return $info;
    }
    log_info(sprintf('  SPARQL : %d bruts', count($bindings)));

    $top = select_top_pois($bindings, TOP_N);
    log_info(sprintf('  Apres dedup id+description+proximite (50m) : %d', count($top)));

    // Fallback : si moins de MIN_POIS POIs apres filtrage, on n'ecrit pas la
    // section (la station n'a pas assez de richesse touristique notable).
    if (count($top) < MIN_POIS) {
        log_info(sprintf('  < %d POIs (MIN_POIS), section non emise', MIN_POIS));
        return $info;
    }

    $pois = [];
    foreach ($top as $b) {
        $entry = enrich_poi($b, $cache, $apiCalls);
        $nearestExit = find_nearest_exit($entry['latitude'], $entry['longitude'], $exits);
        $distanceM = $nearestExit['distance_m'] ?? null;
        // v2 : paraphrase Claude si flag actif
        if ($paraphrase && $apiKey) {
            $entry = paraphrase_poi($entry, $apiKey, $stationName, $distanceM, $cache);
        }
        // Priorite : description_paraphrased > truncate_extract > Wikidata desc courte
        $description = $entry['description_paraphrased']
            ?? truncate_extract($entry['wikipedia_extract'])
            ?? $entry['description'];
        $pois[] = [
            'wikidata_id'   => $entry['wikidata_id'],
            'name'          => $entry['name'],
            'category'      => $entry['category'],
            'description'   => $description,
            'image_url'     => $entry['image_url'],
            'wikipedia_url' => $entry['wikipedia_url'],
            'latitude'      => $entry['latitude'],
            'longitude'     => $entry['longitude'],
            'nearest_exit'  => $nearestExit,
        ];
    }
    $info['count'] = count($pois);
    $info['pois']  = $pois;
    return $info;
}

// ============================================================================
// MAIN
// ============================================================================

log_info('Phase 1: chargement cache POI');
$cache = load_cache();
log_info(sprintf('  %d POIs deja en cache', count($cache)));
$apiCalls = 0;

// v2 : charger la cle Anthropic si paraphrase actif
$apiKey = null;
if ($paraphrase) {
    $apiKey = load_anthropic_key();
    log_info('  Mode --paraphrase active : Claude API ' . ANTHROPIC_MODEL);
}

log_info('Phase 2: iteration data/stations/*.json');
$files = glob(STATIONS_DIR . '/*.json');
if ($onlyStation) {
    $files = array_filter($files, fn($f) => basename($f, '.json') === $onlyStation);
    if (empty($files)) {
        fwrite(STDERR, "[ERREUR] Aucun fichier data/stations/$onlyStation.json\n");
        exit(1);
    }
}
$wroteCount = 0; $skipCount = 0;

foreach ($files as $path) {
    $slug = basename($path, '.json');
    $json = json_decode(file_get_contents($path), true);
    if (!is_array($json)) { log_info("  $slug : JSON invalide, skip"); $skipCount++; continue; }

    log_info("  $slug : SPARQL en cours...");
    $info = build_nearby_pois($json, $cache, $apiCalls, $apiKey ?? null, $paraphrase);

    if ($preview) {
        echo "\n############################################################\n";
        echo "# PREVIEW : $slug\n";
        echo "############################################################\n";
        echo "  POIs trouves : {$info['count']}\n";
        echo "  --- Top liste ---\n";
        foreach ($info['pois'] as $i => $p) {
            $exit = $p['nearest_exit'] ?? null;
            $exitInfo = $exit ? sprintf('Sortie %s "%s" (%dm, %d min)',
                $exit['number'] ?: '?',
                mb_strimwidth($exit['name'], 0, 22, '...'),
                $exit['distance_m'], $exit['walk_minutes']) : '-';
            printf("    %2d. %-32s [%-15s] %s\n",
                $i+1,
                mb_strimwidth($p['name'], 0, 30, '...'),
                $p['category'],
                $exitInfo);
        }
        echo "  --- Detail top 5 ---\n";
        foreach (array_slice($info['pois'], 0, 5) as $i => $p) {
            echo "  [" . ($i+1) . "] " . $p['name'] . " (" . $p['wikidata_id'] . ", " . $p['category'] . ")\n";
            echo "      " . mb_strimwidth($p['description'] ?? '', 0, 140, '...') . "\n";
            echo "      Image: " . ($p['image_url'] ?? '(pas d\'image)') . "\n";
            echo "      Wiki:  " . ($p['wikipedia_url'] ?? '?') . "\n";
            if ($p['nearest_exit']) {
                printf("      Sortie %s « %s » : %dm, %d min a pied\n",
                    $p['nearest_exit']['number'],
                    $p['nearest_exit']['name'],
                    $p['nearest_exit']['distance_m'],
                    $p['nearest_exit']['walk_minutes']);
            }
        }
        continue;
    }

    if ($info['count'] === 0) {
        log_info("  $slug : 0 POI, skip");
        $skipCount++;
        continue;
    }

    // Preserver overrides manuels (is_featured, hidden, etc.) si existant
    $existing = $json['nearby_pois'] ?? [];
    if (is_array($existing) && !empty($existing)) {
        $byId = [];
        foreach ($existing as $e) {
            if (isset($e['wikidata_id'])) $byId[$e['wikidata_id']] = $e;
        }
        foreach ($info['pois'] as &$p) {
            $oid = $p['wikidata_id'] ?? null;
            if ($oid && isset($byId[$oid])) {
                foreach (['is_featured', 'is_hidden', 'editorial_note'] as $editKey) {
                    if (isset($byId[$oid][$editKey])) {
                        $p[$editKey] = $byId[$oid][$editKey];
                    }
                }
            }
        }
        unset($p);
    }

    $json['nearby_pois'] = $info['pois'];
    file_put_contents($path, pretty_json($json) . "\n");
    log_info("  $slug : " . count($info['pois']) . " POIs ecrits");
    $wroteCount++;
}

save_cache($cache);
log_info(sprintf('Cache POIs sauvegarde : %d entrees totales (%d nouveaux fetchs Wikipedia cette run)',
    count($cache), $apiCalls));

// v2 : recap usage Claude
if ($paraphrase) {
    $calls = $GLOBALS['CLAUDE_CALLS'] ?? 0;
    $inT   = $GLOBALS['CLAUDE_INPUT_TOKENS'] ?? 0;
    $outT  = $GLOBALS['CLAUDE_OUTPUT_TOKENS'] ?? 0;
    // Pricing Haiku 4.5 : input ~$1/M, output ~$5/M (Anthropic console)
    $cost  = ($inT * 1.0 + $outT * 5.0) / 1_000_000;
    log_info(sprintf('Claude API : %d appels, %d input tokens, %d output tokens, ~$%.4f total',
        $calls, $inT, $outT, $cost));
}

if ($preview) {
    log_info('Preview terminee. Aucun fichier ecrit.');
} else {
    log_info("Termine : $wroteCount fichier(s) ecrit(s), $skipCount skip(s).");
}
