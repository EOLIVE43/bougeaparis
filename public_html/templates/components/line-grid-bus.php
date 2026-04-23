<?php
/**
 * Composant line-grid-bus : 3 categories de reseaux de bus.
 *
 * Props :
 *   - enable_links : activer les liens vers les pages dediees (defaut false)
 *
 * Structure en dur car les reseaux bus ne sont pas une simple liste de lignes.
 */

$enable_links = $props['enable_links'] ?? false;

$networks = [
    [
        'category' => 'mobilien',
        'title'    => 'Réseau Mobilien',
        'desc'     => 'Lignes à haut niveau de service en Île-de-France',
        'items' => [
            ['label' => 'Mobilien 20', 'href' => '/bus/mobilien/', 'sub' => 'Haute fréquence'],
            ['label' => 'Mobilien 22', 'href' => '/bus/mobilien/', 'sub' => 'Haute fréquence'],
            ['label' => 'Mobilien 27', 'href' => '/bus/mobilien/', 'sub' => 'Haute fréquence'],
        ],
    ],
    [
        'category' => 'banlieue',
        'title'    => 'Bus de banlieue',
        'desc'     => 'Lignes 100 à 799 — desserte des communes franciliennes',
        'items' => [
            ['label' => 'Lignes 100-199',  'href' => '/bus/banlieue/', 'sub' => 'Proche couronne'],
            ['label' => 'Lignes 300-399',  'href' => '/bus/banlieue/', 'sub' => 'Grande banlieue'],
            ['label' => 'Lignes 700+',     'href' => '/bus/banlieue/', 'sub' => 'Express périphérique'],
        ],
    ],
    [
        'category' => 'noctilien',
        'title'    => 'Bus Noctilien',
        'desc'     => '47 lignes de bus de nuit (0h30 - 5h30)',
        'items' => [
            ['label' => 'Paris intramuros', 'href' => '/bus/noctilien/', 'sub' => '17 lignes'],
            ['label' => 'Banlieue',         'href' => '/bus/noctilien/', 'sub' => '30 lignes'],
        ],
    ],
];
?>
<div class="bus-network-grid">
    <?php foreach ($networks as $network): ?>
        <div class="bus-network-grid__category">
            <h3 class="bus-network-grid__title"><?= htmlspecialchars($network['title']) ?></h3>
            <p class="bus-network-grid__desc"><?= htmlspecialchars($network['desc']) ?></p>

            <div class="bus-network-grid__items">
                <?php foreach ($network['items'] as $item): ?>
                    <div class="bus-network-grid__item">
                        <span class="bus-network-grid__badge bus-network-grid__badge--<?= $network['category'] ?>">BUS</span>
                        <span class="bus-network-grid__info">
                            <?php if ($enable_links): ?>
                                <a href="<?= htmlspecialchars($item['href']) ?>" class="bus-network-grid__name"><strong><?= htmlspecialchars($item['label']) ?></strong></a>
                            <?php else: ?>
                                <strong><?= htmlspecialchars($item['label']) ?></strong>
                            <?php endif; ?>
                            <span><?= htmlspecialchars($item['sub']) ?></span>
                        </span>
                    </div>
                <?php endforeach; ?>
            </div>
        </div>
    <?php endforeach; ?>
</div>
