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
     * Pastille Correspondance — SVG inline, style fill cohérent avec .line-pill
     *
     * Refonte 2026-05-12 (correction 16c) : passage du style outline (rect blanc
     * + bordure colorée + 2 textes séparés "M" + "1") au style fill (forme pleine
     * couleur + 1 label centré "M1") pour cohérence visuelle avec le composant
     * .line-pill de bundle.css (cf. corrections 15, 16a, 16b).
     *
     * Formes :
     *   - mode "M" + line numérique → cercle plein (équiv. .line-pill--metro)
     *   - mode "M" + line "Xbis"    → pill allongée (équiv. .line-pill--metro-bis)
     *   - mode "RER" / "T" / "TRANS" → rect arrondi rx=6 (équiv. .line-pill--square)
     *
     * Couleur de texte : calculée via YIQ formula sur le fond (luminance ≥ 150
     * = texte noir, sinon blanc). Pas hardcodé — fonctionne sur toute couleur.
     *
     * Usage (signature inchangée vs ancien helper) :
     *   echo pastilleCorresp('M',     '14', '#62259D');
     *   echo pastilleCorresp('RER',   'A',  '#E2231A');
     *   echo pastilleCorresp('T',     '2',  '#cead2c');
     *   echo pastilleCorresp('TRANS', 'L',  '#7A99C9');
     *
     * @param string $mode  "M" | "RER" | "T" | "TRANS"
     * @param string $line  "1" à "14", "A" à "E", "3a", "3b", "H", "3bis", etc.
     * @param string $color Couleur officielle de la ligne (#FFCD00…)
     * @param string $size  "inline" (22px) | "small" (26px) | "default" (32px) | "large" (40px)
     */
    function pastilleCorresp(string $mode, string $line, string $color, string $size = 'default'): string
    {
        // Hauteur en px selon le variant (match .line-pill 32 desktop / 28 mobile)
        $sizes = [
            'inline'  => 22,
            'small'   => 26,
            'default' => 32,
            'large'   => 40,
        ];
        $h = $sizes[$size] ?? $sizes['default'];

        // Label affiché — cohérent avec .line-pill (M1, RER A, T3a, H…)
        $modeUpper = strtoupper($mode);
        switch ($modeUpper) {
            case 'M':     $label = 'M' . $line; break;
            case 'RER':   $label = 'RER ' . $line; break;
            case 'T':     $label = 'T' . $line; break;
            case 'TRANS': $label = $line; break; // lettre seule pour Transilien
            default:      $label = $line;
        }

        // Détermine la forme : cercle métro / pill allongée bis / square autres
        $isMetroBis = ($modeUpper === 'M') && (bool)preg_match('/bis$/i', $line);
        $isMetro    = ($modeUpper === 'M') && !$isMetroBis;

        // Couleur de texte selon contraste WCAG AA (≥ 4.5:1) — correction 2026-05-12.
        // L'ancien YIQ ≥ 150 donnait des FAILS WCAG sur ~13 couleurs (cf. .line-pill).
        // Nouvelle approche : compute le ratio WCAG strict (luminance relative) sur
        // les 2 candidats (#000 / #fff), retourne celui qui passe ≥ 4.5:1.
        // Si les 2 passent, préfère #000 (signalétique RATP usuelle sur fonds clairs).
        // Si les 2 fail (rare, couleur très moyenne), fallback sur le meilleur ratio.
        $hex = ltrim($color, '#');
        if (strlen($hex) === 3) {
            $hex = $hex[0] . $hex[0] . $hex[1] . $hex[1] . $hex[2] . $hex[2];
        }
        if (strlen($hex) !== 6 || !ctype_xdigit($hex)) {
            $color = '#5d6970';
            $hex = '5d6970';
        }
        $r = hexdec(substr($hex, 0, 2));
        $g = hexdec(substr($hex, 2, 2));
        $b = hexdec(substr($hex, 4, 2));
        // Relative luminance (WCAG 2.x formula sRGB)
        $linearize = function ($c) {
            $v = $c / 255;
            return $v <= 0.03928 ? $v / 12.92 : pow(($v + 0.055) / 1.055, 2.4);
        };
        $L_bg    = 0.2126 * $linearize($r) + 0.7152 * $linearize($g) + 0.0722 * $linearize($b);
        $L_white = 1.0; // luminance #fff = 1.0
        $L_black = 0.0; // luminance #000 = 0.0
        $ratioWhite = (max($L_bg, $L_white) + 0.05) / (min($L_bg, $L_white) + 0.05);
        $ratioBlack = (max($L_bg, $L_black) + 0.05) / (min($L_bg, $L_black) + 0.05);
        if ($ratioBlack >= 4.5) {
            $textColor = '#000000'; // préfère noir si passe AA
        } elseif ($ratioWhite >= 4.5) {
            $textColor = '#FFFFFF';
        } else {
            // Aucun ne passe AA strict : prendre le meilleur
            $textColor = $ratioBlack >= $ratioWhite ? '#000000' : '#FFFFFF';
        }

        // Police & dimensions calculées
        $fontSize   = round($h * 0.42, 1); // ~9-17 px selon hauteur
        $fontFamily = 'system-ui, -apple-system, "Segoe UI", Inter, sans-serif';
        $charWidth  = $fontSize * 0.62;
        $textWidth  = mb_strlen($label, 'UTF-8') * $charWidth;
        $pad        = $h * 0.3;
        $contentW   = $textWidth + $pad * 2;

        if ($isMetro) {
            // Cercle parfait — w = h
            $w  = $h;
            $rx = $h / 2;
            $ry = $h / 2;
        } elseif ($isMetroBis) {
            // Pill allongée — min-width 1.5h pour accueillir "M3bis"
            $w  = max($contentW, $h * 1.5);
            $rx = $h / 2;
            $ry = $h / 2;
        } else {
            // Square arrondi — min-width = h, w auto selon contenu
            $w  = max($contentW, $h);
            $rx = 6;
            $ry = 6;
        }

        $textX = $w / 2;
        $textY = $h / 2 + $fontSize * 0.35; // centrage vertical alphabetic baseline

        // Aria-label sémantique pour accessibilité
        switch ($modeUpper) {
            case 'M':     $aria = 'Ligne ' . $line . ' du métro'; break;
            case 'RER':   $aria = 'RER ' . $line; break;
            case 'T':     $aria = 'Tramway ' . $line; break;
            case 'TRANS': $aria = 'Transilien ' . $line; break;
            default:      $aria = $label;
        }

        // Échappement HTML
        $colorE = htmlspecialchars($color, ENT_QUOTES, 'UTF-8');
        $labelE = htmlspecialchars($label, ENT_QUOTES, 'UTF-8');
        $ariaE  = htmlspecialchars($aria,  ENT_QUOTES, 'UTF-8');

        return <<<SVG
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {$w} {$h}"
     width="{$w}"
     height="{$h}"
     class="pastille-svg"
     role="img"
     aria-label="{$ariaE}">
  <title>{$ariaE}</title>
  <rect x="0" y="0" width="{$w}" height="{$h}"
        rx="{$rx}" ry="{$ry}"
        fill="{$colorE}"/>
  <text x="{$textX}" y="{$textY}"
        font-family="{$fontFamily}"
        font-size="{$fontSize}"
        font-weight="700"
        fill="{$textColor}"
        text-anchor="middle"
        dominant-baseline="alphabetic">{$labelE}</text>
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

// =============================================================================
// LINE-PILL — Helper de forme de pastille selon le mode de transport
// =============================================================================

if (!function_exists('linePillShape')) {
    /**
     * Retourne le modificateur de forme CSS pour une pastille de ligne, selon
     * le label fourni. Utilisé conjointement avec .line-pill et .line-pill--{slug}
     * (cf. bundle.css section LINE-PILL).
     *
     *   M1, M2, ..., M14         → 'metro'      (rond parfait 32×32 px)
     *   M3bis, M7bis             → 'metro-bis'  (pill allongé pour label long)
     *   RER A-E, T1-T13, H/J/.../U → 'square'   (carré arrondi border-radius 6px)
     *   défaut (inconnu)         → 'square'    (fallback safe)
     *
     * Usage :
     *   $shape = linePillShape('M1');     // "metro"
     *   $shape = linePillShape('M3bis');  // "metro-bis"
     *   $shape = linePillShape('RER A');  // "square"
     *   echo "<span class='line-pill line-pill--{$shape} line-pill--m1'>M1</span>";
     *
     * @param string $line Label de la ligne (ex: "M1", "M14", "RER A", "T3a", "H")
     * @return string      'metro' | 'metro-bis' | 'square'
     */
    function linePillShape(string $line): string
    {
        $line = trim($line);
        // M{n}bis (rare : M3bis, M7bis) → forme allongée
        if (preg_match('/^M\d+bis$/i', $line)) {
            return 'metro-bis';
        }
        // M{n} (M1, M2, ..., M14) → rond parfait
        if (preg_match('/^M\d+$/i', $line)) {
            return 'metro';
        }
        // RER, T, Transilien (H/J/K/L/N/P/R/U) → carré arrondi
        return 'square';
    }
}

// =============================================================================
// TARIFS IDFM (source unique : data/tarifs.json)
// =============================================================================

if (!function_exists('getTarif')) {
    /**
     * Lit une valeur de data/tarifs.json. Source unique pour TOUS les tarifs
     * affichés sur le site (home, FAQ, pages stations, hubs).
     *
     * Mise à jour annuelle (chaque janvier) depuis la page IDFM officielle
     * (cf. _meta.source_url dans le JSON). Quand le JSON est à jour, l'ensemble
     * des pages se met à jour automatiquement (~300 pages cibles).
     *
     * Cache mémoire intra-requête : 1 seul read disque même si appelé 50 fois.
     *
     * Usage :
     *   echo getTarif('ticket_metro_train_rer', 'price');     // "2,50 €"
     *   echo getTarif('navigo_decouverte', 'weekly_price');   // "32,40 €"
     *   echo getTarif('aeroports', 'price');                  // "14 €"
     *   $bloc = getTarif('navigo_decouverte');                // tableau complet
     *   $meta = getTarif('_meta', 'last_updated');            // "2026-01-01"
     *
     * @param string      $key    Clé top-level (ex: 'ticket_metro_train_rer', 'navigo_decouverte', 'aeroports', '_meta')
     * @param string|null $subkey Sous-clé optionnelle (ex: 'price', 'weekly_price', 'description')
     * @return mixed|null         Valeur (string ou array), ou null si absente.
     */
    function getTarif(string $key, ?string $subkey = null)
    {
        static $cache = null;

        if ($cache === null) {
            $path = __DIR__ . '/../data/tarifs.json';
            if (!is_file($path)) {
                $cache = [];
                return null;
            }
            $raw = @file_get_contents($path);
            $data = $raw ? json_decode($raw, true) : null;
            $cache = is_array($data) ? $data : [];
        }

        if (!array_key_exists($key, $cache)) {
            return null;
        }
        if ($subkey === null) {
            return $cache[$key];
        }
        return is_array($cache[$key]) ? ($cache[$key][$subkey] ?? null) : null;
    }
}

// =============================================================================
// TRAFIC TEMPS REEL (PRIM IDFM)
// =============================================================================

if (!function_exists('getDisruptionsForStation')) {
    /**
     * Recupere les perturbations PRIM impactant les lignes desservant une station.
     *
     * Pipeline (avec cache 5 min via PrimClient) :
     *   1. Lit la cle PRIM depuis secrets.php (PRIM_API_KEY) ou getenv.
     *   2. PrimClient::fetchDisruptions() avec cache fichier 5 min
     *      dans public_html/api/cache/prim/.
     *   3. DisruptionFilter::filter() -> garde les actives + scope editorial.
     *   4. DisruptionFormatter::groupByLine() -> indexe par slug "mode-ligne-X".
     *   5. Filtre par les codes de lignes de la station (ex. ['1','4','7','11','14']
     *      pour Chatelet).
     *
     * Graceful degradation : si la cle est absente, l'API plante et que le
     * cache n'existe pas, retourne null. Le composant qui consomme verifie
     * et n'affiche rien dans ce cas.
     *
     * @param array<int,array{code:string,color?:string,text_color?:string}> $stationLines
     *        Le champ $station['lines'] du JSON station.
     * @return array{has_disruption:bool,max_severity:?string,
     *               lines_with_disruptions:array,lines_normal:array,
     *               fetched_at:?string}|null
     */
    function getDisruptionsForStation(array $stationLines): ?array
    {
        if (empty($stationLines)) return null;

        // 1. Cle (secrets.php > env), convention PRIM_API_KEY uppercase
        //    alignee avec scripts/generate-article.php et le workflow GitHub.
        $key = null;
        $secretsPath = __DIR__ . '/../config/secrets.php';
        if (is_file($secretsPath)) {
            $secrets = @include $secretsPath;
            if (is_array($secrets)) {
                $key = $secrets['PRIM_API_KEY'] ?? $secrets['prim_api_key'] ?? null;
            }
        }
        if (!$key) $key = getenv('PRIM_API_KEY') ?: null;
        if (!$key || $key === 'COLLER_ICI_VOTRE_CLE_API_PRIM') {
            return null; // graceful : pas de bloc trafic
        }

        // 2. PrimClient + filter/formatter (lazy require)
        require_once __DIR__ . '/PrimClient.php';
        require_once __DIR__ . '/DisruptionFilter.php';
        require_once __DIR__ . '/DisruptionFormatter.php';

        $cacheDir = __DIR__ . '/../api/cache/prim';
        try {
            $client = new PrimClient($key, $cacheDir);
            $raw = $client->fetchDisruptions();
        } catch (\Throwable $e) {
            return null;
        }
        if (!is_array($raw)) return null;

        // 3. Filtre + groupByLine
        $networks = require __DIR__ . '/../config/networks.php';
        $filter = new DisruptionFilter($networks);
        $filtered = $filter->filter($raw);
        $formatter = new DisruptionFormatter($networks);
        $byLine = $formatter->groupByLine($filtered);

        // 4. Filtrer aux lignes de la station. Slug PRIM = "metro/ligne-{code}",
        //    cle dans groupByLine = "metro-ligne-{code}" (le "/" devient "-").
        $linesWithDisruptions = [];
        $linesNormal = [];
        $maxSeverityWeight = 0;
        $maxSeverity = null;
        $severityWeights = $networks['severity_weight'] ?? [
            'BLOQUANTE' => 30, 'PERTURBEE' => 20, 'INFORMATION' => 10,
        ];

        foreach ($stationLines as $line) {
            $code = (string)($line['code'] ?? '');
            if ($code === '') continue;
            $primKey = 'metro-ligne-' . strtolower($code);
            $entry = $byLine[$primKey] ?? null;
            if ($entry !== null && !empty($entry['disruptions'])) {
                // Dedup PRIM peut emettre 2 disruptions au meme titre/severite
                $seen = [];
                $unique = [];
                foreach ($entry['disruptions'] as $d) {
                    $sig = ($d['severity'] ?? '') . '|' . ($d['title'] ?? '');
                    if (isset($seen[$sig])) continue;
                    $seen[$sig] = true;
                    $unique[] = $d;
                    $w = (int)($severityWeights[$d['severity'] ?? ''] ?? 0);
                    if ($w > $maxSeverityWeight) {
                        $maxSeverityWeight = $w;
                        $maxSeverity = $d['severity'] ?? null;
                    }
                }
                $linesWithDisruptions[] = [
                    'code'        => $code,
                    'color'       => (string)($line['color'] ?? '#888'),
                    'text_color'  => (string)($line['text_color'] ?? '#fff'),
                    'disruptions' => $unique,
                ];
            } else {
                $linesNormal[] = $code;
            }
        }

        return [
            'has_disruption'         => !empty($linesWithDisruptions),
            'max_severity'           => $maxSeverity,
            'lines_with_disruptions' => $linesWithDisruptions,
            'lines_normal'           => $linesNormal,
            'fetched_at'             => date('c'),
        ];
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

if (!function_exists('getLineMeta')) {
    /**
     * Retourne les meta d'une ligne (terminus, code, name) depuis
     * data/lines/{slug}.json. Cache memoire intra-requete.
     *
     * Usage :
     *   $meta = getLineMeta('metro-1');
     *   if ($meta) {
     *       echo $meta['terminus_a']; // "La Defense (Grande Arche)"
     *       echo $meta['terminus_b']; // "Chateau de Vincennes"
     *   }
     *
     * @param string $lineSlug Slug fichier (ex: "metro-1", "metro-3bis")
     * @return array{terminus_a:string,terminus_b:string,code:string,name:string}|null
     */
    function getLineMeta(string $lineSlug): ?array
    {
        static $cache = [];
        if (array_key_exists($lineSlug, $cache)) return $cache[$lineSlug];
        if (!preg_match('/^[a-z0-9-]+$/', $lineSlug)) return $cache[$lineSlug] = null;
        $path = __DIR__ . '/../data/lines/' . $lineSlug . '.json';
        if (!is_file($path)) return $cache[$lineSlug] = null;
        $raw = @file_get_contents($path);
        if ($raw === false) return $cache[$lineSlug] = null;
        $data = json_decode($raw, true);
        if (!is_array($data)) return $cache[$lineSlug] = null;
        $tA = (string)($data['terminus_a'] ?? '');
        $tB = (string)($data['terminus_b'] ?? '');
        if ($tA === '' && $tB === '') return $cache[$lineSlug] = null;
        return $cache[$lineSlug] = [
            'terminus_a' => $tA,
            'terminus_b' => $tB,
            'code'       => (string)($data['code'] ?? ''),
            'name'       => (string)($data['name'] ?? ''),
        ];
    }
}

if (!function_exists('getRerTerminus')) {
    /**
     * Retourne les terminus d'une ligne RER, structures par direction.
     *
     * Utilise la config curatoriale config/rer-terminus.php (libelles GTFS
     * officiels). Cache memoire intra-requete.
     *
     * Usage :
     *   $info = getRerTerminus('A');
     *   foreach ($info['directions'] as $dir) {
     *       echo $dir['label']; // "ouest"
     *       echo implode(', ', $dir['terminus']); // "Saint-Germain..., Cergy..."
     *   }
     *
     * @param string $code Code RER (A, B, C, D, E)
     * @return array{directions:array<int,array{label:string,terminus:array<int,string>}>}|null
     */
    function getRerTerminus(string $code): ?array
    {
        static $config = null;
        if ($config === null) {
            $path = __DIR__ . '/../config/rer-terminus.php';
            $config = is_file($path) ? require $path : [];
            if (!is_array($config)) $config = [];
        }
        $code = strtoupper(trim($code));
        return $config[$code] ?? null;
    }
}

// =============================================================================
// LIBELLES IDFM (helper d'affichage)
// =============================================================================

if (!function_exists('expandIdfmAbbreviations')) {
    /**
     * Etend les abreviations courantes des libelles IDFM/GTFS en versions
     * lisibles. Utilise UNIQUEMENT a l'affichage : les fichiers data/ gardent
     * les libelles bruts du GTFS.
     *
     * Exemples :
     *   "r. de Rivoli"        → "Rue de Rivoli"
     *   "pl. Ste-Opportune"   → "Place Sainte-Opportune"
     *   "av. Victoria"        → "Avenue Victoria"
     *   "bd Sébastopol"       → "Boulevard Sébastopol"
     *   "Forum - Pte Lescot"  → "Forum - Porte Lescot"
     *   "St-Denis-Pleyel"     → "Saint-Denis-Pleyel"
     *   "Mal Foch"            → "Maréchal Foch"
     *
     * Ne touche pas aux mots qui ne matchent pas une abreviation cataloguee :
     *   "Rivoli" reste "Rivoli", "rue de Rivoli" reste "rue de Rivoli".
     */
    function expandIdfmAbbreviations(string $text): string
    {
        if ($text === '') return $text;

        static $patterns = null, $replacements = null;
        if ($patterns === null) {
            // Ordre crucial : Ste avant St, Gnal avant Gal pour eviter
            // les chevauchements (St matcherait sinon le debut de Ste).
            $map = [
                // Voies en bas de casse avec point + espace
                'r\. '   => 'Rue ',
                'pl\. '  => 'Place ',
                'av\. '  => 'Avenue ',
                'bd\. '  => 'Boulevard ',
                'bld\. ' => 'Boulevard ',
                'imp\. ' => 'Impasse ',
                'sq\. '  => 'Square ',
                'rte\. ' => 'Route ',
                // Sans point (rare mais possible : "bd Sebastopol")
                'bd '    => 'Boulevard ',
                // Mot a simplement capitaliser
                'allée ' => 'Allée ',
                // Voies capitalisees avec point
                'R\. '   => 'Rue ',
                'Pl\. '  => 'Place ',
                'Av\. '  => 'Avenue ',
                // Prefixes "saints"/Porte avant espace ou tiret (Ste avant St)
                'Ste(?=[\s\-])' => 'Sainte',
                'St(?=[\s\-])'  => 'Saint',
                'Pte(?=[\s\-])' => 'Porte',
                // Titres (Gnal avant Gal)
                'Mal(?=[\s\-])'  => 'Maréchal',
                'Pdt(?=[\s\-])'  => 'Président',
                'Gnal(?=[\s\-])' => 'Général',
                'Gal(?=[\s\-])'  => 'Général',
                'Cdt(?=[\s\-])'  => 'Commandant',
            ];
            $patterns     = [];
            $replacements = [];
            foreach ($map as $p => $r) {
                // \b en debut : non-mot ou debut de chaine devant l'abreviation.
                $patterns[]     = '/\b' . $p . '/u';
                $replacements[] = $r;
            }
        }
        return preg_replace($patterns, $replacements, $text);
    }
}

if (!function_exists('richText')) {
    /**
     * Sanitize un texte éditorial qui peut contenir du HTML inline.
     * Whitelist : <strong>, <em>, <br>, <a> uniquement. Tout le reste strippé.
     *
     * Utilisé pour les champs de contenu rédactionnel (descriptions FAQ,
     * anecdotes, history, itineraires, popular_routes, accessibility tips,
     * works) où l'auteur peut mettre en gras des mots-clés ou ajouter
     * des liens internes.
     *
     * Sécurité : les JSON éditoriaux sont commités côté admin, pas
     * user-generated → pas de risque XSS direct. La whitelist sert
     * surtout de garde-fou contre des balises affichées en clair par
     * htmlspecialchars (bug constaté FAQ ligne 9 : "<strong>" affiché
     * littéralement).
     */
    function richText(?string $content): string {
        if ($content === null || $content === '') return '';
        return strip_tags($content, '<strong><em><br><a>');
    }
}

if (!function_exists('wrapStationName')) {
    /**
     * Casse les noms de stations longs en 2 lignes pour le plan visuel.
     * Retourne du HTML déjà échappé (htmlspecialchars + <br>).
     *
     * Règles (par ordre de priorité) :
     *  1. Si le nom contient " - " (séparateur composé) → wrap au tiret
     *  2. Sinon si > 16 caractères et contient un espace → wrap au premier espace
     *     après position 8 (préfère un point d'équilibre)
     *  3. Sinon → nom inchangé
     */
    function wrapStationName(string $name): string {
        $name = trim($name);
        $len = mb_strlen($name);
        // 1. Tiret entouré d'espaces : "La Motte-Picquet - Grenelle"
        if (strpos($name, ' - ') !== false) {
            [$left, $right] = explode(' - ', $name, 2);
            return htmlspecialchars(trim($left), ENT_QUOTES, 'UTF-8')
                . '<br>- '
                . htmlspecialchars(trim($right), ENT_QUOTES, 'UTF-8');
        }
        // 2. Nom > 19 chars : split à l'espace le plus proche du milieu,
        // en interdisant un mot < 3 chars d'un côté ou de l'autre.
        if ($len > 19 && strpos($name, ' ') !== false) {
            $target = $len / 2;
            $best   = null;
            $bestDist = PHP_INT_MAX;
            $offset = 0;
            while (($pos = mb_strpos($name, ' ', $offset)) !== false) {
                $leftLen  = $pos;
                $rightLen = $len - $pos - 1;
                if ($leftLen >= 3 && $rightLen >= 3) {
                    $dist = abs($pos - $target);
                    if ($dist < $bestDist) {
                        $bestDist = $dist;
                        $best     = $pos;
                    }
                }
                $offset = $pos + 1;
            }
            if ($best !== null) {
                return htmlspecialchars(mb_substr($name, 0, $best), ENT_QUOTES, 'UTF-8')
                    . '<br>'
                    . htmlspecialchars(mb_substr($name, $best + 1), ENT_QUOTES, 'UTF-8');
            }
        }
        // 3. Nom court ou non splittable : inchangé
        return htmlspecialchars($name, ENT_QUOTES, 'UTF-8');
    }
}

if (!function_exists('darkenForWhiteText')) {
    /**
     * Darken une couleur hex jusqu'à atteindre AA (4.5:1) avec texte blanc.
     * Si la couleur passe déjà AA, retourne inchangée (no-op).
     * Sinon blend progressif avec noir par paliers de 5%.
     *
     * Utilisé pour les pastilles correspondance (RER A bleu clair #5291CE
     * + texte blanc = 3.33:1 fail) où la couleur source vient des JSON
     * et ne peut pas être darkenée à la source.
     */
    function darkenForWhiteText(string $hex, float $target = 4.5): string {
        $hex = ltrim($hex, '#');
        if (strlen($hex) !== 6) return '#' . $hex;
        // WCAG luminance + contrast helpers (inline pour autonomie)
        $lum = function (string $h): float {
            $rgb = [hexdec(substr($h, 0, 2)), hexdec(substr($h, 2, 2)), hexdec(substr($h, 4, 2))];
            $rgb = array_map(function ($v) {
                $v = $v / 255.0;
                return $v <= 0.03928 ? $v / 12.92 : pow(($v + 0.055) / 1.055, 2.4);
            }, $rgb);
            return 0.2126 * $rgb[0] + 0.7152 * $rgb[1] + 0.0722 * $rgb[2];
        };
        $contrast = function (string $a, string $b) use ($lum): float {
            $la = $lum($a); $lb = $lum($b);
            return ($la > $lb) ? ($la + 0.05) / ($lb + 0.05) : ($lb + 0.05) / ($la + 0.05);
        };
        // Blanc = #FFFFFF. Si contraste >= target, retourne inchangé.
        if ($contrast($hex, 'FFFFFF') >= $target) return '#' . $hex;
        // Sinon blend progressif avec noir
        for ($mix = 0.05; $mix <= 0.95; $mix += 0.05) {
            $r = (int) round(hexdec(substr($hex, 0, 2)) * (1 - $mix));
            $g = (int) round(hexdec(substr($hex, 2, 2)) * (1 - $mix));
            $b = (int) round(hexdec(substr($hex, 4, 2)) * (1 - $mix));
            $candidate = sprintf('%02X%02X%02X', $r, $g, $b);
            if ($contrast($candidate, 'FFFFFF') >= $target) return '#' . $candidate;
        }
        return '#000000';
    }
}

if (!function_exists('transit_pricing')) {
    /**
     * Charge le JSON central des tarifs IDFM (data/global/transit-pricing.json).
     * Source unique de vérité pour les tarifs métro / RER / bus / tram /
     * Transilien sur les pages station + hub /tarifs/.
     *
     * Cache mémoire intra-requête (single read par render).
     * Retourne array vide si fichier manquant ou JSON invalide.
     *
     * @return array
     */
    function transit_pricing(): array {
        static $cache = null;
        if ($cache === null) {
            $path = __DIR__ . '/../data/global/transit-pricing.json';
            if (is_file($path)) {
                $parsed = json_decode((string) file_get_contents($path), true);
                $cache = is_array($parsed) ? $parsed : [];
            } else {
                $cache = [];
            }
        }
        return $cache;
    }
}

if (!function_exists('format_price')) {
    /**
     * Formate un prix en euros au format FR : « 17,35 € » ou « Gratuit ».
     *
     * @param float|int|null $price
     * @param bool           $showFree Afficher « Gratuit » si 0, sinon « 0,00 € »
     * @return string
     */
    function format_price($price, bool $showFree = true): string {
        if ($price === null) return '';
        $f = (float) $price;
        if ($showFree && $f === 0.0) return 'Gratuit';
        return number_format($f, 2, ',', "\u{202F}") . "\u{202F}€";
    }
}

if (!function_exists('buildStationTitle')) {
    /**
     * Construit le <title> SEO d'une page station.
     *
     * Pattern : "{Mode dominant} {Nom} {codes lignes} | BougeaParis.fr"
     *
     * Mode dominant (detecte automatiquement) :
     *   - metro       si lines[] contient au moins 1 entree type=metro
     *   - RER         sinon si rer_correspondences[] non vide (RER pur)
     *   - Tramway     sinon si tramway_correspondences[] non vide (tram pur)
     *   - Transilien  sinon si transilien_correspondences[] non vide
     *
     * Codes lignes (ordre fixe metro -> RER -> tram -> Transilien) :
     *   - Metro      : "M1 M4 M7"
     *   - RER        : "RER A B" (le mot RER est omis si mode dominant = RER pur)
     *   - Tram       : "T1 T3a"  (idem)
     *   - Transilien : "L U"     (idem)
     *
     * Cible : 50-60 chars max. Si depassement, troncature des codes en
     * priorite (3 codes + "+ autres"), le nom n'est JAMAIS tronque.
     *
     * L'appelant doit utiliser setTitle($title, false) pour desactiver le
     * suffixe title_suffix global ; la brand est integree ici.
     *
     * @param array $station JSON station decode
     * @return string Title final pret pour setTitle($title, false)
     */
    function buildStationTitle(array $station): string
    {
        $brand = ' | BougeaParis.fr';
        $name  = trim((string)($station['name'] ?? ''));

        // Extraction des codes par mode
        $metro = [];
        foreach (($station['lines'] ?? []) as $line) {
            if (($line['type'] ?? '') === 'metro' && !empty($line['code'])) {
                $metro[] = (string)$line['code'];
            }
        }
        $rer   = array_values(array_filter(array_column($station['rer_correspondences']        ?? [], 'code')));
        $tram  = array_values(array_filter(array_column($station['tramway_correspondences']    ?? [], 'code')));
        $trans = array_values(array_filter(array_column($station['transilien_correspondences'] ?? [], 'code')));

        // Detection du mode dominant + prefixe
        if ($metro) {
            $modePrefix = 'Métro';
        } elseif ($rer) {
            $modePrefix = 'RER';
        } elseif ($tram) {
            $modePrefix = 'Tramway';
        } elseif ($trans) {
            $modePrefix = 'Transilien';
        } else {
            $modePrefix = '';
        }

        // Compactage des codes selon le mode dominant
        // - Si mode dominant = metro : nom au milieu, codes apres
        //   ex : "Métro Saint-Michel M4 RER B C"
        // - Si mode dominant = RER/Tram/Transilien pur : codes immediatement apres
        //   le mode prefixe, nom apres ; ex : "RER C Champ de Mars - Tour Eiffel"
        $compactMetroCodes = static fn(array $m): string => implode(' ', array_map(static fn($c) => 'M' . $c, $m));
        $compactRerCodes   = static fn(array $r): string => 'RER ' . implode(' ', $r);
        $compactTramCodes  = static fn(array $t): string => implode(' ', array_map(static fn($c) => 'T' . $c, $t));
        $compactTransCodes = static fn(array $tr): string => implode(' ', $tr);

        // Joiner conversationnel "A", "A et B", "A, B et C" pour le format long.
        $joinLong = static function (array $codes): string {
            $n = count($codes);
            if ($n === 0) { return ''; }
            if ($n === 1) { return $codes[0]; }
            if ($n === 2) { return $codes[0] . ' et ' . $codes[1]; }
            $last = array_pop($codes);
            return implode(', ', $codes) . ' et ' . $last;
        };

        // Signal geo Paris injecte juste apres le nom (avant les codes) en mode
        // Metro/Tram/Transilien ; en RER pur les codes sont devant le nom donc
        // " Paris" arrive en fin avant la brand.
        $nameWithGeo = $name . ' à Paris';

        // Budget pour le title (hors brand).
        $brandLen = mb_strlen($brand, 'UTF-8');
        $maxLen   = 60 - $brandLen;

        if ($modePrefix === 'Métro') {
            // Tentative 1 : format long "(ligne 6)" / "(lignes 6 et 9)" /
            // "(lignes 8, 12 et 14)" / mixte "(lignes 4 + RER B et C)".
            $longParts = [];
            if ($metro) {
                $verb = count($metro) === 1 ? 'ligne ' : 'lignes ';
                $longParts[] = $verb . $joinLong($metro);
            }
            if ($rer) {
                $longParts[] = 'RER ' . $joinLong($rer);
            }
            if ($tram) {
                $longParts[] = (count($tram) === 1 ? 'tram T' : 'trams T') . $joinLong($tram);
            }
            if ($trans) {
                $longParts[] = 'Transilien ' . $joinLong($trans);
            }
            $longCodes = $longParts ? '(' . implode(' + ', $longParts) . ')' : '';
            $longTitle = trim($modePrefix . ' ' . $nameWithGeo . ($longCodes !== '' ? ' ' . $longCodes : ''));

            if (mb_strlen($longTitle, 'UTF-8') <= $maxLen) {
                $title = $longTitle;
            } else {
                // Tentative 2 : fallback compact "M1 M2 RER A B".
                $tail = [];
                if ($metro) { $tail[] = $compactMetroCodes($metro); }
                if ($rer)   { $tail[] = $compactRerCodes($rer); }
                if ($tram)  { $tail[] = $compactTramCodes($tram); }
                if ($trans) { $tail[] = $compactTransCodes($trans); }
                $codesAfterName = trim(implode(' ', $tail));
                $title = trim($modePrefix . ' ' . $nameWithGeo . ($codesAfterName !== '' ? ' ' . $codesAfterName : ''));
            }
        } elseif ($modePrefix === 'RER') {
            // RER pur : "RER {codes} {nom} à Paris" (inchange, format compact assume)
            $codes = implode(' ', $rer);
            $title = trim($modePrefix . ' ' . $codes . ' ' . $nameWithGeo);
        } elseif ($modePrefix === 'Tramway') {
            // Tram pur : tentative long "(T2 et 3a)" puis fallback compact.
            $longLabel = count($tram) === 1 ? 'T' . $tram[0] : 'T' . $joinLong($tram);
            $longTitle = trim($modePrefix . ' ' . $nameWithGeo . ' (' . $longLabel . ')');
            if (mb_strlen($longTitle, 'UTF-8') <= $maxLen) {
                $title = $longTitle;
            } else {
                $codes = $compactTramCodes($tram);
                $title = trim($modePrefix . ' ' . $nameWithGeo . ($codes !== '' ? ' ' . $codes : ''));
            }
        } elseif ($modePrefix === 'Transilien') {
            // Transilien pur : "Transilien {nom} à Paris ({codes})"
            $longLabel = $joinLong($trans);
            $longTitle = trim($modePrefix . ' ' . $nameWithGeo . ' (' . $longLabel . ')');
            if (mb_strlen($longTitle, 'UTF-8') <= $maxLen) {
                $title = $longTitle;
            } else {
                $codes = $compactTransCodes($trans);
                $title = trim($modePrefix . ' ' . $nameWithGeo . ($codes !== '' ? ' ' . $codes : ''));
            }
        } else {
            $title = $name;
        }

        // Si depassement strict (> 60 - brand_len) ET compact full > 70 - brand,
        // troncature progressive des codes. Sinon, on accepte un overflow doux
        // (jusqu'a ~70 chars total) pour preserver tous les codes — cas des
        // stations a nom long avec 4+ lignes (Montparnasse, Saint-Michel mixte).
        // Google clippe visuellement au-dela de 60 mais indexe le title complet.
        $softCap = 70 - $brandLen;
        if (mb_strlen($title, 'UTF-8') > $softCap) {
            $all = array_merge(
                array_map(static fn($c) => 'M' . $c, $metro),
                $rer ? ['RER ' . implode(' ', $rer)] : [],
                array_map(static fn($c) => 'T' . $c, $tram),
                $trans
            );
            $total = count($all);
            $best  = '';
            for ($limit = $total; $limit >= 0; $limit--) {
                $kept = array_slice($all, 0, $limit);
                $tail = $limit > 0 ? implode(' ', $kept) : '';

                if ($modePrefix === 'RER') {
                    $rerKept = array_slice($rer, 0, $limit);
                    $tail    = $limit > 0 ? implode(' ', $rerKept) : '';
                    $candidate = trim($modePrefix . ($tail !== '' ? ' ' . $tail : '') . ' ' . $nameWithGeo);
                } else {
                    $candidate = trim(($modePrefix !== '' ? $modePrefix . ' ' : '') . $nameWithGeo . ($tail !== '' ? ' ' . $tail : ''));
                }
                $best = $candidate;
                if (mb_strlen($candidate, 'UTF-8') <= $softCap) {
                    break;
                }
            }
            $title = $best;
        }

        return $title . $brand;
    }
}

if (!function_exists('buildStationH1')) {
    /**
     * Construit le H1 d'une page station, format long et SEO :
     *
     *   "Station de {type} {Nom} ({Codes})"
     *
     * Patterns par mode dominant :
     *   - Metro pur       : "Station de métro {Nom} (Métro {liste})"
     *   - Mixte M + RER   : "Station de métro {Nom} (Métro {liste} + RER {liste})"
     *   - RER pur         : "Station de RER {Nom} (RER {liste})"
     *   - Tram pur        : "Station de tramway {Nom} (Tram {liste})"
     *   - Transilien pur  : "Station de Transilien {Nom} (Transilien {liste})"
     *
     * Format codes (LONG, pas compact) :
     *   - "Métro 6"            (pas "M6")
     *   - "RER C", "RER B et C"
     *   - "Tram 2", "Tram 2 et 3a"
     *
     * Séparateurs de listes :
     *   - 1 code   : "X"
     *   - 2 codes  : "X et Y"
     *   - 3+ codes : "X, Y et Z"
     *
     * Mirror de buildStationTitle() pour la cohérence de détection du mode
     * dominant. La rendition est en texte brut (pas de HTML) ; l'appelant
     * doit echo dans un contexte sécurisé (le H1 est statique côté code).
     *
     * @param array $station JSON station decode
     * @return string H1 final (texte brut, ex: "Station de métro Cité (Métro 4)")
     */
    function buildStationH1(array $station): string
    {
        $name = trim((string)($station['name'] ?? ''));

        // Extraction des codes par mode (memes regles que buildStationTitle)
        $metro = [];
        foreach (($station['lines'] ?? []) as $line) {
            if (($line['type'] ?? '') === 'metro' && !empty($line['code'])) {
                $metro[] = (string)$line['code'];
            }
        }
        $rer   = array_values(array_filter(array_column($station['rer_correspondences']        ?? [], 'code')));
        $tram  = array_values(array_filter(array_column($station['tramway_correspondences']    ?? [], 'code')));
        $trans = array_values(array_filter(array_column($station['transilien_correspondences'] ?? [], 'code')));

        // Joiner conversationnel : "A", "A et B", "A, B et C"
        $joinCodes = static function (array $codes): string {
            $n = count($codes);
            if ($n === 0) { return ''; }
            if ($n === 1) { return $codes[0]; }
            if ($n === 2) { return $codes[0] . ' et ' . $codes[1]; }
            $last = array_pop($codes);
            return implode(', ', $codes) . ' et ' . $last;
        };

        $metroPart = $metro ? ('Métro ' . $joinCodes($metro)) : '';
        $rerPart   = $rer   ? ('RER '   . $joinCodes($rer))   : '';
        $tramPart  = $tram  ? ('Tram '  . $joinCodes($tram))  : '';
        $transPart = $trans ? ('Transilien ' . $joinCodes($trans)) : '';

        // Detection du mode dominant + prefixe d'introduction
        if ($metro) {
            // CAS 1 ou 2 : metro pur ou metro + correspondances
            $modeIntro = 'Station de métro';
            $codesParts = array_filter([$metroPart, $rerPart, $tramPart, $transPart], static fn($s) => $s !== '');
            $codes = implode(' + ', $codesParts);
        } elseif ($rer) {
            // CAS 3 : RER pur
            $modeIntro = 'Station de RER';
            $codes = $rerPart;
        } elseif ($tram) {
            // CAS 4 : Tram pur
            $modeIntro = 'Station de tramway';
            $codes = $tramPart;
        } elseif ($trans) {
            // CAS 5 : Transilien pur
            $modeIntro = 'Station de Transilien';
            $codes = $transPart;
        } else {
            return 'Station ' . $name . ' à Paris';
        }

        // Signal geo Paris injecte apres le nom, avant les parentheses de codes.
        return $modeIntro . ' ' . $name . ' à Paris (' . $codes . ')';
    }
}

if (!function_exists('detectStationMode')) {
    /**
     * Detecte le mode dominant d'une station pour les helpers de titres.
     *
     * Retourne un des 4 modes (mirror logic des buildStation*) :
     *   - 'metro_pur'  : lines[] metro present ET pas de correspondance RER/tram
     *   - 'mixte'      : lines[] metro present ET au moins une correspondance RER/tram
     *   - 'rer_pur'    : pas de metro, rer_correspondences[] non vide
     *   - 'tram_pur'   : pas de metro/RER, tramway_correspondences[] non vide
     *
     * Fallback (cas inattendu) : 'metro_pur'.
     */
    function detectStationMode(array $station): string
    {
        $hasMetro = false;
        foreach (($station['lines'] ?? []) as $line) {
            if (($line['type'] ?? '') === 'metro') {
                $hasMetro = true;
                break;
            }
        }
        $hasRer  = !empty($station['rer_correspondences']);
        $hasTram = !empty($station['tramway_correspondences']);

        if ($hasMetro && ($hasRer || $hasTram)) { return 'mixte'; }
        if ($hasMetro) { return 'metro_pur'; }
        if ($hasRer)   { return 'rer_pur'; }
        if ($hasTram)  { return 'tram_pur'; }
        return 'metro_pur';
    }
}

if (!function_exists('buildSectionTitleHoraires')) {
    /** Titre H2 section Horaires, adaptatif au mode. */
    function buildSectionTitleHoraires(array $station): string
    {
        $name = trim((string)($station['name'] ?? ''));
        switch (detectStationMode($station)) {
            case 'mixte':    return "Horaires des lignes de métro et RER à $name";
            case 'rer_pur':  return "Horaires des lignes de RER à $name";
            case 'tram_pur': return "Horaires des lignes de tramway à $name";
            case 'metro_pur':
            default:         return "Horaires des lignes de métro à $name";
        }
    }
}

if (!function_exists('buildSectionTitleAdjacent')) {
    /** Titre H2 section Stations adjacentes, adaptatif au mode. */
    function buildSectionTitleAdjacent(array $station): string
    {
        $name = trim((string)($station['name'] ?? ''));
        switch (detectStationMode($station)) {
            case 'mixte':    return "Stations adjacentes à $name à Paris";
            case 'rer_pur':  return "Stations adjacentes au RER $name à Paris";
            case 'tram_pur': return "Stations adjacentes au tramway $name à Paris";
            case 'metro_pur':
            default:         return "Stations adjacentes au métro $name à Paris";
        }
    }
}

if (!function_exists('buildSectionTitleSorties')) {
    /** Titre H2 section Sorties, adaptatif au mode. */
    function buildSectionTitleSorties(array $station): string
    {
        $name = trim((string)($station['name'] ?? ''));
        switch (detectStationMode($station)) {
            case 'mixte':    return "Sorties de la station $name";
            case 'rer_pur':  return "Sorties de la station de RER $name";
            case 'tram_pur': return "Sorties de la station de tramway $name";
            case 'metro_pur':
            default:         return "Sorties de la station de métro $name";
        }
    }
}

if (!function_exists('buildSectionTitleItineraires')) {
    /** Titre H2 section Itinéraires populaires, adaptatif au mode. */
    function buildSectionTitleItineraires(array $station): string
    {
        $name = trim((string)($station['name'] ?? ''));
        switch (detectStationMode($station)) {
            case 'mixte':    return "Itinéraires populaires depuis $name à Paris";
            case 'rer_pur':  return "Itinéraires populaires depuis le RER $name à Paris";
            case 'tram_pur': return "Itinéraires populaires depuis le tramway $name à Paris";
            case 'metro_pur':
            default:         return "Itinéraires populaires depuis le métro $name à Paris";
        }
    }
}

if (!function_exists('extractStationCodesLong')) {
    /**
     * Renvoie les codes par mode + un joiner conversationnel "A", "A et B",
     * "A, B et C". Utilise par les helpers meta description / keywords.
     */
    function extractStationCodesLong(array $station): array
    {
        $metro = [];
        foreach (($station['lines'] ?? []) as $line) {
            if (($line['type'] ?? '') === 'metro' && !empty($line['code'])) {
                $metro[] = (string)$line['code'];
            }
        }
        $rer   = array_values(array_filter(array_column($station['rer_correspondences']     ?? [], 'code')));
        $tram  = array_values(array_filter(array_column($station['tramway_correspondences'] ?? [], 'code')));

        $join = static function (array $codes): string {
            $n = count($codes);
            if ($n === 0) { return ''; }
            if ($n === 1) { return $codes[0]; }
            if ($n === 2) { return $codes[0] . ' et ' . $codes[1]; }
            $last = array_pop($codes);
            return implode(', ', $codes) . ' et ' . $last;
        };

        return [
            'metro'      => $metro,
            'rer'        => $rer,
            'tram'       => $tram,
            'metroJoined'=> $join($metro),
            'rerJoined'  => $join($rer),
            'tramJoined' => $join($tram),
        ];
    }
}

if (!function_exists('extractStationArr')) {
    /**
     * Extrait le numero d'arrondissement Paris depuis un format "5e (Paris)"
     * ou "5e / 6e (Paris)" (premier numero retenu). Retourne null si vide
     * ou non-Parisien.
     */
    function extractStationArr(array $station): ?string
    {
        $raw = trim((string)($station['arrondissement'] ?? ''));
        if ($raw === '') { return null; }
        if (preg_match('/^(\d{1,2})(?:er|e)\b/u', $raw, $m)) {
            return $m[1] . (($m[1] === '1') ? 'er' : 'e');
        }
        return null;
    }
}

if (!function_exists('buildStationMetaDescription')) {
    /**
     * Meta description SEO (<=160 chars) adaptative au mode dominant :
     *
     *   "Station de métro {Nom} à Paris (Métro {codes}) — Xe arr. :
     *    sorties, horaires, plan, accès POI1, POI2, POI3."
     *
     * Variantes mixte / RER pur ("Gare RER ...") / tram pur.
     * Tronque les POIs si depassement, puis le segment arrondissement,
     * jamais le nom ni les codes.
     */
    function buildStationMetaDescription(array $station): string
    {
        $name  = trim((string)($station['name'] ?? ''));
        $codes = extractStationCodesLong($station);
        $arr   = extractStationArr($station);
        $mode  = detectStationMode($station);

        $arrSegment = $arr ? " — {$arr} arr." : '';

        switch ($mode) {
            case 'mixte':
                $intro = "Station de métro $name à Paris (Métro {$codes['metroJoined']} + RER {$codes['rerJoined']})";
                break;
            case 'rer_pur':
                $intro = "Gare RER {$codes['rerJoined']} $name à Paris";
                break;
            case 'tram_pur':
                $intro = "Station de tramway $name à Paris (Tram {$codes['tramJoined']})";
                break;
            case 'metro_pur':
            default:
                $intro = "Station de métro $name à Paris (Métro {$codes['metroJoined']})";
                break;
        }

        $pois = array_values(array_filter(array_map(static function ($p) {
            $n = trim((string)($p['name'] ?? ''));
            return $n !== '' ? mb_convert_case(mb_substr($n, 0, 1, 'UTF-8'), MB_CASE_UPPER, 'UTF-8') . mb_substr($n, 1, null, 'UTF-8') : '';
        }, $station['nearby_pois'] ?? [])));
        $top3 = array_slice($pois, 0, 3);

        $tailBase = ' : sorties, horaires, plan';
        $accessLabel = $top3 ? ', accès ' . implode(', ', $top3) . '.' : '.';

        $candidate = $intro . $arrSegment . $tailBase . $accessLabel;
        if (mb_strlen($candidate, 'UTF-8') <= 160) { return $candidate; }

        // Troncature 1 : reduire les POIs (3 → 2 → 1 → 0)
        for ($k = 2; $k >= 0; $k--) {
            $kept = array_slice($pois, 0, $k);
            $accessLabel = $kept ? ', accès ' . implode(', ', $kept) . '.' : '.';
            $candidate = $intro . $arrSegment . $tailBase . $accessLabel;
            if (mb_strlen($candidate, 'UTF-8') <= 160) { return $candidate; }
        }
        // Troncature 2 : retirer le segment arrondissement
        $candidate = $intro . $tailBase . '.';
        if (mb_strlen($candidate, 'UTF-8') <= 160) { return $candidate; }
        // Troncature 3 : intro seul + point
        return mb_substr($intro . '.', 0, 160, 'UTF-8');
    }
}

if (!function_exists('buildStationMetaKeywords')) {
    /**
     * Meta keywords adaptative au mode. Pattern :
     *   - Metro pur : "métro {Nom}, station de métro {Nom}, Métro X {Nom} Paris, …"
     *   - Mixte     : ajoute "RER X {Nom} Paris" pour chaque ligne RER
     *   - RER pur   : "RER {Nom}, gare RER {Nom}, RER X {Nom} Paris"
     *   - Tram pur  : "tramway {Nom}, station de tramway {Nom}, Tram X {Nom} Paris"
     *
     * Note : Google ignore meta keywords depuis 2009, mais conservee pour les
     * autres crawlers et heritage SEO (Bing, Yandex, DuckDuckGo).
     */
    function buildStationMetaKeywords(array $station): string
    {
        $name  = trim((string)($station['name'] ?? ''));
        $codes = extractStationCodesLong($station);
        $mode  = detectStationMode($station);

        $kw = [];
        switch ($mode) {
            case 'rer_pur':
                $kw[] = "RER $name";
                $kw[] = "gare RER $name";
                foreach ($codes['rer'] as $c) { $kw[] = "RER $c $name Paris"; }
                break;
            case 'tram_pur':
                $kw[] = "tramway $name";
                $kw[] = "station de tramway $name";
                foreach ($codes['tram'] as $c) { $kw[] = "Tram $c $name Paris"; }
                break;
            case 'mixte':
                $kw[] = "métro $name";
                $kw[] = "station de métro $name";
                foreach ($codes['metro'] as $c) { $kw[] = "Métro $c $name Paris"; }
                foreach ($codes['rer'] as $c)   { $kw[] = "RER $c $name Paris"; }
                break;
            case 'metro_pur':
            default:
                $kw[] = "métro $name";
                $kw[] = "station de métro $name";
                foreach ($codes['metro'] as $c) { $kw[] = "Métro $c $name Paris"; }
                break;
        }
        return implode(', ', $kw);
    }
}
