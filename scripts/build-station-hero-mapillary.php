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

const TODAY          = '2026-06-08';
const USER_AGENT     = 'BougeaParisBot/1.0 (https://bougeaparis.fr; ludovic@eoliz.fr)';

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
    if (!$ok || $code !== 200 || !is_file($dest) || filesize($dest) < 1024) {
        @unlink($dest);
        return false;
    }
    return true;
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
        'iiprop' => 'url|size|extmetadata',
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
    $heroExisting = $station['hero_image'] ?? [];
    if (($heroExisting['source'] ?? '') === 'manual'
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

    // 1. Tentative Mapillary avec rayon adaptatif (50 -> 100 -> 200m)
    $adaptive = find_mapillary_adaptive($token, $lat, $lon);
    $best = $adaptive['best'];
    $matchedRadius = $adaptive['matched_radius_m'];
    $attempts = $adaptive['attempts'];
    // Total : utiliser le total du dernier essai (le plus grand bbox)
    $total = end($attempts)['total'] ?? 0;

    if ($best !== null) {
        $mapillarySrc = "$srcDir/mapillary.jpg";
        if (http_download($best['thumb_2048_url'], $mapillarySrc)) {
            $cropped = "$srcDir/mapillary-crop.jpg";
            if (central_crop_16_9($mapillarySrc, $cropped)) {
                // Pour stockage source web : on garde la version croppee comme mapillary.jpg
                @unlink($mapillarySrc);
                rename($cropped, $mapillarySrc);
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

    // 2. Fallback Wikimedia (via nearby_pois)
    $reason = $total === 0
        ? 'mapillary_zero_results_all_radii'
        : ($best === null ? 'mapillary_no_valid_candidate_in_100m' : 'mapillary_download_or_crop_failed');

    $wkFallback = find_wikimedia_fallback($station);
    if ($wkFallback === null) {
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
if (!$slug) fail('Usage : --station=<slug>');

$secrets = load_secrets();
$token = $secrets['MAPILLARY_API_KEY'] ?? null;
if (!$token || str_contains($token, 'COLLER_ICI')) fail('MAPILLARY_API_KEY absent dans secrets.php');

$result = process_station($slug, $token);
echo json_encode($result, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE) . "\n";
