<?php
/**
 * Section Tarifs — Page ligne de métro
 *
 * Affiche les tarifs essentiels pour emprunter la ligne :
 * - Intro contextuelle
 * - 4 cards principaux tarifs (ticket, jour, mensuel, aéroport)
 * - Tarifs additionnels en liste compacte
 * - Lien vers page /tarifs/ complète
 * - Mention de la dernière mise à jour
 *
 * Variables attendues :
 * - $line : array, données de la ligne (incluant 'fares' et 'intros.tarifs')
 *
 * Stratégie SEO :
 * - H2 unique avec "ligne X" + "tarifs"
 * - Mots-clés : "tarif métro", "prix ticket", "Pass Navigo"
 * - Schema.org : pas de schéma standard pour les tarifs (pas Product, on n'est pas e-commerce)
 */

$fares = $line['fares'] ?? null;
if (!$fares) {
    return;
}

$introText = $line['intros']['tarifs'] ?? null;

// Format date de dernière vérif
$lastCheck = !empty($fares['last_check']) ? date('d/m/Y', strtotime($fares['last_check'])) : '';
$validSince = !empty($fares['valid_since']) ? date('d/m/Y', strtotime($fares['valid_since'])) : '';
?>

<section class="section section--tarifs" id="tarifs" aria-labelledby="tarifs-title">

  <h2 id="tarifs-title">Tarifs et titres de transport pour la ligne <?= htmlspecialchars($line['code']) ?></h2>

  <!-- Intro -->
  <div class="tarifs__intro">
    <?php if ($introText): ?>
      <p><?= $introText ?></p>
    <?php else: ?>
      <p>Pour emprunter la <strong>ligne <?= htmlspecialchars($line['code']) ?> du métro parisien</strong>, plusieurs <strong>titres de transport</strong> sont disponibles selon votre profil et votre fréquence d'utilisation.</p>
    <?php endif; ?>
  </div>

  <!-- Cards des 4 tarifs principaux -->
  <div class="tarifs__main">
    <?php foreach ($fares['main_fares'] as $fare): ?>
      <article class="fare-card <?= !empty($fare['is_popular']) ? 'fare-card--popular' : '' ?>">

        <?php if (!empty($fare['is_popular'])): ?>
          <div class="fare-card__badge">⭐ Le plus populaire</div>
        <?php endif; ?>

        <div class="fare-card__header">
          <div class="fare-card__icon" aria-hidden="true"><?= htmlspecialchars($fare['icon']) ?></div>
          <div class="fare-card__title-wrap">
            <h3 class="fare-card__label"><?= htmlspecialchars($fare['label']) ?></h3>
            <?php if (!empty($fare['subtitle'])): ?>
              <div class="fare-card__subtitle"><?= htmlspecialchars($fare['subtitle']) ?></div>
            <?php endif; ?>
          </div>
        </div>

        <div class="fare-card__price-wrap">
          <span class="fare-card__price"><?= htmlspecialchars($fare['price']) ?></span>
          <span class="fare-card__currency">€</span>
        </div>

        <?php if (!empty($fare['price_reduced'])): ?>
          <div class="fare-card__price-reduced">
            Tarif réduit&nbsp;: <strong><?= htmlspecialchars($fare['price_reduced']) ?> €</strong>
          </div>
        <?php endif; ?>

        <p class="fare-card__description"><?= htmlspecialchars($fare['description']) ?></p>

        <?php if (!empty($fare['best_for'])): ?>
          <div class="fare-card__best-for">
            <span class="fare-card__best-for-label">💡 Idéal pour</span>
            <span class="fare-card__best-for-text"><?= htmlspecialchars($fare['best_for']) ?></span>
          </div>
        <?php endif; ?>

      </article>
    <?php endforeach; ?>
  </div>

  <!-- Tarifs additionnels (liste compacte) -->
  <?php if (!empty($fares['additional_fares'])): ?>
    <div class="tarifs__additional">
      <h3 class="tarifs__subtitle">Autres tarifs disponibles</h3>
      <div class="additional-fares-grid">
        <?php foreach ($fares['additional_fares'] as $fare): ?>
          <div class="additional-fare">
            <span class="additional-fare__label"><?= htmlspecialchars($fare['label']) ?></span>
            <span class="additional-fare__price"><?= htmlspecialchars($fare['price']) ?> €</span>
          </div>
        <?php endforeach; ?>
      </div>
    </div>
  <?php endif; ?>

  <!-- CTA vers page tarifs complète -->
  <div class="tarifs__cta">
    <div class="tarifs__cta-icon" aria-hidden="true">💳</div>
    <div class="tarifs__cta-content">
      <div class="tarifs__cta-label">Tous les tarifs en détail</div>
      <div class="tarifs__cta-title">Comparez les tarifs Métro, RER, Bus, Tram et choisissez le titre le plus adapté</div>
    </div>
    <a href="/tarifs/" class="tarifs__cta-btn">Voir tous les tarifs →</a>
  </div>

  <!-- Mention mise à jour -->
  <p class="tarifs__update-note">
    Tarifs en vigueur depuis le <?= htmlspecialchars($validSince) ?>. Source officielle&nbsp;:
    <a href="<?= htmlspecialchars($fares['source_url']) ?>" rel="noopener noreferrer" target="_blank"><strong>Île-de-France Mobilités</strong></a>.
    <?php if ($lastCheck): ?>
      Dernière vérification&nbsp;: <?= htmlspecialchars($lastCheck) ?>.
    <?php endif; ?>
  </p>

</section>
