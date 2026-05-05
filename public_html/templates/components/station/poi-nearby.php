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

<section class="station-section section-poi" id="poi-nearby" aria-labelledby="poi-heading">

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
      // wikipedia_url conserve dans le JSON (audit + future migration vers
      // pages POI internes) mais NON utilise pour le rendu : voir TODO ci-dessous.
      $exit        = $poi['nearest_exit']           ?? null;
      $featured    = !empty($poi['is_featured']);

      // Wikidata renvoie les labels en bas de casse ("cathedrale Notre-Dame",
      // "pont Neuf", "ile de la Cite"). On force une majuscule sur la 1re lettre
      // uniquement (preserve "Notre-Dame", "La Samaritaine", "Saint-Eustache",
      // ...) en multi-byte safe pour les accents (mb_strtoupper sur 1 char).
      $nameDisplay = $name !== ''
          ? mb_strtoupper(mb_substr($name, 0, 1, 'UTF-8'), 'UTF-8') . mb_substr($name, 1, null, 'UTF-8')
          : '';

      $hasImage = $imageUrl !== '';
      $hasExit  = is_array($exit) && !empty($exit['number']);
    ?>
      <li class="poi-card<?= $featured ? ' poi-card--featured' : '' ?>">
        <?php if ($hasImage): ?>
          <div class="poi-image">
            <img src="<?= e($imageUrl) ?>"
                 alt="<?= e($nameDisplay) ?>"
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

          <h3 class="poi-name"><?= e($nameDisplay) ?></h3>

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

          <?php
          // TODO: réactiver le lien quand les pages POI internes existeront (/lieu/{slug}/)
          // Pour l'instant, on évite d'envoyer le trafic vers Wikipedia.
          // L'URL Wikipedia reste disponible dans $poi['wikipedia_url'] pour audit
          // et pour la future migration vers un lien interne « → Découvrir [POI] ».
          ?>
        </div>
      </li>
    <?php endforeach; ?>
  </ul>

  <?php
  // NOTE : crédit sources retiré ici, désormais centralisé dans le footer global
  // (templates/layout/footer.php → bloc .site-footer__sources). Cela évite
  // la duplication entre pages station/ligne/etc. qui utilisent toutes les
  // mêmes sources ouvertes (IDFM, BAN, Wikidata, Wikipedia, Commons).
  ?>

</section>
