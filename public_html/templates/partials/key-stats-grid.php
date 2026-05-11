<?php
/**
 * Partial : key-stats-grid
 *
 * Grille de cards visuelles avec gros chiffre + label. Utilise pour donner
 * du relief a un concept abstrait (ex : nombre de lignes, nombre de POIs).
 * Pattern visuel aligne sur la zones-map de /tarifs/ (degrade vert primary).
 *
 * Variables attendues (set par l'appelant via include) :
 *   $stats (array) : liste de [number => string, label => string,
 *                                sublabel => string|null]
 *
 * Note : pas de H2 dans le partial — l'appelant pose son propre titre H2
 * juste avant l'include (cohérence avec le pattern editorial actuel).
 */
$stats = $stats ?? [];
if (empty($stats)) return;
?>
<div class="key-stats-grid">
    <?php foreach ($stats as $s): ?>
    <div class="key-stat">
        <div class="key-stat__number"><?= htmlspecialchars((string)($s['number'] ?? ''), ENT_QUOTES, 'UTF-8') ?></div>
        <div class="key-stat__label"><?= htmlspecialchars((string)($s['label'] ?? ''), ENT_QUOTES, 'UTF-8') ?></div>
        <?php if (!empty($s['sublabel'])): ?>
        <div class="key-stat__sublabel"><?= htmlspecialchars((string)$s['sublabel'], ENT_QUOTES, 'UTF-8') ?></div>
        <?php endif; ?>
    </div>
    <?php endforeach; ?>
</div>
