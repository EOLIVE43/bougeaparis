<?php
/**
 * Page placeholder : /itineraires/
 * Periode transitoire : planificateur a venir. 4 outils tiers en attendant.
 * Refonte alignee sur /tarifs/ (intro enrichie, tool-cards inline, info-callout).
 * Reste en noindex,follow (page transitoire).
 */

$tpl->seo
    ->setTitle('Itinéraires Paris : planifier votre trajet en transport')
    ->setDescription('Outils pour calculer un itinéraire d\'un point A à un point B en métro, RER, bus, tramway en Île-de-France. Solutions officielles RATP, IDFM.')
    ->setCanonical('/itineraires/')
    ->setRobots('noindex, follow')
    ->setBreadcrumb([
        ['label' => 'Accueil',     'url' => '/'],
        ['label' => 'Se déplacer', 'url' => '/se-deplacer/'],
        ['label' => 'Itinéraires', 'url' => '/itineraires/'],
    ]);
$tpl->addStylesheet('/assets/css/tarifs.css');

$tools = [
    ['icon' => '🚇',
     'name' => 'Bonjour RATP',
     'desc' => 'Application officielle de la RATP. Couvre métro, RER, bus, tramway intra-Paris et proche couronne. Info trafic temps réel, achat de tickets t+ et chargement Navigo Easy/Découverte.',
     'cta'  => 'bonjour.ratp.fr',
     'url'  => 'https://bonjour.ratp.fr/'],
    ['icon' => '🗺️',
     'name' => 'Île-de-France Mobilités',
     'desc' => 'Planificateur officiel régional d\'IDFM. Couvre l\'ensemble des modes franciliens (métro, RER, bus de grande couronne, Transilien). Référence ultime sur tarifs et zones tarifaires.',
     'cta'  => 'iledefrance-mobilites.fr',
     'url'  => 'https://www.iledefrance-mobilites.fr/'],
    ['icon' => '📱',
     'name' => 'Citymapper',
     'desc' => 'Référence internationale (iOS et Android). Combine transport en commun, vélo, scooter et marche. Très bon rendu UX, alertes en temps réel sur les retards et perturbations.',
     'cta'  => 'citymapper.com/paris',
     'url'  => 'https://citymapper.com/paris'],
    ['icon' => '🌐',
     'name' => 'Google Maps',
     'desc' => 'Intégration cartographique complète. Alertes trafic temps réel sur la voirie, alternatives multiples (transport, voiture, vélo, marche). Universel et fonctionne hors-ligne avec téléchargement de cartes.',
     'cta'  => 'maps.google.com',
     'url'  => 'https://maps.google.com/'],
];
?>

<?php $tpl->partial('components/breadcrumb', [
    'items' => [
        ['label' => 'Accueil',     'url' => '/'],
        ['label' => 'Se déplacer', 'url' => '/se-deplacer/'],
        ['label' => 'Itinéraires', 'url' => '/itineraires/'],
    ],
]); ?>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">Itinéraires Paris : planifier votre trajet en transport</h1>
        <p class="hero__subtitle">Calculer un trajet d'un point A à un point B en transport en commun en Île-de-France.</p>
    </div>
</section>

<section class="section">
    <div class="container tarifs-page">

        <h2>Planificateur d'itinéraires : bientôt disponible</h2>
        <p>La fonctionnalité d'<strong>itinéraires personnalisés</strong> sera prochainement disponible sur BougeaParis. Elle vous permettra de <strong>calculer le meilleur trajet</strong> entre deux adresses ou stations en combinant métro, RER, bus, tramway et marche à pied, avec des <strong>informations en temps réel</strong> sur les perturbations.</p>
        <p>En attendant la mise en ligne de notre planificateur, voici les <strong>outils officiels et reconnus</strong> que nous recommandons pour organiser vos déplacements en Île-de-France. Tous exploitent les <strong>mêmes données IDFM</strong> que BougeaParis, donc les résultats restent cohérents.</p>

        <h2>En attendant, utilisez ces outils</h2>
        <div class="tarifs-cards">
            <?php foreach ($tools as $t): ?>
            <article class="tarif-card">
                <div class="tarif-card__header">
                    <span class="tarif-card__icon" aria-hidden="true" style="font-size:1.5rem;background:transparent"><?= $t['icon'] ?></span>
                    <h3 class="tarif-card__title"><?= e($t['name']) ?></h3>
                </div>
                <div class="tarif-card__body">
                    <p><?= e($t['desc']) ?></p>
                    <p><a href="<?= e($t['url']) ?>" class="tarif-card__cta" rel="noopener noreferrer"><?= e($t['cta']) ?> →</a></p>
                </div>
            </article>
            <?php endforeach; ?>
        </div>

        <?php
        $icon = '💡'; $variant = 'info'; $label = 'À savoir';
        $body = 'la <strong>fiabilité des données</strong> est équivalente entre Bonjour RATP, IDFM et Citymapper sur Paris intra-muros : tous consomment les mêmes données officielles IDFM. La différence se joue sur l\'<strong>UX</strong> et les <strong>fonctionnalités supplémentaires</strong> (vélo, achat de tickets, navigation hors-ligne).';
        include __DIR__ . '/../partials/info-callout.php';
        ?>

        <h2>Explorer le réseau en attendant</h2>
        <p>Comprendre les correspondances et choisir votre itinéraire :</p>
        <ul>
            <li><a href="/se-deplacer/">Vue d'ensemble des 7 modes de transport</a></li>
            <li><a href="/metro/">Métro de Paris : plan et lignes</a></li>
            <li><a href="/rer/">Réseau RER : 5 lignes traversantes</a></li>
            <li><a href="/tarifs/">Tarifs IDFM 2026</a></li>
            <li><a href="/info-trafic/">Info-trafic temps réel</a></li>
        </ul>
    </div>
</section>
