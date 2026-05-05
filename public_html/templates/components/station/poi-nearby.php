<?php
/**
 * Composant : Que voir à proximité (page station)
 *
 * Affiche un top 10 de monuments / sites notables à proximité de la station,
 * extraits depuis Wikidata Query Service via scripts/build-station-pois.php.
 * Pour chaque POI : image Commons, nom, catégorie, description courte
 * (extraite de Wikipedia FR), sortie de station la plus proche + temps à pied.
 *
 * Variables attendues :
 *   $pois        : array, liste des POIs (clé "nearby_pois" du JSON station).
 *                  Chaque entrée : { wikidata_id, name, category, description,
 *                                    image_url, wikipedia_url, latitude,
 *                                    longitude, nearest_exit:{number, name,
 *                                    distance_m, walk_minutes} }
 *   $stationName : string, nom de la station (pour titre + aria).
 *
 * Affichage responsive :
 *   - Mobile (<640px)   : 1 col
 *   - Tablet (≥640px)   : 2 col
 *   - Desktop (≥1024px) : 3 col
 *
 * Si $pois est vide, le composant n'affiche rien.
 *
 * @package BougeaParis\Templates\Components\Station
 * @since Livraison 7
 */

$pois        = $props['pois']        ?? null;
$stationName = $props['stationName'] ?? null;

if (empty($pois) || !is_array($pois)) {
    return;
}

$stationName = $stationName ?? 'cette station';
// Filtre : on n'affiche pas les POIs masqués manuellement (override)
$pois = array_values(array_filter($pois, fn($p) => empty($p['is_hidden'])));
if (empty($pois)) return;

$count = count($pois);
?>

<section class="station-section section-poi" id="poi" aria-labelledby="poi-heading">

  <h2 id="poi-heading">Que voir à proximité de la station <?= e($stationName) ?></h2>

  <p class="section-intro">
    Cette sélection de
    <strong><?= (int)$count ?> monuments et sites notables</strong>
    autour de la station <strong><?= e($stationName) ?></strong> est composée
    automatiquement à partir de Wikidata, classée par notoriété (nombre d'articles
    Wikipédia tous langages confondus). Pour chaque lieu, nous indiquons la sortie
    la plus proche et le temps à pied estimé.
  </p>

  <ul class="poi-grid" role="list">
    <?php foreach ($pois as $poi):
      $name        = (string)($poi['name']         ?? '');
      $category    = (string)($poi['category']     ?? '');
      $description = (string)($poi['description']  ?? '');
      $imageUrl    = (string)($poi['image_url']    ?? '');
      $wikiUrl     = (string)($poi['wikipedia_url'] ?? '');
      $exit        = $poi['nearest_exit']           ?? null;
      $featured    = !empty($poi['is_featured']);

      $hasImage = $imageUrl !== '';
      $hasExit  = is_array($exit) && !empty($exit['number']);
    ?>
      <li class="poi-card<?= $featured ? ' poi-card--featured' : '' ?>">
        <?php if ($hasImage): ?>
          <div class="poi-image">
            <img src="<?= e($imageUrl) ?>"
                 alt="<?= e($name) ?>"
                 loading="lazy"
                 referrerpolicy="no-referrer"
                 width="400" height="225">
          </div>
        <?php else: ?>
          <div class="poi-image poi-image--placeholder" aria-hidden="true">
            <span class="poi-image__icon">📍</span>
          </div>
        <?php endif; ?>

        <div class="poi-content">
          <?php if ($category !== ''): ?>
            <span class="poi-category"><?= e($category) ?></span>
          <?php endif; ?>

          <h3 class="poi-name"><?= e($name) ?></h3>

          <?php if ($description !== ''): ?>
            <p class="poi-description"><?= e($description) ?></p>
          <?php endif; ?>

          <?php if ($hasExit): ?>
            <div class="poi-exit" aria-label="Accès depuis la station">
              <span class="poi-exit__icon" aria-hidden="true">→</span>
              Sortie <strong><?= e((string)$exit['number']) ?></strong>
              <?php if (!empty($exit['name'])): ?>
                « <?= e($exit['name']) ?> »
              <?php endif; ?>
              ·
              <span class="poi-exit__walk"><?= (int)$exit['walk_minutes'] ?> min à pied</span>
              <span class="poi-exit__dist"> (<?= (int)$exit['distance_m'] ?> m)</span>
            </div>
          <?php endif; ?>

          <?php if ($wikiUrl !== ''): ?>
            <a class="poi-link"
               href="<?= e($wikiUrl) ?>"
               target="_blank"
               rel="noopener noreferrer"
               aria-label="<?= e($name) ?> sur Wikipédia (nouvel onglet)">
              En savoir plus →
            </a>
          <?php endif; ?>
        </div>
      </li>
    <?php endforeach; ?>
  </ul>

  <p class="poi-note">
    <small>
      Sources : <a href="https://www.wikidata.org/" target="_blank" rel="noopener noreferrer">Wikidata</a>
      (sélection automatique par notoriété),
      <a href="https://fr.wikipedia.org/" target="_blank" rel="noopener noreferrer">Wikipédia FR</a>
      (descriptions),
      <a href="https://commons.wikimedia.org/" target="_blank" rel="noopener noreferrer">Wikimedia Commons</a>
      (photos). Temps à pied estimés à 80 m/min depuis la sortie de métro la plus proche.
    </small>
  </p>

</section>
