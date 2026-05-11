<?php
declare(strict_types=1);

error_reporting(E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED);
ini_set('memory_limit', '512M');

/**
 * scripts/build-station-hero.php
 *
 * Recupere automatiquement une image hero pour chaque station depuis
 * Wikimedia Commons, avec scoring de confiance et fallback graceful.
 *
 * Strategie : preserve les images selectionnees manuellement
 * (hero_image.source === "manual") et n'agit que sur les autres stations.
 *
 * Pipeline pour chaque station :
 *   1. Tenter de trouver une categorie Commons via plusieurs noms candidats
 *      (ex. "Category:Concorde (Paris Metro)" ou "Category:Entrance to ...").
 *   2. Lister les fichiers de la categorie (jusqu'a 50).
 *   3. Pour chaque fichier, recuperer dims/date/auteur/licence + categories.
 *   4. Calculer un score 0-21 (ratio paysage, resolution, badge Featured/
 *      Quality, recence, mot-cle dans titre, format propre, etc.).
 *   5. Garder le fichier au score le plus haut.
 *   6. Categoriser : auto_high (>=12), auto_low (6-11), no_match (<6).
 *
 * Cache : scripts/cache-gtfs/wikimedia-station-hero.json (gitignored).
 *
 * Usage :
 *   php scripts/build-station-hero.php
 *      → run normal sur toutes les stations
 *      → skip celles avec source=manual
 *
 *   php scripts/build-station-hero.php --review-only
 *      → affiche uniquement les low/no_match avec leurs 3 meilleurs candidats
 *
 *   php scripts/build-station-hero.php --station=concorde
 *      → cible une seule station (utile pour debug)
 *
 *   php scripts/build-station-hero.php --preview
 *      → ne pas ecrire les JSON, juste afficher
 *
 * @package BougeaParis\Scripts
 */

const ROOT          = __DIR__ . '/..';
const STATIONS_DIR  = ROOT . '/public_html/data/stations';
const HERO_CACHE    = __DIR__ . '/cache-gtfs/wikimedia-station-hero.json';

const COMMONS_API   = 'https://commons.wikimedia.org/w/api.php';
const SLEEP_MS      = 200_000; // 200 ms entre 2 appels Commons (~5 req/sec)
const USER_AGENT    = 'BougeaParis-build-station-hero/1.0 (https://bougeaparis.fr)';

const TARGET_THUMB_W = 1600;
const SCORE_HIGH     = 12;
const SCORE_LOW      = 6;

// Pipeline image local : tailles + formats
const IMAGE_WIDTHS    = [400, 800, 1200, 1600];
const IMAGE_OUTDIR    = ROOT . '/public_html/assets/img/stations';
const IMAGE_OUT_RELATIVE = '/assets/img/stations';

// Outils image (paths absolus pour eviter dependence du PATH)
// Resize : ImageMagick (magick 7 ou convert 6) en priorité → cross-platform
// (macOS via brew install imagemagick / Linux via apt install imagemagick).
// Fallback sips pour macOS sans ImageMagick (legacy).
const TOOL_MAGICK_CANDIDATES  = [
    '/opt/homebrew/bin/magick', '/usr/local/bin/magick', '/usr/bin/magick', 'magick',
    '/opt/homebrew/bin/convert', '/usr/local/bin/convert', '/usr/bin/convert', 'convert',
];
const TOOL_SIPS_CANDIDATES    = ['/usr/bin/sips'];
const TOOL_CWEBP_CANDIDATES   = ['/opt/homebrew/bin/cwebp', '/usr/local/bin/cwebp', '/usr/bin/cwebp', 'cwebp'];
const TOOL_AVIFENC_CANDIDATES = ['/opt/homebrew/bin/avifenc', '/usr/local/bin/avifenc', '/usr/bin/avifenc', 'avifenc'];

const WEBP_QUALITY = 80;
const AVIF_MIN     = 30; // qualite : plus bas = meilleur, 30-50 plage equilibree
const AVIF_MAX     = 50;

// CLI
$opts = parse_cli_args($argv);
$onlyStation = $opts['station']     ?? null;
$preview     = (bool)($opts['preview']     ?? false);
$reviewOnly  = (bool)($opts['review-only'] ?? false);

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

function pretty_json(array $d): string {
    return json_encode($d, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
}

function load_cache(): array {
    if (!is_file(HERO_CACHE)) return [];
    $raw = @file_get_contents(HERO_CACHE);
    $d = $raw !== false ? json_decode($raw, true) : null;
    return is_array($d) ? $d : [];
}

function save_cache(array $cache): void {
    $tmp = HERO_CACHE . '.tmp';
    file_put_contents($tmp, pretty_json($cache));
    rename($tmp, HERO_CACHE);
}

/** GET JSON sur Commons API avec User-Agent et rate-limit (200ms). */
function commons_api(array $params): ?array {
    $url = COMMONS_API . '?' . http_build_query($params + ['format' => 'json']);
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT        => 15,
        CURLOPT_CONNECTTIMEOUT => 5,
        CURLOPT_USERAGENT      => USER_AGENT,
        CURLOPT_HTTPHEADER     => ['Accept: application/json'],
    ]);
    $resp = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    usleep(SLEEP_MS);
    if ($resp === false || $code !== 200) return null;
    $d = json_decode($resp, true);
    return is_array($d) ? $d : null;
}

/** Liste les fichiers (jusqu'a 50) d'une catégorie Commons. Retourne titres. */
function fetch_category_files(string $catTitle): array {
    $d = commons_api([
        'action'    => 'query',
        'list'      => 'categorymembers',
        'cmtitle'   => $catTitle,
        'cmtype'    => 'file',
        'cmlimit'   => 50,
    ]);
    $members = $d['query']['categorymembers'] ?? [];
    return array_map(fn($m) => $m['title'] ?? '', $members);
}

/** Cherche des fichiers via search full-text (fallback si pas de catégorie). */
function fetch_search_files(string $query, int $limit = 30): array {
    $d = commons_api([
        'action'      => 'query',
        'list'        => 'search',
        'srsearch'    => $query,
        'srnamespace' => 6,
        'srlimit'     => $limit,
    ]);
    $hits = $d['query']['search'] ?? [];
    return array_map(fn($h) => $h['title'] ?? '', $hits);
}

/**
 * Récupère imageinfo + categories pour un batch de titres File:.
 * Retourne array indexé par titre.
 */
function fetch_imageinfo_batch(array $titles): array {
    if (empty($titles)) return [];
    // L'API Commons accepte titres séparés par |. Limit ~50 par batch.
    $chunks = array_chunk($titles, 25);
    $out = [];
    foreach ($chunks as $chunk) {
        $d = commons_api([
            'action'      => 'query',
            'titles'      => implode('|', $chunk),
            'prop'        => 'imageinfo|categories',
            'iiprop'      => 'url|size|extmetadata|mime',
            'iiurlwidth'  => TARGET_THUMB_W,
            'cllimit'     => 'max',
        ]);
        $pages = $d['query']['pages'] ?? [];
        foreach ($pages as $page) {
            $title = $page['title'] ?? null;
            if (!$title) continue;
            $ii = ($page['imageinfo'] ?? [[]])[0];
            $cats = array_map(fn($c) => $c['title'] ?? '', $page['categories'] ?? []);
            $out[$title] = [
                'imageinfo' => $ii,
                'categories' => $cats,
            ];
        }
    }
    return $out;
}

/** Calcule le score 0-21 d'une image candidate selon les heuristiques. */
function compute_score(array $info): int {
    $ii = $info['imageinfo'] ?? [];
    $cats = $info['categories'] ?? [];
    $title = $ii['canonicaltitle'] ?? '';
    if ($title === '') {
        // Fallback : titre depuis la cle parent (passe par le caller)
        $title = $info['title'] ?? '';
    }
    $w = (int)($ii['width']  ?? 0);
    $h = (int)($ii['height'] ?? 0);
    $mime = (string)($ii['mime'] ?? '');
    $em = $ii['extmetadata'] ?? [];

    $score = 0;

    if ($w > 0 && $h > 0) {
        $ratio = $w / $h;
        // +5 ratio paysage idéal
        if ($ratio >= 1.5 && $ratio <= 1.85) $score += 5;
        // -3 ratio portrait/carré
        if ($ratio < 1.3) $score -= 3;
    }

    // +3 résolution >= 3000px width
    if ($w >= 3000) $score += 3;

    // +5 Featured Picture OR Quality Image
    $hasBadge = false;
    foreach ($cats as $c) {
        $cl = mb_strtolower($c, 'UTF-8');
        if (str_contains($cl, 'featured pictures') || str_contains($cl, 'quality images')) {
            $hasBadge = true;
            break;
        }
    }
    if ($hasBadge) $score += 5;

    // +3 si date >= 2020 (récence)
    $date = $em['DateTimeOriginal']['value'] ?? '';
    if ($date && preg_match('/^(\d{4})/', $date, $m) && (int)$m[1] >= 2020) {
        $score += 3;
    }

    // +3 si titre contient édicule/entrance/façade/extérieur
    $tl = mb_strtolower($title, 'UTF-8');
    if (preg_match('/(édicule|edicule|entrance|façade|facade|extérieur|exterieur)/u', $tl)) {
        $score += 3;
    }

    // +2 si mime image/jpeg ou image/png
    if ($mime === 'image/jpeg' || $mime === 'image/png') $score += 2;

    // -5 si titre suggère plan/map/logo/diagram
    if (preg_match('/(plan|map|logo|diagram|svg|schema|schéma)/u', $tl)) {
        $score -= 5;
    }

    // -3 si pas de licence claire
    $licShort = $em['LicenseShortName']['value'] ?? '';
    if ($licShort === '' || $licShort === '?') $score -= 3;

    return $score;
}

/** Categorise un score en 3 niveaux. */
function score_level(int $s): string {
    if ($s >= SCORE_HIGH) return 'auto_high_confidence';
    if ($s >= SCORE_LOW)  return 'auto_low_confidence';
    return 'no_good_match';
}

/** Construit l'URL thumb 1600px depuis le canonical title. */
function build_thumb_url(string $title, int $width, int $height): ?string {
    // canonicaltitle = "File:Foo.jpg"
    $fname = preg_replace('/^File:/', '', $title);
    if ($fname === '') return null;
    // MD5 commons sharding : 2 first chars of md5
    $md5 = md5(str_replace(' ', '_', $fname));
    $a = $md5[0]; $b = $md5[0] . $md5[1];
    $enc = rawurlencode(str_replace(' ', '_', $fname));
    return "https://upload.wikimedia.org/wikipedia/commons/thumb/$a/$b/$enc/" . TARGET_THUMB_W . "px-$enc";
}

/** Génère une URL Commons FilePath fiable pour servir le thumb. */
function thumb_url_from_imageinfo(array $ii): ?string {
    $thumb = $ii['thumburl'] ?? null;
    if (!$thumb) return null;
    // Strip query string utm_*
    return preg_replace('/\?.*/', '', $thumb);
}

// ============================================================================
// PIPELINE IMAGE LOCAL (download + resize + AVIF/WebP/JPG)
// ============================================================================

/** Resout le 1er chemin existant et executable parmi les candidats. */
function find_tool(array $candidates): ?string {
    foreach ($candidates as $c) {
        if (is_file($c) && is_executable($c)) return $c;
        // Si c'est un nom court, tester via shell
        if (!str_contains($c, '/')) {
            $found = trim((string)shell_exec("command -v $c 2>/dev/null"));
            if ($found !== '') return $found;
        }
    }
    return null;
}

/** Telecharge un binaire depuis Wikimedia avec User-Agent propre. */
function download_image(string $url, string $destPath): bool {
    $fp = @fopen($destPath, 'wb');
    if (!$fp) return false;
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_FILE           => $fp,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_TIMEOUT        => 30,
        CURLOPT_CONNECTTIMEOUT => 8,
        CURLOPT_USERAGENT      => USER_AGENT,
    ]);
    $ok = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    fclose($fp);
    if (!$ok || $code !== 200) {
        @unlink($destPath);
        return false;
    }
    return filesize($destPath) > 0;
}

/**
 * Download original + resize + convert AVIF/WebP/JPG en 4 tailles.
 *
 * Retourne array des chemins relatifs ecrits (pour stockage dans le JSON station)
 * ou null en cas d'echec partiel (les fichiers partiels sont nettoyes).
 */
function build_local_image_versions(string $slug, string $sourceUrl, array &$tools): ?array {
    // Resize : ImageMagick (magick/convert) en priorité (cross-platform),
    // sips en fallback macOS legacy. cwebp + avifenc cross-platform.
    $resizer = $tools['magick'] ?: $tools['sips'];
    if (empty($resizer) || empty($tools['cwebp']) || empty($tools['avifenc'])) {
        log_info("    ERREUR : outils image manquants (resizer=" . ($resizer ?: 'absent') . ", cwebp=" . ($tools['cwebp'] ?: 'absent') . ", avifenc=" . ($tools['avifenc'] ?: 'absent') . ")");
        return null;
    }
    // Détection du type de resizer pour adapter la syntaxe :
    //   - ImageMagick : `magick|convert in -resize 'WxW>' -quality 92 -strip out`
    //   - sips macOS  : `sips -Z W in --out out`
    $isMagick = (basename($resizer) === 'magick' || basename($resizer) === 'convert');

    $outDir = IMAGE_OUTDIR . '/' . $slug;
    if (!is_dir($outDir) && !@mkdir($outDir, 0755, true) && !is_dir($outDir)) {
        log_info("    ERREUR : impossible de creer $outDir");
        return null;
    }

    // Download original (la version 1920px de Wikimedia est suffisante pour 1600w)
    $tmpOrig = $outDir . '/_original.jpg';
    log_info("    download original ...");
    if (!download_image($sourceUrl, $tmpOrig)) {
        log_info("    ERREUR : download $sourceUrl");
        return null;
    }
    log_info("    original telecharge : " . number_format(filesize($tmpOrig)) . " octets");

    $versions = ['avif' => [], 'webp' => [], 'jpg' => []];
    $allOk = true;

    foreach (IMAGE_WIDTHS as $w) {
        $jpgFile  = "$outDir/$slug-$w.jpg";
        $webpFile = "$outDir/$slug-$w.webp";
        $avifFile = "$outDir/$slug-$w.avif";

        // 1. Resize JPG (preserve ratio, max dimension = $w)
        if ($isMagick) {
            // ImageMagick : '-resize WxW>' = scale only if larger (matche sips -Z),
            // '-quality 92' pour JPG, '-strip' supprime métadonnées EXIF.
            $cmd = sprintf('%s %s -resize %sx%s\\> -quality 92 -strip %s 2>&1',
                escapeshellcmd($resizer),
                escapeshellarg($tmpOrig),
                (int)$w, (int)$w,
                escapeshellarg($jpgFile));
        } else {
            // sips macOS legacy
            $cmd = sprintf('%s -Z %d %s --out %s 2>&1',
                escapeshellcmd($resizer), $w,
                escapeshellarg($tmpOrig), escapeshellarg($jpgFile));
        }
        exec($cmd, $out, $code);
        if ($code !== 0 || !is_file($jpgFile)) {
            log_info("    ERREUR resize $w (tool=" . basename($resizer) . ", code=$code)");
            $allOk = false; continue;
        }

        // 2. WebP depuis le JPG resize (q=80, plage equilibree)
        $cmd = sprintf('%s -q %d %s -o %s 2>&1',
            escapeshellcmd($tools['cwebp']), WEBP_QUALITY,
            escapeshellarg($jpgFile), escapeshellarg($webpFile));
        exec($cmd, $out, $code);
        if ($code !== 0 || !is_file($webpFile)) {
            log_info("    ERREUR cwebp $w (code=$code)");
            $allOk = false;
        }

        // 3. AVIF depuis le JPG resize (--min/--max pour qualite controlee)
        $cmd = sprintf('%s --min %d --max %d %s %s 2>&1',
            escapeshellcmd($tools['avifenc']), AVIF_MIN, AVIF_MAX,
            escapeshellarg($jpgFile), escapeshellarg($avifFile));
        exec($cmd, $out, $code);
        if ($code !== 0 || !is_file($avifFile)) {
            log_info("    ERREUR avifenc $w (code=$code)");
            $allOk = false;
        }

        $rel = IMAGE_OUT_RELATIVE . '/' . $slug;
        $versions['jpg'][$w]  = "$rel/$slug-$w.jpg";
        $versions['webp'][$w] = "$rel/$slug-$w.webp";
        $versions['avif'][$w] = "$rel/$slug-$w.avif";
    }

    @unlink($tmpOrig);

    if (!$allOk) {
        log_info("    AVERTISSEMENT : conversions partielles (certaines tailles/formats manquent)");
    }
    return $versions;
}

// ============================================================================
// PIPELINE PAR STATION
// ============================================================================

function find_hero_for_station(array $station, array &$cache): array {
    $name = $station['name']      ?? null;
    $slug = $station['slug']      ?? null;
    $info = ['slug' => $slug, 'name' => $name, 'best' => null, 'top3' => [], 'level' => 'no_good_match'];
    if (!$name || !$slug) return $info;

    // Cache : si on a deja un best valide pour ce slug, on le reutilise
    if (isset($cache[$slug]) && !empty($cache[$slug]['best'])) {
        return $cache[$slug];
    }

    // 1. Catégories candidates
    $catCandidates = [
        'Category:' . $name . ' (Paris Metro)',
        'Category:Entrance to ' . $name . ' metro station',
        'Category:' . $name . ' (Paris Metro station)',
    ];
    $titles = [];
    foreach ($catCandidates as $cat) {
        $files = fetch_category_files($cat);
        if (!empty($files)) {
            log_info("    cat OK : $cat (" . count($files) . " fichiers)");
            $titles = array_unique(array_merge($titles, $files));
        }
    }

    // 2. Fallback search
    if (empty($titles)) {
        log_info("    fallback search : '$name métro'");
        $titles = fetch_search_files($name . ' métro intitle:' . $name, 30);
    }

    if (empty($titles)) {
        $info['level'] = 'no_good_match';
        $cache[$slug] = $info;
        return $info;
    }

    // 3. imageinfo batch
    $infos = fetch_imageinfo_batch($titles);

    // 4. Score chaque candidat
    $scored = [];
    foreach ($infos as $title => $rec) {
        $rec['title'] = $title;
        $score = compute_score($rec);
        $ii = $rec['imageinfo'] ?? [];
        $w = (int)($ii['width'] ?? 0);
        $h = (int)($ii['height'] ?? 0);
        if ($w === 0 || $h === 0) continue;
        $em = $ii['extmetadata'] ?? [];
        $artistRaw = (string)($em['Artist']['value'] ?? '');
        $artist = trim(strip_tags($artistRaw)) ?: 'Inconnu';
        $licShort = (string)($em['LicenseShortName']['value'] ?? '');
        $licUrl   = (string)($em['LicenseUrl']['value']        ?? '');
        $date     = (string)($em['DateTimeOriginal']['value']  ?? '');
        $thumb    = thumb_url_from_imageinfo($ii) ?? build_thumb_url($title, $w, $h);

        $scored[] = [
            'title'         => $title,
            'thumb_url'     => $thumb,
            'orig_w'        => $w,
            'orig_h'        => $h,
            'ratio'         => round($w / $h, 2),
            'thumb_w'       => (int)($ii['thumbwidth']  ?? 0),
            'thumb_h'       => (int)($ii['thumbheight'] ?? 0),
            'score'         => $score,
            'artist'        => $artist,
            'license'       => $licShort,
            'license_url'   => $licUrl,
            'date'          => substr($date, 0, 10),
            'source_url'    => (string)($ii['descriptionurl'] ?? ''),
            'mime'          => (string)($ii['mime'] ?? ''),
        ];
    }

    if (empty($scored)) {
        $info['level'] = 'no_good_match';
        $cache[$slug] = $info;
        return $info;
    }

    usort($scored, fn($a, $b) => $b['score'] <=> $a['score']);
    $info['top3'] = array_slice($scored, 0, 3);
    $info['best'] = $scored[0];
    $info['level'] = score_level($scored[0]['score']);
    $cache[$slug] = $info;
    return $info;
}

// ============================================================================
// MAIN
// ============================================================================

log_info('Phase 1: chargement cache + detection outils');
$cache = load_cache();

// Detection outils image (cross-platform):
// - magick/convert : ImageMagick (Linux + macOS via brew)
// - sips : fallback macOS legacy (si IM absent)
// - cwebp : libwebp (Linux + macOS)
// - avifenc : libavif (Linux + macOS)
$tools = [
    'magick'  => find_tool(TOOL_MAGICK_CANDIDATES),
    'sips'    => find_tool(TOOL_SIPS_CANDIDATES),
    'cwebp'   => find_tool(TOOL_CWEBP_CANDIDATES),
    'avifenc' => find_tool(TOOL_AVIFENC_CANDIDATES),
];
foreach ($tools as $name => $path) {
    if ($path) {
        log_info("  outil $name : $path");
    } else {
        log_info("  outil $name : ABSENT");
    }
}
$resizerOk = $tools['magick'] || $tools['sips'];
$canConvertImages = $resizerOk && $tools['cwebp'] && $tools['avifenc'];
if (!$canConvertImages) {
    log_info('  AVERTISSEMENT : outils image insuffisants pour générer les variantes.');
    log_info('    macOS    : brew install imagemagick webp libavif');
    log_info('    Linux    : sudo apt install imagemagick libavif-bin webp');
    log_info('    Le script continuera mais ne convertira pas les images.');
}

$files = glob(STATIONS_DIR . '/*.json');
if ($onlyStation) {
    $files = array_filter($files, fn($f) => basename($f, '.json') === $onlyStation);
}
sort($files);

$results = []; // slug => info
foreach ($files as $path) {
    $slug = basename($path, '.json');
    $json = json_decode(file_get_contents($path), true);
    if (!is_array($json)) continue;

    // Skip find_hero si manual (preservation curation), MAIS on continue
    // sur le pipeline image local pour generer/regenerer les versions AVIF/WebP/JPG.
    $existing = $json['hero_image'] ?? null;
    $isManual = is_array($existing) && ($existing['source'] ?? '') === 'manual';

    if ($isManual) {
        log_info("  $slug : source=manual (skip recherche, pipeline image conserve)");
        $results[$slug] = ['level' => 'manual', 'slug' => $slug, 'name' => $json['name'] ?? null];
    } else {
        log_info("  $slug : recherche image...");
        $info = find_hero_for_station($json, $cache);
        $results[$slug] = $info;
    }

    if ($preview || $reviewOnly) continue; // pas d'ecriture en preview

    // En mode auto, on a calcule un best ; on prepare le JSON hero_image
    if (!$isManual) {
        if (empty($info['best'])) {
            log_info("    pas de match → pas d'ecriture");
            continue;
        }
        $best = $info['best'];
        $json['hero_image'] = [
            'url'    => $best['thumb_url'],
            'alt'    => $json['name'] . ' — métro de Paris',
            'width'  => TARGET_THUMB_W,
            'height' => $best['thumb_h'] ?: (int)round(TARGET_THUMB_W / $best['ratio']),
            'credit' => [
                'author'      => $best['artist'],
                'license'     => $best['license'],
                'license_url' => $best['license_url'],
                'source_url'  => $best['source_url'],
                'date'        => $best['date'],
            ],
            'source'           => 'auto',
            'confidence_score' => $best['score'],
            'confidence_level' => $info['level'],
        ];
        log_info("    score={$best['score']} level={$info['level']}");
    }

    // Pipeline image local : telecharge l'original Wikimedia + resize 4 tailles
    // + convertit en AVIF/WebP/JPG. URL source = $json['hero_image']['url']
    // (pour manual et auto).
    $heroUrl = $json['hero_image']['url'] ?? null;
    if ($heroUrl && $canConvertImages) {
        log_info("    pipeline image local en cours...");
        $local = build_local_image_versions($slug, $heroUrl, $tools);
        if ($local) {
            $json['hero_image']['local_versions'] = $local;
            log_info("    local_versions ecrit (" . count($local['avif']) . "x" . count($local) . " fichiers)");
        }
    } elseif ($heroUrl && !$canConvertImages) {
        log_info("    skip pipeline image (outils manquants)");
    }

    file_put_contents($path, pretty_json($json) . "\n");
}

save_cache($cache);

// ============================================================================
// REPORT
// ============================================================================

echo "\n";
echo "=========================================================\n";
echo "  RECAP\n";
echo "=========================================================\n";

$buckets = ['manual' => [], 'auto_high_confidence' => [], 'auto_low_confidence' => [], 'no_good_match' => []];
foreach ($results as $slug => $info) {
    $level = $info['level'] ?? 'no_good_match';
    if (!isset($buckets[$level])) $buckets[$level] = [];
    $buckets[$level][] = $slug;
}

printf("  ✋ Manual (preserved)           : %d\n", count($buckets['manual']));
printf("  ✅ Auto high confidence (>=12) : %d\n", count($buckets['auto_high_confidence']));
printf("  ⚠️  Auto low confidence (6-11) : %d %s\n",
    count($buckets['auto_low_confidence']),
    count($buckets['auto_low_confidence']) > 0 ? '[' . implode(',', $buckets['auto_low_confidence']) . ']' : ''
);
printf("  ❌ No good match (fallback)    : %d %s\n",
    count($buckets['no_good_match']),
    count($buckets['no_good_match']) > 0 ? '[' . implode(',', $buckets['no_good_match']) . ']' : ''
);

if ($reviewOnly) {
    echo "\n--- REVIEW : top 3 candidats par station <12 score ---\n";
    foreach ($results as $slug => $info) {
        $level = $info['level'] ?? '';
        if ($level === 'manual' || $level === 'auto_high_confidence') continue;
        echo "\n[$slug] level=$level\n";
        foreach (($info['top3'] ?? []) as $i => $c) {
            printf("  %d. score=%-3d ratio=%-4s w=%-5d %s\n",
                $i + 1, $c['score'], $c['ratio'], $c['orig_w'],
                substr($c['title'], 0, 70)
            );
            echo "     $c[thumb_url]\n";
        }
    }
}
