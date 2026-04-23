<?php
/**
 * Composant line-badge : badge universel pour une ligne.
 *
 * Props :
 *   - type       : 'metro' | 'rer' | 'tramway' | 'bus' | 'transilien'
 *   - short      : '1', 'A', 'T3a', '38'
 *   - color      : hex
 *   - text_color : hex
 *   - size       : 'sm' | 'md' | 'lg'
 *   - ariaLabel  : texte accessible
 */

$type      = $props['type']       ?? 'metro';
$short     = $props['short']      ?? '?';
$color     = $props['color']      ?? '#0F6E56';
$textColor = $props['text_color'] ?? '#FFFFFF';
$size      = $props['size']       ?? 'md';
$ariaLabel = $props['ariaLabel']  ?? "Ligne $short";
?>
<span class="line-badge line-badge--<?= htmlspecialchars($type) ?> line-badge--<?= htmlspecialchars($size) ?>"
      style="--badge-bg: <?= htmlspecialchars($color) ?>; --badge-text: <?= htmlspecialchars($textColor) ?>;"
      aria-label="<?= htmlspecialchars($ariaLabel) ?>"
      role="img">
    <span class="line-badge__text"><?= htmlspecialchars($short) ?></span>
</span>
