<?php
/**
 * Page hub Bus
 * /bus/ - page centrale du cocon bus
 */
?>
<nav class="breadcrumb" aria-label="Fil d'Ariane">
    <div class="container">
        <ol class="breadcrumb__list">
            <li><a href="/">Accueil</a></li>
            <li class="breadcrumb__current">Bus</li>
        </ol>
    </div>
</nav>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">Bus a Paris et en Ile-de-France</h1>
        <p class="hero__subtitle">Plus de 350 lignes de bus pour completer le reseau metro-RER. Lignes de jour, bus de nuit Noctilien, arrets, horaires et trafic en temps reel.</p>
    </div>
</section>

<?php include __DIR__ . '/../ads/slot-header.php'; ?>

<section class="section">
    <div class="container">
        <h2 class="section__title">Le reseau de bus parisien</h2>
        <p class="section__intro">Le bus est souvent le mode de transport le plus agreable pour decouvrir Paris en surface. Il permet de voir la ville tout en se deplacant et dessert les quartiers moins bien couverts par le metro. Certaines lignes sont devenues cultes pour leurs itineraires panoramiques.</p>

        <p class="text-muted">Les pages detaillees de chaque ligne de bus seront publiees prochainement.</p>
    </div>
</section>

<?php include __DIR__ . '/../ads/slot-in-article.php'; ?>

<section class="section section--alt">
    <div class="container">
        <h2 class="section__title">Noctilien : le bus de nuit parisien</h2>
        <p>Le Noctilien prend le relais du metro et du RER entre 0h30 et 5h30. Avec une cinquantaine de lignes, il permet de rejoindre Paris et la proche banlieue toute la nuit. Les lignes partent principalement de cinq poles : Chatelet, Gare de l'Est, Gare Saint-Lazare, Gare Montparnasse et Gare de Lyon.</p>

        <p>Que vous rentriez de soiree, preniez un vol tot le matin ou travailliez de nuit, le Noctilien est une solution fiable et beaucoup moins chere qu'un taxi ou un VTC.</p>

        <p>Une page dediee au Noctilien avec toutes les lignes, les horaires et les principaux itineraires sera disponible prochainement sur <a href="/bus/noctilien/">/bus/noctilien/</a>.</p>
    </div>
</section>

<?php include __DIR__ . '/../ads/slot-footer.php'; ?>
