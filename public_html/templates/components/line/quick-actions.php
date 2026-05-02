<?php
/**
 * Quick Actions (chips d'action rapide)
 *
 * 3 raccourcis vers les actions les plus recherchées :
 * - Trafic en direct (point pulsé)
 * - Calculer un itinéraire
 * - Voir les tarifs
 *
 * Stratégie : utiliser display:table au lieu de flex/grid pour compatibilité maximale
 * (y compris navigateurs anciens et outils de rendu type wkhtmltoimage)
 */

$actions = $line['quick_actions'] ?? null;
if (!$actions || empty($actions)) {
    return;
}
?>

<div class="quick-actions" aria-label="Actions rapides">
  <?php foreach ($actions as $action): ?>
    <a href="<?= htmlspecialchars($action['anchor']) ?>" class="quick-action <?= $action['type'] === 'live' ? 'quick-action--live' : '' ?>">
      <span class="quick-action__inner">
        <span class="quick-action__icon">
          <?php if ($action['type'] === 'live'): ?>
            <span class="quick-action__icon-dot" aria-hidden="true"></span>
          <?php else: ?>
            <?= htmlspecialchars($action['icon']) ?>
          <?php endif; ?>
        </span>
        <span class="quick-action__content">
          <span class="quick-action__label"><?= htmlspecialchars($action['label']) ?></span>
          <span class="quick-action__title"><?= htmlspecialchars($action['title']) ?></span>
        </span>
        <span class="quick-action__arrow" aria-hidden="true">→</span>
      </span>
    </a>
  <?php endforeach; ?>
</div>

<script>
(function() {
  document.documentElement.style.scrollPaddingTop = '90px';
  document.querySelectorAll('.quick-action').forEach(link => {
    link.addEventListener('click', e => {
      const href = link.getAttribute('href');
      if (href && href.startsWith('#')) {
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  });
})();
</script>
