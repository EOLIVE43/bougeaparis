<?php
/**
 * scripts/generate-article.php
 *
 * Script CLI pour generer l'article quotidien.
 * Execute par GitHub Actions chaque matin.
 *
 * Usage (local) :
 *   php scripts/generate-article.php
 *
 * Variables d'environnement requises :
 *   - PRIM_API_KEY
 *   - ANTHROPIC_API_KEY
 *   - DISABLE_AUTO_PUBLICATION (optionnel, "true" pour desactiver)
 *
 * Sortie :
 *   - Ecrit le fichier dans content/info-trafic/
 *   - Logs sur stdout
 *   - Exit code 0 si OK, 1 sinon
 */

// Seulement en CLI
if (php_sapi_name() !== 'cli') {
    die("Ce script doit etre execute en ligne de commande.\n");
}

// Racine du projet (depuis scripts/)
$projectRoot = dirname(__DIR__);

require_once $projectRoot . '/core/PrimClient.php';
require_once $projectRoot . '/core/DisruptionFilter.php';
require_once $projectRoot . '/core/DisruptionFormatter.php';
require_once $projectRoot . '/core/ClaudeClient.php';
require_once $projectRoot . '/core/AngleRotator.php';
require_once $projectRoot . '/core/ArticlePrompt.php';

// Helpers de log (sortent sur stdout pour GitHub Actions)
function log_info($msg) {
    echo '[' . date('H:i:s') . '] ' . $msg . "\n";
}

function log_error($msg) {
    fwrite(STDERR, '[' . date('H:i:s') . '] ERROR: ' . $msg . "\n");
}

log_info('=== Generation article BougeaParis.fr ===');
log_info('Date : ' . date('Y-m-d H:i:s'));

// 1. Verifier le panic button
$disableFlag = getenv('DISABLE_AUTO_PUBLICATION');
if ($disableFlag === 'true' || $disableFlag === '1') {
    log_info('DISABLE_AUTO_PUBLICATION active. Generation annulee.');
    exit(0);
}

// 2. Recuperer les cles API
$primKey = getenv('PRIM_API_KEY');
$anthropicKey = getenv('ANTHROPIC_API_KEY');

if (empty($primKey) || empty($anthropicKey)) {
    log_error('Cles API manquantes (PRIM_API_KEY ou ANTHROPIC_API_KEY).');
    exit(1);
}

log_info('Cles API chargees');

// 3. Charger la config networks
$networks = require $projectRoot . '/config/networks.php';

try {
    // 4. PRIM
    log_info('[1/6] Recuperation PRIM...');
    $prim = new PrimClient($primKey, sys_get_temp_dir() . '/prim-cache');
    $primData = $prim->fetchDisruptions();
    if ($primData === null) {
        log_error('Echec recuperation PRIM');
        exit(1);
    }
    log_info('  -> ' . count($primData['disruptions']) . ' perturbations brutes');

    // 5. Filter
    log_info('[2/6] Filtrage Option B...');
    $filter = new DisruptionFilter($networks);
    $filtered = $filter->filter($primData);
    $stats = DisruptionFilter::computeStats($filtered);
    log_info('  -> ' . $stats['total'] . ' perturbations retenues');
    log_info('  -> ' . $stats['bloquante'] . ' bloquantes, ' . $stats['perturbee'] . ' perturbees');

    // 6. Formatter
    log_info('[3/6] Formatage pour Claude...');
    $formatter = new DisruptionFormatter($networks);
    $formatted = $formatter->formatForClaude($filtered);
    log_info('  -> ' . mb_strlen($formatted) . ' caracteres');

    // 7. Angle du jour
    log_info('[4/6] Selection de l angle...');
    $rotator = new AngleRotator();
    $angle = $rotator->getAngleForToday();
    log_info('  -> ' . $angle['day_label'] . ' : ' . $angle['titre_type']);

    // 8. Construire les prompts
    $today = date('Y-m-d');
    $systemPrompt = ArticlePrompt::buildSystemPrompt($angle, $today);
    $userMessage = ArticlePrompt::buildUserMessage($formatted, $stats, $today);

    // 9. Generation Claude
    log_info('[5/6] Generation Claude (peut prendre 30-60s)...');
    $startTime = microtime(true);
    $client = new ClaudeClient($anthropicKey);
    $result = $client->generate($systemPrompt, $userMessage, 3000, 0.7);
    $duration = round(microtime(true) - $startTime, 1);

    if ($result === null) {
        log_error('Claude a echoue : ' . $client->getLastError());
        exit(1);
    }

    log_info('  -> Article genere en ' . $duration . 's');
    log_info('  -> ' . $result['usage']['input_tokens'] . ' in + ' . $result['usage']['output_tokens'] . ' out');
    log_info('  -> Cout : ' . $result['usage']['cost_eur'] . ' EUR');

   // 10. Nettoyer l'article (retirer marqueurs ad-slot)
    $articleMd = $result['text'];
    $articleMd = str_replace('<!-- ad-slot: in-article-1 -->', '', $articleMd);
    $articleMd = str_replace('<!-- ad-slot: in-article-2 -->', '', $articleMd);
    $articleMd = preg_replace("/\n{3,}/", "\n\n", $articleMd);

    // 11. Extraire le titre (H1) et le chapo (premier paragraphe)
    $extractedTitle = 'Info trafic du ' . $today;
    $extractedExcerpt = 'Bulletin trafic quotidien du reseau francilien.';

    $lines = explode("\n", $articleMd);
    $foundTitle = false;
    $foundExcerpt = false;

    foreach ($lines as $i => $line) {
        $trimmed = trim($line);

        // Extraction du H1 (premiere ligne commencant par "# ")
        if (!$foundTitle && strpos($trimmed, '# ') === 0 && strpos($trimmed, '## ') !== 0) {
            $extractedTitle = trim(substr($trimmed, 2));
            $foundTitle = true;
            continue;
        }

        // Extraction du chapo : premier paragraphe non vide apres le H1,
        // qui n'est pas un titre (#), ni une liste (-, *), ni un blockquote (>)
        if ($foundTitle && !$foundExcerpt && $trimmed !== '') {
            if ($trimmed[0] !== '#' && $trimmed[0] !== '-' && $trimmed[0] !== '*' && $trimmed[0] !== '>') {
                $extractedExcerpt = $trimmed;
                // Tronquer a 200 caracteres si trop long
                if (mb_strlen($extractedExcerpt) > 200) {
                    $extractedExcerpt = mb_substr($extractedExcerpt, 0, 197) . '...';
                }
                $foundExcerpt = true;
                break;
            }
        }
    }

    log_info('  -> Titre extrait : ' . $extractedTitle);
    log_info('  -> Chapo extrait : ' . mb_substr($extractedExcerpt, 0, 80) . '...');

    // 12. Retirer le H1 du corps Markdown (il est deja dans le front-matter)
    $articleMdWithoutH1 = preg_replace('/^#\s+.+\n+/m', '', $articleMd, 1);
    // Nettoyer aussi le chapo qui suit le H1 (il est deja dans excerpt)
    // On ne retire PAS le chapo : il fait partie integrante de l'article.
    // Le front-matter excerpt est utilise uniquement pour les meta-descriptions et listings.

    // 13. Echapper les caracteres YAML problematiques dans le front-matter
    $safeTitle = str_replace(array('"', "\n", "\r"), array("'", ' ', ''), $extractedTitle);
    $safeExcerpt = str_replace(array('"', "\n", "\r"), array("'", ' ', ''), $extractedExcerpt);

    // 14. Construire le front-matter
    $slug = $today . '-bulletin-' . $angle['code'];

    $fm = "---\n";
    $fm .= 'title: "' . $safeTitle . "\"\n";
    $fm .= 'excerpt: "' . $safeExcerpt . "\"\n";
    $fm .= "date: " . $today . "\n";
    $fm .= "author: ludo\n";
    $fm .= "image: /assets/images/info-trafic/bienvenue.jpg\n";
    $fm .= "image_alt: Metro parisien\n";
    $fm .= "category: trafic\n";
    $fm .= "stats_bloquante: " . $stats['bloquante'] . "\n";
    $fm .= "stats_perturbee: " . $stats['perturbee'] . "\n";
    $fm .= "stats_information: " . $stats['information'] . "\n";
    $fm .= "stats_total: " . $stats['total'] . "\n";
    $fm .= "---\n\n";

    $finalContent = $fm . $articleMdWithoutH1;

    // 12. Sauvegarde article Markdown
    log_info('[6/7] Sauvegarde article...');
    $targetDir = $projectRoot . '/content/info-trafic/';
    if (!is_dir($targetDir)) {
        mkdir($targetDir, 0755, true);
    }
    $targetFile = $targetDir . $slug . '.md';

    $written = file_put_contents($targetFile, $finalContent);
    if ($written === false) {
        log_error('Echec ecriture article : ' . $targetFile);
        exit(1);
    }

    log_info('  -> ' . $written . ' octets ecrits');
    log_info('  -> Fichier : content/info-trafic/' . $slug . '.md');

    // 13. Sauvegarde du JSON des lignes (pour widget de recherche)
    log_info('[7/7] Sauvegarde JSON des lignes...');
    $byLine = $formatter->groupByLine($filtered);

    // Calculer les stats par mode (metro, rer, tramway, transilien, bus)
    $statsByMode = array(
        'metro'      => array('bloquante' => 0, 'perturbee' => 0, 'information' => 0, 'total' => 0),
        'rer'        => array('bloquante' => 0, 'perturbee' => 0, 'information' => 0, 'total' => 0),
        'tramway'    => array('bloquante' => 0, 'perturbee' => 0, 'information' => 0, 'total' => 0),
        'transilien' => array('bloquante' => 0, 'perturbee' => 0, 'information' => 0, 'total' => 0),
        'bus'        => array('bloquante' => 0, 'perturbee' => 0, 'information' => 0, 'total' => 0),
    );

    $modeMap = array(
        'Metro'        => 'metro',
        'RapidTransit' => 'rer',
        'Tramway'      => 'tramway',
        'LocalTrain'   => 'transilien',
        'Bus'          => 'bus',
    );

    foreach ($filtered as $d) {
        $primaryMode = isset($d['primary_mode']) ? $d['primary_mode'] : '';
        $modeKey = isset($modeMap[$primaryMode]) ? $modeMap[$primaryMode] : null;
        if ($modeKey === null) continue;

        $sev = strtolower($d['severity']);
        if (isset($statsByMode[$modeKey][$sev])) {
            $statsByMode[$modeKey][$sev]++;
        }
        $statsByMode[$modeKey]['total']++;
    }

    $trafficData = array(
        'generated_at' => date('c'),
        'date' => $today,
        'article_slug' => $slug,
        'article_url' => '/info-trafic/' . $slug . '/',
        'total_disruptions' => $stats['total'],
        'stats_total' => array(
            'bloquante'   => $stats['bloquante'],
            'perturbee'   => $stats['perturbee'],
            'information' => $stats['information'],
            'total'       => $stats['total'],
        ),
        'stats_by_mode' => $statsByMode,
        'lines' => $byLine,
    );

    $trafficDir = $projectRoot . '/data/traffic/';
    if (!is_dir($trafficDir)) {
        mkdir($trafficDir, 0755, true);
    }
    $trafficFile = $trafficDir . $today . '.json';

    $trafficJson = json_encode($trafficData, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    $trafficWritten = file_put_contents($trafficFile, $trafficJson);

    if ($trafficWritten === false) {
        log_error('Echec ecriture JSON trafic');
        // Non bloquant : on continue
    } else {
        log_info('  -> ' . $trafficWritten . ' octets ecrits');
        log_info('  -> Fichier : data/traffic/' . $today . '.json');
        log_info('  -> ' . count($byLine) . ' lignes impactees');
    }

    // 14. Sauvegarde du "dernier en date" (alias pour le widget)
    $latestFile = $trafficDir . 'latest.json';
    @copy($trafficFile, $latestFile);
    log_info('  -> Alias latest.json mis a jour');

    log_info('=== Generation terminee avec succes ===');
    exit(0);

} catch (Throwable $e) {
    log_error('Exception : ' . $e->getMessage());
    log_error($e->getTraceAsString());
    exit(1);
}
