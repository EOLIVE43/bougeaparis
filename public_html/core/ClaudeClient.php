<?php
/**
 * ClaudeClient.php
 *
 * Client pour l'API Anthropic (Claude Messages API).
 * Documentation officielle : https://docs.claude.com/en/api/messages
 *
 * Responsabilites :
 * - Executer un appel POST /v1/messages
 * - Gerer l'authentification (header x-api-key)
 * - Retry automatique en cas d'erreur 5xx ou reseau (max 2 retries)
 * - Respecter les rate limits (429 -> retry avec backoff)
 * - Loguer le cout par appel (tokens input/output + estimation €)
 * - Renvoyer le texte genere OU null en cas d'echec total
 *
 * Utilisation :
 *   $client = new ClaudeClient(getenv('ANTHROPIC_API_KEY'));
 *   $result = $client->generate(
 *       systemPrompt: "Tu es un journaliste transport...",
 *       userMessage: "Voici les perturbations du jour...",
 *       maxTokens: 2000
 *   );
 *   if ($result !== null) {
 *       echo $result['text'];
 *       var_dump($result['usage']); // input_tokens, output_tokens, cost_eur
 *   }
 *
 * @package BougeaParis\Core
 * @since Livraison 4.2
 */

declare(strict_types=1);

class ClaudeClient
{
    /**
     * URL de l'API Anthropic.
     */
    private const API_URL = 'https://api.anthropic.com/v1/messages';

    /**
     * Version de l'API Anthropic (header obligatoire).
     * Cf https://docs.claude.com/en/api/versioning
     */
    private const API_VERSION = '2023-06-01';

    /**
     * Modele par defaut.
     * Sonnet 4.5 est le meilleur rapport qualite/prix pour la redaction editoriale.
     */
    private const DEFAULT_MODEL = 'claude-sonnet-4-5';

    /**
     * Timeout des requetes en secondes.
     * Generation d'un article de 600-900 mots = ~10-30s.
     */
    private const HTTP_TIMEOUT = 120;

    /**
     * Nombre max de retries en cas d'erreur 5xx ou reseau.
     */
    private const MAX_RETRIES = 2;

    /**
     * Delai initial entre retries (ms), augmente exponentiellement.
     */
    private const RETRY_DELAY_MS = 2000;

    /**
     * Tarifs Claude Sonnet 4.5 (USD / 1M tokens).
     * Cf https://www.anthropic.com/pricing
     * Input : 3$ / 1M tokens | Output : 15$ / 1M tokens
     */
    private const PRICE_INPUT_PER_1M_USD = 3.0;
    private const PRICE_OUTPUT_PER_1M_USD = 15.0;

    /**
     * Taux de change USD -> EUR (approximatif, a ajuster au fil du temps).
     */
    private const USD_TO_EUR = 0.92;

    /**
     * User-Agent envoye.
     */
    private const USER_AGENT = 'BougeaParis.fr/1.0 (https://bougeaparis.fr)';

    /**
     * Cle API Anthropic.
     */
    private string $apiKey;

    /**
     * Modele Claude utilise.
     */
    private string $model;

    /**
     * Derniere reponse brute (pour debug).
     * @var array<string, mixed>|null
     */
    private ?array $lastResponse = null;

    /**
     * Constructeur.
     *
     * @param string $apiKey Cle API Anthropic (format sk-ant-...).
     * @param string $model  Modele a utiliser (defaut : Sonnet 4.5).
     */
    public function __construct(string $apiKey, string $model = self::DEFAULT_MODEL)
    {
        if (empty($apiKey)) {
            throw new InvalidArgumentException('ClaudeClient: apiKey is required.');
        }
        if (!str_starts_with($apiKey, 'sk-ant-')) {
            throw new InvalidArgumentException('ClaudeClient: apiKey should start with sk-ant-.');
        }

        $this->apiKey = $apiKey;
        $this->model  = $model;
    }

    /**
     * Genere une reponse avec Claude.
     *
     * @param string $systemPrompt Instructions systeme (role, regles, contraintes).
     * @param string $userMessage  Message utilisateur (donnees + demande).
     * @param int $maxTokens       Tokens max dans la reponse (defaut 2000, ~1500 mots).
     * @param float $temperature   0.0 = deterministe, 1.0 = creatif (defaut 0.7 pour editorial).
     * @return array{text: string, usage: array{input_tokens: int, output_tokens: int, cost_eur: float}, stop_reason: string}|null
     */
    public function generate(
        string $systemPrompt,
        string $userMessage,
        int $maxTokens = 2000,
        float $temperature = 0.7
    ): ?array {
        $payload = [
            'model'       => $this->model,
            'max_tokens'  => $maxTokens,
            'temperature' => $temperature,
            'system'      => $systemPrompt,
            'messages'    => [
                [
                    'role'    => 'user',
                    'content' => $userMessage,
                ],
            ],
        ];

        $response = $this->callWithRetry($payload);
        if ($response === null) {
            return null;
        }

        return $this->extractResult($response);
    }

    /**
     * Appelle l'API avec retry automatique.
     *
     * @param array<string, mixed> $payload
     * @return array<string, mixed>|null
     */
    private function callWithRetry(array $payload): ?array
    {
        $attempt = 0;
        $delay = self::RETRY_DELAY_MS;
        $lastError = '';

        while ($attempt <= self::MAX_RETRIES) {
            $result = $this->httpPost($payload);
            $attempt++;

            // Succes : on sort.
            if ($result['success']) {
                return $result['data'];
            }

            $lastError = $result['error'];
            $httpCode = $result['http_code'];

            // Ne pas retry sur les erreurs 4xx autres que 429 (rate limit).
            if ($httpCode >= 400 && $httpCode < 500 && $httpCode !== 429) {
                $this->logError("Non-retryable error HTTP {$httpCode}: {$lastError}");
                return null;
            }

            // Dernier essai deja fait : on abandonne.
            if ($attempt > self::MAX_RETRIES) {
                break;
            }

            // Wait + retry avec backoff exponentiel.
            $this->logError("Retry {$attempt}/" . self::MAX_RETRIES . " after HTTP {$httpCode}: {$lastError}");
            usleep($delay * 1000);
            $delay *= 2;
        }

        $this->logError("All retries exhausted. Last error: {$lastError}");
        return null;
    }

    /**
     * Execute un POST HTTP sur l'API Anthropic.
     *
     * @param array<string, mixed> $payload
     * @return array{success: bool, data: array<string, mixed>|null, http_code: int, error: string}
     */
    private function httpPost(array $payload): array
    {
        $jsonPayload = json_encode($payload, JSON_UNESCAPED_UNICODE);
        if ($jsonPayload === false) {
            return [
                'success'   => false,
                'data'      => null,
                'http_code' => 0,
                'error'     => 'Failed to encode JSON payload',
            ];
        }

        $ch = curl_init();
        curl_setopt_array($ch, [
            CURLOPT_URL            => self::API_URL,
            CURLOPT_POST           => true,
            CURLOPT_POSTFIELDS     => $jsonPayload,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_TIMEOUT        => self::HTTP_TIMEOUT,
            CURLOPT_CONNECTTIMEOUT => 10,
            CURLOPT_HTTPHEADER     => [
                'Content-Type: application/json',
                'x-api-key: ' . $this->apiKey,
                'anthropic-version: ' . self::API_VERSION,
                'User-Agent: ' . self::USER_AGENT,
            ],
            CURLOPT_SSL_VERIFYPEER => true,
            CURLOPT_SSL_VERIFYHOST => 2,
        ]);

        $rawResponse = curl_exec($ch);
        $httpCode    = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $curlError   = curl_error($ch);
        curl_close($ch);

        // Erreur reseau ou timeout.
        if ($rawResponse === false || !empty($curlError)) {
            return [
                'success'   => false,
                'data'      => null,
                'http_code' => 0,
                'error'     => "Network error: {$curlError}",
            ];
        }

        $decoded = json_decode((string) $rawResponse, true);
        if (!is_array($decoded)) {
            return [
                'success'   => false,
                'data'      => null,
                'http_code' => $httpCode,
                'error'     => 'Failed to decode JSON response',
            ];
        }

        // HTTP non 200 : extraire le message d'erreur de l'API.
        if ($httpCode !== 200) {
            $apiError = $decoded['error']['message'] ?? 'Unknown API error';
            return [
                'success'   => false,
                'data'      => null,
                'http_code' => $httpCode,
                'error'     => "API error: {$apiError}",
            ];
        }

        // Succes.
        $this->lastResponse = $decoded;
        return [
            'success'   => true,
            'data'      => $decoded,
            'http_code' => 200,
            'error'     => '',
        ];
    }

    /**
     * Extrait le texte et les stats d'usage de la reponse Anthropic.
     *
     * @param array<string, mixed> $response
     * @return array{text: string, usage: array{input_tokens: int, output_tokens: int, cost_eur: float}, stop_reason: string}
     */
    private function extractResult(array $response): array
    {
        // Le texte est dans content[0].text pour les reponses simples.
        $text = '';
        foreach ($response['content'] ?? [] as $block) {
            if (($block['type'] ?? '') === 'text') {
                $text .= (string) ($block['text'] ?? '');
            }
        }

        $usage = $response['usage'] ?? [];
        $inputTokens  = (int) ($usage['input_tokens'] ?? 0);
        $outputTokens = (int) ($usage['output_tokens'] ?? 0);

        // Calcul du cout estime.
        $costUsd = (
            ($inputTokens / 1_000_000) * self::PRICE_INPUT_PER_1M_USD
            + ($outputTokens / 1_000_000) * self::PRICE_OUTPUT_PER_1M_USD
        );
        $costEur = round($costUsd * self::USD_TO_EUR, 6);

        return [
            'text' => $text,
            'usage' => [
                'input_tokens'  => $inputTokens,
                'output_tokens' => $outputTokens,
                'cost_eur'      => $costEur,
            ],
            'stop_reason' => (string) ($response['stop_reason'] ?? 'unknown'),
        ];
    }

    /**
     * Retourne la derniere reponse brute (debug).
     *
     * @return array<string, mixed>|null
     */
    public function getLastResponse(): ?array
    {
        return $this->lastResponse;
    }

    /**
     * Log une erreur vers error_log PHP.
     */
    private function logError(string $message): void
    {
        @error_log('[ClaudeClient] ' . $message);
    }
}
