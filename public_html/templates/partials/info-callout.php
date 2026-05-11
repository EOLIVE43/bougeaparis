<?php
/**
 * Partial : info-callout
 *
 * Encart de mise en avant 💡 "A savoir" ou ⚠️ "Attention" en bordure gauche
 * coloree. Reutilisable sur /tarifs/, /se-deplacer/, /visiter/, /itineraires/.
 *
 * Variables attendues (set par l'appelant via include) :
 *   $icon    (string) : emoji ou texte court ('💡' defaut, '⚠️', etc.)
 *   $variant (string) : 'info' (defaut, bleu clair) | 'warning' (orange)
 *   $label   (string) : libelle gras avant le body ('À savoir' defaut)
 *   $body    (string) : contenu HTML (richText autorise : <strong>, <em>, <a>)
 *
 * Note design system : la classe CSS reste .tarifs-callout (historique),
 * voir TODO design system : renommer en .info-callout lors d'un futur refactor CSS.
 */
$icon    = $icon    ?? '💡';
$variant = ($variant ?? 'info') === 'warning' ? 'warning' : 'info';
$label   = $label   ?? 'À savoir';
$body    = $body    ?? '';
?>
<div class="tarifs-callout tarifs-callout--<?= $variant ?>">
    <span class="tarifs-callout__icon" aria-hidden="true"><?= $icon ?></span>
    <strong><?= htmlspecialchars($label, ENT_QUOTES, 'UTF-8') ?> :</strong> <?= $body ?>
</div>
