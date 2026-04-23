<?php
/**
 * Template hub-metro : page /metro/ enrichie (objectif SEO top 3).
 */

$tpl->seo
    ->setTitle($cocon['seo']['title']       ?? 'Métro de Paris')
    ->setDescription($cocon['seo']['description'] ?? '')
    ->setCanonical($cocon['seo']['canonical']   ?? '')
    ->setOgType($cocon['seo']['og_type']      ?? 'article');
?>

<?php
$tpl->partial('components/breadcrumb', [
    'items' => [
        ['label' => 'Accueil', 'url' => '/'],
        ['label' => 'Métro'],
    ],
]);
?>

<main class="page-cocon page-cocon--metro">

    <?php
    $tpl->partial('components/hero-cocon', [
        'h1'       => $cocon['hero']['h1']       ?? '',
        'subtitle' => $cocon['hero']['subtitle'] ?? '',
        'chiffres' => $cocon['hero']['chiffres'] ?? [],
        'icon'     => 'metro',
    ]);
    ?>

    <div class="page-cocon__container">

        <?php
        $tpl->partial('components/traffic-widget', [
            'mode'  => 'cocon',
            'cocon' => 'metro',
        ]);
        ?>

        <section class="page-section page-section--intro">
            <?= $cocon['intro'] ?? '' ?>
        </section>

        <?php $tpl->partial('ads/slot-header'); ?>

        <section class="page-section" aria-labelledby="section-lignes">
            <h2 id="section-lignes">Les 16 lignes du métro parisien</h2>
            <p>
                Voici la liste complète des lignes de métro avec leurs terminus et leurs caractéristiques.
                Cliquez sur une ligne pour accéder à sa page dédiée avec stations, horaires et plan détaillé.
            </p>
            <?php $tpl->partial('components/line-grid-metro', [
                'lines' => $lines['metro'] ?? [],
                'show_terminus' => true,
                'link_base' => '/metro/',
            ]); ?>
        </section>

        <section class="page-section" aria-labelledby="section-plan">
            <h2 id="section-plan"><?= htmlspecialchars($cocon['section_plan']['title'] ?? '') ?></h2>
            <?= $cocon['section_plan']['content'] ?? '' ?>
        </section>

        <section class="page-section" aria-labelledby="section-horaires">
            <h2 id="section-horaires"><?= htmlspecialchars($cocon['section_horaires']['title'] ?? '') ?></h2>
            <?= $cocon['section_horaires']['content'] ?? '' ?>
        </section>

        <?php $tpl->partial('ads/slot-in-article'); ?>

        <section class="page-section" aria-labelledby="section-tarifs">
            <h2 id="section-tarifs"><?= htmlspecialchars($cocon['section_tarifs']['title'] ?? '') ?></h2>
            <?= $cocon['section_tarifs']['content'] ?? '' ?>
        </section>

        <section class="page-section" aria-labelledby="section-chiffres">
            <h2 id="section-chiffres"><?= htmlspecialchars($cocon['section_chiffres']['title'] ?? '') ?></h2>
            <?= $cocon['section_chiffres']['content'] ?? '' ?>
        </section>

        <section class="page-section" aria-labelledby="section-histoire">
            <h2 id="section-histoire"><?= htmlspecialchars($cocon['section_histoire']['title'] ?? '') ?></h2>
            <?= $cocon['section_histoire']['content'] ?? '' ?>
        </section>

        <section class="page-section" aria-labelledby="section-accessibilite">
            <h2 id="section-accessibilite"><?= htmlspecialchars($cocon['section_accessibilite']['title'] ?? '') ?></h2>
            <?= $cocon['section_accessibilite']['content'] ?? '' ?>
        </section>

        <section class="page-section" aria-labelledby="section-nuit">
            <h2 id="section-nuit"><?= htmlspecialchars($cocon['section_nuit']['title'] ?? '') ?></h2>
            <?= $cocon['section_nuit']['content'] ?? '' ?>
        </section>

        <section class="page-section" aria-labelledby="section-guide">
            <h2 id="section-guide"><?= htmlspecialchars($cocon['section_guide']['title'] ?? '') ?></h2>
            <?= $cocon['section_guide']['content'] ?? '' ?>
        </section>

        <?php $tpl->partial('ads/slot-in-article'); ?>

        <section class="page-section" aria-labelledby="section-specific">
            <h2 id="section-specific"><?= htmlspecialchars($cocon['section_specific']['title'] ?? '') ?></h2>
            <?= $cocon['section_specific']['content'] ?? '' ?>
        </section>

        <?php if (!empty($cocon['faq']['items'])): ?>
            <?php $tpl->partial('components/faq-accordion', [
                'title' => $cocon['faq']['title'] ?? 'Questions fréquentes',
                'items' => $cocon['faq']['items'],
                'emit_schema' => true,
            ]); ?>
        <?php endif; ?>

        <section class="page-section page-section--related" aria-labelledby="section-related">
            <h2 id="section-related">Explorer les autres transports d'Île-de-France</h2>
            <div class="related-grid">
                <a href="/rer/" class="related-grid__item"><strong>RER</strong> &mdash; 5 lignes express</a>
                <a href="/bus/" class="related-grid__item"><strong>Bus</strong> &mdash; 1500+ lignes</a>
                <a href="/tramway/" class="related-grid__item"><strong>Tramway</strong> &mdash; 13 lignes</a>
                <a href="/transilien/" class="related-grid__item"><strong>Transilien</strong> &mdash; 8 lignes</a>
                <a href="/aeroports/" class="related-grid__item"><strong>Aéroports</strong> &mdash; CDG, Orly, Beauvais</a>
            </div>
        </section>

        <?php $tpl->partial('ads/slot-footer'); ?>

    </div>
</main>
