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

    // ----- Lightbox (plan visuel agrandi) -----
    // Tout bouton avec data-lightbox-target="ID" ouvre le contenu de l'élément
    // d'ID donné dans une modal plein écran. Fermeture : ESC, clic sur le fond,
    // ou bouton de fermeture.
    function openLightbox(targetId) {
        var sourceEl = document.getElementById(targetId);
        if (!sourceEl) return;

        // Cloner le contenu de la source pour ne pas casser le DOM original
        var clone = sourceEl.cloneNode(true);
        clone.removeAttribute('id');

        // Construire la lightbox
        var overlay = document.createElement('div');
        overlay.className = 'lightbox';
        overlay.setAttribute('role', 'dialog');
        overlay.setAttribute('aria-modal', 'true');
        overlay.setAttribute('aria-label', 'Vue agrandie');

        var inner = document.createElement('div');
        inner.className = 'lightbox__inner';

        var closeBtn = document.createElement('button');
        closeBtn.type = 'button';
        closeBtn.className = 'lightbox__close';
        closeBtn.setAttribute('aria-label', 'Fermer');
        closeBtn.innerHTML = '&times;';

        inner.appendChild(closeBtn);
        inner.appendChild(clone);
        overlay.appendChild(inner);
        document.body.appendChild(overlay);
        document.body.classList.add('lightbox-open');

        // Animation d'entrée
        requestAnimationFrame(function() {
            overlay.classList.add('is-open');
        });

        // Fermeture
        function close() {
            overlay.classList.remove('is-open');
            document.body.classList.remove('lightbox-open');
            setTimeout(function() {
                if (overlay.parentNode) overlay.parentNode.removeChild(overlay);
            }, 200);
            document.removeEventListener('keydown', onKey);
        }
        function onKey(e) {
            if (e.key === 'Escape') close();
        }

        closeBtn.addEventListener('click', close);
        overlay.addEventListener('click', function(e) {
            // Fermer si clic sur le fond (pas sur le contenu)
            if (e.target === overlay) close();
        });
        document.addEventListener('keydown', onKey);
    }

    // Brancher tous les boutons data-lightbox-target sur la fonction
    document.querySelectorAll('[data-lightbox-target]').forEach(function(btn) {
        btn.addEventListener('click', function() {
            var targetId = btn.getAttribute('data-lightbox-target');
            if (targetId) openLightbox(targetId);
        });
    });

    // ----- À venir -----
    // - Lazy loading manuel des éléments lourds
    // - Widget temps réel PRIM API

})();
