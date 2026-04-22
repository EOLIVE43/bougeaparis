<?php
/**
 * Configuration SEO globale
 *
 * Valeurs par defaut pour les balises meta.
 * Chaque page peut surcharger ces valeurs via le contexte template.
 */

return [
    // Defaults
    'default_title'       => 'BougeaParis.fr - Guide des transports parisiens',
    'default_description' => 'Guide complet des transports en commun a Paris et en Ile-de-France. Metro, RER, bus, tramway, aeroports : horaires, itineraires et trafic en temps reel.',
    'default_keywords'    => 'transports paris, metro paris, rer paris, bus paris, tramway paris, itineraire paris, horaires metro',

    // Template du title : %s = titre specifique de la page
    'title_suffix'        => ' - BougeaParis.fr',

    // Max image preview (CRITIQUE pour Google Discover)
    'robots'              => 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1',

    // Open Graph
    'og_type'             => 'website',
    'og_site_name'        => 'BougeaParis.fr',
    'og_locale'           => 'fr_FR',

    // Twitter Card
    'twitter_card'        => 'summary_large_image',
    'twitter_site'        => '', // a remplir quand compte cree

    // Organisation (schema.org)
    'organization' => [
        'name'        => 'BougeaParis.fr',
        'url'         => 'https://bougeaparis.fr',
        'logo'        => 'https://bougeaparis.fr/assets/img/logo/logo-512.png',
        'description' => 'Guide independant des transports en commun parisiens et franciliens.',
        'email'       => 'contact@bougeaparis.fr',
        'sameAs'      => [
            // URLs reseaux sociaux a ajouter plus tard
        ],
    ],

    // Site internet (schema.org WebSite + SearchAction)
    'website' => [
        'name'         => 'BougeaParis.fr',
        'alternateName' => 'Bouge a Paris',
        'url'          => 'https://bougeaparis.fr',
        'searchUrl'    => 'https://bougeaparis.fr/recherche/?q={search_term_string}',
    ],
];
