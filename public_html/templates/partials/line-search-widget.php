<?php
/**
 * partials/line-search-widget.php
 *
 * Widget de recherche de ligne avec autocomplete.
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
            placeholder="Ex : metro 6, RER B, tramway T3..."
            autocomplete="off"
            spellcheck="false"
        >
        <datalist id="line-search-suggestions"></datalist>
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
    const datalist = document.getElementById('line-search-suggestions');
    const resultEl = document.getElementById('line-search-result');

    if (!input || !datalist || !resultEl) return;

    let catalog = null;
    let trafficData = null;
    let allLines = [];

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

    function fillDatalist() {
        datalist.innerHTML = '';
        allLines.forEach(line => {
            const opt = document.createElement('option');
            opt.value = line.label;
            datalist.appendChild(opt);
        });
    }

    function findLine(query) {
        const q = query.trim().toLowerCase();
        if (!q) return null;
        return allLines.find(l => l.label.toLowerCase() === q) ||
               allLines.find(l => l.label.toLowerCase().startsWith(q)) ||
               null;
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
            if (w > maxWeight) {
                maxWeight = w;
                maxSev = d.severity;
            }
        });

        return { severity: maxSev, disruptions: entry.disruptions };
    }

    function renderResult(line) {
        const status = getLineStatus(line);
        const statusConfig = {
            'NORMAL':      { cls: 'normal',      icon: 'OK', label: 'Trafic normal aujourd\'hui' },
            'INFORMATION': { cls: 'information', icon: 'i',  label: 'Information' },
            'PERTURBEE':   { cls: 'perturbee',   icon: '!',  label: 'Trafic perturbe' },
            'BLOQUANTE':   { cls: 'bloquante',   icon: 'X',  label: 'Trafic interrompu' }
        };
        const cfg = statusConfig[status.severity] || statusConfig['NORMAL'];

        let html = '';
        html += '<div class="line-search__card line-search__card--' + cfg.cls + '">';
        html += '  <div class="line-search__badge" style="background:' + escapeHtml(line.color) + ';color:' + escapeHtml(line.textColor) + '">';
        html += '    ' + escapeHtml(line.shortName);
        html += '  </div>';
        html += '  <div class="line-search__info">';
        html += '    <h3 class="line-search__line-name">' + escapeHtml(line.label) + '</h3>';
        html += '    <p class="line-search__status"><span class="line-search__status-dot">' + cfg.icon + '</span> ' + escapeHtml(cfg.label) + '</p>';

        if (status.disruptions.length > 0) {
            const firstDisruption = status.disruptions[0];
            if (firstDisruption.title) {
                html += '    <p class="line-search__detail">' + escapeHtml(firstDisruption.title) + '</p>';
            }
            if (status.disruptions.length > 1) {
                html += '    <p class="line-search__more">+ ' + (status.disruptions.length - 1) + ' autre perturbation sur cette ligne</p>';
            }
        }

        html += '  </div>';
        html += '</div>';

        resultEl.innerHTML = html;
        resultEl.hidden = false;
    }

    function escapeHtml(str) {
        if (str === null || str === undefined) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    input.addEventListener('input', function(e) {
        const val = e.target.value;
        if (!val) {
            resultEl.hidden = true;
            resultEl.innerHTML = '';
            return;
        }
        const line = findLine(val);
        if (line) {
            renderResult(line);
        } else {
            resultEl.hidden = true;
        }
    });

    input.addEventListener('change', function(e) {
        const line = findLine(e.target.value);
        if (line) renderResult(line);
    });

})();
</script>
