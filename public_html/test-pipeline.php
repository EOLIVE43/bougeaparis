<?php
/**
 * test-pipeline.php
 *
 * Script de test pour valider le pipeline complet :
 *   PrimClient -> DisruptionFilter -> DisruptionFormatter
 *
 * Sortie : affichage du texte qui sera envoye a Claude + stats + aperçu JSON widgets.
 *
 * A SUPPRIMER apres validation.
 */

declare(strict_types=1);

$TEST_SECRET = 'bougea-test-pipeline-2026-04-24-delete-me';
if (($_GET['key'] ?? '') !== $TEST_SECRET) {
    http_response_code(403);
    echo "Access denied. Add ?key=... to the URL.";
    exit;
}

// Charger les secrets.
$primKey = '';
if (file_exists(__DIR__ . '/config/secrets.php')) {
    $secrets = require __DIR__ . '/config/secrets.php';
    $primKey = $secrets['PRIM_API_KEY'] ?? '';
}
if (empty($primKey)) {
    die("ERROR: PRIM_API_KEY not found in config/secrets.php\n");
}

// Charger les classes et config.
require_once __DIR__ . '/core/PrimClient.php';
require_once __DIR__ . '/core/DisruptionFilter.php';
require_once __DIR__ . '/core/DisruptionFormatter.php';

$networksConfig = require __DIR__ . '/config/networks.php';

// HTML header.
header('Content-Type: text/html; charset=utf-8');
echo "<!DOCTYPE html><html lang='fr'><head><meta charset='UTF-8'>";
echo "<title>Test Pipeline - BougeaParis.fr</title>";
echo "<style>body{font-family:-apple-system,sans-serif;max-width:1100px;margin:2rem auto;padding:1rem;line-height:1.5;color:#1A2B26}";
echo "h1{color:#0F6E56}h2{color:#085041;border-bottom:2px solid #E0E6E4;padding-bottom:.3rem;margin-top:2rem}";
echo ".ok{color:#1D9E75;font-weight:bold}.err{color:#A32D2D;font-weight:bold}";
echo ".stat{background:#E1F5EE;padding:1rem;border-radius:8px;margin:1rem 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem}";
echo ".stat div strong{display:block;color:#085041;font-size:.9em;text-transform:uppercase;letter-spacing:.5px}";
echo ".stat div span{font-size:1.8em;font-weight:bold;color:#0F6E56}";
echo "pre{background:#1A2B26;color:#E1F5EE;padding:1.5rem;border-radius:8px;overflow-x:auto;font-size:.82rem;line-height:1.5;white-space:pre-wrap;word-wrap:break-word}";
echo ".claude-preview{background:#FFF8E1;border-left:4px solid #E5B000;padding:1rem 1.5rem;margin:1rem 0;border-radius:0 8px 8px 0}";
echo ".widgets-preview{background:#F7F9F8;border:1px solid #E0E6E4;padding:1rem;border-radius:8px;max-height:400px;overflow:auto;font-family:monospace;font-size:.8em}</style></head><body>";

echo "<h1>🧪 Test Pipeline : PrimClient → DisruptionFilter → DisruptionFormatter</h1>";
echo "<p><small>Date : " . date('Y-m-d H:i:s') . " | PHP : " . PHP_VERSION . "</small></p>";

try {
    // ====================================================================
    // ETAPE 1 : Recuperer les donnees PRIM
    // ====================================================================
    echo "<h2>Étape 1 — Récupération PRIM</h2>";
    $client = new PrimClient($primKey, sys_get_temp_dir() . '/prim-cache');
    $startTime = microtime(true);
    $primData = $client->fetchDisruptions();
    $fetchTime = round((microtime(true) - $startTime) * 1000, 1);

    if ($primData === null) {
        echo "<p class='err'>❌ Echec PRIM</p>";
        exit;
    }

    echo "<p class='ok'>✅ PRIM OK en {$fetchTime} ms</p>";
    echo "<div class='stat'>";
    echo "<div><strong>Perturbations brutes</strong><span>" . count($primData['disruptions']) . "</span></div>";
    echo "<div><strong>Lignes référencées</strong><span>" . count($primData['lines']) . "</span></div>";
    echo "<div><strong>Dernière MAJ IDFM</strong><span style='font-size:.9em'>" . htmlspecialchars($primData['lastUpdatedDate']) . "</span></div>";
    echo "</div>";

    // ====================================================================
    // ETAPE 2 : Filtrer (scope Option B)
    // ====================================================================
    echo "<h2>Étape 2 — Filtrage (Option B)</h2>";
    $filter = new DisruptionFilter($networksConfig);
    $startTime = microtime(true);
    $filtered = $filter->filter($primData);
    $filterTime = round((microtime(true) - $startTime) * 1000, 1);

    $stats = DisruptionFilter::computeStats($filtered);

    echo "<p class='ok'>✅ Filtrage OK en {$filterTime} ms</p>";
    echo "<div class='stat'>";
    echo "<div><strong>Après filtrage</strong><span>{$stats['total']}</span></div>";
    echo "<div><strong>Bloquante</strong><span>{$stats['bloquante']}</span></div>";
    echo "<div><strong>Perturbée</strong><span>{$stats['perturbee']}</span></div>";
    echo "<div><strong>Info</strong><span>{$stats['information']}</span></div>";
    echo "</div>";
    echo "<div class='stat'>";
    echo "<div><strong>Métro</strong><span>{$stats['metro']}</span></div>";
    echo "<div><strong>RER</strong><span>{$stats['rer']}</span></div>";
    echo "<div><strong>Tramway</strong><span>{$stats['tramway']}</span></div>";
    echo "<div><strong>Transilien</strong><span>{$stats['transilien']}</span></div>";
    echo "<div><strong>Bus Paris (bloq.)</strong><span>{$stats['bus']}</span></div>";
    echo "</div>";

    // ====================================================================
    // ETAPE 3 : Formater pour Claude
    // ====================================================================
    echo "<h2>Étape 3 — Format Claude</h2>";
    $formatter = new DisruptionFormatter($networksConfig);
    $startTime = microtime(true);
    $claudeText = $formatter->formatForClaude($filtered);
    $formatTime = round((microtime(true) - $startTime) * 1000, 1);

    $chars = mb_strlen($claudeText);
    $words = str_word_count(strip_tags($claudeText));
    // Estimation tokens (~1 token = 4 caracteres en francais).
    $tokensEstimate = (int) ceil($chars / 4);

    echo "<p class='ok'>✅ Formatage OK en {$formatTime} ms</p>";
    echo "<div class='stat'>";
    echo "<div><strong>Caractères</strong><span>" . number_format($chars) . "</span></div>";
    echo "<div><strong>Mots</strong><span>" . number_format($words) . "</span></div>";
    echo "<div><strong>Tokens (estim.)</strong><span>" . number_format($tokensEstimate) . "</span></div>";
    echo "<div><strong>Coût Claude (estim.)</strong><span>~" . round($tokensEstimate * 3.0 / 1_000_000, 4) . " €</span></div>";
    echo "</div>";

    // ====================================================================
    // ETAPE 4 : Aperçu du texte envoyé à Claude
    // ====================================================================
    echo "<h2>Étape 4 — Aperçu texte envoyé à Claude (top 30 lignes)</h2>";
    echo "<div class='claude-preview'>";
    $previewLines = array_slice(explode("\n", $claudeText), 0, 40);
    echo "<pre>" . htmlspecialchars(implode("\n", $previewLines)) . "\n\n[... texte complet : {$chars} caractères]</pre>";
    echo "</div>";

    // ====================================================================
    // ETAPE 5 : JSON par ligne (widgets)
    // ====================================================================
    echo "<h2>Étape 5 — JSON par ligne (pour widgets)</h2>";
    $byLine = $formatter->groupByLine($filtered);
    echo "<p class='ok'>✅ " . count($byLine) . " lignes avec au moins une perturbation</p>";

    echo "<p><strong>Liste des lignes :</strong></p><p>";
    $labels = [];
    foreach ($byLine as $key => $data) {
        $labels[] = $data['line']['label'] . ' (' . count($data['disruptions']) . ')';
    }
    echo htmlspecialchars(implode(' • ', $labels));
    echo "</p>";

    // Aperçu JSON pour la première ligne.
    echo "<h3>Aperçu JSON (première ligne)</h3>";
    echo "<div class='widgets-preview'>";
    $firstKey = array_key_first($byLine);
    if ($firstKey !== null) {
        echo "<pre style='background:none;color:#1A2B26;padding:0'>" . htmlspecialchars(json_encode(
            $byLine[$firstKey],
            JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
        )) . "</pre>";
    }
    echo "</div>";

    echo "<h2>✅ Pipeline validé</h2>";
    echo "<p>Les trois briques (PrimClient, DisruptionFilter, DisruptionFormatter) fonctionnent ensemble.</p>";
    echo "<p>Prochaine étape : <strong>ClaudeClient.php</strong> + prompt éditorial.</p>";
    echo "<p class='err'>⚠️ SUPPRIME CE FICHIER APRES VALIDATION</p>";

} catch (Throwable $e) {
    echo "<p class='err'>❌ Erreur : " . htmlspecialchars($e->getMessage()) . "</p>";
    echo "<pre>" . htmlspecialchars($e->getTraceAsString()) . "</pre>";
}

echo "</body></html>";
