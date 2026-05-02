<?php
/**
 * Section Trafic Temps Réel — Page ligne de métro
 *
 * Affiche le détail du trafic via PRIM API (cache 30s).
 * En cas de trafic normal : message "tout va bien".
 * En cas de perturbations : liste détaillée.
 *
 * Variables attendues :
 * - $line : array, données de la ligne
 *
 * TODO L4.3 :
 * - Lire data/traffic/latest.json (généré par PRIM)
 * - Filtrer les perturbations sur cette ligne
 * - Afficher dynamiquement
 */

// MOCK DATA (à remplacer par lecture latest.json)
$trafficStatus = 'ok'; // 'ok' | 'warn' | 'bad'
$lastUpdate = '32 secondes';
$perturbations = []; // En prod : récupérer depuis latest.json filtré par ligne

// Pour démo, on peut simuler des perturbations (à commenter en prod)
// $trafficStatus = 'warn';
// $perturbations = [
//   ['type' => 'works', 'title' => 'Travaux nocturnes', 'description' => '...', 'zone' => '...'],
// ];

$todayDate = date('d/m/Y');
$todayHuman = strftime('%A %d %B %Y', time());
?>

<section class="section section--trafic" id="trafic-temps-reel" aria-labelledby="trafic-title">

  <h2 id="trafic-title">Trafic en temps réel sur la ligne <?= htmlspecialchars($line['code']) ?></h2>

  <div class="trafic__intro">
    <?php if (!empty($line['intros']['trafic'])): ?>
      <p><?= $line['intros']['trafic'] ?></p>
    <?php else: ?>
      <p>Consultez en direct le <strong>trafic de la ligne <?= htmlspecialchars($line['code']) ?></strong> du métro parisien. Les <strong>informations trafic de la ligne <?= htmlspecialchars($line['code']) ?></strong> sont actualisées toutes les 30 secondes pour vous permettre d'<strong>anticiper vos déplacements</strong> entre <strong><?= htmlspecialchars($line['terminus_a']) ?></strong> et <strong><?= htmlspecialchars($line['terminus_b']) ?></strong>.</p>
    <?php endif; ?>
  </div>

  <!-- Widget statut LIVE -->
  <div class="trafic-live trafic-live--<?= $trafficStatus ?>" role="status" aria-live="polite">

    <div class="trafic-live__indicator">
      <span class="trafic-live__dot" aria-hidden="true"></span>
      <span class="trafic-live__label">EN DIRECT</span>
    </div>

    <div class="trafic-live__main">

      <?php if ($trafficStatus === 'ok'): ?>

        <h3 class="trafic-live__title">Trafic normal sur la ligne <?= htmlspecialchars($line['code']) ?></h3>
        <p class="trafic-live__description">
          Aucune perturbation signalée. Les rames circulent à fréquence habituelle entre <?= htmlspecialchars($line['terminus_a']) ?> et <?= htmlspecialchars($line['terminus_b']) ?>.
        </p>

      <?php elseif ($trafficStatus === 'warn'): ?>

        <h3 class="trafic-live__title">Trafic perturbé sur la ligne <?= htmlspecialchars($line['code']) ?></h3>
        <p class="trafic-live__description">
          Des perturbations sont en cours. Voir le détail ci-dessous.
        </p>

      <?php else: ?>

        <h3 class="trafic-live__title">Trafic fortement perturbé sur la ligne <?= htmlspecialchars($line['code']) ?></h3>
        <p class="trafic-live__description">
          Des incidents importants affectent le trafic. Privilégiez un autre itinéraire.
        </p>

      <?php endif; ?>

    </div>

    <div class="trafic-live__actions">
      <div class="trafic-live__update">
        Mis à jour il y a <?= htmlspecialchars($lastUpdate) ?>
      </div>
      <button type="button" class="trafic-live__refresh" aria-label="Actualiser le trafic">
        <span class="trafic-live__refresh-icon" aria-hidden="true">↻</span>
        Actualiser
      </button>
    </div>

  </div>

  <!-- Liste des perturbations (si présentes) -->
  <?php if (!empty($perturbations)): ?>

    <h3 class="trafic__subtitle">Détail des perturbations en cours</h3>

    <div class="perturbation-list">
      <?php foreach ($perturbations as $perturbation): ?>
        <article class="perturbation">
          <div class="perturbation__icon" aria-hidden="true">
            <?= $perturbation['type'] === 'works' ? '🔧' : ($perturbation['type'] === 'incident' ? '⚠️' : 'ℹ️') ?>
          </div>
          <div class="perturbation__content">
            <h4 class="perturbation__title"><?= htmlspecialchars($perturbation['title']) ?></h4>
            <p class="perturbation__description"><?= htmlspecialchars($perturbation['description']) ?></p>
            <?php if (!empty($perturbation['zone'])): ?>
              <div class="perturbation__zone">
                <strong>Zone concernée :</strong> <?= htmlspecialchars($perturbation['zone']) ?>
              </div>
            <?php endif; ?>
          </div>
        </article>
      <?php endforeach; ?>
    </div>

  <?php endif; ?>

  <!-- Lien vers le bulletin trafic du jour -->
  <div class="trafic__bulletin-link">
    <div class="trafic__bulletin-link-icon" aria-hidden="true">📰</div>
    <div class="trafic__bulletin-link-content">
      <div class="trafic__bulletin-link-label">Bulletin trafic du <?= htmlspecialchars($todayDate) ?></div>
      <div class="trafic__bulletin-link-title">Découvrez le bulletin info trafic complet du réseau parisien</div>
    </div>
    <a href="/info-trafic/" class="trafic__bulletin-link-cta">Lire le bulletin →</a>
  </div>

  <!-- Source officielle -->
  <p class="trafic__source">
    Source : <strong>Île-de-France Mobilités</strong>. Données mises à jour toutes les 30 secondes.
  </p>

</section>
