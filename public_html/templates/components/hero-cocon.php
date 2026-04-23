<?php
/**
 * Composant hero-cocon : hero des pages hub transport.
 *
 * Props :
 *   - h1       : titre principal
 *   - subtitle : sous-titre
 *   - chiffres : array de [['value'=>'16', 'label'=>'Lignes'], ...]
 */

$h1       = $props['h1']       ?? '';
$subtitle = $props['subtitle'] ?? '';
$chiffres = $props['chiffres'] ?? [];
?>
<section class="hero-cocon">
    <div class="hero-cocon__inner">
        <h1 class="hero-cocon__title"><?= htmlspecialchars($h1) ?></h1>
        <?php if ($subtitle): ?>
            <p class="hero-cocon__subtitle"><?= htmlspecialchars($subtitle) ?></p>
        <?php endif; ?>

        <?php if (!empty($chiffres)): ?>
            <ul class="hero-cocon__stats" role="list">
                <?php foreach ($chiffres as $c): ?>
                    <li class="hero-cocon__stat">
                        <span class="hero-cocon__stat-value"><?= htmlspecialchars($c['value'] ?? '') ?></span>
                        <span class="hero-cocon__stat-label"><?= htmlspecialchars($c['label'] ?? '') ?></span>
                    </li>
                <?php endforeach; ?>
            </ul>
        <?php endif; ?>
    </div>
</section>
