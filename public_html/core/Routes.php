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
 * Architecture URLs station :
 * --------------------------
 * Les stations ont une URL canonique unique /metro/station/{slug}/, peu importe
 * combien de lignes les desservent. Cela évite la duplication de contenu :
 * "Châtelet" est sur 5 lignes de métro mais a UNE seule URL canonique.
 *
 * Le slug est dérivé du nom (lowercase, sans accent, espaces → tirets) :
 *   "Charles de Gaulle - Étoile" → "charles-de-gaulle-etoile"
 *   "Hôtel de Ville"            → "hotel-de-ville"
 *   "Place d'Italie"            → "place-d-italie"
 *
 * Pour activer une page station, ajouter son slug dans $activeStationSlugs.
 *
 * Architecture cluster Gares :
 * ----------------------------
 * Les 7 grandes gares parisiennes ont leur propre cluster /gare/{slug}/
 * distinct du cluster station métro. Focus voyageur grande ligne (compagnies,
 * billetterie, services), différent du focus transport urbain.
 *
 * À chaque nouvelle page créée, ajouter sa route dans la propriété concernée.
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
        '/gares',                 // Hub cluster gares (page squelette pour l'instant)
        '/info-trafic',
        '/a-propos',
        '/contact',
        '/mentions-legales',
        '/confidentialite',
        '/sources',
        '/auteur/ludo',
        '/auteur/elodie',

        // Pages lignes métro (à activer au fur et à mesure)
        '/metro/ligne-1',

        // Patterns dynamiques
        '~^/info-trafic/[0-9]{4}-[0-9]{2}-[0-9]{2}-[a-z0-9\-]+$~',
    ];

    /**
     * Liste blanche des stations métro actives.
     * Ajouter ici le slug d'une station quand sa page est prête.
     * Tant qu'une station n'est pas listée, son lien est gris (smart-link inactif).
     *
     * Exemples futurs :
     *   'chatelet', 'la-defense', 'charles-de-gaulle-etoile', 'concorde',
     */
    private static array $activeStationSlugs = [
        'chatelet',
    ];

    /**
     * Liste blanche des gares actives (cluster /gare/{slug}/).
     * Périmètre cible : 7 grandes gares parisiennes
     * (Nord, Est, Lyon, Montparnasse, Saint-Lazare, Austerlitz, Bercy).
     */
    private static array $activeGareSlugs = [
        // Aucune gare active pour le moment. À activer au fur et à mesure.
    ];

    /**
     * Vérifie si une URL correspond à une route active.
     */
    public static function exists(string $url): bool
    {
        $clean = rtrim($url, '/');
        if ($clean === '') $clean = '/';

        // 1. Match exact ou regex dans $active
        foreach (self::$active as $route) {
            if (str_starts_with($route, '~') && str_ends_with($route, '~')) {
                if (preg_match($route, $clean) === 1) return true;
            } elseif ($route === $clean) {
                return true;
            }
        }

        // 2. Pages station métro — activation par slug-list
        if (preg_match('~^/metro/station/([a-z0-9\-]+)$~', $clean, $matches) === 1) {
            return in_array($matches[1], self::$activeStationSlugs, true);
        }

        // 3. Pages gare — activation par slug-list
        if (preg_match('~^/gare/([a-z0-9\-]+)$~', $clean, $matches) === 1) {
            return in_array($matches[1], self::$activeGareSlugs, true);
        }

        return false;
    }

    /**
     * Génère le slug canonique d'une station depuis son nom d'affichage.
     *
     * Exemples :
     *   stationSlug("Charles de Gaulle - Étoile") → "charles-de-gaulle-etoile"
     *   stationSlug("Hôtel de Ville")             → "hotel-de-ville"
     *   stationSlug("Place d'Italie")             → "place-d-italie"
     *   stationSlug("La Défense (Grande Arche)")  → "la-defense"
     */
    public static function stationSlug(string $name): string
    {
        // Retirer les compléments entre parenthèses
        $name = preg_replace('/\s*\([^)]*\)\s*/', '', $name);
        // Translittération basique des accents
        $name = strtr($name, [
            'à' => 'a', 'á' => 'a', 'â' => 'a', 'ä' => 'a', 'ã' => 'a',
            'è' => 'e', 'é' => 'e', 'ê' => 'e', 'ë' => 'e',
            'ì' => 'i', 'í' => 'i', 'î' => 'i', 'ï' => 'i',
            'ò' => 'o', 'ó' => 'o', 'ô' => 'o', 'ö' => 'o', 'õ' => 'o',
            'ù' => 'u', 'ú' => 'u', 'û' => 'u', 'ü' => 'u',
            'ç' => 'c', 'ñ' => 'n',
            'À' => 'a', 'Á' => 'a', 'Â' => 'a', 'Ä' => 'a', 'Ã' => 'a',
            'È' => 'e', 'É' => 'e', 'Ê' => 'e', 'Ë' => 'e',
            'Ì' => 'i', 'Í' => 'i', 'Î' => 'i', 'Ï' => 'i',
            'Ò' => 'o', 'Ó' => 'o', 'Ô' => 'o', 'Ö' => 'o', 'Õ' => 'o',
            'Ù' => 'u', 'Ú' => 'u', 'Û' => 'u', 'Ü' => 'u',
            'Ç' => 'c', 'Ñ' => 'n',
        ]);
        // Lowercase
        $slug = strtolower($name);
        // Caractères non alphanumériques → tirets
        $slug = preg_replace('/[^a-z0-9]+/', '-', $slug);
        // Trim tirets en début/fin et tirets multiples
        $slug = trim($slug, '-');
        $slug = preg_replace('/-+/', '-', $slug);
        return $slug;
    }

    /**
     * Construit l'URL canonique d'une page station métro.
     * Usage : Routes::stationUrl("Châtelet") → "/metro/station/chatelet/"
     */
    public static function stationUrl(string $name): string
    {
        return '/metro/station/' . self::stationSlug($name) . '/';
    }
}

/**
 * Helpers globaux pour générer des liens conditionnels.
 *
 * Usage :
 *   echo conditionalLink('/tourisme/monuments/arc-de-triomphe/', 'Arc de Triomphe', 'poi-card__link');
 *
 * Si la page existe (route active), génère un <a>.
 * Sinon, un <span> avec attribut data-future-url et classe modificatrice "--inactive".
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

/**
 * Helper sucre syntaxique pour les liens stations.
 * Usage : echo stationLink("Châtelet", "station-name-link");
 * → <a href="/metro/station/chatelet/" class="station-name-link">Châtelet</a> si actif
 * → <span class="station-name-link station-name-link--inactive" ...>Châtelet</span> sinon
 */
if (!function_exists('stationLink')) {
    function stationLink(string $name, string $cssClass = 'station-link'): string
    {
        return conditionalLink(
            Routes::stationUrl($name),
            htmlspecialchars($name, ENT_QUOTES, 'UTF-8'),
            $cssClass
        );
    }
}
