<?php
/**
 * Page hub : /se-deplacer/
 * Agregat thematique des 7 modes de transport (refonte nav niveau 1).
 * Pattern visuel aligne sur tarifs-hub : intro + grille de cards + sections SEO.
 */

$tpl->seo
    ->setTitle('Se déplacer à Paris : tous les modes de transport en commun')
    ->setDescription('Métro, RER, bus, tramway, Transilien, gares et aéroports : le guide complet pour se déplacer en Île-de-France. Choix du mode, tarifs, itinéraires.')
    ->setCanonical('/se-deplacer/')
    ->setBreadcrumb([
        ['label' => 'Accueil',     'url' => '/'],
        ['label' => 'Se déplacer', 'url' => '/se-deplacer/'],
    ]);
$tpl->addStylesheet('/assets/css/tarifs.css');

$modes = [
    [
        'icon'  => 'metro',
        'label' => 'Métro',
        'url'   => '/metro/',
        'desc'  => 'Réseau dense de 16 lignes desservant Paris intra-muros et la proche banlieue. Le plus rapide pour des trajets courts.',
        'cta'   => 'Découvrir le métro',
    ],
    [
        'icon'  => 'rer',
        'label' => 'RER',
        'url'   => '/rer/',
        'desc'  => '5 lignes traversant Paris en express. Idéal pour rejoindre la banlieue, les aéroports ou Disneyland en moins de 40 minutes.',
        'cta'   => 'Découvrir le RER',
    ],
    [
        'icon'  => 'bus',
        'label' => 'Bus',
        'url'   => '/bus/',
        'desc'  => 'Plus de 60 lignes diurnes et 47 noctiliens pour les zones moins desservies par le métro. Voyage panoramique en surface.',
        'cta'   => 'Découvrir le bus',
    ],
    [
        'icon'  => 'tram',
        'label' => 'Tramway',
        'url'   => '/tramway/',
        'desc'  => '13 lignes redessinant les boulevards extérieurs et la banlieue. Confortable, accessible PMR à 100 %.',
        'cta'   => 'Découvrir le tramway',
    ],
    [
        'icon'  => 'train',
        'label' => 'Transilien',
        'url'   => '/transilien/',
        'desc'  => '8 lignes (H, J, K, L, N, P, R, U) reliant Paris à toute l\'Île-de-France. Fréquence régulière, dessertes longues.',
        'cta'   => 'Découvrir le Transilien',
    ],
    [
        'icon'  => 'train',
        'label' => 'Gares parisiennes',
        'url'   => '/gares/',
        'desc'  => '7 grandes gares pour les trains régionaux, intercités et grande vitesse (TGV, OUIGO, Eurostar). Liaisons nationales et européennes.',
        'cta'   => 'Découvrir les gares',
    ],
    [
        'icon'  => 'plane',
        'label' => 'Aéroports',
        'url'   => '/aeroports/',
        'desc'  => 'Roissy-Charles de Gaulle, Orly et Beauvais. RER, Orlyval, navettes : tous les moyens pour rejoindre l\'avion.',
        'cta'   => 'Découvrir les aéroports',
    ],
];

$conseils = [
    [
        'titre' => 'Trajet court intra-Paris',
        'desc'  => 'Le métro reste la valeur sûre : 14 lignes maillent Paris à moins de 500 m de toute adresse. Pensez au ticket t+ unique (correspondances incluses pendant 2 h).',
    ],
    [
        'titre' => 'Aller à un aéroport',
        'desc'  => 'CDG : RER B direct depuis Châtelet en 35 min. Orly : RER B + Orlyval depuis Antony, ou tram T7 depuis Villejuif. Beauvais : navette officielle depuis Porte Maillot.',
    ],
    [
        'titre' => 'Traverser Paris d\'est en ouest',
        'desc'  => 'Le RER A est l\'axe le plus rapide : La Défense ↔ Nation en 12 minutes. Le métro ligne 1 dessert les mêmes points en 25 minutes avec plus d\'arrêts touristiques.',
    ],
    [
        'titre' => 'Sortir tard le soir',
        'desc'  => 'Métro circulant jusqu\'à 1h15 (2h15 samedi soir). Au-delà, les Noctiliens prennent le relais avec 47 lignes nocturnes. Pas de service entre 0h30 et 5h30 sur RER A et B.',
    ],
    [
        'titre' => 'Visiter avec une poussette ou en fauteuil',
        'desc'  => 'Le tramway et le RER sont 100 % accessibles. Le métro l\'est partiellement (lignes 1 et 14 entièrement, autres lignes en cours d\'aménagement). Préférez le tram T3a/T3b et le RER A/E pour les déplacements longs.',
    ],
];

$tpl->partial('components/breadcrumb', [
    'items' => [
        ['label' => 'Accueil',     'url' => '/'],
        ['label' => 'Se déplacer', 'url' => '/se-deplacer/'],
    ],
]);
?>

<article class="section">
    <div class="container">
        <header class="hero">
            <h1 class="hero__title">Se déplacer à Paris : tous les modes de transport</h1>
            <p class="hero__subtitle">Métro, RER, bus, tramway, Transilien, gares grandes lignes et aéroports : le guide complet du réseau francilien et de ses connexions internationales.</p>
        </header>

        <section class="section">
            <p>Paris dispose de l'un des réseaux de transport en commun les plus denses au monde. <strong>14 lignes de métro</strong>, <strong>5 lignes de RER</strong>, <strong>13 tramways</strong>, plus de <strong>60 lignes de bus</strong> et un réseau Transilien étendu permettent de circuler dans toute l'Île-de-France sans voiture. Chaque mode a sa pertinence : le métro est imbattable dans Paris intra-muros sur des trajets courts, le RER traverse la capitale en quelques minutes pour rejoindre la banlieue, les bus desservent les zones moins maillées, et le tramway redessine les boulevards extérieurs.</p>
            <p>Les <strong>7 grandes gares parisiennes</strong> connectent Paris aux trains régionaux et grandes lignes (TGV, OUIGO, Eurostar, intercités), tandis que les <strong>3 aéroports</strong> (Charles de Gaulle, Orly, Beauvais) disposent chacun de liaisons transport adaptées. BougeaParis vous guide mode par mode : choisir le bon titre de transport, comprendre les zones tarifaires, optimiser vos correspondances. Chaque page mode détaille horaires, stations, accessibilité et conseils pratiques.</p>
        </section>

        <section class="section" id="modes">
            <h2>Les 7 modes de transport en Île-de-France</h2>
            <div class="tarifs-cards">
                <?php foreach ($modes as $m): ?>
                <article class="tarif-card">
                    <div class="tarif-card__icon" aria-hidden="true">
                        <?php $tpl->partial('components/icon-menu', ['icon' => $m['icon'], 'size' => 'md']); ?>
                    </div>
                    <h3 class="tarif-card__title"><?= e($m['label']) ?></h3>
                    <p class="tarif-card__desc"><?= e($m['desc']) ?></p>
                    <a href="<?= e($m['url']) ?>" class="tarif-card__cta"><?= e($m['cta']) ?> →</a>
                </article>
                <?php endforeach; ?>
            </div>
        </section>

        <section class="section" id="conseils">
            <h2>Quel mode choisir selon votre trajet&nbsp;?</h2>
            <?php foreach ($conseils as $c): ?>
            <h3><?= e($c['titre']) ?></h3>
            <p><?= e($c['desc']) ?></p>
            <?php endforeach; ?>
        </section>

        <section class="section" id="liens-utiles">
            <h2>Aller plus loin</h2>
            <ul>
                <li><a href="/tarifs/">Tarifs IDFM 2026 : ticket t+, carnet, Navigo, zones</a> — guide complet des prix.</li>
                <li><a href="/itineraires/">Planifier un itinéraire</a> — calculer un trajet d'un point A à un point B.</li>
                <li><a href="/info-trafic/">Info-trafic temps réel</a> — perturbations métro, RER, bus.</li>
                <li><a href="/visiter/">Visiter Paris en transport en commun</a> — POIs touristiques par métro.</li>
            </ul>
        </section>
    </div>
</article>
