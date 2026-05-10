<?php
/**
 * Composant : Continuer votre exploration (page station)
 *
 * Maillage interne bas de page : 4 blocs de liens internes pour
 * pousser le SEO et l'engagement.
 *
 * Bloc 1 — Stations proches sur la même ligne (4-6 voisines extraites
 *          de data/lines/{slug}.json, autour de la station courante).
 * Bloc 2 — Lien vers la page hub de la ligne.
 * Bloc 3 — Hubs similaires (uniquement si is_major_hub: true).
 *          Sources : data/global/major-hubs.json + station.is_major_hub.
 * Bloc 4 — Liens utilitaires : plan métro, tarifs, info trafic, hub
 *          /metro/.
 *
 * Pattern Routes::exists() partout : pastille cliquable si la page
 * existe, sinon span statique avec data-future-url (cocon SEO).
 *
 * Variables attendues (props) :
 * - station       : array, JSON station courant
 * - stationName   : string
 * - stationSlug   : string
 * - lines         : array (mêmes structure que dans station-metro)
 *
 * Si station vide → composant skip.
 */

$station     = $props['station']     ?? null;
$stationName = $props['stationName'] ?? null;
$stationSlug = $props['stationSlug'] ?? null;
$lines       = $props['lines']       ?? [];

if (empty($station) || !$stationName || !$stationSlug) {
    return;
}

$stationE = Template::e($stationName);

/* -----------------------------------------------------------
 * Bloc 1 : Stations proches sur la même ligne
 * ----------------------------------------------------------- */
$nearbyStations = [];
$primaryLine    = $lines[0] ?? null;
$primaryLineSlug = $primaryLine['slug'] ?? null;
$primaryLineCode = $primaryLine['code'] ?? null;

if ($primaryLineSlug) {
    $linePath = __DIR__ . '/../../../data/lines/' . $primaryLineSlug . '.json';
    if (is_file($linePath)) {
        $lineData = json_decode((string) file_get_contents($linePath), true);
        $allStations = is_array($lineData) ? ($lineData['stations'] ?? []) : [];
        // Trouver l'index de la station courante (par nom approximatif)
        $currentIdx = null;
        $needle = mb_strtolower(trim($station['name'] ?? ''), 'UTF-8');
        foreach ($allStations as $i => $s) {
            $cand = mb_strtolower(trim($s['name'] ?? ''), 'UTF-8');
            if ($cand === $needle || (str_contains($cand, $needle) && mb_strlen($needle) > 4)) {
                $currentIdx = $i;
                break;
            }
        }
        if ($currentIdx !== null) {
            // Prendre 3 stations avant + 3 après (filtrées sur celles qui ont un slug)
            $start = max(0, $currentIdx - 3);
            $end   = min(count($allStations) - 1, $currentIdx + 3);
            for ($j = $start; $j <= $end; $j++) {
                if ($j === $currentIdx) continue;
                $s = $allStations[$j];
                $sname = $s['name'] ?? '';
                if ($sname === '') continue;
                $sslug = $s['slug'] ?? Routes::stationSlug($sname);
                if (!$sslug) continue;
                $nearbyStations[] = [
                    'name' => $sname,
                    'slug' => $sslug,
                    'url'  => '/metro/station/' . $sslug . '/',
                    'subtitle' => $s['subtitle'] ?? null,
                ];
            }
        }
    }
}

/* -----------------------------------------------------------
 * Bloc 3 : Hubs similaires (si is_major_hub)
 * ----------------------------------------------------------- */
$similarHubs = [];
$isHub = !empty($station['is_major_hub']);
if ($isHub) {
    // Source explicite dans le JSON station prioritaire,
    // sinon registre central data/global/major-hubs.json.
    $explicit = $station['similar_hubs'] ?? null;
    if (is_array($explicit) && !empty($explicit)) {
        $hubKeys = $explicit;
    } else {
        $registryPath = __DIR__ . '/../../../data/global/major-hubs.json';
        $hubKeys = [];
        if (is_file($registryPath)) {
            $registry = json_decode((string) file_get_contents($registryPath), true);
            if (is_array($registry)) {
                $entry = $registry['hubs'][$stationSlug] ?? null;
                if ($entry && !empty($entry['similar'])) {
                    $hubKeys = $entry['similar'];
                }
            }
        }
    }
    foreach ($hubKeys as $hubSlug) {
        $similarHubs[] = [
            'slug' => $hubSlug,
            'url'  => '/metro/station/' . $hubSlug . '/',
            // Le label sera dérivé du registre si dispo (pour
            // afficher « Châtelet » plutôt que « chatelet »)
        ];
    }
    // Enrichir les labels via le registre si manquants
    if (!empty($similarHubs)) {
        $registryPath = __DIR__ . '/../../../data/global/major-hubs.json';
        if (is_file($registryPath)) {
            $registry = json_decode((string) file_get_contents($registryPath), true);
            if (is_array($registry)) {
                foreach ($similarHubs as &$h) {
                    $entry = $registry['hubs'][$h['slug']] ?? null;
                    $h['label'] = $entry['label'] ?? ucwords(str_replace('-', ' ', $h['slug']));
                }
                unset($h);
            }
        }
    }
}

/* -----------------------------------------------------------
 * Bloc 2 : URL hub ligne
 * ----------------------------------------------------------- */
$lineHubUrl = $primaryLineCode ? '/metro/ligne-' . strtolower($primaryLineCode) . '/' : null;

/* -----------------------------------------------------------
 * Bloc 4 : URLs utilitaires (Routes::exists pour activation)
 * ----------------------------------------------------------- */
$utilLinks = [
    ['url' => '/metro/',         'label' => 'Toutes les lignes de métro de Paris', 'icon' => '🚇'],
    ['url' => '/info-trafic/',   'label' => 'Info trafic en direct',                 'icon' => '🚦'],
    ['url' => '/tarifs/',        'label' => 'Tarifs et titres de transport',         'icon' => '🎫'],
    ['url' => '/metro/plan/',    'label' => 'Plan du métro de Paris',                'icon' => '🗺️'],
];

if (empty($nearbyStations) && empty($similarHubs) && !$lineHubUrl) {
    return; // Skip si rien à afficher (cas extrême)
}
?>

<section class="station-section section-maillage" id="continuer-exploration" aria-labelledby="maillage-title">

  <h2 id="maillage-title">Continuer votre exploration depuis <?= $stationE ?></h2>

  <?php if (!empty($nearbyStations) && $primaryLineCode): ?>
    <div class="maillage-block">
      <h3 class="maillage-block__title">Stations proches de <?= $stationE ?> sur la Ligne <?= Template::e($primaryLineCode) ?></h3>
      <ul class="maillage-list">
        <?php foreach ($nearbyStations as $s):
          $exists = Routes::exists(rtrim($s['url'], '/'));
        ?>
          <li>
            <?php if ($exists): ?>
              <a href="<?= Template::e($s['url']) ?>" class="maillage-pill">
                <span class="maillage-pill__name"><?= Template::e($s['name']) ?></span>
                <?php if (!empty($s['subtitle'])): ?>
                  <span class="maillage-pill__subtitle"><?= Template::e($s['subtitle']) ?></span>
                <?php endif; ?>
              </a>
            <?php else: ?>
              <span class="maillage-pill maillage-pill--inactive" data-future-url="<?= Template::e($s['url']) ?>">
                <span class="maillage-pill__name"><?= Template::e($s['name']) ?></span>
                <?php if (!empty($s['subtitle'])): ?>
                  <span class="maillage-pill__subtitle"><?= Template::e($s['subtitle']) ?></span>
                <?php endif; ?>
              </span>
            <?php endif; ?>
          </li>
        <?php endforeach; ?>
      </ul>
    </div>
  <?php endif; ?>

  <?php if ($lineHubUrl):
    $lineHubExists = Routes::exists(rtrim($lineHubUrl, '/'));
  ?>
    <div class="maillage-block maillage-block--line-hub">
      <?php if ($lineHubExists): ?>
        <a href="<?= Template::e($lineHubUrl) ?>" class="maillage-cta">
          → Voir toutes les stations de la Ligne <?= Template::e($primaryLineCode) ?>
        </a>
      <?php else: ?>
        <span class="maillage-cta maillage-cta--inactive" data-future-url="<?= Template::e($lineHubUrl) ?>">
          Toutes les stations de la Ligne <?= Template::e($primaryLineCode) ?> (bientôt)
        </span>
      <?php endif; ?>
    </div>
  <?php endif; ?>

  <?php if (!empty($similarHubs)): ?>
    <div class="maillage-block">
      <h3 class="maillage-block__title">Autres grands pôles multimodaux comparables à <?= $stationE ?></h3>
      <ul class="maillage-list">
        <?php foreach ($similarHubs as $h):
          $exists = Routes::exists(rtrim($h['url'], '/'));
          $label  = $h['label'] ?? ucwords(str_replace('-', ' ', $h['slug']));
        ?>
          <li>
            <?php if ($exists): ?>
              <a href="<?= Template::e($h['url']) ?>" class="maillage-pill">
                <span class="maillage-pill__name"><?= Template::e($label) ?></span>
              </a>
            <?php else: ?>
              <span class="maillage-pill maillage-pill--inactive" data-future-url="<?= Template::e($h['url']) ?>">
                <span class="maillage-pill__name"><?= Template::e($label) ?></span>
              </span>
            <?php endif; ?>
          </li>
        <?php endforeach; ?>
      </ul>
    </div>
  <?php endif; ?>

  <div class="maillage-block">
    <h3 class="maillage-block__title">Pour aller plus loin</h3>
    <ul class="maillage-utils">
      <?php foreach ($utilLinks as $u):
        $exists = Routes::exists(rtrim($u['url'], '/'));
      ?>
        <li>
          <?php if ($exists): ?>
            <a href="<?= Template::e($u['url']) ?>" class="maillage-util">
              <span class="maillage-util__icon" aria-hidden="true"><?= Template::e($u['icon']) ?></span>
              <?= Template::e($u['label']) ?>
              <span aria-hidden="true">→</span>
            </a>
          <?php else: ?>
            <span class="maillage-util maillage-util--inactive" data-future-url="<?= Template::e($u['url']) ?>">
              <span class="maillage-util__icon" aria-hidden="true"><?= Template::e($u['icon']) ?></span>
              <?= Template::e($u['label']) ?>
              <span class="maillage-util__soon">(bientôt)</span>
            </span>
          <?php endif; ?>
        </li>
      <?php endforeach; ?>
    </ul>
  </div>

</section>
