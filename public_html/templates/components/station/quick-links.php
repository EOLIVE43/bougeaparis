<?php
/**
 * Composant : Barre de raccourcis (page station)
 *
 * Affiche 6 raccourcis horizontaux sous le hero, ordre stratégique du plus
 * urgent au plus exploratoire :
 *   ⚠️ Trafic        → #trafic
 *   🚪 Sorties       → #sorties
 *   🗺️ Plan         → #plan
 *   🕐 Horaires      → #horaires
 *   🔄 Correspondances → #correspondances
 *   🏛️ Que voir     → #poi-nearby
 *
 * Le bouton Trafic affiche un indicateur de couleur selon l'état du réseau
 * (badge ✓ si normal, badge nombre de lignes impactées si perturbé).
 *
 * Variables attendues :
 *   $disruptionsCount : int, nombre de lignes desservant la station impactées
 *                       par une perturbation (0 = trafic normal, >0 = alerte).
 *                       Si null/absent → pas de badge (cas API down).
 *   $hasExits         : bool, true si la station a des sorties
 *   $hasPois          : bool, true si la station a des POIs
 *   $hasFaq           : bool, ignoré ici (FAQ pas dans la barre par spec)
 *
 * Affichage responsive : flex sur tablet/desktop, scroll horizontal sur mobile
 * (touch-friendly, pas de wrap pour garder une barre visuelle compacte).
 *
 * @package BougeaParis\Templates\Components\Station
 * @since Livraison 10 (quick links)
 */

$disruptionsCount = $props['disruptionsCount'] ?? null; // null = inconnu (API down)
$hasExits         = (bool)($props['hasExits']  ?? false);
$hasPois          = (bool)($props['hasPois']   ?? false);
// hasFaq fourni mais non utilisé : la spec ne demande pas de raccourci FAQ.

// Etat du raccourci Trafic
$trafficAlert = is_int($disruptionsCount) && $disruptionsCount > 0;
$trafficClass = 'quick-link';
$trafficBadge = '';
if ($trafficAlert) {
    $trafficClass .= ' quick-link--alert';
    $trafficBadge = '<span class="quick-link__badge quick-link__badge--alert" aria-label="' .
                    (int)$disruptionsCount . ' ligne' . ($disruptionsCount > 1 ? 's' : '') .
                    ' impactée' . ($disruptionsCount > 1 ? 's' : '') . '">' .
                    (int)$disruptionsCount . '</span>';
} elseif ($disruptionsCount === 0) {
    $trafficBadge = '<span class="quick-link__badge quick-link__badge--ok" aria-label="Trafic normal">✓</span>';
}
// Si $disruptionsCount === null : pas de badge

// Construction des raccourcis (filtrés par disponibilité)
$links = [];

$links[] = [
    'href'    => '#trafic',
    'icon'    => '⚠️',
    'label'   => 'Trafic',
    'class'   => $trafficClass,
    'badge'   => $trafficBadge,
    'visible' => true, // toujours affiché (banner normal ou bloc perturbation)
];

$links[] = [
    'href'    => '#sorties',
    'icon'    => '🚪',
    'label'   => 'Sorties',
    'class'   => 'quick-link',
    'badge'   => '',
    'visible' => $hasExits,
];

$links[] = [
    'href'    => '#plan',
    'icon'    => '🗺️',
    'label'   => 'Plan',
    'class'   => 'quick-link',
    'badge'   => '',
    'visible' => $hasExits || $hasPois, // le plan exige des points à afficher
];

$links[] = [
    'href'    => '#horaires',
    'icon'    => '🕐',
    'label'   => 'Horaires',
    'class'   => 'quick-link',
    'badge'   => '',
    'visible' => true, // les horaires viennent des JSON ligne, toujours dispo
];

$links[] = [
    'href'    => '#correspondances',
    'icon'    => '🔄',
    'label'   => 'Correspondances',
    'class'   => 'quick-link',
    'badge'   => '',
    'visible' => true, // section toujours rendue
];

$links[] = [
    'href'    => '#poi-nearby',
    'icon'    => '🏛️',
    'label'   => 'Que voir',
    'class'   => 'quick-link',
    'badge'   => '',
    'visible' => $hasPois,
];

// Filtrer les visibles
$visibleLinks = array_values(array_filter($links, fn($l) => $l['visible']));
if (count($visibleLinks) <= 1) return; // pas de barre si un seul raccourci dispo
?>

<nav class="quick-links" aria-label="Raccourcis vers les sections de la page">
  <ul class="quick-links__list" role="list">
    <?php foreach ($visibleLinks as $link): ?>
      <li class="quick-links__item">
        <a href="<?= e($link['href']) ?>" class="<?= e($link['class']) ?>">
          <span class="quick-link__icon" aria-hidden="true"><?= e($link['icon']) ?></span>
          <span class="quick-link__label"><?= e($link['label']) ?></span>
          <?= $link['badge'] /* déjà échappé en amont, contenu controlé */ ?>
        </a>
      </li>
    <?php endforeach; ?>
  </ul>
</nav>
