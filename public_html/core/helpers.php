<?php
/**
 * Helpers de rendu spécifiques aux pages de transport
 * (pastille de correspondance, formats de date FR, etc.)
 *
 * Note : les fonctions globales courtes (e, url, asset, component) sont
 * dans bootstrap.php. Ce fichier regroupe les helpers métier transport.
 */

if (!function_exists('dateFr')) {
    /**
     * Formate une date en français sans dépendre de strftime() (déprécié PHP 8.1+)
     * ni de la locale système (instable selon hébergeur).
     *
     * Usage :
     *   dateFr()                        // "vendredi 2 mai 2026"
     *   dateFr(time(), 'short')         // "2 mai 2026"
     *   dateFr('2026-04-28', 'short')   // "28 avril 2026"
     *   dateFr(null, 'long_with_day')   // "vendredi 2 mai 2026"
     *
     * @param int|string|null $date  Timestamp, date string (parsable par strtotime), ou null pour "now"
     * @param string $format         'short' | 'long_with_day' (défaut)
     */
    function dateFr($date = null, string $format = 'long_with_day'): string
    {
        if ($date === null) {
            $ts = time();
        } elseif (is_int($date)) {
            $ts = $date;
        } else {
            $ts = strtotime((string)$date);
            if ($ts === false) return '';
        }

        $jours = [
            'Monday'    => 'lundi',
            'Tuesday'   => 'mardi',
            'Wednesday' => 'mercredi',
            'Thursday'  => 'jeudi',
            'Friday'    => 'vendredi',
            'Saturday'  => 'samedi',
            'Sunday'    => 'dimanche',
        ];
        $mois = [
            1 => 'janvier', 2 => 'février', 3 => 'mars',     4 => 'avril',
            5 => 'mai',     6 => 'juin',    7 => 'juillet',  8 => 'août',
            9 => 'septembre', 10 => 'octobre', 11 => 'novembre', 12 => 'décembre',
        ];

        $j = (int)date('j', $ts);
        $m = $mois[(int)date('n', $ts)];
        $y = (int)date('Y', $ts);
        $d = $jours[date('l', $ts)];

        if ($format === 'short') {
            return sprintf('%d %s %d', $j, $m, $y);
        }
        return sprintf('%s %d %s %d', $d, $j, $m, $y);
    }
}

if (!function_exists('pastilleCorresp')) {
    /**
     * Pastille Correspondance — SVG inline réutilisable
     *
     * Usage :
     *   echo pastilleCorresp('M',     '14', '#62259D');
     *   echo pastilleCorresp('RER',   'A',  '#E2231A');
     *   echo pastilleCorresp('T',     '2',  '#cead2c');
     *   echo pastilleCorresp('TRANS', 'L',  '#7A99C9');
     *
     * @param string $mode  "M" | "RER" | "T" | "TRANS"
     * @param string $line  "1" à "14", "A" à "E", etc.
     * @param string $color Couleur officielle de la ligne (#FFCD00…)
     * @param string $size  "default" | "small" | "large" | "inline"
     */
    function pastilleCorresp(string $mode, string $line, string $color, string $size = 'default'): string
    {
        $sizes = [
            'small'   => ['fontMode' => 9,  'fontLine' => 10, 'padX' => 6,  'padY' => 2, 'gap' => 5, 'radius' => 4, 'border' => 1],
            'inline'  => ['fontMode' => 10, 'fontLine' => 11, 'padX' => 7,  'padY' => 2, 'gap' => 6, 'radius' => 5, 'border' => 1.2],
            'default' => ['fontMode' => 12, 'fontLine' => 13, 'padX' => 9,  'padY' => 3, 'gap' => 8, 'radius' => 6, 'border' => 1.2],
            'large'   => ['fontMode' => 14, 'fontLine' => 15, 'padX' => 11, 'padY' => 4, 'gap' => 9, 'radius' => 7, 'border' => 1.5],
        ];
        $s = $sizes[$size] ?? $sizes['default'];

        $modeChars = strlen($mode);
        $lineChars = strlen($line);
        $modeWidth = $modeChars * $s['fontMode'] * 0.65;
        $lineWidth = $lineChars * $s['fontLine'] * 0.62;

        $totalWidth  = $s['padX'] + $modeWidth + $s['gap'] + $lineWidth + $s['padX'];
        $totalHeight = max($s['fontMode'], $s['fontLine']) + ($s['padY'] * 2) + 2;

        $textY = ($totalHeight / 2) + ($s['fontMode'] / 3.2);
        $modeX = $s['padX'];
        $lineX = $s['padX'] + $modeWidth + $s['gap'];

        $color = htmlspecialchars($color, ENT_QUOTES, 'UTF-8');
        $mode  = htmlspecialchars($mode,  ENT_QUOTES, 'UTF-8');
        $line  = htmlspecialchars($line,  ENT_QUOTES, 'UTF-8');
        $aria  = $mode . ' ligne ' . $line;

        return <<<SVG
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {$totalWidth} {$totalHeight}"
     width="{$totalWidth}"
     height="{$totalHeight}"
     class="pastille-svg"
     role="img"
     aria-label="{$aria}">
  <title>{$aria}</title>
  <rect x="{$s['border']}" y="{$s['border']}"
        width="{$totalWidth}" height="{$totalHeight}"
        rx="{$s['radius']}" ry="{$s['radius']}"
        fill="white"
        stroke="{$color}"
        stroke-width="{$s['border']}"
        transform="translate(-{$s['border']}, -{$s['border']})"/>
  <text x="{$modeX}" y="{$textY}"
        font-family="Inter, sans-serif"
        font-size="{$s['fontMode']}"
        font-weight="600"
        fill="{$color}">{$mode}</text>
  <text x="{$lineX}" y="{$textY}"
        font-family="Inter, sans-serif"
        font-size="{$s['fontLine']}"
        font-weight="400"
        fill="{$color}">{$line}</text>
</svg>
SVG;
    }
}
if (!function_exists('getLineSchedule')) {
    /**
     * Charge et retourne les horaires d'une ligne depuis son JSON.
     *
     * Réutilise les données déjà saisies dans data/lines/{slug}.json (clé "schedule").
     * Cache mémoire intra-requête : si on appelle 5 fois pour la même ligne sur
     * la même page (ex: page station Châtelet avec 5 lignes), un seul read disque.
     *
     * Usage :
     *   $schedule = getLineSchedule('metro-1');
     *   if ($schedule) {
     *       echo $schedule['first_departure']['weekday']; // "5h30"
     *   }
     *
     * @param string $lineSlug Slug de la ligne (ex: "metro-1", "metro-14")
     * @return array<string,mixed>|null Section "schedule" du JSON, ou null si absent/erreur
     */
    function getLineSchedule(string $lineSlug): ?array
    {
        static $cache = [];

        if (array_key_exists($lineSlug, $cache)) {
            return $cache[$lineSlug];
        }

        // Sanitize : on n'accepte que des slugs alphanumériques + tirets
        if (!preg_match('/^[a-z0-9-]+$/', $lineSlug)) {
            return $cache[$lineSlug] = null;
        }

        $path = __DIR__ . '/../data/lines/' . $lineSlug . '.json';

        if (!is_file($path)) {
            return $cache[$lineSlug] = null;
        }

        $raw = @file_get_contents($path);
        if ($raw === false) {
            return $cache[$lineSlug] = null;
        }

        $data = json_decode($raw, true);
        if (!is_array($data) || empty($data['schedule'])) {
            return $cache[$lineSlug] = null;
        }

        return $cache[$lineSlug] = $data['schedule'];
    }
}
