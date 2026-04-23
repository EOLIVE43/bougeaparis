<?php
/**
 * Composant line-grid-rer : grille des lignes RER (losanges colores).
 *
 * Props similaires a line-grid-metro.
 * Lien uniquement sur le nom (desactivable via enable_links).
 */

$lines         = $props['lines']         ?? [];
$show_terminus = $props['show_terminus'] ?? true;
$link_base     = $props['link_base']     ?? '/rer/';
$enable_links  = $props['enable_links']  ?? false;

if (empty($lines)) return;
?>
<ul class="line-grid line-grid--rer" role="list">
    <?php foreach ($lines as $line):
        $slug      = $line['slug']       ?? '';
        $label     = $line['label']      ?? '';
        $name      = $line['name']       ?? 'RER ' . $label;
        $color     = $line['color']      ?? '#999999';
        $textColor = $line['text_color'] ?? '#FFFFFF';
        $termini   = $line['termini']    ?? [];
        $stations  = $line['stations_count'] ?? null;
        $href      = $link_base . 'ligne-' . strtolower($label) . '/';
    ?>
        <li class="line-grid__item">
            <span class="line-grid__badge line-grid__badge--rer" style="background-color: <?= htmlspecialchars($color) ?>; color: <?= htmlspecialchars($textColor) ?>;" aria-hidden="true">
                <span class="line-grid__badge-inner"><?= htmlspecialchars($label) ?></span>
            </span>
            <span class="line-grid__info">
                <?php if ($enable_links): ?>
                    <a href="<?= htmlspecialchars($href) ?>" class="line-grid__name line-grid__name--link"><?= htmlspecialchars($name) ?></a>
                <?php else: ?>
                    <span class="line-grid__name"><?= htmlspecialchars($name) ?></span>
                <?php endif; ?>
                <?php if ($show_terminus && !empty($termini)): ?>
                    <span class="line-grid__termini">
                        <?= htmlspecialchars($termini[0] ?? '') ?>
                        <span class="line-grid__arrow" aria-hidden="true">&harr;</span>
                        <?= htmlspecialchars($termini[1] ?? '') ?>
                    </span>
                <?php endif; ?>
                <?php if ($stations): ?>
                    <span class="line-grid__meta"><?= $stations ?> gares</span>
                <?php endif; ?>
            </span>
        </li>
    <?php endforeach; ?>
</ul>
