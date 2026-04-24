<?php
/**
 * Configuration générale du site BougeaParis.fr
 *
 * Centralise toutes les informations globales : nom, slogan, contact, logo.
 * Modifier ce fichier suffit à mettre à jour ces infos partout sur le site.
 */
return [
    // Identité de la marque
    'brand_name'     => 'BougeaParis.fr',
    'brand_short'    => 'BougeaParis',
    'domain'         => 'bougeaparis.fr',
    'url'            => 'https://bougeaparis.fr',
    'slogan'         => 'Se déplacer. Visiter.',
    'description'    => 'Guide des transports parisiens : métro, RER, bus, tramway, aéroports. Horaires, itinéraires, trafic en temps réel pour Paris et l\'Île-de-France.',
    // Logo & assets
    'logo_svg'       => '/assets/img/logo/logo.svg',
    'logo_compact'   => '/assets/img/logo/logo-compact.svg',
    'favicon'        => '/assets/img/logo/favicon.svg',
    'favicon_png'    => '/assets/img/logo/favicon-512.png',
    'og_image'       => '/assets/img/logo/og-image.png',
    // Couleurs (source de vérité dans tokens.css, dupliquées ici pour usage PHP)
    'color_primary'    => '#0F6E56',
    'color_primary_fg' => '#FFFFFF',
    'color_primary_bg' => '#E1F5EE',
    'color_primary_dk' => '#085041',
    // Contact
    'contact_email'  => 'contact@bougeaparis.fr',
    // Mention légale / éditeur
    'publisher_name'      => 'BougeaParis.fr',
    'non_official_notice' => 'Site non officiel. BougeaParis.fr n\'est pas affilié à la RATP, la SNCF ou Île-de-France Mobilités.',
    // Réseaux sociaux (à remplir plus tard)
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
    'debug' => true,
];
