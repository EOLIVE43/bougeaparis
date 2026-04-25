<?php
/**
 * partials/traffic-banner.php
 *
 * Bandeau "Info trafic aujourd'hui" affichant les stats du jour.
 *
 * Variables disponibles :
 *   $bannerMode (string) : 'all' | 'metro' | 'rer' | 'tramway' | 'transilien' | 'bus'
 *                          Defaut : 'all' (toutes lignes confondues)
 *   $bannerDate (string) : date au format francais (ex: "samedi 25 avril 2026")
 *                          Defaut : auto-detecte depuis latest.json
 */

// Defaults
if (!isset($bannerMode)) $bannerMode = 'all';
if (!isset($bannerDate)) $bannerDate = '';

// Charger les stats depuis latest.json
$trafficLatestPath = __DIR__ . '/../../data/traffic/latest.json';
$bannerStats = null;
$bannerArticleUrl = '/info-trafic/';

if (file_exists($trafficLatestPath)) {
    $rawJson = @file_get_contents($trafficLatestPath);
    $decoded = $rawJson ? json_decode($rawJson, true) : null;

    if (is_array($decoded)) {
        // Date par defaut : celle du JSON si non fournie
        if (empty($bannerDate) && !empty($decoded['date'])) {
            $ts = strtotime($decoded['date']);
            if ($ts !== false) {
                $jrs = ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi'];
                $mns = ['', 'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
                        'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'];
                $bannerDate = $jrs[(int)date('w', $ts)] . ' '
                            . (int)date('j', $ts) . ' '
                            . $mns[(int)date('n', $ts)] . ' '
                            . date('Y', $ts);
            }
        }

        // Article du jour pour le lien
        if (!empty($decoded['article_url'])) {
            $bannerArticleUrl = $decoded['article_url'];
        }

        // Selection des stats : globales ou par mode
        if ($bannerMode === 'all') {
            $bannerStats = isset($decoded['stats_total']) ? $decoded['stats_total'] : null;
        } elseif (isset($decoded['stats_by_mode'][$bannerMode])) {
            $bannerStats = $decoded['stats_by_mode'][$bannerMode];
        }
    }
}

// Si on n'a pas de stats, on n'affiche pas le bandeau
if (!is_array($bannerStats) || (int)($bannerStats['total'] ?? 0) === 0) {
    // Cas particulier : aucune perturbation -> on affiche un message rassurant
    if (is_array($bannerStats) && (int)($bannerStats['total'] ?? 0) === 0) {
        $modeLabels = [
            'all'        => 'sur l\'ensemble du réseau',
            'metro'      => 'sur le métro',
            'rer'        => 'sur le RER',
            'tramway'    => 'sur le tramway',
            'transilien' => 'sur le Transilien',
            'bus'        => 'sur le réseau de bus',
        ];
        $modeText = isset($modeLabels[$bannerMode]) ? $modeLabels[$bannerMode] : '';
        ?>
        <section class="traffic-banner traffic-banner--clear" aria-label="Etat du reseau">
            <h2 class="traffic-banner__title">
                Info trafic aujourd'hui<?php if ($bannerDate): ?> · <span class="traffic-banner__date"><?= htmlspecialchars($bannerDate) ?></span><?php endif; ?>
            </h2>
            <p class="traffic-banner__clear-text">
                ✓ Trafic normal <?= htmlspecialchars($modeText) ?> aujourd'hui.
            </p>
            <p class="traffic-banner__source">
                Source : données officielles Île-de-France Mobilités (PRIM)
            </p>
        </section>
        <?php
    }
    return; // sort du partial sans rien afficher si pas de stats du tout
}

$bloquante   = (int)($bannerStats['bloquante'] ?? 0);
$perturbee   = (int)($bannerStats['perturbee'] ?? 0);
$information = (int)($bannerStats['information'] ?? 0);
$total       = (int)($bannerStats['total'] ?? 0);

$modeLabels = [
    'all'        => '',
    'metro'      => 'métro',
    'rer'        => 'RER',
    'tramway'    => 'tramway',
    'transilien' => 'Transilien',
    'bus'        => 'bus',
];
$modeLabel = $modeLabels[$bannerMode] ?? '';
$titleSuffix = $modeLabel ? ' ' . $modeLabel : '';
?>

<section class="traffic-banner" aria-label="Info trafic aujourd'hui">
    <h2 class="traffic-banner__title">
        Info trafic<?= htmlspecialchars($titleSuffix) ?> aujourd'hui<?php if ($bannerDate): ?> · <span class="traffic-banner__date"><?= htmlspecialchars($bannerDate) ?></span><?php endif; ?>
    </h2>

    <div class="traffic-banner__stats">
        <div class="traffic-banner__stat traffic-banner__stat--bloquante">
            <span class="traffic-banner__stat-number"><?= $bloquante ?></span>
            <span class="traffic-banner__stat-label">Trafic interrompu</span>
        </div>
        <div class="traffic-banner__stat traffic-banner__stat--perturbee">
            <span class="traffic-banner__stat-number"><?= $perturbee ?></span>
            <span class="traffic-banner__stat-label">Trafic perturbé</span>
        </div>
        <div class="traffic-banner__stat traffic-banner__stat--information">
            <span class="traffic-banner__stat-number"><?= $information ?></span>
            <span class="traffic-banner__stat-label">Information</span>
        </div>
    </div>

    <p class="traffic-banner__source">
        Source : données officielles Île-de-France Mobilités (PRIM) ·
        <?= $total ?> perturbation<?= $total > 1 ? 's' : '' ?> recensée<?= $total > 1 ? 's' : '' ?><?php if ($modeLabel): ?> sur le <?= htmlspecialchars($modeLabel) ?><?php endif; ?>
        · <a href="<?= htmlspecialchars($bannerArticleUrl) ?>" class="traffic-banner__article-link">Lire l'article complet →</a>
    </p>
</section>
