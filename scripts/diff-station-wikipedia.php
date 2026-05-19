<?php
declare(strict_types=1);

/**
 * scripts/diff-station-wikipedia.php
 *
 * Quality gate factuel pour les pages station métro. Compare les signaux
 * factuels atomiques extraits du contenu éditorial JSON (dates, noms propres,
 * mesures, durées, capacités) contre le contenu Wikipedia FR des POIs cités
 * et des entités thématiques fréquentes. Détecte les anomalies évidentes
 * (date contradite, nom inventé) SANS censurer les paraphrases légitimes.
 *
 * Usage :
 *   php diff-station-wikipedia.php --slug=bastille
 *   php diff-station-wikipedia.php --slug=bastille --json
 *   php diff-station-wikipedia.php --slug=bastille --verbose
 *   php diff-station-wikipedia.php --slug=bastille --no-cache
 *   php diff-station-wikipedia.php --slug=bastille --cache-ttl=24
 *
 * Exit codes : 0=pass (≥90), 1=warning (70-89), 2=fail (<70), 3=erreur CLI/IO.
 *
 * Sources : fr.wikipedia.org/api/rest_v1/page/{summary|html}/{title}
 * Cache : scripts/cache-wikipedia/{sha1(title)}.json, TTL configurable.
 *
 * V1 — limites assumées : pas de NLP, juste regex + heuristiques contextuelles
 * sur ~15 triggers déclencheurs (prise, inauguré, conçu, etc.) pour la détection
 * CONTRADICTED. Multilingue non couvert (fr.wikipedia.org uniquement).
 */

// ─────────────────────────────────────────────────────────────
// CLI parsing
// ─────────────────────────────────────────────────────────────

$opts = ['slug' => '', 'json' => false, 'verbose' => false, 'no_cache' => false, 'cache_ttl_hours' => 1];
foreach (array_slice($argv, 1) as $arg) {
    if (preg_match('/^--slug=(.+)$/', $arg, $m)) $opts['slug'] = $m[1];
    elseif ($arg === '--json') $opts['json'] = true;
    elseif ($arg === '--verbose') $opts['verbose'] = true;
    elseif ($arg === '--no-cache') $opts['no_cache'] = true;
    elseif (preg_match('/^--cache-ttl=(\d+)$/', $arg, $m)) $opts['cache_ttl_hours'] = (int)$m[1];
    else { fwrite(STDERR, "Argument inconnu : $arg\n"); exit(3); }
}
if ($opts['slug'] === '') {
    fwrite(STDERR, "Usage: php diff-station-wikipedia.php --slug=<slug> [--json] [--verbose] [--no-cache] [--cache-ttl=<hours>]\n");
    exit(3);
}

// ─────────────────────────────────────────────────────────────
// Charger le JSON station
// ─────────────────────────────────────────────────────────────

$jsonPath = __DIR__ . '/../public_html/data/stations/' . $opts['slug'] . '.json';
if (!file_exists($jsonPath)) { fwrite(STDERR, "Erreur : $jsonPath introuvable\n"); exit(3); }
$station = json_decode((string)file_get_contents($jsonPath), true);
if (!is_array($station)) { fwrite(STDERR, "Erreur : JSON invalide dans $jsonPath\n"); exit(3); }

// ─────────────────────────────────────────────────────────────
// Étape 1 : Collecter le texte éditorial à analyser
// ─────────────────────────────────────────────────────────────

function collectEditorialText(array $station): array
{
    // Le quality gate Wikipedia cible les sections PATRIMONIALES/FACTUELLES
    // (history, intro_paragraphs, trivia) où les faits historiques précis se
    // trouvent. On exclut volontairement faq et practical_tips qui contiennent
    // de l'information service voyageur (durées de trajet, distances de marche,
    // conseils pratiques) — données spécifiques à notre contenu, non
    // vérifiables contre Wikipedia, source de faux positifs en cascade.
    $blocks = [];

    if (!empty($station['history']['title']))
        $blocks[] = ['text' => $station['history']['title'], 'context' => 'history.title'];
    foreach ($station['history']['paragraphs'] ?? [] as $i => $p)
        $blocks[] = ['text' => $p, 'context' => 'history §' . ($i + 1)];

    foreach ($station['intro_paragraphs'] ?? [] as $i => $p)
        $blocks[] = ['text' => $p, 'context' => 'intro §' . ($i + 1)];

    foreach ($station['trivia'] ?? [] as $i => $t) {
        if (!empty($t['title']))
            $blocks[] = ['text' => $t['title'], 'context' => 'trivia ' . ($i + 1) . ' title'];
        if (!empty($t['content']))
            $blocks[] = ['text' => $t['content'], 'context' => 'trivia ' . ($i + 1) . ' content'];
    }

    // hero.description (1 paragraphe identitaire patrimonial)
    if (!empty($station['hero']['description']))
        $blocks[] = ['text' => $station['hero']['description'], 'context' => 'hero.description'];

    // Strip HTML tags (<strong>, <em>) pour analyser le texte brut
    foreach ($blocks as &$b) $b['text'] = strip_tags($b['text']);
    return $blocks;
}

// ─────────────────────────────────────────────────────────────
// Étape 2 : Extraire les signaux factuels atomiques
// ─────────────────────────────────────────────────────────────

const MONTHS_FR = 'janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre';

// Stopwords noms propres (à ne PAS extraire comme signal — trop génériques)
const NAME_STOPWORDS = [
    'Paris','France','Métro','RATP','Ligne','Lignes','RER','M1','M2','M3','M4','M5','M6','M7','M8','M9','M10','M11','M12','M13','M14',
    'Wikipedia','Wikidata','Wikimedia','UNESCO','Île-de-France','Île','Seine',
    'Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre',
    'Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche',
    'Nord','Sud','Est','Ouest','Saint','Sainte','Place','Rue','Avenue','Boulevard','Quai','Pont','Hôtel',
    'Premier','Première','Deuxième','Troisième',
    'Bastille','Châtelet','Concorde','Tuileries','Étoile','Louvre','Marais','Vincennes','Arsenal','Beaumarchais',
    'Pas','Sortie','Sorties','Direction','Vers','Aux','Les','Des','Une','Cette','Cet',
    'Note','Voir','Comptez','Empruntez','Privilégiez',
    'Charles','Louis','Napoléon','Roi',
    // Termes communs capitalisés en début de phrase
    'Cependant','Toutefois','Aujourd','Hier','Demain',
];

// Triggers contextuels pour détection CONTRADICTED des années / dates.
// V1 : liste resserrée sur les triggers PEU AMBIGUS pour minimiser les
// faux positifs. Triggers trop génériques (ouvert/ouverte sans contexte,
// fondation, né/mort) écartés car ils matchent trop de contextes sémantiques
// différents dans le wiki et créent des faux contradicted.
// À enrichir en V2 avec détection contextuelle plus fine (NLP).
const YEAR_TRIGGERS = [
    'prise de','prise',
    'inauguré','inaugurée','inaugurés','inaugurées','inauguration',
    'mise en service',
    'édifié','édifiée','édifiés','édifiées','édification',
    'démoli','démolie','démolis','démolies','démolition',
    'détruit','détruite','détruits','détruites','destruction',
    'achevé','achevée','achevés','achevées','achèvement',
];

// Triggers pour noms propres (architecte, sculpteur, etc.)
const NAME_TRIGGERS = [
    'conçu par','conçue par','architecte','sculpteur','dessiné par','dessinée par',
    'œuvre de','réalisé par','réalisée par',
];

function extractSignals(array $blocks): array
{
    $signals = [];
    foreach ($blocks as $block) {
        $text = $block['text'];
        $ctx  = $block['context'];

        // 1. Dates complètes (jour mois année)
        if (preg_match_all('/\b(\d{1,2})\s+(' . MONTHS_FR . ')\s+(\d{4})\b/iu', $text, $matches, PREG_SET_ORDER)) {
            foreach ($matches as $m) {
                $signals[] = [
                    'type' => 'date_full',
                    'value' => $m[1] . ' ' . strtolower($m[2]) . ' ' . $m[3],
                    'year' => (int)$m[3],
                    'context' => $ctx,
                    'snippet' => extractSnippet($text, $m[0]),
                ];
            }
        }

        // 2. Années solo (4 chiffres, 1100-2030). On extrait CHAQUE occurrence
        // indépendamment, y compris celles déjà capturées dans une date complète.
        // Doublons assumés : si "14 juillet 1789" est extracté comme date_full,
        // "1789" sera aussi extracté comme year solo dans le même paragraphe.
        // Le scoring traite chaque signal indépendamment, donc on a 2 checks
        // au lieu d'un — c'est bénin pour le score et bon pour la robustesse
        // de détection CONTRADICTED (chaque occurrence a son propre snippet).
        if (preg_match_all('/\b(1[1-9]\d{2}|20[0-2]\d)\b/u', $text, $matches, PREG_OFFSET_CAPTURE)) {
            foreach ($matches[1] as $m) {
                $year = (int)$m[0];
                $pos = $m[1];
                // Snippet précis : ±60 chars autour de CETTE occurrence (offset connu)
                $start = max(0, $pos - 60);
                $snippet = mb_substr($text, $start, 4 + 2 * 60);
                $signals[] = [
                    'type' => 'year',
                    'value' => $year,
                    'context' => $ctx,
                    'snippet' => trim(preg_replace('/\s+/u', ' ', $snippet)),
                ];
            }
        }

        // 3. Noms propres (séquences de mots capitalisés, hors stopwords)
        if (preg_match_all('/\b([A-ZÀ-Ý][a-zà-ÿ\-]{2,}(?:[\s\-][A-ZÀ-Ý][a-zà-ÿ\-]+)+)\b/u', $text, $matches)) {
            foreach (array_unique($matches[1]) as $name) {
                $first = preg_split('/[\s\-]/u', $name)[0];
                if (in_array($first, NAME_STOPWORDS, true)) continue;
                // Skip si le nom contient un mot stopword unique
                $tokens = preg_split('/[\s\-]/u', $name);
                $stop = false;
                foreach ($tokens as $t) if (in_array($t, NAME_STOPWORDS, true)) { $stop = true; break; }
                if ($stop) continue;
                $signals[] = [
                    'type' => 'name',
                    'value' => $name,
                    'context' => $ctx,
                    'snippet' => extractSnippet($text, $name),
                ];
            }
        }

        // 4. Nombres + unité (mesure, durée, capacité)
        $unitPatterns = [
            'measure_physical' => '/\b(\d+(?:[,.]\d+)?)\s*(m\b|km\b|mètres|kilomètres|tonnes|hectares|ha\b)/u',
            'duration_min'     => '/\b(\d+(?:[,.]\d+)?)\s*(min\b|minute|minutes|h\b|heure|heures)/u',
            'capacity'         => '/\b(\d+(?:[,.]\d+)?)\s*(places|anneaux|noms|spectateurs|voyageurs|stations|sorties|articles|combattants)/u',
        ];
        foreach ($unitPatterns as $type => $pattern) {
            if (preg_match_all($pattern, $text, $matches, PREG_SET_ORDER)) {
                foreach ($matches as $m) {
                    $val = (float)str_replace(',', '.', $m[1]);
                    $signals[] = [
                        'type' => $type,
                        'value' => $val,
                        'unit' => trim($m[2]),
                        'context' => $ctx,
                        'snippet' => extractSnippet($text, $m[0]),
                    ];
                }
            }
        }
    }
    return $signals;
}

function extractSnippet(string $text, string $needle, int $window = 60): string
{
    $pos = mb_stripos($text, $needle);
    if ($pos === false) return '';
    $start = max(0, $pos - $window);
    $len = mb_strlen($needle) + 2 * $window;
    $snippet = mb_substr($text, $start, $len);
    return trim(preg_replace('/\s+/u', ' ', $snippet));
}

// ─────────────────────────────────────────────────────────────
// Étape 3 : Identifier les pages Wikipedia cibles
// ─────────────────────────────────────────────────────────────

function identifyWikiTargets(array $station, array $blocks): array
{
    $targets = [];

    // 3a. POIs déclarés (wikipedia_url)
    foreach ($station['nearby_pois'] ?? [] as $poi) {
        if (!empty($poi['wikipedia_url'])) {
            $title = extractWikiTitle($poi['wikipedia_url']);
            if ($title) $targets[$title] = ['source' => 'poi', 'name' => $poi['name'] ?? $title];
        }
    }

    // 3b. Entités thématiques : noms propres fréquents (≥2 occurrences) hors stopwords
    $allText = implode(' ', array_column($blocks, 'text'));
    $allText = strip_tags($allText);
    $freq = [];
    if (preg_match_all('/\b([A-ZÀ-Ý][a-zà-ÿ\-]{2,}(?:[\s\-][A-ZÀ-Ý][a-zà-ÿ\-]+)+)\b/u', $allText, $matches)) {
        foreach ($matches[1] as $name) {
            $first = preg_split('/[\s\-]/u', $name)[0];
            if (in_array($first, NAME_STOPWORDS, true)) continue;
            $tokens = preg_split('/[\s\-]/u', $name);
            $stop = false;
            foreach ($tokens as $t) if (in_array($t, NAME_STOPWORDS, true)) { $stop = true; break; }
            if ($stop) continue;
            $freq[$name] = ($freq[$name] ?? 0) + 1;
        }
    }
    foreach ($freq as $name => $count) {
        if ($count >= 2 && !isset($targets[str_replace(' ', '_', $name)])) {
            $targets[str_replace(' ', '_', $name)] = ['source' => 'thematic', 'name' => $name, 'occurrences' => $count];
        }
    }

    return $targets;
}

function extractWikiTitle(string $url): ?string
{
    if (preg_match('~fr\.wikipedia\.org/wiki/(.+)$~', $url, $m)) {
        return urldecode($m[1]);
    }
    return null;
}

// ─────────────────────────────────────────────────────────────
// Étape 4 : Fetcher les contenus Wikipedia avec cache
// ─────────────────────────────────────────────────────────────

function fetchWikiContents(array $targets, array $opts): array
{
    $cacheDir = __DIR__ . '/cache-wikipedia';
    if (!is_dir($cacheDir)) @mkdir($cacheDir, 0755, true);

    $contents = [];
    $ttl = $opts['cache_ttl_hours'] * 3600;

    foreach ($targets as $title => $meta) {
        $key = sha1($title);
        $cachePath = $cacheDir . '/' . $key . '.json';

        if (!$opts['no_cache'] && file_exists($cachePath) && (time() - filemtime($cachePath)) < $ttl) {
            $cached = json_decode((string)file_get_contents($cachePath), true);
            if (is_array($cached)) {
                $contents[$title] = array_merge($cached, ['cached' => true, 'meta' => $meta]);
                continue;
            }
        }

        // Fetch summary + HTML complet pour maximiser la couverture des signaux
        // Le résumé seul (3-5 paragraphes) est trop court par rapport à notre
        // contenu éditorial (1500+ mots). On concatène summary + body HTML
        // stripé pour avoir une base de comparaison plus riche.
        $encodedTitle = rawurlencode(str_replace(' ', '_', $title));
        $textParts = [];
        $httpCode = 0;

        foreach (['summary', 'html'] as $endpoint) {
            $url = 'https://fr.wikipedia.org/api/rest_v1/page/' . $endpoint . '/' . $encodedTitle;
            $ch = curl_init($url);
            curl_setopt_array($ch, [
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_TIMEOUT => 15,
                CURLOPT_HTTPHEADER => ['User-Agent: BougeaParis-QualityGate/1.0 (https://bougeaparis.fr; ludovic@eoliz.fr)'],
            ]);
            $body = curl_exec($ch);
            $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            // PHP 8.0+ : curl_close est no-op, $ch GC'd à la sortie de scope

            if ($code === 200 && $body) {
                if ($endpoint === 'summary') {
                    $data = json_decode($body, true);
                    $textParts[] = ($data['extract'] ?? '') . ' ' . ($data['description'] ?? '');
                } else {
                    // HTML complet : strip tags + limit à 30 ko pour rester rapide
                    $stripped = strip_tags($body);
                    $stripped = preg_replace('/\s+/u', ' ', $stripped);
                    $textParts[] = mb_substr($stripped, 0, 30000);
                }
                $httpCode = 200;
            }
        }

        if (!empty($textParts) && $httpCode === 200) {
            $text = implode(' ', $textParts);
            $contents[$title] = ['text' => $text, 'http' => 200, 'meta' => $meta, 'cached' => false];
            file_put_contents($cachePath, json_encode(['text' => $text, 'http' => 200], JSON_UNESCAPED_UNICODE));
        } else {
            $contents[$title] = ['text' => '', 'http' => $httpCode ?: 0, 'meta' => $meta, 'cached' => false, 'error' => "Fetch failed"];
        }
    }
    return $contents;
}

// ─────────────────────────────────────────────────────────────
// Étape 5 : Comparer signaux vs wiki contents
// ─────────────────────────────────────────────────────────────

function normalize(string $s): string
{
    $s = mb_strtolower($s, 'UTF-8');
    $s = strtr($s, [
        'à'=>'a','á'=>'a','â'=>'a','ä'=>'a','ã'=>'a','å'=>'a',
        'è'=>'e','é'=>'e','ê'=>'e','ë'=>'e',
        'ì'=>'i','í'=>'i','î'=>'i','ï'=>'i',
        'ò'=>'o','ó'=>'o','ô'=>'o','ö'=>'o','õ'=>'o',
        'ù'=>'u','ú'=>'u','û'=>'u','ü'=>'u',
        'ç'=>'c','ñ'=>'n',
    ]);
    return preg_replace('/\s+/u', ' ', trim($s));
}

function findTriggerInSnippet(string $snippet, array $triggers): ?string
{
    $n = normalize($snippet);
    foreach ($triggers as $t) {
        if (mb_stripos($n, $t) !== false) return $t;
    }
    return null;
}

function compareSignal(array $sig, array $wikiContents): array
{
    $allWiki = '';
    foreach ($wikiContents as $w) $allWiki .= ' ' . $w['text'];
    $allWikiN = normalize($allWiki);

    switch ($sig['type']) {
        case 'year':
            $needle = (string)$sig['value'];
            // 1. Exact found
            if (mb_stripos($allWikiN, $needle) !== false) {
                return ['status' => 'found', 'penalty' => 0];
            }
            // 2. CONTRADICTED detection via trigger
            $trigger = findTriggerInSnippet($sig['snippet'], YEAR_TRIGGERS);
            if ($trigger) {
                // Cherche une année dans le wiki au voisinage du trigger
                $wikiSays = findYearNearTrigger($trigger, $allWikiN);
                if ($wikiSays !== null && $wikiSays !== (int)$sig['value']) {
                    return [
                        'status' => 'contradicted',
                        'severity' => 'high',
                        'penalty' => -20,
                        'wiki_says' => (string)$wikiSays,
                        'trigger' => $trigger,
                    ];
                }
            }
            return ['status' => 'not_found', 'penalty' => -2];

        case 'date_full':
            $needle = normalize($sig['value']);
            if (mb_stripos($allWikiN, $needle) !== false) return ['status' => 'found', 'penalty' => 0];
            // Tolerance : check si l'année est trouvée (date partielle = signal partiellement validé)
            if (mb_stripos($allWikiN, (string)$sig['year']) !== false) {
                return ['status' => 'partial', 'severity' => 'low', 'penalty' => -2,
                        'note' => 'Date exacte non trouvée mais année ' . $sig['year'] . ' présente dans wiki'];
            }
            // CONTRADICTED detection via trigger : si snippet contient un trigger
            // d'action historique ET si le wiki mentionne une année différente
            // au voisinage de ce trigger → date contradite (severity HIGH).
            $trigger = findTriggerInSnippet($sig['snippet'], YEAR_TRIGGERS);
            if ($trigger) {
                $wikiSays = findYearNearTrigger($trigger, $allWikiN);
                if ($wikiSays !== null && $wikiSays !== (int)$sig['year']) {
                    return [
                        'status' => 'contradicted',
                        'severity' => 'high',
                        'penalty' => -20,
                        'wiki_says' => (string)$wikiSays,
                        'trigger' => $trigger,
                    ];
                }
            }
            return ['status' => 'not_found', 'penalty' => -2];

        case 'name':
            $needle = normalize($sig['value']);
            // Anti-self-référence : exclure le wiki dont le titre matche le nom
            // recherché (cas pathologique : si le JSON contient "Frank Gehry"
            // 2+ fois, identifyWikiTargets fetch sa page wiki, et la simple
            // recherche "Frank Gehry dans le wiki global" trouverait son
            // propre wiki self-fetched → faux FOUND).
            $allWikiNoSelf = '';
            $allWikiNoSelfRaw = '';
            foreach ($wikiContents as $title => $w) {
                $titleN = normalize(str_replace('_', ' ', $title));
                if ($titleN === $needle) continue; // skip self wiki
                $allWikiNoSelf .= ' ' . normalize($w['text']);
                $allWikiNoSelfRaw .= ' ' . $w['text'];
            }
            if (mb_stripos($allWikiNoSelf, $needle) !== false) {
                return ['status' => 'found', 'penalty' => 0];
            }
            // CONTRADICTED detection si trigger nom propre
            $trigger = findTriggerInSnippet($sig['snippet'], NAME_TRIGGERS);
            if ($trigger) {
                $wikiSays = findNameNearTrigger($trigger, $allWikiNoSelfRaw);
                if ($wikiSays !== null && normalize($wikiSays) !== $needle) {
                    return [
                        'status' => 'contradicted',
                        'severity' => 'high',
                        'penalty' => -20,
                        'wiki_says' => $wikiSays,
                        'trigger' => $trigger,
                    ];
                }
            }
            return ['status' => 'not_found', 'penalty' => -2];

        case 'measure_physical':
            return compareNumeric($sig, $wikiContents, 0.05, 'medium', 'low');
        case 'duration_min':
            return compareNumeric($sig, $wikiContents, 0.0, 'medium', 'low', 1);
        case 'capacity':
            $tolerance = ($sig['value'] > 1000) ? 0.10 : 0.05;
            return compareNumeric($sig, $wikiContents, $tolerance, 'medium', 'low');
    }
    return ['status' => 'not_found', 'penalty' => -2];
}

function compareNumeric(array $sig, array $wikiContents, float $relTol, string $sevMid, string $sevLow, int $absTol = 0): array
{
    $unit = $sig['unit'];
    $val = (float)$sig['value'];

    // Cherche tous les nombres avec la même unité (ou unité équivalente) dans le wiki
    $allText = '';
    foreach ($wikiContents as $w) $allText .= ' ' . $w['text'];
    // Normaliser les nombres avec séparateur de milliers français (espace ou
    // espace insécable U+00A0) : "2 745" → "2745" pour matcher notre format JSON.
    $allText = preg_replace('/(\d)[\s\x{00a0}](\d{3})\b/u', '$1$2', $allText);
    // Idem pour décimales avec virgule française : "4,7 km" déjà géré par regex.
    $unitGroup = [$unit];
    // Equivalences d'unités (sémantique commune)
    $aliases = [
        'm' => ['m','mètres'], 'mètres' => ['m','mètres'],
        'km' => ['km','kilomètres'], 'kilomètres' => ['km','kilomètres'],
        'min' => ['min','minute','minutes'], 'minutes' => ['min','minute','minutes'], 'minute' => ['min','minute','minutes'],
        'h' => ['h','heure','heures'], 'heures' => ['h','heure','heures'],
        // Capacités d'accueil : différents termes pour la même réalité
        'places' => ['places','spectateurs','sièges','fauteuils','sieges'],
        'spectateurs' => ['places','spectateurs','sièges','fauteuils','sieges'],
        'sièges' => ['places','spectateurs','sièges','fauteuils','sieges'],
    ];
    if (isset($aliases[$unit])) $unitGroup = $aliases[$unit];

    $unitRe = '(' . implode('|', array_map('preg_quote', $unitGroup)) . ')';
    $pattern = '/\b(\d+(?:[,.]\d+)?)\s*' . $unitRe . '\b/u';

    $found = [];
    if (preg_match_all($pattern, $allText, $matches)) {
        foreach ($matches[1] as $n) $found[] = (float)str_replace(',', '.', $n);
    }

    if (empty($found)) return ['status' => 'not_found', 'penalty' => -2];

    // Cherche la valeur la plus proche
    $closest = null; $minDiff = INF;
    foreach ($found as $f) {
        $diff = abs($f - $val);
        if ($diff < $minDiff) { $minDiff = $diff; $closest = $f; }
    }

    // Tolérance
    $tolerance = max($absTol, $val * $relTol);
    if ($minDiff <= $tolerance) {
        return ['status' => 'found', 'penalty' => 0];
    }
    // Hors tolérance : severity selon écart relatif
    $relDiff = $val > 0 ? abs($val - $closest) / $val : 1.0;
    if ($relDiff < 0.20) {
        // Léger écart → LOW
        return ['status' => 'contradicted', 'severity' => 'low', 'penalty' => -5,
                'wiki_says' => $closest . ' ' . $unit, 'value_diff' => round($relDiff*100,1) . '%'];
    } elseif ($relDiff < 0.50) {
        // Écart moyen → MEDIUM
        return ['status' => 'contradicted', 'severity' => 'medium', 'penalty' => -10,
                'wiki_says' => $closest . ' ' . $unit, 'value_diff' => round($relDiff*100,1) . '%'];
    } else {
        // Écart majeur (>50%) → HIGH (ex: 2745 → 9999 places = 264% off)
        return ['status' => 'contradicted', 'severity' => 'high', 'penalty' => -20,
                'wiki_says' => $closest . ' ' . $unit, 'value_diff' => round($relDiff*100,1) . '%'];
    }
}

function findYearNearTrigger(string $trigger, string $wikiNormalized): ?int
{
    // Itère sur TOUTES les occurrences du trigger (un titre/lien sans année
    // peut être la 1re occurrence — on cherche jusqu'à en trouver une avec
    // une année à proximité dans une window de ±60 chars).
    $offset = 0;
    $trigLen = mb_strlen($trigger);
    while (($pos = mb_stripos($wikiNormalized, $trigger, $offset)) !== false) {
        $start = max(0, $pos - 60);
        $window = mb_substr($wikiNormalized, $start, 180);
        if (preg_match('/\b(1[1-9]\d{2}|20[0-2]\d)\b/u', $window, $m)) {
            return (int)$m[1];
        }
        $offset = $pos + $trigLen;
    }
    return null;
}

function findNameNearTrigger(string $trigger, string $wikiText): ?string
{
    $offset = 0;
    $trigLen = mb_strlen($trigger);
    while (($pos = mb_stripos($wikiText, $trigger, $offset)) !== false) {
        $start = $pos + $trigLen;
        $window = mb_substr($wikiText, $start, 80);
        if (preg_match('/\b([A-ZÀ-Ý][a-zà-ÿ\-]{2,}(?:[\s\-][A-ZÀ-Ý][a-zà-ÿ\-]+)+)\b/u', $window, $m)) {
            return $m[1];
        }
        $offset = $pos + $trigLen;
    }
    return null;
}

// ─────────────────────────────────────────────────────────────
// Étape 6 : Scoring + verdict
// ─────────────────────────────────────────────────────────────

function computeScore(array $results): array
{
    $verified = 0; $contradicted = 0; $notFound = 0; $partial = 0;
    $contradictedPenalty = 0;
    $anomalies = []; $partials = [];

    foreach ($results as $r) {
        $s = $r['status'];
        if ($s === 'found') $verified++;
        elseif ($s === 'contradicted') {
            $contradicted++;
            $contradictedPenalty += abs($r['penalty']);
            $anomalies[] = [
                'type' => 'contradicted',
                'severity' => $r['severity'] ?? 'high',
                'signal_type' => $r['_type'],
                'signal' => $r['_value'],
                'context' => $r['_context'],
                'wiki_says' => $r['wiki_says'] ?? null,
                'trigger' => $r['trigger'] ?? null,
                'value_diff' => $r['value_diff'] ?? null,
                'penalty' => $r['penalty'],
                'note' => $r['note'] ?? "Valeur '{$r['_value']}' contradite (wiki: " . ($r['wiki_says'] ?? '?') . ")",
            ];
        } elseif ($s === 'partial') {
            $partial++;
            $partials[] = [
                'signal_type' => $r['_type'],
                'signal' => $r['_value'],
                'context' => $r['_context'],
                'note' => $r['note'] ?? '',
                'penalty' => $r['penalty'],
            ];
        } else {
            $notFound++;
        }
    }

    // Pénalité not_found cappée : -2 par not_found, max -10 total.
    // Rationale : Wikipedia ne couvre pas tout notre contenu éditorial
    // détaillé (1500+ mots vs 200-500 mots de résumé wiki). On ne veut
    // pas qu'un fort volume de NOT_FOUND fasse exploser le score si la
    // couverture (verified + contradicted) reste raisonnable.
    // Idem pour partial : capped -2 par, max -10 total.
    $notFoundPenalty = min(10, $notFound * 2);
    $partialPenalty  = min(10, $partial * 2);

    // Pénalité contradicted cappée à -25 total. V1 : la détection CONTRADICTED
    // sur years/dates peut générer des faux positifs (triggers ambigus + wiki
    // qui mentionne des années dans d'autres contextes). Le cap protège le
    // score d'un effondrement dû à plusieurs FP successifs, tout en permettant
    // FAIL si 2+ contradictions sévères (1 HIGH + 1 autre).
    $contradictedPenaltyCapped = min(25, $contradictedPenalty);

    // Bonus de couverture : si on a vérifié au moins 10 signaux ET 0 contradicted,
    // on est en zone "haute confiance" → +5 bonus (Bastille happy path doit
    // sortir score ≥ 91 selon brief utilisateur).
    $coverageBonus = ($verified >= 10 && $contradicted === 0) ? 5 : 0;

    $score = max(0, 100 - $contradictedPenaltyCapped - $notFoundPenalty - $partialPenalty + $coverageBonus);
    return [
        'score' => $score,
        'verified' => $verified,
        'contradicted' => $contradicted,
        'partial' => $partial,
        'not_found' => $notFound,
        'penalty_breakdown' => [
            'contradicted_raw' => -$contradictedPenalty,
            'contradicted_capped' => -$contradictedPenaltyCapped,
            'not_found_capped' => -$notFoundPenalty,
            'partial_capped' => -$partialPenalty,
            'coverage_bonus' => $coverageBonus,
        ],
        'anomalies' => $anomalies,
        'partials' => $partials,
    ];
}

function scoreToVerdict(int $score): string
{
    if ($score >= 90) return 'pass';
    if ($score >= 70) return 'warning';
    return 'fail';
}

// ─────────────────────────────────────────────────────────────
// MAIN
// ─────────────────────────────────────────────────────────────

$blocks   = collectEditorialText($station);
$signals  = extractSignals($blocks);
$targets  = identifyWikiTargets($station, $blocks);
$wikis    = fetchWikiContents($targets, $opts);

// Comparer chaque signal et enrichir avec _type / _value / _context pour le report
$results = [];
foreach ($signals as $sig) {
    $r = compareSignal($sig, $wikis);
    $r['_type'] = $sig['type'];
    $r['_value'] = (string)($sig['value'] ?? '');
    $r['_context'] = $sig['context'] . " '" . mb_substr($sig['snippet'] ?? '', 0, 80) . "...'";
    $results[] = $r;
}

$scoring = computeScore($results);
$verdict = scoreToVerdict($scoring['score']);

$report = [
    'slug' => $opts['slug'],
    'report_date' => date('Y-m-d'),
    'wikipedia_sources_consulted' => array_keys($wikis),
    'wikipedia_fetch_errors' => array_filter(array_map(fn($w) => $w['error'] ?? null, $wikis)),
    'signals_extracted' => count($signals),
    'signals_verified' => $scoring['verified'],
    'signals_contradicted' => $scoring['contradicted'],
    'signals_partial' => $scoring['partial'],
    'signals_not_found' => $scoring['not_found'],
    'penalty_breakdown' => $scoring['penalty_breakdown'],
    'score' => $scoring['score'],
    'verdict' => $verdict,
    'anomalies' => $scoring['anomalies'],
    'partials' => $scoring['partials'],
];

if ($opts['json']) {
    echo json_encode($report, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n";
} else {
    $emoji = $verdict === 'pass' ? '✅' : ($verdict === 'warning' ? '⚠️ ' : '❌');
    echo "\n$emoji  Diff Wikipedia — station {$opts['slug']}\n";
    echo str_repeat('─', 60) . "\n";
    echo "  Score      : {$report['score']}/100 ({$verdict})\n";
    echo "  Extraits   : {$report['signals_extracted']} signaux factuels\n";
    echo "  Vérifiés   : {$report['signals_verified']} ✓\n";
    echo "  Contradits : {$report['signals_contradicted']} ❌\n";
    echo "  Partiels   : {$report['signals_partial']} ◐\n";
    echo "  Non trouvés: {$report['signals_not_found']} (tolérance)\n";
    echo "  Sources    : " . count($wikis) . " pages Wikipedia FR\n";
    if (!empty($report['wikipedia_fetch_errors'])) {
        echo "  ⚠️ Erreurs fetch: " . count($report['wikipedia_fetch_errors']) . "\n";
    }

    if (!empty($scoring['anomalies'])) {
        echo "\n──── ANOMALIES (" . count($scoring['anomalies']) . ") ────\n";
        foreach ($scoring['anomalies'] as $a) {
            $sev = strtoupper($a['severity']);
            $pen = $a['penalty'];
            echo "  [$sev / $pen] {$a['signal_type']} : « {$a['signal']} »\n";
            echo "    contexte : {$a['context']}\n";
            if (!empty($a['wiki_says'])) echo "    wiki dit : « {$a['wiki_says']} »\n";
            if (!empty($a['trigger']))   echo "    trigger : « {$a['trigger']} »\n";
            if (!empty($a['note']))      echo "    note : {$a['note']}\n";
            echo "\n";
        }
    }

    if ($opts['verbose']) {
        echo "\n──── DÉTAIL (verbose) ────\n";
        foreach ($results as $r) {
            $icon = $r['status'] === 'found' ? '✓' : ($r['status'] === 'contradicted' ? '✗' : ($r['status'] === 'partial' ? '◐' : '?'));
            echo "  $icon  [{$r['_type']}] « {$r['_value']} » → {$r['status']} ({$r['_context']})\n";
        }
    }
    echo "\n";
}

exit($verdict === 'pass' ? 0 : ($verdict === 'warning' ? 1 : 2));
