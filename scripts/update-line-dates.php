<?php
/**
 * update-line-dates.php
 *
 * Détecte les changements rédactionnels dans les fichiers data/lines/*.json
 * et met à jour automatiquement meta.dates.updated à la date du jour.
 *
 * Lancé par la GitHub Action auto-update-dates.yml à chaque push.
 *
 * Usage :
 *   php scripts/update-line-dates.php           # Tous les fichiers de lignes
 *   php scripts/update-line-dates.php --dry-run # Simulation sans écriture
 *
 * Champs surveillés (modification → MAJ date) :
 * - intros.* (toutes les intros de sections)
 * - history (timeline, anecdotes, chiffres clés)
 * - accessibility (équipements, conseils)
 * - fares.main_fares, fares.additional_fares (changement de prix)
 * - works.current_works, works.upcoming_works (nouveaux travaux)
 * - faq (Q/R)
 * - points_of_interest (POI)
 * - popular_routes, tourist_routes (itinéraires)
 * - tourism (POI)
 * - meta.primary_author.bio, meta.co_author.bio (bio auteurs)
 * - meta.sources (sources externes)
 *
 * Champs ignorés (modification → pas de MAJ) :
 * - meta.dates (sinon boucle infinie)
 * - color, color_text, color_light (techniques)
 * - seo (techniques)
 * - last_check, valid_since (techniques)
 */

declare(strict_types=1);

// =====================================================================
// CONFIGURATION
// =====================================================================

$config = [
    'data_dir' => __DIR__ . '/../public_html/data/lines',
    // Champs surveillés (modification déclenche MAJ date)
    'watched_paths' => [
        'intros',
        'history',
        'accessibility',
        'fares.main_fares',
        'fares.additional_fares',
        'works.current_works',
        'works.upcoming_works',
        'faq',
        'points_of_interest',
        'popular_routes',
        'tourist_routes',
        'tourism',
        'meta.primary_author.bio',
        'meta.primary_author.expertise_tags',
        'meta.co_author.bio',
        'meta.co_author.contributed_sections',
        'meta.sources',
    ],
];

// =====================================================================
// PARSE OPTIONS
// =====================================================================

$options = getopt('', ['dry-run', 'help']);

if (isset($options['help'])) {
    echo <<<HELP
Usage : php scripts/update-line-dates.php [OPTIONS]

OPTIONS :
  --dry-run    Simulation sans écrire les fichiers
  --help       Affiche cette aide

Le script :
1. Compare l'état actuel des fichiers data/lines/*.json avec la version git HEAD
2. Si un changement rédactionnel détecté, met à jour meta.dates.updated
3. Si aucun changement rédactionnel, ne fait rien

HELP;
    exit(0);
}

$dryRun = isset($options['dry-run']);

// =====================================================================
// FONCTIONS UTILITAIRES
// =====================================================================

/**
 * Récupère la version précédente d'un fichier depuis git HEAD~1
 * (avant le dernier commit)
 */
function getPreviousVersion(string $filepath): ?array {
    $relativePath = str_replace(getcwd() . '/', '', realpath($filepath));
    $cmd = sprintf('git show HEAD~1:%s 2>/dev/null', escapeshellarg($relativePath));
    $output = shell_exec($cmd);

    if (!$output) {
        return null; // Fichier nouveau ou pas dans git
    }

    $data = json_decode($output, true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        return null;
    }

    return $data;
}

/**
 * Récupère une valeur dans un array imbriqué via un chemin dot-notation
 * Ex : getNestedValue($data, 'meta.primary_author.bio')
 */
function getNestedValue(array $data, string $path) {
    $keys = explode('.', $path);
    $current = $data;
    foreach ($keys as $key) {
        if (!is_array($current) || !array_key_exists($key, $current)) {
            return null;
        }
        $current = $current[$key];
    }
    return $current;
}

/**
 * Détermine si deux valeurs sont différentes (comparaison profonde pour arrays)
 */
function valuesChanged($v1, $v2): bool {
    return json_encode($v1, JSON_UNESCAPED_UNICODE) !== json_encode($v2, JSON_UNESCAPED_UNICODE);
}

/**
 * Vérifie si un changement rédactionnel a été détecté
 * dans un fichier de ligne donné.
 *
 * Retourne un array des champs modifiés.
 */
function detectChanges(array $current, ?array $previous, array $watchedPaths): array {
    if ($previous === null) {
        // Fichier nouveau : considérer comme nouvelle publication, pas une mise à jour
        return [];
    }

    $changes = [];
    foreach ($watchedPaths as $path) {
        $currentValue = getNestedValue($current, $path);
        $previousValue = getNestedValue($previous, $path);

        if (valuesChanged($currentValue, $previousValue)) {
            $changes[] = $path;
        }
    }

    return $changes;
}

// =====================================================================
// MAIN
// =====================================================================

echo "╔════════════════════════════════════════════════╗\n";
echo "║  Auto-update meta.dates.updated               ║\n";
echo "╚════════════════════════════════════════════════╝\n\n";

if ($dryRun) {
    echo "🔍 MODE DRY-RUN (aucune modification)\n\n";
}

// Lister tous les fichiers de lignes
$lineFiles = glob($config['data_dir'] . '/*.json');

if (empty($lineFiles)) {
    echo "Aucun fichier trouvé dans " . $config['data_dir'] . "\n";
    exit(0);
}

$today = date('Y-m-d');
$todayLabel = strftime('%-d %B %Y', strtotime($today));
// Fallback si strftime ne marche pas (PHP 8.1+)
if (strpos($todayLabel, '%') !== false) {
    $months = ['', 'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
               'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'];
    $todayLabel = (int)date('j') . ' ' . $months[(int)date('n')] . ' ' . date('Y');
    if ((int)date('j') === 1) {
        $todayLabel = '1er ' . $months[(int)date('n')] . ' ' . date('Y');
    }
}

$totalUpdated = 0;
$totalUnchanged = 0;

foreach ($lineFiles as $filepath) {
    $lineId = basename($filepath, '.json');
    echo "📄 {$lineId}.json\n";

    // Charger version actuelle
    $current = json_decode(file_get_contents($filepath), true);
    if (!$current) {
        echo "   ✗ JSON invalide, ignoré\n\n";
        continue;
    }

    // Charger version précédente depuis git
    $previous = getPreviousVersion($filepath);

    if ($previous === null) {
        echo "   ℹ️  Nouveau fichier (pas de version précédente)\n";
        echo "   → Pas de mise à jour auto (utilisez 'published' à la création)\n\n";
        continue;
    }

    // Détecter les changements rédactionnels
    $changes = detectChanges($current, $previous, $config['watched_paths']);

    if (empty($changes)) {
        echo "   ✓ Aucun changement rédactionnel détecté\n";
        $totalUnchanged++;
    } else {
        echo "   📝 Changements détectés :\n";
        foreach ($changes as $path) {
            echo "      - {$path}\n";
        }

        // Mise à jour de la date
        $oldDate = $current['meta']['dates']['updated'] ?? '?';
        if ($oldDate === $today) {
            echo "   ℹ️  Déjà à jour aujourd'hui ({$today})\n";
        } else {
            $current['meta']['dates']['updated'] = $today;
            $current['meta']['dates']['updated_label'] = $todayLabel;

            if (!$dryRun) {
                file_put_contents(
                    $filepath,
                    json_encode($current, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT)
                );
                echo "   ✅ Date mise à jour : {$oldDate} → {$today}\n";
                $totalUpdated++;
            } else {
                echo "   [DRY-RUN] Date à mettre à jour : {$oldDate} → {$today}\n";
            }
        }
    }
    echo "\n";
}

echo "╔════════════════════════════════════════════════╗\n";
echo "║  Résumé                                         ║\n";
echo "╠════════════════════════════════════════════════╣\n";
echo "║  Fichiers mis à jour : {$totalUpdated}\n";
echo "║  Fichiers inchangés  : {$totalUnchanged}\n";
echo "╚════════════════════════════════════════════════╝\n";

exit($totalUpdated > 0 ? 0 : 0); // 0 = succès dans tous les cas
