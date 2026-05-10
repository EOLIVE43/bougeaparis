<?php
/**
 * Page hub : /tarifs/
 * Topic cluster Tarifs IDFM, canonique principal du cluster.
 * Lit data/global/transit-pricing.json (source unique).
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

// FAQ schema
$faqs = [
    ['q' => 'Combien coûte un ticket de métro à Paris en 2026 ?',
     'a' => "Un <strong>ticket t+</strong> (à l'unité) coûte <strong>2,15 €</strong> en 2026 et donne droit à un trajet en métro avec correspondances illimitées pendant 2 heures (métro/RER intra-Paris uniquement)."],
    ['q' => 'Quel est le prix du carnet de 10 tickets ?',
     'a' => "Le <strong>carnet de 10 tickets t+</strong> coûte <strong>17,35 €</strong>, soit 1,73 € par ticket — une économie de 19 % par rapport à l'achat à l'unité. Disponible sur Navigo Easy ou en tickets papier."],
    ['q' => 'Combien coûte un Pass Navigo mensuel toutes zones ?',
     'a' => "Le <strong>forfait Navigo Découverte mensuel</strong> coûte <strong>88,80 €</strong> en 2026, valable sur les 5 zones (1-5) sans supplément. Il s'agit du tarif unique francilien instauré en 2015."],
    ['q' => 'Quelle est la différence entre Navigo Découverte et Navigo Liberté+ ?',
     'a' => "Le <strong>Navigo Découverte</strong> est un forfait mensuel ou hebdomadaire à payer d'avance. Le <strong>Navigo Liberté+</strong> facture à l'usage : 1,73 € par voyage métro/RER, prélevé en fin de mois avec un plafond mensuel garanti. Liberté+ est plus économique pour les voyageurs occasionnels."],
    ['q' => 'Le ticket t+ est-il valable dans les bus ?',
     'a' => "Oui. Le <strong>ticket t+</strong> est valable sur le métro, le RER intra-Paris, le bus et le tramway, avec correspondances illimitées entre métro et RER pendant 2 heures. Les correspondances bus-bus et bus-tramway sont également couvertes."],
    ['q' => 'Quelles sont les zones tarifaires en Île-de-France ?',
     'a' => "Le réseau est divisé en <strong>5 zones</strong> : zone 1 (Paris intra-muros), zone 2 (petite couronne), zone 3 (banlieue proche), zones 4-5 (grande couronne). Depuis 2015, le forfait Navigo Découverte est au tarif unique sur les zones 1-5."],
    ['q' => 'Combien coûte le RER B vers l\'aéroport Charles de Gaulle ?',
     'a' => "Le billet <strong>Paris ↔ CDG en RER B</strong> coûte <strong>11,80 €</strong> en 2026. Trajet direct depuis Châtelet ou Gare du Nord en environ 35 minutes. Le ticket t+ classique n'est <em>pas</em> valable sur cette liaison."],
    ['q' => 'Comment aller à Disneyland en transport en commun ?',
     'a' => "Le <strong>RER A direct Paris ↔ Marne-la-Vallée — Chessy</strong> (gare Disneyland) coûte <strong>8,45 €</strong>. Trajet d'environ 35 min. Couvert par le forfait Navigo zones 1-5 sans supplément."],
    ['q' => 'Existe-t-il des tarifs réduits pour les jeunes ?',
     'a' => "Oui. Les <strong>moins de 4 ans</strong> voyagent gratuitement. Les <strong>4-10 ans</strong> bénéficient d'un tarif réduit de -50 %. Les <strong>scolaires et étudiants -26 ans</strong> peuvent souscrire au forfait Imagine'R à tarif préférentiel."],
    ['q' => 'Où acheter un ticket de métro à Paris ?',
     'a' => "Les tickets t+ et carnets s'achètent : aux <strong>guichets RATP</strong> dans les stations principales, aux <strong>distributeurs automatiques</strong> dans toutes les stations, sur l'<strong>application Bonjour RATP</strong> (chargement Navigo Easy/Découverte) ou en ligne sur le site IDFM."],
    ['q' => 'Le Pass Navigo est-il rentable pour 4 jours à Paris ?',
     'a' => "Oui, généralement. Le <strong>forfait hebdomadaire Navigo Découverte (30,75 €)</strong> devient rentable à partir de 14 voyages dans la semaine. Pour 4 jours actifs (≈ 4-5 trajets/jour), le forfait est plus économique qu'un carnet de 10 + tickets supplémentaires."],
    ['q' => 'Les tarifs IDFM 2026 sont-ils valables toute l\'année ?',
     'a' => "Oui. Les tarifs IDFM sont fixés annuellement et valables du 1er janvier au 31 décembre. Toute mise à jour est annoncée via le site officiel <strong>iledefrance-mobilites.fr</strong>."],
];

$tpl->seo->addSchema([
    '@context' => 'https://schema.org',
    '@type'    => 'FAQPage',
    'mainEntity' => array_map(fn($f) => [
        '@type' => 'Question',
        'name'  => $f['q'],
        'acceptedAnswer' => ['@type' => 'Answer', 'text' => strip_tags($f['a'])],
    ], $faqs),
]);
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
    <div class="container" style="max-width:920px;">

        <p>Les <strong>tarifs des transports en commun en Île-de-France</strong> sont fixés annuellement par <strong>Île-de-France Mobilités (IDFM)</strong>, l'autorité organisatrice régionale, et appliqués par les opérateurs : <strong>RATP</strong> (métro, bus, tramway et RER A/B), <strong>SNCF Transilien</strong> (RER C/D/E et lignes Transilien), <strong>Optile</strong> et autres opérateurs privés (bus de banlieue, navettes aéroports). Ce guide regroupe tous les titres de transport en vigueur et leurs cas d'usage les plus fréquents.</p>

        <h2>Le système tarifaire francilien</h2>

        <p>Depuis le <strong>1er septembre 2015</strong>, le forfait <strong>Navigo Découverte</strong> est passé au <strong>tarif unique zones 1-5</strong> : peu importe que vous habitiez à Paris ou à 50 km, le mensuel coûte le même prix. Cette réforme a simplifié massivement la grille, mais les <strong>tickets unitaires</strong> (ticket t+, carnet) restent eux limités aux zones 1-2 dans la pratique pour le métro/RER intra-Paris.</p>

        <p>Le réseau reste divisé en 5 zones tarifaires :</p>
        <ul>
            <?php foreach ($zones as $z => $label): ?>
                <?php if ($z === '_doc') continue; ?>
                <li><strong>Zone <?= e($z) ?></strong> — <?= e($label) ?></li>
            <?php endforeach; ?>
        </ul>

        <h2>Tickets unitaires</h2>
        <p>Les tickets t+ et le carnet de 10 sont les solutions les plus économiques pour les voyageurs occasionnels et les touristes en visite courte (1 à 3 jours).</p>

        <?php foreach (['ticket_t_plus', 'carnet_10', 'navigo_easy'] as $key):
            $t = $tickets[$key] ?? null; if (!$t) continue;
        ?>
            <h3><?= e($t['name']) ?> <?php if (!empty($t['price_eur'])): ?>(<?= e(format_price((float)$t['price_eur'])) ?>)<?php endif; ?></h3>
            <p>
                <?php if (!empty($t['valid_for'])): ?>
                    <strong>Valable :</strong> <?= e($t['valid_for']) ?>.
                <?php endif; ?>
                <?php if (!empty($t['ideal_for'])): ?>
                    <strong>Idéal pour :</strong> <?= e($t['ideal_for']) ?>.
                <?php endif; ?>
                <?php if (!empty($t['discount_vs_unit_pct'])): ?>
                    <strong>Économie :</strong> −<?= (int)$t['discount_vs_unit_pct'] ?> % vs ticket à l'unité.
                <?php endif; ?>
                <?php if (!empty($t['transfers_note'])): ?>
                    <?= e($t['transfers_note']) ?>.
                <?php endif; ?>
            </p>
        <?php endforeach; ?>

        <h2>Forfaits Navigo</h2>
        <p>Pour les voyageurs réguliers (résidents franciliens, séjours longs, étudiants), les forfaits Navigo offrent un coût marginal très bas par voyage et un confort d'usage incomparable.</p>

        <?php foreach (['navigo_decouverte', 'navigo_liberte_plus'] as $key):
            $p = $passes[$key] ?? null; if (!$p) continue;
        ?>
            <h3><?= e($p['name']) ?></h3>
            <p>
                <?php if (isset($p['card_price_eur'])): ?>
                    <strong>Carte :</strong> <?= e(format_price((float)$p['card_price_eur'])) ?>.
                <?php endif; ?>
                <?php if (!empty($p['weekly_price_eur'])): ?>
                    <strong>Forfait hebdomadaire :</strong> <?= e(format_price((float)$p['weekly_price_eur'])) ?>.
                <?php endif; ?>
                <?php if (!empty($p['monthly_price_eur'])): ?>
                    <strong>Forfait mensuel :</strong> <?= e(format_price((float)$p['monthly_price_eur'])) ?>.
                <?php endif; ?>
                <?php if (!empty($p['price_per_trip_eur'])): ?>
                    <strong>Coût par trajet :</strong> <?= e(format_price((float)$p['price_per_trip_eur'])) ?>.
                <?php endif; ?>
                <?php if (!empty($p['ideal_for'])): ?>
                    <strong>Idéal pour :</strong> <?= e($p['ideal_for']) ?>.
                <?php endif; ?>
            </p>
        <?php endforeach; ?>

        <h2>Tarifs réduits et gratuités</h2>
        <ul>
            <?php foreach ($free as $fc): ?>
                <li><strong><?= e($fc['category']) ?></strong> — <?= e($fc['description'] ?? '') ?>.</li>
            <?php endforeach; ?>
        </ul>

        <h2>Tarifs spéciaux : aéroports et Disneyland</h2>
        <p>Pour les liaisons vers les aéroports parisiens et Disneyland, des billets dédiés s'appliquent (le ticket t+ classique n'est pas toujours valable). Voici les principaux tarifs :</p>
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
        <p>Les titres de transport sont disponibles dans plusieurs canaux :</p>
        <ul>
            <li><strong>Distributeurs automatiques</strong> : présents dans toutes les stations métro et RER, paiement carte ou espèces.</li>
            <li><strong>Guichets RATP</strong> : conseil voyageur + vente de Navigo dans les stations principales.</li>
            <li><strong>Application Bonjour RATP</strong> : achat de tickets t+ et chargement Navigo Easy/Découverte sur smartphone (Android NFC + iPhone récents).</li>
            <li><strong>Tabacs et points relais agréés</strong> : tickets t+ et carnets en région.</li>
            <li><strong>Site et app IDFM</strong> : commande de Navigo Découverte par envoi postal.</li>
        </ul>

        <h2>Questions fréquentes sur les tarifs IDFM</h2>
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
            <li><a href="/tarifs/metro/">Tarifs du métro de Paris : guide complet</a></li>
            <li><a href="/tarifs/aeroports/">Tarifs métro/RER vers les aéroports parisiens</a></li>
            <li><a href="/metro/">Toutes les lignes de métro de Paris</a></li>
            <li><a href="/info-trafic/">Info trafic en direct</a></li>
        </ul>

        <p style="font-size:0.9em;color:#5A6B66;margin-top:2.5rem;">
            <?php if ($valid): ?>Tarifs en vigueur depuis le <?= e(dateFr($valid, 'long_with_day')) ?>. <?php endif; ?>
            Source officielle : <?php if ($srcUrl): ?><a href="<?= e($srcUrl) ?>" target="_blank" rel="noopener">Île-de-France Mobilités</a><?php else: ?>Île-de-France Mobilités<?php endif; ?>.
        </p>
    </div>
</section>
