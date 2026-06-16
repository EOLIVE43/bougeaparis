<?php
/**
 * Bootstrap de l'application
 *
 * Charge les classes du noyau, configure l'environnement,
 * definit les helpers globaux.
 */

// Encodage et timezone
mb_internal_encoding('UTF-8');
date_default_timezone_set('Europe/Paris');

// Chargement des classes du noyau (autoload simple)
spl_autoload_register(function ($class) {
    $path = __DIR__ . '/' . $class . '.php';
    if (file_exists($path)) {
        require_once $path;
    }
});

// Helpers métier (fonctions globales : pastilleCorresp, etc.)
require_once __DIR__ . '/helpers.php';

// Helper centralisé titles SEO (bp_title_*)
require_once __DIR__ . '/../templates/helpers/title.php';

// Mode debug selon config
$debug = Config::get('site.debug', false);
if ($debug) {
    error_reporting(E_ALL);
    ini_set('display_errors', '1');
} else {
    // E_STRICT deprecated en PHP 8.4 (retiré en 9.x). E_ALL inclut déjà les
    // niveaux strict ; ne pas l'exclure explicitement (sinon le constant lookup
    // émet lui-même un Deprecated dès 8.4).
    error_reporting(E_ALL & ~E_DEPRECATED);
    ini_set('display_errors', '0');
    ini_set('log_errors', '1');
}

/**
 * Helpers globaux courts (plus pratiques que Template::e())
 */
if (!function_exists('e')) {
    function e(?string $s): string {
        return htmlspecialchars($s ?? '', ENT_QUOTES, 'UTF-8');
    }
}

if (!function_exists('url')) {
    function url(string $path = '/'): string {
        return rtrim(Config::get('site.url'), '/') . $path;
    }
}

if (!function_exists('asset')) {
    /**
     * Versionne les assets locaux (/assets/*) avec ?v=<mtime>.
     * Permet un cache HTTP « immutable » long (1 an) sans risquer
     * que les visiteurs voient une version obsolète après un déploiement :
     * la query string change automatiquement quand le fichier change.
     *
     * Fallback CSS minifié : si /assets/css/X.css est demandé ET qu'un
     * /assets/css/X.min.css existe à côté (généré en CI au déploiement,
     * jamais commité au repo), on sert le .min.css. Le mtime du fichier
     * réellement servi est utilisé pour le cache-bust, donc les caches
     * navigateur restent cohérents entre dev (source) et prod (minifié).
     */
    function asset(string $path): string {
        if ($path === '' || $path[0] !== '/') {
            return $path;
        }
        $base = __DIR__ . '/..';

        // Bascule .css → .min.css si l'artefact minifié est présent
        $serve = $path;
        if (substr($path, -4) === '.css' && substr($path, -8) !== '.min.css') {
            $minPath = substr($path, 0, -4) . '.min.css';
            if (is_file($base . $minPath)) {
                $serve = $minPath;
            }
        }

        $absolute = $base . $serve;
        if (is_file($absolute)) {
            $mtime = @filemtime($absolute);
            if ($mtime) {
                $sep = (strpos($serve, '?') === false) ? '?' : '&';
                return $serve . $sep . 'v=' . $mtime;
            }
        }
        return $serve;
    }
}

if (!function_exists('component')) {
    function component(string $name, array $props = []): void {
        Template::component($name, $props);
    }
}

/**
 * Helper : charge les conditional-link helpers (Routes::exists + conditionalLink*).
 * Routes est chargée automatiquement par l'autoload via Routes::exists(),
 * mais les fonctions globales conditionalLink* doivent être définies ici.
 *
 * On force l'inclusion une fois pour avoir les fonctions globales disponibles.
 */
class_exists('Routes'); // déclenche l'autoload
