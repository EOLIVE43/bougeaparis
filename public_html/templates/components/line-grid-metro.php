<?php
/**
 * Grille des lignes de metro - cercles colores
 */

$lines        = $props['lines']         ?? [];
$showTerminus = $props['show_terminus'] ?? true;
$linkBase     = $props['link_base']     ?? '/metro/';

if (empty($lines)) return;
?>
<div class="line-grid line-grid--metro" role="list" aria-label="Liste des lignes de metro">
    <?php foreach ($lines as $line):
        $slug       = $line['slug']       ?? '';
        $short      = $line['short']      ?? '?';
        $name       = $line['name']       ?? '';
        $color      = $line['color']      ?? '#CCCCCC';
        $textColor  = $line['text_color'] ?? '#FFFFFF';
        $terminus_a = $line['terminus_a'] ?? '';
        $terminus_b = $line['terminus_b'] ?? '';
        $automated  = $line['automated']  ?? false;
        $stations   = $line['stations']   ?? null;
    ?>
        <a href="<?= htmlspecialchars($linkBase . $slug . '/') ?>"
           class="line-grid__item line-grid__item--metro"
           role="listitem"
           aria-label="<?= htmlspecialchars($name . ' : de ' . $terminus_a . ' a ' . $terminus_b) ?>">
            <span class="line-grid__badge line-grid__badge--metro"
                  style="background-color: <?= htmlspecialchars($color) ?>; color: <?= htmlspecialchars($textColor) ?>;"
                  aria-hidden="true"><?= htmlspecialchars($short) ?></span>
            <?php if ($showTerminus): ?>
                <div class="line-grid__info">
                    <span class="line-grid__name"><?= htmlspecialchars($name) ?></span>
                    <span class="line-grid__termini">
                        <?= htmlspecialchars($terminus_a) ?> <span class="line-grid__arrow" aria-hidden="true">&harr;</span> <?= htmlspecialchars($terminus_b) ?>
                    </span>
                    <?php if ($automated || $stations): ?>
                        <span class="line-grid__meta">
                            <?php if ($stations): ?><?= $stations ?> stations<?php endif; ?>
                            <?php if ($automated): ?><?= $stations ? ' &middot; ' : '' ?><span class="line-grid__tag">Auto</span><?php endif; ?>
                        </span>
                    <?php endif; ?>
                </div>
            <?php endif; ?>
        </a>
    <?php endforeach; ?>
</div>
