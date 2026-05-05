/**
 * carte-station.js
 *
 * Lazy-loader pour la carte interactive Leaflet sur les pages station.
 * Leaflet (CSS + JS) n'est telecharge QUE quand l'utilisateur clique sur le
 * bouton "Afficher le plan interactif". Aucun cout sur les Core Web Vitals
 * tant que la carte n'est pas demandee.
 *
 * Tuiles : OpenStreetMap (gratuit, attribution legale obligatoire incluse).
 *
 * Markers :
 *   - station central : pastille primary "M"
 *   - sorties         : pastille verte avec numero
 *   - POIs            : pastille blanche avec emoji categorie
 *
 * Source du composant : templates/components/station/carte.php
 *
 * @since Livraison 9
 */

(function () {
    'use strict';

    var LEAFLET_CSS = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css';
    var LEAFLET_JS  = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';
    var TILE_URL    = 'https://tile.openstreetmap.org/{z}/{x}/{y}.png';
    var TILE_ATTR   = '&copy; <a href="https://openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors';

    /** Promise singleton pour le chargement Leaflet. */
    var leafletPromise = null;
    function loadLeaflet() {
        if (typeof window.L !== 'undefined') return Promise.resolve();
        if (leafletPromise) return leafletPromise;

        leafletPromise = new Promise(function (resolve, reject) {
            // CSS d'abord (parallel avec le JS, mais on le declare en 1er)
            if (!document.querySelector('link[data-leaflet-css]')) {
                var css = document.createElement('link');
                css.rel = 'stylesheet';
                css.href = LEAFLET_CSS;
                css.crossOrigin = 'anonymous';
                css.setAttribute('data-leaflet-css', '1');
                document.head.appendChild(css);
            }
            // JS
            var script = document.createElement('script');
            script.src = LEAFLET_JS;
            script.crossOrigin = 'anonymous';
            script.async = true;
            script.onload = function () { resolve(); };
            script.onerror = function () { reject(new Error('Leaflet load failed')); };
            document.head.appendChild(script);
        });
        return leafletPromise;
    }

    /** Mapping categorie -> emoji pour les POIs. */
    var POI_EMOJI = {
        'cathédrale': '⛪', 'basilique': '⛪', 'église': '⛪', 'chapelle': '⛪',
        'mosquée': '🕌', 'synagogue': '🕍',
        'musée': '🏛️', 'théâtre': '🎭', 'opéra': '🎭',
        'pont': '🌉', 'tour': '🗼', 'place': '⛲',
        'mairie': '🏛️', 'palais': '🏰', 'château': '🏰',
        'commerce': '🛍️', 'librairie': '📚', 'café': '☕',
        'hôpital': '🏥', 'gare': '🚆',
        'île': '🏞️', 'jardin': '🌳', 'fontaine': '⛲',
        'monument': '🏛️', 'statue': '🗿', 'quartier': '🏘️'
    };
    function emojiFor(category) {
        return POI_EMOJI[category] || '📍';
    }

    /** Echappe une string pour insertion dans du HTML. */
    function escapeHtml(s) {
        var div = document.createElement('div');
        div.textContent = (s == null) ? '' : String(s);
        return div.innerHTML;
    }

    /** Construit l'icone divIcon Leaflet pour la station. */
    function stationIcon(L) {
        return L.divIcon({
            className: 'marker-station',
            html: '<div class="marker-station__inner" aria-hidden="true">M</div>',
            iconSize: [34, 34],
            iconAnchor: [17, 17],
            popupAnchor: [0, -18]
        });
    }
    function exitIcon(L, number) {
        return L.divIcon({
            className: 'marker-exit',
            html: '<div class="marker-exit__inner">' + escapeHtml(number || '·') + '</div>',
            iconSize: [28, 28],
            iconAnchor: [14, 14],
            popupAnchor: [0, -14]
        });
    }
    function poiIcon(L, category) {
        return L.divIcon({
            className: 'marker-poi',
            html: '<div class="marker-poi__inner">' + escapeHtml(emojiFor(category)) + '</div>',
            iconSize: [30, 30],
            iconAnchor: [15, 15],
            popupAnchor: [0, -15]
        });
    }

    /** Initialise la carte une fois Leaflet charge. */
    function initMap(trigger) {
        var L = window.L;
        var lat = parseFloat(trigger.dataset.stationLat);
        var lon = parseFloat(trigger.dataset.stationLon);
        var stationName = trigger.dataset.stationName || 'Station';
        var exits = [], pois = [];
        try { exits = JSON.parse(trigger.dataset.exits || '[]'); } catch (e) { exits = []; }
        try { pois  = JSON.parse(trigger.dataset.pois  || '[]'); } catch (e) { pois  = []; }

        if (!isFinite(lat) || !isFinite(lon)) {
            trigger.textContent = '⚠️ Coordonnées station invalides';
            return;
        }

        var container = document.getElementById('carte-container');
        if (!container) return;

        // Prepare le wrapper map
        container.hidden = false;
        container.innerHTML = '';
        var mapDiv = document.createElement('div');
        mapDiv.className = 'carte-leaflet';
        container.appendChild(mapDiv);

        var map = L.map(mapDiv, { scrollWheelZoom: false }).setView([lat, lon], 17);
        L.tileLayer(TILE_URL, {
            maxZoom: 19,
            attribution: TILE_ATTR
        }).addTo(map);

        var bounds = [[lat, lon]];

        // Marqueur station central
        L.marker([lat, lon], { icon: stationIcon(L), title: stationName, zIndexOffset: 1000 })
            .addTo(map)
            .bindPopup('<div class="marker-popup"><strong>Station ' + escapeHtml(stationName) + '</strong></div>');

        // Marqueurs sorties
        exits.forEach(function (e) {
            if (!isFinite(e.lat) || !isFinite(e.lon)) return;
            var addrLine = e.address ? '<small class="marker-popup__addr">' + escapeHtml(e.address) + '</small>' : '';
            var html = ''
                + '<div class="marker-popup">'
                +   '<strong>Sortie ' + escapeHtml(e.number) + '</strong>'
                +   '<span class="marker-popup__name">' + escapeHtml(e.name || '') + '</span>'
                +   addrLine
                + '</div>';
            L.marker([e.lat, e.lon], { icon: exitIcon(L, e.number) })
                .addTo(map).bindPopup(html);
            bounds.push([e.lat, e.lon]);
        });

        // Marqueurs POIs
        pois.forEach(function (p) {
            if (!isFinite(p.lat) || !isFinite(p.lon)) return;
            var ne = p.nearest_exit;
            var exitInfo = '';
            if (ne && ne.number) {
                exitInfo = '<small class="marker-popup__exit">→ Sortie '
                    + escapeHtml(ne.number) + ' · '
                    + escapeHtml(ne.walk_minutes || '?') + ' min à pied</small>';
            }
            var catLine = p.category
                ? '<span class="marker-popup__cat">' + escapeHtml(p.category) + '</span>'
                : '';
            var html = ''
                + '<div class="marker-popup">'
                +   '<strong>' + escapeHtml(p.name) + '</strong>'
                +   catLine
                +   exitInfo
                + '</div>';
            L.marker([p.lat, p.lon], { icon: poiIcon(L, p.category) })
                .addTo(map).bindPopup(html);
            bounds.push([p.lat, p.lon]);
        });

        // Zoom auto pour englober tous les marqueurs
        if (bounds.length > 1) {
            map.fitBounds(bounds, { padding: [40, 40] });
        }

        // Maj du bouton
        trigger.dataset.loaded = 'true';
        trigger.setAttribute('aria-expanded', 'true');
        trigger.innerHTML = '<span aria-hidden="true">🗺️</span> Plan affiché ci-dessous';
    }

    document.addEventListener('DOMContentLoaded', function () {
        var trigger = document.querySelector('.carte-trigger');
        if (!trigger) return;

        trigger.addEventListener('click', function () {
            if (trigger.dataset.loaded === 'true') return;
            trigger.disabled = true;
            var originalHtml = trigger.innerHTML;
            trigger.innerHTML = '<span aria-hidden="true">⏳</span> Chargement…';
            loadLeaflet().then(function () {
                initMap(trigger);
                trigger.disabled = false;
            }).catch(function (err) {
                console.error('[carte-station]', err);
                trigger.innerHTML = '<span aria-hidden="true">⚠️</span> Plan indisponible (réessayez)';
                trigger.disabled = false;
                // Reset loaded pour permettre retry
                trigger.dataset.loaded = 'false';
                leafletPromise = null;
            });
        });
    });
})();
