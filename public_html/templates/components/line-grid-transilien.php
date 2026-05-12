<?php
/**
 * Composant line-grid-transilien : grille des lignes Transilien (H, J, K, L...).
 */

$lines         = $props['lines']         ?? [];
$show_terminus = $props['show_terminus'] ?? true;
$link_base     = $props['link_base']     ?? '/transilien/';
$enable_links  = $props['enable_links']  ?? false;

if (empty($lines)) return;
?>
<ul class="line-grid line-grid--transilien" role="list">
    <?php foreach ($lines as $line):
        $slug      = $line['slug']       ?? '';
        $label     = $line['label']      ?? '';
        $name      = $line['name']       ?? 'Ligne ' . $label;
        $color     = $line['color']      ?? '#999999';
        $textColor = $line['text_color'] ?? '#FFFFFF';
        $termini   = $line['termini']    ?? [];
        $href      = $link_base . 'ligne-' . strtolower($label) . '/';
    ?>
        <?php
          // Correction 16b : .line-pill--square pour Transilien (lettre seule H/J/K/...).
          $pillSlug = strtolower((string)$label);
        ?>
        <li class="line-grid__item">
            <span class="line-pill line-pill--square line-pill--<?= htmlspecialchars($pillSlug) ?>" aria-hidden="true">
                <?= htmlspecialchars($label) ?>
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
            </span>
        </li>
    <?php endforeach; ?>
</ul>
