<?php
/**
 * Composant line-grid-metro : grille des lignes de metro avec cercles colores.
 *
 * Props :
 *   - lines         : array des lignes du metro (data/lines.json)
 *   - show_terminus : afficher les terminus (defaut true)
 *   - link_base     : base URL pour les liens (defaut '/metro/')
 *   - enable_links  : activer les liens (defaut false tant que pages lignes pas creees)
 *
 * Comportement :
 *   - Lien uniquement sur le nom de la ligne (pas sur toute la card)
 *   - Si enable_links=false, le nom n'est pas un lien
 */

$lines         = $props['lines']         ?? [];
$show_terminus = $props['show_terminus'] ?? true;
$link_base     = $props['link_base']     ?? '/metro/';
$enable_links  = $props['enable_links']  ?? false;

if (empty($lines)) return;
?>
<ul class="line-grid line-grid--metro" role="list">
    <?php foreach ($lines as $line):
        $slug      = $line['slug']       ?? '';
        $label     = $line['label']      ?? '';
        $name      = $line['name']       ?? 'Ligne ' . $label;
        $color     = $line['color']      ?? '#999999';
        $textColor = $line['text_color'] ?? '#FFFFFF';
        $termini   = $line['termini']    ?? [];
        $stations  = $line['stations_count'] ?? null;
        $auto      = !empty($line['automatic']);
        $href      = $link_base . 'ligne-' . $label . '/';
    ?>
        <li class="line-grid__item">
            <span class="line-grid__badge line-grid__badge--metro" style="background-color: <?= htmlspecialchars($color) ?>; color: <?= htmlspecialchars($textColor) ?>;" aria-hidden="true">
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
                <span class="line-grid__meta">
                    <?php if ($stations): ?><?= $stations ?> stations<?php endif; ?>
                    <?php if ($auto): ?> &middot; <span class="line-grid__tag">Auto</span><?php endif; ?>
                </span>
            </span>
        </li>
    <?php endforeach; ?>
</ul>
