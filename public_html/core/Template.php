<?php
/**
 * Classe Template
 *
 * Moteur de rendu PHP pur (pas de Twig/Blade, pour rester leger).
 * Gere layouts, partials et composants reutilisables.
 */

class Template
{
    private string $page;
    private string $layout = 'base';
    private array $data = [];
    public Seo $seo;

    public function __construct(string $page)
    {
        $this->page = $page;
        $this->seo  = new Seo();
    }

    public function with(string $key, $value): self
    {
        $this->data[$key] = $value;
        return $this;
    }

    public function withData(array $data): self
    {
        $this->data = array_merge($this->data, $data);
        return $this;
    }

    public function setLayout(string $layout): self
    {
        $this->layout = $layout;
        return $this;
    }

    /**
     * Retourne les donnees globales injectees dans tous les templates
     */
    private function globalData(): array
    {
        return [
            'site' => Config::all('site'),
            'nav'  => Config::all('nav'),
            'ads'  => Config::all('ads'),
            'analytics' => Config::all('analytics'),

        ];
    }

    /**
     * Partial : inclut un fichier de template avec des donnees
     */
    public function partial(string $path, array $data = []): void
{
    $fullPath = __DIR__ . '/../templates/' . $path . '.php';
    if (!file_exists($fullPath)) {
        throw new RuntimeException("Template introuvable : $path");
    }
    // Donnees globales (site, nav, ads) + donnees du template
    extract(array_merge($this->globalData(), $this->data), EXTR_SKIP);
    $tpl = $this;
    $seo = $this->seo;
    // Les props specifiques du partial sont passees dans $props
    $props = $data;
    include $fullPath;
}

    /**
     * Rendu d'un composant (avec son propre scope)
     */
    public static function component(string $name, array $props = []): void
    {
        $path = __DIR__ . '/../templates/components/' . $name . '.php';
        if (!file_exists($path)) {
            throw new RuntimeException("Composant introuvable : $name");
        }
        extract($props, EXTR_SKIP);
        include $path;
    }

    /**
     * Rendu complet : layout + page
     */
    public function render(): void
    {
        // Capture du contenu de la page
        ob_start();
        $this->partial('pages/' . $this->page);
        $content = ob_get_clean();

        // Donnees globales dispo dans le layout
        $data = array_merge($this->globalData(), $this->data, [
            'content' => $content,
        ]);

        extract($data, EXTR_SKIP);
        $tpl = $this;
        $seo = $this->seo;
        include __DIR__ . '/../templates/layout/' . $this->layout . '.php';
    }

    /**
     * Echappement HTML (helper)
     */
    public static function e(?string $s): string
    {
        return htmlspecialchars($s ?? '', ENT_QUOTES, 'UTF-8');
    }

    /**
     * URL absolue depuis un chemin relatif
     */
    public static function url(string $path = '/'): string
    {
        return rtrim(Config::get('site.url'), '/') . $path;
    }

    /**
     * Asset URL (avec versioning cache-busting possible plus tard)
     */
    public static function asset(string $path): string
    {
        return $path;
    }
}
