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
