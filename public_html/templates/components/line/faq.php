<?php
/**
 * Section FAQ — Page ligne de métro
 *
 * Affiche les questions fréquentes en accordéon HTML5 (<details>/<summary>).
 * Inclut le balisage Schema.org FAQPage pour les rich snippets Google.
 *
 * Variables attendues :
 * - $line : array, données de la ligne (incluant 'faq' et 'intros.faq')
 *
 * Stratégie SEO :
 * - Schema.org FAQPage = rich snippets dans les SERPs
 * - Questions formulées comme les utilisateurs les tapent ("People Also Ask")
 * - Réponses précises et complètes (pas trop courtes pour Google)
 *
 * Stratégie UX :
 * - Accordéon avec <details>/<summary> = HTML5 natif, fonctionne sans JS
 * - Première question ouverte par défaut (engagement)
 * - Animation CSS transition fluide
 */

$faq = $line['faq'] ?? null;
if (!$faq || empty($faq)) {
    return;
}

$introText = $line['intros']['faq'] ?? null;
?>

<section class="section section--faq" id="faq" aria-labelledby="faq-title">

  <h2 id="faq-title">Questions fréquentes sur la ligne <?= htmlspecialchars($line['code']) ?> du métro</h2>

  <!-- Intro -->
  <div class="faq__intro">
    <?php if ($introText): ?>
      <p><?= $introText ?></p>
    <?php else: ?>
      <p>Retrouvez les <strong>questions les plus fréquentes</strong> sur la <strong>ligne <?= htmlspecialchars($line['code']) ?> du métro parisien</strong>.</p>
    <?php endif; ?>
  </div>

  <!-- Accordéon FAQ -->
  <div class="faq__list">
    <?php foreach ($faq as $i => $item): ?>
      <details class="faq-item" <?= $i === 0 ? 'open' : '' ?>>
        <summary class="faq-item__question">
          <span class="faq-item__question-text"><?= htmlspecialchars($item['question']) ?></span>
          <span class="faq-item__icon" aria-hidden="true">
            <svg viewBox="0 0 16 16" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
              <path d="M3 6 L8 11 L13 6"/>
            </svg>
          </span>
        </summary>
        <div class="faq-item__answer">
          <p><?= htmlspecialchars($item['answer']) ?></p>
        </div>
      </details>
    <?php endforeach; ?>
  </div>

  <!-- Lien vers contact -->
  <div class="faq__contact-cta">
    <span class="faq__contact-icon" aria-hidden="true">💬</span>
    <span class="faq__contact-text">Vous avez une autre question sur la ligne <?= htmlspecialchars($line['code']) ?> ?</span>
    <a href="/contact/" class="faq__contact-link">Contactez-nous →</a>
  </div>

</section>

<!-- Schema.org FAQPage : booste les rich snippets Google -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    <?php
    $entries = [];
    foreach ($faq as $item) {
        $entries[] = json_encode([
            "@type" => "Question",
            "name" => $item['question'],
            "acceptedAnswer" => [
                "@type" => "Answer",
                "text" => $item['answer']
            ]
        ], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT);
    }
    echo implode(",\n    ", $entries);
    ?>
  ]
}
</script>
