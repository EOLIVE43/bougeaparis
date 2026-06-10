<?php
/**
 * Page hub : /visiter/
 * Agregateur tourisme : 7 cards thematiques regroupant les POIs des
 * stations LOT 1 par categorie. Sous-pages /visiter/{tag}/ hors scope.
 *
 * Refonte aligne sur /tarifs/ : intro enrichie, key-stats-grid, info-callout,
 * top lieux en cards, FAQ accordion, maillage.
 */

$tpl->seo
    ->setTitle('Visiter Paris : monuments, musées, parcs et lieux emblématiques')
    ->setDescription('Tous les lieux à visiter à Paris classés par catégorie : monuments, musées, jardins, places, patrimoine religieux. Accès en métro et RER pour chaque lieu.')
    ->setCanonical('/visiter/')
    ->setBreadcrumb([
        ['label' => 'Accueil', 'url' => '/'],
        ['label' => 'Visiter', 'url' => '/visiter/'],
    ]);
$tpl->addStylesheet('/assets/css/tarifs.css');

// Agregation POIs LOT 1 -> 7 groupes
$activeStations = ['chatelet','la-defense-grande-arche','charles-de-gaulle-etoile',
                   'concorde','tuileries','palais-royal-musee-du-louvre'];
$groupsMap = [
    'monuments'            => ['monument','tour','sculpture','gratte-ciel'],
    'musees'               => ['musée'],
    'places-avenues'       => ['place','avenue'],
    'jardins'              => ['jardin'],
    'patrimoine-religieux' => ['cathédrale','chapelle','église'],
    'ponts-seine'          => ['pont','île'],
    'vie-parisienne'       => ['mairie','commerce','café','hôpital','centre commercial'],
];
// Mapping picto Lucide par categorie (coherence avec sous-menu nav Visiter)
$cards = [
    'monuments'            => ['title' => 'Monuments emblématiques',  'icon' => 'landmark',   'lead' => 'Symboles de Paris : Arc de Triomphe, Grande Arche, obélisque de Louxor, pyramide du Louvre et autres icônes urbaines.', 'pois' => []],
    'musees'               => ['title' => 'Musées & arts',            'icon' => 'building-2', 'lead' => 'Les grands musées et institutions culturelles : Louvre, Centre Pompidou, Orangerie, Comédie-Française.', 'pois' => []],
    'places-avenues'       => ['title' => 'Places & avenues iconiques','icon' => 'compass',   'lead' => 'Concorde, Champs-Élysées, place Vendôme, Étoile : les espaces urbains les plus reconnaissables de Paris.', 'pois' => []],
    'jardins'              => ['title' => 'Jardins & espaces verts',  'icon' => 'leaf',       'lead' => 'Tuileries, Palais-Royal, Carrousel : poumons verts au cœur de la capitale, héritage des jardins royaux.', 'pois' => []],
    'patrimoine-religieux' => ['title' => 'Patrimoine religieux',     'icon' => 'church',     'lead' => 'Notre-Dame, Sainte-Chapelle, Saint-Eustache : architecture gothique et histoire millénaire.', 'pois' => []],
    'ponts-seine'          => ['title' => 'Ponts & rives de Seine',   'icon' => 'archway',    'lead' => 'Pont Neuf, pont des Arts, île de la Cité : la Seine et ses traversées, axe historique de Paris.', 'pois' => []],
    'vie-parisienne'       => ['title' => 'Vie parisienne',           'icon' => 'coffee',     'lead' => 'Lieux de vie urbaine au-delà des monuments : hôtel de ville, La Samaritaine, café de la Régence, hôtel-Dieu.', 'pois' => []],
];
$seen = [];
foreach ($activeStations as $slug) {
    $path = __DIR__ . '/../../data/stations/' . $slug . '.json';
    if (!is_file($path)) continue;
    $data = json_decode((string)file_get_contents($path), true) ?? [];
    foreach (($data['nearby_pois'] ?? []) as $poi) {
        $qid = $poi['wikidata_id'] ?? '';
        if ($qid === '' || isset($seen[$qid])) continue;
        $cat = $poi['category'] ?? '';
        foreach ($groupsMap as $gKey => $catList) {
            if (in_array($cat, $catList, true)) {
                $cards[$gKey]['pois'][] = [
                    'name'          => $poi['name'] ?? '?',
                    'description'   => $poi['description'] ?? '',
                    'wikipedia_url' => $poi['wikipedia_url'] ?? '',
                    'image_url'     => $poi['image_url']    ?? '',  // pattern Special:FilePath, deja en place
                    'station_slug'  => $slug,
                    'station_name'  => $data['name'] ?? '?',
                ];
                $seen[$qid] = true;
                break;
            }
        }
    }
}

$keyStats = [
    ['number' => '14', 'label' => 'monuments',          'sublabel' => 'Arc Triomphe, Grande Arche…'],
    ['number' => '5',  'label' => 'musées majeurs',     'sublabel' => 'Louvre, Pompidou, Orangerie…'],
    ['number' => '4',  'label' => 'jardins historiques','sublabel' => 'Tuileries, Palais-Royal…'],
    ['number' => '3',  'label' => 'lieux religieux',    'sublabel' => 'Notre-Dame, Sainte-Chapelle…'],
    ['number' => '3',  'label' => 'ponts & îles',       'sublabel' => 'Pont Neuf, Île de la Cité…'],
];

// Top lieux : extraction depuis les groupes prioritaires
$topPois = array_merge(
    array_slice($cards['monuments']['pois'], 0, 4),
    array_slice($cards['musees']['pois'], 0, 3),
    array_slice($cards['patrimoine-religieux']['pois'], 0, 2),
    array_slice($cards['jardins']['pois'], 0, 1)
);
$topPois = array_slice($topPois, 0, 10);

$faqs = [
    ['q' => 'Quel ticket de transport prendre pour visiter Paris en touriste ?',
     'a' => 'Pour <strong>1 jour</strong>, le <strong>ticket t+ unique (2,15 €)</strong> avec correspondances suffit si vous prévoyez peu de trajets. Pour <strong>2-3 jours</strong>, le <strong>carnet de 10 tickets (17,35 €)</strong> est plus économique. Pour <strong>4 jours et plus</strong>, le <strong>forfait Navigo Découverte hebdomadaire (30,75 €)</strong> devient rentable à partir de 14 voyages, et couvre tout le réseau zones 1-5 sans réflexion.'],
    ['q' => 'Quelle station de métro pour visiter le Louvre ?',
     'a' => 'La station <strong>Palais-Royal — Musée du Louvre</strong> (lignes 1 et 7) débouche directement face à la pyramide du Louvre via la sortie n°7 « Pyramide ». Alternative : station <strong>Louvre — Rivoli</strong> (ligne 1) à 400 m de l\'entrée principale. <strong>Astuce</strong> : réservez vos billets en ligne pour éviter 30-60 min de queue.'],
    ['q' => 'Comment voir le maximum de monuments en 1 journée ?',
     'a' => 'Itinéraire optimisé : <strong>matin (avant 10h)</strong> Tour Eiffel + Trocadéro (ligne 6) → <strong>midi</strong> Arc de Triomphe + Champs-Élysées (ligne 1 ou 6) → <strong>après-midi</strong> Louvre + Tuileries + Concorde (ligne 1) → <strong>fin de journée</strong> Notre-Dame + Sainte-Chapelle + Île de la Cité (ligne 4). Comptez 8 stations métro maximum sur la journée.'],
    ['q' => 'Où acheter le Paris Museum Pass ?',
     'a' => 'Le <strong>Paris Museum Pass</strong> (52 € pour 2 jours, 64 € pour 4 jours) s\'achète en ligne sur parismuseumpass.fr, à l\'Office de Tourisme (Hôtel de Ville, Pyramide du Louvre), dans la plupart des grands musées ou aux aéroports CDG/Orly. Il couvre <strong>50+ musées et monuments</strong> avec accès coupe-file. Économie réelle à partir de 3 sites visités.'],
    ['q' => 'Le forfait Navigo est-il valable pour les musées ?',
     'a' => 'Non. Le <strong>forfait Navigo</strong> couvre uniquement le <strong>transport</strong> (métro, RER, bus, tram). Pour les musées, c\'est un <strong>achat séparé</strong> : billets à l\'unité ou Paris Museum Pass. Certaines visites guidées peuvent inclure le transport, mais c\'est l\'exception.'],
    ['q' => 'Peut-on visiter Paris sans prendre le métro ?',
     'a' => 'Oui, dans le centre historique : la <strong>marche</strong> est viable entre Louvre, Tuileries, Concorde, Champs-Élysées, Trocadéro (5 à 30 minutes selon les segments). Pour les distances longues, le <strong>bus 24 et 72</strong> longent la Seine et offrent une vue panoramique. Vélib\' et trottinettes électriques en libre-service complètent l\'offre.'],
    ['q' => 'Les monuments sont-ils accessibles en fauteuil roulant ?',
     'a' => 'La majorité des grands musées sont accessibles : <strong>Louvre, Orsay, Pompidou, Orangerie</strong> disposent d\'accès dédiés. Les monuments classés (Notre-Dame, Sainte-Chapelle, Conciergerie) ont des contraintes architecturales mais des aménagements partiels. Pour le transport, préférez le <strong>RER A/E</strong> et le <strong>tramway</strong>, 100 % accessibles, plutôt que le métro.'],
    ['q' => 'Quel est le meilleur moment pour visiter Paris ?',
     'a' => '<strong>Printemps (avril-juin)</strong> et <strong>automne (septembre-octobre)</strong> offrent le meilleur compromis météo + affluence. Évitez juillet-août : foule maximale + chaleur. Évitez décembre : journées courtes (16h45 coucher). Les <strong>jours de semaine matin (8h-11h)</strong> et <strong>tard l\'après-midi (16h-18h)</strong> sont les moins fréquentés sur les sites majeurs.'],
];
?>

<?php $tpl->partial('components/breadcrumb', [
    'items' => [
        ['label' => 'Accueil', 'url' => '/'],
        ['label' => 'Visiter', 'url' => '/visiter/'],
    ],
]); ?>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">Visiter Paris : monuments, musées, parcs et lieux emblématiques</h1>
        <p class="hero__subtitle">Tous les lieux incontournables de la capitale, regroupés par catégorie thématique avec leur station de métro la plus proche.</p>
    </div>
</section>

<?php $tpl->partial('ads/slot-header'); ?>

<section class="section">
    <div class="container tarifs-page">

        <h2>Découvrir Paris en transport en commun</h2>
        <p>Paris regroupe en quelques kilomètres carrés une <strong>densité de monuments, musées et lieux emblématiques unique au monde</strong>. La majorité des sites incontournables sont à <strong>moins de 5 minutes à pied d'une station de métro</strong>, ce qui fait du réseau RATP-IDFM le meilleur outil pour découvrir la capitale sans perdre de temps dans les embouteillages.</p>
        <p>Que vous prépariez votre <strong>première visite</strong> ou que vous cherchiez à approfondir un quartier que vous croyez connaître, BougeaParis recense les lieux à voir organisés <strong>par catégorie</strong> (monuments, musées, jardins, patrimoine religieux, lieux de vie parisienne) et <strong>par station de métro</strong>. Chaque page station détaille les points d'intérêt accessibles à pied, le plus proche pour chacun, ses horaires et son histoire. Pour vous repérer dans le réseau, les <a href="/se-deplacer/">pages mode de transport</a> complètent les fiches lieu.</p>

        <h2>Paris en chiffres touristiques</h2>
        <p>Sélection des points d'intérêt actuellement documentés sur les 6 stations LOT 1 :</p>
        <?php $stats = $keyStats; include __DIR__ . '/../partials/key-stats-grid.php'; ?>

        <h2>Explorer Paris par catégorie</h2>
        <p>7 grandes catégories couvrent l'offre touristique parisienne. Chaque card renvoie vers les POIs concernés et leur station d'accès la plus proche.</p>

        <div class="tarifs-cards">
        <?php foreach ($cards as $key => $card): ?>
            <article class="tarif-card" id="<?= e($key) ?>">
                <div class="tarif-card__header">
                    <span class="tarif-card__icon" aria-hidden="true">
                        <?php $tpl->partial('components/icon-menu', [
                            'icon'  => $card['icon'],
                            'size'  => 'md',
                            'style' => 'outline',
                        ]); ?>
                    </span>
                    <h3 class="tarif-card__title"><?= e($card['title']) ?></h3>
                </div>
                <div class="tarif-card__body">
                    <p><?= e($card['lead']) ?></p>
                    <?php if (!empty($card['pois'])): ?>
                    <ul class="tarif-card__sub">
                        <?php foreach (array_slice($card['pois'], 0, 4) as $poi): ?>
                        <li>
                            <strong><?= e($poi['name']) ?></strong>
                            — <?= stationLink($poi['station_name']) ?>
                        </li>
                        <?php endforeach; ?>
                        <?php if (count($card['pois']) > 4): ?>
                        <li><em>+ <?= count($card['pois']) - 4 ?> autres lieux</em></li>
                        <?php endif; ?>
                    </ul>
                    <?php endif; ?>
                </div>
            </article>
        <?php endforeach; ?>
        </div>

        <?php
        $icon = '💡'; $variant = 'info'; $label = 'À savoir';
        $body = 'le <strong>Paris Museum Pass</strong> (52 € pour 2 jours, 64 € pour 4 jours) couvre 50+ musées et monuments avec accès coupe-file. Économique dès 3 sites visités. Combinez-le avec un <strong>forfait Navigo Découverte hebdomadaire</strong> pour le transport et vous payez moins de 100 € pour 4 jours de visite illimitée.';
        include __DIR__ . '/../partials/info-callout.php';
        ?>

        <h2>Top lieux à visiter par métro</h2>
        <p>Sélection des sites les plus emblématiques accessibles depuis les stations actuellement détaillées sur BougeaParis :</p>
        <ul class="visiter-poi-grid" role="list">
            <?php foreach ($topPois as $poi):
                $nameDisplay = $poi['name'] !== ''
                    ? mb_strtoupper(mb_substr($poi['name'], 0, 1, 'UTF-8'), 'UTF-8') . mb_substr($poi['name'], 1, null, 'UTF-8')
                    : '';
                $hasImage = !empty($poi['image_url']);
            ?>
            <li class="visiter-poi-card">
                <?php if ($hasImage): ?>
                <div class="visiter-poi-card__image">
                    <img src="<?= e($poi['image_url']) ?>"
                         alt="<?= e($nameDisplay) ?>"
                         loading="lazy" decoding="async"
                         referrerpolicy="no-referrer"
                         width="400" height="225">
                </div>
                <?php else: ?>
                <div class="visiter-poi-card__image visiter-poi-card__image--placeholder" aria-hidden="true">
                    <span>📍</span>
                </div>
                <?php endif; ?>
                <div class="visiter-poi-card__content">
                    <h3 class="visiter-poi-card__name"><?= e($nameDisplay) ?></h3>
                    <div class="visiter-poi-card__station">
                        Station <?= stationLink($poi['station_name']) ?>
                    </div>
                    <?php if (!empty($poi['description'])): ?>
                    <p class="visiter-poi-card__desc"><?= e(mb_substr($poi['description'], 0, 140) . '…') ?></p>
                    <?php endif; ?>
                </div>
            </li>
            <?php endforeach; ?>
        </ul>

        <h2>Questions fréquentes sur la visite de Paris</h2>
        <?php include __DIR__ . '/../partials/faq-accordion.php'; /* consomme $faqs */ ?>

        <h2>Pour aller plus loin</h2>
        <ul>
            <li><a href="/se-deplacer/">Tous les modes de transport pour vous déplacer dans Paris</a></li>
            <li><a href="/tarifs/">Tarifs des transports : ticket, carnet, Navigo</a></li>
            <li><a href="/metro/">Métro de Paris : 16 lignes, 308 stations</a></li>
            <li><a href="/info-trafic/">Info-trafic temps réel</a></li>
        </ul>
    </div>
</section>

<?php $tpl->partial('ads/slot-in-article'); ?>

<?php $tpl->partial('ads/slot-footer'); ?>
