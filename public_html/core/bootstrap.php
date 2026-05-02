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

// Mode debug selon config
$debug = Config::get('site.debug', false);
if ($debug) {
    error_reporting(E_ALL);
    ini_set('display_errors', '1');
} else {
    error_reporting(E_ALL & ~E_DEPRECATED & ~E_STRICT);
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
    function asset(string $path): string {
        return $path;
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
