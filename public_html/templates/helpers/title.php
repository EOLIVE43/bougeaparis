<?php
declare(strict_types=1);

/**
 * Helper centralisé pour génération des titles SEO.
 *
 * Patterns validés user :
 *   - Mot-clé principal en début (Métro / Aéroport / Mode-aéroport)
 *   - Mots-clés transactionnels en fin (plan, horaires, guide, durée+prix)
 *   - Cible affichage ≤ 65 caractères Google (suffix désactivé via withSuffix=false)
 *
 * Usage : $tpl->seo->setTitle(bp_title_station($name, $codes), false);
 */

if (!function_exists('bp_title_station')) {

    /**
     * Title station métro.
     * Pattern : "Métro {Nom} (M1, M4, RER A) : plan et horaires"
     * Ex : "Métro Châtelet (M1, M4, M7, M11) : plan et horaires"
     */
    function bp_title_station(string $name, array $codes): string
    {
        $codes = array_values(array_filter($codes));
        $shown = array_slice($codes, 0, 5);
        $extra = count($codes) > 5 ? '…' : '';
        $codesStr = $shown ? '(' . implode(', ', $shown) . $extra . ')' : '';
        $title = trim("Métro $name $codesStr : plan et horaires");
        if (strlen($title) > 65 && $codes) {
            // Try short codes list
            $title = trim("Métro $name : plan et horaires");
        }
        return $title;
    }

    /**
     * Title ligne métro.
     * Pattern : "Ligne {N} du métro de Paris : plan, stations, horaires"
     */
    function bp_title_ligne_metro(string $code): string
    {
        return "Ligne $code du métro de Paris : plan et horaires";
    }

    /**
     * Title station RER.
     * Pattern : "RER {Nom} ({lignes}) : plan et horaires"
     * Ex : "RER Châtelet — Les Halles (A, B, D) : plan et horaires"
     */
    function bp_title_station_rer(string $name, array $codes): string
    {
        $codes = array_values(array_filter($codes));
        $shown = array_slice($codes, 0, 5);
        $extra = count($codes) > 5 ? '…' : '';
        $codesStr = $shown ? '(' . implode(', ', $shown) . $extra . ')' : '';
        $title = trim("RER $name $codesStr : plan et horaires");
        if (strlen($title) > 65 && $codes) {
            $title = trim("RER $name : plan et horaires");
        }
        return $title;
    }

    /**
     * Title ligne RER.
     * Pattern : "Ligne {A/B/C/D/E} du RER : plan, stations, horaires"
     */
    function bp_title_ligne_rer(string $code): string
    {
        $code = strtoupper($code);
        return "Ligne $code du RER : plan, stations et horaires";
    }

    /**
     * Title hub aéroport (CDG / Orly / Beauvais).
     * Pattern : "Aéroport Paris-{X} ({IATA}) : guide complet"
     * Atemporel par défaut. Une année figée injectée par code = signal
     * "page non maintenue" pour Google. Les faits datés sourcés vont dans
     * le corps de la page, pas dans le helper title.
     */
    function bp_title_aeroport_hub(string $name, string $iata): string
    {
        return "Aéroport $name ($iata) : guide complet";
    }

    /**
     * Title page mode-aéroport (métro/bus/RER/tramway/train/navette).
     * Pattern : "{Mode} aéroport Paris-{X} : {durée}, {prix}"
     * Ex : "Métro 14 aéroport Paris-Orly : 25 min, 2,15 €"
     */
    function bp_title_aeroport_mode(
        string $modeName,
        string $aeroName,
        ?string $duration = null,
        ?string $price = null
    ): string {
        $aero = bp_title_aeroport_short($aeroName);
        $title = "$modeName aéroport $aero";
        $parts = array_filter([$duration, $price]);
        if ($parts) {
            $title .= ' : ' . implode(', ', $parts);
        }
        if (strlen($title) > 65) {
            $title = "$modeName aéroport $aero";
        }
        return $title;
    }

    /**
     * Title page taxi-aéroport.
     * Pattern : "Taxi aéroport Paris-{X} : {prix}, {durée}"
     */
    function bp_title_taxi_aeroport(string $aeroName, string $price, string $duration): string
    {
        $aero = bp_title_aeroport_short($aeroName);
        $t = "Taxi aéroport $aero : $price, $duration";
        if (strlen($t) > 65) {
            $t = "Taxi aéroport $aero : $price";
        }
        return $t;
    }

    /**
     * Title hub mode de transport (métro, RER, bus, tramway, transilien).
     * Pattern : "{Hub} Paris : guide complet, plans et horaires"
     */
    function bp_title_hub(string $hubName): string
    {
        return "$hubName Paris : guide complet, plans et horaires";
    }

    /**
     * Title hub global aéroports.
     */
    function bp_title_aeroports_hub(): string
    {
        return "Aéroports de Paris : guide d'accès (CDG, Orly, Beauvais)";
    }

    /**
     * Normalise un nom d'aéroport vers sa forme courte "Paris-X".
     * "Paris-Charles de Gaulle" → "Paris-CDG" (via IATA si dans le nom)
     * "Paris-Orly" → "Paris-Orly"
     */
    function bp_title_aeroport_short(string $name): string
    {
        $name = trim($name);
        // Si le nom contient déjà "Paris-", on le garde
        if (stripos($name, 'paris-') === 0) {
            return $name;
        }
        // Sinon on préfixe "Paris-"
        return 'Paris-' . $name;
    }
}
