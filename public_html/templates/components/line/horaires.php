<?php
/**
 * Section Horaires — Page ligne de métro
 *
 * Premier et dernier métro + tableau par jour + fréquence des rames.
 *
 * Variables attendues :
 * - $line : array, données de la ligne (incluant schedule)
 */

$schedule = $line['schedule'] ?? null;
if (!$schedule) {
    return; // Sécurité
}

$first = $schedule['first_departure'];
$last = $schedule['last_departure'];
$freq = $schedule['frequency'];
?>

<section class="section section--horaires" id="horaires" aria-labelledby="horaires-title">

  <h2 id="horaires-title">Horaires de la ligne <?= htmlspecialchars($line['code']) ?> : premier et dernier métro</h2>

  <div class="horaires__intro">
    <?php if (!empty($line['intros']['horaires'])): ?>
      <p><?= $line['intros']['horaires'] ?></p>
    <?php else: ?>
      <p>Le <strong>métro de la ligne <?= htmlspecialchars($line['code']) ?></strong> circule tous les jours, du <strong>premier départ à <?= htmlspecialchars($first['weekday']) ?></strong> jusqu'au <strong>dernier passage</strong> entre <?= htmlspecialchars($last['weekday']) ?> et <?= htmlspecialchars($last['friday']) ?> selon le jour. La <strong>fréquence des rames sur la ligne <?= htmlspecialchars($line['code']) ?></strong> varie de <?= htmlspecialchars($freq['peak_hours']['interval']) ?> en heure de pointe à <?= htmlspecialchars($freq['off_peak']['interval']) ?> en heures creuses.</p>
    <?php endif; ?>
  </div>

  <!-- Bloc 1 : Premier / Dernier métro (cards visuelles) -->
  <div class="horaires__highlights">

    <div class="schedule-card schedule-card--first">
      <div class="schedule-card__icon" aria-hidden="true">🌅</div>
      <div class="schedule-card__label">Premier métro</div>
      <div class="schedule-card__time"><?= htmlspecialchars($first['weekday']) ?></div>
      <div class="schedule-card__detail">Tous les jours</div>
    </div>

    <div class="schedule-card schedule-card--last">
      <div class="schedule-card__icon" aria-hidden="true">🌙</div>
      <div class="schedule-card__label">Dernier métro</div>
      <div class="schedule-card__time"><?= htmlspecialchars($last['weekday']) ?></div>
      <div class="schedule-card__detail">Du dimanche au jeudi</div>
    </div>

    <div class="schedule-card schedule-card--last-extended">
      <div class="schedule-card__icon" aria-hidden="true">🌃</div>
      <div class="schedule-card__label">Dernier métro <span class="schedule-card__badge">Service prolongé</span></div>
      <div class="schedule-card__time"><?= htmlspecialchars($last['friday']) ?></div>
      <div class="schedule-card__detail">Vendredi et samedi soir</div>
    </div>

  </div>

  <!-- Bloc 2 : Tableau détaillé par jour -->
  <h3 class="horaires__subtitle">Horaires détaillés par jour</h3>
  <div class="horaires__table-wrapper">
    <table class="horaires-table">
      <thead>
        <tr>
          <th scope="col">Jour</th>
          <th scope="col">Premier départ</th>
          <th scope="col">Dernier départ</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">Lundi</th>
          <td><?= htmlspecialchars($first['weekday']) ?></td>
          <td><?= htmlspecialchars($last['weekday']) ?></td>
        </tr>
        <tr>
          <th scope="row">Mardi</th>
          <td><?= htmlspecialchars($first['weekday']) ?></td>
          <td><?= htmlspecialchars($last['weekday']) ?></td>
        </tr>
        <tr>
          <th scope="row">Mercredi</th>
          <td><?= htmlspecialchars($first['weekday']) ?></td>
          <td><?= htmlspecialchars($last['weekday']) ?></td>
        </tr>
        <tr>
          <th scope="row">Jeudi</th>
          <td><?= htmlspecialchars($first['weekday']) ?></td>
          <td><?= htmlspecialchars($last['weekday']) ?></td>
        </tr>
        <tr class="horaires-table__row--extended">
          <th scope="row">Vendredi <span class="horaires-table__badge">Prolongé</span></th>
          <td><?= htmlspecialchars($first['weekday']) ?></td>
          <td><strong><?= htmlspecialchars($last['friday']) ?></strong></td>
        </tr>
        <tr class="horaires-table__row--extended">
          <th scope="row">Samedi <span class="horaires-table__badge">Prolongé</span></th>
          <td><?= htmlspecialchars($first['saturday']) ?></td>
          <td><strong><?= htmlspecialchars($last['saturday']) ?></strong></td>
        </tr>
        <tr>
          <th scope="row">Dimanche</th>
          <td><?= htmlspecialchars($first['sunday']) ?></td>
          <td><?= htmlspecialchars($last['sunday']) ?></td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Bloc 3 : Fréquence des rames -->
  <h3 class="horaires__subtitle">Fréquence des rames de la ligne <?= htmlspecialchars($line['code']) ?></h3>
  <div class="frequency-grid">

    <div class="frequency-card">
      <div class="frequency-card__label"><?= htmlspecialchars($freq['peak_hours']['label']) ?></div>
      <div class="frequency-card__interval"><?= htmlspecialchars($freq['peak_hours']['interval']) ?></div>
      <div class="frequency-card__times"><?= htmlspecialchars($freq['peak_hours']['times']) ?></div>
    </div>

    <div class="frequency-card">
      <div class="frequency-card__label"><?= htmlspecialchars($freq['off_peak']['label']) ?></div>
      <div class="frequency-card__interval"><?= htmlspecialchars($freq['off_peak']['interval']) ?></div>
      <div class="frequency-card__times"><?= htmlspecialchars($freq['off_peak']['times']) ?></div>
    </div>

    <div class="frequency-card">
      <div class="frequency-card__label"><?= htmlspecialchars($freq['evening']['label']) ?></div>
      <div class="frequency-card__interval"><?= htmlspecialchars($freq['evening']['interval']) ?></div>
      <div class="frequency-card__times"><?= htmlspecialchars($freq['evening']['times']) ?></div>
    </div>

    <div class="frequency-card">
      <div class="frequency-card__label"><?= htmlspecialchars($freq['weekend']['label']) ?></div>
      <div class="frequency-card__interval"><?= htmlspecialchars($freq['weekend']['interval']) ?></div>
      <div class="frequency-card__times"><?= htmlspecialchars($freq['weekend']['times']) ?></div>
    </div>

  </div>

  <!-- Note légale -->
  <p class="horaires__note">
    Les <strong>horaires</strong> et la <strong>fréquence</strong> des rames sont susceptibles d'évoluer en fonction de la situation du trafic. Pour les <strong>horaires en temps réel</strong>, consultez la section <a href="#trafic-temps-reel">trafic en temps réel</a>.
  </p>

</section>
