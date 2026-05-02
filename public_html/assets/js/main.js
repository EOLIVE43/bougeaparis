/**
 * main.js - BougeaParis.fr
 *
 * Interactions JavaScript globales :
 * - Menu burger mobile (header)
 * - Smooth scroll pour les ancres internes (#trafic-temps-reel, etc.)
 * - Préparation pour les composants à venir (widget itinéraire, etc.)
 *
 * Vanilla JS, pas de framework. Chargé en defer.
 */

(function() {
    'use strict';

    // ----- Menu burger mobile -----
    const toggle = document.querySelector('.site-header__menu-toggle');
    const nav = document.querySelector('#site-nav');

    if (toggle && nav) {
        toggle.addEventListener('click', function() {
            const isOpen = nav.classList.toggle('is-open');
            toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        });

        // Fermer le menu quand on clique sur un lien (mobile)
        nav.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                nav.classList.remove('is-open');
                toggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    // ----- Smooth scroll pour les ancres internes -----
    // Utilisé notamment par les Quick Actions et le breadcrumb des pages ligne
    document.querySelectorAll('a[href^="#"]').forEach(function(link) {
        link.addEventListener('click', function(e) {
            var href = this.getAttribute('href');
            if (!href || href === '#') return;
            var target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ----- À venir -----
    // - Lazy loading manuel des éléments lourds
    // - Widget temps réel PRIM API

})();
