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
 */

$pois = $line['points_of_interest'] ?? null;
if (!$pois) {
    return; // Pas de POI définis pour cette ligne
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
.poi-card__credit {
    margin-top: 0.5rem;
    padding-top: 0.5rem;
    border-top: 1px solid var(--color-border, #E0E6E4);
    font-size: 0.75rem;
    color: var(--color-text-muted, #5A6B66);
    line-height: 1.4;
}
.poi-card__credit a {
    color: var(--color-text-muted, #5A6B66);
    text-decoration: underline;
    text-decoration-color: rgba(90, 107, 102, 0.3);
}
.poi-card__credit a:hover {
    color: var(--color-primary, #0F6E56);
    text-decoration-color: currentColor;
}
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
        <span class="theme-section__icon" aria-hidden="true"><?= htmlspecialchars($theme['icon']) ?></span>
        <h3 class="theme-section__title">
          <?= htmlspecialchars(str_replace('{code}', $line['code'], $theme['title_template'])) ?>
        </h3>
        <span class="theme-section__count"><?= count($theme['items']) ?> lieux</span>
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
          <article class="poi-card <?= $hasImage ? 'poi-card--with-image' : '' ?>" itemscope itemtype="https://schema.org/<?= htmlspecialchars($poi['schema_type']) ?>">

            <?php if ($hasImage): ?>
              <!-- Photo réelle (Wikimedia, optimisée Discover 1200x675) -->
              <div class="poi-card__image poi-card__image--photo">
                <img src="<?= htmlspecialchars($poi['image']['src']) ?>"
                     alt="<?= htmlspecialchars($poi['image']['alt'] ?? $poi['name']) ?>"
                     width="<?= htmlspecialchars($poi['image']['width'] ?? 1200) ?>"
                     height="<?= htmlspecialchars($poi['image']['height'] ?? 675) ?>"
                     loading="lazy"
                     decoding="async"
                     itemprop="image">
              </div>
            <?php else: ?>
              <!-- Fallback : emoji thématique sur gradient coloré -->
              <div class="poi-card__image" style="background: <?= htmlspecialchars($theme['color_gradient']) ?>;">
                <span class="poi-card__icon" aria-hidden="true"><?= htmlspecialchars($poi['icon']) ?></span>
              </div>
            <?php endif; ?>

            <div class="poi-card__content">
              <div class="poi-card__name" itemprop="name">
                <?= conditionalLink($poiUrl, htmlspecialchars($poi['name']), 'poi-card__name-link') ?>
              </div>
              <div class="poi-card__desc" itemprop="description"><?= htmlspecialchars($poi['description']) ?></div>
              <div class="poi-card__station">
                <span class="poi-card__station-icon" aria-hidden="true">🚇</span>
                <span>Station&nbsp;: <span class="poi-card__station-name"><?= htmlspecialchars($poi['station']) ?></span></span>
              </div>
              <?php if ($hasImage && !empty($poi['image']['credit']['author'])): ?>
                <div class="poi-card__credit">
                  Photo&nbsp;:
                  <?php if (!empty($poi['image']['credit']['wikimedia_url'])): ?>
                    <a href="<?= htmlspecialchars($poi['image']['credit']['wikimedia_url']) ?>" rel="nofollow noopener" target="_blank">
                      <?= htmlspecialchars($poi['image']['credit']['author']) ?>
                    </a>
                  <?php else: ?>
                    <?= htmlspecialchars($poi['image']['credit']['author']) ?>
                  <?php endif; ?>
                  <?php if (!empty($poi['image']['credit']['license'])): ?>
                    · <?= htmlspecialchars($poi['image']['credit']['license']) ?>
                  <?php endif; ?>
                </div>
              <?php endif; ?>
            </div>

          </article>
        <?php endforeach; ?>
      </div>

    </div>
  <?php endforeach; ?>

</section>
