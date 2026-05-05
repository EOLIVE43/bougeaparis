<?php
/**
 * Composant : Paragraphe SEO statique trafic (page station)
 *
 * S'affiche EN PERMANENCE sous le bloc trafic-temps-reel, indépendamment
 * de l'état du trafic. Objectif : permettre à la page de ranker sur des
 * requêtes "trafic", "perturbation", "incident métro {station}" même quand
 * aucune perturbation n'est active.
 *
 * Variables attendues :
 *   $stationName : string, nom de la station (ex. "Châtelet")
 *   $lines       : array, soit liste de codes ("1", "4", ...) soit liste
 *                  d'objets avec clé 'code'. Le composant accepte les deux.
 *
 * Si $stationName ou $lines vides, le composant ne s'affiche pas (graceful).
 *
 * @package BougeaParis\Templates\Components\Station
 * @since Livraison 8 (SEO statique trafic)
 */

$stationName = $props['stationName'] ?? null;
$lines       = $props['lines']       ?? [];

if (!$stationName || empty($lines)) return;

// Normaliser : accepte soit ["1","4",...] soit [{"code":"1"},...]
$codes = [];
foreach ($lines as $line) {
    if (is_array($line) && !empty($line['code'])) {
        $codes[] = (string)$line['code'];
    } elseif (is_string($line) && $line !== '') {
        $codes[] = $line;
    }
}
$codes = array_values(array_unique($codes));
if (empty($codes)) return;

// Formate "1, 4, 7, 11 et 14" (virgules sauf dernier "et X")
$formatLines = function (array $c): string {
    if (count($c) === 1) return $c[0];
    if (count($c) === 2) return $c[0] . ' et ' . $c[1];
    $last = array_pop($c);
    return implode(', ', $c) . ' et ' . $last;
};
$linesList = $formatLines($codes);
$nbLines   = count($codes);
?>

<section class="trafic-info-seo" aria-labelledby="trafic-seo-title">
  <h2 id="trafic-seo-title" class="trafic-info-seo__title">
    Info trafic en temps réel à <?= e($stationName) ?>
  </h2>
  <p class="trafic-info-seo__lead">
    Cette page affiche en direct l'état du trafic sur les
    <strong><?= (int)$nbLines ?> lignes du métro</strong>
    desservant la station <strong><?= e($stationName) ?></strong> :
    lignes <?= e($linesList) ?>.
    En cas de <strong>perturbation</strong>, panne de signalisation,
    incident technique ou travaux, le détail s'affiche au-dessus avec la
    liste précise des lignes concernées et le motif de l'incident.
  </p>
  <p class="trafic-info-seo__lead">
    Pour <strong>anticiper vos trajets</strong>, pensez à consulter cette page
    avant de quitter votre domicile, surtout aux heures de pointe.
  </p>
</section>
