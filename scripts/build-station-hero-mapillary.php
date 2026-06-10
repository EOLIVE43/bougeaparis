#!/usr/bin/env php
<?php
declare(strict_types=1);
error_reporting(E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED);

/**
 * Pipeline hero hybride Mapillary > OSM fallback.
 *
 * Strategie :
 *  1. Query Mapillary Graph API v4 (bbox 100m autour GPS station)
 *  2. Filtre is_pano=false + thumb_2048_url present
 *  3. Tri par distance (plus proche d'abord)
 *  4. Si >=1 candidat valide : download thumb_2048 + crop central 16:9
 *  5. Si 0 candidat : fallback OSM staticmap (maps.wikimedia.org) +
 *     marker rouge teardrop centre
 *  6. Genere 12 variantes AVIF/WebP/JPG x 4 tailles via sips/cwebp/avifenc
 *  7. Update JSON station (hero_image)
 *
 * Usage : php scripts/build-station-hero-mapillary.php --station=<slug>
 *
 * Sortie JSON sur stdout pour permettre agregation/log par le caller.
 */

const RADII_M        = [50, 100]; // escalade adaptative (abandon 200m apres v3)
const MIN_YEAR       = 2018;      // filtre captured_at
const HERO_WIDTHS    = [400, 800, 1200, 1600];
const HERO_RATIO_W   = 16;
const HERO_RATIO_H   = 9;
const WIKIMEDIA_MIN_W = 1200;     // largeur min image Wikimedia POI
const WIKIMEDIA_MAX_POI_TRIES = 5;

const ROOT_DIR       = __DIR__ . '/..';
const STATIONS_DIR   = ROOT_DIR . '/public_html/data/stations';
const IMG_DIR        = ROOT_DIR . '/public_html/assets/img/stations';
const SECRETS_PHP    = ROOT_DIR . '/public_html/config/secrets.php';

const SIPS           = '/usr/bin/sips';
const CWEBP          = '/opt/homebrew/bin/cwebp';
const AVIFENC        = '/opt/homebrew/bin/avifenc';

const TODAY          = '2026-06-10';
const USER_AGENT     = 'BougeaParisBot/1.0 (https://bougeaparis.fr; ludovic@eoliz.fr)';

// v9 : Vision API constants (validation visuelle de candidates heros)
const ANTHROPIC_URL   = 'https://api.anthropic.com/v1/messages';
const VISION_MODEL    = 'claude-sonnet-4-6';
const VISION_COST_USD = 0.012; // approx coût moyen / image (Sonnet 4.6 vision)
const VISION_LOG      = '/tmp/vision-validations.log';

// ------------------------------------------------------------------
// Helpers
// ------------------------------------------------------------------

function parse_args(array $argv): array {
    $args = [];
    foreach ($argv as $a) {
        if (preg_match('/^--([^=]+)=(.*)$/', $a, $m)) $args[$m[1]] = $m[2];
    }
    return $args;
}

/**
 * v9 : Validation visuelle d'une candidate hero via Claude Vision API.
 *
 * Critère : la photo doit permettre d'identifier visuellement la station
 * précise (extérieur OU intérieur avec nom visible OU décoration iconique).
 *
 * Rejets : escalier sans nom, couloir générique, photo floue, panneau macro,
 * grille hors-sujet, personnes au premier plan dominantes.
 *
 * Retour : ['valid' => bool, 'subject' => string, 'identifies' => bool,
 *          'reason' => string, 'cost_usd' => float].
 *
 * Coût ~$0.012/appel (Sonnet 4.6 + image 1600px).
 */
function validate_hero_with_vision(string $localPath, string $stationName, string $apiKey): array {
    if (!is_file($localPath)) {
        return ['valid' => false, 'subject' => 'unknown', 'identifies' => false,
                'reason' => 'file_not_found', 'cost_usd' => 0.0];
    }
    $imgData = @file_get_contents($localPath);
    if (!$imgData) {
        return ['valid' => false, 'subject' => 'unknown', 'identifies' => false,
                'reason' => 'fetch_failed', 'cost_usd' => 0.0];
    }
    // Detection media_type (JPEG/PNG via magic bytes)
    $mediaType = 'image/jpeg';
    if (strncmp($imgData, "\x89PNG", 4) === 0) $mediaType = 'image/png';
    $base64 = base64_encode($imgData);

    $prompt = "Tu valides une photo pour la fiche de la station de métro parisien '{$stationName}'.\n\n"
        . "OBJECTIF : la photo doit permettre au lecteur d'identifier visuellement la station '{$stationName}' (et pas une autre).\n\n"
        . "✅ ACCEPTABLES :\n"
        . "1. Photo nette\n"
        . "2. Vue extérieure (rue, place, façade, édicule) avec contexte urbain reconnaissable\n"
        . "3. Édicule métro visible (Guimard, totem, escalier extérieur)\n"
        . "4. Quartier/monument iconique identifiable (Mairie, église, parc, pont, etc.)\n"
        . "5. INTÉRIEUR DE STATION SI le nom '{$stationName}' est VISIBLE sur les murs (carrelage métro, lettrage en faïence émaillée)\n"
        . "6. INTÉRIEUR SI décoration architecturale unique reconnaissable (ex: Arts et Métiers cuivre Nautilus, fresques thématiques)\n\n"
        . "❌ REJETÉES :\n"
        . "1. Photo floue\n"
        . "2. Escalier intérieur sans nom de station visible\n"
        . "3. Couloir générique sans identification\n"
        . "4. Quai/rame/wagon (pas identifiable)\n"
        . "5. Panneau directionnel macro sans contexte\n"
        . "6. Personnes au premier plan dominantes\n"
        . "7. Grille/clôture sans intérêt\n"
        . "8. Vue trop générique (pourrait être n'importe quelle rue/station)\n\n"
        . "Réponds STRICTEMENT en JSON valide, sans préambule :\n"
        . '{"valid": true|false, "subject": "Façade"|"Bouche métro"|"Édicule Guimard"|"Intérieur avec nom"|"Décoration iconique"|"Quartier identifiable"|"Escalier sans nom"|"Couloir générique"|"Quai/rame"|"Macro"|"Floue"|"Personnes"|"Grille"|"Générique"|"Autre", "identifies_station": true|false, "reason": "explication brève 1 phrase"}';

    $payload = [
        'model'      => VISION_MODEL,
        'max_tokens' => 300,
        'messages'   => [[
            'role'    => 'user',
            'content' => [
                ['type' => 'image', 'source' => [
                    'type' => 'base64', 'media_type' => $mediaType, 'data' => $base64,
                ]],
                ['type' => 'text', 'text' => $prompt],
            ],
        ]],
    ];

    $ch = curl_init(ANTHROPIC_URL);
    curl_setopt_array($ch, [
        CURLOPT_POST           => true,
        CURLOPT_HTTPHEADER     => [
            'x-api-key: ' . $apiKey,
            'anthropic-version: 2023-06-01',
            'content-type: application/json',
        ],
        CURLOPT_POSTFIELDS     => json_encode($payload),
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT        => 45,
    ]);
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($httpCode !== 200) {
        return ['valid' => false, 'subject' => 'unknown', 'identifies' => false,
                'reason' => "api_error_$httpCode", 'cost_usd' => 0.0];
    }
    $data = json_decode($response, true);
    $text = $data['content'][0]['text'] ?? '{}';
    // Parser le JSON même si entouré de ```json ... ```
    if (preg_match('/\{[^{}]*\}/s', $text, $matches)) {
        $parsed = json_decode($matches[0], true) ?: [];
    } else {
        $parsed = [];
    }
    return [
        'valid'      => (bool)($parsed['valid'] ?? false),
        'subject'    => $parsed['subject'] ?? 'unknown',
        'identifies' => (bool)($parsed['identifies_station'] ?? false),
        'reason'     => $parsed['reason'] ?? '',
        'cost_usd'   => VISION_COST_USD,
    ];
}

/** v9 : Log validation dans /tmp/vision-validations.log. */
function vision_log(string $slug, string $candidateSrc, array $result): void {
    $line = sprintf("[%s] %s | %s | valid=%s identifies=%s subject=%s | %s\n",
        date('H:i:s'), $slug, basename($candidateSrc),
        $result['valid'] ? 'YES' : 'NO',
        $result['identifies'] ? 'YES' : 'NO',
        $result['subject'], $result['reason']
    );
    @file_put_contents(VISION_LOG, $line, FILE_APPEND);
}

function fail(string $msg): void {
    fwrite(STDERR, "ERR: $msg\n");
    exit(1);
}

function load_secrets(): array {
    if (!is_file(SECRETS_PHP)) fail('secrets.php absent');
    return require SECRETS_PHP;
}

function load_station(string $slug): array {
    $path = STATIONS_DIR . "/$slug.json";
    if (!is_file($path)) fail("station JSON absent : $path");
    $raw = file_get_contents($path);
    $data = json_decode($raw, true);
    if (!is_array($data)) fail("station JSON malforme : $path");
    return $data;
}

function save_station(string $slug, array $data): void {
    $path = STATIONS_DIR . "/$slug.json";
    $json = json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    file_put_contents($path, $json . "\n");
}

function distance_m(float $lat1, float $lon1, float $lat2, float $lon2): float {
    $R = 6371000.0;
    $dlat = deg2rad($lat2 - $lat1);
    $dlon = deg2rad($lon2 - $lon1);
    $a = sin($dlat/2) ** 2 + cos(deg2rad($lat1)) * cos(deg2rad($lat2)) * sin($dlon/2) ** 2;
    return 2 * $R * asin(sqrt($a));
}

function http_get(string $url, string $accept = 'application/json'): array {
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_TIMEOUT        => 30,
        CURLOPT_USERAGENT      => USER_AGENT,
        CURLOPT_HTTPHEADER     => ["Accept: $accept"],
    ]);
    $body = curl_exec($ch);
    $code = (int)curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    return [$code, $body === false ? '' : $body];
}

function http_download(string $url, string $dest): bool {
    // v6 : retry 429 (Wikimedia rate-limit aggressive sur originaux 4K+)
    $attempts = 3;
    for ($i = 0; $i < $attempts; $i++) {
        $fp = fopen($dest, 'w');
        if (!$fp) return false;
        $ch = curl_init($url);
        curl_setopt_array($ch, [
            CURLOPT_FILE           => $fp,
            CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_TIMEOUT        => 60,
            CURLOPT_USERAGENT      => USER_AGENT,
        ]);
        $ok = curl_exec($ch);
        $code = (int)curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        fclose($fp);
        if ($ok && $code === 200 && is_file($dest) && filesize($dest) >= 1024) {
            return true;
        }
        @unlink($dest);
        if ($code === 429 && $i < $attempts - 1) {
            sleep(15 * ($i + 1));
            continue;
        }
        break;
    }
    return false;
}

// ------------------------------------------------------------------
// Mapillary
// ------------------------------------------------------------------

function query_mapillary(string $token, float $lat, float $lon, int $radius_m): array {
    // bbox approximatif a partir du radius (Paris : 1 deg lat ~111km, 1 deg lon ~73km)
    $dlat = $radius_m / 111000.0;
    $dlon = $radius_m / 73000.0;
    $w = $lon - $dlon; $s = $lat - $dlat;
    $e = $lon + $dlon; $n = $lat + $dlat;

    $params = http_build_query([
        'access_token' => $token,
        'fields'       => 'id,thumb_2048_url,thumb_1024_url,is_pano,captured_at,compass_angle,creator,geometry',
        'bbox'         => "$w,$s,$e,$n",
        'limit'        => 100,
    ]);
    [$code, $body] = http_get("https://graph.mapillary.com/images?$params");
    if ($code !== 200) return [];
    $d = json_decode($body, true);
    return $d['data'] ?? [];
}

function pick_best_mapillary(array $images, float $lat, float $lon): ?array {
    $candidates = [];
    foreach ($images as $img) {
        if (($img['is_pano'] ?? false) === true) continue;
        if (empty($img['thumb_2048_url'])) continue;
        $geom = $img['geometry'] ?? null;
        if (!$geom || empty($geom['coordinates'])) continue;
        // Filtre annee : captured_at est un timestamp ms
        $cap = (int)($img['captured_at'] ?? 0);
        if ($cap > 0) {
            $year = (int)date('Y', (int)($cap / 1000));
            if ($year < MIN_YEAR) continue;
        }
        [$glon, $glat] = $geom['coordinates'];
        $img['_dist_m'] = distance_m($lat, $lon, (float)$glat, (float)$glon);
        $candidates[] = $img;
    }
    if (!$candidates) return null;
    usort($candidates, fn($a, $b) => $a['_dist_m'] <=> $b['_dist_m']);
    return $candidates[0];
}

/**
 * Rayon adaptatif : tente RADII_M dans l'ordre croissant. Retourne le premier
 * match valide trouve avec son rayon de declenchement, OU null.
 */
function find_mapillary_adaptive(string $token, float $lat, float $lon): array {
    $attempts = [];
    foreach (RADII_M as $r) {
        $imgs = query_mapillary($token, $lat, $lon, $r);
        $total = count($imgs);
        $best = pick_best_mapillary($imgs, $lat, $lon);
        $attempts[] = ['radius_m' => $r, 'total' => $total, 'match' => $best !== null];
        if ($best !== null) {
            return ['best' => $best, 'matched_radius_m' => $r, 'attempts' => $attempts];
        }
    }
    return ['best' => null, 'matched_radius_m' => null, 'attempts' => $attempts];
}

// ------------------------------------------------------------------
// Wikimedia Commons fallback via nearby_pois[].image_url
// ------------------------------------------------------------------

/**
 * Extrait le nom de fichier (sans Wikimedia path/prefix) depuis une image_url POI.
 * Supporte 2 formats observes :
 *  - https://commons.wikimedia.org/wiki/Special:FilePath/{filename}?width=N
 *  - https://upload.wikimedia.org/wikipedia/commons/thumb/.../{filename}/{N}px-{filename}
 */
function extract_wikimedia_filename(string $url): ?string {
    if (preg_match('~/Special:FilePath/([^?]+)~', $url, $m)) {
        return rawurldecode($m[1]);
    }
    if (preg_match('~/wikipedia/commons/(?:thumb/)?[^/]+/[^/]+/([^/]+)~', $url, $m)) {
        $f = rawurldecode($m[1]);
        // Si format thumb /Npx-{filename}, retirer "Npx-"
        if (preg_match('/^\d+px-(.+)$/', $f, $m2)) $f = $m2[1];
        return $f;
    }
    return null;
}

/**
 * Query Wikimedia Commons API pour obtenir url, size, license, author d'un fichier.
 */
function wikimedia_imageinfo(string $filename): ?array {
    $title = 'File:' . str_replace(' ', '_', $filename);
    $url = 'https://commons.wikimedia.org/w/api.php?' . http_build_query([
        'action' => 'query',
        'titles' => $title,
        'prop'   => 'imageinfo',
        // v6 : ajout 'mime' pour permettre le filtre image/jpeg|png
        'iiprop' => 'url|size|mime|extmetadata',
        'format' => 'json',
    ]);
    [$code, $body] = http_get($url);
    if ($code !== 200) return null;
    $d = json_decode($body, true);
    $pages = $d['query']['pages'] ?? [];
    foreach ($pages as $p) {
        if (isset($p['missing'])) return null;
        $ii = $p['imageinfo'][0] ?? null;
        if (!$ii) return null;
        $m = $ii['extmetadata'] ?? [];
        return [
            'url'         => $ii['url'] ?? '',
            'width'       => (int)($ii['width'] ?? 0),
            'height'      => (int)($ii['height'] ?? 0),
            'mime'        => $ii['mime'] ?? '',
            'artist'      => trim(strip_tags($m['Artist']['value'] ?? '')),
            'license'     => $m['LicenseShortName']['value'] ?? '',
            'license_url' => $m['LicenseUrl']['value'] ?? '',
            'desc_url'    => $ii['descriptionurl'] ?? '',
        ];
    }
    return null;
}

function license_is_cc_compatible(string $license): bool {
    $l = strtolower($license);
    return $l === 'cc0' || $l === 'public domain' || str_starts_with($l, 'cc by');
}

/**
 * PRIORITE 1 (v6) : recherche d'une photo Wikimedia de la station elle-meme.
 *
 * Tests successifs (apprentissages M4 batch :
 *  9/15 matches en T2 "Accès Station X Métro Paris" — pattern Chabe01) :
 *   T1 — Cat:Entrances to {nom} metro station       (entree, le top)
 *   T2 — Fulltext "Accès Station {nom} Métro Paris" (Chabe01 pattern)
 *   T3 — Fulltext "Station {nom} Métro Paris"       (général)
 *   T4 — Cat:{nom} (Paris Metro)                    (general gare, files root)
 *   T5 — Cat:{nom} (Paris Metro line N)             (par ligne)
 *   T6 — Cat:{nom} (Métro de Paris)                 (variante française)
 *
 * Filtres : license CC + dims >= WIKIMEDIA_MIN_W + mime image/jpeg|png +
 *           exclusion .pdf/.gif/.svg/.tiff dans le nom de fichier.
 *
 * Retourne ['filename' => str, 'info' => imageinfo, 'source' => str, 'query' => str]
 * ou null. 'source' = identifiant du test qui a matché.
 */
function wm_files_in_cat(string $cat): array {
    $url = 'https://commons.wikimedia.org/w/api.php?' . http_build_query([
        'action'      => 'query',
        'list'        => 'categorymembers',
        'cmtitle'     => "Category:$cat",
        'cmnamespace' => 6,
        'cmlimit'     => 30,
        'format'      => 'json',
    ]);
    [$code, $body] = http_get($url);
    if ($code !== 200) return [];
    $d = json_decode($body, true);
    $members = $d['query']['categorymembers'] ?? [];
    $out = [];
    foreach ($members as $m) {
        $t = $m['title'] ?? '';
        if (str_starts_with($t, 'File:')) $out[] = substr($t, 5);
    }
    return $out;
}

function wm_files_in_search(string $query): array {
    $url = 'https://commons.wikimedia.org/w/api.php?' . http_build_query([
        'action'    => 'query',
        'list'      => 'search',
        'srsearch'  => $query,
        'srnamespace' => 6,
        'srlimit'   => 15,
        'format'    => 'json',
    ]);
    [$code, $body] = http_get($url);
    if ($code !== 200) return [];
    $d = json_decode($body, true);
    $hits = $d['query']['search'] ?? [];
    $out = [];
    foreach ($hits as $h) {
        $t = $h['title'] ?? '';
        if (str_starts_with($t, 'File:')) $out[] = substr($t, 5);
    }
    return $out;
}

function wm_is_excluded_filename(string $filename): bool {
    $lower = strtolower($filename);
    // Extensions non-photo
    foreach (['.pdf', '.gif', '.svg', '.tiff', '.tif', '.webm', '.ogv', '.ogg', '.wav', '.mp4'] as $ext) {
        if (str_ends_with($lower, $ext)) return true;
    }
    // v7 : filtre etendu sujet medioce (apprentissages M3bis+M7bis : 36% echec qualite)
    // Chantier/travaux exclus en absolute (jamais utilisable)
    foreach (['chantier', 'travaux', 'construction', '_construction_', ' construction '] as $bad) {
        if (str_contains($lower, $bad)) return true;
    }
    // Detail/macro/palissade/clôture/mur — sujet non identifiable comme station
    foreach (['détail ', 'detail ', 'macro', 'palissade', 'clôture', 'cloture'] as $bad) {
        if (str_contains($lower, $bad)) return true;
    }
    // Tunnel/voie/rame/wagon/train — sujet ferroviaire pas station
    foreach (['tunnel ', 'voie ', 'voies ', 'rame ', 'rames ', 'wagon', 'train à quai'] as $bad) {
        if (str_contains($lower, $bad)) return true;
    }
    // Note : 'couloir', 'intérieur', 'quai', 'panneau', 'plaque', 'plateforme'
    // ne sont PAS exclus absolument car parfois acceptables (CAS B).
    // Ils sont penalises dans wm_score_filename() au lieu d'etre exclus.
    return false;
}

/**
 * v7 : scoring qualite sur le nom de fichier (et dimensions).
 * Score > 0 souhaitable. Plus c'est haut, mieux c'est.
 * Permet de departager plusieurs candidats matchant un meme test.
 */
function wm_score_filename(string $filename, array $info): int {
    $lower = strtolower($filename);
    $score = 0;
    // Preferences positives : vue exterieure / acces / edicule
    if (str_contains($lower, 'accès ') || str_contains($lower, 'acces '))   $score += 10;
    if (str_contains($lower, 'edicule') || str_contains($lower, 'édicule')) $score += 10;
    if (str_contains($lower, 'façade ') || str_contains($lower, 'facade ')) $score += 8;
    if (str_contains($lower, 'entrée ') || str_contains($lower, 'entree ')) $score += 8;
    if (str_contains($lower, 'sortie '))                                     $score += 5;
    if (str_contains($lower, 'vue exterieure') || str_contains($lower, 'vue extérieure')) $score += 10;
    // Nom contient "station" + identifiant (lieu) : signal positif
    if (preg_match('/(station|métro|metro)/u', $lower) && preg_match('/(rue|avenue|boulevard|place|av\.|bd\.|bd |av )/u', $lower)) {
        $score += 5;
    }
    // Penalites : sujet interieur / detail
    if (str_contains($lower, 'couloir'))   $score -= 8;
    if (str_contains($lower, 'intérieur') || str_contains($lower, 'interieur')) $score -= 8;
    if (str_contains($lower, 'détail') || str_contains($lower, 'detail')) $score -= 10;
    if (str_contains($lower, 'macro'))     $score -= 10;
    if (str_contains($lower, 'quai '))     $score -= 5;
    if (str_contains($lower, 'panneau'))   $score -= 3;
    if (str_contains($lower, 'totem'))     $score -= 3;
    if (str_contains($lower, 'plaque'))    $score -= 3;
    if (str_contains($lower, 'fantôme') || str_contains($lower, 'fantome')) $score -= 5;
    // v8 : penalites anti-escalier (audit utilisateur 2026-06-10)
    // Le pattern Chabe01 "Accès Station X" est ambigu : peut être façade rue OU
    // vue plongeante d'escalier intérieur descendant. Penalise les mots
    // explicites + ratio portrait extrême (escalier vertical étroit).
    if (str_contains($lower, 'escalier') || str_contains($lower, 'escaliers')) $score -= 15;
    if (str_contains($lower, 'marche ') || str_contains($lower, 'marches ')) $score -= 10;
    if (str_contains($lower, 'plongeant') || str_contains($lower, 'descendant')) $score -= 10;
    // Date >= 2020 : signal positif (style Chabe01 pattern recent)
    if (preg_match('/\b(2020|2021|2022|2023|2024|2025|2026)\b/', $filename)) $score += 5;
    // Date < 2015 : signal negatif (vieilles photos parfois bas)
    if (preg_match('/\b(20[01][0-4])\b/', $filename)) $score -= 2;
    // Dimensions : paysage > portrait > carre
    // v8 : pénalité portrait extrême renforcée (h/w > 1.4 = silhouette escalier vertical)
    $w = (int)($info['width'] ?? 0);
    $h = (int)($info['height'] ?? 0);
    if ($h > 0) {
        $ratio = $w / $h;
        if ($ratio > 1.2)  $score += 5;
        elseif ($ratio < 0.85) $score -= 3;
        if ($ratio < 0.71)  $score -= 10;  // v8 : portrait extrême = probable escalier
    }
    // Resolution >= 2400 : meilleur pour AVIF 1600 sans pixelisation
    if ($w >= 2400) $score += 3;
    return $score;
}

function wm_validate_file(string $filename): ?array {
    if (wm_is_excluded_filename($filename)) return null;
    $info = wikimedia_imageinfo($filename);
    if (!$info) return null;
    if ($info['width'] < WIKIMEDIA_MIN_W) return null;
    if (!license_is_cc_compatible($info['license'])) return null;
    if (!in_array($info['mime'], ['image/jpeg', 'image/png'], true)) return null;
    return $info;
}

function find_wikimedia_station(array $station): ?array {
    $name = $station['name'] ?? '';
    if ($name === '') return null;
    $lineCode = $station['lines'][0]['code'] ?? '';

    $tests = [
        ['T1-Cat:Entrances',     fn() => wm_files_in_cat("Entrances to $name metro station")],
        ['T2-Search:AccesStation', fn() => wm_files_in_search("Accès Station $name Métro Paris")],
        ['T3-Search:Station',    fn() => wm_files_in_search("Station $name Métro Paris")],
        ['T4-Cat:ParisMetro',    fn() => wm_files_in_cat("$name (Paris Metro)")],
        ['T5-Cat:ParisMetroLine',fn() => wm_files_in_cat("$name (Paris Metro line $lineCode)")],
        ['T6-Cat:MetroDeParis',  fn() => wm_files_in_cat("$name (Métro de Paris)")],
    ];

    foreach ($tests as [$label, $fn]) {
        $files = $fn();
        if (empty($files)) continue;
        // v7 : on score TOUS les candidats valides du test puis on prend le meilleur
        // (au lieu de prendre le 1er qui valide en v6).
        $candidates = [];
        $tried = 0;
        foreach ($files as $filename) {
            // v7 max 8 essais par test (vs 5 en v6) — plus de chances de trouver bonne photo
            if ($tried >= 8) break;
            $tried++;
            $info = wm_validate_file($filename);
            if (!$info) continue;
            $score = wm_score_filename($filename, $info);
            $candidates[] = [
                'filename' => $filename,
                'info'     => $info,
                'score'    => $score,
            ];
        }
        if (empty($candidates)) continue;
        // Tri par score decroissant (le mieux d'abord)
        usort($candidates, fn($a, $b) => $b['score'] <=> $a['score']);
        $best = $candidates[0];
        return [
            'filename' => $best['filename'],
            'info'     => $best['info'],
            'source'   => $label,
            'query'    => $label,
            'score'    => $best['score'],
            'tried'    => count($candidates),
        ];
    }
    return null;
}

/**
 * Helper : déduit le type de sujet depuis le nom du fichier Wikimedia.
 * Permet de construire un alt text plus précis.
 */
function wikimedia_subject_from_filename(string $filename): string {
    $lower = strtolower($filename);
    // v7 : categorisation plus fine
    if (preg_match('/(façade|facade)/u', $lower))                        return "Façade";
    if (preg_match('/(accès|acces|entrée|entree|edicule|édicule|sortie)/u', $lower)) return "Entrée extérieure";
    if (preg_match('/vue ext[éeè]rieure/u', $lower))                     return "Vue d'ensemble extérieure";
    if (preg_match('/(couloir|hall|souterrain|passage)/u', $lower))      return "Couloir intérieur";
    if (preg_match('/(quai|plateforme|platform)/u', $lower))             return "Quai";
    if (preg_match('/(rame|train)/u', $lower))                            return "Train à quai";
    if (preg_match('/(aérien|aerien|viaduc)/u', $lower))                  return "Vue aérienne";
    if (preg_match('/(panneau|totem|plaque)/u', $lower))                  return "Signalétique extérieure";
    return "Vue extérieure";
}

/**
 * Tente le fallback Wikimedia : itere sur nearby_pois, prend le 1er POI dont
 * l'image satisfait : >=WIKIMEDIA_MIN_W de large + license CC compatible.
 * Retourne [poi, imageinfo] ou null.
 */
function find_wikimedia_fallback(array $station): ?array {
    $pois = $station['nearby_pois'] ?? [];
    $tried = 0;
    foreach ($pois as $poi) {
        if ($tried >= WIKIMEDIA_MAX_POI_TRIES) break;
        $imgUrl = $poi['image_url'] ?? '';
        if (!$imgUrl) continue;
        $filename = extract_wikimedia_filename($imgUrl);
        if (!$filename) continue;
        $tried++;
        $info = wikimedia_imageinfo($filename);
        if (!$info) continue;
        if ($info['width'] < WIKIMEDIA_MIN_W) continue;
        if (!license_is_cc_compatible($info['license'])) continue;
        // Filtre mime : photo (pas SVG, pas PDF)
        if (!in_array($info['mime'], ['image/jpeg', 'image/png'], true)) continue;
        return ['poi' => $poi, 'info' => $info];
    }
    return null;
}

// ------------------------------------------------------------------
// Image pipeline : crop central 16:9 + 12 variantes (4 tailles x 3 formats)
// ------------------------------------------------------------------

function central_crop_16_9(string $src, string $dest): bool {
    // sips -g pixelWidth/pixelHeight pour dimensions
    $info = shell_exec(escapeshellcmd(SIPS) . ' -g pixelWidth -g pixelHeight ' . escapeshellarg($src));
    if (!preg_match('/pixelWidth:\s*(\d+).*pixelHeight:\s*(\d+)/s', $info, $m)) return false;
    $w = (int)$m[1]; $h = (int)$m[2];
    $target_ratio = HERO_RATIO_W / HERO_RATIO_H;
    $cur_ratio = $w / max($h, 1);
    if (abs($cur_ratio - $target_ratio) < 0.01) {
        copy($src, $dest);
        return true;
    }
    if ($cur_ratio > $target_ratio) {
        // trop large : crop horizontal
        $new_w = (int)round($h * $target_ratio);
        $new_h = $h;
    } else {
        // trop haut : crop vertical
        $new_w = $w;
        $new_h = (int)round($w / $target_ratio);
    }
    $cmd = sprintf('%s -c %d %d %s --out %s 2>/dev/null',
        escapeshellcmd(SIPS), $new_h, $new_w,
        escapeshellarg($src), escapeshellarg($dest));
    shell_exec($cmd);
    return is_file($dest) && filesize($dest) > 1024;
}

function generate_variants(string $srcCropped, string $slug, string $outDir): int {
    $count = 0;
    foreach (HERO_WIDTHS as $w) {
        $jpg  = "$outDir/$slug-$w.jpg";
        $webp = "$outDir/$slug-$w.webp";
        $avif = "$outDir/$slug-$w.avif";
        shell_exec(sprintf('%s -Z %d %s -s format jpeg --out %s 2>/dev/null',
            escapeshellcmd(SIPS), $w, escapeshellarg($srcCropped), escapeshellarg($jpg)));
        if (is_file($jpg)) {
            shell_exec(sprintf('%s -q 85 -quiet %s -o %s', escapeshellcmd(CWEBP), escapeshellarg($jpg), escapeshellarg($webp)));
            shell_exec(sprintf('%s --speed 6 -q 60 %s %s > /dev/null 2>&1', escapeshellcmd(AVIFENC), escapeshellarg($jpg), escapeshellarg($avif)));
            if (is_file($jpg) && is_file($webp) && is_file($avif)) $count++;
        }
    }
    return $count;
}

// ------------------------------------------------------------------
// JSON hero updates
// ------------------------------------------------------------------

function build_local_versions(string $slug): array {
    // URLs RELATIVES (sans domaine) attendues par le template <picture>+srcset
    $versions = ['avif' => [], 'webp' => [], 'jpg' => []];
    foreach (HERO_WIDTHS as $w) {
        $versions['avif'][$w] = "/assets/img/stations/$slug/$slug-$w.avif";
        $versions['webp'][$w] = "/assets/img/stations/$slug/$slug-$w.webp";
        $versions['jpg'][$w]  = "/assets/img/stations/$slug/$slug-$w.jpg";
    }
    return $versions;
}

function set_hero_mapillary(array &$station, string $slug, array $img): void {
    $cap = (int)($img['captured_at'] ?? 0);
    $date = $cap > 0 ? date('Y-m-d', (int)($cap / 1000)) : '?';
    $creator = $img['creator']['username'] ?? '?';
    $compass = (int)round((float)($img['compass_angle'] ?? 0));
    $dist = (int)round($img['_dist_m'] ?? 0);
    $lineLabel = $station['name_full'] ?? $station['name'];
    $station['hero_image'] = [
        'url'    => "https://bougeaparis.fr/assets/img/stations/$slug/source/mapillary.jpg",
        'alt'    => sprintf(
            "Vue street-level Mapillary à %d m de la station %s — perspective rue captée le %s par %s (compass %d°)",
            $dist, $lineLabel, $date, $creator, $compass
        ),
        'width'  => 1200,
        'height' => 675,
        'credit' => [
            'author'      => "$creator (Mapillary)",
            'license'     => 'CC BY-SA 4.0',
            'license_url' => 'https://creativecommons.org/licenses/by-sa/4.0',
            'source_url'  => 'https://www.mapillary.com/app/?focus=photo&pKey=' . ($img['id'] ?? ''),
            'date'        => TODAY,
        ],
        'source'           => 'mapillary_streetview',
        'confidence_score' => 22,
        'confidence_level' => 'auto_generated',
        'local_versions'   => build_local_versions($slug),
    ];
}

function set_hero_wikimedia(array &$station, string $slug, array $poi, array $info, int $finalW, int $finalH): void {
    $lineLabel = $station['name_full'] ?? $station['name'];
    $poiName = $poi['name'] ?? '?';
    $poiDist = (int)($poi['nearest_exit']['distance_m'] ?? 0);
    $station['hero_image'] = [
        'url'    => "https://bougeaparis.fr/assets/img/stations/$slug/source/wikimedia.jpg",
        'alt'    => sprintf(
            "Vue Wikimedia Commons de %s (POI proche de la station %s, à %d m) — photo %s",
            $poiName, $lineLabel, $poiDist, $info['license']
        ),
        'width'  => $finalW,
        'height' => $finalH,
        'credit' => [
            'author'      => $info['artist'] ?: 'Wikimedia Commons contributors',
            'license'     => $info['license'] ?: 'CC BY-SA 4.0',
            'license_url' => $info['license_url'] ?: 'https://creativecommons.org/licenses/by-sa/4.0',
            'source_url'  => $info['desc_url'] ?: '',
            'date'        => TODAY,
        ],
        'source'           => 'wikimedia_poi_fallback',
        'confidence_score' => 22,
        'confidence_level' => 'auto_generated',
        'local_versions'   => build_local_versions($slug),
    ];
}

// ------------------------------------------------------------------
// Main
// ------------------------------------------------------------------

function process_station(string $slug, string $token): array {
    $station = load_station($slug);
    $lat = (float)($station['latitude'] ?? 0);
    $lon = (float)($station['longitude'] ?? 0);
    if ($lat === 0.0 || $lon === 0.0) fail("$slug : pas de coords");

    // Flag keep_hero : preserve les heros monument iconique manuellement curates
    // Dry-run bypass : utile pour tester find_wikimedia_station sans ecraser
    $heroExisting = $station['hero_image'] ?? [];
    if (empty($GLOBALS['BP_DRY_RUN'])
        && ($heroExisting['source'] ?? '') === 'manual'
        && ($heroExisting['keep_hero'] ?? false) === true) {
        return [
            'slug'     => $slug,
            'source'   => 'skipped_keep_hero',
            'total'    => null,
            'image_id' => null,
            'creator'  => null,
            'date'     => null,
            'dist_m'   => null,
            'compass'  => null,
            'variants' => 0,
            'tiles'    => null,
            'reason'   => 'keep_hero_flag_true',
        ];
    }

    $outDir = IMG_DIR . "/$slug";
    $srcDir = "$outDir/source";
    if (!is_dir($srcDir)) @mkdir($srcDir, 0755, true);

    // PRIORITE 1 : Wikimedia station (photo edicule/entree/hall de LA gare)
    // v8 : --skip-wikimedia force le fallback Mapillary (utile pour stations
    // sans édicule Guimard, où Wikimedia retourne souvent des photos d'escalier
    // intérieur que le scoring v7 ne distingue pas visuellement).
    $wkStation = !empty($GLOBALS['BP_SKIP_WIKIMEDIA']) ? null : find_wikimedia_station($station);
    if ($wkStation !== null) {
        // Dry-run : log et exit sans modifier
        if (!empty($GLOBALS['BP_DRY_RUN'])) {
            return [
                'slug'   => $slug,
                'source' => 'wikimedia_station',
                'dry_run' => true,
                'test_matched' => $wkStation['source'],
                'filename' => $wkStation['filename'],
                'creator'  => $wkStation['info']['artist'],
                'license'  => $wkStation['info']['license'],
                'dims'     => $wkStation['info']['width'] . 'x' . $wkStation['info']['height'],
                'score'    => $wkStation['score'] ?? null,
                'subject'  => wikimedia_subject_from_filename($wkStation['filename']),
                'candidates_tried' => $wkStation['tried'] ?? null,
            ];
        }
        $info = $wkStation['info'];
        $wkSrc = "$srcDir/wikimedia-station.jpg";
        // v6 : Special:FilePath?width=2400 (thumbnail, evite 429 sur originals 4K+)
        $thumbUrl = 'https://commons.wikimedia.org/wiki/Special:FilePath/' . rawurlencode($wkStation['filename']) . '?width=2400';
        $dlOk = http_download($thumbUrl, $wkSrc);
        if (!$dlOk) {
            // Fallback sur l'original si thumb echoue
            $dlOk = http_download($info['url'], $wkSrc);
        }
        if ($dlOk) {
            $cropped = "$srcDir/wikimedia-station-crop.jpg";
            if (!central_crop_16_9($wkSrc, $cropped)) @copy($wkSrc, $cropped);
            @unlink($wkSrc);
            rename($cropped, $wkSrc);
            // v9 : validation Claude Vision avant de retenir cette candidate
            if (!empty($GLOBALS['BP_VISION'])) {
                $stationName = $station['name_full'] ?? $station['name'];
                $vRes = validate_hero_with_vision($wkSrc, $stationName, $GLOBALS['BP_VISION_KEY']);
                vision_log($slug, $wkStation['filename'], $vRes);
                if (!$vRes['valid'] || !$vRes['identifies']) {
                    @unlink($wkSrc);
                    $wkStation = null; // signale rejet → tombe vers Mapillary
                    goto try_mapillary;
                }
            }
            $n = generate_variants($wkSrc, $slug, $outDir);
            $stationName = $station['name_full'] ?? $station['name'];
            $subject = wikimedia_subject_from_filename($wkStation['filename']);
            $station['hero_image'] = [
                'url'    => "https://bougeaparis.fr/assets/img/stations/$slug/source/wikimedia-station.jpg",
                'alt'    => sprintf(
                    "%s de la station %s — photo Wikimedia Commons par %s (%s)",
                    $subject, $stationName,
                    $info['artist'] ?: 'contributeur Wikimedia',
                    $wkStation['source']
                ),
                'width'  => 1200,
                'height' => 675,
                'credit' => [
                    'author'      => $info['artist'] ?: 'Wikimedia Commons contributors',
                    'license'     => $info['license'] ?: 'CC BY-SA 4.0',
                    'license_url' => $info['license_url'] ?: 'https://creativecommons.org/licenses/by-sa/4.0',
                    'source_url'  => $info['desc_url'] ?: '',
                    'date'        => TODAY,
                ],
                'source'           => 'wikimedia_station',
                'confidence_score' => 22,
                'confidence_level' => 'auto_generated',
                'local_versions'   => build_local_versions($slug),
            ];
            save_station($slug, $station);
            return [
                'slug'             => $slug,
                'source'           => 'wikimedia_station',
                'total'            => null,
                'image_id'         => null,
                'creator'          => $info['artist'],
                'date'             => null,
                'dist_m'           => null,
                'compass'          => null,
                'matched_radius_m' => null,
                'attempts'         => [],
                'variants'         => $n,
                'tiles'            => null,
                'wikimedia_test'   => $wkStation['source'],
                'wikimedia_filename' => $wkStation['filename'],
                'subject'          => $subject,
                'reason'           => null,
            ];
        }
    }

    try_mapillary:
    // 2. Tentative Mapillary avec rayon adaptatif (50 -> 100 -> 200m)
    $adaptive = find_mapillary_adaptive($token, $lat, $lon);
    $best = $adaptive['best'];
    $matchedRadius = $adaptive['matched_radius_m'];
    $attempts = $adaptive['attempts'];
    // Total : utiliser le total du dernier essai (le plus grand bbox)
    $total = end($attempts)['total'] ?? 0;

    // Dry-run : log et exit sans modifier
    if (!empty($GLOBALS['BP_DRY_RUN'])) {
        return [
            'slug'    => $slug,
            'source'  => $best !== null ? 'mapillary_streetview' : 'no_fallback_available',
            'dry_run' => true,
            'test_matched' => $best !== null
                ? "Mapillary-r{$matchedRadius}m"
                : 'no_match',
            'mapillary_attempts' => $attempts,
            'mapillary_best' => $best !== null ? [
                'creator' => $best['creator']['username'] ?? '?',
                'date' => date('Y-m-d', (int)(($best['captured_at'] ?? 0) / 1000)),
                'dist_m' => (int)round($best['_dist_m'] ?? 0),
            ] : null,
        ];
    }

    if ($best !== null) {
        $mapillarySrc = "$srcDir/mapillary.jpg";
        if (http_download($best['thumb_2048_url'], $mapillarySrc)) {
            $cropped = "$srcDir/mapillary-crop.jpg";
            if (central_crop_16_9($mapillarySrc, $cropped)) {
                // Pour stockage source web : on garde la version croppee comme mapillary.jpg
                @unlink($mapillarySrc);
                rename($cropped, $mapillarySrc);
                // v9 : validation Claude Vision avant de retenir
                if (!empty($GLOBALS['BP_VISION'])) {
                    $stationName = $station['name_full'] ?? $station['name'];
                    $vRes = validate_hero_with_vision($mapillarySrc, $stationName, $GLOBALS['BP_VISION_KEY']);
                    vision_log($slug, 'mapillary_' . ($best['id'] ?? 'unknown'), $vRes);
                    if (!$vRes['valid'] || !$vRes['identifies']) {
                        @unlink($mapillarySrc);
                        $best = null; // tombe vers fallback POI puis placeholder
                        goto vision_fallback;
                    }
                }
                $n = generate_variants($mapillarySrc, $slug, $outDir);
                set_hero_mapillary($station, $slug, $best);
                save_station($slug, $station);
                return [
                    'slug'            => $slug,
                    'source'          => 'mapillary_streetview',
                    'total'           => $total,
                    'image_id'        => $best['id'] ?? '',
                    'creator'         => $best['creator']['username'] ?? '?',
                    'date'            => date('Y-m-d', (int)(($best['captured_at'] ?? 0) / 1000)),
                    'dist_m'          => (int)round($best['_dist_m'] ?? 0),
                    'compass'         => (int)round((float)($best['compass_angle'] ?? 0)),
                    'matched_radius_m'=> $matchedRadius,
                    'attempts'        => $attempts,
                    'variants'        => $n,
                    'tiles'           => null,
                    'reason'          => null,
                ];
            }
        }
        // Si crop/download fail : on tombe en fallback
    }

    vision_fallback:
    // 2. Fallback Wikimedia (via nearby_pois)
    $reason = $total === 0
        ? 'mapillary_zero_results_all_radii'
        : ($best === null ? 'mapillary_no_valid_candidate_in_100m' : 'mapillary_download_or_crop_failed');

    $wkFallback = find_wikimedia_fallback($station);
    if ($wkFallback === null) {
        // v9 : si --vision actif, bascule en design_placeholder
        if (!empty($GLOBALS['BP_VISION'])) {
            $station['hero_image'] = [
                'url'      => '',
                'alt'      => sprintf("Station %s — visuel illustratif", $station['name_full'] ?? $station['name']),
                'width'    => 1200,
                'height'   => 675,
                'source'   => 'design_placeholder',
                'fallback' => 'design_placeholder',
                'reason'   => 'no_candidate_passed_vision',
                'keep_hero' => true,
                'credit'   => null,
            ];
            save_station($slug, $station);
            return [
                'slug'   => $slug,
                'source' => 'design_placeholder',
                'reason' => 'no_candidate_passed_vision',
                'variants' => 0,
            ];
        }
        return [
            'slug'            => $slug,
            'source'          => 'no_fallback_available',
            'total'           => $total,
            'image_id'        => null,
            'creator'         => null,
            'date'            => null,
            'dist_m'          => null,
            'compass'         => null,
            'matched_radius_m'=> null,
            'attempts'        => $attempts,
            'variants'        => 0,
            'wikimedia_poi'   => null,
            'reason'          => $reason . '+wikimedia_no_valid_poi (kept previous hero)',
        ];
    }
    $poi = $wkFallback['poi'];
    $info = $wkFallback['info'];
    $wkSrc = "$srcDir/wikimedia.jpg";
    if (!http_download($info['url'], $wkSrc)) {
        fail("$slug : Wikimedia download failed for {$info['url']}");
    }
    $cropped = "$srcDir/wikimedia-crop.jpg";
    if (!central_crop_16_9($wkSrc, $cropped)) {
        @copy($wkSrc, $cropped);
    }
    @unlink($wkSrc);
    rename($cropped, $wkSrc);
    // v9 : validation Claude Vision sur POI fallback
    if (!empty($GLOBALS['BP_VISION'])) {
        $stationName = $station['name_full'] ?? $station['name'];
        $vRes = validate_hero_with_vision($wkSrc, $stationName, $GLOBALS['BP_VISION_KEY']);
        vision_log($slug, 'poi_' . ($poi['name'] ?? 'unknown'), $vRes);
        if (!$vRes['valid'] || !$vRes['identifies']) {
            @unlink($wkSrc);
            // Bascule en design_placeholder
            $station['hero_image'] = [
                'url'      => '',
                'alt'      => sprintf("Station %s — visuel illustratif", $station['name_full'] ?? $station['name']),
                'width'    => 1200,
                'height'   => 675,
                'source'   => 'design_placeholder',
                'fallback' => 'design_placeholder',
                'reason'   => 'all_candidates_rejected_by_vision',
                'keep_hero' => true,
                'credit'   => null,
            ];
            save_station($slug, $station);
            return [
                'slug'   => $slug,
                'source' => 'design_placeholder',
                'reason' => 'all_candidates_rejected_by_vision',
                'variants' => 0,
            ];
        }
    }
    // Read final dimensions after crop
    $finalInfo = shell_exec(escapeshellcmd(SIPS) . ' -g pixelWidth -g pixelHeight ' . escapeshellarg($wkSrc));
    preg_match('/pixelWidth:\s*(\d+).*pixelHeight:\s*(\d+)/s', (string)$finalInfo, $m2);
    $finalW = (int)($m2[1] ?? $info['width']);
    $finalH = (int)($m2[2] ?? $info['height']);
    $n = generate_variants($wkSrc, $slug, $outDir);
    set_hero_wikimedia($station, $slug, $poi, $info, $finalW, $finalH);
    save_station($slug, $station);
    return [
        'slug'            => $slug,
        'source'          => 'wikimedia_poi_fallback',
        'total'           => $total,
        'image_id'        => null,
        'creator'         => $info['artist'],
        'date'            => null,
        'dist_m'          => (int)($poi['nearest_exit']['distance_m'] ?? 0),
        'compass'         => null,
        'matched_radius_m'=> null,
        'attempts'        => $attempts,
        'variants'        => $n,
        'wikimedia_poi'   => [
            'name'     => $poi['name'] ?? '?',
            'category' => $poi['category'] ?? '?',
            'license'  => $info['license'],
            'src_w'    => $info['width'],
            'src_h'    => $info['height'],
            'desc_url' => $info['desc_url'],
        ],
        'reason'          => $reason . '+wikimedia_match',
    ];
}

// ------------------------------------------------------------------
// Entry point
// ------------------------------------------------------------------

$args = parse_args($argv);
$slug = $args['station'] ?? null;
if (!$slug) fail('Usage : --station=<slug> [--dry-run] [--skip-wikimedia]');
$GLOBALS['BP_DRY_RUN'] = isset($args['dry-run']) || in_array('--dry-run', $argv, true);
// v8 : --skip-wikimedia force le fallback Mapillary streetview (vue extérieure
// rue garantie). Utile quand Wikimedia retourne des photos d'escalier intérieur
// que le scoring v7 ne distingue pas du nom "Accès Station X" (vue plongeante).
$GLOBALS['BP_SKIP_WIKIMEDIA'] = isset($args['skip-wikimedia']) || in_array('--skip-wikimedia', $argv, true);
// v9 : --vision active la validation Claude Vision sur chaque candidate.
// Si une candidate Wikimedia ou Mapillary échoue la validation, on essaie
// la suivante. Si toutes échouent, design_placeholder coloré ligne métro.
$GLOBALS['BP_VISION'] = isset($args['vision']) || in_array('--vision', $argv, true);
if ($GLOBALS['BP_VISION']) {
    $GLOBALS['BP_VISION_KEY'] = (function_exists('load_secrets') ? load_secrets() : require SECRETS_PHP)['ANTHROPIC_API_KEY'] ?? null;
    if (!$GLOBALS['BP_VISION_KEY']) fail('--vision requiert ANTHROPIC_API_KEY dans secrets.php');
}

$secrets = load_secrets();
$token = $secrets['MAPILLARY_API_KEY'] ?? null;
if (!$token || str_contains($token, 'COLLER_ICI')) fail('MAPILLARY_API_KEY absent dans secrets.php');

$result = process_station($slug, $token);
echo json_encode($result, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE) . "\n";
