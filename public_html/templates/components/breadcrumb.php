<?php
/**
 * Composant breadcrumb (fil d'Ariane) avec schema.org BreadcrumbList.
 *
 * Props :
 *   - items : array de [['label' => '...', 'url' => '...'], ...]
 *     Le dernier item est la page courante (sans url).
 */

$items = $props['items'] ?? [];
if (empty($items)) return;
?>
<nav class="breadcrumb" aria-label="Fil d'Ariane">
    <ol class="breadcrumb__list" itemscope itemtype="https://schema.org/BreadcrumbList">
        <?php foreach ($items as $idx => $item):
            $label  = $item['label'] ?? '';
            $url    = $item['url']   ?? null;
            $isLast = ($idx === count($items) - 1);
            $pos    = $idx + 1;
        ?>
            <li class="breadcrumb__item" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                <?php if ($url && !$isLast): ?>
                    <a href="<?= htmlspecialchars($url) ?>" itemprop="item">
                        <span itemprop="name"><?= htmlspecialchars($label) ?></span>
                    </a>
                <?php else: ?>
                    <span itemprop="name" aria-current="page"><?= htmlspecialchars($label) ?></span>
                <?php endif; ?>
                <meta itemprop="position" content="<?= $pos ?>" />
                <?php if (!$isLast): ?>
                    <span class="breadcrumb__separator" aria-hidden="true">&rsaquo;</span>
                <?php endif; ?>
            </li>
        <?php endforeach; ?>
    </ol>
</nav>
