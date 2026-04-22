<?php
/**
 * Classe Config
 *
 * Chargement centralise et mise en cache des fichiers de config.
 * Usage : Config::get('site.brand_name') ou Config::all('nav')
 */

class Config
{
    private static array $cache = [];

    /**
     * Charge un fichier de config (mis en cache)
     */
    public static function load(string $name): array
    {
        if (!isset(self::$cache[$name])) {
            $path = __DIR__ . '/../config/' . $name . '.php';
            if (!file_exists($path)) {
                throw new RuntimeException("Config '$name' introuvable : $path");
            }
            self::$cache[$name] = require $path;
        }
        return self::$cache[$name];
    }

    /**
     * Recupere une cle avec notation pointee : 'site.brand_name'
     */
    public static function get(string $key, $default = null)
    {
        $parts = explode('.', $key, 2);
        $file = $parts[0];
        $path = $parts[1] ?? null;

        $config = self::load($file);

        if ($path === null) {
            return $config;
        }

        // Support des sous-cles : 'site.social.twitter'
        $segments = explode('.', $path);
        $value = $config;
        foreach ($segments as $segment) {
            if (!is_array($value) || !array_key_exists($segment, $value)) {
                return $default;
            }
            $value = $value[$segment];
        }
        return $value;
    }

    /**
     * Retourne tout un fichier de config
     */
    public static function all(string $name): array
    {
        return self::load($name);
    }
}
