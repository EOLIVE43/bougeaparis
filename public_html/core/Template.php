<?php
/**
 * Classe Template
 *
 * Moteur de rendu PHP pur (pas de Twig/Blade, pour rester leger).
 * Gere layouts, partials et composants reutilisables.
 *
 * Supporte aussi des stylesheets additionnels par page (ex: line.css uniquement
 * sur les pages /metro/ligne-X/) via addStylesheet().
 */

class Template
{
    private string $page;
    private string $layout = 'base';
    private array $data = [];
    private array $extraStylesheets = [];
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
     * Ajoute une feuille de style supplementaire pour cette page,
     * injectee dans le <head> par le layout.
     *
     * Utile pour charger un CSS specifique uniquement quand la page le requiert
     * (ex: line.css ne charge que sur les pages ligne).
     */
    public function addStylesheet(string $href): self
    {
        if (!in_array($href, $this->extraStylesheets, true)) {
            $this->extraStylesheets[] = $href;
        }
        return $this;
    }

    public function getExtraStylesheets(): array
    {
        return $this->extraStylesheets;
    }

    /**
     * Retourne le CSS critical above-the-fold a inliner dans <style>.
     *
     * Convention : pour chaque addStylesheet('/assets/css/X.css'), on cherche
     * public_html/assets/css/critical-X.css (genere en CI par `critical@7`
     * dans deploy.yml, jamais commite au repo).
     *
     * Si AUCUN critical n'est trouve, retourne '' -> base.php tombe en
     * synchrone classique (comportement legacy preserve pour les pages
     * non encore optimisees : home, blog, lignes...).
     *
     * Si un critical est present, le layout passe en mode preload+swap
     * async (cf. base.php) : critical inline en <style>, le reste des CSS
     * (bundle + additionals) en preload non-blocking.
     */
    public function getCriticalCss(): string
    {
        $css = '';
        $cssDir = __DIR__ . '/../assets/css';
        foreach ($this->extraStylesheets as $href) {
            if (preg_match('|/assets/css/([a-z0-9-]+)\.css$|i', $href, $m)) {
                $file = $cssDir . '/critical-' . $m[1] . '.css';
                if (is_file($file)) {
                    $css .= file_get_contents($file);
                }
            }
        }
        return $css;
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
            'extra_stylesheets' => $this->extraStylesheets,
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
