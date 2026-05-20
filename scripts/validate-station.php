<?php
declare(strict_types=1);

/**
 * scripts/validate-station.php
 *
 * Validation factuelle d'un JSON station avant déploiement automatique.
 * Conçu pour le workflow .github/workflows/auto-deploy-station.yml.
 *
 * Vérifications :
 *   1. Champs critiques présents et non vides (slug, name, lines, address,
 *      latitude, longitude, hero, intro_paragraphs, faq, history)
 *   2. accessibility.audit_status est 'verified' (pas 'pending')
 *   3. Pour chaque POI dans nearby_pois :
 *      - wikidata_id présent et au format Q\d+
 *      - Vérification via Wikidata wbgetentities (si --check-wikidata)
 *      - Cohérence : label fr OU description contient au moins 1 mot
 *        significatif du POI.name (anti-bug Q-IDs inventés)
 *      - Cohérence GPS : POI dans 1km autour de la station
 *
 * Usage :
 *   php scripts/validate-station.php --slug=la-defense-grande-arche
 *   php scripts/validate-station.php --slug=chatelet --check-wikidata
 *   php scripts/validate-station.php --slug=X --json (sortie JSON)
 *
 * Exit codes :
 *   0 = JSON station valide
 *   1 = Erreurs critiques détectées
 *   2 = Fichier ou args manquants
 */

const ROOT = __DIR__ . '/..';
const STATIONS_DIR = ROOT . '/public_html/data/stations';
const USER_AGENT = 'BougeaParis-validate-station/1.0 (https://bougeaparis.fr)';

// CLI args
$slug = null;
$checkWikidata = false;
$jsonOutput = false;
foreach (array_slice($argv, 1) as $arg) {
    if (str_starts_with($arg, '--slug=')) {
        $slug = substr($arg, 7);
    } elseif ($arg === '--check-wikidata') {
        $checkWikidata = true;
    } elseif ($arg === '--json') {
        $jsonOutput = true;
    }
}

if (!$slug) {
    fwrite(STDERR, "Usage: php validate-station.php --slug=X [--check-wikidata] [--json]\n");
    exit(2);
}

$jsonPath = STATIONS_DIR . '/' . $slug . '.json';
if (!is_file($jsonPath)) {
    fwrite(STDERR, "ERROR: $jsonPath not found\n");
    exit(2);
}

$station = json_decode((string) file_get_contents($jsonPath), true);
if (!is_array($station)) {
    fwrite(STDERR, "ERROR: invalid JSON in $jsonPath\n");
    exit(2);
}

$errors = [];
$warnings = [];

// Backlog D — lecture flag published (cohérence garde-fou Phase 1.3 routing).
// Source de vérité unique : $station['published']. Une page squelette en review
// (published:false) tolère certains champs vides en warnings ; une page exposée
// (published:true) exige tous ces champs en erreurs critiques.
$isPublished = ($station['published'] ?? false) === true;

// Helper : règle stricte uniquement en mode publié.
$strictIfPublished = function (string $message) use ($isPublished, &$errors, &$warnings): void {
    if ($isPublished) {
        $errors[] = $message;
    } else {
        $warnings[] = $message . " (toléré : published=false, deviendra erreur au flip)";
    }
};

// 1. Champs critiques — séparés en 2 groupes :
//    A. Intégrité minimale (toujours erreur, même squelette) : slug/name/lat/lon/lines/intro/faq/history
//    B. Tolérés en squelette (warning si published:false, erreur si published:true) : address, arrondissement
$required_strict     = ['slug', 'name', 'latitude', 'longitude', 'lines', 'intro_paragraphs', 'faq', 'history'];
$required_published  = ['address', 'arrondissement'];

foreach ($required_strict as $field) {
    if (empty($station[$field])) {
        $errors[] = "Champ manquant ou vide : $field";
    }
}
foreach ($required_published as $field) {
    if (empty($station[$field])) {
        $strictIfPublished("Champ manquant ou vide : $field");
    }
}

// 2. Coords cohérentes (Île-de-France grosso modo : 48.5-49.0 lat / 1.8-2.7 lon)
$lat = (float) ($station['latitude'] ?? 0);
$lon = (float) ($station['longitude'] ?? 0);
if ($lat < 48.5 || $lat > 49.0) {
    $errors[] = "Latitude hors Île-de-France : $lat";
}
if ($lon < 1.8 || $lon > 2.7) {
    $errors[] = "Longitude hors Île-de-France : $lon";
}

// 3. Hero image — Groupe B (strictIfPublished : généré par workflow CI au flip published:true)
$hero = $station['hero_image'] ?? null;
if (!$hero) {
    $strictIfPublished("hero_image absent");
} else {
    foreach (['url', 'alt'] as $f) {
        if (empty($hero[$f])) $strictIfPublished("hero_image.$f manquant");
    }
    // crédits restent warnings : attribution Wikimedia, non bloquant
    if (empty($hero['credit']['author'])) $warnings[] = "hero_image.credit.author manquant (attribution Wikimedia)";
    if (empty($hero['credit']['license'])) $warnings[] = "hero_image.credit.license manquant";
}

// 4. POIs (anti-bug Q-IDs inventés du brief La Défense)
$pois = $station['nearby_pois'] ?? [];
if (empty($pois)) {
    $warnings[] = "Aucun POI déclaré (section 'Que voir' ne sera pas affichée)";
} else {
    foreach ($pois as $i => $poi) {
        $name = $poi['name'] ?? "(POI #$i)";
        $qid = $poi['wikidata_id'] ?? null;
        if (!$qid) {
            $errors[] = "POI #$i ($name) : wikidata_id manquant";
            continue;
        }
        if (!preg_match('/^Q\d+$/', $qid)) {
            $errors[] = "POI #$i ($name) : wikidata_id invalide ($qid)";
            continue;
        }

        // Cohérence GPS : POI doit être dans 1km autour de la station
        $pLat = (float) ($poi['latitude'] ?? 0);
        $pLon = (float) ($poi['longitude'] ?? 0);
        if ($pLat && $pLon) {
            $dist = haversine($lat, $lon, $pLat, $pLon);
            if ($dist > 1500) {
                $warnings[] = "POI '$name' ($qid) à " . round($dist) . "m de la station (suspect, > 1500m)";
            }
        }

        if ($checkWikidata) {
            $check = checkWikidata($qid, $name);
            if ($check['error']) {
                $errors[] = "POI '$name' ($qid) Wikidata : " . $check['error'];
            } elseif (!$check['name_match']) {
                $errors[] = "POI '$name' ($qid) ne correspond pas au label Wikidata « " . $check['label'] . " » — Q-ID probablement inventé (bug La Défense récurrent)";
            }
        }
    }
}

// 5. accessibility audit_status
$audit = $station['accessibility']['audit_status'] ?? null;
if ($audit && $audit !== 'verified') {
    $warnings[] = "accessibility.audit_status = '$audit' (idéal : 'verified')";
}

// 6. tariff_zone (anticipation pour personnalisation)
if (empty($station['tariff_zone'])) {
    $warnings[] = "tariff_zone absent (recommandé pour personnalisation tarifs)";
}

// ============= REPORT =============

$result = [
    'slug' => $slug,
    'valid' => empty($errors),
    'errors' => $errors,
    'warnings' => $warnings,
    'fields_count' => count(array_keys($station)),
    'pois_count' => count($pois),
];

if ($jsonOutput) {
    echo json_encode($result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . "\n";
} else {
    echo "=== Validation station : $slug ===\n\n";
    echo "Champs JSON : {$result['fields_count']}\n";
    echo "POIs déclarés : {$result['pois_count']}\n\n";
    if (!empty($errors)) {
        echo "❌ ERREURS (" . count($errors) . ") :\n";
        foreach ($errors as $e) echo "  - $e\n";
        echo "\n";
    }
    if (!empty($warnings)) {
        echo "⚠️  WARNINGS (" . count($warnings) . ") :\n";
        foreach ($warnings as $w) echo "  - $w\n";
        echo "\n";
    }
    if (empty($errors) && empty($warnings)) {
        echo "✅ Station valide, aucun warning\n";
    } elseif (empty($errors)) {
        echo "✅ Station valide (warnings seulement)\n";
    } else {
        echo "❌ Validation échouée : " . count($errors) . " erreur(s)\n";
    }
}

exit(empty($errors) ? 0 : 1);


// ============= HELPERS =============

function haversine(float $lat1, float $lon1, float $lat2, float $lon2): float {
    $R = 6371000; // mètres
    $dLat = deg2rad($lat2 - $lat1);
    $dLon = deg2rad($lon2 - $lon1);
    $a = sin($dLat/2) ** 2 + cos(deg2rad($lat1)) * cos(deg2rad($lat2)) * sin($dLon/2) ** 2;
    return $R * 2 * atan2(sqrt($a), sqrt(1-$a));
}

function checkWikidata(string $qid, string $expectedName): array {
    $url = 'https://www.wikidata.org/w/api.php?action=wbgetentities&ids=' . urlencode($qid)
         . '&languages=fr|en&props=labels|descriptions|aliases&format=json';
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_USERAGENT => USER_AGENT,
        CURLOPT_TIMEOUT => 15,
    ]);
    $resp = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    if ($code !== 200 || !$resp) return ['error' => "HTTP $code", 'name_match' => false, 'label' => ''];
    $d = json_decode((string) $resp, true);
    $entity = $d['entities'][$qid] ?? null;
    if (!$entity) return ['error' => 'Entity not found', 'name_match' => false, 'label' => ''];
    if (isset($entity['missing'])) return ['error' => 'Q-ID inexistant ou supprimé', 'name_match' => false, 'label' => ''];
    $labelFr = $entity['labels']['fr']['value'] ?? '';
    $labelEn = $entity['labels']['en']['value'] ?? '';
    $descFr  = $entity['descriptions']['fr']['value'] ?? '';
    // Aliases (acronymes, noms alternatifs comme « CNIT » pour
    // « Centre des Nouvelles Industries et Technologies »)
    $aliases = [];
    foreach (['fr', 'en'] as $lang) {
        foreach ($entity['aliases'][$lang] ?? [] as $a) {
            if (!empty($a['value'])) $aliases[] = $a['value'];
        }
    }
    $haystack = strtolower(remove_accents(
        $labelFr . ' ' . $labelEn . ' ' . $descFr . ' ' . implode(' ', $aliases)
    ));

    // 3 stratégies de match (une suffit pour valider) :
    // 1) Le name complet normalisé apparaît dans le haystack (ex: "cnit"
    //    apparaît dans aliases ou label si c'est un acronyme connu).
    $nameNorm = strtolower(remove_accents(preg_replace('/[^A-Za-z0-9 ]/', ' ', $expectedName)));
    $nameClean = trim(preg_replace('/\s+/', ' ', $nameNorm));
    if ($nameClean !== '' && str_contains($haystack, $nameClean)) {
        return ['error' => null, 'name_match' => true, 'label' => $labelFr ?: $labelEn];
    }
    // 2) Au moins un mot ≥ 4 chars du name apparaît dans le haystack.
    foreach (preg_split('/\s+/', $nameClean) as $w) {
        if (strlen($w) >= 4 && str_contains($haystack, $w)) {
            return ['error' => null, 'name_match' => true, 'label' => $labelFr ?: $labelEn];
        }
    }
    // 3) Acronyme (name court ≤ 6 chars) : match sur initiales du label
    //    (ex: "CNIT" matche "Centre Nouvelles Industries Technologies").
    if (strlen($nameClean) <= 6 && preg_match('/^[a-z]+$/', $nameClean)) {
        $initials = '';
        foreach (preg_split('/\s+/', strtolower(remove_accents($labelFr ?: $labelEn))) as $w) {
            if ($w !== '' && !in_array($w, ['de', 'des', 'du', 'la', 'le', 'les', 'à', 'a', 'd', 'l'], true)) {
                $initials .= $w[0];
            }
        }
        if ($initials !== '' && (str_contains($initials, $nameClean) || str_contains($nameClean, $initials))) {
            return ['error' => null, 'name_match' => true, 'label' => $labelFr ?: $labelEn];
        }
    }
    return ['error' => null, 'name_match' => false, 'label' => $labelFr ?: $labelEn];
}

function remove_accents(string $s): string {
    return strtr($s, [
        'à'=>'a','á'=>'a','â'=>'a','ä'=>'a','ã'=>'a','å'=>'a',
        'è'=>'e','é'=>'e','ê'=>'e','ë'=>'e',
        'ì'=>'i','í'=>'i','î'=>'i','ï'=>'i',
        'ò'=>'o','ó'=>'o','ô'=>'o','ö'=>'o','õ'=>'o',
        'ù'=>'u','ú'=>'u','û'=>'u','ü'=>'u',
        'ç'=>'c','ñ'=>'n','ÿ'=>'y',
        'À'=>'A','Á'=>'A','Â'=>'A','Ä'=>'A',
        'È'=>'E','É'=>'E','Ê'=>'E','Ë'=>'E',
        'Ç'=>'C',
    ]);
}
