<?php
/**
 * Composant icon-menu V2 : pictos transport en style Lucide (trait minimaliste).
 *
 * Props :
 *   - icon : slug ('metro', 'rer', 'bus', 'tram', 'plane', 'train', 'blog')
 *   - size : 'sm' (26px), 'md' (32px, defaut), 'lg' (40px), 'xl' (48px)
 *   - class : classe CSS additionnelle optionnelle
 *
 * Rend : <span class="bp-icon bp-icon--md"><svg>...</svg></span>
 */

$icon        = $props['icon']  ?? 'metro';
$size        = $props['size']  ?? 'md';
$extra_class = $props['class'] ?? '';

$svg_map = [

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
];

$svg = $svg_map[$icon] ?? $svg_map['metro'];
?>
<span class="bp-icon bp-icon--<?= htmlspecialchars($size) ?><?= $extra_class ? ' ' . htmlspecialchars($extra_class) : '' ?>" aria-hidden="true"><?= $svg ?></span>
