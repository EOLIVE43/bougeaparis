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

// Garde réelle : skip si aucun item n'a title ET content non vides (stubs
// auto-bootstrap = tous les champs en ''). Évite un H2 orphelin "Le saviez-vous"
// suivi d'une grille vide.
$_triviaHasContent = false;
foreach ($trivia as $_item) {
    if (is_array($_item)
        && trim((string)($_item['title']   ?? '')) !== ''
        && trim((string)($_item['content'] ?? '')) !== '') {
        $_triviaHasContent = true;
        break;
    }
}
if (!$_triviaHasContent) return;
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
        <p class="trivia-content"><?= richText($content) ?></p>
      </article>
    <?php endforeach; ?>
  </div>
</section>
