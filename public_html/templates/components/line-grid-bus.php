<?php
/**
 * Composant line-grid-bus - reseau bus segmente par categorie.
 * Le reseau bus (~1500 lignes) est trop dense pour tout afficher.
 */
?>
<div class="bus-network-grid" role="list" aria-label="Reseaux de bus d'Ile-de-France">

    <div class="bus-network-grid__category">
        <h3 class="bus-network-grid__title">Reseau parisien &amp; proche banlieue</h3>
        <div class="bus-network-grid__items">
            <a href="/bus/mobilien/" class="bus-network-grid__item" role="listitem">
                <span class="bus-network-grid__badge bus-network-grid__badge--mobilien">Mobilien</span>
                <span class="bus-network-grid__info">
                    <strong>Lignes Mobilien</strong>
                    <span>Bus frequents et amplitudes elargies</span>
                </span>
            </a>
            <a href="/bus/paris/" class="bus-network-grid__item" role="listitem">
                <span class="bus-network-grid__badge bus-network-grid__badge--urbain">20-96</span>
                <span class="bus-network-grid__info">
                    <strong>Bus parisiens</strong>
                    <span>Reseau historique de Paris intramuros</span>
                </span>
            </a>
            <a href="/bus/petite-ceinture/" class="bus-network-grid__item" role="listitem">
                <span class="bus-network-grid__badge bus-network-grid__badge--petite-ceinture">PC</span>
                <span class="bus-network-grid__info">
                    <strong>Petite Ceinture</strong>
                    <span>Lignes PC1, PC2, PC3 autour de Paris</span>
                </span>
            </a>
        </div>
    </div>

    <div class="bus-network-grid__category">
        <h3 class="bus-network-grid__title">Banlieue &amp; grande couronne</h3>
        <div class="bus-network-grid__items">
            <a href="/bus/banlieue/" class="bus-network-grid__item" role="listitem">
                <span class="bus-network-grid__badge bus-network-grid__badge--banlieue">100-799</span>
                <span class="bus-network-grid__info">
                    <strong>Lignes de banlieue</strong>
                    <span>Reseau IDFM en petite et grande couronne</span>
                </span>
            </a>
            <a href="/bus/express/" class="bus-network-grid__item" role="listitem">
                <span class="bus-network-grid__badge bus-network-grid__badge--express">Express</span>
                <span class="bus-network-grid__info">
                    <strong>Lignes Express</strong>
                    <span>Liaisons rapides inter-banlieues</span>
                </span>
            </a>
        </div>
    </div>

    <div class="bus-network-grid__category">
        <h3 class="bus-network-grid__title">Reseau nocturne</h3>
        <div class="bus-network-grid__items">
            <a href="/bus/noctilien/" class="bus-network-grid__item" role="listitem">
                <span class="bus-network-grid__badge bus-network-grid__badge--noctilien">N</span>
                <span class="bus-network-grid__info">
                    <strong>Noctilien</strong>
                    <span>47 lignes de bus de nuit (0h30 - 5h30)</span>
                </span>
            </a>
        </div>
    </div>

</div>
