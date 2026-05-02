<?php
/**
 * Section Introduction SEO — Texte riche, dense en mots-clés
 *
 * Lit le texte personnalisé depuis $line['intros']['introduction'].
 * Avec fallback générique si non défini (sécurité industrialisation).
 *
 * Variables attendues :
 * - $line : array, données de la ligne
 */

$introHtml = $line['intros']['introduction'] ?? null;
$introTitle = $line['intros']['introduction_title'] ?? 'au cœur du métro parisien';

// Fallback générique si pas de texte custom
if (!$introHtml) {
    $code = htmlspecialchars($line['code']);
    $terminusA = htmlspecialchars($line['terminus_a']);
    $terminusB = htmlspecialchars($line['terminus_b']);
    $stationsCount = htmlspecialchars($line['stations_count']);
    $introHtml = "<p>La <strong>ligne {$code} du métro de Paris</strong> traverse la capitale en desservant <strong>{$stationsCount} stations</strong> entre <strong>{$terminusA}</strong> et <strong>{$terminusB}</strong>. Elle assure des correspondances majeures avec les autres lignes du métro parisien, RER et tramways.</p>";
}
?>

<section class="intro-seo" aria-labelledby="intro-title">

  <h2 id="intro-title" class="intro-seo__title">
    La ligne <?= htmlspecialchars($line['code']) ?>, <?= htmlspecialchars($introTitle) ?>
  </h2>

  <div class="intro-seo__content">
    <?= $introHtml ?>

    <p class="intro-seo__navigation">
      Sur cette page, retrouvez le <a href="#plan-visuel">plan complet de la ligne <?= htmlspecialchars($line['code']) ?></a>, les <a href="#horaires">horaires</a>, le <a href="#trafic-temps-reel">trafic en temps réel</a>, le <a href="#stations-table">détail des correspondances par station</a> et les <a href="#que-voir">incontournables touristiques</a>.
    </p>
  </div>

</section>
