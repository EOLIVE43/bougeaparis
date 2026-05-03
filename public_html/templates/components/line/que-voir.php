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
 * Architecture :
 * - Lit l'intro depuis $line['intros']['que_voir'] (avec fallback)
 * - Affiche les thèmes depuis $line['points_of_interest']
 * - Chaque card POI = lien sur le NOM uniquement (pas sur toute la card)
 * - Smart linking : si la page POI/catégorie n'existe pas (cf. Routes::active),
 *   le titre devient un <span> non cliquable. Évite les liens 404.
 */

$pois = $line['points_of_interest'] ?? null;
if (!$pois) {
    return; // Pas de POI définis pour cette ligne
}

$introText = $line['intros']['que_voir'] ?? null;
?>

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
          // URL de la page POI individuelle (peut ne pas exister encore)
          $poiUrl = $theme['category_url'] . $poi['slug'] . '/';
        ?>
          <article class="poi-card" itemscope itemtype="https://schema.org/<?= htmlspecialchars($poi['schema_type']) ?>">

            <div class="poi-card__image" style="background: <?= htmlspecialchars($theme['color_gradient']) ?>;">
              <span class="poi-card__icon" aria-hidden="true"><?= htmlspecialchars($poi['icon']) ?></span>
            </div>

            <div class="poi-card__content">
              <div class="poi-card__name" itemprop="name">
                <?= conditionalLink($poiUrl, htmlspecialchars($poi['name']), 'poi-card__name-link') ?>
              </div>
              <div class="poi-card__desc" itemprop="description"><?= htmlspecialchars($poi['description']) ?></div>
              <div class="poi-card__station">
                <span class="poi-card__station-icon" aria-hidden="true">🚇</span>
                <span>Station&nbsp;: <span class="poi-card__station-name"><?= htmlspecialchars($poi['station']) ?></span></span>
              </div>
            </div>

          </article>
        <?php endforeach; ?>
      </div>

    </div>
  <?php endforeach; ?>

</section>
