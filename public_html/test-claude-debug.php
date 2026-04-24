<?php
/**
 * test-claude-debug.php
 *
 * Version de test avec affichage complet des erreurs PHP.
 * A utiliser si test-claude.php donne une erreur 500.
 */

// Force l'affichage de TOUTES les erreurs.
error_reporting(E_ALL);
ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');

declare(strict_types=1);

$TEST_SECRET = 'bougea-debug-2026-04-24-delete-me';
if (($_GET['key'] ?? '') !== $TEST_SECRET) {
    http_response_code(403);
    echo "Access denied. Add ?key=... to the URL.";
    exit;
}

header('Content-Type: text/html; charset=utf-8');
echo "<!DOCTYPE html><html lang='fr'><head><meta charset='UTF-8'>";
echo "<title>Debug Claude</title>";
echo "<style>body{font-family:-apple-system,sans-serif;max-width:1000px;margin:2rem auto;padding:1rem;line-height:1.5}";
echo "h1{color:#0F6E56}h2{color:#085041;border-bottom:1px solid #ccc}";
echo ".ok{color:green;font-weight:bold}.err{color:red;font-weight:bold;background:#fee;padding:.5rem;border-radius:4px}";
echo "pre{background:#1A2B26;color:#E1F5EE;padding:1rem;border-radius:4px;overflow-x:auto;font-size:.85rem;white-space:pre-wrap}</style></head><body>";

echo "<h1>🔍 Debug Claude</h1>";
echo "<p><small>Date : " . date('Y-m-d H:i:s') . " | PHP : " . PHP_VERSION . "</small></p>";

// === Check 1 : Version PHP ===
echo "<h2>1. Version PHP</h2>";
echo "<p>Version : <strong>" . PHP_VERSION . "</strong></p>";
if (version_compare(PHP_VERSION, '8.0.0', '<')) {
    echo "<p class='err'>❌ PHP trop ancien. Il faut au moins 8.0.</p>";
} else {
    echo "<p class='ok'>✅ Version PHP suffisante</p>";
}

// === Check 2 : Extensions PHP ===
echo "<h2>2. Extensions requises</h2>";
$required = ['curl', 'json', 'mbstring'];
foreach ($required as $ext) {
    if (extension_loaded($ext)) {
        echo "<p class='ok'>✅ Extension <code>{$ext}</code> disponible</p>";
    } else {
        echo "<p class='err'>❌ Extension <code>{$ext}</code> MANQUANTE</p>";
    }
}

// === Check 3 : Fichiers presents ===
echo "<h2>3. Fichiers</h2>";
$files = [
    'config/secrets.php' => __DIR__ . '/config/secrets.php',
    'core/ClaudeClient.php' => __DIR__ . '/core/ClaudeClient.php',
    'core/PrimClient.php' => __DIR__ . '/core/PrimClient.php',
    'core/DisruptionFilter.php' => __DIR__ . '/core/DisruptionFilter.php',
    'core/DisruptionFormatter.php' => __DIR__ . '/core/DisruptionFormatter.php',
    'config/networks.php' => __DIR__ . '/config/networks.php',
];
foreach ($files as $label => $path) {
    if (file_exists($path)) {
        echo "<p class='ok'>✅ {$label} existe</p>";
    } else {
        echo "<p class='err'>❌ {$label} MANQUANT</p>";
    }
}

// === Check 4 : Chargement secrets ===
echo "<h2>4. Secrets</h2>";
try {
    if (!file_exists(__DIR__ . '/config/secrets.php')) {
        throw new RuntimeException('config/secrets.php introuvable');
    }
    $secrets = require __DIR__ . '/config/secrets.php';
    if (!is_array($secrets)) {
        throw new RuntimeException('secrets.php doit retourner un array');
    }

    $keyChecks = ['PRIM_API_KEY', 'ANTHROPIC_API_KEY', 'UNSPLASH_ACCESS_KEY'];
    foreach ($keyChecks as $k) {
        if (isset($secrets[$k]) && !empty($secrets[$k])) {
            $preview = substr((string) $secrets[$k], 0, 10) . '...';
            echo "<p class='ok'>✅ {$k} présente ({$preview})</p>";
        } else {
            echo "<p class='err'>⚠️ {$k} manquante ou vide</p>";
        }
    }

    // Verifier le format de la cle Anthropic.
    $anthropicKey = (string) ($secrets['ANTHROPIC_API_KEY'] ?? '');
    if (!str_starts_with($anthropicKey, 'sk-ant-')) {
        echo "<p class='err'>❌ ANTHROPIC_API_KEY ne commence pas par 'sk-ant-'. Format incorrect ?</p>";
    } else {
        echo "<p class='ok'>✅ Format ANTHROPIC_API_KEY correct</p>";
    }
} catch (Throwable $e) {
    echo "<p class='err'>❌ Erreur : " . htmlspecialchars($e->getMessage()) . "</p>";
}

// === Check 5 : Chargement ClaudeClient ===
echo "<h2>5. Chargement ClaudeClient</h2>";
try {
    require_once __DIR__ . '/core/ClaudeClient.php';
    echo "<p class='ok'>✅ ClaudeClient.php charge sans erreur</p>";

    if (class_exists('ClaudeClient')) {
        echo "<p class='ok'>✅ Classe ClaudeClient existe</p>";
    } else {
        echo "<p class='err'>❌ Classe ClaudeClient introuvable</p>";
    }
} catch (Throwable $e) {
    echo "<p class='err'>❌ Erreur lors du chargement : " . htmlspecialchars($e->getMessage()) . "</p>";
    echo "<pre>" . htmlspecialchars($e->getTraceAsString()) . "</pre>";
    exit;
}

// === Check 6 : Instanciation ===
echo "<h2>6. Instanciation</h2>";
try {
    $anthropicKey = (string) ($secrets['ANTHROPIC_API_KEY'] ?? '');
    $client = new ClaudeClient($anthropicKey);
    echo "<p class='ok'>✅ ClaudeClient instancie</p>";
} catch (Throwable $e) {
    echo "<p class='err'>❌ Erreur instanciation : " . htmlspecialchars($e->getMessage()) . "</p>";
    echo "<pre>" . htmlspecialchars($e->getTraceAsString()) . "</pre>";
    exit;
}

// === Check 7 : Appel API minimaliste ===
echo "<h2>7. Appel API (test minimal)</h2>";
echo "<p>Envoi d'un message de 1 mot a Claude...</p>";

try {
    $startTime = microtime(true);
    $result = $client->generate(
        'Tu es un assistant. Reponds en francais.',
        'Dis juste "OK"',
        50,
        0.0
    );
    $duration = round((microtime(true) - $startTime) * 1000, 1);

    if ($result === null) {
        echo "<p class='err'>❌ L'appel a echoue (result = null)</p>";

        // Essayer de lire le dernier error_log.
        echo "<p><em>Le detail de l'erreur est dans error_log PHP. Verifie /public_html/error_log sur o2switch.</em></p>";
    } else {
        echo "<p class='ok'>✅ Reponse recue en {$duration} ms</p>";
        echo "<p><strong>Texte :</strong> " . htmlspecialchars($result['text']) . "</p>";
        echo "<p><strong>Tokens :</strong> {$result['usage']['input_tokens']} in + {$result['usage']['output_tokens']} out</p>";
        echo "<p><strong>Cout :</strong> " . number_format($result['usage']['cost_eur'], 6) . " €</p>";
    }
} catch (Throwable $e) {
    echo "<p class='err'>❌ Exception : " . htmlspecialchars($e->getMessage()) . "</p>";
    echo "<pre>" . htmlspecialchars($e->getTraceAsString()) . "</pre>";
}

echo "<hr><p><small>Si tout est vert mais l'appel API echoue, regarde <code>/public_html/error_log</code> pour plus de detail.</small></p>";

echo "</body></html>";
