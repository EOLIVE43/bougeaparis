<?php
/**
 * Fichier de secrets - TEMPLATE
 *
 * A COPIER en 'secrets.php' sur le serveur (cote o2switch via FTP)
 * et remplir avec vos vraies cles API.
 *
 * IMPORTANT : le fichier reel 'secrets.php' est exclu de Git (.gitignore)
 * pour que vos cles ne soient JAMAIS exposees sur GitHub.
 *
 * Sur o2switch, creer le fichier :
 *   /home/loxo5141/public_html/config/secrets.php
 * avec le contenu ci-dessous (en remplacant les valeurs).
 */

// Convention : nom des cles ALIGNE sur les variables d'environnement
// (utilisees par le workflow GitHub Actions et scripts/generate-article.php
// via getenv('PRIM_API_KEY')). Ne pas utiliser snake_case ici.
return [
    // Cle API PRIM (Ile-de-France Mobilites)
    // A obtenir sur : https://prim.iledefrance-mobilites.fr
    'PRIM_API_KEY' => 'COLLER_ICI_VOTRE_CLE_API_PRIM',

    // Cle API Anthropic (utilisee par scripts/generate-article.php)
    'ANTHROPIC_API_KEY' => '',

    // Cle API Navitia (optionnel)
    'NAVITIA_API_KEY' => '',
];
