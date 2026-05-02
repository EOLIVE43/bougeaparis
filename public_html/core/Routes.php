<?php
/**
 * Classe Routes
 *
 * Registre des routes connues (pages effectivement servies par index.php).
 * Permet aux helpers conditionalLink* de savoir si une URL doit être un
 * <a> cliquable (page existante) ou un <span> en attente (page future).
 *
 * Stratégie SEO : on pose tous les liens internes dès maintenant. Ils
 * s'activent automatiquement dès qu'une route est ajoutée ici.
 *
 * À chaque nouvelle page créée, ajouter sa route ci-dessous.
 */

class Routes
{
    /**
     * Liste des routes "actives" : URL exactes ou patterns regex.
     * Les patterns commencent par '~' et finissent par '~'.
     */
    private static array $active = [
        // Pages racines existantes
        '/',
        '/metro',
        '/rer',
        '/bus',
        '/tramway',
        '/aeroports',
        '/transilien',
        '/info-trafic',
        '/a-propos',
        '/contact',
        '/mentions-legales',
        '/confidentialite',
        '/auteur/ludo',
        '/auteur/elodie',

        // Pages lignes métro (à activer au fur et à mesure)
        '/metro/ligne-1',

        // Patterns dynamiques
        '~^/info-trafic/[0-9]{4}-[0-9]{2}-[0-9]{2}-[a-z0-9\-]+$~',
    ];

    /**
     * Vérifie si une URL correspond à une route active.
     */
    public static function exists(string $url): bool
    {
        $clean = rtrim($url, '/');
        if ($clean === '') $clean = '/';

        foreach (self::$active as $route) {
            if (str_starts_with($route, '~') && str_ends_with($route, '~')) {
                if (preg_match($route, $clean) === 1) return true;
            } elseif ($route === $clean) {
                return true;
            }
        }
        return false;
    }
}

/**
 * Helpers globaux pour générer des liens conditionnels.
 *
 * Usage :
 *   echo conditionalLink('/tourisme/monuments/arc-de-triomphe/', 'Arc de Triomphe', 'poi-card__link');
 *
 * Si la page existe (route active dans Routes::$active), génère un <a>.
 * Sinon, un <span> avec attribut data-future-url, plus une classe modificatrice
 * "--inactive" pour styler différemment côté CSS.
 */
if (!function_exists('conditionalLink')) {
    function conditionalLink(string $url, string $content, string $cssClass = ''): string
    {
        $exists = Routes::exists($url);
        $cssClassFull = trim($cssClass . ($exists ? '' : ' ' . $cssClass . '--inactive'));

        if ($exists) {
            return sprintf(
                '<a href="%s" class="%s">%s</a>',
                htmlspecialchars($url, ENT_QUOTES, 'UTF-8'),
                htmlspecialchars($cssClassFull, ENT_QUOTES, 'UTF-8'),
                $content
            );
        }
        return sprintf(
            '<span class="%s" data-future-url="%s">%s</span>',
            htmlspecialchars($cssClassFull, ENT_QUOTES, 'UTF-8'),
            htmlspecialchars($url, ENT_QUOTES, 'UTF-8'),
            $content
        );
    }
}

if (!function_exists('conditionalLinkOpen')) {
    function conditionalLinkOpen(string $url, string $cssClass = ''): string
    {
        $exists = Routes::exists($url);
        $cssClassFull = trim($cssClass . ($exists ? '' : ' ' . $cssClass . '--inactive'));

        if ($exists) {
            return sprintf(
                '<a href="%s" class="%s">',
                htmlspecialchars($url, ENT_QUOTES, 'UTF-8'),
                htmlspecialchars($cssClassFull, ENT_QUOTES, 'UTF-8')
            );
        }
        return sprintf(
            '<div class="%s" data-future-url="%s">',
            htmlspecialchars($cssClassFull, ENT_QUOTES, 'UTF-8'),
            htmlspecialchars($url, ENT_QUOTES, 'UTF-8')
        );
    }
}

if (!function_exists('conditionalLinkClose')) {
    function conditionalLinkClose(string $url): string
    {
        return Routes::exists($url) ? '</a>' : '</div>';
    }
}
