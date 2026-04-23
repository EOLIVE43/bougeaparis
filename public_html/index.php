<?php
/**
 * Front Controller - BougeaParis.fr
 *
 * Livraison 2 : routing vers les nouveaux templates hub enrichis.
 * Les 6 cocons (metro, rer, bus, tramway, aeroports, transilien) utilisent
 * les templates dedies avec contenu editorial et composants.
 *
 * Pour chaque cocon :
 * - Charge config/cocons/<slug>.php (contenu editorial)
 * - Charge data/lines.json (donnees des lignes)
 * - Rend le template pages/hub-<slug>.php
 *
 * Les autres pages (home, a-propos, contact, legal, 404...) continuent
 * d'utiliser les templates de la Livraison 1.
 */

declare(strict_types=1);

// -------------------- Bootstrap --------------------
require_once __DIR__ . '/core/bootstrap.php';

// -------------------- Parse URL --------------------
$uri  = $_SERVER['REQUEST_URI'] ?? '/';
$path = parse_url($uri, PHP_URL_PATH) ?? '/';
$path = rtrim($path, '/');
if ($path === '') $path = '/';

// -------------------- Helpers chargement cocon --------------------

/**
 * Charge le contenu editorial d'un cocon + les donnees lignes.
 * Retourne false si un fichier manque.
 */
function bp_load_cocon(string $slug): array|false {
    $cocon_path = __DIR__ . '/config/cocons/' . $slug . '.php';
    $lines_path = __DIR__ . '/data/lines.json';

    if (!file_exists($cocon_path) || !file_exists($lines_path)) {
        return false;
    }

    $cocon = require $cocon_path;
    $lines = json_decode(file_get_contents($lines_path), true) ?: [];

    return ['cocon' => $cocon, 'lines' => $lines];
}

/**
 * Rend une page hub transport.
 */
function bp_render_hub(string $slug, string $template = null): void {
    $data = bp_load_cocon($slug);
    if (!$data) {
        bp_render_404();
        return;
    }

    $tpl = new Template($template ?? ('hub-' . $slug));
    $tpl->withData([
        'cocon' => $data['cocon'],
        'lines' => $data['lines'],
    ]);
    $tpl->render();
}

/**
 * Rend la page 404.
 */
function bp_render_404(): void {
    http_response_code(404);
    $tpl = new Template('404');
    $tpl->render();
}

// -------------------- Routing --------------------

switch ($path) {

    // --- Home ---
    case '/':
        $tpl = new Template('home');
        $tpl->render();
        break;

    // --- Pages hub transport (enrichies Livraison 2) ---
    case '/metro':
        bp_render_hub('metro');
        break;
    case '/rer':
        bp_render_hub('rer');
        break;
    case '/bus':
        bp_render_hub('bus');
        break;
    case '/tramway':
        bp_render_hub('tramway');
        break;
    case '/aeroports':
        bp_render_hub('aeroports');
        break;
    case '/transilien':
        bp_render_hub('transilien');
        break;

    // --- Pages Livraison 1 ---
    case '/blog':
        (new Template('blog-index'))->render();
        break;
    case '/a-propos':
        (new Template('about'))->render();
        break;
    case '/contact':
        (new Template('contact'))->render();
        break;
    case '/mentions-legales':
        (new Template('legal'))->render();
        break;
    case '/confidentialite':
        (new Template('privacy'))->render();
        break;
    case '/auteur/ludo':
        (new Template('author-ludo'))->render();
        break;
    case '/auteur/elodie':
        (new Template('author-elodie'))->render();
        break;

    default:
        bp_render_404();
        break;
}
