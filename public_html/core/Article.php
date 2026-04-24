<?php

/**
 * Article
 *
 * Gestion des articles Markdown avec front matter.
 *
 * Format des fichiers attendus dans content/info-trafic/ ou content/guides/ :
 *
 * ---
 * title: Mon titre d'article
 * excerpt: Description courte
 * date: 2026-04-24
 * author: ludo
 * image: /content/info-trafic/images/mon-image.jpg
 * image_alt: Description de l'image
 * category: trafic
 * ---
 *
 * # Premier titre
 *
 * Contenu Markdown ici...
 *
 * Usage :
 *   $article = Article::load('info-trafic', '2026-04-24-bienvenue');
 *   $article->getTitle();       // string
 *   $article->getHtml();         // HTML rendu
 *   $article->getMeta('author'); // string
 */

class Article
{
    private array $meta = [];
    private string $markdown = '';
    private string $html = '';
    private string $section = '';
    private string $slug = '';

    /**
     * Charge un article depuis le filesystem.
     *
     * @param string $section 'info-trafic' ou 'guides'
     * @param string $slug    ex: '2026-04-24-bienvenue' (sans le .md)
     */
    public static function load(string $section, string $slug): ?self
    {
        $path = self::contentPath($section, $slug);
        if (!file_exists($path)) {
            return null;
        }

        $article = new self();
        $article->section = $section;
        $article->slug = $slug;
        $article->parse(file_get_contents($path));
        return $article;
    }

    /**
     * Retourne le chemin du fichier markdown.
     * content/ est HORS de public_html/ pour securite.
     */
    private static function contentPath(string $section, string $slug): string
    {
        // On remonte d'un niveau pour sortir de public_html/
        return __DIR__ . '/../../content/' . $section . '/' . $slug . '.md';
    }

    /**
     * Parse le contenu brut (front matter + markdown).
     */
    private function parse(string $raw): void
    {
        // Detection du front matter
        if (!preg_match('/^---\s*\n(.*?)\n---\s*\n(.*)$/s', $raw, $matches)) {
            // Pas de front matter : tout est du markdown
            $this->markdown = $raw;
            return;
        }

        $frontMatter = $matches[1];
        $this->markdown = $matches[2];

        // Parse du front matter (format simple : key: value)
        foreach (explode("\n", $frontMatter) as $line) {
            $line = trim($line);
            if ($line === '' || strpos($line, '#') === 0) continue;

            $colonPos = strpos($line, ':');
            if ($colonPos === false) continue;

            $key = trim(substr($line, 0, $colonPos));
            $value = trim(substr($line, $colonPos + 1));

            // Retire les guillemets simples/doubles
            if (preg_match('/^["\'](.*)["\']\s*$/', $value, $m)) {
                $value = $m[1];
            }

            $this->meta[$key] = $value;
        }
    }

    /**
     * Retourne le HTML parse du contenu Markdown.
     * Cache en memoire pour ne pas parser 2x.
     */
    public function getHtml(): string
    {
        if ($this->html === '') {
            $parsedown = new Parsedown();
            $parsedown->setSafeMode(true); // Bloque le HTML brut pour securite
            $this->html = $parsedown->text($this->markdown);
        }
        return $this->html;
    }

    // -------------------- Accesseurs meta --------------------

    public function getTitle(): string
    {
        return $this->meta['title'] ?? 'Sans titre';
    }

    public function getExcerpt(): string
    {
        return $this->meta['excerpt'] ?? '';
    }

    public function getDate(): string
    {
        return $this->meta['date'] ?? '';
    }

    /**
     * Date formatee pour affichage humain. Ex: "24 avril 2026"
     */
    public function getDateFormatted(): string
    {
        $date = $this->getDate();
        if (!$date) return '';

        $timestamp = strtotime($date);
        if (!$timestamp) return $date;

        $monthsAcc = [
            1 => 'janvier', 2 => 'février', 3 => 'mars', 4 => 'avril',
            5 => 'mai', 6 => 'juin', 7 => 'juillet', 8 => 'août',
            9 => 'septembre', 10 => 'octobre', 11 => 'novembre', 12 => 'décembre'
        ];

        $day = (int) date('j', $timestamp);
        $month = $monthsAcc[(int) date('n', $timestamp)];
        $year = date('Y', $timestamp);

        return "$day $month $year";
    }

    /**
     * Date ISO 8601 pour schema.org et meta tags.
     */
    public function getDateIso(): string
    {
        $date = $this->getDate();
        if (!$date) return '';
        $timestamp = strtotime($date);
        return $timestamp ? date('c', $timestamp) : '';
    }

    public function getAuthor(): string
    {
        return $this->meta['author'] ?? 'ludo';
    }

    /**
     * Retourne les infos de l'auteur depuis config/authors.php (s'il existe)
     * ou un fallback basique.
     */
    public function getAuthorInfo(): array
    {
        $authorSlug = $this->getAuthor();
        $fallback = [
            'ludo' => [
                'slug' => 'ludo',
                'name' => 'Ludo',
                'full_name' => 'Ludovic',
                'url' => '/auteur/ludo/',
                'bio' => 'Spécialiste des transports franciliens et des informations pratiques.',
            ],
            'elodie' => [
                'slug' => 'elodie',
                'name' => 'Élodie',
                'full_name' => 'Élodie',
                'url' => '/auteur/elodie/',
                'bio' => 'Passionnée de tourisme, de patrimoine et d\'histoire parisienne.',
            ],
        ];

        // Tente de charger depuis config/authors.php si existe
        try {
            $authors = Config::all('authors');
            if (isset($authors[$authorSlug])) {
                return $authors[$authorSlug];
            }
        } catch (Exception $e) {
            // Pas de config/authors.php, on utilise le fallback
        }

        return $fallback[$authorSlug] ?? $fallback['ludo'];
    }

    public function getImage(): string
    {
        return $this->meta['image'] ?? '';
    }

    public function getImageAlt(): string
    {
        return $this->meta['image_alt'] ?? $this->getTitle();
    }

    public function getCategory(): string
    {
        return $this->meta['category'] ?? '';
    }

    public function getSection(): string
    {
        return $this->section;
    }

    public function getSlug(): string
    {
        return $this->slug;
    }

    /**
     * URL canonique de l'article (sans le host).
     */
    public function getUrl(): string
    {
        return '/' . $this->section . '/' . $this->slug . '/';
    }

    /**
     * Temps de lecture estime (en minutes, base 200 mots/min).
     */
    public function getReadingTime(): int
    {
        $wordCount = str_word_count(strip_tags($this->getHtml()));
        return max(1, (int) ceil($wordCount / 200));
    }

    /**
     * Nombre de mots de l'article (hors HTML).
     */
    public function getWordCount(): int
    {
        return str_word_count(strip_tags($this->getHtml()));
    }

    /**
     * Retourne toute la meta sous forme de tableau.
     */
    public function getAllMeta(): array
    {
        return $this->meta;
    }

    /**
     * Meta generique (fallback).
     */
    public function getMeta(string $key, $default = null)
    {
        return $this->meta[$key] ?? $default;
    }
}
