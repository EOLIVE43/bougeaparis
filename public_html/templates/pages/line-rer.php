<?php
/**
 * Template page : ligne de métro (ex: /metro/ligne-1)
 *
 * Variables disponibles :
 *   $line : array, données complètes de la ligne (data/lines/metro-X.json)
 *   $tpl  : instance Template
 *   $seo  : instance Seo
 *
 * Architecture : assemble 16 composants line/* via $tpl->partial(), en
 * propageant $line à chacun. Le SEO est centralisé via $seo->set*().
 */

// -------------------- SEO --------------------

$lineCode    = $line['code']      ?? '';
$lineColor   = $line['color']     ?? '#0F6E56';
$lineColorTx = $line['color_text']?? '#FFFFFF';
$lineMode    = $line['mode']      ?? 'metro';
$h1          = $line['seo']['h1']          ?? ('Ligne ' . $lineCode);
$pageDesc    = $line['seo']['description'] ?? '';
$canonical   = '/rer/ligne-' . strtolower($lineCode);

$tpl->seo
    ->setTitle(bp_title_ligne_rer((string)$lineCode), false)
    ->setDescription($pageDesc)
    ->setCanonical($canonical)
    ->setOgType('article');

// Hero image (LCP) : preload responsive + og:image si presente.
$heroImage = $line['hero_image'] ?? null;
if (is_array($heroImage) && !empty($heroImage['url'])) {
    $tpl->seo->setOgImage($heroImage['url']);
    $localVersionsLine = $heroImage['local_versions'] ?? null;
    if (is_array($localVersionsLine) && !empty($localVersionsLine['avif'])) {
        $tpl->seo->addPreloadImageSet(
            $localVersionsLine['avif'],
            'image/avif',
            '(max-width: 768px) 100vw, 1200px'
        );
    } else {
        $tpl->seo->addPreloadImage($heroImage['url']);
    }
}

// Schema.org Article (E-E-A-T)
$primaryAuthor = $line['meta']['primary_author'] ?? null;
$datePublished = $line['meta']['dates']['published'] ?? '2026-04-28';
$dateModified  = $line['meta']['dates']['updated']   ?? date('Y-m-d');

$tpl->seo->addSchema([
    '@context' => 'https://schema.org',
    '@type'    => 'Article',
    'headline' => $h1,
    'description' => $pageDesc,
    'datePublished' => $datePublished,
    'dateModified'  => $dateModified,
    'author' => $primaryAuthor ? [
        '@type' => 'Person',
        'name'  => $primaryAuthor['name'] ?? 'Ludo',
        'url'   => 'https://bougeaparis.fr' . ($primaryAuthor['url'] ?? '/auteur/ludo/'),
    ] : null,
    'publisher' => [
        '@type' => 'Organization',
        'name'  => 'BougeaParis.fr',
        'logo'  => [
            '@type' => 'ImageObject',
            'url'   => 'https://bougeaparis.fr/assets/img/logo/og-image.png',
        ],
    ],
]);

// Breadcrumb (rendu visuel + schema.org)
$tpl->seo->setBreadcrumb([
    ['label' => 'Accueil',         'url' => '/'],
    ['label' => 'Métro',           'url' => '/metro/'],
    ['label' => 'Ligne ' . $lineCode, 'url' => $canonical],
]);

// Charge le CSS dedie aux pages ligne (uniquement sur ces pages)
$tpl->addStylesheet('/assets/css/line.css');

if (Config::get('site.line_pages_noindex', false)) {
    $tpl->seo->setRobots('noindex,follow');
}
?>

<?php
// Breadcrumb visible en haut de page
$tpl->partial('components/breadcrumb', [
    'items' => [
        ['label' => 'Accueil', 'url' => '/'],
        ['label' => 'Métro',   'url' => '/metro/'],
        ['label' => 'Ligne ' . $lineCode],
    ],
]);
?>

<?php
// Couleur d'accent dynamique : injecte 6 CSS custom properties depuis le JSON
// ligne, scopees a l'article. Les rules de line.css picquent automatiquement
// la couleur de la ligne courante (DRY pour les 16 lignes).
//
// - --accent            : couleur de la ligne (#62259D L14, #FFCD00 L1, ...)
// - --accent-light      : version eclaircie 80% (pour key-fact, discover-pill)
// - --accent-text       : couleur du texte sur fond accent
// - --accent-bg-soft    : tint tres pale 92% (anecdote, schedule, alternatives)
// - --accent-border-soft: tint medium 65% (border dashed, separateurs)
// - --accent-strong     : version assombrie SI besoin pour passer AA (4.5:1)
//                         entre --accent-text et le bg. Si --accent passe deja,
//                         retourne --accent inchange (preserve identite visuelle
//                         pour L1/L4/L14). Pour les futures lignes claires
//                         (L6/L7/L9/L10/L12/L13), darken automatiquement.
$lightenHex = function (string $hex, float $mix): string {
    $hex = ltrim($hex, '#');
    if (strlen($hex) !== 6) return '#FFFFFF';
    $r = (int)hexdec(substr($hex, 0, 2));
    $g = (int)hexdec(substr($hex, 2, 2));
    $b = (int)hexdec(substr($hex, 4, 2));
    $r = (int)round($r + $mix * (255 - $r));
    $g = (int)round($g + $mix * (255 - $g));
    $b = (int)round($b + $mix * (255 - $b));
    return sprintf('#%02X%02X%02X', $r, $g, $b);
};
// Helpers WCAG : luminance relative + ratio de contraste
$wcagLuminance = function (string $hex): float {
    $hex = ltrim($hex, '#');
    if (strlen($hex) !== 6) return 1.0;
    $rgb = [hexdec(substr($hex, 0, 2)), hexdec(substr($hex, 2, 2)), hexdec(substr($hex, 4, 2))];
    $lin = array_map(function ($c) {
        $cs = $c / 255;
        return $cs <= 0.03928 ? ($cs / 12.92) : pow(($cs + 0.055) / 1.055, 2.4);
    }, $rgb);
    return 0.2126 * $lin[0] + 0.7152 * $lin[1] + 0.0722 * $lin[2];
};
$wcagContrast = function (string $a, string $b) use ($wcagLuminance): float {
    $la = $wcagLuminance($a); $lb = $wcagLuminance($b);
    return (max($la, $lb) + 0.05) / (min($la, $lb) + 0.05);
};
// Blend with black at $mix (0..1) : 0 = unchanged, 1 = pure black
$blendBlack = function (string $hex, float $mix): string {
    $hex = ltrim($hex, '#');
    if (strlen($hex) !== 6) return '#000000';
    $r = (int)round(hexdec(substr($hex, 0, 2)) * (1 - $mix));
    $g = (int)round(hexdec(substr($hex, 2, 2)) * (1 - $mix));
    $b = (int)round(hexdec(substr($hex, 4, 2)) * (1 - $mix));
    return sprintf('#%02X%02X%02X', $r, $g, $b);
};
// darken_until_contrast : si contrast(text, accent) >= 4.5, retourne accent
// inchange. Sinon assombrit accent par paliers de 5% jusqu'a passer AA.
$darkenUntilContrast = function (string $accent, string $text, float $target = 4.5)
    use ($wcagContrast, $blendBlack): string {
    if ($wcagContrast($text, $accent) >= $target) return $accent;
    for ($mix = 0.05; $mix <= 0.95; $mix += 0.05) {
        $candidate = $blendBlack($accent, $mix);
        if ($wcagContrast($text, $candidate) >= $target) return $candidate;
    }
    return '#000000';
};

$lineColorRaw  = $line['color']       ?? '#FFCD00';
$lineColorLite = $line['color_light'] ?? '#FFF6CC';
$lineColorText = $line['color_text']  ?? '#1A2B26';
$accentBgSoft     = $lightenHex($lineColorRaw, 0.92);
$accentBorderSoft = $lightenHex($lineColorRaw, 0.65);
// Trois variables d'accent darkenées, pour trois usages distincts :
//  --accent-strong       : bg coloré + texte --accent-text (badges, CTA, pills)
//                          → darken jusqu'à contraste(accent-text, accent) >= 4.5
//  --accent-on-light     : couleur sur fond blanc/quasi-blanc
//                          → darken jusqu'à contraste(accent, blanc) >= 4.5
//  --accent-text-on-soft : couleur sur fond --accent-light (pastel ligne,
//                          ex .stat-card avec bg pastel ligne)
//                          → darken jusqu'à contraste(accent, accent-light) >= 4.5
// Indépendantes pour éviter qu'un fix d'un contexte casse les autres.
$accentStrong      = $darkenUntilContrast($lineColorRaw, $lineColorText, 4.5);
$accentOnLight     = $darkenUntilContrast($lineColorRaw, '#FFFFFF',      4.5);
$accentTextOnSoft  = $darkenUntilContrast($lineColorRaw, $lineColorLite, 4.5);
$accentStyle = sprintf(
    '--accent:%s;--accent-light:%s;--accent-text:%s;--accent-bg-soft:%s;--accent-border-soft:%s;--accent-strong:%s;--accent-on-light:%s;--accent-text-on-soft:%s;',
    htmlspecialchars($lineColorRaw,     ENT_QUOTES, 'UTF-8'),
    htmlspecialchars($lineColorLite,    ENT_QUOTES, 'UTF-8'),
    htmlspecialchars($lineColorText,    ENT_QUOTES, 'UTF-8'),
    htmlspecialchars($accentBgSoft,     ENT_QUOTES, 'UTF-8'),
    htmlspecialchars($accentBorderSoft, ENT_QUOTES, 'UTF-8'),
    htmlspecialchars($accentStrong,     ENT_QUOTES, 'UTF-8'),
    htmlspecialchars($accentOnLight,    ENT_QUOTES, 'UTF-8'),
    htmlspecialchars($accentTextOnSoft, ENT_QUOTES, 'UTF-8')
);
?>
<article class="line-page line-page--metro"
         data-line="<?= e($lineMode . '-' . $lineCode) ?>"
         style="<?= $accentStyle ?>">
    <div class="line-page__container">

        <!-- 1. HERO -->
        <?php $tpl->partial('components/line/hero', ['line' => $line]); ?>

        <!-- ✨ Quick Actions -->
        <?php $tpl->partial('components/line/quick-actions', ['line' => $line]); ?>

        <!-- 2. INTRODUCTION SEO -->
        <?php $tpl->partial('components/line/introduction', ['line' => $line]); ?>

        <!-- AdSlot 1 : header -->
        <?php $tpl->partial('ads/slot-header'); ?>

        <!-- 3. PLAN VISUEL -->
        <?php $tpl->partial('components/line/plan-visuel', ['line' => $line]); ?>

        <!-- 4. TABLEAU DES STATIONS -->
        <?php $tpl->partial('components/line/stations-table', ['line' => $line]); ?>

        <!-- AdSlot 2 : in-article -->
        <?php $tpl->partial('ads/slot-in-article'); ?>

        <!-- 5. HORAIRES -->
        <?php $tpl->partial('components/line/horaires', ['line' => $line]); ?>

        <!-- 6. TRAFIC TEMPS RÉEL (DÉTAIL) -->
        <?php $tpl->partial('components/line/trafic-temps-reel', ['line' => $line]); ?>

        <!-- 7. ITINÉRAIRES POPULAIRES -->
        <?php $tpl->partial('components/line/itineraires', ['line' => $line]); ?>

        <!-- 8. QUE VOIR SUR LA LIGNE -->
        <?php $tpl->partial('components/line/que-voir', ['line' => $line]); ?>

        <!-- AdSlot 3 : in-article -->
        <?php $tpl->partial('ads/slot-in-article'); ?>

        <!-- 9. HISTOIRE DE LA LIGNE -->
        <?php $tpl->partial('components/line/histoire', ['line' => $line]); ?>

        <!-- 10. ACCESSIBILITÉ PMR -->
        <?php $tpl->partial('components/line/accessibilite', ['line' => $line]); ?>

        <!-- 11. TARIFS -->
        <?php $tpl->partial('components/line/tarifs', ['line' => $line]); ?>

        <!-- 12. TRAVAUX & FERMETURES -->
        <?php $tpl->partial('components/line/travaux', ['line' => $line]); ?>

        <!-- 13. FAQ -->
        <?php $tpl->partial('components/line/faq', ['line' => $line]); ?>

        <!-- AdSlot 4 : avant articles -->
        <?php $tpl->partial('ads/slot-in-article'); ?>

        <!-- 14. ARTICLES & ACTUALITÉS LIÉS -->
        <?php $tpl->partial('components/line/articles-lies', ['line' => $line]); ?>

        <!-- 15. LIENS INTERNES (cocon SEO) -->
        <?php $tpl->partial('components/line/liens-internes', ['line' => $line]); ?>

        <!-- 16. AUTEUR + DATES (E-E-A-T) -->
        <?php $tpl->partial('components/line/meta-auteur', ['line' => $line]); ?>

        <!-- AdSlot 5 : footer -->
        <?php $tpl->partial('ads/slot-footer'); ?>

    </div>
</article>
