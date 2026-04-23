<?php
/**
 * Classe SEO
 *
 * Gere l'ensemble des balises meta et donnees structurees (schema.org)
 * de chaque page. Permet de definir titre, description, images, breadcrumb,
 * type de page et d'emettre le bloc <head> complet.
 */

class Seo
{
    private array $data = [];
    private array $schemas = [];

    public function __construct()
    {
        $seoConfig = Config::all('seo');
        $this->data = [
            'title'       => $seoConfig['default_title'],
            'description' => $seoConfig['default_description'],
            'keywords'    => $seoConfig['default_keywords'],
            'canonical'   => null,
            'robots'      => $seoConfig['robots'],
            'og_type'     => $seoConfig['og_type'],
            'og_image'    => Config::get('site.url') . Config::get('site.og_image'),
            'og_locale'   => $seoConfig['og_locale'],
            'twitter_card'=> $seoConfig['twitter_card'],
            'article'     => null,
        ];
    }

    public function setTitle(string $title, bool $withSuffix = true): self
    {
        $suffix = $withSuffix ? Config::get('seo.title_suffix') : '';
        $this->data['title'] = $title . $suffix;
        return $this;
    }

    public function setDescription(string $desc): self
    {
        $this->data['description'] = $this->truncate($desc, 160);
        return $this;
    }

    public function setCanonical(string $path): self
{
    // Si l'argument est deja une URL complete (http/https), on l'utilise tel quel
    // Sinon on concatene avec l'URL du site
    if (str_starts_with($path, 'http://') || str_starts_with($path, 'https://')) {
        $this->data['canonical'] = $path;
    } else {
        $this->data['canonical'] = rtrim(Config::get('site.url'), '/') . $path;
    }
    return $this;
}

    public function setOgImage(string $url): self
    {
        $this->data['og_image'] = str_starts_with($url, 'http')
            ? $url
            : rtrim(Config::get('site.url'), '/') . $url;
        return $this;
    }

    public function setOgType(string $type): self
    {
        $this->data['og_type'] = $type;
        return $this;
    }

    /**
     * Pour un article de blog (NewsArticle)
     */
    public function setArticle(array $meta): self
    {
        $this->data['article'] = $meta;
        $this->setOgType('article');
        return $this;
    }

    /**
     * Ajoute un bloc de donnees structurees (schema.org)
     */
    public function addSchema(array $schema): self
    {
        $this->schemas[] = $schema;
        return $this;
    }

    /**
     * Raccourci : genere un BreadcrumbList schema.org
     */
    public function setBreadcrumb(array $items): self
    {
        $listItems = [];
        $i = 1;
        foreach ($items as $item) {
            $listItems[] = [
                '@type'    => 'ListItem',
                'position' => $i++,
                'name'     => $item['label'],
                'item'     => rtrim(Config::get('site.url'), '/') . $item['url'],
            ];
        }
        $this->addSchema([
            '@context'         => 'https://schema.org',
            '@type'            => 'BreadcrumbList',
            'itemListElement'  => $listItems,
        ]);
        return $this;
    }

    /**
     * Emet toutes les balises meta du <head>
     */
    public function renderHead(): string
    {
        $site = Config::all('site');
        $seo  = Config::all('seo');
        $d    = $this->data;
        $out  = '';

        $out .= '<title>' . htmlspecialchars($d['title'], ENT_QUOTES, 'UTF-8') . "</title>\n";
        $out .= '<meta name="description" content="' . htmlspecialchars($d['description'], ENT_QUOTES, 'UTF-8') . "\">\n";
        $out .= '<meta name="keywords" content="' . htmlspecialchars($d['keywords'], ENT_QUOTES, 'UTF-8') . "\">\n";
        $out .= '<meta name="robots" content="' . htmlspecialchars($d['robots'], ENT_QUOTES, 'UTF-8') . "\">\n";

        if ($d['canonical']) {
            $out .= '<link rel="canonical" href="' . htmlspecialchars($d['canonical'], ENT_QUOTES, 'UTF-8') . "\">\n";
        }

        // Open Graph
        $out .= '<meta property="og:title" content="' . htmlspecialchars($d['title'], ENT_QUOTES, 'UTF-8') . "\">\n";
        $out .= '<meta property="og:description" content="' . htmlspecialchars($d['description'], ENT_QUOTES, 'UTF-8') . "\">\n";
        $out .= '<meta property="og:type" content="' . htmlspecialchars($d['og_type'], ENT_QUOTES, 'UTF-8') . "\">\n";
        $out .= '<meta property="og:locale" content="' . htmlspecialchars($d['og_locale'], ENT_QUOTES, 'UTF-8') . "\">\n";
        $out .= '<meta property="og:site_name" content="' . htmlspecialchars($seo['og_site_name'], ENT_QUOTES, 'UTF-8') . "\">\n";
        if ($d['canonical']) {
            $out .= '<meta property="og:url" content="' . htmlspecialchars($d['canonical'], ENT_QUOTES, 'UTF-8') . "\">\n";
        }
        $out .= '<meta property="og:image" content="' . htmlspecialchars($d['og_image'], ENT_QUOTES, 'UTF-8') . "\">\n";

        // Twitter Card
        $out .= '<meta name="twitter:card" content="' . htmlspecialchars($d['twitter_card'], ENT_QUOTES, 'UTF-8') . "\">\n";
        $out .= '<meta name="twitter:title" content="' . htmlspecialchars($d['title'], ENT_QUOTES, 'UTF-8') . "\">\n";
        $out .= '<meta name="twitter:description" content="' . htmlspecialchars($d['description'], ENT_QUOTES, 'UTF-8') . "\">\n";
        $out .= '<meta name="twitter:image" content="' . htmlspecialchars($d['og_image'], ENT_QUOTES, 'UTF-8') . "\">\n";

        // Article-specifique (NewsArticle)
        if ($d['article']) {
            $a = $d['article'];
            if (!empty($a['published'])) {
                $out .= '<meta property="article:published_time" content="' . htmlspecialchars($a['published'], ENT_QUOTES, 'UTF-8') . "\">\n";
            }
            if (!empty($a['modified'])) {
                $out .= '<meta property="article:modified_time" content="' . htmlspecialchars($a['modified'], ENT_QUOTES, 'UTF-8') . "\">\n";
            }
            if (!empty($a['author'])) {
                $out .= '<meta property="article:author" content="' . htmlspecialchars($a['author'], ENT_QUOTES, 'UTF-8') . "\">\n";
            }
            if (!empty($a['section'])) {
                $out .= '<meta property="article:section" content="' . htmlspecialchars($a['section'], ENT_QUOTES, 'UTF-8') . "\">\n";
            }
        }

        // Schemas JSON-LD
        foreach ($this->schemas as $schema) {
            $out .= '<script type="application/ld+json">'
                 . json_encode($schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE)
                 . "</script>\n";
        }

        return $out;
    }

    private function truncate(string $text, int $maxLen): string
    {
        if (mb_strlen($text) <= $maxLen) return $text;
        return mb_substr($text, 0, $maxLen - 1) . '…';
    }
}
