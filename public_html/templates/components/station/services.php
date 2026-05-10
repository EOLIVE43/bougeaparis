<?php
/**
 * Composant : Services et infos pratiques (page station)
 *
 * Génère du contenu PERSONNALISÉ par station (nom + lieux précis +
 * contexte local) à partir d'un format JSON structuré. Évite le
 * duplicate content entre les 305 pages station.
 *
 * Format JSON `services` attendu :
 * {
 *   "wifi": { "available": bool, "location_detail": str, "coverage_detail": str },
 *   "toilets": { "public_paid": {...}, "public_free": {...} },
 *   "atm": { "available": bool, "banks_count_estimate": str, "locations": [str] },
 *   "ratp_office": { "available": bool, "location": str, "services": str },
 *   "left_luggage": { "ratp_available": bool, "third_party": [{name, type}] },
 *   "shopping_dining": { "main_location": str, "details": str, "secondary": str }
 * }
 *
 * Compatible legacy : si `services.wifi` est un booléen ou string
 * direct (ancien format), affiche en mode minimal.
 *
 * Variables attendues (props) :
 * - services    : array
 * - stationName : string
 *
 * Si vide → composant skip.
 */

$services    = $props['services']    ?? null;
$stationName = $props['stationName'] ?? null;

if (empty($services) || !is_array($services) || !$stationName) {
    return;
}

$stationE = Template::e($stationName); // déjà échappé pour réutilisation

/**
 * Helpers internes : génèrent le contenu d'une carte service
 * personnalisée selon le format structuré + nom de station.
 */

// WiFi
$renderWifi = function ($w) use ($stationE): string {
    if (is_bool($w)) {
        return $w
            ? "Le WiFi gratuit RATP est disponible à la station {$stationE}."
            : "Le WiFi gratuit RATP n'est pas déployé à la station {$stationE}.";
    }
    if (is_string($w) && $w !== '') return Template::e($w);
    if (!is_array($w)) return '';
    $available = $w['available'] ?? null;
    $loc = !empty($w['location_detail'])
        ? ' dans <strong>' . Template::e($w['location_detail']) . '</strong>'
        : '';
    $cov = !empty($w['coverage_detail'])
        ? ' La couverture s\'étend également sur ' . Template::e($w['coverage_detail']) . '.'
        : '';
    if ($available === false) {
        return "Le WiFi gratuit RATP n'est pas déployé à la station {$stationE}.";
    }
    return "Le <strong>WiFi gratuit RATP</strong> est disponible{$loc} de la station {$stationE}.{$cov}";
};

// Toilettes
$renderToilets = function ($t) use ($stationE): string {
    if (is_string($t) && $t !== '') return Template::e($t);
    if (!is_array($t)) return '';
    $parts = [];
    if (!empty($t['public_paid']['available'])) {
        $loc = !empty($t['public_paid']['location'])
            ? ' au niveau ' . Template::e($t['public_paid']['location'])
            : '';
        $acc = !empty($t['public_paid']['access'])
            ? ', accès via ' . Template::e($t['public_paid']['access'])
            : '';
        $parts[] = "<strong>Toilettes publiques payantes</strong>{$loc} de la station {$stationE}{$acc}.";
    }
    if (!empty($t['public_free']['available'])) {
        $loc = !empty($t['public_free']['location'])
            ? ' dans ' . Template::e($t['public_free']['location'])
            : '';
        $acc = !empty($t['public_free']['access'])
            ? ' (' . Template::e($t['public_free']['access']) . ')'
            : '';
        $parts[] = "Toilettes gratuites à proximité{$loc}{$acc}.";
    }
    if (empty($parts)) {
        return "Pas de toilettes publiques signalées à la station {$stationE}.";
    }
    return implode(' ', $parts);
};

// Distributeurs
$renderAtm = function ($a) use ($stationE): string {
    if (is_string($a) && $a !== '') return Template::e($a);
    if (!is_array($a)) return '';
    if (($a['available'] ?? null) === false) {
        return "Pas de distributeur signalé à la station {$stationE}.";
    }
    $banks = !empty($a['banks_count_estimate'])
        ? ' de ' . Template::e($a['banks_count_estimate'])
        : '';
    $locs = $a['locations'] ?? [];
    $locsTxt = '';
    if (!empty($locs)) {
        $escapedLocs = array_map(fn($l) => Template::e($l), $locs);
        if (count($escapedLocs) === 1) {
            $locsTxt = ' dans ' . $escapedLocs[0];
        } else {
            $last = array_pop($escapedLocs);
            $locsTxt = ' dans ' . implode(', ', $escapedLocs) . ' et ' . $last;
        }
    }
    return "Distributeurs de billets{$banks} disponibles{$locsTxt} à la station {$stationE}.";
};

// Espace voyageurs RATP
$renderOffice = function ($o) use ($stationE): string {
    if (is_string($o) && $o !== '') return Template::e($o);
    if (!is_array($o)) return '';
    if (($o['available'] ?? null) === false) {
        return "Pas d'espace voyageurs RATP en propre à la station {$stationE}.";
    }
    $loc = !empty($o['location']) ? ' au niveau ' . Template::e($o['location']) : '';
    $svc = !empty($o['services']) ? ' Services : ' . Template::e($o['services']) . '.' : '';
    return "<strong>Espace voyageurs RATP</strong>{$loc} de la station {$stationE}.{$svc}";
};

// Consigne à bagages
$renderLuggage = function ($l) use ($stationE): string {
    if (is_string($l) && $l !== '') return Template::e($l);
    if (!is_array($l)) return '';
    $parts = [];
    if (!empty($l['ratp_available'])) {
        $parts[] = "Consigne à bagages RATP disponible à la station {$stationE}.";
    } else {
        $parts[] = "Pas de consigne RATP en propre à la station {$stationE}.";
    }
    $tps = $l['third_party'] ?? [];
    if (!empty($tps) && is_array($tps)) {
        $names = [];
        foreach ($tps as $tp) {
            if (!empty($tp['name'])) {
                $names[] = '<strong>' . Template::e($tp['name']) . '</strong>'
                         . (!empty($tp['type']) ? ' (' . Template::e($tp['type']) . ')' : '');
            }
        }
        if ($names) {
            $parts[] = 'Services privés disponibles : ' . implode(', ', $names) . '.';
        }
    }
    return implode(' ', $parts);
};

// Commerces et restauration
$renderShopping = function ($s) use ($stationE): string {
    if (is_string($s) && $s !== '') return Template::e($s);
    if (!is_array($s)) return '';
    $main = !empty($s['main_location']) ? '<strong>' . Template::e($s['main_location']) . '</strong>' : '';
    $det  = !empty($s['details']) ? Template::e($s['details']) : '';
    $sec  = !empty($s['secondary']) ? ' ' . Template::e($s['secondary']) . '.' : '';
    if ($main && $det) {
        return "Commerces et restauration accessibles depuis {$stationE} : {$main} — {$det}.{$sec}";
    }
    if ($main) {
        return "Commerces et restauration accessibles depuis {$stationE} : {$main}.{$sec}";
    }
    return "Commerces à proximité de la station {$stationE}.{$sec}";
};

$items = [
    'wifi'             => ['label' => 'WiFi gratuit',           'icon' => '📶', 'render' => $renderWifi],
    'toilets'          => ['label' => 'Toilettes',              'icon' => '🚻', 'render' => $renderToilets],
    'atm'              => ['label' => 'Distributeurs',          'icon' => '💳', 'render' => $renderAtm],
    'ratp_office'      => ['label' => 'Espace voyageurs RATP',  'icon' => 'ℹ️',  'render' => $renderOffice],
    'left_luggage'     => ['label' => 'Consigne à bagages',     'icon' => '🧳', 'render' => $renderLuggage],
    'shopping_dining'  => ['label' => 'Commerces et restauration', 'icon' => '🛍️', 'render' => $renderShopping],
];

// Compat ancien format (pré-2026-05-10) : services.consigne_bagages,
// services.espace_voyageurs, services.commerces (clés plates).
$legacyMap = [
    'consigne_bagages' => 'left_luggage',
    'espace_voyageurs' => 'ratp_office',
    'commerces'        => 'shopping_dining',
];
foreach ($legacyMap as $oldKey => $newKey) {
    if (isset($services[$oldKey]) && !isset($services[$newKey])) {
        $services[$newKey] = $services[$oldKey];
    }
}

$visibleCount = 0;
foreach ($items as $k => $cfg) {
    if (isset($services[$k]) && $services[$k] !== null && $services[$k] !== '') {
        $visibleCount++;
    }
}
if ($visibleCount === 0) {
    return;
}
?>

<section class="station-section section-services" id="services" aria-labelledby="services-title">

  <h2 id="services-title">Services et infos pratiques à <?= $stationE ?></h2>

  <p class="section-intro">
    Voici les services disponibles à la station <strong><?= $stationE ?></strong>. Les équipements peuvent évoluer ; consultez l'application <a href="https://www.bonjour-ratp.fr/" target="_blank" rel="noopener">Bonjour RATP</a> pour l'information la plus à jour avant votre voyage.
  </p>

  <ul class="services-list">
    <?php foreach ($items as $key => $cfg):
      $val = $services[$key] ?? null;
      if ($val === null || $val === '') continue;
      $body = $cfg['render']($val);
      if ($body === '') continue;
    ?>
      <li class="service-item">
        <span class="service-item__icon" aria-hidden="true"><?= Template::e($cfg['icon']) ?></span>
        <div class="service-item__content">
          <strong class="service-item__label"><?= Template::e($cfg['label']) ?></strong>
          <span class="service-item__detail"><?= richText($body) ?></span>
        </div>
      </li>
    <?php endforeach; ?>
  </ul>

</section>
