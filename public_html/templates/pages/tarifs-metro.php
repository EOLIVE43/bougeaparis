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
     'a' => "<strong>Non, pas tel quel.</strong> Le ticket t+ ne couvre pas la liaison Paris ↔ CDG (RER B), ni Paris ↔ Orly (Ligne 14). Voir <a href=\"/tarifs/aeroports/\">tarifs aéroports</a> pour les billets dédiés. Cependant, le tramway T7 vers Orly et le bus 350 vers CDG sont couverts par le t+."],
    ['q' => "Que se passe-t-il en cas de contrôle sans titre valide ?",
     'a' => "L'amende au tarif de base est de <strong>50 €</strong> en cas de paiement immédiat (le contrôleur encaisse sur place), <strong>75 €</strong> en cas de règlement sous 2 mois, et plus si recouvrement plus tardif. La RATP applique également des amendes spécifiques pour fraude récidiviste."],
    ['q' => "Existe-t-il un ticket touristique illimité ?",
     'a' => "Le <strong>Paris Visite</strong> propose 1, 2, 3 ou 5 jours de transport illimité zones 1-3 ou 1-5, avec quelques avantages partenaires. Tarif 1 jour zones 1-3 : 14,90 € (à confirmer en 2026). Pour des séjours actifs, le forfait Navigo Découverte hebdomadaire (30,75 €) est généralement plus avantageux."],
];

$tpl->seo->addSchema([
    '@context' => 'https://schema.org',
    '@type' => 'FAQPage',
    'mainEntity' => array_map(fn($f) => [
        '@type' => 'Question', 'name' => $f['q'],
        'acceptedAnswer' => ['@type' => 'Answer', 'text' => strip_tags($f['a'])],
    ], $faqs),
]);
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
    <div class="container" style="max-width:920px;">

        <p>Le <strong>métro de Paris</strong> est exploité par la <strong>RATP</strong> pour le compte d'<strong>Île-de-France Mobilités</strong>. Tous les tarifs sont fixés par IDFM et harmonisés sur l'ensemble du réseau. Que vous voyagiez à Châtelet, à La Défense ou à Bastille, le prix d'un trajet métro est le même : <strong><?= e(format_price(2.15)) ?> avec un ticket t+</strong> ou son équivalent en forfait Navigo.</p>

        <h2>Le tarif unique métro</h2>
        <p>Depuis 2015, le métro parisien fonctionne au <strong>tarif unique</strong> : la distance parcourue n'a aucune influence sur le prix, et toutes les correspondances entre lignes sont incluses pendant 2 heures après la première validation. Concrètement, un Paris ↔ La Défense (15 stations Ligne 1) coûte exactement le même prix qu'un Châtelet ↔ Hôtel de Ville (1 station). C'est l'un des réseaux les plus simples au monde sur le plan tarifaire.</p>

        <h2>Quels titres sont valables sur le métro ?</h2>

        <h3>Ticket t+ (<?= e(format_price(2.15)) ?>)</h3>
        <p>Le <strong>ticket t+</strong> est le titre unitaire de référence. Il est valable sur le métro, le RER intra-Paris, le bus et le tramway. Correspondances illimitées entre métro/RER pendant 2 heures, et entre bus/tramway pendant 90 minutes. <strong>Idéal pour les touristes en visite courte (1-2 jours).</strong></p>

        <h3>Carnet de 10 tickets t+ (<?= e(format_price(17.35)) ?>)</h3>
        <p>Soit <strong>1,73 € par ticket</strong>, une économie de 19 %. Disponible en tickets papier ou rechargé sur Navigo Easy. <strong>Idéal pour 3-5 jours de visite ou des résidents franciliens occasionnels.</strong></p>

        <h3>Navigo Easy (<?= e(format_price(2.00)) ?> la carte)</h3>
        <p>Carte sans contact rechargeable, anonyme. Permet de charger des tickets t+ ou un forfait journée. <strong>Idéal pour éviter les tickets papier (perte, démagnétisation).</strong> Une fois chargée, elle remplace le carton t+ et passe au lecteur des portillons sans contact.</p>

        <h3>Navigo Découverte (<?= e(format_price(5.00)) ?> la carte + forfait)</h3>
        <p>Carte personnalisée (photo obligatoire) qui supporte les <strong>forfaits Navigo</strong> : hebdomadaire à <strong><?= e(format_price(30.75)) ?></strong> ou mensuel à <strong><?= e(format_price(88.80)) ?></strong>. Tarif unique zones 1-5. <strong>Idéal pour 4 jours et plus, ou résidents franciliens.</strong></p>

        <h3>Navigo Liberté+ (carte gratuite, paiement à l'usage)</h3>
        <p>Carte personnalisée gratuite. Vous validez à chaque trajet, et la RATP prélève <strong><?= e(format_price(1.73)) ?> par voyage métro/RER</strong> en fin de mois, avec un plafond mensuel garanti (égal au prix du forfait mensuel). <strong>Idéal pour des résidents franciliens occasionnels qui ne savent pas combien de voyages ils feront.</strong></p>

        <h2>Acheter un titre pour le métro</h2>
        <p>Plusieurs canaux disponibles :</p>
        <ul>
            <li><strong>Distributeurs automatiques</strong> dans toutes les stations métro (paiement CB ou espèces, multilingue).</li>
            <li><strong>Guichets RATP</strong> dans les stations principales (Châtelet, Gare de Lyon, Saint-Lazare, La Défense, etc.) — conseil + Navigo personnalisé.</li>
            <li><strong>Application Bonjour RATP</strong> pour acheter et valider des tickets t+ via NFC sur smartphone (Android + iPhone récents).</li>
            <li><strong>Tabacs et points relais agréés</strong> en Paris et région (autocollant « Vente RATP »).</li>
        </ul>

        <h2>Validation et contrôles</h2>
        <p>L'accès au quai métro se fait obligatoirement par un <strong>portillon validateur</strong> (ticket papier ou Navigo). Toutes les stations sont fermées : pas de validation = pas d'accès. Des contrôleurs RATP circulent ponctuellement dans les rames et aux sorties, l'amende au tarif de base est de <strong><?= e(format_price(50.00)) ?></strong> en paiement immédiat. Conservez votre ticket pendant tout le trajet : le contrôle peut intervenir à la sortie.</p>

        <h2>Cas particuliers</h2>

        <h3>Métro vers les aéroports</h3>
        <p>La <strong>Ligne 14</strong> dessert directement l'<strong>aéroport d'Orly</strong> depuis 2024 (terminus sud). Le billet dédié coûte <strong><?= e(format_price(13.00)) ?></strong>. Pour <strong>Charles de Gaulle</strong>, pas de métro direct : utiliser le <strong>RER B</strong> depuis Châtelet ou Gare du Nord (<?= e(format_price(11.80)) ?>). Voir le <a href="/tarifs/aeroports/">guide complet tarifs aéroports</a>.</p>

        <h3>Métro vers les gares parisiennes</h3>
        <p>Les 7 grandes gares parisiennes (Lyon, Nord, Est, Saint-Lazare, Montparnasse, Austerlitz, Bercy) sont toutes desservies par au moins une ligne de métro et le RER. Trajet couvert par le ticket t+ classique.</p>

        <h2>Tarifs jeunes et seniors</h2>
        <p>Plusieurs réductions sont disponibles :</p>
        <ul>
            <li><strong>-4 ans</strong> : voyagent gratuitement, sans titre.</li>
            <li><strong>4-10 ans</strong> : tarif réduit -50 % sur tickets t+ et Navigo.</li>
            <li><strong>Imagine'R (-26 ans)</strong> : forfait étudiant à tarif préférentiel pour scolaires/étudiants.</li>
            <li><strong>Solidarité Transport</strong> : réduction 75-100 % pour bénéficiaires RSA et CSS, attribuée par IDFM.</li>
            <li><strong>Senior (65+ ans)</strong> : pas de tarif spécifique métro, mais le <strong>Forfait Améthyste</strong> permet aux seniors résidents Paris/IDF d'obtenir un Navigo gratuit ou très réduit selon les revenus (à demander à la mairie de résidence).</li>
        </ul>

        <h2>Questions fréquentes sur les tarifs métro</h2>
        <div class="faq-list">
            <?php foreach ($faqs as $i => $f): ?>
                <details class="faq-item" <?= $i === 0 ? 'open' : '' ?>>
                    <summary class="faq-question">
                        <h3 class="faq-question__heading"><?= e($f['q']) ?></h3>
                    </summary>
                    <div class="faq-answer">
                        <p><?= richText($f['a']) ?></p>
                    </div>
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
