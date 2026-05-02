<?php
/**
 * Section Itinéraires Populaires — Page ligne de métro
 *
 * - Calculateur d'itinéraire mini (widget)
 * - Top itinéraires populaires (cards)
 * - Itinéraires touristiques recommandés
 *
 * Variables attendues :
 * - $line : array, données de la ligne
 */

$popularRoutes = $line['popular_routes'] ?? [];
$touristRoutes = $line['tourist_routes'] ?? [];

// Helper pour générer le slug d'un itinéraire (URL SEO)
function routeSlug($from, $to) {
    return $from . '-vers-' . $to;
}
?>

<section class="section section--itineraires" id="itineraires" aria-labelledby="itineraires-title">

  <h2 id="itineraires-title">Itinéraires populaires sur la ligne <?= htmlspecialchars($line['code']) ?></h2>

  <div class="itineraires__intro">
    <?php if (!empty($line['intros']['itineraires'])): ?>
      <p><?= $line['intros']['itineraires'] ?></p>
    <?php else: ?>
      <p>Découvrez les <strong>trajets les plus recherchés</strong> sur la <strong>ligne <?= htmlspecialchars($line['code']) ?></strong> entre <strong><?= htmlspecialchars($line['terminus_a']) ?></strong> et <strong><?= htmlspecialchars($line['terminus_b']) ?></strong>.</p>
    <?php endif; ?>
  </div>

  <!-- Mini calculateur d'itinéraire -->
  <div class="itineraire-calc">
    <div class="itineraire-calc__icon" aria-hidden="true">🗺️</div>
    <div class="itineraire-calc__main">
      <div class="itineraire-calc__title">Calculer un itinéraire personnalisé</div>
      <div class="itineraire-calc__subtitle">De n'importe quelle adresse vers une station de la ligne <?= htmlspecialchars($line['code']) ?></div>
    </div>
    <a href="/itineraires/?line=<?= htmlspecialchars($line['code']) ?>" class="itineraire-calc__cta">
      Calculer →
    </a>
  </div>

  <!-- Top itinéraires populaires -->
  <h3 class="itineraires__subtitle">Les trajets les plus recherchés</h3>

  <div class="itineraire-grid">
    <?php foreach ($popularRoutes as $route): ?>
      <a href="/itineraires/<?= routeSlug($route['from']['slug'], $route['to']['slug']) ?>/" class="itineraire-card">

        <!-- Trajet : départ → arrivée -->
        <div class="itineraire-card__route">
          <div class="itineraire-card__from">
            <div class="itineraire-card__label">Départ</div>
            <div class="itineraire-card__station"><?= htmlspecialchars($route['from']['name']) ?></div>
          </div>
          <div class="itineraire-card__arrow" aria-hidden="true">→</div>
          <div class="itineraire-card__to">
            <div class="itineraire-card__label">Arrivée</div>
            <div class="itineraire-card__station"><?= htmlspecialchars($route['to']['name']) ?></div>
          </div>
        </div>

        <!-- Métadonnées du trajet -->
        <div class="itineraire-card__meta">
          <div class="itineraire-card__duration">
            <span aria-hidden="true">⏱️</span>
            <?= $route['duration_min'] ?> min
          </div>
          <div class="itineraire-card__transfers">
            <?php if ($route['transfers'] === 0): ?>
              <span class="itineraire-card__direct">Direct</span>
            <?php else: ?>
              <?= $route['transfers'] ?> correspondance<?= $route['transfers'] > 1 ? 's' : '' ?>
            <?php endif; ?>
          </div>
          <div class="itineraire-card__lines">
            <?php foreach ($route['lines'] as $lineNum): ?>
              <span class="itineraire-card__line-pill" style="background: <?= $lineNum === $line['code'] ? htmlspecialchars($line['color']) : '#E5E5E5' ?>; color: <?= $lineNum === $line['code'] ? htmlspecialchars($line['color_text']) : '#1A2B26' ?>;">
                <?= htmlspecialchars($lineNum) ?>
              </span>
            <?php endforeach; ?>
          </div>
        </div>

        <!-- Description -->
        <?php if (!empty($route['description'])): ?>
          <div class="itineraire-card__description"><?= htmlspecialchars($route['description']) ?></div>
        <?php endif; ?>

      </a>
    <?php endforeach; ?>
  </div>

  <!-- Itinéraires touristiques recommandés -->
  <?php if (!empty($touristRoutes)): ?>
    <h3 class="itineraires__subtitle">Itinéraires touristiques recommandés</h3>

    <div class="tourist-routes">
      <?php foreach ($touristRoutes as $route): ?>
        <article class="tourist-route">

          <div class="tourist-route__header">
            <div class="tourist-route__icon" aria-hidden="true"><?= htmlspecialchars($route['icon']) ?></div>
            <div class="tourist-route__title-wrapper">
              <h4 class="tourist-route__title"><?= htmlspecialchars($route['title']) ?></h4>
              <div class="tourist-route__duration">⏱️ <?= $route['duration_min'] ?> min</div>
            </div>
          </div>

          <p class="tourist-route__description"><?= htmlspecialchars($route['description']) ?></p>

          <div class="tourist-route__stops">
            <?php foreach ($route['stops'] as $i => $stop): ?>
              <span class="tourist-route__stop"><?= htmlspecialchars($stop) ?></span>
              <?php if ($i < count($route['stops']) - 1): ?>
                <span class="tourist-route__arrow" aria-hidden="true">›</span>
              <?php endif; ?>
            <?php endforeach; ?>
          </div>

        </article>
      <?php endforeach; ?>
    </div>
  <?php endif; ?>

  <!-- Lien vers tous les itinéraires -->
  <div class="itineraires__more">
    <a href="/itineraires/?line=<?= htmlspecialchars($line['code']) ?>" class="itineraires__more-link">
      Voir tous les itinéraires sur la ligne <?= htmlspecialchars($line['code']) ?> →
    </a>
  </div>

</section>
