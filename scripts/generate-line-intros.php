<?php
/**
 * generate-line-intros.php
 *
 * Script de génération des textes d'intro uniques pour chaque ligne.
 * Appelle l'API Claude pour produire 5 intros par ligne avec des
 * structures de phrases différentes pour éviter le duplicate content.
 *
 * Usage : php scripts/generate-line-intros.php [--line=metro-1] [--dry-run]
 *
 * - Sans options : génère pour toutes les lignes manquantes
 * - --line=X : génère uniquement pour la ligne X
 * - --dry-run : affiche les prompts sans appeler l'API
 *
 * IMPORTANT : Ne régénère PAS les intros déjà présentes dans les JSON,
 *             sauf avec --force.
 *
 * Sécurité : ANTHROPIC_API_KEY doit être en variable d'environnement.
 *            Sur o2switch / GitHub Actions, ne JAMAIS commiter la clé.
 */

declare(strict_types=1);

// =====================================================================
// CONFIGURATION
// =====================================================================

$config = [
    'data_dir'     => __DIR__ . '/../data/lines',
    'api_url'      => 'https://api.anthropic.com/v1/messages',
    'model'        => 'claude-sonnet-4-5-20250929',
    'max_tokens'   => 4000,
    'api_key_env'  => 'ANTHROPIC_API_KEY',
    'styles'       => [
        // Affecte un style à chaque ligne pour éviter l'uniformité
        'metro-1'  => 'direct',          // Direct/efficace
        'metro-2'  => 'conversationnel', // Conversationnel
        'metro-3'  => 'pratique',        // Pratique/utilitaire
        'metro-3bis' => 'informatif',
        'metro-4'  => 'pratique',
        'metro-5'  => 'conversationnel',
        'metro-6'  => 'direct',
        'metro-7'  => 'informatif',
        'metro-7bis' => 'direct',
        'metro-8'  => 'conversationnel',
        'metro-9'  => 'pratique',
        'metro-10' => 'informatif',
        'metro-11' => 'direct',
        'metro-12' => 'conversationnel',
        'metro-13' => 'pratique',
        'metro-14' => 'informatif',  // Spécifique : automatique, moderne
    ],
];

// =====================================================================
// PROMPTS PAR SECTION
// =====================================================================

/**
 * Génère le prompt pour une section donnée d'une ligne.
 */
function buildPrompt(array $line, string $section, string $style): string {
    $code = $line['code'];
    $terminusA = $line['terminus_a'];
    $terminusB = $line['terminus_b'];
    $stationsCount = $line['stations_count'];

    $styleHints = [
        'direct'          => "Style direct et efficace. Phrases affirmatives. Va à l'essentiel.",
        'conversationnel' => "Style conversationnel, accessible. Tu peux t'adresser à l'utilisateur (vouvoiement). Plus chaleureux.",
        'pratique'        => "Style pratique et utilitaire. Met l'accent sur l'action et l'utilité pour l'utilisateur. Verbes d'action.",
        'informatif'      => "Style informatif, légèrement encyclopédique. Données factuelles. Ton neutre.",
    ];

    $styleHint = $styleHints[$style] ?? $styleHints['direct'];

    $sectionPrompts = [
        'introduction' => "Rédige une introduction SEO de 250-300 mots pour la page de la ligne {$code} du métro de Paris. La ligne va de {$terminusA} à {$terminusB} et compte {$stationsCount} stations.\n\nStructure attendue : 3 paragraphes <p>...</p>.\n- §1 : présentation générale et histoire si pertinent\n- §2 : caractéristiques techniques, fréquentation, monuments desservis\n- §3 : correspondances avec autres lignes (métro, RER, tramway, Transilien)\n\nDensité de mots-clés : 5-7 occurrences variées (\"ligne {$code}\", \"métro ligne {$code}\", \"métro de la ligne {$code}\", \"ligne {$code} du métro de Paris\"). Mets en gras (<strong>) UNIQUEMENT les mots-clés SEO importants, jamais les chiffres ni les phrases descriptives.",

        'plan' => "Rédige un texte d'intro de 100-130 mots pour la section \"Plan de la ligne {$code}\" du métro parisien. La ligne va de {$terminusA} à {$terminusB} et compte {$stationsCount} stations.\n\nMentionne : le plan complet, les correspondances, les couleurs officielles IDFM, la possibilité de télécharger le plan.\n\nDensité : 4-5 occurrences variées de \"ligne {$code}\". Cite explicitement les terminus.",

        'stations' => "Rédige un texte d'intro de 80-110 mots pour la section \"Liste des {$stationsCount} stations de la ligne {$code}\" du métro parisien. La ligne va de {$terminusA} à {$terminusB}.\n\nMentionne : la liste complète, l'ordre de circulation, les correspondances par station, l'accessibilité PMR, les stations majeures (pôles).\n\nDensité : 4-5 occurrences variées de \"ligne {$code}\".",

        'horaires' => "Rédige un texte d'intro de 110-140 mots pour la section \"Horaires de la ligne {$code}\" du métro parisien. La ligne va de {$terminusA} à {$terminusB}. Premier métro vers 5h30, dernier vers 1h15 (semaine) / 2h15 (vendredi-samedi). Fréquence 85 secondes en pointe, 2-4 min en creuses.\n\nMentionne : premier/dernier métro, service prolongé vendredi-samedi, fréquence selon période, fiabilité.\n\nDensité : 5-6 occurrences variées de \"ligne {$code}\". NE PAS mettre en gras les chiffres (5h30, 85 secondes), uniquement les mots-clés.",

        'trafic' => "Rédige un texte d'intro de 100-130 mots pour la section \"Trafic en temps réel de la ligne {$code}\" du métro parisien. La ligne va de {$terminusA} à {$terminusB}.\n\nMentionne : actualisation 30 secondes, anticipation des déplacements, détail des perturbations en cas d'incident, lien vers le bulletin trafic du jour. NE PAS mentionner d'API technique (PRIM, IDFM API), mais juste \"Île-de-France Mobilités\" comme source.\n\nDensité : 5-6 occurrences variées de \"ligne {$code}\" (\"trafic de la ligne {$code}\", \"perturbation sur le métro ligne {$code}\", etc.).",

        'itineraires' => "Rédige un texte d'intro de 50-70 mots pour la section \"Itinéraires populaires sur la ligne {$code}\" du métro parisien. La ligne va de {$terminusA} à {$terminusB}.\n\nMentionne : trajets les plus recherchés au départ/arrivée des stations, durée estimée, nombre de correspondances, lignes empruntées. NE PAS mentionner de calculateur d'itinéraires (le widget est juste après).\n\nDensité : 3-4 occurrences variées de \"ligne {$code}\" (\"itinéraire ligne {$code}\", \"stations de la ligne {$code}\", \"itinéraire sur la ligne {$code}\"). Cite les terminus.",
    ];

    $sectionPrompt = $sectionPrompts[$section] ?? '';

    return <<<PROMPT
{$sectionPrompt}

{$styleHint}

CONTRAINTES STRICTES :
- Pas de jargon technique (API, PRIM, scraping, etc.)
- Pas d'emoji
- Mots-clés en <strong> UNIQUEMENT (pas de bourrage)
- Texte unique et naturel à lire
- Réponds UNIQUEMENT avec le texte HTML, sans introduction ni commentaire
- Pas de balise <h2> ou <h3>, juste les paragraphes <p> ou texte simple selon la section
PROMPT;
}

// =====================================================================
// APPEL CLAUDE API
// =====================================================================

function callClaudeAPI(string $prompt, array $config): ?string {
    $apiKey = getenv($config['api_key_env']);
    if (!$apiKey) {
        echo "[ERREUR] Variable d'environnement {$config['api_key_env']} non définie.\n";
        return null;
    }

    $payload = [
        'model'      => $config['model'],
        'max_tokens' => $config['max_tokens'],
        'messages'   => [
            ['role' => 'user', 'content' => $prompt]
        ],
    ];

    $ch = curl_init($config['api_url']);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_POSTFIELDS     => json_encode($payload),
        CURLOPT_HTTPHEADER     => [
            'Content-Type: application/json',
            'x-api-key: ' . $apiKey,
            'anthropic-version: 2023-06-01',
        ],
        CURLOPT_TIMEOUT        => 60,
    ]);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($httpCode !== 200) {
        echo "[ERREUR] HTTP {$httpCode} : {$response}\n";
        return null;
    }

    $data = json_decode($response, true);
    return $data['content'][0]['text'] ?? null;
}

// =====================================================================
// MAIN
// =====================================================================

$options = getopt('', ['line:', 'dry-run', 'force']);
$dryRun = isset($options['dry-run']);
$force = isset($options['force']);
$onlyLine = $options['line'] ?? null;

$sections = ['introduction', 'plan', 'stations', 'horaires', 'trafic', 'itineraires'];

echo "=== Génération des intros uniques ===\n";
echo $dryRun ? "[MODE DRY-RUN]\n" : "[MODE PRODUCTION]\n";
echo "\n";

$lineFiles = glob($config['data_dir'] . '/metro-*.json');

foreach ($lineFiles as $lineFile) {
    $lineId = basename($lineFile, '.json');

    if ($onlyLine && $onlyLine !== $lineId) {
        continue;
    }

    $line = json_decode(file_get_contents($lineFile), true);
    if (!$line) {
        echo "[SKIP] {$lineId} : JSON invalide\n";
        continue;
    }

    $style = $config['styles'][$lineId] ?? 'direct';
    echo "📝 {$lineId} (style: {$style})\n";

    if (!isset($line['intros'])) {
        $line['intros'] = [];
    }

    foreach ($sections as $section) {
        // Skip si déjà présent et pas de --force
        if (!empty($line['intros'][$section]) && !$force) {
            echo "  ✓ {$section} : déjà présent\n";
            continue;
        }

        $prompt = buildPrompt($line, $section, $style);

        if ($dryRun) {
            echo "  [DRY] {$section} : prompt = " . substr($prompt, 0, 80) . "...\n";
            continue;
        }

        echo "  → {$section} : génération...\n";
        $generated = callClaudeAPI($prompt, $config);

        if ($generated) {
            $line['intros'][$section] = trim($generated);
            echo "  ✓ {$section} : " . strlen($generated) . " caractères\n";

            // Sauvegarde immédiate (au cas où le script crashe ensuite)
            file_put_contents(
                $lineFile,
                json_encode($line, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT)
            );

            // Petit délai pour respecter le rate limit
            usleep(500000); // 0.5s
        } else {
            echo "  ✗ {$section} : échec\n";
        }
    }

    echo "\n";
}

echo "=== Terminé ===\n";
