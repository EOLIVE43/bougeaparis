<?php
/**
 * Composant faq-accordion avec balisage schema.org FAQPage.
 *
 * Props :
 *   - title       : titre de la section
 *   - items       : array de [['question'=>'', 'answer'=>''], ...]
 *   - emit_schema : emettre le JSON-LD (defaut true)
 */

$title      = $props['title']       ?? 'Questions frequentes';
$items      = $props['items']       ?? [];
$emitSchema = $props['emit_schema'] ?? true;

if (empty($items)) return;
?>

<section class="faq-section" aria-labelledby="faq-title">
    <h2 class="faq-section__title" id="faq-title"><?= htmlspecialchars($title) ?></h2>

    <div class="faq-accordion">
        <?php foreach ($items as $idx => $item):
            $question = $item['question'] ?? '';
            $answer   = $item['answer']   ?? '';
        ?>
            <details class="faq-accordion__item">
                <summary class="faq-accordion__question">
                    <span><?= htmlspecialchars($question) ?></span>
                    <span class="faq-accordion__icon" aria-hidden="true">+</span>
                </summary>
                <div class="faq-accordion__answer">
                    <?= $answer /* HTML autorise */ ?>
                </div>
            </details>
        <?php endforeach; ?>
    </div>
</section>

<?php if ($emitSchema): ?>
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
<?php foreach ($items as $idx => $item):
    $q = json_encode(strip_tags($item['question'] ?? ''), JSON_UNESCAPED_UNICODE);
    $a = json_encode(strip_tags($item['answer']   ?? ''), JSON_UNESCAPED_UNICODE);
?>
        {
            "@type": "Question",
            "name": <?= $q ?>,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": <?= $a ?>
            }
        }<?= ($idx < count($items) - 1) ? ',' : '' ?>
<?php endforeach; ?>
    ]
}
</script>
<?php endif; ?>
