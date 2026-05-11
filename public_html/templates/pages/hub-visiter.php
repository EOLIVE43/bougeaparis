<?php
/**
 * Page hub : /visiter/
 * Agregateur tourisme : 7 cards thematiques regroupant les POIs des
 * stations LOT 1 par categorie. Sous-pages /visiter/{tag}/ hors scope
 * (cette page utilise des ancres internes #tag-{slug}).
 *
 * Mapping categories JSON -> 7 groupes thematiques :
 *   monuments         : monument + tour + sculpture + gratte-ciel
 *   musees            : musée
 *   places-avenues    : place + avenue
 *   jardins           : jardin
 *   patrimoine-religieux : cathédrale + chapelle + église
 *   ponts-seine       : pont + île
 *   vie-parisienne    : mairie + commerce + café + hôpital + centre commercial
 *
 * Dedup par wikidata_id : un POI present dans 2 stations (Jardin des Tuileries)
 * n'apparait qu'une seule fois dans la card.
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
$cards = [
    'monuments'            => ['title' => 'Monuments emblématiques',  'lead' => 'Symboles de Paris : Arc de Triomphe, Grande Arche, obélisque de Louxor, pyramide du Louvre et autres icônes urbaines.', 'pois' => []],
    'musees'               => ['title' => 'Musées & arts',            'lead' => 'Les grands musées et institutions culturelles : Louvre, Centre Pompidou, Orangerie, Comédie-Française.', 'pois' => []],
    'places-avenues'       => ['title' => 'Places & avenues iconiques','lead' => 'Concorde, Champs-Élysées, place Vendôme, Étoile : les espaces urbains les plus reconnaissables de Paris.', 'pois' => []],
    'jardins'              => ['title' => 'Jardins & espaces verts',  'lead' => 'Tuileries, Palais-Royal, Carrousel : poumons verts au cœur de la capitale, héritage des jardins royaux.', 'pois' => []],
    'patrimoine-religieux' => ['title' => 'Patrimoine religieux',     'lead' => 'Notre-Dame, Sainte-Chapelle, Saint-Eustache : architecture gothique et histoire millénaire.', 'pois' => []],
    'ponts-seine'          => ['title' => 'Ponts & rives de Seine',   'lead' => 'Pont Neuf, pont des Arts, île de la Cité : la Seine et ses traversées, axe historique de Paris.', 'pois' => []],
    'vie-parisienne'       => ['title' => 'Vie parisienne',           'lead' => 'Lieux de vie urbaine au-delà des monuments : hôtel de ville, La Samaritaine, café de la Régence, hôtel-Dieu.', 'pois' => []],
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
                    'name'           => $poi['name'] ?? '?',
                    'description'    => $poi['description'] ?? '',
                    'wikipedia_url'  => $poi['wikipedia_url'] ?? '',
                    'station_slug'   => $slug,
                    'station_name'   => $data['name'] ?? '?',
                ];
                $seen[$qid] = true;
                break;
            }
        }
    }
}

$tpl->partial('components/breadcrumb', [
    'items' => [
        ['label' => 'Accueil', 'url' => '/'],
        ['label' => 'Visiter', 'url' => '/visiter/'],
    ],
]);
?>

<article class="section">
    <div class="container">
        <header class="hero">
            <h1 class="hero__title">Visiter Paris : monuments, musées, parcs et lieux emblématiques</h1>
            <p class="hero__subtitle">Tous les lieux incontournables de la capitale, regroupés par catégorie thématique avec leur station de métro la plus proche.</p>
        </header>

        <section class="section">
            <p>Paris regroupe en quelques kilomètres carrés une densité de monuments, musées et lieux emblématiques unique au monde. La majorité des sites incontournables sont à moins de 5 minutes à pied d'une station de métro, ce qui fait du <strong>réseau RATP-IDFM le meilleur outil pour découvrir la capitale sans perdre de temps dans les embouteillages</strong>.</p>
            <p>Que vous prépariez votre première visite ou que vous cherchiez à approfondir un quartier que vous croyez connaître, BougeaParis recense les lieux à voir organisés par catégorie (monuments, musées, jardins, patrimoine religieux, lieux de vie parisienne) et par station de métro. Chaque page station détaille les points d'intérêt accessibles à pied, le plus proche pour chacun, ses horaires et son histoire. Pour vous repérer dans le réseau, les pages dédiées à chaque mode de transport (métro, RER, bus, tramway) complètent les fiches lieu.</p>
            <p>Découvrez ci-dessous les <strong>7 grandes catégories</strong> qui structurent l'offre touristique parisienne, ou consultez directement les <a href="/se-deplacer/">pages mode de transport</a> pour partir explorer.</p>
        </section>

        <section class="section" id="categories">
            <h2>Explorer Paris par catégorie</h2>
            <div class="tarifs-cards">
            <?php foreach ($cards as $key => $card): ?>
                <article class="tarif-card" id="<?= e($key) ?>">
                    <h3 class="tarif-card__title"><?= e($card['title']) ?></h3>
                    <p class="tarif-card__desc"><?= e($card['lead']) ?></p>
                    <?php if (!empty($card['pois'])): ?>
                    <ul class="visiter-poi-list">
                        <?php foreach (array_slice($card['pois'], 0, 4) as $poi): ?>
                        <li>
                            <strong><?= e($poi['name']) ?></strong>
                            — accessible depuis
                            <?= stationLink($poi['station_name']) ?>
                        </li>
                        <?php endforeach; ?>
                        <?php if (count($card['pois']) > 4): ?>
                        <li><em>+ <?= count($card['pois']) - 4 ?> autres lieux dans cette catégorie</em></li>
                        <?php endif; ?>
                    </ul>
                    <?php endif; ?>
                </article>
            <?php endforeach; ?>
            </div>
        </section>

        <section class="section" id="top-lieux">
            <h2>Top lieux à visiter par métro</h2>
            <p>Sélection des sites les plus emblématiques accessibles depuis les stations LOT 1 actuellement détaillées sur BougeaParis :</p>
            <ul>
                <?php
                // Top par notoriete : extrait monuments + musees principaux
                $topPois = array_merge(
                    array_slice($cards['monuments']['pois'], 0, 4),
                    array_slice($cards['musees']['pois'], 0, 3),
                    array_slice($cards['patrimoine-religieux']['pois'], 0, 2),
                    array_slice($cards['jardins']['pois'], 0, 1)
                );
                foreach (array_slice($topPois, 0, 10) as $poi):
                ?>
                <li><strong><?= e($poi['name']) ?></strong> — station <?= stationLink($poi['station_name']) ?>. <?= e(mb_substr($poi['description'], 0, 120) . '…') ?></li>
                <?php endforeach; ?>
            </ul>
        </section>

        <section class="section" id="aller-plus-loin">
            <h2>Aller plus loin</h2>
            <ul>
                <li><a href="/se-deplacer/">Tous les modes de transport pour vous déplacer dans Paris</a></li>
                <li><a href="/tarifs/">Tarifs des transports : ticket, carnet, Navigo</a></li>
                <li><a href="/metro/">Métro de Paris : 16 lignes, 308 stations</a></li>
                <li><a href="/info-trafic/">Info-trafic temps réel</a></li>
            </ul>
        </section>
    </div>
</article>
