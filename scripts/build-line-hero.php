<?php
declare(strict_types=1);

error_reporting(E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED);
ini_set('memory_limit', '512M');

/**
 * scripts/build-line-hero.php
 *
 * Pipeline image hero pour les pages LIGNE (15 lignes metro restantes).
 * Adaptation du script build-station-hero.php avec une strategie de recherche
 * specifique aux lignes : combinaison de categories Commons (rame + station
 * iconique) et de full-text search avec mots-cles materiel roulant.
 *
 * Differences cle vs build-station-hero :
 *   - Multiple categories candidates par ligne (rolling stock + iconic stations)
 *   - Multiple search queries enchainees pour elargir l'horizon
 *   - Scoring : bonus mots-cles materiel roulant (MP 05/MP 14/etc.) et stations
 *     emblematiques
 *   - JSON cible : data/lines/metro-{N}.json (au lieu de data/stations/{slug}.json)
 *   - Dossier images : public_html/assets/img/lines/ligne-{N}/
 *
 * Usage :
 *   php scripts/build-line-hero.php --line=1 --review-only
 *      → review uniquement la ligne 1, top 15 candidats sans ecriture
 *
 *   php scripts/build-line-hero.php --line=1 --pick="File:Foo.jpg"
 *      → choix manuel : pipeline image complet avec ce candidat
 *
 *   php scripts/build-line-hero.php --line=1
 *      → mode auto : pick le best score, lance le pipeline image
 *
 * Cache : scripts/cache-gtfs/wikimedia-line-hero.json (gitignored).
 *
 * NOTE : helpers HTTP/scoring/pipeline image dupliques de build-station-hero.php.
 * Refactor future : extraire dans scripts/lib/wikimedia-hero.php.
 *
 * @package BougeaParis\Scripts
 */

const ROOT          = __DIR__ . '/..';
const LINES_DIR     = ROOT . '/public_html/data/lines';
const HERO_CACHE    = __DIR__ . '/cache-gtfs/wikimedia-line-hero.json';

const COMMONS_API   = 'https://commons.wikimedia.org/w/api.php';
const SLEEP_MS      = 200_000;
const USER_AGENT    = 'BougeaParis-build-line-hero/1.0 (https://bougeaparis.fr)';

const TARGET_THUMB_W = 1600;
const SCORE_HIGH     = 12;
const SCORE_LOW      = 6;

const IMAGE_WIDTHS    = [400, 800, 1200, 1600];
const IMAGE_OUTDIR    = ROOT . '/public_html/assets/img/lines';
const IMAGE_OUT_RELATIVE = '/assets/img/lines';

const TOOL_SIPS_CANDIDATES    = ['/usr/bin/sips'];
const TOOL_CWEBP_CANDIDATES   = ['/opt/homebrew/bin/cwebp', '/usr/local/bin/cwebp', 'cwebp'];
const TOOL_AVIFENC_CANDIDATES = ['/opt/homebrew/bin/avifenc', '/usr/local/bin/avifenc', 'avifenc'];

const WEBP_QUALITY = 80;
const AVIF_MIN     = 30;
const AVIF_MAX     = 50;

/**
 * Strategie de recherche par ligne : categories Commons + queries full-text +
 * mots-cles bonus pour le scoring (materiel roulant + stations emblematiques).
 *
 * Pour chaque ligne, on essaie d'abord les categories. Si aucune ne retourne
 * de fichier, on tombe sur les search queries.
 *
 * @var array<int,array{categories: list<string>, queries: list<string>, keywords_bonus: list<string>}>
 */
const LINE_STRATEGY = [
    1 => [
        'categories' => [
            'Category:MP 05',
            'Category:Bastille (Paris Metro)',
            'Category:Charles de Gaulle - Étoile (Paris Metro)',
        ],
        'queries' => [
            'MP 05 Paris metro ligne 1',
            'Métro Paris ligne 1 Bastille rame',
            'Paris metro Line 1 train',
        ],
        // Mots-cles bonus pour le scoring : materiel roulant + stations iconiques
        'keywords_bonus' => [
            'mp 05', 'mp05',
            'bastille', 'étoile', 'etoile', 'gaulle', 'gare de lyon', 'gare lyon',
            'concorde', 'louvre', 'châtelet', 'chatelet', 'tuileries', 'palais royal',
        ],
    ],
    // Templates pour les autres lignes a remplir au fil des sessions :
    // 2 => [...],  // MF 01 (pneu MF67/MF77 archive)
    // 4 => [...],  // MP 14 CC (automatisée)
    // ...
];

// CLI
$opts = parse_cli_args($argv);
$onlyLine    = isset($opts['line']) ? (string)$opts['line'] : null;
$preview     = (bool)($opts['preview']     ?? false);
$reviewOnly  = (bool)($opts['review-only'] ?? false);
$pickTitle   = isset($opts['pick']) ? (string)$opts['pick'] : null;

if (!$onlyLine) {
    fwrite(STDERR, "ERREUR : --line=N obligatoire (ex: --line=1)\n");
    exit(1);
}
$lineNum = (int)$onlyLine;
if (!isset(LINE_STRATEGY[$lineNum])) {
    fwrite(STDERR, "ERREUR : aucune stratégie definie pour ligne $lineNum. Ajouter une entree dans LINE_STRATEGY.\n");
    exit(1);
}

// ============================================================================
// HELPERS (dupliques de build-station-hero.php pour autonomie)
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

function fetch_imageinfo_batch(array $titles): array {
    if (empty($titles)) return [];
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
            $out[$title] = ['imageinfo' => $ii, 'categories' => $cats];
        }
    }
    return $out;
}

/**
 * Score 0-25 specifique aux pages ligne (bonus mots-cles materiel roulant +
 * stations iconiques). Sur-bonus possible sur ligne, contrairement au score
 * stations qui plafonne autour de 13.
 */
function compute_score(array $info, array $keywordsBonus): int {
    $ii = $info['imageinfo'] ?? [];
    $cats = $info['categories'] ?? [];
    $title = $ii['canonicaltitle'] ?? ($info['title'] ?? '');
    $w = (int)($ii['width']  ?? 0);
    $h = (int)($ii['height'] ?? 0);
    $mime = (string)($ii['mime'] ?? '');
    $em = $ii['extmetadata'] ?? [];

    $score = 0;

    if ($w > 0 && $h > 0) {
        $ratio = $w / $h;
        if ($ratio >= 1.5 && $ratio <= 1.85) $score += 5;
        if ($ratio < 1.3) $score -= 3;
    }
    if ($w >= 3000) $score += 3;

    $hasBadge = false;
    foreach ($cats as $c) {
        $cl = mb_strtolower($c, 'UTF-8');
        if (str_contains($cl, 'featured pictures') || str_contains($cl, 'quality images')) {
            $hasBadge = true; break;
        }
    }
    if ($hasBadge) $score += 5;

    $date = $em['DateTimeOriginal']['value'] ?? '';
    if ($date && preg_match('/^(\d{4})/', $date, $m) && (int)$m[1] >= 2020) $score += 3;

    $tl = mb_strtolower($title, 'UTF-8');

    // Bonus mots-cles : materiel roulant (MP 05) + stations iconiques
    foreach ($keywordsBonus as $kw) {
        if (str_contains($tl, $kw)) {
            // +5 pour le materiel roulant (premiers de la liste), +3 pour les stations
            $score += (str_starts_with($kw, 'mp ') || str_starts_with($kw, 'mp0') || str_starts_with($kw, 'mp1')) ? 5 : 3;
            // ne compter qu'une fois par categorie pour eviter inflation
            break;
        }
    }
    // Si une station iconique apparait en plus du materiel roulant, +3 supplementaire
    foreach (array_slice($keywordsBonus, 2) as $kw) { // skip 2 premiers (materiel)
        if (str_contains($tl, $kw)) { $score += 3; break; }
    }

    if (preg_match('/(rame|platform|quai|train|station)/u', $tl)) $score += 2;
    if ($mime === 'image/jpeg' || $mime === 'image/png') $score += 2;

    if (preg_match('/(plan|map|logo|diagram|svg|schema|schéma|intérieur|interieur|couloir|écran|ecran)/u', $tl)) {
        $score -= 5;
    }

    $licShort = $em['LicenseShortName']['value'] ?? '';
    if ($licShort === '' || $licShort === '?') $score -= 3;

    return $score;
}

function score_level(int $s): string {
    if ($s >= SCORE_HIGH) return 'auto_high_confidence';
    if ($s >= SCORE_LOW)  return 'auto_low_confidence';
    return 'no_good_match';
}

function thumb_url_from_imageinfo(array $ii): ?string {
    $thumb = $ii['thumburl'] ?? null;
    if (!$thumb) return null;
    return preg_replace('/\?.*/', '', $thumb);
}

// === PIPELINE IMAGE LOCAL ===

function find_tool(array $candidates): ?string {
    foreach ($candidates as $c) {
        if (is_file($c) && is_executable($c)) return $c;
        if (!str_contains($c, '/')) {
            $found = trim((string)shell_exec("command -v $c 2>/dev/null"));
            if ($found !== '') return $found;
        }
    }
    return null;
}

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
 * Telecharge + resize + convert AVIF/WebP/JPG dans assets/img/lines/{slugDir}.
 * Retourne le tableau des chemins relatifs ou null.
 */
function build_local_image_versions(string $slugDir, string $sourceUrl, array &$tools): ?array {
    if (empty($tools['sips']) || empty($tools['cwebp']) || empty($tools['avifenc'])) return null;
    $outDir = IMAGE_OUTDIR . '/' . $slugDir;
    if (!is_dir($outDir) && !@mkdir($outDir, 0755, true) && !is_dir($outDir)) {
        log_info("    ERREUR : impossible de creer $outDir");
        return null;
    }

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
        $jpgFile  = "$outDir/$slugDir-$w.jpg";
        $webpFile = "$outDir/$slugDir-$w.webp";
        $avifFile = "$outDir/$slugDir-$w.avif";

        $cmd = sprintf('%s -Z %d %s --out %s 2>&1',
            escapeshellcmd($tools['sips']), $w,
            escapeshellarg($tmpOrig), escapeshellarg($jpgFile));
        exec($cmd, $out, $code);
        if ($code !== 0 || !is_file($jpgFile)) {
            log_info("    ERREUR sips $w (code=$code)");
            $allOk = false; continue;
        }

        $cmd = sprintf('%s -q %d %s -o %s 2>&1',
            escapeshellcmd($tools['cwebp']), WEBP_QUALITY,
            escapeshellarg($jpgFile), escapeshellarg($webpFile));
        exec($cmd, $out, $code);
        if ($code !== 0 || !is_file($webpFile)) { log_info("    ERREUR cwebp $w (code=$code)"); $allOk = false; }

        $cmd = sprintf('%s --min %d --max %d %s %s 2>&1',
            escapeshellcmd($tools['avifenc']), AVIF_MIN, AVIF_MAX,
            escapeshellarg($jpgFile), escapeshellarg($avifFile));
        exec($cmd, $out, $code);
        if ($code !== 0 || !is_file($avifFile)) { log_info("    ERREUR avifenc $w (code=$code)"); $allOk = false; }

        $rel = IMAGE_OUT_RELATIVE . '/' . $slugDir;
        $versions['jpg'][$w]  = "$rel/$slugDir-$w.jpg";
        $versions['webp'][$w] = "$rel/$slugDir-$w.webp";
        $versions['avif'][$w] = "$rel/$slugDir-$w.avif";
    }

    @unlink($tmpOrig);
    if (!$allOk) log_info("    AVERTISSEMENT : conversions partielles");
    return $versions;
}

// ============================================================================
// PIPELINE PAR LIGNE
// ============================================================================

function find_hero_for_line(int $lineNum, array &$cache): array {
    $strategy = LINE_STRATEGY[$lineNum];
    $cacheKey = "metro-$lineNum";
    $info = ['line' => $lineNum, 'best' => null, 'top' => [], 'level' => 'no_good_match'];

    if (isset($cache[$cacheKey]) && !empty($cache[$cacheKey]['best'])) {
        return $cache[$cacheKey];
    }

    $titles = [];
    foreach ($strategy['categories'] as $cat) {
        $files = fetch_category_files($cat);
        if (!empty($files)) {
            log_info("    cat OK : $cat (" . count($files) . " fichiers)");
            $titles = array_unique(array_merge($titles, $files));
        }
    }
    foreach ($strategy['queries'] as $q) {
        $files = fetch_search_files($q, 30);
        if (!empty($files)) {
            log_info("    search : '$q' (" . count($files) . " hits)");
            $titles = array_unique(array_merge($titles, $files));
        }
        if (count($titles) >= 80) break; // assez de candidats
    }

    // Pre-filtre : on ne garde que les jpg/png (pas de .ogv .ogg .flac .svg)
    $titles = array_filter($titles, function (string $t): bool {
        $tl = mb_strtolower($t, 'UTF-8');
        return preg_match('/\.(jpg|jpeg|png)$/u', $tl) === 1;
    });

    if (empty($titles)) {
        $info['level'] = 'no_good_match';
        $cache[$cacheKey] = $info;
        return $info;
    }

    $infos = fetch_imageinfo_batch(array_values($titles));
    $scored = [];
    foreach ($infos as $title => $rec) {
        $rec['title'] = $title;
        $score = compute_score($rec, $strategy['keywords_bonus']);
        $ii = $rec['imageinfo'] ?? [];
        $w = (int)($ii['width'] ?? 0); $h = (int)($ii['height'] ?? 0);
        if ($w === 0 || $h === 0) continue;
        $em = $ii['extmetadata'] ?? [];
        $artist = trim(strip_tags((string)($em['Artist']['value'] ?? ''))) ?: 'Inconnu';
        $licShort = (string)($em['LicenseShortName']['value'] ?? '');
        $licUrl   = (string)($em['LicenseUrl']['value']        ?? '');
        $date     = (string)($em['DateTimeOriginal']['value']  ?? '');
        $thumb    = thumb_url_from_imageinfo($ii);

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
        $cache[$cacheKey] = $info;
        return $info;
    }

    usort($scored, fn($a, $b) => $b['score'] <=> $a['score']);
    $info['top'] = array_slice($scored, 0, 15);
    $info['best'] = $scored[0];
    $info['level'] = score_level($scored[0]['score']);
    $cache[$cacheKey] = $info;
    return $info;
}

// ============================================================================
// MAIN
// ============================================================================

log_info("Phase 1 : detection outils + recherche candidats ligne $lineNum");
$cache = load_cache();

$tools = [
    'sips'    => find_tool(TOOL_SIPS_CANDIDATES),
    'cwebp'   => find_tool(TOOL_CWEBP_CANDIDATES),
    'avifenc' => find_tool(TOOL_AVIFENC_CANDIDATES),
];
foreach ($tools as $name => $path) {
    log_info("  outil $name : " . ($path ?: 'ABSENT'));
}
$canConvertImages = $tools['sips'] && $tools['cwebp'] && $tools['avifenc'];

$info = find_hero_for_line($lineNum, $cache);
save_cache($cache);

// ============================================================================
// REVIEW MODE : top 15 candidats + URLs
// ============================================================================
if ($reviewOnly) {
    echo "\n=== TOP 15 candidats Wikimedia pour ligne $lineNum ===\n\n";
    foreach (($info['top'] ?? []) as $i => $c) {
        printf("#%-2d  score=%-3d  ratio=%-5s  %sx%s  %-12s  %s  par %s\n",
            $i + 1, $c['score'], $c['ratio'],
            $c['orig_w'], $c['orig_h'],
            $c['license'] ?: '(no licence)',
            $c['date'] ?: '(no date)',
            substr($c['artist'], 0, 30)
        );
        echo "    📄 $c[title]\n";
        echo "    🖼  $c[thumb_url]\n";
        echo "    🔗 $c[source_url]\n\n";
    }
    echo "\n→ Choisis un candidat puis relance avec : --line=$lineNum --pick=\"<File:Title.jpg>\"\n";
    exit(0);
}

// ============================================================================
// PICK + IMAGE PIPELINE
// ============================================================================
if ($pickTitle) {
    $best = null;
    foreach (($info['top'] ?? []) as $c) {
        if ($c['title'] === $pickTitle) { $best = $c; break; }
    }
    if (!$best) {
        fwrite(STDERR, "ERREUR : --pick=\"$pickTitle\" introuvable dans le top 15. Relance avec --review-only.\n");
        exit(1);
    }
    log_info("  pick utilisateur : $pickTitle (score=$best[score])");
} else {
    $best = $info['best'] ?? null;
    if (!$best) {
        fwrite(STDERR, "ERREUR : aucun candidat trouve pour ligne $lineNum.\n");
        exit(1);
    }
    log_info("  pick auto : $best[title] (score=$best[score])");
}

$slugDir = "ligne-$lineNum";
$jsonPath = LINES_DIR . "/metro-$lineNum.json";
if (!is_file($jsonPath)) {
    fwrite(STDERR, "ERREUR : $jsonPath introuvable.\n");
    exit(1);
}

$json = json_decode(file_get_contents($jsonPath), true);
if (!is_array($json)) {
    fwrite(STDERR, "ERREUR : JSON invalide $jsonPath\n");
    exit(1);
}

$json['hero_image'] = [
    'url'    => $best['thumb_url'],
    'alt'    => "Ligne $lineNum du métro de Paris — rame en station",
    'width'  => TARGET_THUMB_W,
    'height' => $best['thumb_h'] ?: (int)round(TARGET_THUMB_W / max($best['ratio'], 0.01)),
    'credit' => [
        'author'      => $best['artist'],
        'license'     => $best['license'],
        'license_url' => $best['license_url'],
        'source_url'  => $best['source_url'],
        'date'        => $best['date'],
    ],
    'source'           => $pickTitle ? 'manual' : 'auto',
    'confidence_score' => $best['score'],
    'confidence_level' => score_level($best['score']),
];

if ($preview) {
    log_info("  PREVIEW : pas d'ecriture. hero_image preview :");
    echo pretty_json($json['hero_image']) . "\n";
    exit(0);
}

if ($canConvertImages) {
    log_info("  pipeline image local en cours ($slugDir) ...");
    $local = build_local_image_versions($slugDir, $best['thumb_url'], $tools);
    if ($local) {
        $json['hero_image']['local_versions'] = $local;
        log_info("  local_versions ecrites (12 fichiers attendus)");
    }
} else {
    log_info("  AVERTISSEMENT : outils image absents, pas de conversion local.");
}

file_put_contents($jsonPath, pretty_json($json) . "\n");
log_info("  JSON ecrit : $jsonPath");
log_info("Termine.");
