<?php
/**
 * Page hub : /tarifs/
 * Topic cluster Tarifs IDFM, canonique principal du cluster.
 * Pattern visuel aligné sur les pages station (cards + accordéon FAQ).
 */

$pricing = transit_pricing();
$tickets = $pricing['tickets']  ?? [];
$passes  = $pricing['passes']   ?? [];
$free    = $pricing['free_categories'] ?? [];
$zones   = $pricing['zones']    ?? [];
$meta    = $pricing['_meta']    ?? [];
$valid   = $meta['valid_from']  ?? null;
$srcUrl  = $meta['source_url']  ?? null;

$tpl->seo
    ->setTitle('Tarifs et titres de transport en commun en Île-de-France 2026')
    ->setDescription('Guide complet des tarifs IDFM 2026 : ticket t+, carnet, Navigo, zones tarifaires, gratuités, tarifs vers aéroports. Source unique mise à jour.')
    ->setCanonical('/tarifs/')
    ->setBreadcrumb([
        ['label' => 'Accueil', 'url' => '/'],
        ['label' => 'Tarifs',  'url' => '/tarifs/'],
    ]);
$tpl->addStylesheet('/assets/css/tarifs.css');

// FAQ
$faqs = [
    ['q' => 'Combien coûte un ticket de métro à Paris en 2026 ?',
     'a' => "Un <strong>ticket t+</strong> (à l'unité) coûte <strong>2,15 €</strong> et donne droit à un trajet en métro avec correspondances illimitées pendant 2 heures (métro/RER intra-Paris uniquement)."],
    ['q' => 'Quel est le prix du carnet de 10 tickets ?',
     'a' => "Le <strong>carnet de 10 tickets t+</strong> coûte <strong>17,35 €</strong>, soit 1,73 € par ticket — une économie de 19 % par rapport à l'achat à l'unité. Disponible sur Navigo Easy ou en tickets papier."],
    ['q' => 'Combien coûte un Pass Navigo mensuel toutes zones ?',
     'a' => "Le <strong>forfait Navigo Découverte mensuel</strong> coûte <strong>88,80 €</strong> en 2026, valable sur les 5 zones (1-5) sans supplément. Tarif unique francilien depuis 2015."],
    ['q' => 'Quelle est la différence entre Navigo Découverte et Navigo Liberté+ ?',
     'a' => "Le <strong>Navigo Découverte</strong> est un forfait mensuel ou hebdomadaire à payer d'avance. Le <strong>Navigo Liberté+</strong> facture à l'usage : 1,73 € par voyage métro/RER, prélevé en fin de mois avec un plafond mensuel garanti. Liberté+ est plus économique pour les voyageurs occasionnels."],
    ['q' => 'Le ticket t+ est-il valable dans les bus ?',
     'a' => "Oui. Le <strong>ticket t+</strong> est valable sur le métro, le RER intra-Paris, le bus et le tramway, avec correspondances illimitées entre métro et RER pendant 2 heures."],
    ['q' => 'Quelles sont les zones tarifaires en Île-de-France ?',
     'a' => "Le réseau est divisé en <strong>5 zones</strong> : zone 1 (Paris intra-muros), zone 2 (petite couronne), zone 3 (banlieue proche), zones 4-5 (grande couronne). Depuis 2015, le forfait Navigo Découverte est au tarif unique sur les zones 1-5."],
    ['q' => 'Combien coûte le RER B vers l\'aéroport Charles de Gaulle ?',
     'a' => "Le billet <strong>Paris ↔ CDG en RER B</strong> coûte <strong>11,80 €</strong> en 2026. Trajet direct depuis Châtelet ou Gare du Nord en environ 35 minutes."],
    ['q' => 'Comment aller à Disneyland en transport en commun ?',
     'a' => "Le <strong>RER A direct Paris ↔ Marne-la-Vallée — Chessy</strong> coûte <strong>8,45 €</strong>. Trajet d'environ 35 min. Couvert par le forfait Navigo zones 1-5 sans supplément."],
    ['q' => 'Existe-t-il des tarifs réduits pour les jeunes ?',
     'a' => "Oui. Les <strong>moins de 4 ans</strong> voyagent gratuitement. Les <strong>4-10 ans</strong> bénéficient d'un tarif réduit de -50 %. Les <strong>scolaires et étudiants -26 ans</strong> peuvent souscrire au forfait Imagine'R à tarif préférentiel."],
    ['q' => 'Où acheter un ticket de métro à Paris ?',
     'a' => "Aux <strong>guichets RATP</strong>, aux <strong>distributeurs automatiques</strong> dans toutes les stations, sur l'<strong>application Bonjour RATP</strong> (chargement Navigo Easy/Découverte) ou en ligne sur le site IDFM."],
    ['q' => 'Le Pass Navigo est-il rentable pour 4 jours à Paris ?',
     'a' => "Oui, généralement. Le <strong>forfait hebdomadaire Navigo Découverte (30,75 €)</strong> devient rentable à partir de 14 voyages dans la semaine."],
    ['q' => 'Les tarifs IDFM 2026 sont-ils valables toute l\'année ?',
     'a' => "Oui. Les tarifs IDFM sont fixés annuellement et valables du 1er janvier au 31 décembre. Toute mise à jour est annoncée via le site officiel <strong>iledefrance-mobilites.fr</strong>."],
];

$tpl->seo->addSchema([
    '@context' => 'https://schema.org', '@type' => 'FAQPage',
    'mainEntity' => array_map(fn($f) => [
        '@type' => 'Question', 'name' => $f['q'],
        'acceptedAnswer' => ['@type' => 'Answer', 'text' => strip_tags($f['a'])],
    ], $faqs),
]);

// Helper card render
$renderCard = function (string $key, array $t) {
    $name        = $t['name'] ?? $key;
    $icon        = $t['icon'] ?? '🎫';
    $primaryEur  = $t['price_eur']      ?? $t['card_price_eur']      ?? null;
    $primaryLab  = $t['type']           ?? null;
    $weekly      = $t['weekly_price_eur']  ?? null;
    $monthly     = $t['monthly_price_eur'] ?? null;
    $perTrip     = $t['price_per_trip_eur'] ?? null;
    $idealFor    = $t['ideal_for']      ?? null;
    $validFor    = $t['valid_for']      ?? null;
    $features    = explode(',', $validFor ?? '');
    ?>
    <article class="tarif-card">
      <div class="tarif-card__header">
        <span class="tarif-card__icon" aria-hidden="true"><?= e($icon) ?></span>
        <h3 class="tarif-card__title"><?= e($name) ?></h3>
        <?php if ($primaryEur !== null): ?>
          <span class="tarif-card__price">
            <?= e(format_price((float)$primaryEur)) ?>
            <?php if ($primaryLab): ?><small class="tarif-card__price-sub"><?= e($primaryLab) ?></small><?php endif; ?>
          </span>
        <?php endif; ?>
      </div>
      <div class="tarif-card__body">
        <?php if ($validFor): ?>
          <p><strong>Valable :</strong> <?= e($validFor) ?>.</p>
        <?php endif; ?>
        <?php if ($weekly !== null || $monthly !== null || $perTrip !== null): ?>
          <ul class="tarif-card__sub">
            <?php if ($weekly !== null): ?><li><strong>Forfait hebdomadaire :</strong> <?= e(format_price((float)$weekly)) ?></li><?php endif; ?>
            <?php if ($monthly !== null): ?><li><strong>Forfait mensuel :</strong> <?= e(format_price((float)$monthly)) ?></li><?php endif; ?>
            <?php if ($perTrip !== null): ?><li><strong>Coût par trajet :</strong> <?= e(format_price((float)$perTrip)) ?></li><?php endif; ?>
          </ul>
        <?php endif; ?>
        <?php if ($idealFor): ?>
          <p><strong>Idéal pour :</strong> <?= e($idealFor) ?>.</p>
        <?php endif; ?>
      </div>
    </article>
    <?php
};
?>

<nav class="breadcrumb" aria-label="Fil d'Ariane">
    <div class="container">
        <ol class="breadcrumb__list">
            <li><a href="/">Accueil</a></li>
            <li class="breadcrumb__current">Tarifs</li>
        </ol>
    </div>
</nav>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">Tarifs et titres de transport en commun en Île-de-France</h1>
        <p class="hero__subtitle">Guide complet 2026 : ticket t+, carnet, Pass Navigo, zones tarifaires, tarifs vers aéroports et Disneyland. Tous les prix mis à jour, source unique IDFM.</p>
    </div>
</section>

<section class="section">
    <div class="container tarifs-page">

        <p>Les <strong>tarifs des transports en commun en Île-de-France</strong> sont fixés annuellement par <strong>Île-de-France Mobilités (IDFM)</strong>, l'autorité organisatrice régionale, et appliqués par les opérateurs : <strong>RATP</strong>, <strong>SNCF Transilien</strong>, <strong>Optile</strong> et autres. Ce guide regroupe tous les titres en vigueur et leurs cas d'usage les plus fréquents.</p>

        <h2>Le système tarifaire francilien</h2>

        <p>Depuis le <strong>1er septembre 2015</strong>, le forfait <strong>Navigo Découverte</strong> est passé au <strong>tarif unique zones 1-5</strong> : peu importe que vous habitiez à Paris ou à 50 km, le mensuel coûte le même prix. Les <strong>tickets unitaires</strong> (ticket t+, carnet) restent eux limités aux zones 1-2 dans la pratique pour le métro/RER intra-Paris.</p>

        <div class="zones-map" role="img" aria-label="Schéma des 5 zones tarifaires d'Île-de-France">
          <p class="zones-map__title">Zones tarifaires IDFM</p>
          <div class="zones-map__rings">
            <span class="zones-map__ring zones-map__ring--1">Zone 1<small>Paris</small></span>
            <span class="zones-map__ring zones-map__ring--2">Zone 2<small>Petite couronne</small></span>
            <span class="zones-map__ring zones-map__ring--3">Zone 3<small>Puteaux, Issy</small></span>
            <span class="zones-map__ring zones-map__ring--4">Zone 4<small>Saint-Germain</small></span>
            <span class="zones-map__ring zones-map__ring--5">Zone 5<small>Versailles, MLV</small></span>
          </div>
        </div>

        <div class="tarifs-callout tarifs-callout--info">
          <span class="tarifs-callout__icon" aria-hidden="true">💡</span>
          <strong>À savoir :</strong> le forfait Navigo Découverte est <strong>identique pour les 5 zones</strong>. Pas besoin de réfléchir à votre zone d'habitation pour calculer le prix de votre abonnement mensuel.
        </div>

        <h2>Tickets unitaires</h2>
        <p>Les tickets t+ et le carnet de 10 sont les solutions les plus économiques pour les voyageurs occasionnels et les touristes en visite courte (1 à 3 jours).</p>

        <div class="tarifs-cards">
            <?php foreach (['ticket_t_plus', 'carnet_10', 'navigo_easy'] as $k):
                if (!empty($tickets[$k])) $renderCard($k, $tickets[$k]); endforeach; ?>
        </div>

        <h2>Forfaits Navigo</h2>
        <p>Pour les voyageurs réguliers (résidents franciliens, séjours longs, étudiants), les forfaits Navigo offrent un coût marginal très bas par voyage.</p>

        <div class="tarifs-cards">
            <?php foreach (['navigo_decouverte', 'navigo_liberte_plus'] as $k):
                if (!empty($passes[$k])) $renderCard($k, $passes[$k]); endforeach; ?>
        </div>

        <h2>Comparateur des titres de transport</h2>
        <p>Quel titre choisir selon votre profil ? Le tableau ci-dessous synthétise les options principales.</p>

        <div class="tarifs-compare-wrapper">
          <table class="tarifs-compare">
            <thead>
              <tr><th scope="col">Titre</th><th scope="col">Prix</th><th scope="col">Validité</th><th scope="col">Idéal pour</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Ticket t+</strong></td><td class="tarifs-compare__price">2,15 €</td><td>2 h, métro/RER</td><td>Touriste 1 jour</td></tr>
              <tr><td><strong>Carnet de 10</strong></td><td class="tarifs-compare__price">17,35 €</td><td>2 h chacun</td><td>Touriste 2-3 jours</td></tr>
              <tr><td><strong>Navigo Easy</strong></td><td class="tarifs-compare__price">2 €</td><td>Carte rechargeable</td><td>Touristes occasionnels</td></tr>
              <tr><td><strong>Navigo Découverte hebdo</strong></td><td class="tarifs-compare__price">30,75 €</td><td>1 semaine</td><td>Visiteur 4 jours+</td></tr>
              <tr><td><strong>Navigo Découverte mensuel</strong></td><td class="tarifs-compare__price">88,80 €</td><td>1 mois</td><td>Résident occasionnel</td></tr>
              <tr><td><strong>Navigo Liberté+</strong></td><td class="tarifs-compare__price">1,73 € / voyage</td><td>À l'usage</td><td>Résident peu fréquent</td></tr>
            </tbody>
          </table>
        </div>

        <h2>Tarifs réduits et gratuités</h2>
        <ul>
            <?php foreach ($free as $fc): ?>
                <li><strong><?= e($fc['category']) ?></strong> — <?= e($fc['description'] ?? '') ?>.</li>
            <?php endforeach; ?>
        </ul>

        <h2>Tarifs spéciaux : aéroports et Disneyland</h2>
        <p>Pour les liaisons vers les aéroports parisiens et Disneyland, des billets dédiés s'appliquent. Le ticket t+ classique n'est pas toujours valable.</p>

        <div class="tarifs-callout tarifs-callout--warning">
          <span class="tarifs-callout__icon" aria-hidden="true">⚠️</span>
          <strong>Attention :</strong> le ticket t+ ne couvre pas le RER B Paris ↔ CDG (11,80 €) ni la Ligne 14 vers Orly (13 €). Ces liaisons nécessitent un billet dédié.
        </div>

        <ul>
            <li><strong>RER B vers Charles de Gaulle (CDG)</strong> : <?= e(format_price(11.80)) ?> — environ 35 min depuis Châtelet</li>
            <li><strong>Roissybus (Opéra ↔ CDG)</strong> : <?= e(format_price(16.60)) ?></li>
            <li><strong>Bus 350 (Gare de l'Est ↔ CDG)</strong> : <?= e(format_price(2.15)) ?> avec ticket t+</li>
            <li><strong>Ligne 14 directe vers Orly</strong> : <?= e(format_price(13.00)) ?> — 25 min depuis Châtelet (depuis 2024)</li>
            <li><strong>Tramway T7 vers Orly</strong> : <?= e(format_price(2.15)) ?> avec ticket t+</li>
            <li><strong>Orlybus (Denfert-Rochereau ↔ Orly)</strong> : <?= e(format_price(11.50)) ?></li>
            <li><strong>RER A direct vers Disneyland</strong> : <?= e(format_price(8.45)) ?> — 35 min depuis Paris</li>
        </ul>
        <p><a href="/tarifs/aeroports/">→ Voir le guide complet des tarifs vers les aéroports</a></p>

        <h2>Où acheter ?</h2>
        <ul>
            <li><strong>Distributeurs automatiques</strong> : présents dans toutes les stations métro et RER, paiement carte ou espèces.</li>
            <li><strong>Guichets RATP</strong> : conseil voyageur + vente de Navigo dans les stations principales.</li>
            <li><strong>Application Bonjour RATP</strong> : achat de tickets t+ et chargement Navigo Easy/Découverte sur smartphone (Android NFC + iPhone récents).</li>
            <li><strong>Tabacs et points relais agréés</strong> en Paris et région.</li>
            <li><strong>Site et app IDFM</strong> : commande de Navigo Découverte par envoi postal.</li>
        </ul>

        <h2>Questions fréquentes sur les tarifs IDFM</h2>
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
            <li><a href="/tarifs/metro/">Tarifs du métro de Paris : guide complet</a></li>
            <li><a href="/tarifs/aeroports/">Tarifs métro/RER vers les aéroports parisiens</a></li>
            <li><a href="/metro/">Toutes les lignes de métro de Paris</a></li>
            <li><a href="/info-trafic/">Info trafic en direct</a></li>
        </ul>

        <p class="tarifs-meta-footer">
            <?php if ($valid): ?>Tarifs en vigueur depuis le <?= e(dateFr($valid, 'long_with_day')) ?>. <?php endif; ?>
            Source officielle : <?php if ($srcUrl): ?><a href="<?= e($srcUrl) ?>" target="_blank" rel="noopener">Île-de-France Mobilités</a><?php else: ?>Île-de-France Mobilités<?php endif; ?>.
        </p>
    </div>
</section>
