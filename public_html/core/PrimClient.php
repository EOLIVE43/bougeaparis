<?php
/**
 * PrimClient.php
 *
 * Client pour l'API Ile-de-France Mobilites (PRIM).
 * Endpoint : Diffusion des donnees de perturbation du trafic (disruptions_bulk).
 *
 * Responsabilites :
 * - Effectuer un appel GET a l'API PRIM
 * - Gerer l'authentification via header apikey
 * - Mettre en cache la reponse (TTL 5 minutes par defaut)
 * - Gerer les erreurs reseau et API
 * - Fournir un fallback si l'API est indisponible
 *
 * Utilisation :
 *   $client = new PrimClient(getenv('PRIM_API_KEY'));
 *   $data = $client->fetchDisruptions();
 *   if ($data === null) {
 *       // Fallback : API indisponible
 *   }
 *
 * @package BougeaParis\Core
 * @since Livraison 4.2
 */

declare(strict_types=1);

class PrimClient
{
    /**
     * URL de base de l'API PRIM.
     */
    private const API_BASE_URL = 'https://prim.iledefrance-mobilites.fr/marketplace/disruptions_bulk';

    /**
     * Endpoint des perturbations (v2).
     */
    private const ENDPOINT_DISRUPTIONS = '/disruptions/v2';

    /**
     * TTL du cache en secondes (5 minutes).
     * Les donnees de perturbation sont mises a jour toutes les quelques minutes.
     */
    private const CACHE_TTL = 300;

    /**
     * Timeout des requetes HTTP en secondes.
     */
    private const HTTP_TIMEOUT = 30;

    /**
     * User-Agent envoye dans les requetes (identifie le client proprement).
     */
    private const USER_AGENT = 'BougeaParis.fr/1.0 (https://bougeaparis.fr)';

    /**
     * Cle API PRIM.
     */
    private string $apiKey;

    /**
     * Dossier ou stocker le cache.
     */
    private string $cacheDir;

    /**
     * Derniere reponse HTTP (pour debug).
     * @var array<string, mixed>|null
     */
    private ?array $lastResponse = null;

    /**
     * Constructeur.
     *
     * @param string $apiKey   Cle API PRIM.
     * @param string $cacheDir Dossier de cache (par defaut : /tmp/prim-cache).
     */
    public function __construct(string $apiKey, string $cacheDir = '/tmp/prim-cache')
    {
        if (empty($apiKey)) {
            throw new InvalidArgumentException('PrimClient: apiKey is required.');
        }

        $this->apiKey   = $apiKey;
        $this->cacheDir = rtrim($cacheDir, '/');

        // Cree le dossier de cache s'il n'existe pas.
        if (!is_dir($this->cacheDir)) {
            if (!@mkdir($this->cacheDir, 0755, true) && !is_dir($this->cacheDir)) {
                throw new RuntimeException("PrimClient: cannot create cache dir: {$this->cacheDir}");
            }
        }
    }

    /**
     * Recupere les perturbations depuis l'API PRIM (avec cache).
     *
     * @param bool $forceRefresh Si true, ignore le cache et refait l'appel.
     * @return array<string, mixed>|null Tableau associatif decode depuis JSON, ou null si echec.
     */
    public function fetchDisruptions(bool $forceRefresh = false): ?array
    {
        $cacheFile = $this->cacheDir . '/disruptions.json';

        // Tentative de lecture du cache.
        if (!$forceRefresh && $this->isCacheValid($cacheFile)) {
            $cached = $this->readCache($cacheFile);
            if ($cached !== null) {
                return $cached;
            }
        }

        // Appel API reel.
        $data = $this->httpGet(self::API_BASE_URL . self::ENDPOINT_DISRUPTIONS);

        if ($data !== null) {
            // Succes : on ecrit le cache.
            $this->writeCache($cacheFile, $data);
        } elseif ($this->cacheExists($cacheFile)) {
            // Echec API mais cache existant (meme expire) : fallback sur le cache.
            // Mieux vaut des donnees un peu vieilles que pas de donnees du tout.
            return $this->readCache($cacheFile);
        }

        return $data;
    }

    /**
     * Execute un GET HTTP sur l'API PRIM.
     *
     * @param string $url URL complete a appeler.
     * @return array<string, mixed>|null Donnees JSON decodees, ou null si echec.
     */
    private function httpGet(string $url): ?array
    {
        $ch = curl_init();

        curl_setopt_array($ch, [
            CURLOPT_URL            => $url,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_TIMEOUT        => self::HTTP_TIMEOUT,
            CURLOPT_CONNECTTIMEOUT => 10,
            CURLOPT_HTTPHEADER     => [
                'apikey: ' . $this->apiKey,
                'Accept: application/json',
                'User-Agent: ' . self::USER_AGENT,
            ],
            CURLOPT_SSL_VERIFYPEER => true,
            CURLOPT_SSL_VERIFYHOST => 2,
            CURLOPT_ENCODING       => '', // supporte gzip/deflate
        ]);

        $rawResponse = curl_exec($ch);
        $httpCode    = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $curlError   = curl_error($ch);

        curl_close($ch);

        // Traces pour debug (uniquement en memoire, pas dans le cache).
        $this->lastResponse = [
            'http_code'   => $httpCode,
            'curl_error'  => $curlError,
            'bytes'       => is_string($rawResponse) ? strlen($rawResponse) : 0,
            'timestamp'   => time(),
        ];

        // Erreur reseau.
        if ($rawResponse === false || !empty($curlError)) {
            $this->logError("HTTP request failed: {$curlError}");
            return null;
        }

        // Erreur API.
        if ($httpCode !== 200) {
            $this->logError("API returned HTTP {$httpCode} for {$url}");
            return null;
        }

        // Decodage JSON.
        $decoded = json_decode((string) $rawResponse, true);
        if (!is_array($decoded)) {
            $this->logError('Failed to decode JSON response: ' . json_last_error_msg());
            return null;
        }

        // Sanity check : on attend au moins la cle "disruptions".
        if (!isset($decoded['disruptions'])) {
            $this->logError('Unexpected API response: missing "disruptions" key');
            return null;
        }

        return $decoded;
    }

    /**
     * Verifie si le cache est valide (non expire).
     */
    private function isCacheValid(string $cacheFile): bool
    {
        if (!file_exists($cacheFile)) {
            return false;
        }

        $mtime = @filemtime($cacheFile);
        if ($mtime === false) {
            return false;
        }

        return (time() - $mtime) < self::CACHE_TTL;
    }

    /**
     * Verifie si un fichier de cache existe (meme expire).
     */
    private function cacheExists(string $cacheFile): bool
    {
        return file_exists($cacheFile) && filesize($cacheFile) > 0;
    }

    /**
     * Lit le cache.
     *
     * @return array<string, mixed>|null
     */
    private function readCache(string $cacheFile): ?array
    {
        $raw = @file_get_contents($cacheFile);
        if ($raw === false) {
            return null;
        }

        $decoded = json_decode($raw, true);
        return is_array($decoded) ? $decoded : null;
    }

    /**
     * Ecrit le cache.
     *
     * @param array<string, mixed> $data
     */
    private function writeCache(string $cacheFile, array $data): bool
    {
        $encoded = json_encode($data, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
        if ($encoded === false) {
            return false;
        }

        // Ecriture atomique via fichier temporaire.
        $tmpFile = $cacheFile . '.tmp';
        if (@file_put_contents($tmpFile, $encoded, LOCK_EX) === false) {
            return false;
        }

        if (!@rename($tmpFile, $cacheFile)) {
            @unlink($tmpFile);
            return false;
        }

        return true;
    }

    /**
     * Log une erreur (vers error_log PHP par defaut).
     */
    private function logError(string $message): void
    {
        @error_log('[PrimClient] ' . $message);
    }

    /**
     * Retourne les infos de la derniere reponse HTTP (debug).
     *
     * @return array<string, mixed>|null
     */
    public function getLastResponse(): ?array
    {
        return $this->lastResponse;
    }

    /**
     * Force le vidage du cache (utile pour les tests).
     */
    public function clearCache(): void
    {
        $cacheFile = $this->cacheDir . '/disruptions.json';
        if (file_exists($cacheFile)) {
            @unlink($cacheFile);
        }
    }
}
