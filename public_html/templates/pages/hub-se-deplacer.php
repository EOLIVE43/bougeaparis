<?php
/**
 * Page hub : /se-deplacer/
 * Agregat thematique des 7 modes de transport (refonte nav niveau 1).
 * Polish CSS et structure aligne sur /tarifs/ (cf. brief polish).
 *
 * Partials reutilises :
 *   - partials/key-stats-grid.php  : "Réseau francilien en chiffres"
 *   - partials/info-callout.php    : encart "À savoir"
 *   - partials/faq-accordion.php   : FAQ pliable native
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
    ['icon' => 'metro', 'label' => 'Métro', 'url' => '/metro/',
     'desc' => 'Réseau dense de 16 lignes desservant Paris intra-muros et la proche banlieue. Le plus rapide pour des trajets courts.',
     'cta'  => 'Découvrir le métro'],
    ['icon' => 'rer', 'label' => 'RER', 'url' => '/rer/',
     'desc' => '5 lignes traversant Paris en express. Idéal pour rejoindre la banlieue, les aéroports ou Disneyland en moins de 40 minutes.',
     'cta'  => 'Découvrir le RER'],
    ['icon' => 'bus', 'label' => 'Bus', 'url' => '/bus/',
     'desc' => 'Plus de 60 lignes diurnes et 47 noctiliens pour les zones moins desservies par le métro. Voyage panoramique en surface.',
     'cta'  => 'Découvrir le bus'],
    ['icon' => 'tram', 'label' => 'Tramway', 'url' => '/tramway/',
     'desc' => '13 lignes redessinant les boulevards extérieurs et la banlieue. Confortable, accessible PMR à 100 %.',
     'cta'  => 'Découvrir le tramway'],
    ['icon' => 'train', 'label' => 'Transilien', 'url' => '/transilien/',
     'desc' => '8 lignes (H, J, K, L, N, P, R, U) reliant Paris à toute l\'Île-de-France. Fréquence régulière, dessertes longues.',
     'cta'  => 'Découvrir le Transilien'],
    ['icon' => 'train', 'label' => 'Gares parisiennes', 'url' => '/gares/',
     'desc' => '7 grandes gares pour les trains régionaux, intercités et grande vitesse (TGV, OUIGO, Eurostar). Liaisons nationales et européennes.',
     'cta'  => 'Découvrir les gares'],
    ['icon' => 'plane', 'label' => 'Aéroports', 'url' => '/aeroports/',
     'desc' => 'Roissy-Charles de Gaulle, Orly et Beauvais. RER, Orlyval, navettes : tous les moyens pour rejoindre l\'avion.',
     'cta'  => 'Découvrir les aéroports'],
];

$keyStats = [
    ['number' => '16', 'label' => 'lignes de métro', 'sublabel' => 'Paris + proche banlieue'],
    ['number' => '5',  'label' => 'lignes de RER',   'sublabel' => 'Express IDF'],
    ['number' => '13', 'label' => 'tramways',        'sublabel' => '100 % accessibles PMR'],
    ['number' => '8',  'label' => 'Transiliens',     'sublabel' => 'H, J, K, L, N, P, R, U'],
    ['number' => '60+','label' => 'lignes de bus',   'sublabel' => '+ 47 Noctiliens'],
];

$conseils = [
    ['titre' => 'Trajet court intra-Paris',
     'desc'  => 'Le <strong>métro</strong> reste la valeur sûre : 14 lignes maillent Paris à moins de 500 m de toute adresse. Pensez au <strong>ticket t+ unique</strong> avec correspondances incluses pendant 2 h.'],
    ['titre' => 'Aller à un aéroport',
     'desc'  => '<strong>CDG</strong> : RER B direct depuis Châtelet en 35 min. <strong>Orly</strong> : RER B + Orlyval depuis Antony, ou tram T7 depuis Villejuif. <strong>Beauvais</strong> : navette officielle depuis Porte Maillot.'],
    ['titre' => 'Traverser Paris d\'est en ouest',
     'desc'  => 'Le <strong>RER A</strong> est l\'axe le plus rapide : La Défense ↔ Nation en 12 minutes. Le métro ligne 1 dessert les mêmes points en 25 minutes avec plus d\'arrêts touristiques.'],
    ['titre' => 'Sortir tard le soir',
     'desc'  => 'Métro circulant jusqu\'à <strong>1h15 en semaine</strong> et 2h15 le samedi soir. Au-delà, les <strong>Noctiliens</strong> prennent le relais avec 47 lignes nocturnes. Pas de service RER A/B entre 0h30 et 5h30.'],
    ['titre' => 'Visiter avec poussette ou en fauteuil',
     'desc'  => 'Le <strong>tramway et le RER</strong> sont 100 % accessibles. Le métro l\'est partiellement (lignes 1 et 14 entièrement). Préférez le tram T3a/T3b et le RER A/E pour les déplacements longs.'],
];

$faqs = [
    ['q' => 'Quel mode de transport est le plus rapide à Paris ?',
     'a' => 'Pour les trajets <strong>intra-Paris courts</strong>, le métro reste le plus rapide grâce à sa fréquence (2-4 min en heure de pointe) et sa densité. Pour traverser Paris d\'est en ouest, le <strong>RER A</strong> est imbattable : La Défense ↔ Nation en 12 minutes. Pour la banlieue lointaine, le Transilien et les bus express sont souvent plus directs que les changements métro/RER multiples.'],
    ['q' => 'Le métro fonctionne-t-il toute la nuit ?',
     'a' => 'Non. Le métro circule de <strong>5h30 à 1h15</strong> en semaine, de 5h30 à 2h15 les vendredis, samedis et veilles de fêtes. Entre la fermeture du métro et la reprise au matin, les <strong>Noctiliens</strong> (47 lignes de bus de nuit) couvrent les principaux axes franciliens. Le RER A et B s\'arrêtent eux à 0h30 et reprennent à 5h30.'],
    ['q' => 'Comment combiner plusieurs modes de transport ?',
     'a' => 'Le <strong>ticket t+</strong> est valable 2 heures avec correspondances illimitées entre <strong>métro et RER</strong> intra-Paris, ainsi qu\'entre <strong>bus et tramway</strong>. Attention : <strong>les correspondances métro↔bus ne sont pas couvertes</strong> par un même ticket t+, il faut compostage un nouveau. Le forfait Navigo Découverte couvre lui tous les modes sans limite, zones 1-5.'],
    ['q' => 'Le ticket t+ est-il valable dans le bus ?',
     'a' => 'Oui. Le <strong>ticket t+</strong> est valable sur le bus, le tramway, le métro et le RER intra-Paris. Sur les bus, les correspondances entre bus et tramway sont incluses pendant 90 minutes. En revanche, les bus express vers les aéroports (Roissybus, Orlybus) nécessitent un billet dédié.'],
    ['q' => 'Quel mode pour aller à l\'aéroport CDG depuis Paris ?',
     'a' => 'Le plus rapide est le <strong>RER B</strong> direct (35 min depuis Châtelet ou Gare du Nord, 11,80 €). Alternatives : <strong>Roissybus</strong> depuis Opéra (60 min, 16,60 €) ou la <strong>navette Le Bus Direct</strong>. Évitez le taxi en heure de pointe : la circulation peut tripler le temps de trajet.'],
    ['q' => 'Quel mode pour Orly depuis Paris ?',
     'a' => 'Depuis 2024, la <strong>ligne 14 du métro</strong> dessert directement Orly en 25 min depuis Châtelet (13 €). Alternative historique : <strong>RER B + Orlyval</strong> (depuis Antony). Plus économique : <strong>tram T7</strong> depuis Villejuif (45 min, ticket t+ à 2,15 €).'],
    ['q' => 'Quelle est la différence entre métro et RER ?',
     'a' => 'Le <strong>métro</strong> dessert Paris intra-muros et la proche banlieue avec des arrêts rapprochés (500 m en moyenne). Le <strong>RER</strong> traverse Paris en express avec peu d\'arrêts intra-Paris mais prolonge jusqu\'à 50 km en banlieue. RER = solution rapide pour la banlieue, métro = solution dense pour Paris.'],
    ['q' => 'Les enfants paient-ils le transport ?',
     'a' => 'Les <strong>moins de 4 ans</strong> voyagent gratuitement, sans titre. Les <strong>4-10 ans</strong> bénéficient du tarif réduit (-50 %) sur les tickets t+ et les forfaits. À partir de 11 ans, tarif adulte plein. Les étudiants -26 ans peuvent souscrire au forfait <strong>Imagine\'R</strong> à tarif préférentiel.'],
];
?>

<?php $tpl->partial('components/breadcrumb', [
    'items' => [
        ['label' => 'Accueil',     'url' => '/'],
        ['label' => 'Se déplacer', 'url' => '/se-deplacer/'],
    ],
]); ?>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">Se déplacer à Paris : tous les modes de transport</h1>
        <p class="hero__subtitle">Métro, RER, bus, tramway, Transilien, gares grandes lignes et aéroports : le guide complet du réseau francilien et de ses connexions internationales.</p>
    </div>
</section>

<?php $tpl->partial('ads/slot-header'); ?>

<section class="section">
    <div class="container tarifs-page">

        <h2>Le réseau de transport en Île-de-France</h2>
        <p>Paris dispose de l'un des <strong>réseaux de transport en commun les plus denses au monde</strong>. Métro, RER, bus, tramway et Transilien permettent de circuler dans toute l'Île-de-France sans voiture, à un coût marginal par voyage très bas grâce au forfait <strong>Navigo Découverte</strong> ou aux tickets unitaires <strong>t+</strong>. Chaque mode a sa pertinence : le métro pour Paris intra-muros, le RER pour traverser la capitale en express, le bus pour les zones moins maillées, le tramway pour les boulevards extérieurs et la banlieue accessible PMR.</p>
        <p>Les <strong>7 grandes gares parisiennes</strong> connectent Paris aux trains régionaux et grandes lignes (TGV, OUIGO, Eurostar, intercités), tandis que les <strong>3 aéroports</strong> (Charles de Gaulle, Orly, Beauvais) disposent chacun de liaisons transport adaptées. BougeaParis vous guide mode par mode : choisir le bon titre de transport, comprendre les zones tarifaires, optimiser vos correspondances. Chaque page mode détaille horaires, stations, accessibilité et conseils pratiques.</p>

        <h2>Le réseau francilien en chiffres</h2>
        <?php $stats = $keyStats; include __DIR__ . '/../partials/key-stats-grid.php'; ?>

        <h2>Les 7 modes de transport en Île-de-France</h2>
        <p>Chaque mode est documenté en détail sur sa page dédiée : lignes, horaires, accessibilité, conseils pratiques.</p>

        <div class="tarifs-cards">
            <?php foreach ($modes as $m): ?>
            <article class="tarif-card">
                <div class="tarif-card__header">
                    <span class="tarif-card__icon" aria-hidden="true">
                        <?php $tpl->partial('components/icon-menu', ['icon' => $m['icon'], 'size' => 'md']); ?>
                    </span>
                    <h3 class="tarif-card__title"><?= e($m['label']) ?></h3>
                </div>
                <div class="tarif-card__body">
                    <p><?= e($m['desc']) ?></p>
                    <p><a href="<?= e($m['url']) ?>" class="tarif-card__cta"><?= e($m['cta']) ?> →</a></p>
                </div>
            </article>
            <?php endforeach; ?>
        </div>

        <?php
        $icon = '💡'; $variant = 'info'; $label = 'À savoir';
        $body = 'le <strong>ticket t+ unique à 2,15 €</strong> couvre métro, RER intra-Paris, bus et tramway avec correspondances illimitées pendant 2 heures. Pour un séjour de 4 jours+ à Paris, le <strong>forfait Navigo Découverte hebdomadaire à 30,75 €</strong> devient rentable à partir de 14 voyages.';
        include __DIR__ . '/../partials/info-callout.php';
        ?>

        <h2>Quel mode choisir selon votre trajet&nbsp;?</h2>
        <ul class="conseil-list">
            <?php foreach ($conseils as $c): ?>
            <li class="conseil-list__item">
                <h3 class="conseil-list__title"><?= e($c['titre']) ?></h3>
                <p class="conseil-list__desc"><?= richText($c['desc']) ?></p>
            </li>
            <?php endforeach; ?>
        </ul>

        <h2>Questions fréquentes sur les transports parisiens</h2>
        <?php include __DIR__ . '/../partials/faq-accordion.php'; /* consomme $faqs */ ?>

        <h2>Pour aller plus loin</h2>
        <ul>
            <li><a href="/tarifs/">Tarifs IDFM 2026 : ticket t+, carnet, Pass Navigo, zones</a> — guide complet des prix.</li>
            <li><a href="/itineraires/">Planifier un itinéraire</a> — calculer un trajet d'un point A à un point B.</li>
            <li><a href="/info-trafic/">Info-trafic temps réel</a> — perturbations métro, RER, bus.</li>
            <li><a href="/visiter/">Visiter Paris en transport en commun</a> — POIs touristiques par métro.</li>
        </ul>
    </div>
</section>

<?php $tpl->partial('ads/slot-in-article'); ?>

<?php $tpl->partial('ads/slot-footer'); ?>
