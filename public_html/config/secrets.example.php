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

return [
    // Cle API PRIM (Ile-de-France Mobilites)
    // A obtenir sur : https://prim.iledefrance-mobilites.fr
    'prim_api_key' => 'COLLER_ICI_VOTRE_CLE_API_PRIM',

    // Cle API Navitia (optionnel - si vous utilisez Navitia en plus de PRIM)
    // A obtenir sur : https://navitia.io
    'navitia_api_key' => '',
];
