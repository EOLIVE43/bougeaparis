<?php
declare(strict_types=1);
/**
 * scripts/generate-sitemap-images.php
 * Génère public_html/sitemap-images.xml (schémas Google sitemap-image).
 */
const ROOT_DIR  = __DIR__ . '/..';
const OUT_FILE  = ROOT_DIR . '/public_html/sitemap-images.xml';
const BASE_URL  = 'https://bougeaparis.fr';

$lineImages = [
    [
        'page_url'  => BASE_URL . '/aeroports/paris-orly/tramway/',
        'image_url' => BASE_URL . '/assets/images/lines/t7-trace-villejuif-louis-aragon-aeroport-dorly.png',
        'caption'   => "Plan officiel ligne T7 du tramway entre Villejuif-Louis Aragon et l'aéroport Paris-Orly (15 stations).",
        'title'     => 'Plan T7 Tramway Villejuif - Aéroport Paris-Orly',
    ],
];

$xml  = '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
$xml .= '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"' . "\n";
$xml .= '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">' . "\n";
foreach ($lineImages as $img) {
    $xml .= "  <url>\n";
    $xml .= "    <loc>" . htmlspecialchars($img['page_url'], ENT_XML1) . "</loc>\n";
    $xml .= "    <image:image>\n";
    $xml .= "      <image:loc>" . htmlspecialchars($img['image_url'], ENT_XML1) . "</image:loc>\n";
    $xml .= "      <image:caption>" . htmlspecialchars($img['caption'], ENT_XML1) . "</image:caption>\n";
    $xml .= "      <image:title>" . htmlspecialchars($img['title'], ENT_XML1) . "</image:title>\n";
    $xml .= "    </image:image>\n";
    $xml .= "  </url>\n";
}
$xml .= "</urlset>\n";
file_put_contents(OUT_FILE, $xml);
echo "✓ Sitemap-images : " . count($lineImages) . " image(s) → " . OUT_FILE . "\n";
