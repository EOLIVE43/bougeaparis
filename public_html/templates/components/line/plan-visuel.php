<?php
/**
 * Section Plan Visuel — Page ligne de métro
 *
 * Affiche la frise horizontale de la ligne :
 * - Trait coloré horizontal
 * - Cercles centrés sur la ligne (terminus, pôles majeurs, stations classiques)
 * - Noms de stations inclinés en bas
 * - Pastilles de correspondance en haut (SVG cohérent avec helpers)
 * - Étiquettes culturelles teal sous les noms
 *
 * v1.3 :
 * - Pastilles uniformisées via pastilleCorresp() (style bord blanc)
 * - Bouton "Agrandir" qui ouvre une lightbox plein écran
 * - Scroll horizontal propre sur mobile (pas de double scrollbar)
 *
 * Variables attendues :
 * - $line : array, données de la ligne (depuis JSON)
 */

$stations = $line['stations'];
$totalStations = count($stations);
$lineColor = $line['color'] ?? '#0F6E56';
?>

<section class="section section--plan-visuel" id="plan-visuel" aria-labelledby="plan-title">

  <h2 id="plan-title">Plan de la ligne <?= htmlspecialchars($line['code']) ?> du métro parisien</h2>

  <div class="plan-visuel__intro">
    <?php if (!empty($line['intros']['plan'])): ?>
      <p><?= $line['intros']['plan'] ?></p>
    <?php else: ?>
      <p>Découvrez le <strong>plan de la ligne <?= htmlspecialchars($line['code']) ?> du métro de Paris</strong> : les <?= htmlspecialchars($totalStations) ?> stations entre <strong><?= htmlspecialchars($line['terminus_a']) ?></strong> et <strong><?= htmlspecialchars($line['terminus_b']) ?></strong>, toutes les correspondances et les principaux points d'intérêt.</p>
    <?php endif; ?>
  </div>

  <!-- LE PLAN -->
  <figure class="line-plan" role="img" aria-label="Plan de la ligne <?= htmlspecialchars($line['code']) ?> du métro de Paris, de <?= htmlspecialchars($line['terminus_a']) ?> à <?= htmlspecialchars($line['terminus_b']) ?>">

    <!-- Bouton Agrandir (lightbox) -->
    <button type="button"
            class="line-plan__zoom-btn"
            data-lightbox-target="line-plan-content"
            aria-label="Agrandir le plan de la ligne <?= htmlspecialchars($line['code']) ?>">
      <span class="line-plan__zoom-icon" aria-hidden="true">⛶</span>
      <span class="line-plan__zoom-label">Agrandir</span>
    </button>

    <div class="line-plan__scroll-wrapper" id="line-plan-content">
      <div class="line-plan__frise" style="--line-color: <?= htmlspecialchars($lineColor) ?>;">

        <!-- La ligne horizontale colorée -->
        <div class="line-plan__line" aria-hidden="true"></div>

        <!-- Les stations -->
        <div class="line-plan__stations">

          <?php foreach ($stations as $station): ?>
            <div class="line-plan__station <?= ($station['is_major'] ?? false) ? 'line-plan__station--major' : '' ?>">

              <!-- Pastilles de correspondance (SVG, style cohérent avec le tableau) -->
              <?php if (!empty($station['correspondences'])): ?>
                <div class="line-plan__corresp">
                  <?php foreach ($station['correspondences'] as $corresp): ?>
                    <?= pastilleCorresp(
                        $corresp['mode'],
                        $corresp['line'],
                        $corresp['color'],
                        'small'
                    ) ?>
                  <?php endforeach; ?>
                </div>
                <div class="line-plan__connector" aria-hidden="true"></div>
              <?php endif; ?>

              <!-- Le rond de la station (centré sur la ligne) -->
              <div class="line-plan__dot <?= ($station['is_major'] ?? false) ? 'line-plan__dot--major' : 'line-plan__dot--small' ?>"
                   <?= ($station['is_major'] ?? false) ? '' : 'aria-hidden="true"' ?>></div>

              <!-- Nom de la station (sous la ligne, incliné).
                   wrapStationName() casse les noms longs sur 2 lignes au tiret
                   de séparation (ex: "La Motte-Picquet - Grenelle"). HTML déjà
                   échappé par le helper. -->
              <div class="line-plan__name <?= ($station['is_major'] ?? false) ? 'line-plan__name--major' : '' ?>">
                <?= wrapStationName($station['name']) ?>
              </div>

              <!-- Étiquette culturelle teal -->
              <?php if (!empty($station['cultural_label'])): ?>
                <div class="line-plan__label">
                  <?= str_replace("\n", '<br>', htmlspecialchars($station['cultural_label'])) ?>
                </div>
              <?php endif; ?>

            </div>
          <?php endforeach; ?>

        </div>

      </div>
    </div>

    <figcaption class="line-plan__caption">
      Plan de la ligne <?= htmlspecialchars($line['code']) ?> du métro parisien · <?= htmlspecialchars($totalStations) ?> stations · <?= str_replace('.', ',', $line['length_km']) ?> km · BougeaParis.fr
    </figcaption>

  </figure>

</section>
