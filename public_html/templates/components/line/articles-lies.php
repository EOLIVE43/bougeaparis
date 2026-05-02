<?php
/**
 * Section Articles & actualités liés — Page ligne de métro
 *
 * Affiche les derniers articles du blog liés à la ligne (filtrage par tag/catégorie).
 * Format : 1 article featured + 3 articles secondaires + CTA "Tous les articles"
 *
 * Variables attendues :
 * - $line : array, données de la ligne (incluant 'related_articles' et 'intros.articles_lies')
 *
 * Stratégie SEO :
 * - Maillage interne fort (page hub → articles)
 * - Date de publication visible (signal de fraîcheur)
 * - Schema.org Article potentiellement à ajouter pour chaque card
 *
 * Stratégie Discover :
 * - Articles frais auto-affichés (page jamais "vieille")
 * - Images 16:9 (format Discover)
 * - Auteur + date visible (E-E-A-T)
 */

$articles = $line['related_articles'] ?? null;
if (!$articles || empty($articles)) {
    return;
}

$introText = $line['intros']['articles_lies'] ?? null;

// Séparation : article featured (premier) + secondaires (les autres)
$featured = $articles[0];
$secondary = array_slice($articles, 1, 3); // max 3 articles secondaires
?>

<section class="section section--articles" id="articles" aria-labelledby="articles-title">

  <h2 id="articles-title">Articles et actualités sur la ligne <?= htmlspecialchars($line['code']) ?></h2>

  <!-- Intro -->
  <div class="articles__intro">
    <?php if ($introText): ?>
      <p><?= $introText ?></p>
    <?php else: ?>
      <p>Restez informé de l'actualité de la <strong>ligne <?= htmlspecialchars($line['code']) ?> du métro parisien</strong>.</p>
    <?php endif; ?>
  </div>

  <div class="articles__grid">

    <!-- Article featured (en grand, à gauche) -->
    <article class="article-card article-card--featured">
      <a href="<?= htmlspecialchars($featured['url']) ?>" class="article-card__link">
        <div class="article-card__image-wrap">
          <div class="article-card__image" style="background: linear-gradient(135deg, <?= htmlspecialchars($featured['category_color']) ?>15 0%, <?= htmlspecialchars($featured['category_color']) ?>30 100%);">
            <span class="article-card__placeholder-icon" aria-hidden="true">📰</span>
          </div>
          <span class="article-card__category" style="background: <?= htmlspecialchars($featured['category_color']) ?>;">
            <?= htmlspecialchars($featured['category']) ?>
          </span>
        </div>
        <div class="article-card__content">
          <h3 class="article-card__title"><?= htmlspecialchars($featured['title']) ?></h3>
          <p class="article-card__excerpt"><?= htmlspecialchars($featured['excerpt']) ?></p>
          <div class="article-card__meta">
            <span class="article-card__author">Par <strong><?= htmlspecialchars($featured['author']) ?></strong></span>
            <span class="article-card__separator" aria-hidden="true">·</span>
            <time class="article-card__date" datetime="<?= htmlspecialchars($featured['published_at']) ?>">
              <?= htmlspecialchars($featured['published_label']) ?>
            </time>
            <span class="article-card__separator" aria-hidden="true">·</span>
            <span class="article-card__reading-time"><?= htmlspecialchars($featured['reading_time']) ?> min</span>
          </div>
        </div>
      </a>
    </article>

    <!-- Articles secondaires (à droite, 3 max) -->
    <div class="articles__secondary">
      <?php foreach ($secondary as $article): ?>
        <article class="article-card article-card--secondary">
          <a href="<?= htmlspecialchars($article['url']) ?>" class="article-card__link">
            <div class="article-card__image-wrap">
              <div class="article-card__image" style="background: linear-gradient(135deg, <?= htmlspecialchars($article['category_color']) ?>15 0%, <?= htmlspecialchars($article['category_color']) ?>30 100%);">
                <span class="article-card__placeholder-icon" aria-hidden="true">📰</span>
              </div>
              <span class="article-card__category" style="background: <?= htmlspecialchars($article['category_color']) ?>;">
                <?= htmlspecialchars($article['category']) ?>
              </span>
            </div>
            <div class="article-card__content">
              <h3 class="article-card__title"><?= htmlspecialchars($article['title']) ?></h3>
              <div class="article-card__meta">
                <time class="article-card__date" datetime="<?= htmlspecialchars($article['published_at']) ?>">
                  <?= htmlspecialchars($article['published_label']) ?>
                </time>
                <span class="article-card__separator" aria-hidden="true">·</span>
                <span class="article-card__reading-time"><?= htmlspecialchars($article['reading_time']) ?> min</span>
              </div>
            </div>
          </a>
        </article>
      <?php endforeach; ?>
    </div>

  </div>

  <!-- CTA voir tous les articles -->
  <div class="articles__cta">
    <div class="articles__cta-icon" aria-hidden="true">📚</div>
    <div class="articles__cta-content">
      <div class="articles__cta-label">Tous les articles</div>
      <div class="articles__cta-title">Retrouvez tous nos articles, conseils et actualités sur la ligne <?= htmlspecialchars($line['code']) ?></div>
    </div>
    <a href="/blog/?ligne=<?= htmlspecialchars($line['code']) ?>" class="articles__cta-btn">Voir tous les articles →</a>
  </div>

</section>
