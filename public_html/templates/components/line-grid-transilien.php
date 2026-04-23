<?php
$lines        = $props['lines']         ?? [];
$showTerminus = $props['show_terminus'] ?? true;
$linkBase     = $props['link_base']     ?? '/transilien/';

if (empty($lines)) return;
?>
<div class="line-grid line-grid--transilien" role="list" aria-label="Liste des lignes Transilien">
    <?php foreach ($lines as $line):
        $short      = $line['short']      ?? '?';
        $name       = $line['name']       ?? '';
        $color      = $line['color']      ?? '#CCCCCC';
        $textColor  = $line['text_color'] ?? '#FFFFFF';
        $terminus_a = $line['terminus_a'] ?? '';
        $terminus_b = $line['terminus_b'] ?? '';
    ?>
        <a href="<?= htmlspecialchars($linkBase . strtolower($short) . '/') ?>"
           class="line-grid__item line-grid__item--transilien"
           role="listitem"
           aria-label="<?= htmlspecialchars($name) ?>">
            <span class="line-grid__badge line-grid__badge--transilien"
                  style="background-color: <?= htmlspecialchars($color) ?>; color: <?= htmlspecialchars($textColor) ?>;"
                  aria-hidden="true"><?= htmlspecialchars($short) ?></span>
            <?php if ($showTerminus): ?>
                <div class="line-grid__info">
                    <span class="line-grid__name"><?= htmlspecialchars($name) ?></span>
                    <span class="line-grid__termini">
                        <?= htmlspecialchars($terminus_a) ?> <span class="line-grid__arrow" aria-hidden="true">&harr;</span> <?= htmlspecialchars($terminus_b) ?>
                    </span>
                </div>
            <?php endif; ?>
        </a>
    <?php endforeach; ?>
</div>
