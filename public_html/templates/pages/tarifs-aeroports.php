<?php
/**
 * Page : /tarifs/aeroports/
 * Sous-page spécialisée du cluster Tarifs.
 * Très fort volume SEO : « rer b cdg prix », « metro orly tarif », etc.
 */

$pricing = transit_pricing();
$airports = $pricing['airports'] ?? [];
$cdg  = $airports['cdg']  ?? null;
$orly = $airports['orly'] ?? null;
$bva  = $airports['beauvais'] ?? null;

$tpl->seo
    ->setTitle('Tarifs métro/RER vers les aéroports parisiens 2026')
    ->setDescription('Tarifs CDG (RER B 11,80 €, Roissybus 16,60 €, Bus 350 2,15 €), Orly (Ligne 14 13 €, T7 2,15 €) et Beauvais. Comparateur prix vs temps de trajet.')
    ->setCanonical('/tarifs/aeroports/')
    ->setBreadcrumb([
        ['label' => 'Accueil',   'url' => '/'],
        ['label' => 'Tarifs',    'url' => '/tarifs/'],
        ['label' => 'Aéroports', 'url' => '/tarifs/aeroports/'],
    ]);

$faqs = [
    ['q' => "Combien coûte le RER B vers l'aéroport Charles de Gaulle ?",
     'a' => "Le billet <strong>Paris ↔ CDG en RER B</strong> coûte <strong>11,80 €</strong> en 2026 (tarif unique adulte). Le trajet dure environ 35 minutes depuis Châtelet ou Gare du Nord, avec un train toutes les 10-15 minutes."],
    ['q' => "Le ticket t+ classique est-il valable pour aller à CDG ?",
     'a' => "<strong>Non, pas pour le RER B direct</strong>. Il faut acheter un billet « Paris-CDG » dédié à 11,80 €. <strong>En revanche, le bus 350 (Gare de l'Est ↔ CDG)</strong> est couvert par le ticket t+ à 2,15 €, mais le trajet dure environ 80 minutes."],
    ['q' => "Quelle est la solution la moins chère pour aller à CDG ?",
     'a' => "Le <strong>bus 350</strong> à 2,15 € avec ticket t+ est l'option la plus économique, mais aussi la plus lente (≈ 80 min). Pour un compromis prix/temps, le <strong>RER B</strong> à 11,80 € en 35 min reste le meilleur rapport. Le <strong>Roissybus</strong> à 16,60 € est plus cher mais évite les correspondances."],
    ['q' => "Comment aller à l'aéroport d'Orly en métro ?",
     'a' => "Depuis juin 2024, la <strong>Ligne 14</strong> du métro dessert directement <strong>Orly</strong> (terminus sud). Tarif : <strong>13,00 €</strong>, durée 25 minutes depuis Châtelet. C'est l'option la plus rapide et la plus simple. Avant 2024, il fallait emprunter le RER B + Orlyval."],
    ['q' => "Quelle est la différence entre Orlybus et Tramway T7 vers Orly ?",
     'a' => "L'<strong>Orlybus</strong> (Denfert-Rochereau ↔ Orly) coûte <strong>11,50 €</strong> et met 30 min. Le <strong>Tramway T7</strong> (Villejuif ↔ Orly) ne coûte que <strong>2,15 €</strong> avec ticket t+ mais met 70 min depuis Paris (correspondance). T7 est plus économique, Orlybus est plus rapide et confortable."],
    ['q' => "Les enfants paient-ils le même prix pour les aéroports ?",
     'a' => "Les <strong>moins de 4 ans</strong> voyagent gratuitement sur tous les modes IDFM. Les <strong>4-10 ans</strong> bénéficient d'un tarif réduit -50 % sur le RER B (≈ 5,90 € vers CDG) et la Ligne 14 vers Orly. Le bus 350 est gratuit -4 ans et facturé tarif réduit 4-10 ans."],
    ['q' => "Le Pass Navigo couvre-t-il les trajets vers les aéroports ?",
     'a' => "Le <strong>Navigo Découverte zones 1-5</strong> couvre intégralement les trajets <strong>Paris ↔ CDG</strong> (RER B), <strong>Paris ↔ Orly</strong> (Ligne 14, RER B + Orlyval, T7) et les bus 350/Orlybus/Roissybus. Aucun supplément. C'est l'option la plus rentable pour des allers-retours fréquents ou un long séjour."],
    ['q' => "Comment aller à Beauvais en transport en commun ?",
     'a' => "L'<strong>aéroport de Beauvais-Tillé</strong> n'a pas de liaison ferroviaire directe. La <strong>navette officielle</strong> Porte Maillot ↔ Beauvais (75 min, <strong>17,90 €</strong>) est la seule option transport public. Réservation conseillée en ligne pour les vols low-cost matinaux."],
    ['q' => "Faut-il acheter le billet aéroport à l'avance ?",
     'a' => "Non, pas obligatoire pour le RER B, la Ligne 14 ou les bus RATP : achat aux distributeurs des stations le jour J. <strong>Pour la navette Beauvais</strong>, la réservation en ligne est fortement conseillée (places limitées). <strong>Pour le Roissybus</strong>, achat à bord avec carte ou aux automates Opéra/CDG."],
    ['q' => "Existe-t-il un billet « Aéroport » spécial touriste ?",
     'a' => "Le <strong>Paris Visite</strong> (forfait touriste 1-5 jours) inclut les liaisons aéroports en zones 1-5 (CDG, Orly), à condition d'acheter la version « zones 1-5 ». Tarif Paris Visite 1 jour zones 1-5 : ≈ 25 € (à confirmer 2026). Rentable uniquement si vous prévoyez de nombreux trajets dans la même journée."],
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
            <li class="breadcrumb__current">Aéroports</li>
        </ol>
    </div>
</nav>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">Tarifs métro/RER vers les aéroports parisiens</h1>
        <p class="hero__subtitle">Toutes les options de transport public vers Charles de Gaulle, Orly et Beauvais en 2026 : prix, durée, conseils. Comparateur honnête prix vs temps de trajet.</p>
    </div>
</section>

<section class="section">
    <div class="container" style="max-width:920px;">

        <p>Rejoindre les <strong>aéroports parisiens</strong> en transport en commun est un choix économique et écologique, mais le réseau IDFM propose plusieurs options dont les prix varient de 2,15 € à 17,90 € selon la destination et le mode. Ce guide compare honnêtement le prix, la durée et le confort de chaque option pour <strong>Charles de Gaulle (CDG)</strong>, <strong>Orly</strong> et <strong>Beauvais-Tillé (BVA)</strong>.</p>

        <?php /* ============= CDG ============= */ ?>
        <h2>Aéroport Charles de Gaulle (CDG)</h2>
        <p><strong>4 options principales</strong> pour rejoindre CDG depuis Paris en transport public, du moins cher au plus rapide :</p>

        <?php if ($cdg && !empty($cdg['options'])): foreach ($cdg['options'] as $key => $o): ?>
            <h3><?= e($o['label']) ?> (<?= e(format_price((float)$o['price_eur'])) ?>)</h3>
            <p>
                <strong>Prix :</strong> <?= e(format_price((float)$o['price_eur'])) ?>.
                <strong>Durée :</strong> ~<?= (int)$o['duration_min_paris'] ?> min depuis Paris.
                <strong>Fréquence :</strong> <?= e($o['frequency']) ?>.
                <br><strong>Idéal pour :</strong> <?= e($o['ideal_for']) ?>.
                <br><strong>Validité :</strong> <?= e($o['valid_for']) ?>.
            </p>
        <?php endforeach; endif; ?>

        <?php /* ============= ORLY ============= */ ?>
        <h2>Aéroport d'Orly</h2>
        <p>Depuis juin 2024, la <strong>Ligne 14</strong> du métro dessert directement Orly. Cela a transformé l'accessibilité de l'aéroport sud, désormais relié à Châtelet en 25 minutes. Les autres options restent disponibles selon votre point de départ :</p>

        <?php if ($orly && !empty($orly['options'])): foreach ($orly['options'] as $key => $o): ?>
            <h3><?= e($o['label']) ?> (<?= e(format_price((float)$o['price_eur'])) ?>)</h3>
            <p>
                <strong>Prix :</strong> <?= e(format_price((float)$o['price_eur'])) ?>.
                <strong>Durée :</strong> ~<?= (int)$o['duration_min_paris'] ?> min depuis Paris.
                <strong>Fréquence :</strong> <?= e($o['frequency']) ?>.
                <br><strong>Idéal pour :</strong> <?= e($o['ideal_for']) ?>.
                <br><strong>Validité :</strong> <?= e($o['valid_for']) ?>.
            </p>
        <?php endforeach; endif; ?>

        <?php /* ============= BEAUVAIS ============= */ ?>
        <h2>Aéroport de Beauvais-Tillé (BVA)</h2>
        <p>L'aéroport de <strong>Beauvais-Tillé</strong>, situé à 85 km au nord de Paris, accueille principalement les compagnies low-cost (Ryanair, Wizz Air, Volotea). Aucune liaison ferroviaire directe — la navette officielle est la seule option transport public.</p>

        <?php if ($bva && !empty($bva['options'])): foreach ($bva['options'] as $key => $o): ?>
            <h3><?= e($o['label']) ?> (<?= e(format_price((float)$o['price_eur'])) ?>)</h3>
            <p>
                <strong>Prix :</strong> <?= e(format_price((float)$o['price_eur'])) ?>.
                <strong>Durée :</strong> ~<?= (int)$o['duration_min_paris'] ?> min.
                <strong>Fréquence :</strong> <?= e($o['frequency']) ?>.
                <br><strong>Idéal pour :</strong> <?= e($o['ideal_for']) ?>.
                <br><strong>Validité :</strong> <?= e($o['valid_for']) ?>.
            </p>
        <?php endforeach; endif; ?>

        <?php /* ============= COMPARATEUR ============= */ ?>
        <h2>Comparateur prix vs temps de trajet</h2>
        <p>Tableau récapitulatif pour choisir l'option adaptée à votre profil (vol matinal, bagages, budget) :</p>

        <div style="overflow-x:auto;">
        <table style="width:100%;border-collapse:collapse;font-size:0.95rem;">
            <thead>
                <tr style="background:#F1F3F2;">
                    <th style="padding:0.6rem;text-align:left;border-bottom:2px solid #B8C2BE;">Aéroport</th>
                    <th style="padding:0.6rem;text-align:left;border-bottom:2px solid #B8C2BE;">Option</th>
                    <th style="padding:0.6rem;text-align:right;border-bottom:2px solid #B8C2BE;">Prix</th>
                    <th style="padding:0.6rem;text-align:right;border-bottom:2px solid #B8C2BE;">Durée</th>
                </tr>
            </thead>
            <tbody>
                <tr><td style="padding:0.5rem;border-bottom:1px solid #E0E6E4;"><strong>CDG</strong></td><td style="padding:0.5rem;border-bottom:1px solid #E0E6E4;">Bus 350</td><td style="padding:0.5rem;text-align:right;border-bottom:1px solid #E0E6E4;">2,15 €</td><td style="padding:0.5rem;text-align:right;border-bottom:1px solid #E0E6E4;">80 min</td></tr>
                <tr><td style="padding:0.5rem;border-bottom:1px solid #E0E6E4;"><strong>CDG</strong></td><td style="padding:0.5rem;border-bottom:1px solid #E0E6E4;">RER B</td><td style="padding:0.5rem;text-align:right;border-bottom:1px solid #E0E6E4;">11,80 €</td><td style="padding:0.5rem;text-align:right;border-bottom:1px solid #E0E6E4;">35 min</td></tr>
                <tr><td style="padding:0.5rem;border-bottom:1px solid #E0E6E4;"><strong>CDG</strong></td><td style="padding:0.5rem;border-bottom:1px solid #E0E6E4;">Roissybus</td><td style="padding:0.5rem;text-align:right;border-bottom:1px solid #E0E6E4;">16,60 €</td><td style="padding:0.5rem;text-align:right;border-bottom:1px solid #E0E6E4;">60 min</td></tr>
                <tr><td style="padding:0.5rem;border-bottom:1px solid #E0E6E4;"><strong>Orly</strong></td><td style="padding:0.5rem;border-bottom:1px solid #E0E6E4;">Tramway T7</td><td style="padding:0.5rem;text-align:right;border-bottom:1px solid #E0E6E4;">2,15 €</td><td style="padding:0.5rem;text-align:right;border-bottom:1px solid #E0E6E4;">70 min</td></tr>
                <tr><td style="padding:0.5rem;border-bottom:1px solid #E0E6E4;"><strong>Orly</strong></td><td style="padding:0.5rem;border-bottom:1px solid #E0E6E4;">Orlybus</td><td style="padding:0.5rem;text-align:right;border-bottom:1px solid #E0E6E4;">11,50 €</td><td style="padding:0.5rem;text-align:right;border-bottom:1px solid #E0E6E4;">30 min</td></tr>
                <tr><td style="padding:0.5rem;border-bottom:1px solid #E0E6E4;"><strong>Orly</strong></td><td style="padding:0.5rem;border-bottom:1px solid #E0E6E4;">Ligne 14 (depuis 2024)</td><td style="padding:0.5rem;text-align:right;border-bottom:1px solid #E0E6E4;">13,00 €</td><td style="padding:0.5rem;text-align:right;border-bottom:1px solid #E0E6E4;">25 min</td></tr>
                <tr><td style="padding:0.5rem;border-bottom:1px solid #E0E6E4;"><strong>Orly</strong></td><td style="padding:0.5rem;border-bottom:1px solid #E0E6E4;">RER B + Orlyval</td><td style="padding:0.5rem;text-align:right;border-bottom:1px solid #E0E6E4;">13,55 €</td><td style="padding:0.5rem;text-align:right;border-bottom:1px solid #E0E6E4;">35 min</td></tr>
                <tr><td style="padding:0.5rem;"><strong>Beauvais</strong></td><td style="padding:0.5rem;">Navette Porte Maillot</td><td style="padding:0.5rem;text-align:right;">17,90 €</td><td style="padding:0.5rem;text-align:right;">75 min</td></tr>
            </tbody>
        </table>
        </div>

        <h2>Conseils pratiques</h2>
        <ul>
            <li><strong>Bagages volumineux</strong> : éviter le bus 350 et le tramway T7 (souvent saturés). Privilégier RER B, Ligne 14 ou navettes dédiées (Roissybus, Orlybus).</li>
            <li><strong>Vols très matinaux</strong> (avant 6h30) : aucun transport public ne couvre. Prévoir taxi/VTC.</li>
            <li><strong>Vols très tardifs</strong> (après 23h) : RER B ralenti, dernier départ Châtelet ≈ minuit. Ligne 14 jusqu'à 1h15 (2h15 V/S). Au-delà, taxi.</li>
            <li><strong>Économie maximale</strong> : combiner Pass Navigo Découverte zones 1-5 (88,80 €/mois) si vous voyagez plusieurs fois dans le mois.</li>
            <li><strong>Famille</strong> : la Ligne 14 vers Orly est l'option la plus simple avec enfants (pas de correspondance, accès PMR partout).</li>
        </ul>

        <h2>Questions fréquentes sur les tarifs aéroports</h2>
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
            <li><a href="/tarifs/metro/">Tarifs du métro de Paris : guide complet</a></li>
            <li><a href="/aeroports/">Hub Aéroports parisiens</a></li>
            <li><a href="/info-trafic/">Info trafic en direct</a></li>
        </ul>

    </div>
</section>
