<?php
/**
 * Configuration AdSense
 *
 * Emplacements publicitaires pre-cables dans les templates.
 * Pour activer AdSense le jour J :
 *   1. Passer 'enabled' a true
 *   2. Remplir 'publisher_id' avec votre ID AdSense (ca-pub-xxx)
 *   3. Remplir chaque 'slot_id' avec les ID de vos emplacements AdSense
 *   Les pubs apparaitront automatiquement sur toutes les pages concernees.
 */

return [
    // Interrupteur principal
    'enabled'      => false,

    // Identifiant AdSense (ca-pub-xxxxxxxxxxxxxxxx)
    'publisher_id' => '',

    // Auto ads (laisser Google choisir les emplacements automatiquement)
    // Si active, les slots manuels ci-dessous sont ignores
    'auto_ads'     => false,

    // Emplacements manuels (plus de controle)
    'slots' => [
        // Header : banniere horizontale en haut de page
        'header' => [
            'slot_id' => '',
            'format'  => 'auto',
            'layout'  => 'responsive',
        ],
        // In-article : entre deux sections de contenu
        'in_article' => [
            'slot_id' => '',
            'format'  => 'fluid',
            'layout'  => 'in-article',
        ],
        // In-article 2 : deuxieme emplacement dans un article long
        'in_article_2' => [
            'slot_id' => '',
            'format'  => 'fluid',
            'layout'  => 'in-article',
        ],
        // Sidebar : emplacement vertical cote
        'sidebar' => [
            'slot_id' => '',
            'format'  => 'auto',
            'layout'  => 'responsive',
        ],
        // Footer : banniere en bas de page
        'footer' => [
            'slot_id' => '',
            'format'  => 'auto',
            'layout'  => 'responsive',
        ],
    ],
];
