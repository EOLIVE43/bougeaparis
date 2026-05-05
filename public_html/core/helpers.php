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
