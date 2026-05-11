<?php
/**
 * Composant icon-menu : pictos SVG inline (style Lucide).
 *
 * Props :
 *   - icon  : slug ('metro', 'rer', 'bus', 'tram', 'plane', 'train', 'blog',
 *             'train-front', 'landmark', 'map', 'activity', 'euro',
 *             'building-2', 'compass', 'leaf', 'church', 'archway', 'coffee')
 *   - size  : 'sm' (26px), 'md' (32px, defaut), 'lg' (40px), 'xl' (48px)
 *   - style : 'block' (defaut, container vert fond plein) | 'outline'
 *             (trait simple sans container, couleur primaire — pour les
 *             sous-items du mega-menu Visiter)
 *   - class : classe CSS additionnelle optionnelle
 *
 * Rend : <span class="bp-icon bp-icon--md [bp-icon--outline]"><svg>...</svg></span>
 */

$icon        = $props['icon']  ?? 'metro';
$size        = $props['size']  ?? 'md';
$style       = $props['style'] ?? 'block'; // 'block' | 'outline'
$extra_class = $props['class'] ?? '';

$svg_map = [

    // ====================================================================
    // PICTOS CUSTOM TRANSPORT (existants, dessines specifiquement)
    // ====================================================================

    // Metro : wagon vu de face avec pare-brise haut + trait vertical + roues
    'metro' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <rect x="4" y="3" width="16" height="13" rx="2"/>
        <line x1="4" y1="9" x2="20" y2="9"/>
        <line x1="12" y1="3" x2="12" y2="9"/>
        <circle cx="8" cy="13" r="0.7" fill="currentColor" stroke="none"/>
        <circle cx="16" cy="13" r="0.7" fill="currentColor" stroke="none"/>
        <line x1="6" y1="18" x2="8" y2="21"/>
        <line x1="18" y1="18" x2="16" y2="21"/>
    </svg>',

    // RER : train horizontal avec ligne centrale + grosses roues rondes
    'rer' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <rect x="2" y="8" width="20" height="8" rx="1"/>
        <line x1="2" y1="12" x2="22" y2="12"/>
        <circle cx="6" cy="18" r="1.5" fill="currentColor" stroke="none"/>
        <circle cx="18" cy="18" r="1.5" fill="currentColor" stroke="none"/>
        <line x1="9" y1="18" x2="15" y2="18"/>
    </svg>',

    // Bus : carrosserie de profil avec 2 fenetres pleines + roues
    'bus' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M3 7a2 2 0 0 1 2-2h13a3 3 0 0 1 3 3v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7z"/>
        <line x1="3" y1="12" x2="21" y2="12"/>
        <rect x="5" y="7" width="4" height="4" fill="currentColor" stroke="none"/>
        <rect x="11" y="7" width="4" height="4" fill="currentColor" stroke="none"/>
        <circle cx="7" cy="18" r="1.5" fill="currentColor" stroke="none"/>
        <circle cx="17" cy="18" r="1.5" fill="currentColor" stroke="none"/>
    </svg>',

    // Tramway : carre vertical avec catenaire (ligne electrique au-dessus)
    'tram' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <line x1="4" y1="2" x2="20" y2="2"/>
        <line x1="12" y1="2" x2="12" y2="5"/>
        <rect x="5" y="5" width="14" height="14" rx="2"/>
        <line x1="5" y1="11" x2="19" y2="11"/>
        <rect x="7" y="7" width="3" height="3" fill="currentColor" stroke="none"/>
        <rect x="14" y="7" width="3" height="3" fill="currentColor" stroke="none"/>
        <line x1="5" y1="21" x2="7" y2="19"/>
        <line x1="19" y1="21" x2="17" y2="19"/>
    </svg>',

    // Aeroports : avion classique en croix (vue de dessus)
    'plane' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M21.5 10.5L14 9V4a2 2 0 0 0-4 0v5L2.5 10.5a1 1 0 0 0-.5 1.5l1.5 1.5 6.5-1v4l-2 1.5v2l4-1 4 1v-2l-2-1.5v-4l6.5 1 1.5-1.5a1 1 0 0 0-.5-1.5z"/>
    </svg>',

    // Transilien : train de banlieue allonge avec 2 fenetres + rail
    'train' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <rect x="3" y="4" width="18" height="12" rx="1"/>
        <line x1="3" y1="10" x2="21" y2="10"/>
        <rect x="5" y="6" width="5" height="3" fill="currentColor" stroke="none"/>
        <rect x="14" y="6" width="5" height="3" fill="currentColor" stroke="none"/>
        <circle cx="7" cy="18" r="1.5" fill="currentColor" stroke="none"/>
        <circle cx="17" cy="18" r="1.5" fill="currentColor" stroke="none"/>
        <path d="M1 16h22"/>
    </svg>',

    // Blog : feuille avec coin plie + lignes de texte
    'blog' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/>
        <polyline points="14 3 14 9 20 9"/>
        <line x1="8" y1="13" x2="16" y2="13"/>
        <line x1="8" y1="17" x2="13" y2="17"/>
    </svg>',

    // ====================================================================
    // PICTOS LUCIDE OFFICIELS (https://lucide.dev/icons)
    // Pour mega-menu niveau 1 + sous-menu Visiter (refonte nav).
    // ====================================================================

    // Se deplacer (mega-menu niveau 1)
    'train-front' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M8 3.1V7a4 4 0 0 0 8 0V3.1"/><path d="m9 15-1-1"/><path d="m15 15 1-1"/><path d="M9 19c-2.8 0-5-2.2-5-5v-4a8 8 0 0 1 16 0v4c0 2.8-2.2 5-5 5Z"/><path d="m8 19-2 3"/><path d="m16 19 2 3"/></svg>',

    // Visiter (mega-menu niveau 1) + Monuments emblematiques (sous-menu)
    'landmark' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M10 18v-7"/><path d="M11.119 2.205a2 2 0 0 1 1.762 0l7.84 3.846A.5.5 0 0 1 20.5 7h-17a.5.5 0 0 1-.22-.949z"/><path d="M14 18v-7"/><path d="M18 18v-7"/><path d="M3 22h18"/><path d="M6 18v-7"/></svg>',

    // Itineraires (mega-menu niveau 1)
    'map' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M14.106 5.553a2 2 0 0 0 1.788 0l3.659-1.83A1 1 0 0 1 21 4.619v12.764a1 1 0 0 1-.553.894l-4.553 2.277a2 2 0 0 1-1.788 0l-4.212-2.106a2 2 0 0 0-1.788 0l-3.659 1.83A1 1 0 0 1 3 19.381V6.618a1 1 0 0 1 .553-.894l4.553-2.277a2 2 0 0 1 1.788 0z"/><path d="M15 5.764v15"/><path d="M9 3.236v15"/></svg>',

    // Trafic temps reel (mega-menu niveau 1)
    'activity' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M22 12h-2.48a2 2 0 0 0-1.93 1.46l-2.35 8.36a.5.5 0 0 1-.96 0L9.24 2.18a.5.5 0 0 0-.96 0l-2.35 8.36A2 2 0 0 1 4 12H2"/></svg>',

    // Tarifs (mega-menu niveau 1)
    'euro' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M4 10h12"/><path d="M4 14h9"/><path d="M19 6a7.7 7.7 0 0 0-5.2-2A7.9 7.9 0 0 0 6 12c0 4.4 3.5 8 7.8 8 2 0 3.8-.8 5.2-2"/></svg>',

    // Musees & arts (sous-menu Visiter)
    'building-2' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4"/><path d="M10 10h4"/><path d="M10 14h4"/><path d="M10 18h4"/></svg>',

    // Places & avenues iconiques (sous-menu Visiter)
    'compass' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z"/><circle cx="12" cy="12" r="10"/></svg>',

    // Jardins & espaces verts (sous-menu Visiter)
    'leaf' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19.2 2.96a1 1 0 0 1 1.8.5c0 4.36-1.39 8.83-4.6 12.05-2.5 2.5-6 3.5-5.4 4.49"/><path d="M2 21c0-3 1.85-5.36 5.08-6"/></svg>',

    // Patrimoine religieux (sous-menu Visiter)
    'church' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M10 9h4"/><path d="M12 7v5"/><path d="M14 22v-4a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v4"/><path d="M18 22V5.618a1 1 0 0 0-.553-.894l-4.553-2.277a2 2 0 0 0-1.788 0L6.553 4.724A1 1 0 0 0 6 5.618V22"/><path d="m18 7 3.447 1.724a1 1 0 0 1 .553.894V20a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V9.618a1 1 0 0 1 .553-.894L6 7"/></svg>',

    // Ponts & rives de Seine (sous-menu Visiter)
    // NOTE : "archway" n\'existe pas dans Lucide (404). Substitut "ship"
    // qui evoque les bateaux-mouches sur la Seine (cluster maritime urbain
    // le plus identifiable parmi les icones Lucide disponibles).
    'archway' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M12 10.189V14"/><path d="M12 2v3"/><path d="M19 13V7a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2v6"/><path d="M19.38 20A11.6 11.6 0 0 0 21 14l-8.188-3.639a2 2 0 0 0-1.624 0L3 14a11.6 11.6 0 0 0 2.81 7.76"/><path d="M2 21c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1s1.2 1 2.5 1c2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/></svg>',

    // Vie parisienne (sous-menu Visiter)
    'coffee' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M10 2v2"/><path d="M14 2v2"/><path d="M16 8a1 1 0 0 1 1 1v8a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V9a1 1 0 0 1 1-1h14a4 4 0 1 1 0 8h-1"/><path d="M6 2v2"/></svg>',
];

$svg = $svg_map[$icon] ?? $svg_map['metro'];
$classes = 'bp-icon bp-icon--' . htmlspecialchars($size);
if ($style === 'outline') {
    $classes .= ' bp-icon--outline';
}
if ($extra_class !== '') {
    $classes .= ' ' . htmlspecialchars($extra_class);
}
?>
<span class="<?= $classes ?>" aria-hidden="true"><?= $svg ?></span>
