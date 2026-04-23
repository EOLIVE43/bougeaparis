<?php
/**
 * Template generique hub-transport.
 * Lit les variables depuis $props car appele en tant que partial via les wrappers.
 */

$cocon          = $props['cocon']          ?? [];
$lines          = $props['lines']          ?? [];
$cocon_slug     = $props['cocon_slug']     ?? '';
$cocon_label    = $props['cocon_label']    ?? '';
$grid_component = $props['grid_component'] ?? '';
$data_key       = $props['data_key']       ?? '';

$tpl->seo
    ->setTitle($cocon['seo']['title']       ?? '')
    ->setDescription($cocon['seo']['description'] ?? '')
    ->setCanonical($cocon['seo']['canonical']   ?? '')
    ->setOgType($cocon['seo']['og_type']      ?? 'article');

$traffic_cocon_map = [
    'rer'        => 'rer',
    'tramway'    => 'tramway',
    'transilien' => 'transilien',
    'bus'        => 'bus',
];
$traffic_cocon = $traffic_cocon_map[$cocon_slug] ?? null;

$icon_map = [
    'rer'        => 'rer',
    'bus'        => 'bus',
    'tramway'    => 'tram',
    'aeroports'  => 'plane',
    'transilien' => 'train',
];
$hero_icon = $icon_map[$cocon_slug] ?? null;
?>

<?php
$tpl->partial('components/breadcrumb', [
    'items' => [
        ['label' => 'Accueil', 'url' => '/'],
        ['label' => $cocon_label],
    ],
]);
?>

<main class="page-cocon page-cocon--<?= htmlspecialchars($cocon_slug) ?>">

    <?php
    $tpl->partial('components/hero-cocon', [
        'h1'       => $cocon['hero']['h1']       ?? '',
        'subtitle' => $cocon['hero']['subtitle'] ?? '',
        'chiffres' => $cocon['hero']['chiffres'] ?? [],
        'icon'     => $hero_icon,
    ]);
    ?>

    <div class="page-cocon__container">

        <?php if ($traffic_cocon): ?>
            <?php $tpl->partial('components/traffic-widget', [
                'mode'  => 'cocon',
                'cocon' => $traffic_cocon,
            ]); ?>
        <?php endif; ?>

        <section class="page-section page-section--intro">
            <?= $cocon['intro'] ?? '' ?>
        </section>

        <?php $tpl->partial('ads/slot-header'); ?>

        <?php if ($cocon_slug === 'aeroports'): ?>
            <section class="page-section" aria-labelledby="section-airports">
                <h2 id="section-airports">Les 3 aéroports parisiens</h2>
                <?php $tpl->partial('components/airport-grid', [
                    'airports' => $lines['aeroports'] ?? [],
                    'link_base' => '/aeroports/',
                ]); ?>
            </section>
        <?php elseif ($cocon_slug === 'bus'): ?>
            <section class="page-section" aria-labelledby="section-reseaux">
                <h2 id="section-reseaux"><?= htmlspecialchars($cocon['section_reseaux']['title'] ?? 'Les réseaux') ?></h2>
                <?= $cocon['section_reseaux']['content'] ?? '' ?>
                <?php $tpl->partial('components/line-grid-bus'); ?>
            </section>
        <?php elseif (!empty($grid_component) && !empty($data_key) && !empty($lines[$data_key])): ?>
            <section class="page-section" aria-labelledby="section-lignes">
                <h2 id="section-lignes">Toutes les lignes</h2>
                <?php $tpl->partial('components/' . $grid_component, [
                    'lines' => $lines[$data_key],
                    'show_terminus' => true,
                    'link_base' => '/' . $cocon_slug . '/',
                ]); ?>
            </section>
        <?php endif; ?>

        <?php
        $sections_order = [
            'section_lignes', 'section_cdg', 'section_orly', 'section_beauvais',
            'section_tarifs', 'section_horaires', 'section_specificites',
        ];
        foreach ($sections_order as $key):
            if (!empty($cocon[$key])):
                $section = $cocon[$key];
        ?>
                <section class="page-section" aria-labelledby="section-<?= $key ?>">
                    <h2 id="section-<?= $key ?>"><?= htmlspecialchars($section['title'] ?? '') ?></h2>
                    <?= $section['content'] ?? '' ?>
                </section>
        <?php
            endif;
        endforeach;
        ?>

        <?php $tpl->partial('ads/slot-in-article'); ?>

        <?php if (!empty($cocon['faq']['items'])): ?>
            <?php $tpl->partial('components/faq-accordion', [
                'title' => $cocon['faq']['title'] ?? 'Questions fréquentes',
                'items' => $cocon['faq']['items'],
                'emit_schema' => true,
            ]); ?>
        <?php endif; ?>

        <section class="page-section page-section--related" aria-labelledby="section-related">
            <h2 id="section-related">Explorer les autres transports</h2>
            <nav class="related-nav" aria-label="Autres transports">
                <?php
                $all_cocons = [
                    'metro'      => ['label' => 'Métro',      'icon' => 'metro'],
                    'rer'        => ['label' => 'RER',        'icon' => 'rer'],
                    'bus'        => ['label' => 'Bus',        'icon' => 'bus'],
                    'tramway'    => ['label' => 'Tramway',    'icon' => 'tram'],
                    'transilien' => ['label' => 'Transilien', 'icon' => 'train'],
                    'aeroports'  => ['label' => 'Aéroports',  'icon' => 'plane'],
                ];
                foreach ($all_cocons as $slug => $info):
                    if ($slug === $cocon_slug) continue;
                ?>
                    <a href="/<?= $slug ?>/" class="related-nav__item">
                        <span class="related-nav__label"><?= htmlspecialchars($info['label']) ?></span>
                        <?php $tpl->partial('components/icon-menu', ['icon' => $info['icon'], 'size' => 'lg']); ?>
                    </a>
                <?php endforeach; ?>
            </nav>
        </section>

        <?php $tpl->partial('ads/slot-footer'); ?>

    </div>
</main>
