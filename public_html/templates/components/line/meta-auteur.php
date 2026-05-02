<?php
/**
 * Section Meta auteur + dates — Page ligne de métro
 *
 * Signature E-E-A-T (Expertise, Experience, Authoritativeness, Trustworthiness)
 * - Auteur principal (Ludo) avec bio + lien profil
 * - Co-auteur (Élodie) si elle a contribué
 * - Dates : publié + dernière mise à jour
 * - Sources et références
 * - Schema.org Person + Article pour rich snippets
 *
 * Variables attendues :
 * - $line : array, données de la ligne (incluant 'meta')
 *
 * Stratégie SEO :
 * - Schema.org Person + Article = E-E-A-T
 * - Auteurs nommés = trust signal Google
 * - Sources externes = vérifiabilité
 * - Dates = fraîcheur
 */

$meta = $line['meta'] ?? null;
if (!$meta || empty($meta['primary_author'])) {
    return;
}

$primary = $meta['primary_author'];
$coAuthor = $meta['co_author'] ?? null;
$dates = $meta['dates'] ?? null;
$sources = $meta['sources'] ?? [];
?>

<section class="section section--meta" id="meta" aria-labelledby="meta-title">

  <div class="meta__inner">

    <!-- Auteur principal -->
    <div class="meta-author">
      <a href="<?= htmlspecialchars($primary['url']) ?>" class="meta-author__avatar" aria-label="Voir le profil de <?= htmlspecialchars($primary['name']) ?>">
        <?php if (!empty($primary['avatar_svg'])): ?>
          <img src="<?= htmlspecialchars($primary['avatar_svg']) ?>" alt="" class="meta-author__avatar-img" width="80" height="80" loading="lazy">
        <?php else: ?>
          <span class="meta-author__avatar-initials" style="background:<?= htmlspecialchars($primary['avatar_color']) ?>;">
            <?= htmlspecialchars($primary['avatar_initials']) ?>
          </span>
        <?php endif; ?>
      </a>

      <div class="meta-author__content">
        <div class="meta-author__header">
          <a href="<?= htmlspecialchars($primary['url']) ?>" class="meta-author__name">
            <?= htmlspecialchars($primary['full_name']) ?>
          </a>
          <span class="meta-author__role"><?= htmlspecialchars($primary['role']) ?></span>
        </div>

        <p class="meta-author__bio"><?= htmlspecialchars($primary['bio']) ?></p>

        <?php if (!empty($primary['expertise_tags'])): ?>
          <div class="meta-author__tags">
            <?php foreach ($primary['expertise_tags'] as $tag): ?>
              <span class="meta-tag"><?= htmlspecialchars($tag) ?></span>
            <?php endforeach; ?>
          </div>
        <?php endif; ?>

        <a href="<?= htmlspecialchars($primary['url']) ?>" class="meta-author__profile-link">
          Voir le profil de <?= htmlspecialchars($primary['name']) ?> →
        </a>
      </div>
    </div>

    <!-- Co-auteur Élodie (compact) -->
    <?php if ($coAuthor): ?>
      <div class="meta-coauthor">
        <span class="meta-coauthor__label">Avec la contribution de&nbsp;:</span>
        <a href="<?= htmlspecialchars($coAuthor['url']) ?>" class="meta-coauthor__link">
          <span class="meta-coauthor__avatar">
            <?php if (!empty($coAuthor['avatar_svg'])): ?>
              <img src="<?= htmlspecialchars($coAuthor['avatar_svg']) ?>" alt="<?= htmlspecialchars($coAuthor['name']) ?>" class="meta-coauthor__avatar-img" width="28" height="28" loading="lazy">
            <?php else: ?>
              <span class="meta-coauthor__avatar-initials" style="background:<?= htmlspecialchars($coAuthor['avatar_color']) ?>;">
                <?= htmlspecialchars($coAuthor['avatar_initials']) ?>
              </span>
            <?php endif; ?>
          </span>
          <span class="meta-coauthor__name"><?= htmlspecialchars($coAuthor['full_name']) ?></span>
        </a>
        <span class="meta-coauthor__role"><?= htmlspecialchars($coAuthor['role']) ?></span>
        <?php if (!empty($coAuthor['contributed_sections'])): ?>
          <span class="meta-coauthor__sections">
            (<?= htmlspecialchars(implode(', ', $coAuthor['contributed_sections'])) ?>)
          </span>
        <?php endif; ?>
      </div>
    <?php endif; ?>

    <!-- Dates -->
    <?php if ($dates): ?>
      <div class="meta-dates">
        <?php if (!empty($dates['published'])): ?>
          <div class="meta-date">
            <span class="meta-date__icon" aria-hidden="true">📝</span>
            <span class="meta-date__label">Publié le</span>
            <time datetime="<?= htmlspecialchars($dates['published']) ?>" class="meta-date__value"><?= htmlspecialchars($dates['published_label']) ?></time>
          </div>
        <?php endif; ?>
        <?php if (!empty($dates['updated'])): ?>
          <div class="meta-date">
            <span class="meta-date__icon" aria-hidden="true">🔄</span>
            <span class="meta-date__label">Dernière mise à jour rédactionnelle</span>
            <time datetime="<?= htmlspecialchars($dates['updated']) ?>" class="meta-date__value"><?= htmlspecialchars($dates['updated_label']) ?></time>
          </div>
        <?php endif; ?>
        <?php if (!empty($dates['live_data_note'])): ?>
          <div class="meta-date meta-date--live">
            <span class="meta-date__icon meta-date__icon--pulse" aria-hidden="true"></span>
            <span class="meta-date__label"><?= htmlspecialchars($dates['live_data_note']) ?></span>
          </div>
        <?php endif; ?>
      </div>
    <?php endif; ?>

    <!-- Sources -->
    <?php if (!empty($sources)): ?>
      <div class="meta-sources">
        <div class="meta-sources__title">📚 Sources et références</div>
        <ul class="meta-sources__list">
          <?php foreach ($sources as $source): ?>
            <li>
              <a href="<?= htmlspecialchars($source['url']) ?>" rel="noopener noreferrer" target="_blank">
                <?= htmlspecialchars($source['label']) ?>
                <span aria-hidden="true">↗</span>
              </a>
            </li>
          <?php endforeach; ?>
        </ul>
      </div>
    <?php endif; ?>

    <!-- Disclaimer site non officiel -->
    <div class="meta-disclaimer">
      <span class="meta-disclaimer__icon" aria-hidden="true">ℹ️</span>
      <p>
        <strong>BougeàParis.fr</strong> est un site indépendant non officiel, non affilié à la RATP, à Île-de-France Mobilités ou à la SNCF Transilien. 
        Les données affichées sont issues des API et données ouvertes officielles. Pour toute information officielle, consultez les sites de ces opérateurs.
      </p>
    </div>

  </div>

</section>

<!-- Schema.org : Article + Person pour E-E-A-T et rich snippets -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Métro Ligne <?= htmlspecialchars($line['code']) ?> Paris : plan, stations, horaires et trafic en temps réel",
  "datePublished": "<?= htmlspecialchars($dates['published'] ?? '') ?>",
  "dateModified": "<?= htmlspecialchars($dates['updated'] ?? '') ?>",
  "author": [
    {
      "@type": "Person",
      "name": "<?= htmlspecialchars($primary['full_name']) ?>",
      "url": "https://bougeaparis.fr<?= htmlspecialchars($primary['url']) ?>",
      "description": "<?= htmlspecialchars($primary['role']) ?>"
    }<?php if ($coAuthor): ?>,
    {
      "@type": "Person",
      "name": "<?= htmlspecialchars($coAuthor['full_name']) ?>",
      "url": "https://bougeaparis.fr<?= htmlspecialchars($coAuthor['url']) ?>",
      "description": "<?= htmlspecialchars($coAuthor['role']) ?>"
    }<?php endif; ?>
  ],
  "publisher": {
    "@type": "Organization",
    "name": "BougeàParis.fr",
    "url": "https://bougeaparis.fr",
    "logo": {
      "@type": "ImageObject",
      "url": "https://bougeaparis.fr/assets/images/logo-512.png"
    }
  }
}
</script>
