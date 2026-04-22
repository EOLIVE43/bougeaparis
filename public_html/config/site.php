<?php
/**
 * Configuration generale du site BougeaParis.fr
 *
 * Centralise toutes les informations globales : nom, slogan, contact, logo.
 * Modifier ce fichier suffit a mettre a jour ces infos partout sur le site.
 */

return [
    // Identite de la marque
    'brand_name'     => 'BougeaParis.fr',
    'brand_short'    => 'BougeaParis',
    'domain'         => 'bougeaparis.fr',
    'url'            => 'https://bougeaparis.fr',
    'slogan'         => 'Se deplacer. Visiter.',
    'description'    => 'Guide des transports parisiens : metro, RER, bus, tramway, aeroports. Horaires, itineraires, trafic en temps reel pour Paris et l\'Ile-de-France.',

    // Logo & assets
    'logo_svg'       => '/assets/img/logo/logo.svg',
    'logo_compact'   => '/assets/img/logo/logo-compact.svg',
    'favicon'        => '/assets/img/logo/favicon.svg',
    'favicon_png'    => '/assets/img/logo/favicon-512.png',
    'og_image'       => '/assets/img/logo/og-image.png',

    // Couleurs (source de verite dans tokens.css, dupliquees ici pour usage PHP)
    'color_primary'    => '#0F6E56',
    'color_primary_fg' => '#FFFFFF',
    'color_primary_bg' => '#E1F5EE',
    'color_primary_dk' => '#085041',

    // Contact
    'contact_email'  => 'contact@bougeaparis.fr',

    // Mention legale / editeur
    'publisher_name'      => 'BougeaParis.fr',
    'non_official_notice' => 'Site non officiel. BougeaParis.fr n\'est pas affilie a la RATP, la SNCF ou Ile-de-France Mobilites.',

    // Reseaux sociaux (a remplir plus tard)
    'social' => [
        'twitter'   => '',
        'facebook'  => '',
        'instagram' => '',
        'linkedin'  => '',
    ],

    // Langue & timezone
    'locale'   => 'fr_FR',
    'language' => 'fr',
    'timezone' => 'Europe/Paris',

    // Environnement
    'debug' => false,
];
