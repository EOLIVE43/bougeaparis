<?php
/**
 * partials/line-search-widget.php
 *
 * Widget de recherche de ligne avec dropdown custom et badges colores.
 *
 * Variables disponibles :
 *   $lineSearchMode (string) : 'all' | 'metro' | 'rer' | 'tramway' | 'transilien'
 *                              Defaut : 'all'
 *   $lineSearchDate (string) : date au format francais
 */
if (!isset($lineSearchMode)) $lineSearchMode = 'all';
if (!isset($lineSearchDate)) $lineSearchDate = '';
?>

<section class="line-search" aria-label="Rechercher le trafic d'une ligne" data-mode="<?= htmlspecialchars($lineSearchMode) ?>">
    <?php
    $modeLabels = [
        'all'        => 'd\'une ligne',
        'metro'      => 'd\'un métro',
        'rer'        => 'd\'une ligne RER',
        'tramway'    => 'd\'un tramway',
        'transilien' => 'd\'un Transilien',
    ];
    $modeLabel = $modeLabels[$lineSearchMode] ?? 'd\'une ligne';

    $modeRegions = [
        'all'        => 'à Paris et en Île-de-France',
        'metro'      => 'à Paris',
        'rer'        => 'en Île-de-France',
        'tramway'    => 'à Paris et en Île-de-France',
        'transilien' => 'en Île-de-France',
    ];
    $regionLabel = $modeRegions[$lineSearchMode] ?? 'à Paris et en Île-de-France';

    $modePlaceholders = [
        'all'        => 'Ex : metro 6, RER B, tramway T3...',
        'metro'      => 'Ex : metro 6, ligne 4...',
        'rer'        => 'Ex : RER A, RER B...',
        'tramway'    => 'Ex : tramway T3, T11...',
        'transilien' => 'Ex : ligne H, ligne J...',
    ];
    $modePlaceholder = $modePlaceholders[$lineSearchMode] ?? 'Ex : metro 6, RER B, tramway T3...';
    ?>
    <label for="line-search-input" class="line-search__label">
        Rechercher le trafic <?= htmlspecialchars($modeLabel) ?> <span class="line-search__region"><?= htmlspecialchars($regionLabel) ?></span><?php if (!empty($lineSearchDate)): ?> · <span class="line-search__date"><?= e($lineSearchDate) ?></span><?php endif; ?>
    </label>

    <div class="line-search__input-wrap">
        <input
            type="search"
            id="line-search-input"
            class="line-search__input"
            placeholder="<?= htmlspecialchars($modePlaceholder) ?>"
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
        Tapez le nom de votre ligne pour connaître son état actuel
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
        const sectionEl = document.querySelector('.line-search');
        const filterMode = sectionEl ? sectionEl.getAttribute('data-mode') : 'all';

        let groups = [
            { mode: 'Metro',        key: 'metro',      prefix: 'Metro' },
            { mode: 'RapidTransit', key: 'rer',        prefix: 'RER' },
            { mode: 'Tramway',      key: 'tramway',    prefix: 'Tramway' },
            { mode: 'LocalTrain',   key: 'transilien', prefix: 'Transilien' }
        ];

        // Filtrage par mode si specifie
        if (filterMode && filterMode !== 'all') {
            groups = groups.filter(g => g.key === filterMode);
        }

        allLines = [];
        groups.forEach(g => {
            const items = catalog[g.key] || [];
            items.forEach(line => {
                allLines.push({
                    mode: g.mode,
                    shortName: line.short || line.label,
                    label: g.prefix + ' ' + (line.label || line.id),
                    color: line.color || '#0F6E56',
                    textColor: line.text_color || '#FFFFFF',
                    slug: line.slug || '',
                    hasPage: line.has_page === true,
                    pathPrefix: g.key === 'metro' ? '/metro/' :
                                g.key === 'rer' ? '/rer/' :
                                g.key === 'tramway' ? '/tramway/' :
                                g.key === 'transilien' ? '/transilien/' : '/'
                });
            });
        });
    }

    function getLineTrafficKey(line) {
        // Les cles dans latest.json sont du type :
        //   metro-ligne-4, rer-ligne-a, tramway-ligne-t1, transilien-ligne-h
        const modeToPrefix = {
            'Metro': 'metro',
            'RapidTransit': 'rer',
            'Tramway': 'tramway',
            'LocalTrain': 'transilien'
        };
        const prefix = modeToPrefix[line.mode] || '';
        const shortLower = line.shortName.toLowerCase();
        return prefix + '-ligne-' + shortLower;
    }

    // Renvoie l'entry trafic en testant plusieurs formats de cles possibles
    function findTrafficEntry(line) {
        if (!trafficData || !trafficData.lines) return null;
        const lines = trafficData.lines;

        // Essai 1 : cle composee mode-ligne-shortName (format reel)
        const k1 = getLineTrafficKey(line);
        if (lines[k1]) return lines[k1];

        // Essai 2 : variantes de fallback
        const modeToPrefix = {
            'Metro': 'metro',
            'RapidTransit': 'rer',
            'Tramway': 'tramway',
            'LocalTrain': 'transilien'
        };
        const prefix = modeToPrefix[line.mode] || '';
        const shortLower = line.shortName.toLowerCase();

        // Sans 'ligne-' (compatibilite ancienne)
        if (lines[prefix + '-' + shortLower]) return lines[prefix + '-' + shortLower];

        // Recherche fuzzy : on parcourt et matche par mode+shortName
        for (const k in lines) {
            const e = lines[k];
            if (e && e.line && e.line.mode === line.mode && e.line.shortName === line.shortName) {
                return e;
            }
        }
        return null;
    }

    function getLineStatus(line) {
        if (!trafficData || !trafficData.lines) {
            return { severity: 'NORMAL', disruptions: [] };
        }
        const entry = findTrafficEntry(line);
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
        const statusLabels = {
            'NORMAL':      'Trafic normal',
            'INFORMATION': 'Information',
            'PERTURBEE':   'Perturbé',
            'BLOQUANTE':   'Interrompu'
        };
        suggestions.forEach((line, i) => {
            const status = getLineStatus(line);
            const chipClass = 'line-search__dropdown-chip--' + status.severity.toLowerCase();
            const chipLabel = statusLabels[status.severity] || 'Trafic normal';
            html += '<div class="line-search__dropdown-item" data-index="' + i + '" role="option">';
            html += '  <span class="line-search__dropdown-badge" style="background:' + escapeAttr(line.color) + ';color:' + escapeAttr(line.textColor) + '">' + escapeHtml(line.shortName) + '</span>';
            html += '  <span class="line-search__dropdown-label">' + escapeHtml(line.label) + '</span>';
            html += '  <span class="line-search__dropdown-chip ' + chipClass + '">' + escapeHtml(chipLabel) + '</span>';
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
            'PERTURBEE':   { cls: 'perturbee',   icon: '!',  label: 'Trafic perturbé' },
            'BLOQUANTE':   { cls: 'bloquante',   icon: 'X',  label: 'Trafic interrompu' }
        };
        const cfg = statusConfig[status.severity] || statusConfig['NORMAL'];

        let html = '';
        html += '<div class="line-search__card line-search__card--' + cfg.cls + '">';
        html += '  <div class="line-search__badge" style="background:' + escapeAttr(line.color) + ';color:' + escapeAttr(line.textColor) + '">' + escapeHtml(line.shortName) + '</div>';
        html += '  <div class="line-search__info">';
        html += '    <h3 class="line-search__line-name">' + escapeHtml(line.label) + '</h3>';
        html += '    <p class="line-search__status"><span class="line-search__status-dot">' + cfg.icon + '</span> ' + escapeHtml(cfg.label) + '</p>';

        if (status.disruptions.length > 0) {
            const first = status.disruptions[0];
            if (first.title) {
                html += '    <p class="line-search__detail">' + escapeHtml(first.title) + '</p>';
            }
            if (status.disruptions.length > 1) {
                html += '    <p class="line-search__more">+ ' + (status.disruptions.length - 1) + ' autre perturbation sur cette ligne</p>';
            }
        }

        // Bouton "Voir la ligne" si la page existe
        if (line.hasPage && line.slug) {
            const url = line.pathPrefix + line.slug + '/';
            html += '    <a href="' + escapeAttr(url) + '" class="line-search__cta">Voir la ' + escapeHtml(line.label) + ' →</a>';
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

    function escapeAttr(str) {
        return escapeHtml(str);
    }

    // Input : filtrage en temps reel
    input.addEventListener('input', function(e) {
        const val = e.target.value;
        const suggestions = filterLines(val);
        renderDropdown(suggestions);
        activeIndex = -1;

        if (!val) {
            resultEl.hidden = true;
            resultEl.innerHTML = '';
        }
    });

    // Focus : ne montre rien si l'input est vide
    input.addEventListener('focus', function() {
        const val = input.value;
        if (val) {
            renderDropdown(filterLines(val));
        }
    });

    // Blur : masque le dropdown
    input.addEventListener('blur', function() {
        setTimeout(function() {
            dropdown.hidden = true;
            input.setAttribute('aria-expanded', 'false');
        }, 150);
    });

    // Clavier : fleches haut/bas + Enter + Escape
    input.addEventListener('keydown', function(e) {
        if (dropdown.hidden) return;
        const items = dropdown.querySelectorAll('.line-search__dropdown-item');
        if (e.key === 'ArrowDown') {
            e.preventDefault();
            setActive(Math.min(activeIndex + 1, items.length - 1));
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            setActive(Math.max(activeIndex - 1, 0));
        } else if (e.key === 'Enter' && activeIndex >= 0) {
            e.preventDefault();
            const suggestions = filterLines(input.value);
            if (suggestions[activeIndex]) {
                selectLine(suggestions[activeIndex]);
            }
        } else if (e.key === 'Escape') {
            dropdown.hidden = true;
            input.setAttribute('aria-expanded', 'false');
        }
    });

})();
</script>
