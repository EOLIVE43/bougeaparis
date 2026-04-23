<?php
/**
 * Composant icon-menu : rendu d'un picto transport dans un badge teal carre.
 *
 * Props :
 *   - icon : slug du picto ('metro', 'rer', 'bus', 'tram', 'plane', 'train', 'blog')
 *   - size : 'sm' (26px), 'md' (32px, defaut), 'lg' (40px), 'xl' (48px)
 *   - class : classe CSS additionnelle optionnelle
 *
 * Rend :
 *   <span class="bp-icon bp-icon--md"><svg>...</svg></span>
 */

$icon = $props['icon'] ?? 'metro';
$size = $props['size'] ?? 'md';
$extra_class = $props['class'] ?? '';

$svg_map = [

    'metro' => '<svg width="100%" height="100%" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M6 3h12a2 2 0 0 1 2 2v11a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V5a2 2 0 0 1 2-2z" fill="currentColor"/>
        <rect x="6.5" y="6" width="4" height="4" rx="1" fill="white"/>
        <rect x="13.5" y="6" width="4" height="4" rx="1" fill="white"/>
        <circle cx="8" cy="15.5" r="1" fill="white"/>
        <circle cx="16" cy="15.5" r="1" fill="white"/>
        <path d="M7 19l-1.5 2M17 19l1.5 2" stroke="white" stroke-width="1.5" stroke-linecap="round"/>
    </svg>',

    'rer' => '<svg width="100%" height="100%" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M5 4h14a2 2 0 0 1 2 2v9a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3V6a2 2 0 0 1 2-2z" fill="currentColor"/>
        <rect x="5" y="7" width="14" height="4" rx="0.5" fill="white"/>
        <circle cx="7" cy="14.5" r="1" fill="white"/>
        <circle cx="17" cy="14.5" r="1" fill="white"/>
        <path d="M6 18l-1.5 2M18 18l1.5 2" stroke="white" stroke-width="1.5" stroke-linecap="round"/>
    </svg>',

    'bus' => '<svg width="100%" height="100%" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M5 5h14a1.5 1.5 0 0 1 1.5 1.5V16a2 2 0 0 1-2 2H5.5a2 2 0 0 1-2-2V6.5A1.5 1.5 0 0 1 5 5z" fill="currentColor"/>
        <rect x="5" y="7.5" width="4" height="4" rx="0.5" fill="white"/>
        <rect x="10" y="7.5" width="4" height="4" rx="0.5" fill="white"/>
        <rect x="15" y="7.5" width="4" height="4" rx="0.5" fill="white"/>
        <circle cx="7.5" cy="17.5" r="1.5" fill="white"/>
        <circle cx="16.5" cy="17.5" r="1.5" fill="white"/>
        <circle cx="7.5" cy="17.5" r="0.6" fill="currentColor"/>
        <circle cx="16.5" cy="17.5" r="0.6" fill="currentColor"/>
    </svg>',

    'tram' => '<svg width="100%" height="100%" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M12 2v3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        <path d="M6 5h12a1.5 1.5 0 0 1 1.5 1.5v10a2 2 0 0 1-2 2H6.5a2 2 0 0 1-2-2v-10A1.5 1.5 0 0 1 6 5z" fill="currentColor"/>
        <rect x="6" y="7.5" width="5" height="4" rx="0.5" fill="white"/>
        <rect x="13" y="7.5" width="5" height="4" rx="0.5" fill="white"/>
        <circle cx="8" cy="15.5" r="1" fill="white"/>
        <circle cx="16" cy="15.5" r="1" fill="white"/>
        <path d="M7 19l-1.5 2M17 19l1.5 2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
    </svg>',

    'plane' => '<svg width="100%" height="100%" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M21 15.5l-1 2-7-1.5v4l1.5 1.5L12 22l-2.5-1.5v-3L8 18l-5-2 1-2 4 0.5V10L5 7l1-1.5 4.5 2.5L12 4a1.5 1.5 0 0 1 3 0l1.5 4 4.5-2.5L22 7l-3.5 3v4.5L21 15.5z" fill="currentColor"/>
    </svg>',

    'train' => '<svg width="100%" height="100%" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M5 4h14a1.5 1.5 0 0 1 1.5 1.5V15a3 3 0 0 1-3 3H6.5a3 3 0 0 1-3-3V5.5A1.5 1.5 0 0 1 5 4z" fill="currentColor"/>
        <rect x="5" y="6.5" width="6" height="5" rx="0.5" fill="white"/>
        <rect x="13" y="6.5" width="6" height="5" rx="0.5" fill="white"/>
        <rect x="7" y="13" width="10" height="1.5" rx="0.3" fill="white"/>
        <circle cx="7.5" cy="16.5" r="1" fill="white"/>
        <circle cx="16.5" cy="16.5" r="1" fill="white"/>
        <path d="M6 19l-1.5 2M18 19l1.5 2" stroke="white" stroke-width="1.5" stroke-linecap="round"/>
    </svg>',

    'blog' => '<svg width="100%" height="100%" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M5 3h10l4 4v12a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z" fill="currentColor"/>
        <path d="M15 3v4h4" fill="white"/>
        <path d="M7 11h10M7 14h10M7 17h6" stroke="white" stroke-width="1.5" stroke-linecap="round"/>
    </svg>',
];

$svg = $svg_map[$icon] ?? $svg_map['metro'];
?>
<span class="bp-icon bp-icon--<?= htmlspecialchars($size) ?><?= $extra_class ? ' ' . htmlspecialchars($extra_class) : '' ?>" aria-hidden="true"><?= $svg ?></span>
