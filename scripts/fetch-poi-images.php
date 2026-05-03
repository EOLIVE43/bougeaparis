<?php
/**
 * fetch-poi-images.php
 *
 * Script d'industrialisation des photos POI via Wikimedia Commons.
 *
 * Pour chaque POI dans data/lines/*.json :
 * 1. Recherche sur l'API Wikimedia Commons
 * 2. Sélectionne la meilleure photo (taille, qualité)
 * 3. Télécharge l'image originale
 * 4. Crop au format 16:9 (recommandation Discover)
 * 5. Redimensionne en 1200×675px (full) + 600×338px (thumb)
 * 6. Compose le watermark BougeàParis.fr (bandeau bas + nom du lieu en overlay)
 * 7. Optimise en WebP qualité 85
 * 8. Sauvegarde dans /assets/images/poi/{categorie}/{slug}.webp
 * 9. Met à jour le JSON avec chemins + attribution
 *
 * Usage :
 *   php scripts/fetch-poi-images.php [--line=metro-1] [--poi=arc-de-triomphe] [--dry-run] [--force]
 *
 * Prérequis :
 * - PHP 7.4+ avec extensions : curl, gd, json, mbstring
 * - ImageMagick optionnel mais recommandé (meilleure qualité de crop)
 *
 * Légalement :
 * - Photos Wikimedia sous licence CC BY-SA (libres)
 * - Attribution OBLIGATOIRE (auteur + licence)
 * - L'attribution est stockée dans le JSON et affichée discrètement sous la photo
 */

declare(strict_types=1);

// =====================================================================
// CONFIGURATION
// =====================================================================

$config = [
    'data_dir'         => __DIR__ . '/../public_html/data/lines',
    'images_dir'       => __DIR__ . '/../public_html/assets/images/poi',
    'wikimedia_api'    => 'https://commons.wikimedia.org/w/api.php',

    // Discover-friendly : 1200×675 = ratio 16:9
    'image_full'       => ['width' => 1200, 'height' => 675],
    'image_thumb'      => ['width' => 600, 'height' => 338],
    'webp_quality'     => 85,

    // Watermark
    'brand_color'      => '#0F6E56',     // teal BougeàParis
    'brand_color_rgba' => [15, 110, 86, 242],  // 95% opacity
    'brand_text'       => 'bougeàparis.fr',
    'brand_tagline'    => 'Se déplacer. Visiter.',
    'brand_logo'       => 'B',

    // User-Agent pour Wikimedia (poli)
    'user_agent'       => 'BougeaParis/1.0 (https://bougeaparis.fr; ludo@bougeaparis.fr)',
];

// =====================================================================
// PARSING DES OPTIONS
// =====================================================================

$options = getopt('', ['line:', 'poi:', 'dry-run', 'force', 'help']);

if (isset($options['help'])) {
    echo <<<HELP
Usage : php scripts/fetch-poi-images.php [OPTIONS]

OPTIONS :
  --line=metro-X      Traiter une seule ligne (ex: --line=metro-1)
  --poi=slug          Traiter un seul POI (ex: --poi=arc-de-triomphe)
  --dry-run           Simulation sans télécharger ni écrire
  --force             Régénérer même si la photo existe déjà
  --help              Affiche cette aide

EXEMPLES :
  php scripts/fetch-poi-images.php --dry-run
  php scripts/fetch-poi-images.php --line=metro-1
  php scripts/fetch-poi-images.php --line=metro-1 --poi=louvre --force

HELP;
    exit(0);
}

$dryRun = isset($options['dry-run']);
$force = isset($options['force']);
$onlyLine = $options['line'] ?? null;
$onlyPoi = $options['poi'] ?? null;

// =====================================================================
// FONCTIONS UTILITAIRES
// =====================================================================

/**
 * Effectue une requête HTTP avec User-Agent personnalisé
 */
function httpGet(string $url, array $config): ?string {
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_TIMEOUT        => 30,
        CURLOPT_USERAGENT      => $config['user_agent'],
    ]);
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($httpCode !== 200) {
        echo "  [HTTP {$httpCode}] {$url}\n";
        return null;
    }
    return $response;
}

/**
 * Recherche d'images sur Wikimedia Commons
 *
 * Retourne un tableau de candidats avec leurs métadonnées.
 */
function searchWikimediaImages(string $query, array $config): array {
    // 1. Rechercher les fichiers correspondants
    $searchUrl = $config['wikimedia_api'] . '?' . http_build_query([
        'action'    => 'query',
        'list'      => 'search',
        'srsearch'  => $query . ' filetype:bitmap',
        'srnamespace' => 6, // namespace File:
        'srlimit'   => 10,
        'format'    => 'json',
    ]);

    $response = httpGet($searchUrl, $config);
    if (!$response) return [];

    $data = json_decode($response, true);
    $files = $data['query']['search'] ?? [];

    if (empty($files)) return [];

    // 2. Récupérer les métadonnées (taille, URL, auteur, licence) de chaque fichier
    $titles = array_map(fn($f) => $f['title'], $files);

    $infoUrl = $config['wikimedia_api'] . '?' . http_build_query([
        'action'      => 'query',
        'titles'      => implode('|', $titles),
        'prop'        => 'imageinfo',
        'iiprop'      => 'url|size|extmetadata',
        'iiurlwidth'  => 1600,  // demande version 1600px
        'format'      => 'json',
    ]);

    $response = httpGet($infoUrl, $config);
    if (!$response) return [];

    $data = json_decode($response, true);
    $pages = $data['query']['pages'] ?? [];

    $candidates = [];
    foreach ($pages as $page) {
        $info = $page['imageinfo'][0] ?? null;
        if (!$info) continue;

        // Filtre : ne garder que les images de bonne taille
        if (($info['width'] ?? 0) < 1200) continue;

        $meta = $info['extmetadata'] ?? [];
        $candidates[] = [
            'title'       => $page['title'],
            'url'         => $info['url'],
            'thumb_url'   => $info['thumburl'] ?? $info['url'],
            'width'       => $info['width'],
            'height'      => $info['height'],
            'mime'        => $info['mime'] ?? 'image/jpeg',
            'author'      => strip_tags($meta['Artist']['value'] ?? 'Anonyme'),
            'license'     => $meta['LicenseShortName']['value'] ?? 'CC BY-SA',
            'license_url' => $meta['LicenseUrl']['value'] ?? '',
            'description' => strip_tags($meta['ImageDescription']['value'] ?? ''),
        ];
    }

    // Trier par taille décroissante (les plus grandes en premier)
    usort($candidates, fn($a, $b) => ($b['width'] * $b['height']) - ($a['width'] * $a['height']));

    return $candidates;
}

/**
 * Télécharge une image depuis une URL
 */
function downloadImage(string $url, array $config): ?string {
    $tmpFile = tempnam(sys_get_temp_dir(), 'wmedia_');
    $ch = curl_init($url);
    $fp = fopen($tmpFile, 'wb');
    curl_setopt_array($ch, [
        CURLOPT_FILE      => $fp,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_TIMEOUT   => 60,
        CURLOPT_USERAGENT => $config['user_agent'],
    ]);
    $success = curl_exec($ch);
    curl_close($ch);
    fclose($fp);

    if (!$success || filesize($tmpFile) < 1000) {
        @unlink($tmpFile);
        return null;
    }
    return $tmpFile;
}

/**
 * Crop une image au ratio 16:9 (centré)
 */
function cropTo16x9(string $imagePath, string $outputPath, int $targetW, int $targetH): bool {
    $info = getimagesize($imagePath);
    if (!$info) return false;

    [$origW, $origH, $type] = $info;

    // Charger l'image source
    $srcImg = match($type) {
        IMAGETYPE_JPEG => imagecreatefromjpeg($imagePath),
        IMAGETYPE_PNG  => imagecreatefrompng($imagePath),
        IMAGETYPE_WEBP => imagecreatefromwebp($imagePath),
        default        => null,
    };

    if (!$srcImg) return false;

    // Calculer le crop centré au ratio 16:9
    $targetRatio = $targetW / $targetH; // ~1.778
    $origRatio = $origW / $origH;

    if ($origRatio > $targetRatio) {
        // Image trop large : crop horizontal
        $cropH = $origH;
        $cropW = (int)($origH * $targetRatio);
        $cropX = (int)(($origW - $cropW) / 2);
        $cropY = 0;
    } else {
        // Image trop haute : crop vertical (mais on garde le tiers supérieur de préférence)
        $cropW = $origW;
        $cropH = (int)($origW / $targetRatio);
        $cropX = 0;
        $cropY = (int)(($origH - $cropH) / 3); // tiers supérieur
    }

    // Créer l'image de destination
    $dstImg = imagecreatetruecolor($targetW, $targetH);
    imagecopyresampled($dstImg, $srcImg, 0, 0, $cropX, $cropY, $targetW, $targetH, $cropW, $cropH);

    // Sauvegarder en WebP
    $success = imagewebp($dstImg, $outputPath, 90); // 90 avant watermark

    imagedestroy($srcImg);
    imagedestroy($dstImg);

    return $success;
}

/**
 * Applique le watermark sur l'image :
 * - Pill teal "B bougeaparis.fr" en coin haut-gauche (Option A validée)
 * - Bandeau nom du POI en overlay bas (gradient + nom + catégorie)
 *
 * Style discret et lisible, n'empiète pas sur le sujet de la photo.
 * Utilise GD avec font TTF si disponible (Inter Bold), sinon fallback sur imagestring().
 */
function applyWatermark(string $imagePath, array $poi, array $theme, array $config, int $finalQuality = 85): bool {
    $img = imagecreatefromwebp($imagePath);
    if (!$img) return false;

    $w = imagesx($img);
    $h = imagesy($img);

    // Activer alpha blending
    imagealphablending($img, true);
    imagesavealpha($img, true);

    // Détecter font TTF disponible
    $fontPaths = [
        __DIR__ . '/../assets/fonts/Inter-Bold.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        '/usr/share/fonts/truetype/inter/Inter-Bold.ttf',
        '/Library/Fonts/Helvetica.ttc',
    ];
    $fontPath = null;
    foreach ($fontPaths as $candidate) {
        if (file_exists($candidate)) {
            $fontPath = $candidate;
            break;
        }
    }
    $hasTTF = $fontPath !== null;

    // ============================================
    // 1. BANDEAU NOM DU POI (overlay bas, gradient noir)
    // Pas besoin d'être très grand puisque le watermark est désormais en haut.
    // ============================================
    $overlayHeight = (int)($h * 0.20); // 20% de la hauteur
    $overlayY = $h - $overlayHeight;

    // Créer un gradient noir transparent (du haut vers bas du gradient)
    for ($i = 0; $i < $overlayHeight; $i++) {
        // alpha de 110 (transparent) à 40 (plus opaque vers le bas)
        $alpha = (int)(110 - ($i / $overlayHeight) * 70);
        $alpha = max(0, min(127, $alpha));
        $blackColor = imagecolorallocatealpha($img, 0, 0, 0, $alpha);
        imageline($img, 0, $overlayY + $i, $w, $overlayY + $i, $blackColor);
    }

    // Texte : "MONUMENT" en small caps + nom du POI
    $whiteColor = imagecolorallocate($img, 255, 255, 255);
    $themeLabel = strtoupper($theme['title'] ?? 'À VISITER');

    if ($hasTTF) {
        // Avec vraie font Inter Bold
        $themeLabelSize = (int)($h * 0.022);
        $poiNameSize = (int)($h * 0.045);

        // Small label (catégorie)
        imagettftext($img, $themeLabelSize, 0, 30, $overlayY + (int)($overlayHeight * 0.45),
                     $whiteColor, $fontPath, $themeLabel);

        // Nom du POI
        imagettftext($img, $poiNameSize, 0, 30, $overlayY + (int)($overlayHeight * 0.85),
                     $whiteColor, $fontPath, $poi['name']);
    } else {
        // Fallback sans font TTF
        imagestring($img, 3, 30, $overlayY + (int)($overlayHeight * 0.3), $themeLabel, $whiteColor);
        imagestring($img, 5, 30, $overlayY + (int)($overlayHeight * 0.55), $poi['name'], $whiteColor);
    }

    // ============================================
    // 2. WATERMARK COIN HAUT-GAUCHE : Pill teal arrondie
    // ============================================
    // Format : [B] bougeaparis.fr
    // Position : coin haut-gauche, padding 16px
    // Style : pill arrondie (border-radius 50%)
    //   - Fond teal #0F6E56 95% opaque
    //   - Logo "B" rond blanc avec B teal au centre
    //   - Texte "bougeaparis.fr" blanc
    //   - Ombre douce sous la pill pour la détacher du fond
    //
    // Discret mais lisible, n'empiète pas sur le sujet de la photo.

    $pillMarginTop = 16;
    $pillMarginLeft = 16;
    $pillBrandText = 'bougeaparis.fr';

    if ($hasTTF) {
        // Tailles proportionnelles à la hauteur de l'image
        $pillTextSize = (int)($h * 0.022);  // ~14px sur 675px
        $pillLogoSize = (int)($h * 0.038);  // ~26px sur 675px - cercle blanc
        $pillLogoTextSize = (int)($pillLogoSize * 0.55); // taille du "B" dans le cercle

        // Padding interne de la pill
        $pillPadding = (int)($h * 0.011); // ~7px
        $pillGap = 10; // espace entre logo et texte

        // Mesurer le texte "bougeaparis.fr"
        $textBox = imagettfbbox($pillTextSize, 0, $fontPath, $pillBrandText);
        $textWidth = $textBox[2] - $textBox[0];
        $textHeight = $textBox[1] - $textBox[7];

        // Dimensions totales de la pill
        $pillWidth = $pillPadding + $pillLogoSize + $pillGap + $textWidth + (int)($pillPadding * 1.6);
        $pillHeight = $pillLogoSize + ($pillPadding * 2);

        // Position de la pill
        $pillX = $pillMarginLeft;
        $pillY = $pillMarginTop;

        // === OMBRE PORTÉE (sous la pill, pour la détacher) ===
        $shadowColor = imagecolorallocatealpha($img, 0, 0, 0, 100); // semi-transparent
        for ($i = 1; $i <= 3; $i++) {
            imagefilledroundedrect(
                $img,
                $pillX + $i,
                $pillY + $i,
                $pillX + $pillWidth + $i,
                $pillY + $pillHeight + $i,
                (int)($pillHeight / 2),
                $shadowColor
            );
        }

        // === FOND TEAL DE LA PILL ===
        $tealBgColor = imagecolorallocatealpha($img, 15, 110, 86, 6); // ~95% opaque (alpha 6 = ~95%)
        imagefilledroundedrect(
            $img,
            $pillX,
            $pillY,
            $pillX + $pillWidth,
            $pillY + $pillHeight,
            (int)($pillHeight / 2),
            $tealBgColor
        );

        // === LOGO "B" : cercle blanc avec B teal au centre ===
        $logoCenterX = $pillX + $pillPadding + (int)($pillLogoSize / 2);
        $logoCenterY = $pillY + (int)($pillHeight / 2);

        // Cercle blanc
        $whiteCircleColor = imagecolorallocate($img, 255, 255, 255);
        imagefilledellipse($img, $logoCenterX, $logoCenterY, $pillLogoSize, $pillLogoSize, $whiteCircleColor);

        // Lettre "B" teal au centre du cercle
        $bBox = imagettfbbox($pillLogoTextSize, 0, $fontPath, 'B');
        $bWidth = $bBox[2] - $bBox[0];
        $bHeight = $bBox[1] - $bBox[7];
        $tealTextColor = imagecolorallocate($img, 15, 110, 86);
        imagettftext(
            $img,
            $pillLogoTextSize,
            0,
            $logoCenterX - (int)($bWidth / 2),
            $logoCenterY + (int)($bHeight / 2) - 1,
            $tealTextColor,
            $fontPath,
            'B'
        );

        // === TEXTE "bougeaparis.fr" en blanc ===
        $brandTextX = $pillX + $pillPadding + $pillLogoSize + $pillGap;
        $brandTextY = $pillY + (int)($pillHeight / 2) + (int)($textHeight / 2) - 1;
        imagettftext(
            $img,
            $pillTextSize,
            0,
            $brandTextX,
            $brandTextY,
            $whiteColor,
            $fontPath,
            $pillBrandText
        );

    } else {
        // Fallback sans font TTF (utilise imagestring + cercle simulé)
        // Moins joli mais marche partout
        $pillX = $pillMarginLeft;
        $pillY = $pillMarginTop;
        $pillW = 180;
        $pillH = 32;

        // Ombre
        $shadowColor = imagecolorallocatealpha($img, 0, 0, 0, 100);
        imagefilledrectangle($img, $pillX + 2, $pillY + 2, $pillX + $pillW + 2, $pillY + $pillH + 2, $shadowColor);

        // Pill teal
        $tealBgColor = imagecolorallocatealpha($img, 15, 110, 86, 6);
        imagefilledrectangle($img, $pillX, $pillY, $pillX + $pillW, $pillY + $pillH, $tealBgColor);

        // Cercle blanc avec B
        $whiteCircleColor = imagecolorallocate($img, 255, 255, 255);
        imagefilledellipse($img, $pillX + 18, $pillY + 16, 22, 22, $whiteCircleColor);

        $tealTextColor = imagecolorallocate($img, 15, 110, 86);
        imagestring($img, 4, $pillX + 13, $pillY + 8, 'B', $tealTextColor);

        // Texte
        imagestring($img, 3, $pillX + 38, $pillY + 10, $pillBrandText, $whiteColor);
    }

    // ============================================
    // 3. SAUVEGARDE FINALE
    // ============================================
    $success = imagewebp($img, $imagePath, $finalQuality);
    imagedestroy($img);

    return $success;
}

/**
 * Helper : dessine un rectangle aux coins arrondis (compat GD pas natif)
 */
function imagefilledroundedrect($img, $x1, $y1, $x2, $y2, $radius, $color) {
    imagefilledrectangle($img, $x1 + $radius, $y1, $x2 - $radius, $y2, $color);
    imagefilledrectangle($img, $x1, $y1 + $radius, $x2, $y2 - $radius, $color);
    imagefilledellipse($img, $x1 + $radius, $y1 + $radius, $radius * 2, $radius * 2, $color);
    imagefilledellipse($img, $x2 - $radius, $y1 + $radius, $radius * 2, $radius * 2, $color);
    imagefilledellipse($img, $x1 + $radius, $y2 - $radius, $radius * 2, $radius * 2, $color);
    imagefilledellipse($img, $x2 - $radius, $y2 - $radius, $radius * 2, $radius * 2, $color);
}

/**
 * Crée un slug propre depuis un nom
 */
function slugify(string $text): string {
    $slug = mb_strtolower($text);
    $slug = strtr($slug, [
        'à'=>'a','á'=>'a','â'=>'a','ä'=>'a','ã'=>'a',
        'é'=>'e','è'=>'e','ê'=>'e','ë'=>'e',
        'í'=>'i','ì'=>'i','î'=>'i','ï'=>'i',
        'ó'=>'o','ò'=>'o','ô'=>'o','ö'=>'o','õ'=>'o',
        'ú'=>'u','ù'=>'u','û'=>'u','ü'=>'u',
        'ç'=>'c','ñ'=>'n', "'"=>'-', ' '=>'-'
    ]);
    $slug = preg_replace('/[^a-z0-9\-]/', '', $slug);
    return preg_replace('/-+/', '-', trim($slug, '-'));
}

// =====================================================================
// MAIN
// =====================================================================

echo "╔════════════════════════════════════════════════╗\n";
echo "║  Industrialisation photos POI Wikimedia       ║\n";
echo "╚════════════════════════════════════════════════╝\n\n";

if ($dryRun) {
    echo "🔍 MODE DRY-RUN (aucune modification)\n\n";
}

$lineFiles = glob($config['data_dir'] . '/metro-*.json');

foreach ($lineFiles as $lineFile) {
    $lineId = basename($lineFile, '.json');

    if ($onlyLine && $onlyLine !== $lineId) continue;

    $line = json_decode(file_get_contents($lineFile), true);
    if (!$line || empty($line['points_of_interest'])) {
        echo "⏭️  {$lineId} : pas de POI\n";
        continue;
    }

    echo "📍 LIGNE {$line['code']} ({$lineId})\n";
    echo str_repeat('─', 50) . "\n";

    foreach ($line['points_of_interest'] as $themeKey => &$theme) {
        echo "\n  🎨 Thème : {$theme['icon']} {$themeKey}\n";

        foreach ($theme['items'] as &$poi) {
            if ($onlyPoi && $onlyPoi !== $poi['slug']) continue;

            $imageDir = $config['images_dir'] . '/' . $themeKey;
            $imageFile = $imageDir . '/' . $poi['slug'] . '.webp';
            $thumbFile = $imageDir . '/' . $poi['slug'] . '-thumb.webp';

            // Skip si déjà présent et pas de --force
            if (!$force && file_exists($imageFile) && !empty($poi['image']['src'])) {
                echo "    ✓ {$poi['name']} : déjà téléchargée\n";
                continue;
            }

            echo "    → {$poi['name']}\n";

            if ($dryRun) {
                echo "      [DRY] Recherche Wikimedia : '{$poi['name']} Paris'\n";
                continue;
            }

            // 1. Recherche sur Wikimedia
            $candidates = searchWikimediaImages($poi['name'] . ' Paris', $config);
            if (empty($candidates)) {
                echo "      ✗ Aucune image trouvée\n";
                continue;
            }
            echo "      📥 " . count($candidates) . " candidats trouvés\n";

            // 2. Sélectionner le meilleur (déjà trié par taille)
            $best = $candidates[0];
            echo "      📷 Sélection : {$best['title']} ({$best['width']}x{$best['height']})\n";
            echo "      👤 Auteur : {$best['author']}\n";

            // 3. Télécharger
            $tmpFile = downloadImage($best['url'], $config);
            if (!$tmpFile) {
                echo "      ✗ Échec téléchargement\n";
                continue;
            }

            // 4. Crop + redimensionnement
            if (!is_dir($imageDir)) mkdir($imageDir, 0755, true);

            cropTo16x9($tmpFile, $imageFile, $config['image_full']['width'], $config['image_full']['height']);
            cropTo16x9($tmpFile, $thumbFile, $config['image_thumb']['width'], $config['image_thumb']['height']);

            // 5. Watermark sur l'image full uniquement
            applyWatermark($imageFile, $poi, $theme, $config);

            // 6. Mettre à jour le JSON
            $poi['image'] = [
                'src'        => '/assets/images/poi/' . $themeKey . '/' . $poi['slug'] . '.webp',
                'thumb'      => '/assets/images/poi/' . $themeKey . '/' . $poi['slug'] . '-thumb.webp',
                'alt'        => $poi['name'] . ' à Paris, station ' . $poi['station'],
                'width'      => $config['image_full']['width'],
                'height'     => $config['image_full']['height'],
                'credit'     => [
                    'author'      => $best['author'],
                    'source'      => 'Wikimedia Commons',
                    'license'     => $best['license'],
                    'license_url' => $best['license_url'],
                    'wikimedia_url' => 'https://commons.wikimedia.org/wiki/' . urlencode($best['title']),
                ],
            ];

            @unlink($tmpFile);

            // Sauvegarde JSON après chaque POI (résistant aux crashes)
            file_put_contents($lineFile, json_encode($line, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));

            echo "      ✅ Sauvegardée : {$imageFile}\n";

            // Politesse envers Wikimedia
            usleep(800000); // 0.8s entre chaque requête
        }
    }
    unset($theme); // unset reference
    echo "\n";
}

echo "\n╔════════════════════════════════════════════════╗\n";
echo "║  Terminé                                       ║\n";
echo "╚════════════════════════════════════════════════╝\n";
