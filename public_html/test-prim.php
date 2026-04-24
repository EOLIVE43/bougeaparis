<?php
/**
 * test-prim.php
 *
 * Script de test STANDALONE pour valider PrimClient en live.
 *
 * Usage :
 *   1. Placer ce fichier a la racine de /public_html/
 *   2. Acceder a https://bougeaparis.fr/test-prim.php?key=SECRET_DE_TEST
 *   3. Verifier que l'appel PRIM reussit et affiche des stats
 *   4. SUPPRIMER CE FICHIER apres validation (securite)
 *
 * IMPORTANT : ce fichier contient une protection par cle secrete pour eviter
 * que n'importe qui puisse l'appeler (car il utilise la vraie cle PRIM).
 */

declare(strict_types=1);

// Protection basique : cle secrete dans l'URL pour empecher les acces non autorises.
// A CHANGER a chaque deploiement de test.
$TEST_SECRET = 'bougea-test-2026-04-24-delete-me';

if (($_GET['key'] ?? '') !== $TEST_SECRET) {
    http_response_code(403);
    echo "Access denied. Add ?key=... to the URL.";
    exit;
}

// Charge la cle API PRIM depuis les variables d'environnement ou un fichier secret.
// En prod, passe par config/secrets.php.
$primKey = getenv('PRIM_API_KEY') ?: '';

// Fallback : lecture depuis config/secrets.php si disponible.
if (empty($primKey) && file_exists(__DIR__ . '/config/secrets.php')) {
    $secrets = require __DIR__ . '/config/secrets.php';
    $primKey = $secrets['PRIM_API_KEY'] ?? '';
}

if (empty($primKey)) {
    die("ERROR: PRIM_API_KEY not found. Set it via env var or config/secrets.php.\n");
}

// Charge la classe PrimClient.
require_once __DIR__ . '/core/PrimClient.php';

// Prepare l'affichage HTML.
header('Content-Type: text/html; charset=utf-8');
echo "<!DOCTYPE html><html lang='fr'><head><meta charset='UTF-8'>";
echo "<title>Test PrimClient - BougeaParis.fr</title>";
echo "<style>body{font-family:-apple-system,sans-serif;max-width:960px;margin:2rem auto;padding:1rem;line-height:1.5;color:#1A2B26}";
echo "h1{color:#0F6E56}h2{color:#085041;border-bottom:2px solid #E0E6E4;padding-bottom:.3rem;margin-top:2rem}";
echo ".ok{color:#1D9E75;font-weight:bold}.err{color:#A32D2D;font-weight:bold}";
echo ".stat{background:#E1F5EE;padding:1rem;border-radius:8px;margin:1rem 0}";
echo "pre{background:#F1F3F2;padding:1rem;border-radius:8px;overflow-x:auto;font-size:.85rem}";
echo "table{border-collapse:collapse;width:100%;margin:1rem 0}";
echo "th,td{text-align:left;padding:.5rem 1rem;border-bottom:1px solid #E0E6E4}";
echo "th{background:#F7F9F8}</style></head><body>";

echo "<h1>🧪 Test PrimClient.php</h1>";
echo "<p><small>Date : " . date('Y-m-d H:i:s') . " | PHP : " . PHP_VERSION . "</small></p>";

try {
    echo "<h2>1. Instanciation de PrimClient</h2>";
    $client = new PrimClient($primKey, sys_get_temp_dir() . '/prim-cache-test');
    echo "<p class='ok'>✅ PrimClient instancie avec succes</p>";

    echo "<h2>2. Appel API PRIM (force refresh)</h2>";
    $startTime = microtime(true);
    $data = $client->fetchDisruptions(forceRefresh: true);
    $duration = round((microtime(true) - $startTime) * 1000, 1);

    $lastResp = $client->getLastResponse();
    echo "<div class='stat'>";
    echo "<strong>Duree HTTP :</strong> {$duration} ms<br>";
    echo "<strong>HTTP code :</strong> " . ($lastResp['http_code'] ?? 'N/A') . "<br>";
    echo "<strong>Bytes recus :</strong> " . number_format($lastResp['bytes'] ?? 0) . "<br>";
    echo "<strong>Curl error :</strong> " . ($lastResp['curl_error'] ?: 'aucune') . "<br>";
    echo "</div>";

    if ($data === null) {
        echo "<p class='err'>❌ Appel API echoue. Verifier la cle API et la connectivite.</p>";
        exit;
    }

    echo "<p class='ok'>✅ Appel API reussi</p>";

    echo "<h2>3. Analyse de la reponse</h2>";

    $disruptions = $data['disruptions'] ?? [];
    $lines       = $data['lines'] ?? [];
    $lastUpdate  = $data['lastUpdatedDate'] ?? 'N/A';

    echo "<div class='stat'>";
    echo "<strong>Perturbations totales :</strong> " . count($disruptions) . "<br>";
    echo "<strong>Lignes referencees :</strong> " . count($lines) . "<br>";
    echo "<strong>Derniere MAJ IDFM :</strong> " . htmlspecialchars($lastUpdate) . "<br>";
    echo "</div>";

    // Stats par severite.
    echo "<h2>4. Distribution par severite</h2>";
    $bySeverity = [];
    foreach ($disruptions as $d) {
        $sev = $d['severity'] ?? 'UNKNOWN';
        $bySeverity[$sev] = ($bySeverity[$sev] ?? 0) + 1;
    }
    arsort($bySeverity);
    echo "<table><tr><th>Severite</th><th>Nombre</th></tr>";
    foreach ($bySeverity as $sev => $count) {
        echo "<tr><td>" . htmlspecialchars($sev) . "</td><td>{$count}</td></tr>";
    }
    echo "</table>";

    // Stats par cause.
    echo "<h2>5. Distribution par cause</h2>";
    $byCause = [];
    foreach ($disruptions as $d) {
        $cause = $d['cause'] ?? 'UNKNOWN';
        $byCause[$cause] = ($byCause[$cause] ?? 0) + 1;
    }
    arsort($byCause);
    echo "<table><tr><th>Cause</th><th>Nombre</th></tr>";
    foreach ($byCause as $cause => $count) {
        echo "<tr><td>" . htmlspecialchars($cause) . "</td><td>{$count}</td></tr>";
    }
    echo "</table>";

    // Stats par mode.
    echo "<h2>6. Distribution par mode de transport</h2>";
    $byMode = [];
    foreach ($lines as $line) {
        $mode = $line['mode'] ?? 'UNKNOWN';
        $byMode[$mode] = ($byMode[$mode] ?? 0) + 1;
    }
    arsort($byMode);
    echo "<table><tr><th>Mode</th><th>Lignes impactees</th></tr>";
    foreach ($byMode as $mode => $count) {
        echo "<tr><td>" . htmlspecialchars($mode) . "</td><td>{$count}</td></tr>";
    }
    echo "</table>";

    // Aperçu 3 perturbations métro/RER.
    echo "<h2>7. Aperçu : perturbations Métro/RER</h2>";
    $today = date('Ymd');

    // Index : disruptionId -> lignes impactées.
    $disruptionLines = [];
    foreach ($lines as $line) {
        foreach ($line['impactedObjects'] ?? [] as $impact) {
            foreach ($impact['disruptionIds'] ?? [] as $did) {
                $disruptionLines[$did][] = [
                    'mode'      => $line['mode'] ?? '',
                    'name'      => $line['name'] ?? '',
                    'shortName' => $line['shortName'] ?? '',
                ];
            }
        }
    }

    $shown = 0;
    foreach ($disruptions as $d) {
        // Actif aujourd'hui ?
        $active = false;
        foreach ($d['applicationPeriods'] ?? [] as $ap) {
            $begin = substr((string)($ap['begin'] ?? ''), 0, 8);
            $end   = substr((string)($ap['end'] ?? ''), 0, 8);
            if ($begin <= $today && $today <= $end) {
                $active = true;
                break;
            }
        }
        if (!$active) continue;

        $dLines = $disruptionLines[$d['id']] ?? [];
        $majorLines = array_filter($dLines, fn($l) => in_array($l['mode'], ['Metro', 'RapidTransit'], true));
        if (empty($majorLines)) continue;

        $lineNames = array_map(fn($l) => $l['mode'] . ' ' . $l['shortName'], $majorLines);
        echo "<div style='border:1px solid #E0E6E4;border-radius:8px;padding:1rem;margin:1rem 0'>";
        echo "<strong>Ligne(s) :</strong> " . htmlspecialchars(implode(', ', $lineNames)) . "<br>";
        echo "<strong>Severite :</strong> " . htmlspecialchars($d['severity'] ?? '') . "<br>";
        echo "<strong>Cause :</strong> " . htmlspecialchars($d['cause'] ?? '') . "<br>";
        echo "<strong>Titre :</strong> " . htmlspecialchars($d['title'] ?? '') . "<br>";
        echo "</div>";

        if (++$shown >= 3) break;
    }

    echo "<h2>8. Test du cache</h2>";
    $startCache = microtime(true);
    $dataCached = $client->fetchDisruptions(forceRefresh: false);
    $cacheDuration = round((microtime(true) - $startCache) * 1000, 1);

    if ($dataCached !== null && count($dataCached['disruptions'] ?? []) === count($disruptions)) {
        echo "<p class='ok'>✅ Cache fonctionne ({$cacheDuration} ms au lieu de {$duration} ms)</p>";
    } else {
        echo "<p class='err'>⚠️ Cache non fonctionnel ou donnees incoherentes</p>";
    }

    echo "<h2>✅ Resume</h2>";
    echo "<p><strong>PrimClient est operationnel.</strong> On peut continuer avec DisruptionFilter.php.</p>";
    echo "<p style='color:#A32D2D;font-weight:bold'>⚠️ SUPPRIME CE FICHIER APRES VALIDATION (securite)</p>";

} catch (Throwable $e) {
    echo "<p class='err'>❌ Erreur : " . htmlspecialchars($e->getMessage()) . "</p>";
    echo "<pre>" . htmlspecialchars($e->getTraceAsString()) . "</pre>";
}

echo "</body></html>";
