<?php
/**
 * Helpers schema.org pour les pages stations métro.
 *
 * Méthodes statiques stateless qui retournent des sous-tableaux JSON-LD
 * réinjectables dans le @graph d'une page. Évite de répéter la même
 * construction sur les 300 stations du réseau.
 *
 * Voir docs/TEMPLATE_GUIDE.md (Section Backlog I) pour la stratégie globale.
 */

class SchemaHelpers
{
    /**
     * Convention RATP réseau métro pour les horaires de service.
     *
     * Source : convention RATP figée dans TEMPLATE_GUIDE Q4 FAQ.
     * Applicable à 99% des stations du réseau métro Paris. Les exceptions
     * (terminus nouveau M14, stations à horaires propres) pourront un jour
     * être prises en charge via un champ JSON `opening_hours_override` sur
     * la station — non implémenté aujourd'hui (YAGNI).
     *
     * @return array Liste de 2 OpeningHoursSpecification (semaine + week-end).
     */
    public static function ratpMetroOpeningHours(): array
    {
        return [
            [
                '@type'     => 'OpeningHoursSpecification',
                'dayOfWeek' => ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Sunday'],
                'opens'     => '05:30',
                'closes'    => '01:15',
            ],
            [
                '@type'     => 'OpeningHoursSpecification',
                'dayOfWeek' => ['Friday', 'Saturday'],
                'opens'     => '05:30',
                'closes'    => '02:15',
            ],
        ];
    }

    /**
     * Features d'accessibilité PMR d'une station, format
     * LocationFeatureSpecification[] pour fusion dans `amenityFeature`.
     *
     * Mapping selon `accessibility.level` (TEMPLATE_GUIDE Section 7C) :
     *  - "accessible"               → 2 features = true
     *  - "partial" / "partiellement-accessible" + elevators_count > 0
     *                               → "Ascenseur PMR" true, "Accès sans marche" false
     *  - "partial" sans ascenseurs  → 2 features = false
     *  - "non-conforme"             → 2 features = false
     *  - autre / absent             → [] (T0 strict : pas d'émission sans audit)
     *
     * @param array $station Le JSON station décodé.
     * @return array Liste de LocationFeatureSpecification (peut être vide).
     */
    public static function stationAccessibilityFeatures(array $station): array
    {
        $accessibility = $station['accessibility'] ?? null;
        if (!is_array($accessibility)) {
            return [];
        }

        $level     = $accessibility['level'] ?? null;
        $elevators = (int)($accessibility['stats']['elevators_count'] ?? 0);

        $isAccessible  = ($level === 'accessible');
        $isPartial     = in_array($level, ['partial', 'partiellement-accessible'], true);
        $isNonConforme = ($level === 'non-conforme');

        if (!$isAccessible && !$isPartial && !$isNonConforme) {
            return []; // T0 strict : pas d'émission si level inconnu
        }

        if ($isAccessible) {
            return [
                self::feature('Accès sans marche', true),
                self::feature('Ascenseur PMR',     true),
            ];
        }

        if ($isPartial && $elevators > 0) {
            return [
                self::feature('Accès sans marche', false),
                self::feature('Ascenseur PMR',     true),
            ];
        }

        // partial sans ascenseur, ou non-conforme
        return [
            self::feature('Accès sans marche', false),
            self::feature('Ascenseur PMR',     false),
        ];
    }

    /**
     * Features de services confirmés d'une station, format
     * LocationFeatureSpecification[] pour fusion dans `amenityFeature`.
     *
     * Supporte les 2 schémas du JSON :
     *  - Schéma 3-statuts (post-pilote) : émet si status === "verified_present"
     *  - Schéma legacy LOT 1/2          : émet si available === true
     *
     * Les services à structure imbriquée (toilets.public_paid/free,
     * left_luggage.ratp/third_party, shopping_dining descriptif) sont
     * skippés en V1 — extension possible si besoin futur. Pas de
     * doublon avec stationAccessibilityFeatures() : le service
     * `elevator`/`ascenseur` n'est pas dans le schéma JSON station
     * (l'accessibilité PMR est portée par .accessibility.*).
     *
     * @param array $station Le JSON station décodé.
     * @return array Liste de LocationFeatureSpecification (peut être vide).
     */
    public static function stationServiceFeatures(array $station): array
    {
        $services = $station['services'] ?? null;
        if (!is_array($services)) {
            return [];
        }

        // Mapping clé JSON → libellé FR. Restreint aux services binaires
        // (status ou available direct). Imbriqués traités en V2 si besoin.
        $labels = [
            'atm'         => 'Distributeur de billets',
            'wifi'        => 'Wi-Fi',
            'ratp_office' => 'Agence RATP',
        ];

        $features = [];
        foreach ($labels as $key => $label) {
            $entry = $services[$key] ?? null;
            if (!is_array($entry)) continue;

            $present = false;
            if (array_key_exists('status', $entry)) {
                $present = ($entry['status'] === 'verified_present');
            } elseif (array_key_exists('available', $entry)) {
                $present = ($entry['available'] === true);
            }

            if ($present) {
                $features[] = self::feature($label, true);
            }
        }
        return $features;
    }

    /**
     * Helper privé : construit un LocationFeatureSpecification.
     */
    private static function feature(string $name, bool $value): array
    {
        return [
            '@type' => 'LocationFeatureSpecification',
            'name'  => $name,
            'value' => $value,
        ];
    }

    /**
     * Liste des POIs touristiques à proximité d'une station, format
     * ItemList (Carousel rich result Google) avec items TouristAttraction.
     *
     * Stratégie (TEMPLATE_GUIDE Section 6C) : top 5 POIs uniquement,
     * car eux seuls ont une description auditée T0. Les POIs 6-N ont
     * `description: null` côté JSON et sont émis sans description
     * (Pattern 4 de l'investigation I.5).
     *
     * Filtres T0 :
     *  - nearby_pois absent / vide → return null (skip propre dans @graph)
     *  - POI sans name → skipped
     *  - POI sans description → émis avec name + geo + url, clé description omise
     *  - POI sans coordonnées (lat/lng) → geo omis (POI émis quand même si name)
     *
     * @param array  $station    Le JSON station décodé.
     * @param string $stationUrl URL canonique absolue de la station
     *                           (pour construction des @id internes).
     * @return array|null ItemList complet ou null si rien à émettre.
     */
    public static function stationNearbyPoisAsItemList(array $station, string $stationUrl): ?array
    {
        $pois = $station['nearby_pois'] ?? null;
        if (!is_array($pois) || empty($pois)) {
            return null;
        }

        // Section 6C : seul le top 5 est audité T0 (description rédigée)
        $topPois = array_slice($pois, 0, 5);

        $items = [];
        $position = 1;
        foreach ($topPois as $poi) {
            if (!is_array($poi)) continue;

            $name = $poi['name'] ?? null;
            if (!is_string($name) || $name === '') {
                continue; // T0 : pas de POI sans nom
            }

            $attraction = [
                '@type' => 'TouristAttraction',
                'name'  => $name,
            ];

            $wikiUrl = $poi['wikipedia_url'] ?? null;
            if (is_string($wikiUrl) && $wikiUrl !== '') {
                $attraction['url'] = $wikiUrl;
            }

            // T0 strict : pas d'émission de description si null/vide
            $description = $poi['description'] ?? null;
            if (is_string($description) && $description !== '') {
                $attraction['description'] = $description;
            }

            $lat = $poi['latitude']  ?? null;
            $lng = $poi['longitude'] ?? null;
            if (is_numeric($lat) && is_numeric($lng)) {
                $attraction['geo'] = [
                    '@type'     => 'GeoCoordinates',
                    'latitude'  => (float)$lat,
                    'longitude' => (float)$lng,
                ];
            }

            $items[] = [
                '@type'    => 'ListItem',
                'position' => $position++,
                'item'     => $attraction,
            ];
        }

        if (empty($items)) {
            return null;
        }

        $stationName = $station['name'] ?? 'la station';

        return [
            '@type'           => 'ItemList',
            '@id'             => $stationUrl . '#nearby-pois',
            'name'            => "Lieux touristiques à proximité de la station {$stationName}",
            'numberOfItems'   => count($items),
            'itemListElement' => $items,
        ];
    }

    /**
     * Liste des itinéraires populaires depuis une station, format
     * ItemList (Carousel rich result Google) avec items Trip.
     *
     * Chaque item est un Trip (schema.org) avec :
     *  - name        : "{destination} (~{N} min)" si durée connue, sinon nom seul
     *  - description : "Itinéraire via {lines_label}" si lines_label présent
     *  - url         : présent UNIQUEMENT si Routes::exists($future_url) — cohérent
     *                  avec le pattern conditionalLink du front. Évite d'émettre
     *                  des liens vers du 404 (le cocon /itineraires/ Phase 3
     *                  n'est pas encore livré au 2026-06). Le jour où il l'est,
     *                  l'url apparaît automatiquement dans le schema sans modif.
     *
     * Filtres T0 :
     *  - popular_itineraries absent / vide → return null (skip propre dans @graph)
     *  - itin sans destination_name → skipped
     *  - duration_minutes absent / 0 → name = nom seul (pas de "~ min")
     *  - lines_label absent / vide → clé description omise
     *
     * @param array  $station    Le JSON station décodé.
     * @param string $stationUrl URL canonique absolue de la station.
     * @return array|null ItemList complet ou null si rien à émettre.
     */
    public static function stationPopularItinerariesAsItemList(array $station, string $stationUrl): ?array
    {
        $itineraries = $station['popular_itineraries'] ?? null;
        if (!is_array($itineraries) || empty($itineraries)) {
            return null;
        }

        $siteUrl = rtrim(Config::get('site.url'), '/');

        $items = [];
        $position = 1;
        foreach ($itineraries as $itin) {
            if (!is_array($itin)) continue;

            $destinationName = $itin['destination_name'] ?? null;
            if (!is_string($destinationName) || $destinationName === '') {
                continue; // T0 : pas d'item sans destination
            }

            // Nom : "Destination (~XX min)" si durée dispo, sinon nom seul
            $duration = $itin['duration_minutes'] ?? null;
            if (is_numeric($duration) && (int)$duration > 0) {
                $name = sprintf('%s (~%d min)', $destinationName, (int)$duration);
            } else {
                $name = $destinationName;
            }

            $trip = [
                '@type' => 'Trip',
                'name'  => $name,
            ];

            $linesLabel = $itin['lines_label'] ?? null;
            if (is_string($linesLabel) && $linesLabel !== '') {
                $trip['description'] = 'Itinéraire via ' . $linesLabel;
            }

            // URL : seulement si la page cible existe vraiment (évite 404).
            // Pattern cohérent avec conditionalLink utilisé dans le front
            // (templates/components/station/itineraires-populaires.php).
            $futureUrl = $itin['future_url'] ?? null;
            if (is_string($futureUrl) && $futureUrl !== '') {
                if (Routes::exists(rtrim($futureUrl, '/'))) {
                    $trip['url'] = $siteUrl . $futureUrl;
                }
            }

            $items[] = [
                '@type'    => 'ListItem',
                'position' => $position++,
                'item'     => $trip,
            ];
        }

        if (empty($items)) {
            return null;
        }

        $stationName = $station['name'] ?? 'la station';

        return [
            '@type'           => 'ItemList',
            '@id'             => $stationUrl . '#popular-itineraries',
            'name'            => "Itinéraires populaires depuis la station {$stationName}",
            'numberOfItems'   => count($items),
            'itemListElement' => $items,
        ];
    }
}
