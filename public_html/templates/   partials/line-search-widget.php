<?php
/**
 * partials/line-search-widget.php
 *
 * Widget de recherche de ligne avec autocomplete.
 * S'appuie sur :
 *   - /data/lines.json       (catalogue statique des lignes)
 *   - /data/traffic/latest.json (etat du reseau du jour, genere chaque matin)
 *
 * Usage :
 *   include __DIR__ . '/partials/line-search-widget.php';
 */
?>

<section class="line-search" aria-label="Rechercher l'etat d'une ligne">
    <label for="line-search-input" class="line-search__label">
        Rechercher l'etat d'une ligne
    </label>

    <div class="line-search__input-wrap">
        <input
            type="search"
            id="line-search-input"
            class="line-search__input"
            list="line-search-suggestions"
            placeholder="Ex : métro 6, RER B, tramway T3..."
            autocomplete="off"
            spellcheck="false"
        >
        <datalist id="line-search-suggestions">
            <!-- Rempli dynamiquement par JS -->
        </datalist>
    </div>

    <div id="line-search-result" class="line-search__result" hidden>
        <!-- Rempli par JS au choix d'une ligne -->
    </div>

    <p class="line-search__hint">
        Tapez le nom de votre ligne pour connaître son état actuel
    </p>
</section>

<script>
(function() {
    'use strict';

    const input = document.getElementById('line-search-input');
    const datalist = document.getElementById('line-search-suggestions');
    const resultEl = document.getElementById('line-search-result');

    if (!input || !datalist || !resultEl) return;

    let catalog = null;
    let trafficData = null;
    let allLines = [];

    // Charger les deux JSON en parallele
    Promise.all([
        fetch('/data/lines.json').then(r => r.ok ? r.json() : null),
        fetch('/data/traffic/latest.json').then(r => r.ok ? r.json() : { lines: {} })
    ]).then(([catalogData, traffic]) => {
        catalog = catalogData;
        trafficData = traffic || { lines: {} };
        buildAllLines();
        fillDatalist();
    }).catch(err => {
        console.warn('Line search widget: erreur de chargement', err);
    });

    // Construire la liste unifiee (metro + RER + tram + transilien)
    function buildAllLines() {
        if (!catalog) return;
        const groups = [
            { mode: 'Metro',        key: 'metro',      prefix: 'Métro',     slugBase: 'metro' },
            { mode: 'RapidTransit', key: 'rer',        prefix: 'RER',       slugBase: 'rer' },
            { mode: 'Tramway',      key: 'tramway',    prefix: 'Tramway',   slugBase: 'tramway' },
            { mode: 'LocalTrain',   key: 'transilien', prefix: 'Transilien', slugBase: 'transilien' }
        ];

        allLines = [];
        groups.forEach(g => {
            const items = catalog[g.key] || [];
            items.forEach(line => {
                allLines.push({
                    mode: g.mode,
                    shortName: line.short || line.label,
                    label: g.prefix + ' ' + (line.label || line.id),
                    slug: g.slugBase + '/' + (line.slug || ''),
                    color: line.color || '#0F6E56',
                    textColor: line.text_color || '#FFFFFF'
                });
            });
        });
    }

    // Alimenter le datalist avec tous les labels
    function fillDatalist() {
        datalist.innerHTML = '';
        allLines.forEach(line => {
            const opt = document.createElement('option');
            opt.value = line.label;
            datalist.appendChild(opt);
        });
    }

    // Recherche d'une ligne dans la liste par label (casse ignoree)
    function findLine(query) {
        const q = query.trim().toLowerCase();
        if (!q) return null;
        return allLines.find(l => l.label.toLowerCase() === q) ||
               allLines.find(l => l.label.toLowerCase().startsWith(q)) ||
               null;
    }

    // Trouver les perturbations d'une ligne dans trafficData
    function getLineTrafficKey(line) {
        // Les cles dans trafficData.lines sont : metro-1, rer-a, tramway-t1, transilien-h, etc.
        const modeToPrefix = {
            'Metro': 'metro',
            'RapidTransit': 'rer',
            'Tramway': 'tramway',
            'LocalTrain': 'transilien'
        };
        const prefix = modeToPrefix[line.mode] || '';
        return prefix + '-' + line.shortName.toLowerCase();
    }

    function getLineStatus(line) {
        if (!trafficData || !trafficData.lines) {
            return { severity: 'NORMAL', disruptions: [] };
        }
        const key = getLineTrafficKey(line);
        const entry = trafficData.lines[key];
        if (!entry || !entry.disruptions || entry.disruptions.length === 0) {
            return { severity: 'NORMAL', disruptions: [] };
        }

        // Priorite : BLOQUANTE > PERTURBEE > INFORMATION
        const weights = { 'BLOQUANTE': 3, 'PERTURBEE': 2, 'INFORMATION': 1 };
        let maxWeight = 0;
        let maxSev = 'INFORMATION';
        entry.disruptions.forEach(d => {
            const w = weights[d.severity] || 0;
            if (w > maxWeight) {
                maxWeight = w;
                maxSev = d.severity;
            }
        });

        return { severity: maxSev, disruptions: entry.disruptions };
    }

    // Afficher le resultat
    function renderResult(line) {
        const status = getLineStatus(line);
        const statusConfig = {
            'NORMAL':      { cls: 'normal',      icon: '✓', label: 'Trafic normal aujourd\'hui' },
            'INFORMATION': { cls: 'information', icon: 'i', label: 'Information' },
            'PERTURBEE':   { cls: 'perturbee',   icon: '!', label: 'Trafic perturbé' },
            'BLOQUANTE':   { cls: 'bloquante',   icon: '✕', label: 'Trafic interrompu' }
        };
        const cfg = statusConfig[status.severity] || statusConfig['NORMAL'];

        let html = '';
        html += '<div class="line-search__card line-search__card--' + cfg.cls + '">';

        // Badge de la ligne
        html += '  <div class="line-search__badge" style="background:' + escapeHtml(line.color) + ';color:' + escapeHtml(line.textColor) + '">';
        html += '    ' + escapeHtml(line.shortName);
        html += '  </div>';

        // Infos
        html += '  <div class="line-search__info">';
        html += '    <h3 class="line-search__line-name">' + escapeHtml(line.label) + '</h3>';
        html += '    <p class="line-search__status"><span class="line-search__status-dot">' + cfg.icon + '</span> ' + escapeHtml(cfg.label) + '</p>';

        // Messages de perturbation
        if (status.disruptions.length > 0) {
            const firstDisruption = status.disruptions[0];
            if (firstDisruption.title)
