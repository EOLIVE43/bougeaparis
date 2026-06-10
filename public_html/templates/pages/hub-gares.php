<?php
/**
 * Template page : hub Gares parisiennes
 *
 * Squelette pour la livraison future. Pour l'instant, affiche les 7 grandes
 * gares parisiennes en cards "à venir" (smart-link inactif), avec une intro
 * SEO solide pour amorcer le ranking.
 *
 * Quand une page gare individuelle sera prête (data/gares/{slug}.json + slug
 * ajouté à Routes::$activeGareSlugs), sa carte deviendra automatiquement
 * cliquable.
 */

$tpl->seo
    ->setTitle('Gares de Paris : guide complet des grandes gares parisiennes')
    ->setDescription('Découvrez les 7 grandes gares de Paris : Gare du Nord, Gare de l\'Est, Gare de Lyon, Gare Montparnasse, Gare Saint-Lazare, Gare d\'Austerlitz, Gare de Bercy. Plans, accès, services, restaurants, parkings.')
    ->setCanonical('/gares/')
    ->setBreadcrumb([
        ['label' => 'Accueil', 'url' => '/'],
        ['label' => 'Gares',   'url' => '/gares/'],
    ]);

// Liste des 7 grandes gares parisiennes (squelette)
$gares = [
    [
        'slug'         => 'gare-du-nord',
        'name'         => 'Gare du Nord',
        'description'  => 'Plus grande gare d\'Europe. Trains Eurostar, Thalys, TGV, RER B, D, E.',
        'icon'         => '🚄',
        'compagnies'   => ['Eurostar', 'Thalys', 'SNCF Voyageurs'],
    ],
    [
        'slug'         => 'gare-de-lyon',
        'name'         => 'Gare de Lyon',
        'description'  => 'Direction sud-est de la France. TGV, Lyria, RER A, RER D.',
        'icon'         => '🚄',
        'compagnies'   => ['SNCF Voyageurs', 'TGV Lyria', 'OUIGO'],
    ],
    [
        'slug'         => 'gare-montparnasse',
        'name'         => 'Gare Montparnasse',
        'description'  => 'Direction ouest et sud-ouest. TGV Atlantique, Transilien N.',
        'icon'         => '🚄',
        'compagnies'   => ['SNCF Voyageurs', 'OUIGO'],
    ],
    [
        'slug'         => 'gare-saint-lazare',
        'name'         => 'Gare Saint-Lazare',
        'description'  => 'Direction Normandie et banlieue ouest. Transilien J et L, intercités Normandie.',
        'icon'         => '🚂',
        'compagnies'   => ['SNCF Voyageurs', 'Transilien'],
    ],
    [
        'slug'         => 'gare-de-l-est',
        'name'         => 'Gare de l\'Est',
        'description'  => 'Direction est de la France et Allemagne. TGV Est, ICE, Transilien P.',
        'icon'         => '🚄',
        'compagnies'   => ['SNCF Voyageurs', 'Deutsche Bahn'],
    ],
    [
        'slug'         => 'gare-d-austerlitz',
        'name'         => 'Gare d\'Austerlitz',
        'description'  => 'Direction centre et sud-ouest. Intercités, RER C.',
        'icon'         => '🚂',
        'compagnies'   => ['SNCF Voyageurs', 'Intercités'],
    ],
    [
        'slug'         => 'gare-de-bercy',
        'name'         => 'Gare de Bercy',
        'description'  => 'Liaisons Bourgogne, Auvergne et trains de nuit. Annexe de la Gare de Lyon.',
        'icon'         => '🚂',
        'compagnies'   => ['SNCF Voyageurs', 'OUIGO Train Classique'],
    ],
];

$tpl->addStylesheet('/assets/css/line.css');
?>

<?php $tpl->partial('components/breadcrumb', [
    'items' => [
        ['label' => 'Accueil', 'url' => '/'],
        ['label' => 'Gares'],
    ],
]); ?>

<article class="line-page">
  <div class="line-page__container">

    <header class="hub-gares__header">
      <h1>Gares de Paris</h1>
      <p class="hub-gares__lead">
        Paris compte <strong>7 grandes gares ferroviaires</strong> qui desservent toute la France et l'Europe&nbsp;: <strong>Gare du Nord</strong>, <strong>Gare de Lyon</strong>, <strong>Montparnasse</strong>, <strong>Saint-Lazare</strong>, <strong>Gare de l'Est</strong>, <strong>Austerlitz</strong> et <strong>Bercy</strong>. Retrouvez bientôt pour chacune un guide complet&nbsp;: plans, accès, compagnies ferroviaires, services, restaurants, parkings, taxis et conseils pratiques pour votre voyage.
      </p>
    </header>

    <section class="hub-gares__grid-section">
      <h2>Les 7 grandes gares parisiennes</h2>
      <div class="hub-gares__grid">
        <?php foreach ($gares as $gare):
          $url = '/gare/' . $gare['slug'] . '/';
          $isActive = Routes::exists(rtrim($url, '/'));
          $cssClass = 'gare-card' . ($isActive ? '' : ' gare-card--inactive');
        ?>
          <article class="<?= $cssClass ?>">
            <div class="gare-card__icon" aria-hidden="true"><?= e($gare['icon']) ?></div>
            <h3 class="gare-card__title">
              <?= conditionalLink($url, e($gare['name']), 'gare-card__title-link') ?>
            </h3>
            <p class="gare-card__desc"><?= e($gare['description']) ?></p>
            <div class="gare-card__compagnies">
              <?php foreach ($gare['compagnies'] as $cie): ?>
                <span class="gare-card__cie"><?= e($cie) ?></span>
              <?php endforeach; ?>
            </div>
            <?php if (!$isActive): ?>
              <div class="gare-card__soon">📅 Page détaillée à venir</div>
            <?php endif; ?>
          </article>
        <?php endforeach; ?>
      </div>
    </section>

<?php $tpl->partial('ads/slot-header'); ?>

    <section class="hub-gares__intro">
      <h2>Pourquoi consulter les guides BougeaParis ?</h2>
      <p>
        Que vous soyez un voyageur occasionnel ou habitué, trouver son chemin dans une <strong>grande gare parisienne</strong> n'est pas toujours simple&nbsp;: terminaux multiples, voies, halls, sorties métro, taxis, parkings… Les guides BougeaParis rassemblent toutes les <strong>informations pratiques</strong> dont vous avez besoin&nbsp;: plans détaillés, services disponibles, accès depuis le métro et le RER, conseils pour préparer votre voyage.
      </p>
      <p>
        Chaque gare a ses spécificités&nbsp;: la <strong>Gare du Nord</strong> accueille l'Eurostar et les trains internationaux, la <strong>Gare de Lyon</strong> dessert le sud-est de la France et l'Italie, <strong>Montparnasse</strong> couvre l'ouest et le sud-ouest. Notre équipe prépare des guides complets pour chacune.
      </p>
    </section>

<?php $tpl->partial('ads/slot-in-article'); ?>

    <section class="hub-gares__alternatives">
      <h2>Pour voyager dans Paris et l'Île-de-France</h2>
      <p>
        Pour vos déplacements urbains au sein de Paris, consultez nos guides dédiés&nbsp;:
      </p>
      <ul>
        <li><a href="/metro/">Plan et lignes du métro parisien</a></li>
        <li><a href="/rer/">Le réseau RER d'Île-de-France</a></li>
        <li><a href="/transilien/">Trains Transilien (banlieue)</a></li>
        <li><a href="/aeroports/">Aéroports parisiens (Roissy CDG, Orly)</a></li>
      </ul>
    </section>

<?php $tpl->partial('ads/slot-footer'); ?>

  </div>
</article>
