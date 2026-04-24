<?php
/**
 * DisruptionFormatter.php
 *
 * Transforme une liste de perturbations filtrees en structure compacte et lisible,
 * prete a etre envoyee a Claude (ou affichee dans un article).
 *
 * Responsabilites :
 * - Nettoyer le HTML des messages PRIM (garde le texte propre)
 * - Regrouper les perturbations par ligne
 * - Produire un resume textuel compact (~3-5k tokens max)
 * - Generer aussi une version structuree (JSON) pour les widgets
 *
 * @package BougeaParis\Core
 * @since Livraison 4.2
 */

declare(strict_types=1);

class DisruptionFormatter
{
    /**
     * Config des networks/modes.
     * @var array<string, mixed>
     */
    private array $config;

    /**
     * @param array<string, mixed> $config Config depuis config/networks.php.
     */
    public function __construct(array $config)
    {
        $this->config = $config;
    }

    /**
     * Nettoie le HTML d'un message PRIM (retire balises, styles, entites).
     */
    public static function cleanHtml(string $html): string
    {
        if ($html === '') {
            return '';
        }

        // Remplacer <br> et variations par des sauts de ligne.
        $text = preg_replace('#<br\s*/?\s*>#i', "\n", $html) ?? $html;

        // Remplacer </p> par double saut de ligne (conserve paragraphes).
        $text = preg_replace('#</p>#i', "\n\n", $text) ?? $text;

        // Retirer toutes les balises HTML restantes.
        $text = strip_tags($text);

        // Decoder les entites HTML.
        $text = html_entity_decode($text, ENT_QUOTES | ENT_HTML5, 'UTF-8');

        // Remplacer &nbsp; residuel par espace normal (au cas ou).
        $text = str_replace(["\xc2\xa0", '&nbsp;'], ' ', $text);

        // Nettoyer les espaces multiples sur chaque ligne.
        $lines = explode("\n", $text);
        $lines = array_map(static function (string $l): string {
            return trim(preg_replace('/\s+/', ' ', $l) ?? $l);
        }, $lines);

        // Retirer les lignes vides consecutives.
        $cleaned = [];
        $lastEmpty = false;
        foreach ($lines as $l) {
            $empty = ($l === '');
            if ($empty && $lastEmpty) {
                continue;
            }
            $cleaned[] = $l;
            $lastEmpty = $empty;
        }

        return trim(implode("\n", $cleaned));
    }

    /**
     * Formate une liste de perturbations en texte compact pour Claude.
     *
     * Format de sortie (exemple) :
     *
     *   ### METRO
     *
     *   **Métro 4** - Trafic interrompu (Travaux)
     *   Titre : Métro 4 : Travaux d'entretien - Trafic interrompu
     *   Détail : Jusqu'au 1er mai, trafic interrompu entre Châtelet et Barbès.
     *
     *   **Métro 6** - Trafic perturbé (Incident)
     *   ...
     *
     * @param array<int, array<string, mixed>> $disruptions Resultat de DisruptionFilter::filter()
     * @param int $maxMessageLength Longueur max du message par perturbation (troncature).
     */
    public function formatForClaude(array $disruptions, int $maxMessageLength = 400): string
    {
        if (empty($disruptions)) {
            return "Aucune perturbation significative dans le scope editorial aujourd'hui.";
        }

        $modesLabels    = $this->config['modes'] ?? [];
        $severityLabels = $this->config['severity_labels'] ?? [];
        $causeLabels    = $this->config['cause_labels'] ?? [];

        // Regrouper par mode principal.
        $byMode = [];
        foreach ($disruptions as $d) {
            $mode = (string) ($d['primary_mode'] ?? 'UNKNOWN');
            $byMode[$mode][] = $d;
        }

        // Ordre d'affichage : metro > rer > tram > transilien > bus.
        $modePriority = $this->config['mode_priority'] ?? [];
        uksort($byMode, function (string $a, string $b) use ($modePriority): int {
            $pa = $modePriority[$a] ?? 999;
            $pb = $modePriority[$b] ?? 999;
            return $pa - $pb;
        });

        $output = [];
        foreach ($byMode as $mode => $modeDisruptions) {
            $label = strtoupper($modesLabels[$mode] ?? $mode);
            $output[] = "### {$label}";
            $output[] = '';

            foreach ($modeDisruptions as $d) {
                // Ligne(s) impactee(s).
                $lineNames = [];
                foreach ($d['lines'] ?? [] as $line) {
                    $lineLabel = ($modesLabels[$line['mode']] ?? $line['mode']) . ' ' . $line['shortName'];
                    if (!in_array($lineLabel, $lineNames, true)) {
                        $lineNames[] = $lineLabel;
                    }
                }
                $linesStr = implode(', ', $lineNames);

                $sevLabel   = $severityLabels[$d['severity']] ?? $d['severity'];
                $causeLabel = $causeLabels[$d['cause']] ?? $d['cause'];

                $output[] = "**{$linesStr}** - {$sevLabel} ({$causeLabel})";

                $title = trim((string) ($d['title'] ?? ''));
                if ($title !== '') {
                    $output[] = "Titre : {$title}";
                }

                $message = self::cleanHtml((string) ($d['message'] ?? ''));
                // Supprimer le doublon si le titre est deja dans le message.
                if ($title !== '' && stripos($message, $title) === 0) {
                    $message = trim(substr($message, strlen($title)));
                }
                if ($message !== '') {
                    $message = self::truncate($message, $maxMessageLength);
                    $output[] = "Détail : {$message}";
                }

                // Periode.
                $period = $this->formatApplicationPeriod($d['applicationPeriods'] ?? []);
                if ($period !== '') {
                    $output[] = "Période : {$period}";
                }

                $output[] = '';
            }
        }

        return trim(implode("\n", $output));
    }

    /**
     * Produit une structure JSON groupee par ligne, pour les widgets.
     *
     * Format :
     *   {
     *     "metro-4": {
     *       "line": {"mode": "Metro", "shortName": "4", "label": "Métro 4"},
     *       "disruptions": [...]
     *     },
     *     ...
     *   }
     *
     * @param array<int, array<string, mixed>> $disruptions
     * @return array<string, array<string, mixed>>
     */
    public function groupByLine(array $disruptions): array
    {
        $modesLabels = $this->config['modes'] ?? [];
        $lineSlugs   = $this->config['line_slugs'] ?? [];

        $byLine = [];

        foreach ($disruptions as $d) {
            foreach ($d['lines'] ?? [] as $line) {
                $mode      = $line['mode'];
                $shortName = $line['shortName'];
                $key       = $mode . ':' . $shortName;

                // On genere un slug : soit depuis le mapping config, soit fallback.
                $slug = $lineSlugs[$key] ?? strtolower(str_replace(':', '-', $key));

                // Cle de tableau : slug avec / remplace par - (pour JSON filename).
                $lineKey = str_replace('/', '-', $slug);

                if (!isset($byLine[$lineKey])) {
                    $byLine[$lineKey] = [
                        'line' => [
                            'mode'      => $mode,
                            'shortName' => $shortName,
                            'label'     => ($modesLabels[$mode] ?? $mode) . ' ' . $shortName,
                            'slug'      => $slug,
                        ],
                        'disruptions' => [],
                    ];
                }

                // Ajouter la perturbation (version allegee).
                $byLine[$lineKey]['disruptions'][] = [
                    'id'           => $d['id'],
                    'severity'     => $d['severity'],
                    'cause'        => $d['cause'],
                    'title'        => $d['title'],
                    'message'      => self::cleanHtml($d['message']),
                    'shortMessage' => $d['shortMessage'] ?? '',
                    'lastUpdate'   => $d['lastUpdate'] ?? '',
                ];
            }
        }

        return $byLine;
    }

    /**
     * Formate une periode d'application en texte lisible.
     *
     * @param array<int, array{begin?: string, end?: string}> $periods
     */
    private function formatApplicationPeriod(array $periods): string
    {
        if (empty($periods)) {
            return '';
        }

        // On ne prend que la 1ere periode (simplification).
        $p = $periods[0];
        $begin = (string) ($p['begin'] ?? '');
        $end   = (string) ($p['end'] ?? '');

        if ($begin === '' || $end === '') {
            return '';
        }

        $beginDate = self::parseIdfmDate($begin);
        $endDate   = self::parseIdfmDate($end);

        if ($beginDate === null || $endDate === null) {
            return '';
        }

        // Format lisible francais.
        $today = date('Y-m-d');
        $beginStr = $beginDate->format('d/m/Y');
        $endStr   = $endDate->format('d/m/Y');

        if ($beginDate->format('Y-m-d') === $endDate->format('Y-m-d')) {
            return "le {$beginStr}";
        }

        if ($beginDate->format('Y-m-d') <= $today && $today <= $endDate->format('Y-m-d')) {
            return "en cours, jusqu'au {$endStr}";
        }

        return "du {$beginStr} au {$endStr}";
    }

    /**
     * Parse une date au format IDFM (YYYYMMDDTHHMMSS).
     */
    private static function parseIdfmDate(string $raw): ?DateTimeImmutable
    {
        if (strlen($raw) < 8) {
            return null;
        }

        // Tenter le format complet d'abord.
        $dt = DateTimeImmutable::createFromFormat('Ymd\THis', $raw);
        if ($dt === false) {
            // Fallback : juste la date.
            $dt = DateTimeImmutable::createFromFormat('Ymd', substr($raw, 0, 8));
        }

        return $dt === false ? null : $dt;
    }

    /**
     * Tronque un texte proprement (sur une limite de mots si possible).
     */
    private static function truncate(string $text, int $maxLength): string
    {
        if (mb_strlen($text) <= $maxLength) {
            return $text;
        }

        $truncated = mb_substr($text, 0, $maxLength);
        $lastSpace = mb_strrpos($truncated, ' ');
        if ($lastSpace !== false && $lastSpace > ($maxLength * 0.7)) {
            $truncated = mb_substr($truncated, 0, $lastSpace);
        }

        return rtrim($truncated) . '...';
    }
}
