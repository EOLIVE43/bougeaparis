<?php
/**
 * Section Histoire — Page ligne de métro
 *
 * Affiche l'histoire de la ligne sous forme éditoriale :
 * - Intro narrative
 * - Chiffres clés (4 cards visuelles)
 * - Timeline des dates importantes
 * - Anecdotes / faits méconnus
 * - Lien vers article approfondi
 *
 * Variables attendues :
 * - $line : array, données de la ligne (incluant 'history' et 'intros.histoire')
 *
 * Architecture SEO + Discover :
 * - H2 unique avec "ligne X"
 * - H3 "Chiffres clés", "Dates marquantes", "Anecdotes"
 * - Schema.org : pas de schéma spécifique mais structure sémantique forte
 * - Storytelling = signal Discover fort
 */

$history = $line['history'] ?? null;
if (!$history) {
    return; // Pas de données historiques
}

$introText = $line['intros']['histoire'] ?? null;
?>

<section class="section section--histoire" id="histoire" aria-labelledby="histoire-title">

  <h2 id="histoire-title">Histoire de la ligne <?= htmlspecialchars($line['code']) ?> du métro parisien</h2>

  <!-- Intro narrative -->
  <div class="histoire__intro">
    <?php if ($introText): ?>
      <p><?= $introText ?></p>
    <?php else: ?>
      <p>L'histoire de la <strong>ligne <?= htmlspecialchars($line['code']) ?> du métro parisien</strong> est intimement liée à celle de la capitale française, témoin vivant de l'évolution de Paris depuis l'ouverture du réseau métropolitain.</p>
    <?php endif; ?>
  </div>

  <!-- Chiffres clés -->
  <h3 class="histoire__subtitle">La ligne <?= htmlspecialchars($line['code']) ?> en chiffres</h3>
  <div class="histoire__key-facts">
    <?php foreach ($history['key_facts'] as $fact): ?>
      <div class="key-fact">
        <div class="key-fact__value"><?= htmlspecialchars($fact['value']) ?></div>
        <div class="key-fact__label"><?= htmlspecialchars($fact['label']) ?></div>
        <div class="key-fact__desc"><?= htmlspecialchars($fact['description']) ?></div>
      </div>
    <?php endforeach; ?>
  </div>

  <!-- Timeline des dates -->
  <h3 class="histoire__subtitle">Les dates clés de la ligne <?= htmlspecialchars($line['code']) ?></h3>
  <div class="histoire__timeline">
    <?php foreach ($history['key_dates'] as $i => $date): ?>
      <article class="timeline-event">
        <div class="timeline-event__year-wrap">
          <div class="timeline-event__year"><?= htmlspecialchars($date['year']) ?></div>
          <div class="timeline-event__line" aria-hidden="true"></div>
        </div>
        <div class="timeline-event__content">
          <div class="timeline-event__icon" aria-hidden="true"><?= htmlspecialchars($date['icon']) ?></div>
          <h4 class="timeline-event__title"><?= htmlspecialchars($date['title']) ?></h4>
          <p class="timeline-event__desc"><?= htmlspecialchars($date['description']) ?></p>
        </div>
      </article>
    <?php endforeach; ?>
  </div>

  <!-- Anecdotes -->
  <?php if (!empty($history['anecdotes'])): ?>
    <h3 class="histoire__subtitle">Anecdotes et faits méconnus de la ligne <?= htmlspecialchars($line['code']) ?></h3>
    <div class="histoire__anecdotes">
      <?php foreach ($history['anecdotes'] as $anecdote): ?>
        <div class="anecdote">
          <div class="anecdote__title"><?= htmlspecialchars($anecdote['title']) ?></div>
          <p class="anecdote__desc"><?= htmlspecialchars($anecdote['description']) ?></p>
        </div>
      <?php endforeach; ?>
    </div>
  <?php endif; ?>

  <!-- Lien vers article approfondi -->
  <?php if (!empty($history['article_url'])): ?>
    <div class="histoire__article-link">
      <div class="histoire__article-link-icon" aria-hidden="true">📖</div>
      <div class="histoire__article-link-content">
        <div class="histoire__article-link-label">Article approfondi</div>
        <div class="histoire__article-link-title">L'histoire complète de la ligne <?= htmlspecialchars($line['code']) ?> du métro parisien</div>
      </div>
      <a href="<?= htmlspecialchars($history['article_url']) ?>" class="histoire__article-link-cta">Lire l'article →</a>
    </div>
  <?php endif; ?>

</section>
