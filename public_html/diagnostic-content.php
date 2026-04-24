<?php
/**
 * Diagnostic temporaire : trouve où se trouve le dossier content/
 * À SUPPRIMER après diagnostic.
 */

echo "<h1>Diagnostic dossier content/</h1>";
echo "<p><strong>__DIR__ actuel :</strong> " . __DIR__ . "</p>";

$candidats = [
    __DIR__ . '/../content/info-trafic/',
    __DIR__ . '/content/info-trafic/',
    __DIR__ . '/../../content/info-trafic/',
    '/home/loxo5141/content/info-trafic/',
    '/home/loxo5141/public_html/content/info-trafic/',
];

echo "<h2>Test des chemins possibles :</h2><ul>";
foreach ($candidats as $path) {
    $exists = is_dir($path) ? '✅ EXISTE' : '❌ N\'EXISTE PAS';
    echo "<li><code>$path</code> : $exists";
    if (is_dir($path)) {
        $files = glob($path . '*.md');
        echo "<br>Fichiers .md trouvés : " . count($files);
        if (!empty($files)) {
            echo "<ul>";
            foreach ($files as $f) echo "<li>" . basename($f) . "</li>";
            echo "</ul>";
        }
    }
    echo "</li>";
}
echo "</ul>";
