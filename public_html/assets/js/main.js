/**
 * main.js - BougeaParis.fr
 *
 * Interactions JavaScript de base :
 * - Menu burger mobile
 * - Preparation pour les composants a venir (widget itineraire, etc.)
 */

(function() {
    'use strict';

    // Menu burger
    const toggle = document.querySelector('.site-header__menu-toggle');
    const nav = document.querySelector('#site-nav');

    if (toggle && nav) {
        toggle.addEventListener('click', function() {
            const isOpen = nav.classList.toggle('is-open');
            toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        });

        // Fermer le menu quand on clique sur un lien (mobile)
        nav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                nav.classList.remove('is-open');
                toggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    // Les prochains composants (widget itineraire, autocomplete...) seront
    // charges ici ou dans leurs propres fichiers dedies.

})();
