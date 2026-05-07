<?php
/**
 * Section Que voir — Page ligne de métro
 *
 * Affiche les points d'intérêt touristiques le long de la ligne,
 * regroupés par thème (monuments, musées, jardins, quartiers).
 *
 * Variables attendues :
 * - $line : array, données de la ligne (incluant points_of_interest)
 *
 * v1.4.3 — Gestion des images :
 * - Si le POI a un champ 'image' (enrichi par fetch-poi-images.php) → affiche la photo
 * - Sinon, fallback sur l'emoji 'icon' avec gradient coloré
 * - Schema.org Article requiert un champ 'image' → on l'ajoute si dispo
 * - Attribution Wikimedia obligatoire pour CC BY-SA → affichée discrètement
 *
 * v1.4.6 — Filtrage POI skippés :
 * - Les POI marqués `skip: true` dans /data/poi-overrides.json sont retirés de la liste
 *   avant l'affichage. Le compteur "X lieux" est mis à jour automatiquement.
 */

$pois = $line['points_of_interest'] ?? null;
if (!$pois) {
    return; // Pas de POI définis pour cette ligne
}

// v1.4.6 : Charger les overrides POI (poi-overrides.json) et retirer les POI marqués skip:true
$overridesFile = __DIR__ . '/../../../data/poi-overrides.json';
$skipSlugs = [];
$overrides = [];
if (file_exists($overridesFile)) {
    $overridesParsed = json_decode(file_get_contents($overridesFile), true);
    if (is_array($overridesParsed)) {
        $overrides = $overridesParsed;
        foreach ($overridesParsed as $slug => $cfg) {
            if (is_array($cfg) && !empty($cfg['skip'])) {
                $skipSlugs[] = $slug;
            }
        }
    }
}
if (!empty($skipSlugs)) {
    foreach ($pois as $themeKey => &$theme) {
        if (!isset($theme['items'])) continue;
        $theme['items'] = array_values(array_filter(
            $theme['items'],
            fn($poi) => !in_array($poi['slug'] ?? '', $skipSlugs, true)
        ));
    }
    unset($theme);
}

// v2.0.0 : résolution registry-aware. Si un POI est marqué shared_asset
// dans poi-overrides.json, on force son image.src vers /assets/images/poi/shared/...
// même si le JSON ligne n'a pas encore été ré-écrit par le workflow Fetch POI.
// Le template devient ainsi self-sufficient : page propre dès que les fichiers
// /shared/ sont en place + le registry à jour, sans attendre le re-fetch.
$registryFile = __DIR__ . '/../../../data/poi-registry.json';
$poiRegistry = [];
if (file_exists($registryFile)) {
    $regParsed = json_decode(file_get_contents($registryFile), true);
    if (is_array($regParsed)) {
        $poiRegistry = $regParsed['pois'] ?? [];
    }
}
if (!empty($overrides) && !empty($poiRegistry)) {
    foreach ($pois as $themeKey => &$theme) {
        if (!isset($theme['items'])) continue;
        foreach ($theme['items'] as &$poi) {
            $slug = $poi['slug'] ?? '';
            if ($slug === '') continue;
            $cfg = $overrides[$slug] ?? null;
            if (!is_array($cfg) || empty($cfg['shared_asset'])) continue;
            $regKey = $cfg['registry_key'] ?? $slug;
            if (!isset($poiRegistry[$regKey])) continue;
            $entry = $poiRegistry[$regKey];
            // Override l'image avec la version shared canonique (même si le JSON
            // ligne pointait vers l'ancien path /poi/{theme}/{slug}.webp).
            $ws = $entry['wikimedia_source'] ?? [];
            $poi['image'] = [
                'src'    => '/assets/images/poi/' . ($entry['asset']  ?? "shared/$slug.webp"),
                'thumb'  => '/assets/images/poi/' . ($entry['thumb']  ?? "shared/$slug-thumb.webp"),
                'alt'    => $entry['alt']    ?? ($poi['name'] . ' à Paris'),
                'width'  => $poi['image']['width']  ?? 1200,
                'height' => $poi['image']['height'] ?? 675,
                'credit' => [
                    'author'        => $ws['author']      ?? 'unknown',
                    'license'       => $ws['license']     ?? 'unknown',
                    'license_url'   => $ws['license_url'] ?? '',
                    'wikimedia_url' => $ws['url']         ?? '',
                    'source'        => 'shared_asset (poi-registry)',
                ],
            ];
        }
        unset($poi);
    }
    unset($theme);
}

$introText = $line['intros']['que_voir'] ?? null;

// Détecter s'il y a au moins une photo dans la liste, pour conditionner les styles
$hasAnyImage = false;
foreach ($pois as $theme) {
    foreach ($theme['items'] ?? [] as $poi) {
        if (!empty($poi['image']['src'])) {
            $hasAnyImage = true;
            break 2;
        }
    }
}
?>

<?php if ($hasAnyImage): ?>
<style>
/* v1.4.3 — Styles cards POI avec photos Wikimedia (chargés inline car liés au contenu) */
.poi-card__image--photo {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    background: #f0f4f2;
}
.poi-card__image--photo img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
}
.poi-card--with-image .poi-card__icon { display: none; }
</style>
<?php endif; ?>

<section class="section section--que-voir" id="que-voir" aria-labelledby="que-voir-title">

  <h2 id="que-voir-title">Que voir le long de la ligne <?= htmlspecialchars($line['code']) ?> du métro parisien</h2>

  <div class="que-voir__intro">
    <?php if ($introText): ?>
      <p><?= $introText ?></p>
    <?php else: ?>
      <p>La <strong>ligne <?= htmlspecialchars($line['code']) ?> du métro parisien</strong> dessert plusieurs <strong>sites touristiques</strong> à découvrir le long du parcours. Voici les principaux <strong>monuments, musées et lieux culturels</strong> à visiter, avec pour chacun la station de métro la plus proche.</p>
    <?php endif; ?>
  </div>

  <?php foreach ($pois as $themeKey => $theme): ?>
    <div class="theme-section">

      <!-- Bandeau du thème (titre + lien catégorie) -->
      <div class="theme-section__header">
        <span class="theme-section__icon" aria-hidden="true"><?= htmlspecialchars($theme['icon'] ?? '📍') ?></span>
        <h3 class="theme-section__title">
          <?= htmlspecialchars(str_replace('{code}', $line['code'] ?? '', $theme['title_template'] ?? '')) ?>
        </h3>
        <span class="theme-section__count"><?= count($theme['items'] ?? []) ?> lieux</span>
        <?php
          // "Voir tout" : actif uniquement si la page categorie existe
          $catUrl = $theme['category_url'] ?? '';
          if (!empty($catUrl) && Routes::exists(rtrim($catUrl, '/'))):
        ?>
          <a href="<?= htmlspecialchars($catUrl) ?>" class="theme-section__view-all">
            Voir tout →
          </a>
        <?php endif; ?>
      </div>

      <!-- Cards POI -->
      <div class="poi-cards">
        <?php foreach ($theme['items'] as $poi):
          $poiUrl   = $theme['category_url'] . $poi['slug'] . '/';
          $hasImage = !empty($poi['image']) && !empty($poi['image']['src']);
        ?>
          <article class="poi-card <?= $hasImage ? 'poi-card--with-image' : '' ?>" itemscope itemtype="https://schema.org/<?= htmlspecialchars($poi['schema_type'] ?? 'Place') ?>">

            <?php if ($hasImage): ?>
              <!-- Photo réelle (Wikimedia, optimisée Discover 1200x675).
                   Srcset : mobile sert le thumb 600w (~80KB), desktop sert le full 1200w (~150KB).
                   Économie typique sur mobile : ~50% du poids image. -->
              <?php
                $imgSrc   = $poi['image']['src']                   ?? '';
                $imgThumb = $poi['image']['thumb']                 ?? '';
                $imgAlt   = $poi['image']['alt']                   ?? $poi['name'];
                $imgW     = (int)($poi['image']['width']  ?? 1200);
                $imgH     = (int)($poi['image']['height'] ?? 675);
                $hasThumb = $imgThumb !== '' && $imgThumb !== $imgSrc;
              ?>
              <div class="poi-card__image poi-card__image--photo">
                <img src="<?= htmlspecialchars($imgSrc) ?>"
                     <?php if ($hasThumb): ?>
                     srcset="<?= htmlspecialchars($imgThumb) ?> 600w, <?= htmlspecialchars($imgSrc) ?> 1200w"
                     sizes="(max-width: 768px) 100vw, 380px"
                     <?php endif; ?>
                     alt="<?= htmlspecialchars($imgAlt) ?>"
                     width="<?= $imgW ?>"
                     height="<?= $imgH ?>"
                     loading="lazy"
                     decoding="async"
                     itemprop="image">
              </div>
            <?php else: ?>
              <!-- Fallback : emoji thématique sur gradient coloré -->
              <div class="poi-card__image" style="background: <?= htmlspecialchars($theme['color_gradient'] ?? '#0F6E56') ?>;">
                <span class="poi-card__icon" aria-hidden="true"><?= htmlspecialchars($poi['icon'] ?? '📍') ?></span>
              </div>
            <?php endif; ?>

            <div class="poi-card__content">
              <div class="poi-card__name" itemprop="name">
                <?= conditionalLink($poiUrl, htmlspecialchars($poi['name'] ?? ''), 'poi-card__name-link') ?>
              </div>
              <div class="poi-card__desc" itemprop="description"><?= htmlspecialchars($poi['description'] ?? '') ?></div>
              <div class="poi-card__station">
                <span class="poi-card__station-icon" aria-hidden="true">🚇</span>
                <span>Station&nbsp;: <span class="poi-card__station-name"><?= htmlspecialchars($poi['station'] ?? '') ?></span></span>
              </div>
            </div>

          </article>
        <?php endforeach; ?>
      </div>

    </div>
  <?php endforeach; ?>

  <?php if ($hasAnyImage): ?>
    <p class="que-voir__credits-link">
      Crédits photographiques : <a href="/sources/#credits-photos">voir nos sources →</a>
    </p>
  <?php endif; ?>

</section>
