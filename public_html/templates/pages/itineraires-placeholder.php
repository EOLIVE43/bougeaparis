<?php
/**
 * Page placeholder : /itineraires/
 * Periode transitoire : planificateur a venir. 4 outils tiers en attendant.
 * Refonte alignee sur /tarifs/ (intro enrichie, tool-cards inline, info-callout).
 * Reste en noindex,follow (page transitoire).
 */

$tpl->seo
    ->setTitle('Itinéraires Paris : planificateur multimodal BougeaParis')
    ->setDescription('Calculateur d\'itinéraires multimodaux en métro, RER, bus, tramway en Île-de-France. Fonctionnalité en cours de développement sur BougeaParis.')
    ->setCanonical('/itineraires/')
    ->setRobots('noindex, follow')
    ->setBreadcrumb([
        ['label' => 'Accueil',     'url' => '/'],
        ['label' => 'Se déplacer', 'url' => '/se-deplacer/'],
        ['label' => 'Itinéraires', 'url' => '/itineraires/'],
    ]);
$tpl->addStylesheet('/assets/css/tarifs.css');
?>

<?php $tpl->partial('components/breadcrumb', [
    'items' => [
        ['label' => 'Accueil',     'url' => '/'],
        ['label' => 'Se déplacer', 'url' => '/se-deplacer/'],
        ['label' => 'Itinéraires', 'url' => '/itineraires/'],
    ],
]); ?>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">Itinéraires Paris : planifier votre trajet en transport</h1>
        <p class="hero__subtitle">Calculer un trajet d'un point A à un point B en transport en commun en Île-de-France.</p>
    </div>
</section>

<section class="section">
    <div class="container tarifs-page">

        <h2>Bientôt sur BougeaParis : le planificateur d'itinéraires</h2>
        <p>Le planificateur d'<strong>itinéraires multimodaux</strong> est en cours de développement sur BougeaParis. Il vous permettra de <strong>calculer le meilleur trajet</strong> entre deux adresses ou stations en combinant métro, RER, bus, tramway et marche à pied, avec des <strong>informations en temps réel</strong> sur les perturbations.</p>
        <p>Cette fonctionnalité fait partie des <strong>prochaines évolutions du site</strong>. En attendant sa mise en ligne, retrouvez ci-dessous les ressources BougeaParis pour explorer le réseau et préparer vos trajets.</p>

        <h2>Explorer le réseau en attendant</h2>
        <p>Comprendre les correspondances et choisir votre itinéraire :</p>
        <ul>
            <li><a href="/se-deplacer/">Vue d'ensemble des 7 modes de transport</a></li>
            <li><a href="/metro/">Métro de Paris : plan et lignes</a></li>
            <li><a href="/rer/">Réseau RER : 5 lignes traversantes</a></li>
            <li><a href="/tarifs/">Tarifs IDFM 2026</a></li>
            <li><a href="/info-trafic/">Info-trafic temps réel</a></li>
        </ul>
    </div>
</section>
