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

log_info('Phase 1: chargement cache + iteration stations');
$cache = load_cache();

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

    // Skip si manual (preservation curation)
    $existing = $json['hero_image'] ?? null;
    if (is_array($existing) && ($existing['source'] ?? '') === 'manual') {
        log_info("  $slug : SKIP (source=manual)");
        $results[$slug] = ['level' => 'manual', 'slug' => $slug, 'name' => $json['name'] ?? null];
        continue;
    }

    log_info("  $slug : recherche image...");
    $info = find_hero_for_station($json, $cache);
    $results[$slug] = $info;

    if ($preview || $reviewOnly) continue; // pas d'ecriture en preview

    // Ecriture conditionnelle
    if (!empty($info['best'])) {
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
        file_put_contents($path, pretty_json($json) . "\n");
        log_info("    ecrit : score={$best['score']} level={$info['level']}");
    } else {
        log_info("    pas de match → pas d'ecriture");
    }
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
