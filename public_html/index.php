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
 * Livraison 3 : pages détail ligne (ex: /metro/ligne-1).
 * Charge data/lines/{slug}.json + rend templates/pages/line-metro.php.
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
 * Charge le détail d'une ligne (data/lines/{slug}.json).
 * Retourne false si la ligne n'existe pas.
 *
 * @param string $mode 'metro' | 'rer' | 'bus' | 'tramway' | 'transilien'
 * @param string $code Code de la ligne (1, 2, ..., A, B, T1, ...)
 */
function bp_load_line(string $mode, string $code): array|false {
    $slug = $mode . '-' . strtolower($code);
    $line_path = __DIR__ . '/data/lines/' . $slug . '.json';

    if (!file_exists($line_path)) {
        return false;
    }

    $json = file_get_contents($line_path);
    $line = json_decode($json, true);
    if (!is_array($line)) {
        return false;
    }
    return $line;
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
 * Rend une page détail de ligne.
 *
 * @param string $mode 'metro' (étendable plus tard à 'rer', 'tramway'...)
 * @param string $code Code de la ligne ('1', '14', 'A'...)
 */
function bp_render_line(string $mode, string $code): void {
    $line = bp_load_line($mode, $code);
    if (!$line) {
        bp_render_404();
        return;
    }

    $tpl = new Template('line-' . $mode);
    $tpl->withData(['line' => $line]);
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
    case '/gares':
        // Hub cluster Gares (livraison future : 7 grandes gares parisiennes)
        // Pour l'instant : page squelette "Bientôt disponible"
        (new Template('hub-gares'))->render();
        break;

    // --- Info-Trafic (Livraison 4) ---
    case '/info-trafic':
        // Page liste : on scanne content/info-trafic/ pour lister les articles existants
        $articles = [];
        $contentDir = __DIR__ . '/content/info-trafic/';
        if (is_dir($contentDir)) {
            $files = glob($contentDir . '*.md');
            // Tri par date descendante (les noms commencent par YYYY-MM-DD)
            rsort($files);
            foreach ($files as $file) {
                $slug = basename($file, '.md');
                $article = Article::load('info-trafic', $slug);
                if ($article) {
                    $articles[] = $article;
                }
            }
        }
        $tpl = new Template('info-trafic-index');
        $tpl->withData(['articles' => $articles]);
        $tpl->render();
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
    case '/sources':
        (new Template('sources'))->render();
        break;
    case '/auteur/ludo':
        (new Template('author-ludo'))->render();
        break;
    case '/auteur/elodie':
        (new Template('author-elodie'))->render();
        break;
    case '/tarifs':
        (new Template('tarifs-hub'))->render();
        break;
    case '/tarifs/metro':
        (new Template('tarifs-metro'))->render();
        break;
    case '/tarifs/aeroports':
        (new Template('tarifs-aeroports'))->render();
        break;

    // --- Hubs thematiques (refonte nav niveau 1) ---
    case '/se-deplacer':
        (new Template('hub-se-deplacer'))->render();
        break;
    case '/visiter':
        (new Template('hub-visiter'))->render();
        break;
    case '/itineraires':
        (new Template('itineraires-placeholder'))->render();
        break;

    default:
        // Route dynamique /metro/ligne-{code} (ex: /metro/ligne-1, /metro/ligne-14, /metro/ligne-3bis)
        if (preg_match('#^/metro/ligne-([a-z0-9]+)$#i', $path, $matches)) {
            bp_render_line('metro', $matches[1]);
            break;
        }

        // Route dynamique /rer/ligne-{a|b|c|d|e} - fiche ligne RER
        if (preg_match('#^/rer/ligne-([a-e])$#i', $path, $matches)) {
            $code = strtoupper($matches[1]);
            $file = __DIR__ . '/data/lines-rer/rer-' . strtolower($code) . '.json';
            if (file_exists($file)) {
                $line = json_decode(file_get_contents($file), true);
                if (is_array($line) && ($line['published'] ?? false) === true) {
                    $tpl = new Template('line-rer');
                    $tpl->withData(['line' => $line]);
                    $tpl->render();
                    break;
                }
            }
            bp_render_404();
            break;
        }

        // Route dynamique /rer/station/{slug} - URL canonique par station RER
        // Convention slugs (T16) : "rer-{nomstation}" — distinct des slugs métro
        // pour éviter cannibalisation (ex: chatelet / rer-chatelet-les-halles).
        if (preg_match('#^/rer/station/([a-z0-9\-]+)$#', $path, $matches)) {
            $slug = $matches[1];
            $stationFile = __DIR__ . '/data/stations-rer/' . $slug . '.json';
            if (file_exists($stationFile)) {
                $station = json_decode(file_get_contents($stationFile), true);
                if (is_array($station) && ($station['published'] ?? false) === true) {
                    $tpl = new Template('station-rer');
                    $tpl->withData(['station' => $station]);
                    $tpl->render();
                    break;
                }
            }
            bp_render_404();
            break;
        }

        // Route dynamique /metro/station/{slug} - URL canonique unique par station
        // (peu importe combien de lignes la desservent, évite duplicate content)
        // Garde-fou : la station n'est servie que si "published": true au niveau
        // racine du JSON. Sinon → 404 (squelette en review, pas encore publié).
        // Même critère que Routes::isStationActive() pour les liens internes.
        if (preg_match('#^/metro/station/([a-z0-9\-]+)$#', $path, $matches)) {
            $slug = $matches[1];
            $stationFile = __DIR__ . '/data/stations/' . $slug . '.json';
            if (file_exists($stationFile)) {
                $station = json_decode(file_get_contents($stationFile), true);
                if (is_array($station) && ($station['published'] ?? false) === true) {
                    $tpl = new Template('station-metro');
                    $tpl->withData(['station' => $station]);
                    $tpl->render();
                    break;
                }
            }
            bp_render_404();
            break;
        }

        // Route dynamique /aeroports/{aeroport}/{mode}/{sub} - sous-pages mode (ex: bus/orlybus)
        if (preg_match('#^/aeroports/([a-z0-9\-]+)/([a-z0-9\-]+)/([a-z0-9\-]+)$#', $path, $matches)) {
            $aero = $matches[1]; $mode = $matches[2]; $sub = $matches[3];
            $subFile = __DIR__ . '/data/aeroports/' . $aero . '/' . $mode . '/' . $sub . '.json';
            if (file_exists($subFile)) {
                $subData = json_decode(file_get_contents($subFile), true);
                if (is_array($subData) && ($subData['published'] ?? false) === true) {
                    $tpl = new Template('aeroport-mode');
                    $tpl->withData(['mode' => $subData]);
                    $tpl->render();
                    break;
                }
            }
            bp_render_404();
            break;
        }

        // Route dynamique /aeroports/{aeroport}/{mode} - pages détail par mode
        if (preg_match('#^/aeroports/([a-z0-9\-]+)/([a-z0-9\-]+)$#', $path, $matches)) {
            $aero = $matches[1]; $mode = $matches[2];
            $modeFile = __DIR__ . '/data/aeroports/' . $aero . '/' . $mode . '.json';
            if (file_exists($modeFile)) {
                $modeData = json_decode(file_get_contents($modeFile), true);
                if (is_array($modeData) && ($modeData['published'] ?? false) === true) {
                    $tpl = new Template('aeroport-mode');
                    $tpl->withData(['mode' => $modeData]);
                    $tpl->render();
                    break;
                }
            }
            bp_render_404();
            break;
        }

        // Route dynamique /aeroports/{slug} - 3 aéroports parisiens (CDG, Orly, Beauvais)
        if (preg_match('#^/aeroports/([a-z0-9\-]+)$#', $path, $matches)) {
            $slug = $matches[1];
            $aeroFile = __DIR__ . '/data/aeroports/' . $slug . '.json';
            if (file_exists($aeroFile)) {
                $aeroport = json_decode(file_get_contents($aeroFile), true);
                if (is_array($aeroport) && ($aeroport['published'] ?? false) === true) {
                    $tpl = new Template('aeroport');
                    $tpl->withData(['aeroport' => $aeroport]);
                    $tpl->render();
                    break;
                }
            }
            bp_render_404();
            break;
        }

        // Route dynamique /gare/{slug} - 7 grandes gares parisiennes
        if (preg_match('#^/gare/([a-z0-9\-]+)$#', $path, $matches)) {
            $slug = $matches[1];
            $gareFile = __DIR__ . '/data/gares/' . $slug . '.json';
            if (file_exists($gareFile)) {
                $gare = json_decode(file_get_contents($gareFile), true);
                if (is_array($gare)) {
                    $tpl = new Template('gare-detail');
                    $tpl->withData(['gare' => $gare]);
                    $tpl->render();
                    break;
                }
            }
            bp_render_404();
            break;
        }

        // Route dynamique /info-trafic/YYYY-MM-DD-slug/
        if (preg_match('#^/info-trafic/([0-9]{4}-[0-9]{2}-[0-9]{2}-[a-z0-9\-]+)$#', $path, $matches)) {
            $slug = $matches[1];
            $article = Article::load('info-trafic', $slug);
            if ($article) {
                $tpl = new Template('info-trafic-article');
                $tpl->withData(['article' => $article]);
                $tpl->render();
                break;
            }
        }
        bp_render_404();
        break;
}
