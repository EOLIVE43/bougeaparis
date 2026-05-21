<?php
/**
 * Page : /tarifs/metro/
 * Sous-page spécialisée du cluster Tarifs.
 */

$pricing = transit_pricing();
$tickets = $pricing['tickets'] ?? [];
$passes  = $pricing['passes']  ?? [];

$tpl->seo
    ->setTitle('Tarifs du métro de Paris : guide complet 2026')
    ->setDescription('Tarifs métro Paris 2026 : ticket t+ 2,15 €, carnet 17,35 €, Navigo Easy, Découverte, Liberté+. Validité, correspondances, où acheter.')
    ->setCanonical('/tarifs/metro/')
    ->setBreadcrumb([
        ['label' => 'Accueil', 'url' => '/'],
        ['label' => 'Tarifs',  'url' => '/tarifs/'],
        ['label' => 'Métro',   'url' => '/tarifs/metro/'],
    ]);
$tpl->addStylesheet('/assets/css/tarifs.css');

$faqs = [
    ['q' => "Combien coûte un ticket de métro à Paris en 2026 ?",
     'a' => "Un <strong>ticket t+</strong> coûte <strong>2,15 €</strong>. Il donne droit à un voyage métro avec correspondances illimitées entre métro et RER intra-Paris pendant 2 heures."],
    ['q' => "Le ticket de métro est-il valable dans le bus ?",
     'a' => "Oui. Le <strong>ticket t+</strong> est valable sur le métro, le RER intra-Paris, le bus et le tramway. Les correspondances bus-bus et bus-tramway sont incluses pendant 90 minutes après la première validation."],
    ['q' => "Faut-il valider son ticket à chaque correspondance dans le métro ?",
     'a' => "Non. Un seul passage aux portillons à l'entrée suffit. Les correspondances entre lignes de métro et entre métro et RER intra-Paris sont autorisées pendant 2 heures sans nouvelle validation, à condition de ne pas sortir du réseau."],
    ['q' => "Le carnet de 10 tickets est-il rentable ?",
     'a' => "Oui. Le <strong>carnet de 10 tickets t+</strong> à <strong>17,35 €</strong> revient à 1,73 € par ticket, soit une économie de 19 % par rapport à l'achat à l'unité. Il est rentable dès le 4e voyage."],
    ['q' => "Le Pass Navigo couvre-t-il toutes les lignes de métro ?",
     'a' => "Oui. Le <strong>Navigo Découverte</strong> et le <strong>Navigo Liberté+</strong> couvrent l'intégralité du réseau métro RATP (lignes 1 à 14, 3bis, 7bis), sans restriction de zone depuis 2015."],
    ['q' => "Le ticket t+ est-il valable pour aller à l'aéroport en métro ?",
     'a' => "<strong>Non, pas tel quel.</strong> Le ticket t+ ne couvre pas la liaison Paris ↔ CDG (RER B), ni Paris ↔ Orly (Ligne 14). Voir <a href=\"/tarifs/aeroports/\">tarifs aéroports</a>. Cependant, le tramway T7 vers Orly et le bus 350 vers CDG sont couverts par le t+."],
    ['q' => "Que se passe-t-il en cas de contrôle sans titre valide ?",
     'a' => "L'amende au tarif de base est de <strong>50 €</strong> en cas de paiement immédiat (le contrôleur encaisse sur place), <strong>75 €</strong> en cas de règlement sous 2 mois, et plus si recouvrement plus tardif."],
    ['q' => "Existe-t-il un ticket touristique illimité ?",
     'a' => "Le <strong>Paris Visite</strong> propose 1, 2, 3 ou 5 jours de transport illimité zones 1-3 ou 1-5. Pour des séjours actifs, le forfait Navigo Découverte hebdomadaire (30,75 €) est généralement plus avantageux."],
];

$tpl->seo->addSchema([
    '@context' => 'https://schema.org', '@type' => 'FAQPage',
    'mainEntity' => array_map(fn($f) => [
        '@type' => 'Question', 'name' => $f['q'],
        'acceptedAnswer' => ['@type' => 'Answer', 'text' => strip_tags($f['a'])],
    ], $faqs),
]);

$renderCard = function (string $key, array $t) {
    $name      = $t['name'] ?? $key;
    $icon      = $t['icon'] ?? '🎫';
    $primary   = $t['price_eur'] ?? $t['card_price_eur'] ?? null;
    $primaryLab = $t['type'] ?? null;
    $weekly    = $t['weekly_price_eur']  ?? null;
    $monthly   = $t['monthly_price_eur'] ?? null;
    $perTrip   = $t['price_per_trip_eur'] ?? null;
    $idealFor  = $t['ideal_for'] ?? null;
    $validFor  = $t['valid_for'] ?? null;
    ?>
    <article class="tarif-card">
      <div class="tarif-card__header">
        <span class="tarif-card__icon" aria-hidden="true"><?= e($icon) ?></span>
        <h3 class="tarif-card__title"><?= e($name) ?></h3>
        <?php if ($primary !== null): ?>
          <span class="tarif-card__price">
            <?= e(format_price((float)$primary)) ?>
            <?php if ($primaryLab): ?><small class="tarif-card__price-sub"><?= e($primaryLab) ?></small><?php endif; ?>
          </span>
        <?php endif; ?>
      </div>
      <div class="tarif-card__body">
        <?php if ($validFor): ?><p><strong>Valable :</strong> <?= e($validFor) ?>.</p><?php endif; ?>
        <?php if ($weekly !== null || $monthly !== null || $perTrip !== null): ?>
          <ul class="tarif-card__sub">
            <?php if ($weekly !== null): ?><li><strong>Forfait hebdomadaire :</strong> <?= e(format_price((float)$weekly)) ?></li><?php endif; ?>
            <?php if ($monthly !== null): ?><li><strong>Forfait mensuel :</strong> <?= e(format_price((float)$monthly)) ?></li><?php endif; ?>
            <?php if ($perTrip !== null): ?><li><strong>Coût par trajet :</strong> <?= e(format_price((float)$perTrip)) ?></li><?php endif; ?>
          </ul>
        <?php endif; ?>
        <?php if ($idealFor): ?><p><strong>Idéal pour :</strong> <?= e($idealFor) ?>.</p><?php endif; ?>
      </div>
    </article>
    <?php
};
?>

<nav class="breadcrumb" aria-label="Fil d'Ariane">
    <div class="container">
        <ol class="breadcrumb__list">
            <li><a href="/">Accueil</a></li>
            <li><a href="/tarifs/">Tarifs</a></li>
            <li class="breadcrumb__current">Métro</li>
        </ol>
    </div>
</nav>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">Tarifs du métro de Paris : guide complet 2026</h1>
        <p class="hero__subtitle">Ticket t+, carnet, Pass Navigo : tous les titres valables sur le métro RATP, leurs prix 2026, leur durée de validité et leurs cas d'usage.</p>
    </div>
</section>

<section class="section">
    <div class="container tarifs-page">

        <p>Le <strong>métro de Paris</strong> est exploité par la <strong>RATP</strong> pour le compte d'<strong>Île-de-France Mobilités</strong>. Tous les tarifs sont fixés par IDFM et harmonisés sur l'ensemble du réseau. Que vous voyagiez à Châtelet, à La Défense ou à Bastille, le prix d'un trajet métro est le même : <strong>2,15 € avec un ticket t+</strong> ou son équivalent en forfait Navigo.</p>

        <h2>Le tarif unique métro</h2>
        <p>Depuis 2015, le métro parisien fonctionne au <strong>tarif unique</strong> : la distance parcourue n'a aucune influence sur le prix, et toutes les correspondances entre lignes sont incluses pendant 2 heures après la première validation. Concrètement, un Paris ↔ La Défense (15 stations Ligne 1) coûte exactement le même prix qu'un Châtelet ↔ Hôtel de Ville (1 station). C'est l'un des réseaux les plus simples au monde sur le plan tarifaire.</p>

        <div class="tarifs-callout tarifs-callout--info">
          <span class="tarifs-callout__icon" aria-hidden="true">💡</span>
          <strong>À savoir :</strong> les <strong>correspondances métro ↔ RER intra-Paris</strong> sont incluses dans le ticket t+ pendant 2 heures, à condition de ne pas sortir du réseau (rester en sous-sol).
        </div>

        <h2>Quels titres sont valables sur le métro ?</h2>

        <div class="tarifs-cards">
            <?php foreach (['ticket_t_plus', 'carnet_10', 'navigo_easy'] as $k):
                if (!empty($tickets[$k])) $renderCard($k, $tickets[$k]); endforeach; ?>
            <?php foreach (['navigo_decouverte', 'navigo_liberte_plus'] as $k):
                if (!empty($passes[$k])) $renderCard($k, $passes[$k]); endforeach; ?>
        </div>

        <h2>Acheter un titre pour le métro</h2>
        <ul>
            <li><strong>Distributeurs automatiques</strong> dans toutes les stations métro (paiement CB ou espèces, multilingue).</li>
            <li><strong>Guichets RATP</strong> dans les stations principales (Châtelet, Gare de Lyon, Saint-Lazare, La Défense) — conseil + Navigo personnalisé.</li>
            <li><strong>Tabacs et points relais agréés</strong> en Paris et région.</li>
        </ul>

        <h2>Validation et contrôles</h2>
        <p>L'accès au quai métro se fait obligatoirement par un <strong>portillon validateur</strong> (ticket papier ou Navigo). Toutes les stations sont fermées : pas de validation = pas d'accès. Des contrôleurs RATP circulent ponctuellement dans les rames et aux sorties.</p>

        <div class="tarifs-callout tarifs-callout--warning">
          <span class="tarifs-callout__icon" aria-hidden="true">⚠️</span>
          <strong>Attention :</strong> conservez votre ticket pendant tout le trajet. Le contrôle peut intervenir à la sortie. L'amende au tarif de base est de <strong>50 €</strong> en paiement immédiat.
        </div>

        <h2>Cas particuliers</h2>

        <h3>Métro vers les aéroports</h3>
        <p>La <strong>Ligne 14</strong> dessert directement l'<strong>aéroport d'Orly</strong> depuis 2024 (terminus sud). Le billet dédié coûte <strong><?= e(format_price(13.00)) ?></strong>. Pour <strong>Charles de Gaulle</strong>, pas de métro direct : utiliser le <strong>RER B</strong> depuis Châtelet ou Gare du Nord (<?= e(format_price(11.80)) ?>). Voir le <a href="/tarifs/aeroports/">guide complet tarifs aéroports</a>.</p>

        <h3>Métro vers les gares parisiennes</h3>
        <p>Les 7 grandes gares parisiennes (Lyon, Nord, Est, Saint-Lazare, Montparnasse, Austerlitz, Bercy) sont toutes desservies par au moins une ligne de métro et le RER. Trajet couvert par le ticket t+ classique.</p>

        <h2>Tarifs jeunes et seniors</h2>
        <ul>
            <li><strong>-4 ans</strong> : voyagent gratuitement, sans titre.</li>
            <li><strong>4-10 ans</strong> : tarif réduit -50 % sur tickets t+ et Navigo.</li>
            <li><strong>Imagine'R (-26 ans)</strong> : forfait étudiant à tarif préférentiel.</li>
            <li><strong>Solidarité Transport</strong> : réduction 75-100 % pour bénéficiaires RSA et CSS, attribuée par IDFM.</li>
            <li><strong>Senior (65+ ans)</strong> : <strong>Forfait Améthyste</strong> permet un Navigo gratuit ou très réduit selon les revenus (à demander à la mairie de résidence).</li>
        </ul>

        <h2>Questions fréquentes sur les tarifs métro</h2>
        <div class="faq-accordion">
            <?php foreach ($faqs as $i => $f): ?>
                <details class="faq-accordion__item" <?= $i === 0 ? 'open' : '' ?>>
                    <summary><h3><?= e($f['q']) ?></h3></summary>
                    <div class="faq-accordion__answer"><p><?= richText($f['a']) ?></p></div>
                </details>
            <?php endforeach; ?>
        </div>

        <h2>Pour aller plus loin</h2>
        <ul>
            <li><a href="/tarifs/">Tarifs et titres de transport en commun en Île-de-France (hub)</a></li>
            <li><a href="/tarifs/aeroports/">Tarifs métro/RER vers les aéroports parisiens</a></li>
            <li><a href="/metro/">Toutes les lignes de métro de Paris</a></li>
        </ul>

    </div>
</section>
