<?php
/**
 * Page placeholder : /itineraires/
 * Le planificateur d'itineraires sera disponible dans une version
 * ulterieure. Pour ne pas casser le menu, page transitoire avec
 * 4 liens vers les outils tiers officiels.
 */

$tpl->seo
    ->setTitle('Itinéraires Paris : planifier votre trajet en transport')
    ->setDescription('Outils pour calculer un itinéraire d\'un point A à un point B en métro, RER, bus, tramway en Île-de-France. Solutions officielles RATP, IDFM.')
    ->setCanonical('/itineraires/')
    ->setRobots('noindex, follow')  // placeholder, ne pas indexer pour l'instant
    ->setBreadcrumb([
        ['label' => 'Accueil',     'url' => '/'],
        ['label' => 'Se déplacer', 'url' => '/se-deplacer/'],
        ['label' => 'Itinéraires', 'url' => '/itineraires/'],
    ]);
$tpl->addStylesheet('/assets/css/tarifs.css');

$tpl->partial('components/breadcrumb', [
    'items' => [
        ['label' => 'Accueil',     'url' => '/'],
        ['label' => 'Se déplacer', 'url' => '/se-deplacer/'],
        ['label' => 'Itinéraires', 'url' => '/itineraires/'],
    ],
]);
?>

<article class="section">
    <div class="container">
        <header class="hero">
            <h1 class="hero__title">Itinéraires Paris : planifier votre trajet en transport</h1>
            <p class="hero__subtitle">Calculer un trajet d'un point A à un point B en transport en commun en Île-de-France.</p>
        </header>

        <section class="section">
            <p>La fonctionnalité d'<strong>itinéraires personnalisés</strong> sera prochainement disponible sur BougeaParis. Elle vous permettra de calculer le meilleur trajet entre deux adresses ou stations en combinant métro, RER, bus, tramway et marche à pied, avec des informations en temps réel sur les perturbations.</p>
            <p>En attendant la mise en ligne de notre planificateur, voici les <strong>outils officiels et reconnus</strong> que nous recommandons pour organiser vos déplacements :</p>
            <ul>
                <li><strong>Bonjour RATP</strong> — application officielle de la RATP, couvrant métro, RER, bus et tramway, avec info trafic temps réel. <a href="https://bonjour.ratp.fr/" rel="noopener noreferrer">bonjour.ratp.fr</a></li>
                <li><strong>Île-de-France Mobilités</strong> — planificateur officiel régional, couvre l'ensemble des modes franciliens (y compris Transilien, bus de grande couronne). <a href="https://www.iledefrance-mobilites.fr/" rel="noopener noreferrer">iledefrance-mobilites.fr</a></li>
                <li><strong>Citymapper</strong> — référence internationale pour iOS et Android, prend en compte le vélo, le scooter et la marche en plus du transport en commun. <a href="https://citymapper.com/paris" rel="noopener noreferrer">citymapper.com/paris</a></li>
                <li><strong>Google Maps</strong> — intégration cartographique complète, alertes trafic temps réel et alternatives multiples. <a href="https://maps.google.com/" rel="noopener noreferrer">maps.google.com</a></li>
            </ul>
            <p>Tous ces services exploitent les mêmes données IDFM officielles que BougeaParis, donc les résultats restent cohérents avec ceux qui apparaîtront ici une fois notre planificateur lancé.</p>
        </section>

        <section class="section">
            <h2>En attendant le planificateur</h2>
            <p>Explorez le réseau mode par mode pour comprendre les correspondances et choisir votre itinéraire :</p>
            <ul>
                <li><a href="/se-deplacer/">Vue d'ensemble des 7 modes de transport</a></li>
                <li><a href="/metro/">Métro de Paris : plan et lignes</a></li>
                <li><a href="/rer/">Réseau RER : 5 lignes traversantes</a></li>
                <li><a href="/tarifs/">Tarifs IDFM 2026</a></li>
                <li><a href="/info-trafic/">Info-trafic temps réel</a></li>
            </ul>
        </section>
    </div>
</article>
