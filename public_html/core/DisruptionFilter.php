<?php
/**
 * DisruptionFilter.php
 *
 * Filtre les perturbations PRIM selon la strategie editoriale Option B :
 * - Actives aujourd'hui
 * - Modes : Metro + RER + Tramway + Transilien (tous)
 * - Modes : Bus (uniquement reseau RATP Paris + uniquement BLOQUANTE)
 * - Dedoublonnage par ligne
 * - Tri par severite puis par mode
 *
 * @package BougeaParis\Core
 * @since Livraison 4.2
 */

declare(strict_types=1);

class DisruptionFilter
{
    /**
     * Configuration des networks/modes (loadee depuis config/networks.php).
     * @var array<string, mixed>
     */
    private array $config;

    /**
     * Index interne : disruptionId => array of impacted lines.
     * @var array<string, array<int, array{mode: string, shortName: string, network: string, lineId: string}>>
     */
    private array $disruptionLines = [];

    /**
     * Constructeur.
     *
     * @param array<string, mixed> $config Config depuis config/networks.php.
     */
    public function __construct(array $config)
    {
        $this->config = $config;
    }

    /**
     * Filtre une reponse PRIM brute et renvoie les perturbations pertinentes.
     *
     * @param array<string, mixed> $primResponse Reponse brute de PrimClient::fetchDisruptions()
     * @param string|null $referenceDate Date de reference (format YYYYMMDD). Defaut : aujourd'hui.
     * @return array<int, array<string, mixed>> Tableau de perturbations filtrees et enrichies.
     */
    public function filter(array $primResponse, ?string $referenceDate = null): array
    {
        $referenceDate = $referenceDate ?? date('Ymd');

        $disruptions = $primResponse['disruptions'] ?? [];
        $lines       = $primResponse['lines'] ?? [];

        if (empty($disruptions) || empty($lines)) {
            return [];
        }

        // 1. Indexer les lignes par disruptionId (pour lookup rapide).
        $this->buildDisruptionLinesIndex($lines);

        // 2. Filtrer les perturbations actives a la date de reference.
        $activeDisruptions = array_filter(
            $disruptions,
            fn (array $d): bool => $this->isActiveOn($d, $referenceDate)
        );

        // 3. Enrichir + filtrer par scope (Option B).
        $enriched = [];
        foreach ($activeDisruptions as $d) {
            $enrichedItem = $this->enrichDisruption($d);
            if ($enrichedItem === null) {
                continue; // hors scope
            }
            $enriched[] = $enrichedItem;
        }

        // 4. Tri : severite (BLOQUANTE > PERTURBEE > INFO) puis mode priorite.
        usort($enriched, function (array $a, array $b): int {
            $severityDiff = $this->getSeverityWeight($b['severity']) - $this->getSeverityWeight($a['severity']);
            if ($severityDiff !== 0) {
                return $severityDiff;
            }
            $modeA = $a['primary_mode'] ?? '';
            $modeB = $b['primary_mode'] ?? '';
            return $this->getModePriority($modeA) - $this->getModePriority($modeB);
        });

        return array_values($enriched);
    }

    /**
     * Construit l'index disruptionId -> lignes impactees (dedoublonne).
     *
     * @param array<int, array<string, mixed>> $lines
     */
    private function buildDisruptionLinesIndex(array $lines): void
    {
        $this->disruptionLines = [];

        foreach ($lines as $line) {
            $mode      = (string) ($line['mode'] ?? '');
            $shortName = (string) ($line['shortName'] ?? $line['name'] ?? '');
            $network   = (string) ($line['networkId'] ?? '');
            $lineId    = (string) ($line['id'] ?? '');

            foreach ($line['impactedObjects'] ?? [] as $impact) {
                foreach ($impact['disruptionIds'] ?? [] as $did) {
                    $did = (string) $did;
                    if (!isset($this->disruptionLines[$did])) {
                        $this->disruptionLines[$did] = [];
                    }

                    // Dedoublonnage : on n'ajoute pas deux fois la meme ligne.
                    $key = $mode . ':' . $shortName;
                    $alreadyAdded = false;
                    foreach ($this->disruptionLines[$did] as $existing) {
                        if (($existing['mode'] . ':' . $existing['shortName']) === $key) {
                            $alreadyAdded = true;
                            break;
                        }
                    }
                    if ($alreadyAdded) {
                        continue;
                    }

                    $this->disruptionLines[$did][] = [
                        'mode'      => $mode,
                        'shortName' => $shortName,
                        'network'   => $network,
                        'lineId'    => $lineId,
                    ];
                }
            }
        }
    }

    /**
     * Verifie qu'une perturbation est active a une date donnee.
     *
     * @param array<string, mixed> $disruption
     * @param string $date Format YYYYMMDD.
     */
    private function isActiveOn(array $disruption, string $date): bool
    {
        foreach ($disruption['applicationPeriods'] ?? [] as $period) {
            $begin = substr((string) ($period['begin'] ?? ''), 0, 8);
            $end   = substr((string) ($period['end'] ?? ''), 0, 8);
            if ($begin !== '' && $end !== '' && $begin <= $date && $date <= $end) {
                return true;
            }
        }
        return false;
    }

    /**
     * Enrichit une perturbation avec ses lignes, et verifie qu'elle entre dans le scope.
     *
     * @param array<string, mixed> $d
     * @return array<string, mixed>|null Null si la perturbation est hors scope.
     */
    private function enrichDisruption(array $d): ?array
    {
        $did = (string) ($d['id'] ?? '');
        $dLines = $this->disruptionLines[$did] ?? [];

        if (empty($dLines)) {
            return null;
        }

        $scopeModes   = $this->config['scope_modes'] ?? [];
        $busNetworks  = $this->config['scope_bus_networks'] ?? [];
        $severity     = (string) ($d['severity'] ?? '');

        // Filtrer les lignes en scope.
        $inScopeLines = [];
        foreach ($dLines as $line) {
            $mode    = $line['mode'];
            $network = $line['network'];

            // Metro / RER / Tram / Transilien : toujours inclus.
            if (in_array($mode, $scopeModes, true)) {
                $inScopeLines[] = $line;
                continue;
            }

            // Bus : seulement RATP Paris et seulement BLOQUANTE.
            if ($mode === 'Bus'
                && in_array($network, $busNetworks, true)
                && $severity === 'BLOQUANTE') {
                $inScopeLines[] = $line;
            }
        }

        // Si aucune ligne n'est dans le scope, on ecarte cette perturbation.
        if (empty($inScopeLines)) {
            return null;
        }

        // Determiner le mode principal (le plus prioritaire parmi les lignes impactees).
        $primaryMode = $this->determinePrimaryMode($inScopeLines);

        return [
            'id'                 => $did,
            'title'              => (string) ($d['title'] ?? ''),
            'message'            => (string) ($d['message'] ?? ''),
            'shortMessage'       => (string) ($d['shortMessage'] ?? ''),
            'cause'              => (string) ($d['cause'] ?? ''),
            'severity'           => $severity,
            'tags'               => $d['tags'] ?? [],
            'lastUpdate'         => (string) ($d['lastUpdate'] ?? ''),
            'applicationPeriods' => $d['applicationPeriods'] ?? [],
            'impactedSections'   => $d['impactedSections'] ?? [],
            'lines'              => $inScopeLines,
            'primary_mode'       => $primaryMode,
        ];
    }

    /**
     * Determine le mode "principal" d'une perturbation (le plus prioritaire).
     *
     * @param array<int, array{mode: string}> $lines
     */
    private function determinePrimaryMode(array $lines): string
    {
        $bestMode = '';
        $bestPriority = PHP_INT_MAX;
        foreach ($lines as $line) {
            $p = $this->getModePriority($line['mode']);
            if ($p < $bestPriority) {
                $bestPriority = $p;
                $bestMode = $line['mode'];
            }
        }
        return $bestMode;
    }

    /**
     * Poids numerique de la severite (pour tri).
     */
    private function getSeverityWeight(string $severity): int
    {
        return (int) ($this->config['severity_weight'][$severity] ?? 0);
    }

    /**
     * Priorite d'affichage du mode (plus bas = prioritaire).
     */
    private function getModePriority(string $mode): int
    {
        return (int) ($this->config['mode_priority'][$mode] ?? 999);
    }

    /**
     * Retourne des statistiques sur le filtrage (utile pour logs et monitoring).
     *
     * @param array<int, array<string, mixed>> $filtered Resultat de filter()
     * @return array<string, int>
     */
    public static function computeStats(array $filtered): array
    {
        $stats = [
            'total'        => count($filtered),
            'bloquante'    => 0,
            'perturbee'    => 0,
            'information'  => 0,
            'metro'        => 0,
            'rer'          => 0,
            'tramway'      => 0,
            'transilien'   => 0,
            'bus'          => 0,
        ];

        $modeMap = [
            'Metro'        => 'metro',
            'RapidTransit' => 'rer',
            'Tramway'      => 'tramway',
            'LocalTrain'   => 'transilien',
            'Bus'          => 'bus',
        ];

        foreach ($filtered as $d) {
            $sev = strtolower((string) ($d['severity'] ?? ''));
            if (isset($stats[$sev])) {
                $stats[$sev]++;
            }

            $mode = (string) ($d['primary_mode'] ?? '');
            if (isset($modeMap[$mode]) && isset($stats[$modeMap[$mode]])) {
                $stats[$modeMap[$mode]]++;
            }
        }

        return $stats;
    }
}
