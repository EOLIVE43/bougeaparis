<?php
/**
 * partials/line-search-widget.php
 *
 * Widget de recherche de ligne avec dropdown custom et badges colores.
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
            placeholder="Ex : metro 6, RER B, tramway T3..."
            autocomplete="off"
            spellcheck="false"
            role="combobox"
            aria-expanded="false"
            aria-controls="line-search-dropdown"
        >
        <div id="line-search-dropdown" class="line-search__dropdown" role="listbox" hidden></div>
    </div>

    <div id="line-search-result" class="line-search__result" hidden></div>

    <p class="line-search__hint">
        Tapez le nom de votre ligne pour connaitre son etat actuel
    </p>
</section>

<script>
(function() {
    'use strict';

    const input = document.getElementById('line-search-input');
    const dropdown = document.getElementById('line-search-dropdown');
    const resultEl = document.getElementById('line-search-result');

    if (!input || !dropdown || !resultEl) return;

    let catalog = null;
    let trafficData = null;
    let allLines = [];
    let activeIndex = -1;

    Promise.all([
        fetch('/data/lines.json').then(r => r.ok ? r.json() : null),
        fetch('/data/traffic/latest.json').then(r => r.ok ? r.json() : { lines: {} })
    ]).then(([catalogData, traffic]) => {
        catalog = catalogData;
        trafficData = traffic || { lines: {} };
        buildAllLines();
    }).catch(err => {
        console.warn('Line search widget: erreur de chargement', err);
    });

    function buildAllLines() {
        if (!catalog) return;
        const groups = [
            { mode: 'Metro',        key: 'metro',      prefix: 'Metro' },
            { mode: 'RapidTransit', key: 'rer',        prefix: 'RER' },
            { mode: 'Tramway',      key: 'tramway',    prefix: 'Tramway' },
            { mode: 'LocalTrain',   key: 'transilien', prefix: 'Transilien' }
        ];

        allLines = [];
        groups.forEach(g => {
            const items = catalog[g.key] || [];
            items.forEach(line => {
                allLines.push({
                    mode: g.mode,
                    shortName: line.short || line.label,
                    label: g.prefix + ' ' + (line.label || line.id),
                    color: line.color || '#0F6E56',
                    textColor: line.text_color || '#FFFFFF'
                });
            });
        });
    }

    function getLineTrafficKey(line) {
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
        const weights = { 'BLOQUANTE': 3, 'PERTURBEE': 2, 'INFORMATION': 1 };
        let maxWeight = 0;
        let maxSev = 'INFORMATION';
        entry.disruptions.forEach(d => {
            const w = weights[d.severity] || 0;
            if (w > maxWeight) { maxWeight = w; maxSev = d.severity; }
        });
        return { severity: maxSev, disruptions: entry.disruptions };
    }

    function filterLines(query) {
        const q = query.trim().toLowerCase();
        if (!q) return [];
        // Tri intelligent : priorise les matches en debut de label
        const exact = [];
        const startsWith = [];
        const contains = [];
        allLines.forEach(line => {
            const lbl = line.label.toLowerCase();
            if (lbl === q) exact.push(line);
            else if (lbl.startsWith(q)) startsWith.push(line);
            else if (lbl.includes(q) || line.shortName.toLowerCase().includes(q)) contains.push(line);
        });
        return [...exact, ...startsWith, ...contains].slice(0, 10);
    }

    function renderDropdown(suggestions) {
        if (suggestions.length === 0) {
            dropdown.hidden = true;
            input.setAttribute('aria-expanded', 'false');
            return;
        }

        let html = '';
        suggestions.forEach((line, i) => {
            const status = getLineStatus(line);
            const dotClass = 'line-search__dropdown-dot--' + status.severity.toLowerCase();
            html += '<div class="line-search__dropdown-item" data-index="' + i + '" role="option">';
            html += '  <span class="line-search__dropdown-badge" style="background:' + escapeAttr(line.color) + ';color:' + escapeAttr(line.textColor) + '">' + escapeHtml(line.shortName) + '</span>';
            html += '  <span class="line-search__dropdown-label">' + escapeHtml(line.label) + '</span>';
            html += '  <span class="line-search__dropdown-dot ' + dotClass + '" aria-hidden="true"></span>';
            html += '</div>';
        });
        dropdown.innerHTML = html;
        dropdown.hidden = false;
        input.setAttribute('aria-expanded', 'true');

        // Click sur un item
        dropdown.querySelectorAll('.line-search__dropdown-item').forEach((el, i) => {
            el.addEventListener('mousedown', function(e) {
                e.preventDefault(); // evite le blur de l'input
                selectLine(suggestions[i]);
            });
            el.addEventListener('mouseenter', function() {
                setActive(i);
            });
        });
    }

    function setActive(i) {
        activeIndex = i;
        const items = dropdown.querySelectorAll('.line-search__dropdown-item');
        items.forEach((el, idx) => {
            el.classList.toggle('is-active', idx === i);
        });
    }

    function selectLine(line) {
        input.value = line.label;
        dropdown.hidden = true;
        input.setAttribute('aria-expanded', 'false');
        renderResult(line);
    }

    function renderResult(line) {
        const status = getLineStatus(line);
        const statusConfig = {
            'NORMAL':      { cls: 'normal',      icon: 'OK', label: 'Trafic normal aujourd\'hui' },
            'INFORMATION': { cls: 'information', icon: 'i',  label: 'Information' },
            'PERTURBEE':   { cls: 'perturbee',   icon: '!',
