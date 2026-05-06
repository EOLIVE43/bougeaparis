<?php
declare(strict_types=1);

error_reporting(E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED);

/**
 * scripts/bootstrap-line.php
 *
 * Outil d'industrialisation pour le batch des 15 lignes metro restantes.
 * Lit data/lines/metro-{N}.json (existant : 15 fields baseline déjà présents)
 * et complete les champs manquants avec des defaults mécaniques OU des
 * stubs editoriaux pour aider l'enrichissement manuel.
 *
 * STRATEGIE : ne JAMAIS écraser un champ existant non vide. On comble
 * uniquement ce qui manque. Les blocs editoriaux restent en stubs vides.
 *
 * Usage :
 *   php scripts/bootstrap-line.php --line=14
 *      → complete metro-14.json en place
 *
 *   php scripts/bootstrap-line.php --line=14 --dry-run
 *      → affiche le diff JSON sans ecrire
 *
 *   php scripts/bootstrap-line.php --line=14 --print-only
 *      → affiche le JSON resultat (full) sans ecrire
 *
 * @package BougeaParis\Scripts
 */

const ROOT          = __DIR__ . '/..';
const LINES_DIR     = ROOT . '/public_html/data/lines';
const REFERENCE_FILE = LINES_DIR . '/metro-1.json';

/**
 * Donnees publiques 2026 (sources : IDFM open data, RATP, Wikipedia FR).
 * Approximatives, a affiner manuellement si valeurs precises requises.
 */
const DAILY_RIDERS = [
    1    => 750000,  2    => 478000,  3    => 423000,  '3bis' => 17000,
    4    => 803000,  5    => 467000,  6    => 388000,  7      => 597000,
    '7bis' => 32000, 8    => 425000,  9    => 567000,  10     => 169000,
    11   => 234000,  12   => 285000,  13   => 612000,  14     => 820000,
];

const AUTOMATED_YEAR = [
    1  => 2012,  // automatisation totale terminée fin 2012
    4  => 2022,  // dernière conversion automatique réseau classique
    14 => 1998,  // automatisée dès l'origine
    // L11 : non automatisée malgré le prolongement Rosny
];

/**
 * Coordonnees indicatives terminus (deja renseignees pour la plupart, on
 * patche si vraiment vide). Format : [terminus_a, terminus_b].
 * Liste de secours si jamais terminus_a/b absents du JSON existant.
 */
const TERMINUS_FALLBACK = [
    1    => ['La Défense (Grande Arche)', 'Château de Vincennes'],
    2    => ['Porte Dauphine', 'Nation'],
    3    => ['Pont de Levallois - Bécon', 'Gallieni'],
    '3bis' => ['Gambetta', 'Porte des Lilas'],
    4    => ['Porte de Clignancourt', 'Bagneux — Lucie Aubrac'],
    5    => ['Bobigny — Pablo Picasso', 'Place d\'Italie'],
    6    => ['Charles de Gaulle - Étoile', 'Nation'],
    7    => ['La Courneuve — 8 Mai 1945', 'Villejuif Louis Aragon / Mairie d\'Ivry'],
    '7bis' => ['Louis Blanc', 'Pré Saint-Gervais'],
    8    => ['Balard', 'Pointe du Lac'],
    9    => ['Pont de Sèvres', 'Mairie de Montreuil'],
    10   => ['Boulogne — Pont de Saint-Cloud', 'Gare d\'Austerlitz'],
    11   => ['Châtelet', 'Rosny — Bois-Perrier'],
    12   => ['Front Populaire', 'Mairie d\'Issy'],
    13   => ['Saint-Denis — Université / Asnières — Gennevilliers — Les Courtilles', 'Châtillon — Montrouge'],
    14   => ['Saint-Denis — Pleyel', 'Aéroport d\'Orly'],
];

// =============================================================================
// HELPERS
// =============================================================================

function parse_cli_args(array $argv): array {
    $out = [];
    foreach (array_slice($argv, 1) as $arg) {
        if (str_starts_with($arg, '--')) {
            $arg = substr($arg, 2);
            if (str_contains($arg, '=')) { [$k, $v] = explode('=', $arg, 2); $out[$k] = $v; }
            else { $out[$arg] = true; }
        }
    }
    return $out;
}

function pretty_json(array $d): string {
    return json_encode($d, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
}

function log_info(string $msg): void {
    fwrite(STDOUT, '[' . date('H:i:s') . '] ' . $msg . "\n");
}

/**
 * Eclaircit une couleur hexa de ~85% pour générer color_light.
 * #FFCE00 → #FFF6CC (mélange avec blanc à 80%).
 */
function lighten_color(string $hex, float $mix = 0.8): string {
    $hex = ltrim($hex, '#');
    if (strlen($hex) !== 6) return '#FFFFFF';
    $r = (int)hexdec(substr($hex, 0, 2));
    $g = (int)hexdec(substr($hex, 2, 2));
    $b = (int)hexdec(substr($hex, 4, 2));
    $r = (int)round($r + ($mix * (255 - $r)));
    $g = (int)round($g + ($mix * (255 - $g)));
    $b = (int)round($b + ($mix * (255 - $b)));
    return sprintf('#%02X%02X%02X', $r, $g, $b);
}

/**
 * Charge l'index data/lines.json et retourne les lignes metro indexees par code.
 *
 * @return array<string, array> code => {name, color, color_text, url}
 */
function load_metro_index(): array {
    static $cache = null;
    if ($cache !== null) return $cache;
    $cache = [];
    $linesIndex = ROOT . '/public_html/data/lines.json';
    if (!is_file($linesIndex)) return $cache;
    $idx = json_decode(file_get_contents($linesIndex), true);
    if (!is_array($idx)) return $cache;
    // lines.json utilise 'label' / 'id' (pas 'code'). Normalisation.
    foreach ($idx['metro'] ?? [] as $line) {
        $code = (string)($line['label'] ?? $line['id'] ?? '');
        if ($code === '') continue;
        $cache[$code] = [
            'code'       => $code,
            'name'       => $line['name'] ?? "Ligne $code",
            'color'      => $line['color']       ?? '#999',
            'color_text' => $line['text_color']  ?? $line['color_text'] ?? '#FFF',
            'url'        => '/metro/ligne-' . strtolower($code) . '/',
        ];
    }
    return $cache;
}

/**
 * Reconstruit la liste des "discover_metro_lines" : 4 lignes (self + top 3
 * lignes les plus connectees a la courante par stations partagees).
 */
function build_discover_lines(string|int $currentLine, array $connectionsMetro): array {
    $idx = load_metro_index();
    $currentCode = (string)$currentLine;

    // Trier les connexions par nombre de stations partagees (desc)
    $sorted = $connectionsMetro;
    usort($sorted, fn($a, $b) => count($b['stations'] ?? []) - count($a['stations'] ?? []));
    $top3 = array_slice($sorted, 0, 3);

    $out = [];
    // 1. Self (is_current: true)
    if (isset($idx[$currentCode])) {
        $self = $idx[$currentCode];
        $self['is_current'] = true;
        $out[] = $self;
    }
    // 2. Top 3 connectees
    foreach ($top3 as $conn) {
        $code = $conn['code'];
        if ($code === $currentCode || !isset($idx[$code])) continue;
        $out[] = $idx[$code];
    }
    return $out;
}

/**
 * Construit les 3 listes de correspondances (metro/rer/other) en parcourant
 * les stations de la ligne et en groupant les correspondances par mode+code.
 *
 * @param array $stations Liste des stations de la ligne (chaque station a
 *                        eventuellement un champ 'correspondences[]' avec
 *                        {mode, line, color, ...}).
 * @param string|int $currentLine Code de la ligne courante (ex: '14').
 * @return array {connections_metro, connections_rer, connections_other}
 */
function build_connections(array $stations, string|int $currentLine): array {
    $metroIdx = load_metro_index();
    $currentCode = (string)$currentLine;

    // mode + code => array de noms de stations partagees
    $groups = [];

    foreach ($stations as $st) {
        $stName = $st['name'] ?? '';
        if ($stName === '') continue;
        foreach ($st['correspondences'] ?? [] as $c) {
            $mode = $c['mode'] ?? '';
            $code = (string)($c['line'] ?? '');
            if ($mode === '' || $code === '') continue;
            // Skip self
            if ($mode === 'M' && $code === $currentCode) continue;
            $key = "$mode-$code";
            if (!isset($groups[$key])) {
                $groups[$key] = [
                    'mode'       => $mode,
                    'code'       => $code,
                    'color'      => $c['color']      ?? '#999',
                    'color_text' => $c['color_text'] ?? '#FFF',
                    'stations'   => [],
                ];
            }
            if (!in_array($stName, $groups[$key]['stations'], true)) {
                $groups[$key]['stations'][] = $stName;
            }
        }
    }

    $metro = []; $rer = []; $other = [];
    foreach ($groups as $g) {
        $code = $g['code'];
        $mode = $g['mode'];
        $entry = [
            'code'       => $code,
            'color'      => $g['color'],
            'color_text' => $g['color_text'],
            'stations'   => $g['stations'],
        ];
        if ($mode === 'M') {
            // Pour metro on utilise les data canoniques de l'index si dispo
            if (isset($metroIdx[$code])) {
                $entry['name']       = $metroIdx[$code]['name'];
                $entry['color']      = $metroIdx[$code]['color'];
                $entry['color_text'] = $metroIdx[$code]['color_text'];
                $entry['url']        = $metroIdx[$code]['url'];
            } else {
                $entry['name'] = "Ligne $code";
                $entry['url']  = "/metro/ligne-" . strtolower($code) . "/";
            }
            $metro[] = $entry;
        } elseif ($mode === 'RER') {
            $entry['name'] = "RER $code";
            $entry['url']  = "/rer/rer-" . strtolower($code) . "/";
            $rer[] = $entry;
        } elseif ($mode === 'T') {
            $entry['name'] = "Tramway T$code";
            $entry['url']  = "/tramway/t" . strtolower($code) . "/";
            $other[] = $entry;
        } elseif ($mode === 'TRANS') {
            $entry['name'] = "Transilien $code";
            $entry['url']  = "/transilien/" . strtolower($code) . "/";
            $other[] = $entry;
        }
    }

    // Tri : metro par code numerique croissant ; RER alpha ; other alpha
    usort($metro, fn($a, $b) => strnatcmp($a['code'], $b['code']));
    usort($rer,   fn($a, $b) => strcmp($a['code'], $b['code']));
    usort($other, fn($a, $b) => strcmp($a['name'], $b['name']));

    return [
        'connections_metro' => $metro,
        'connections_rer'   => $rer,
        'connections_other' => $other,
    ];
}

/**
 * Patches a appliquer si la cle est absente OU vide. Returns le diff
 * applique (pour le mode --dry-run).
 *
 * @param array $d JSON existant (modifié in-place)
 * @param array $ref JSON metro-1 (référence pour les structures à copier)
 * @param int|string $lineNum
 */
function apply_patches(array &$d, array $ref, int|string $lineNum): array {
    $diff = [];
    $patch = function (string $key, $value, $force = false) use (&$d, &$diff) {
        if ($force || !isset($d[$key]) || $d[$key] === null
            || (is_array($d[$key]) && empty($d[$key]))
            || (is_string($d[$key]) && trim($d[$key]) === '')) {
            $d[$key] = $value;
            $diff[$key] = '+' . (is_scalar($value) ? (string)$value : '(' . gettype($value) . ')');
        }
    };

    // 1. color_light : derivee de color
    $color = $d['color'] ?? '#999999';
    $patch('color_light', lighten_color($color, 0.8));

    // 2. automated_year (si la ligne est automatisee)
    if (($d['automated'] ?? false) && isset(AUTOMATED_YEAR[$lineNum])) {
        $patch('automated_year', AUTOMATED_YEAR[$lineNum]);
    }

    // 3. daily_riders (lookup table 2026)
    if (isset(DAILY_RIDERS[$lineNum])) {
        $patch('daily_riders', DAILY_RIDERS[$lineNum]);
    }

    // 4. terminus_a / terminus_b (si vraiment vides)
    if (isset(TERMINUS_FALLBACK[$lineNum])) {
        [$tA, $tB] = TERMINUS_FALLBACK[$lineNum];
        $patch('terminus_a', $tA);
        $patch('terminus_b', $tB);
    }

    // 5. fares : copie integralement de metro-1 (uniforme reseau)
    $patch('fares', $ref['fares'] ?? []);

    // 6. quick_actions : copie de metro-1 (template)
    $patch('quick_actions', $ref['quick_actions'] ?? []);

    // 7. meta (auteur + dates)
    $today = date('Y-m-d');
    $metaTpl = $ref['meta'] ?? [];
    if (isset($metaTpl['dates'])) {
        $metaTpl['dates'] = [
            'published' => $today,
            'updated'   => $today,
            'updated_human' => date('j F Y'),
        ];
    }
    $patch('meta', $metaTpl);

    // 8. seo : template avec interpolation du code de ligne
    $code = (string)($d['code'] ?? $lineNum);
    $tA = $d['terminus_a'] ?? '';
    $tB = $d['terminus_b'] ?? '';
    $count = (int)($d['stations_count'] ?? 0);
    $patch('seo', [
        'h1'          => "Métro Ligne $code Paris : plan, horaires et trafic",
        'title'       => "Métro Ligne $code Paris : plan, horaires et trafic temps réel",
        'description' => "Toute l'info sur la ligne $code du métro parisien : $count stations de $tA à $tB, horaires, trafic temps réel, correspondances et tourisme.",
        'lead'        => "Toute l'information sur la <strong>ligne $code du métro parisien</strong> : <strong>$count stations</strong> de <strong>$tA</strong> à <strong>$tB</strong>, horaires des premières et dernières rames, trafic en temps réel, correspondances avec les autres lignes, accessibilité PMR et incontournables touristiques le long du parcours.",
    ]);

    // 9. intros : 16 paragraphes seo (stubs vides — a enrichir manuellement)
    $patch('intros', [
        'introduction'   => '',
        'plan'           => '',
        'stations'       => '',
        'horaires'       => '',
        'trafic'         => '',
        'itineraires'    => '',
        'que_voir'       => '',
        'histoire'       => '',
        'accessibilite'  => '',
        'tarifs'         => '',
        'travaux'        => '',
        'faq'            => '',
        'articles_lies'  => '',
        'liens_internes' => '',
    ]);

    // 10. internal_links : auto-build depuis stations[].correspondences[]
    //     (connections_metro/rer/other) + discover_metro_lines = self + top 3
    //     les plus connectees + related_pages copie depuis metro-1 (uniformes).
    $stations = $d['stations'] ?? [];
    $connections = build_connections($stations, $lineNum);
    $internalLinks = array_merge($connections, [
        'discover_metro_lines' => build_discover_lines($lineNum, $connections['connections_metro']),
        'related_pages'        => $ref['internal_links']['related_pages'] ?? [],
    ]);
    // Force le re-calcul si l'internal_links existant est incomplet (n'a pas
    // les 5 keys attendues : connections_metro/rer/other + discover + related).
    $existing = $d['internal_links'] ?? [];
    $hasFullSet = isset($existing['connections_metro'], $existing['connections_rer'], $existing['connections_other']);
    if (!$hasFullSet) {
        $d['internal_links'] = $internalLinks;
        $diff['internal_links'] = '+rebuild (5 keys)';
    }

    // 11. Stubs editoriaux vides (a enrichir : aucune valeur par defaut sensible)
    $patch('history', ['paragraphs' => [], 'timeline' => []]);
    $patch('faq', []);
    $patch('accessibility', []);
    $patch('works', []);
    $patch('points_of_interest', []);
    $patch('tourism', []);
    $patch('tourist_routes', []);
    $patch('popular_routes', []);
    $patch('related_articles', []);

    // 12. hero_image : a remplir par scripts/build-line-hero.php
    $patch('hero_image', null);

    // 13. Stations : flag is_major sur chaque station si absent.
    //     Heuristique : terminus (premier/dernier) OR ≥3 correspondances.
    //     Pas defensif sur les composants line/* desormais (?? false partout)
    //     mais on flag quand meme proprement pour avoir un rendu visuel correct.
    if (isset($d['stations']) && is_array($d['stations'])) {
        $total = count($d['stations']);
        foreach ($d['stations'] as $i => &$station) {
            if (!isset($station['is_major'])) {
                $isTerminus = ($i === 0 || $i === $total - 1);
                $nCorresp = count($station['correspondences'] ?? []);
                $station['is_major'] = $isTerminus || $nCorresp >= 3;
                $diff["stations[$i].is_major"] = '+' . ($station['is_major'] ? 'true' : 'false');
            }
        }
        unset($station);
    }

    return $diff;
}

// =============================================================================
// MAIN
// =============================================================================

$opts = parse_cli_args($argv);
$lineArg = $opts['line'] ?? null;
if (!$lineArg) { fwrite(STDERR, "ERREUR : --line=N obligatoire (ex: --line=14, --line=3bis)\n"); exit(1); }

$dryRun    = (bool)($opts['dry-run']    ?? false);
$printOnly = (bool)($opts['print-only'] ?? false);

// Normalisation du numero (string si bis, int sinon)
$lineNum = is_numeric($lineArg) ? (int)$lineArg : (string)$lineArg;
$lineSlug = is_int($lineNum) ? "metro-$lineNum" : "metro-$lineNum";
$jsonPath = LINES_DIR . "/$lineSlug.json";

if (!is_file($jsonPath)) {
    fwrite(STDERR, "ERREUR : $jsonPath introuvable\n"); exit(1);
}
if (!is_file(REFERENCE_FILE)) {
    fwrite(STDERR, "ERREUR : reference metro-1.json introuvable\n"); exit(1);
}

log_info("Bootstrap ligne $lineNum (depuis $jsonPath)");
$d = json_decode(file_get_contents($jsonPath), true);
$ref = json_decode(file_get_contents(REFERENCE_FILE), true);
if (!is_array($d) || !is_array($ref)) {
    fwrite(STDERR, "ERREUR : JSON invalide\n"); exit(1);
}

$keysBefore = count($d);
$diff = apply_patches($d, $ref, $lineNum);
$keysAfter = count($d);

log_info("Champs ajoutes : " . count($diff) . " (avant: $keysBefore keys, apres: $keysAfter keys)");
foreach ($diff as $k => $v) {
    echo "  + $k : $v\n";
}

if ($printOnly) {
    echo "\n=== JSON resultat ===\n";
    echo pretty_json($d) . "\n";
    exit(0);
}

if ($dryRun) {
    log_info("MODE --dry-run : aucune ecriture. Relance sans le flag pour ecrire.");
    exit(0);
}

file_put_contents($jsonPath, pretty_json($d) . "\n");
log_info("JSON ecrit : $jsonPath");
log_info("Etapes suivantes :");
log_info("  1. Editer manuellement les stubs (intros, history, faq, points_of_interest, ...)");
log_info("  2. Ajouter une entree LINE_STRATEGY dans scripts/build-line-hero.php pour ligne $lineNum");
log_info("  3. php scripts/build-line-hero.php --line=$lineNum --review-only");
log_info("  4. Choisir un candidat puis : php scripts/build-line-hero.php --line=$lineNum --pick=\"<File:Title.jpg>\"");
log_info("  5. git push origin main → deploiement auto");
