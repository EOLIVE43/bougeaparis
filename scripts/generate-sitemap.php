<?php
declare(strict_types=1);

/**
 * scripts/generate-sitemap.php
 *
 * Régénère public_html/sitemap.xml depuis l'état actuel du repo :
 *   - Pages hub (home, /metro/, /rer/, /bus/, /tramway/, /aeroports/,
 *     /gares/, /transilien/, /info-trafic/)
 *   - Pages ligne (/metro/ligne-{slug}/) depuis data/lines.json
 *   - Toutes stations published=true (/metro/station/{slug}/)
 *   - Pages éditoriales (/sources/, /a-propos/, /contact/, ...)
 *
 * Lastmod station = mtime du JSON (format YYYY-MM-DD).
 *
 * Usage :
 *   php scripts/generate-sitemap.php
 *
 * Sortie : public_html/sitemap.xml (écrasement complet).
 * Exit : 0 succès, 1 erreur.
 *
 * Intégré dans .github/workflows/deploy.yml (régénération avant chaque
 * upload FTP) pour rester en phase avec les stations publiées.
 */

const ROOT_DIR     = __DIR__ . '/..';
const STATIONS_DIR = ROOT_DIR . '/public_html/data/stations';
const AEROPORTS_DIR = ROOT_DIR . '/public_html/data/aeroports';
const LINES_JSON   = ROOT_DIR . '/public_html/data/lines.json';
const OUT_FILE     = ROOT_DIR . '/public_html/sitemap.xml';
const BASE_URL     = 'https://bougeaparis.fr';

function log_line(string $msg): void {
    fwrite(STDERR, "[" . date('H:i:s') . "] $msg\n");
}

function url_entry(string $loc, string $changefreq, string $priority, ?string $lastmod = null): string {
    $out  = "  <url>\n";
    $out .= "    <loc>$loc</loc>\n";
    if ($lastmod !== null) {
        $out .= "    <lastmod>$lastmod</lastmod>\n";
    }
    $out .= "    <changefreq>$changefreq</changefreq>\n";
    $out .= "    <priority>$priority</priority>\n";
    $out .= "  </url>\n";
    return $out;
}

// 1. Charger les lignes metro depuis lines.json
$linesData = json_decode((string)file_get_contents(LINES_JSON), true);
if (!is_array($linesData) || empty($linesData['metro'])) {
    fwrite(STDERR, "[ERREUR] lines.json invalide ou vide\n");
    exit(1);
}
$metroLines = $linesData['metro'];

// 2. Scanner stations published=true
$stationFiles = glob(STATIONS_DIR . '/*.json') ?: [];
$publishedStations = [];
foreach ($stationFiles as $f) {
    $data = json_decode((string)file_get_contents($f), true);
    if (!is_array($data)) continue;
    if (empty($data['published'])) continue;
    $slug = $data['slug'] ?? basename($f, '.json');
    $publishedStations[] = [
        'slug'    => $slug,
        'lastmod' => date('Y-m-d', (int)filemtime($f)),
    ];
}
usort($publishedStations, fn($a, $b) => strcmp($a['slug'], $b['slug']));

log_line('Lignes metro : ' . count($metroLines));
log_line('Stations published : ' . count($publishedStations));

// 3. Construire sitemap
$today = date('Y-m-d');
$xml  = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
$xml .= "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n";

// 3.1 Home
$xml .= url_entry(BASE_URL . '/', 'daily', '1.0', $today);

// 3.2 Hubs mode
$hubs = [
    ['/metro/',      'weekly', '0.9'],
    ['/rer/',        'weekly', '0.9'],
    ['/bus/',        'weekly', '0.9'],
    ['/tramway/',    'weekly', '0.9'],
    ['/aeroports/',  'weekly', '0.9'],
    ['/transilien/', 'weekly', '0.9'],
    ['/gares/',      'weekly', '0.8'],
    ['/info-trafic/','daily',  '0.8'],
];
foreach ($hubs as [$path, $cf, $pr]) {
    $xml .= url_entry(BASE_URL . $path, $cf, $pr, $today);
}

// 3.3 Pages ligne metro
foreach ($metroLines as $line) {
    $slug = $line['slug'] ?? null;
    if (!$slug) continue;
    $priority = (str_ends_with($slug, 'bis')) ? '0.7' : '0.9';
    $xml .= url_entry(BASE_URL . "/metro/$slug/", 'daily', $priority, $today);
}

// 3.4 Stations published
foreach ($publishedStations as $st) {
    $xml .= url_entry(
        BASE_URL . "/metro/station/{$st['slug']}/",
        'weekly',
        '0.8',
        $st['lastmod']
    );
}

// 3.4b Aéroports published (3 fiches détail)
$aeroFiles = glob(AEROPORTS_DIR . '/*.json') ?: [];
$publishedAeroports = [];
foreach ($aeroFiles as $f) {
    $data = json_decode((string)file_get_contents($f), true);
    if (!is_array($data) || empty($data['published'])) continue;
    $publishedAeroports[] = [
        'slug'    => $data['slug'] ?? basename($f, '.json'),
        'lastmod' => date('Y-m-d', (int)filemtime($f)),
    ];
}
usort($publishedAeroports, fn($a, $b) => strcmp($a['slug'], $b['slug']));
foreach ($publishedAeroports as $ap) {
    $xml .= url_entry(
        BASE_URL . "/aeroports/{$ap['slug']}/",
        'weekly',
        '0.8',
        $ap['lastmod']
    );
}
log_line('Aéroports publiés : ' . count($publishedAeroports));

// 3.5 Pages éditoriales / footer
$footer = [
    ['/sources/',            'monthly', '0.5'],
    ['/a-propos/',           'monthly', '0.5'],
    ['/contact/',            'monthly', '0.4'],
    ['/mentions-legales/',   'yearly',  '0.3'],
    ['/confidentialite/',    'yearly',  '0.3'],
    ['/auteur/ludo/',        'monthly', '0.4'],
    ['/auteur/elodie/',      'monthly', '0.4'],
];
foreach ($footer as [$path, $cf, $pr]) {
    $xml .= url_entry(BASE_URL . $path, $cf, $pr);
}

$xml .= "</urlset>\n";

// 4. Écriture
file_put_contents(OUT_FILE, $xml);
$totalUrls = substr_count($xml, '<loc>');
log_line("Sitemap généré : $totalUrls URLs → " . OUT_FILE);

exit(0);
