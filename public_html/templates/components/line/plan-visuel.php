<?php
/**
 * Section Plan Visuel — Page ligne de métro
 *
 * Affiche la frise horizontale de la ligne :
 * - Trait coloré horizontal
 * - Cercles centrés sur la ligne (terminus, pôles majeurs, stations classiques)
 * - Noms de stations inclinés en bas
 * - Pastilles de correspondance en haut (au-dessus du trait)
 * - Étiquettes culturelles teal sous les noms
 *
 * Variables attendues :
 * - $line : array, données de la ligne (depuis JSON)
 * - $lineColor : string, couleur officielle
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

    <div class="line-plan__scroll-wrapper">
      <div class="line-plan__frise" style="--line-color: <?= htmlspecialchars($lineColor) ?>;">

        <!-- La ligne horizontale colorée -->
        <div class="line-plan__line" aria-hidden="true"></div>

        <!-- Les stations -->
        <div class="line-plan__stations">

          <?php foreach ($stations as $station): ?>
            <div class="line-plan__station <?= $station['is_major'] ? 'line-plan__station--major' : '' ?>">

              <!-- Pastilles de correspondance (au-dessus de la ligne) -->
              <?php if (!empty($station['correspondences'])): ?>
                <div class="line-plan__corresp">
                  <?php foreach ($station['correspondences'] as $corresp): ?>
                    <span class="pastille-corresp" style="border-color: <?= htmlspecialchars($corresp['color']) ?>;">
                      <span class="pastille-corresp__mode" style="color: <?= htmlspecialchars($corresp['color']) ?>;"><?= htmlspecialchars($corresp['mode']) ?></span><span class="pastille-corresp__line" style="color: <?= htmlspecialchars($corresp['color']) ?>;"><?= htmlspecialchars($corresp['line']) ?></span>
                    </span>
                  <?php endforeach; ?>
                </div>
                <div class="line-plan__connector" aria-hidden="true"></div>
              <?php endif; ?>

              <!-- Le rond de la station (centré sur la ligne) -->
              <div class="line-plan__dot <?= $station['is_major'] ? 'line-plan__dot--major' : 'line-plan__dot--small' ?>"
                   <?= $station['is_major'] ? '' : 'aria-hidden="true"' ?>></div>

              <!-- Nom de la station (sous la ligne, incliné) -->
              <div class="line-plan__name <?= $station['is_major'] ? 'line-plan__name--major' : '' ?>">
                <?= htmlspecialchars($station['name']) ?>
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
