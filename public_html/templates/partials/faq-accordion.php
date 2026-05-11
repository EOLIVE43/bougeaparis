<?php
/**
 * Partial : faq-accordion
 *
 * FAQ pliable native <details>/<summary> (zero JS, a11y clavier gratuit).
 * Reutilisable sur /tarifs/, /se-deplacer/, /visiter/.
 *
 * Variables attendues (set par l'appelant via include) :
 *   $faqs      (array)  : liste de [q => string, a => string].
 *                         La reponse 'a' supporte richText (<strong><em><a>).
 *   $openFirst (bool)   : si true (defaut), 1ere question deja ouverte.
 *
 * Note : le helper richText() doit etre disponible (helpers.php charge dans
 * bootstrap.php, donc dispo partout).
 */
$faqs      = $faqs      ?? [];
$openFirst = $openFirst ?? true;
if (empty($faqs)) return;
?>
<div class="faq-accordion">
    <?php foreach ($faqs as $i => $f): ?>
        <details class="faq-accordion__item"<?= ($openFirst && $i === 0) ? ' open' : '' ?>>
            <summary><h3><?= htmlspecialchars($f['q'] ?? '', ENT_QUOTES, 'UTF-8') ?></h3></summary>
            <div class="faq-accordion__answer"><p><?= richText($f['a'] ?? '') ?></p></div>
        </details>
    <?php endforeach; ?>
</div>
