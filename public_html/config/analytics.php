<?php
/**
 * Configuration du tracking et de l'analytique.
 * Desactive par defaut : aucune requete exterieure, aucun cookie.
 */
return [
    // Google Search Console
    'gsc_enabled'           => true,
    'gsc_verification_code' => 'czchIjp46RR8O0ATPO8hVN0_tQyouwydJ7CvmY_qSg0',

    // Google Analytics 4
    'ga4_enabled'           => true,
    'ga4_measurement_id'    => 'G-YXXJVF3CWN',

    // Google Tag Manager (pas utilise)
    'gtm_enabled'           => false,
    'gtm_container_id'      => '',

    // Consent Mode v2 (RGPD)
    'consent_mode_enabled'   => true,
    'consent_default_state'  => 'denied',

    // Banniere cookies
    'cookie_banner_enabled'  => true,
    'cookie_banner_mode'     => 'simple',
    'cookie_lifetime_days'   => 180,

    // Performance
    'load_async'             => true,
    'defer_scripts'          => true,
];
