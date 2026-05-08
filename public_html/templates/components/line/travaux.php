<?php
/**
 * Section Travaux & fermetures — Page ligne de métro
 *
 * Affiche les travaux en cours, à venir et récemment terminés.
 *
 * Variables attendues :
 * - $line : array, données de la ligne (incluant 'works' et 'intros.travaux')
 *
 * Stratégie SEO :
 * - H2 unique avec "ligne X" + "travaux"
 * - H3 par catégorie (en cours, à venir, terminés)
 * - Mots-clés : "travaux", "fermeture", "rénovation", "modernisation"
 *
 * Stratégie Discover :
 * - Date "last_updated" visible (signal de fraîcheur)
 * - Dates précises des travaux (utilité immédiate)
 * - CTA "S'inscrire aux alertes" (engagement)
 */

$works = $line['works'] ?? null;
if (!$works) {
    return;
}

$introText = $line['intros']['travaux'] ?? null;

// Format date dernière MAJ
$lastUpdated = !empty($works['last_updated']) ? date('d/m/Y', strtotime($works['last_updated'])) : '';

// Helper severity → couleur
function getSeverityClass($severity) {
    return match($severity) {
        'high' => 'severity-high',
        'medium' => 'severity-medium',
        'low' => 'severity-low',
        default => 'severity-low',
    };
}
?>

<section class="section section--travaux" id="travaux" aria-labelledby="travaux-title">

  <h2 id="travaux-title">Travaux et fermetures sur la ligne <?= htmlspecialchars($line['code']) ?> du métro</h2>

  <!-- Intro -->
  <div class="travaux__intro">
    <?php if ($introText): ?>
      <p><?= $introText ?></p>
    <?php else: ?>
      <p>Retrouvez les <strong>travaux et fermetures</strong> programmés sur la <strong>ligne <?= htmlspecialchars($line['code']) ?> du métro parisien</strong>.</p>
    <?php endif; ?>
  </div>

  <!-- Statut global -->
  <?php if (!empty($works['current_works'])): ?>
    <div class="works-status works-status--has-works">
      <span class="works-status__icon" aria-hidden="true">⚠️</span>
      <div class="works-status__content">
        <div class="works-status__title">Travaux en cours sur la ligne <?= htmlspecialchars($line['code']) ?></div>
        <div class="works-status__detail"><?= count($works['current_works']) ?> perturbation<?= count($works['current_works']) > 1 ? 's' : '' ?> en cours · Voir le détail ci-dessous</div>
      </div>
    </div>
  <?php else: ?>
    <div class="works-status works-status--clear">
      <span class="works-status__icon" aria-hidden="true">✅</span>
      <div class="works-status__content">
        <div class="works-status__title">Aucun travaux en cours sur la ligne <?= htmlspecialchars($line['code']) ?></div>
        <div class="works-status__detail">Le trafic circule normalement entre <?= htmlspecialchars($line['terminus_a']) ?> et <?= htmlspecialchars($line['terminus_b']) ?></div>
      </div>
    </div>
  <?php endif; ?>

  <!-- TRAVAUX EN COURS -->
  <?php if (!empty($works['current_works'])): ?>
    <h3 class="travaux__subtitle">⚠️ Travaux et fermetures en cours</h3>
    <div class="works-list">
      <?php foreach ($works['current_works'] as $work): ?>
        <article class="work-card work-card--current <?= getSeverityClass($work['severity'] ?? 'low') ?>">
          <div class="work-card__header">
            <span class="work-card__icon" aria-hidden="true"><?= htmlspecialchars($work['icon']) ?></span>
            <div class="work-card__header-content">
              <h4 class="work-card__title"><?= htmlspecialchars($work['title']) ?></h4>
              <div class="work-card__dates">
                <span class="work-card__dates-icon" aria-hidden="true">📅</span>
                <time><?= htmlspecialchars($work['dates_label']) ?></time>
                <?php if (!empty($work['weekends_only'])): ?>
                  <span class="work-card__weekends-badge">Week-ends uniquement</span>
                <?php endif; ?>
              </div>
            </div>
          </div>

          <p class="work-card__description"><?= richText($work['description'] ?? '') ?></p>

          <?php if (!empty($work['stations_affected'])): ?>
            <div class="work-card__stations">
              <div class="work-card__stations-label">🚇 Stations concernées</div>
              <div class="work-card__stations-list">
                <?php foreach ($work['stations_affected'] as $station): ?>
                  <span class="work-station"><?= htmlspecialchars($station) ?></span>
                <?php endforeach; ?>
              </div>
            </div>
          <?php endif; ?>

          <?php if (!empty($work['alternatives'])): ?>
            <div class="work-card__alternatives">
              <div class="work-card__alternatives-label">💡 Alternatives proposées</div>
              <ul class="work-card__alternatives-list">
                <?php foreach ($work['alternatives'] as $alt): ?>
                  <li><?= htmlspecialchars($alt) ?></li>
                <?php endforeach; ?>
              </ul>
            </div>
          <?php endif; ?>
        </article>
      <?php endforeach; ?>
    </div>
  <?php endif; ?>

  <!-- TRAVAUX À VENIR -->
  <?php if (!empty($works['upcoming_works'])): ?>
    <h3 class="travaux__subtitle">📅 Travaux à venir sur la ligne <?= htmlspecialchars($line['code']) ?></h3>
    <div class="works-list">
      <?php foreach ($works['upcoming_works'] as $work): ?>
        <article class="work-card work-card--upcoming">
          <div class="work-card__header">
            <span class="work-card__icon" aria-hidden="true"><?= htmlspecialchars($work['icon']) ?></span>
            <div class="work-card__header-content">
              <h4 class="work-card__title"><?= htmlspecialchars($work['title']) ?></h4>
              <div class="work-card__dates">
                <span class="work-card__dates-icon" aria-hidden="true">📅</span>
                <time><?= htmlspecialchars($work['dates_label']) ?></time>
              </div>
            </div>
          </div>

          <p class="work-card__description"><?= richText($work['description'] ?? '') ?></p>

          <?php if (!empty($work['stations_affected'])): ?>
            <div class="work-card__stations">
              <div class="work-card__stations-label">🚇 Stations concernées</div>
              <div class="work-card__stations-list">
                <?php foreach ($work['stations_affected'] as $station): ?>
                  <span class="work-station"><?= htmlspecialchars($station) ?></span>
                <?php endforeach; ?>
              </div>
            </div>
          <?php endif; ?>
        </article>
      <?php endforeach; ?>
    </div>
  <?php endif; ?>

  <!-- TRAVAUX RÉCEMMENT TERMINÉS -->
  <?php if (!empty($works['recent_works'])): ?>
    <h3 class="travaux__subtitle">✅ Travaux récemment terminés</h3>
    <div class="works-completed-list">
      <?php foreach ($works['recent_works'] as $work): ?>
        <div class="work-completed">
          <span class="work-completed__icon" aria-hidden="true"><?= htmlspecialchars($work['icon']) ?></span>
          <div class="work-completed__content">
            <div class="work-completed__title"><?= htmlspecialchars($work['title']) ?></div>
            <div class="work-completed__date"><?= htmlspecialchars($work['completed_label']) ?></div>
            <p class="work-completed__desc"><?= richText($work['description'] ?? '') ?></p>
          </div>
        </div>
      <?php endforeach; ?>
    </div>
  <?php endif; ?>

  <!-- CTA Calendrier complet -->
  <?php if (!empty($works['calendar_url'])): ?>
    <div class="travaux__cta">
      <div class="travaux__cta-icon" aria-hidden="true">🗓️</div>
      <div class="travaux__cta-content">
        <div class="travaux__cta-label">Calendrier complet</div>
        <div class="travaux__cta-title">Tous les travaux planifiés sur la ligne <?= htmlspecialchars($line['code']) ?> jusqu'en 2027</div>
      </div>
      <a href="<?= htmlspecialchars($works['calendar_url']) ?>" class="travaux__cta-btn">Voir le calendrier →</a>
    </div>
  <?php endif; ?>

  <!-- Note de mise à jour -->
  <p class="travaux__update-note">
    Informations mises à jour le <?= htmlspecialchars($lastUpdated) ?>. Source officielle&nbsp;: <strong>Île-de-France Mobilités</strong> et RATP.
  </p>

</section>
