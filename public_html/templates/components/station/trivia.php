<?php
/**
 * Composant : Section "Le saviez-vous" (page station)
 *
 * Grille de cards avec anecdotes verifiees sur la station (origine du nom,
 * records, faits architecturaux, etc.). Chaque card a une icone (emoji ou
 * SVG inline), un titre court et un paragraphe factuel.
 *
 * Variables attendues :
 *   $trivia      : array d'objets { icon, title, content }
 *   $stationName : string, nom court de la station (pour le H2)
 *
 * Si trivia vide ou absent : ne rend rien (graceful).
 *
 * @package BougeaParis\Templates\Components\Station
 */

$trivia      = $props['trivia']      ?? [];
$stationName = $props['stationName'] ?? '';

if (empty($trivia) || !is_array($trivia)) {
    return;
}
?>

<section class="station-section section-trivia" id="trivia" aria-labelledby="trivia-heading">
  <h2 id="trivia-heading">Le saviez-vous sur <?= Template::e($stationName) ?> ?</h2>

  <div class="trivia-grid">
    <?php foreach ($trivia as $item): ?>
      <?php
        $icon    = $item['icon']    ?? '';
        $title   = $item['title']   ?? '';
        $content = $item['content'] ?? '';
        if ($title === '' || $content === '') continue;
      ?>
      <article class="trivia-card">
        <?php if ($icon !== ''): ?>
          <div class="trivia-icon" aria-hidden="true"><?= Template::e($icon) ?></div>
        <?php endif; ?>
        <h3 class="trivia-title"><?= Template::e($title) ?></h3>
        <p class="trivia-content"><?= Template::e($content) ?></p>
      </article>
    <?php endforeach; ?>
  </div>
</section>
