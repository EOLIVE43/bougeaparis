<?php
/**
 * Composant : Itinéraires populaires depuis une station
 *
 * Section éditoriale qui liste les 6-8 destinations les plus recherchées
 * depuis cette station, avec lignes empruntées, durée, nombre de changements.
 *
 * Stratégie hub-and-spoke V1 :
 * - Cette V1 affiche le contenu éditorial uniquement (pas de pages dédiées)
 * - Le lien « Voir tous les itinéraires » est posé en placeholder via Routes
 *   (futur cluster /itineraires/station-{slug}/)
 * - V2 : pages détaillées /itineraires/{station}/{station}-vers-{dest}/
 *
 * Variables attendues (props) :
 * - itineraries : array, format JSON station champ "popular_itineraries"
 * - stationName : string, nom de la station courante
 * - stationSlug : string, slug de la station courante (pour le lien hub V2)
 *
 * Si itineraries vide, le composant n'affiche rien.
 */

$itineraries = $props['itineraries'] ?? null;
$stationName = $props['stationName'] ?? null;
$stationSlug = $props['stationSlug'] ?? null;

if (empty($itineraries) || !is_array($itineraries)) {
    return;
}

$stationName = $stationName ?? 'cette station';
$count = count($itineraries);
$hubUrl = $stationSlug ? '/itineraires/station-' . $stationSlug . '/' : null;
$hubActive = $hubUrl ? Routes::exists(rtrim($hubUrl, '/')) : false;
?>

<section class="station-section section-itineraires" id="itineraires-populaires" aria-labelledby="itineraires-title">

  <h2 id="itineraires-title">Itinéraires populaires depuis <?= Template::e($stationName) ?></h2>

  <p class="section-intro">
    <?= Template::e($stationName) ?> est un point de départ stratégique pour rejoindre rapidement les principaux pôles de Paris et de la région Île-de-France. Voici les <strong><?= (int)$count ?> destinations</strong> les plus empruntées depuis cette station, avec les lignes utilisées, la durée estimée et le nombre de changements.
  </p>

  <ul class="itineraires-grid" role="list">
    <?php foreach ($itineraries as $it):
      $destName     = (string)($it['destination_name']      ?? '');
      $destFullName = (string)($it['destination_full_name'] ?? $destName);
      $destSlug     = (string)($it['destination_slug']      ?? '');
      $linesUsed    = $it['lines_used']      ?? [];
      $linesLabel   = (string)($it['lines_label'] ?? '');
      $duration     = (int)($it['duration_minutes'] ?? 0);
      $changes      = (int)($it['changes_count']    ?? 0);
      $futureUrl    = (string)($it['future_url']        ?? '');

      // Si une URL future existe ET qu'une page interne y répond déjà
      // (côté Routes), le titre devient cliquable. Sinon, c'est un span.
      $linkActive = $futureUrl !== '' && Routes::exists(rtrim($futureUrl, '/'));

      // Label « lignes » : préfère lines_label si fourni, sinon construit
      // depuis lines_used (ex: ["1"] → "Ligne 1", ["RER A"] → "RER A").
      if ($linesLabel === '' && is_array($linesUsed)) {
          $parts = [];
          foreach ($linesUsed as $l) {
              $l = (string)$l;
              if ($l === '') continue;
              if (ctype_digit($l)) {
                  $parts[] = 'Ligne ' . $l;
              } else {
                  $parts[] = $l;
              }
          }
          $linesLabel = implode(' + ', $parts);
      }

      $changesLabel = $changes === 0
          ? 'Trajet direct, 0 changement'
          : ($changes . ' changement' . ($changes > 1 ? 's' : ''));
    ?>
      <li class="itineraire-card">
        <div class="itineraire-card__header">
          <span class="itineraire-card__arrow" aria-hidden="true">→</span>
          <span class="itineraire-card__title"<?= $futureUrl !== '' ? ' data-future-url="' . Template::e($futureUrl) . '"' : '' ?>>
            <?php if ($linkActive): ?>
              <a href="<?= Template::e($futureUrl) ?>"><?= Template::e($destFullName) ?></a>
            <?php else: ?>
              <strong><?= Template::e($destFullName) ?></strong>
            <?php endif; ?>
          </span>
        </div>
        <dl class="itineraire-card__meta">
          <?php if ($linesLabel !== ''): ?>
            <div class="itineraire-card__row">
              <dt class="itineraire-card__label">Lignes</dt>
              <dd class="itineraire-card__value"><?= Template::e($linesLabel) ?></dd>
            </div>
          <?php endif; ?>
          <?php if ($duration > 0): ?>
            <div class="itineraire-card__row">
              <dt class="itineraire-card__label">Durée</dt>
              <dd class="itineraire-card__value">~<?= (int)$duration ?> min</dd>
            </div>
          <?php endif; ?>
          <div class="itineraire-card__row">
            <dt class="itineraire-card__label">Changements</dt>
            <dd class="itineraire-card__value"><?= Template::e($changesLabel) ?></dd>
          </div>
        </dl>
      </li>
    <?php endforeach; ?>
  </ul>

  <?php
  // Tache 3 : toggle de masquage de la card "Voir tous les itineraires".
  // Default false : la card disparait de toutes les pages stations
  // (l'utilisateur la jugeait frustrante quand cocon /itineraires/ pas pret).
  // Reactiver (= true) quand le cocon /itineraires/ sera lance (Phase 3).
  $itinerariesHubExists = false;
  ?>
  <?php if ($hubUrl && $itinerariesHubExists): ?>
    <div class="itineraires-hub-link">
      <?php if ($hubActive): ?>
        <a href="<?= Template::e($hubUrl) ?>" class="itineraires-hub-link__btn">
          Voir tous les itinéraires depuis <?= Template::e($stationName) ?> →
        </a>
      <?php else: ?>
        <span class="itineraires-hub-link__btn itineraires-hub-link__btn--inactive"
              data-future-url="<?= Template::e($hubUrl) ?>"
              aria-disabled="true">
          Voir tous les itinéraires depuis <?= Template::e($stationName) ?> <span aria-hidden="true">(bientôt)</span>
        </span>
      <?php endif; ?>
    </div>
  <?php endif; ?>

</section>
