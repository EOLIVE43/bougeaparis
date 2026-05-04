# BougeaParis.fr — Guide Claude Code

Site PHP custom (pas de framework) qui édite un guide indépendant des transports en commun en Île-de-France (métro, RER, bus, tramway, aéroports, Transilien, gares). Stratégie SEO forte : un cocon par mode + page détail par ligne + page station mutualisée.

> Le `README.md` contient l'historique de livraisons et la procédure de déploiement (FTP o2switch via GitHub Actions). Ce fichier-ci est l'aide-mémoire d'**architecture**.

## Stack

- PHP 8.1+ pur, sans framework
- Front controller unique : `public_html/index.php`
- Données : JSON statiques dans `public_html/data/` + (à terme) API PRIM
- CSS natif avec design tokens, bundle unique `bundle.css` + CSS additionnels par page
- JS minimal (`assets/js/main.js` pour le burger menu, etc.)
- Markdown (Parsedown) pour le blog `info-trafic`
- Hébergement : o2switch ; déploiement : GitHub Actions → FTP

## Arborescence

```
public_html/
├── index.php              # Front controller (routing + bootstrap)
├── core/                  # Classes du noyau + helpers globaux
│   ├── bootstrap.php      # Autoload PSR-0 simple + helpers globaux courts (e, url, asset, component)
│   ├── helpers.php        # Helpers métier transport (dateFr, pastilleCorresp, getLineSchedule)
│   ├── Config.php         # Config::get('site.brand_name'), Config::all('nav')
│   ├── Template.php       # Moteur de rendu (layouts, partials, components, addStylesheet)
│   ├── Seo.php            # <head>, OG, Twitter, schema.org
│   ├── Routes.php         # Registre des routes actives + helpers conditionalLink*
│   ├── Article.php        # Articles Markdown (info-trafic)
│   ├── Parsedown.php      # Markdown vendored
│   ├── PrimClient.php     # Client API PRIM (IDFM)
│   ├── DisruptionFilter / DisruptionFormatter   # Trafic temps réel
│   └── ClaudeClient / ArticlePrompt / AngleRotator   # Génération auto blog
├── config/                # Tableaux PHP retournés par require
│   ├── site.php nav.php seo.php ads.php authors.php app.php analytics.php
│   ├── line-mapping.php networks.php angles.php
│   ├── cocons/{slug}.php  # Contenu éditorial des hubs (metro, rer, bus, ...)
│   └── secrets.php        # NON commité, créé sur le serveur
├── data/                  # JSON statiques
│   ├── lines.json                  # Liste résumée des lignes (pour les hubs)
│   ├── lines/{slug}.json           # Détail riche d'une ligne (ex: metro-1.json — ~2000 lignes)
│   ├── stations/{slug}.json        # Détail simple d'une station (ex: chatelet.json — ~90 lignes)
│   ├── gares/{slug}.json           # Détail des 7 grandes gares parisiennes
│   ├── poi-overrides.json tarifs.json
│   └── traffic/                    # Cache trafic
├── templates/
│   ├── layout/{base,header,footer}.php
│   ├── pages/             # Une page = un fichier (home.php, hub-metro.php, line-metro.php, ...)
│   ├── components/        # Composants réutilisables
│   │   ├── breadcrumb.php hero-cocon.php traffic-widget.php line-badge.php
│   │   ├── line-grid-{metro,rer,bus,tram,transilien}.php airport-grid.php
│   │   ├── line/          # 16 sections d'une page ligne (hero, horaires, faq, ...)
│   │   └── station/       # Sections d'une page station (horaires-par-ligne, ...)
│   ├── partials/          # Petits bouts (line-search-widget, traffic-banner)
│   └── ads/               # 4 emplacements AdSense (header, in-article, sidebar, footer)
├── assets/{css,js,img}/
└── api/                   # Endpoints AJAX / proxy PRIM
content/info-trafic/       # Articles blog en Markdown (YYYY-MM-DD-slug.md)
scripts/                   # Scripts CLI (build, génération auto, ...)
```

## Conventions de code

- **PHP strict** : `declare(strict_types=1)` au top des fichiers principaux.
- **Style** : pas de PSR-12 strict, mais cohérent. Indent 4 espaces, accolades K&R, snake_case pour variables/fonctions globales, PascalCase pour classes.
- **Toujours échapper** : `e($var)` ou `htmlspecialchars(...)` pour tout output utilisateur. Les helpers sortent du HTML déjà échappé.
- **Commentaires** : docblocks PHPDoc en tête de fichier décrivant les props attendues. Commentaires en français OK.
- **Pas de framework** : pas de Composer, pas de namespaces (autoload simple sur `core/<ClassName>.php`).
- **Charset/timezone** : fixés dans `bootstrap.php` (UTF-8, Europe/Paris).

## Moteur de rendu (`Template`)

Cycle classique : route → `new Template($pageName)` → `withData([...])` → `render()`.

```php
$tpl = new Template('line-metro');
$tpl->withData(['line' => $lineData]);
$tpl->addStylesheet('/assets/css/line.css'); // CSS additionnel pour cette page
$tpl->seo->setTitle(...)->setDescription(...)->setCanonical(...);
$tpl->render();
```

`render()` charge `templates/layout/base.php` qui inclut header, `$content` (la page), footer.

### Partials et props : pattern à RETENIR

Dans une page ou un layout :

```php
<?php $tpl->partial('components/line/hero', ['line' => $line]); ?>
```

Dans le partial cible (`templates/components/line/hero.php`) :

```php
<?php
// Les props passées sont disponibles dans $props
$line = $props['line'];
// $tpl, $seo, $site, $nav, $ads, $analytics sont aussi extraits automatiquement
?>
```

Détails de `Template::partial()` :
- Toutes les données globales (`site`, `nav`, `ads`, `analytics`) + `$this->data` sont `extract()`-ées dans le scope.
- Les **props locaux** passées en 2ᵉ argument arrivent dans une variable `$props` (pas `extract()`-ée — pour éviter les collisions avec les data globales). Les composants doivent donc lire `$props['xxx']`.
- `$tpl` et `$seo` sont aussi disponibles dans le partial.

### Components vs partials

- `$tpl->partial('path', $data)` — hérite du contexte global (site, nav, etc.) ET reçoit `$props`. Utilisé pour la majorité des sections de page.
- `Template::component('name', $props)` (ou helper global `component('name', $props)`) — scope **isolé**, chaque clé de `$props` est extraite directement comme variable locale (`$props` n'existe pas ici). Utilisé plus rarement.

Quand tu crées un composant, choisis : besoin du contexte global ? → `partial()`. Sinon → `component()`.

## Données

### `data/lines/{slug}.json` — très riche

Format `metro-1.json` : ~2000 lignes, sert à générer la page `/metro/ligne-1`. Sections principales :
- Identité ligne : `code`, `mode`, `color`, `color_text`, `terminus_a/b`, `stations_count`, `length_km`, `daily_riders`, `automated`, `opened_year`
- `seo` : `h1`, `title`, `description`, `lead`
- `intros` : 16 paragraphes d'intro SEO (un par section : `introduction`, `plan`, `stations`, `horaires`, `trafic`, `itineraires`, `que_voir`, `histoire`, `accessibilite`, `tarifs`, `travaux`, `faq`, `articles_lies`, `liens_internes`)
- `schedule` : premier/dernier départ par jour, fréquences (peak/off-peak/evening/weekend)
- `stations` : liste ordonnée avec correspondances + accessibilité PMR
- `popular_routes` : itinéraires populaires (avec `from`, `to`, `duration_min`, `transfers`, `lines`)
- `tourism` : POI le long de la ligne (avec station la plus proche, photo, auteur, crédit)
- `accessibility`, `tarifs`, `travaux`, `faq`, `history`, `articles`, `meta` (auteur principal, dates `published`/`updated`)

→ Les pages ligne assemblent **16 composants** dans `components/line/` qui consomment chacun une sous-section de ce JSON.

### `data/stations/{slug}.json` — plus simple

Format `chatelet.json` : ~90 lignes. Champs principaux :
- Identité : `slug`, `name`, `name_full`, `arrondissement`, `address`, `latitude`, `longitude`
- `lines` : lignes métro qui desservent la station (`type`, `code`, `slug`, `color`, `text_color`)
- `rer_correspondences` : RER avec `walking_minutes`
- `hero` : `tagline`, `description`
- `adjacent_stations` : par slug de ligne, `previous`/`next` (nom, slug, direction)
- `intro_paragraphs`, `faq`, `practical_tips`, `history`

→ Les horaires des stations ne sont **pas dupliqués** : ils sont récupérés via `getLineSchedule($lineSlug)` qui lit `data/lines/{slug}.json` (cache mémoire intra-requête).

### `data/lines.json`

Liste résumée de toutes les lignes (pour les hubs). Bien plus léger que les fichiers individuels.

## Routing (`index.php`)

Switch sur `$path` :

- `/` → home
- `/metro`, `/rer`, `/bus`, `/tramway`, `/aeroports`, `/transilien`, `/gares` → `bp_render_hub($slug)` qui charge `config/cocons/{slug}.php` + `data/lines.json`
- `/metro/ligne-{code}` (regex) → `bp_render_line('metro', $code)` qui charge `data/lines/metro-{code}.json`
- `/metro/station/{slug}` (regex) → charge `data/stations/{slug}.json` → `station-metro.php`. **URL canonique unique par station** (Châtelet a UNE seule URL même si 5 lignes la desservent → évite duplicate content)
- `/gare/{slug}` → `data/gares/{slug}.json`
- `/info-trafic` + `/info-trafic/{YYYY-MM-DD-slug}` → articles Markdown via `Article::load()`
- Pages éditoriales (`/a-propos`, `/contact`, `/mentions-legales`, `/confidentialite`, `/auteur/ludo`, `/auteur/elodie`)
- Fallback → `bp_render_404()`

## SEO (`Seo` class)

Chaque page configure son SEO **dans le template page** (pas le layout) :

```php
$tpl->seo
    ->setTitle('Métro Ligne 1')        // suffixe automatique de seo.title_suffix
    ->setDescription($lead)
    ->setCanonical('/metro/ligne-1')
    ->setOgType('article')
    ->setBreadcrumb([                  // génère schema.org BreadcrumbList ET breadcrumb visuel à part
        ['label' => 'Accueil', 'url' => '/'],
        ['label' => 'Métro',   'url' => '/metro/'],
        ['label' => 'Ligne 1', 'url' => '/metro/ligne-1'],
    ])
    ->addSchema([ /* JSON-LD libre */ ]);
```

`renderHead()` sort title, description, robots, canonical, OG, Twitter Card, blocs `<script type="application/ld+json">`.

Le `layout/base.php` injecte aussi 2 blocs JSON-LD globaux (Organization + WebSite) sur toutes les pages.

Le breadcrumb visuel est rendu en plus via `components/breadcrumb.php` (passer le même tableau d'items).

### CSS dédié par page

`$tpl->addStylesheet('/assets/css/line.css')` charge un CSS supplémentaire **uniquement** sur cette page (en plus de `bundle.css` chargé partout). Pattern utilisé pour `line.css`, `station.css` qui sinon polluraient le bundle.

## Liens internes — `Routes` (très important)

`Routes::exists($url)` retourne `true` si l'URL pointe vers une page effectivement servie. Liste blanche maintenue à la main dans `Routes::$active` + `$activeStationSlugs` + `$activeGareSlugs`.

**Stratégie SEO** : on pose tous les liens internes **dès maintenant** (cocon complet), même vers des pages futures. Les helpers retournent un `<a>` cliquable si la route existe, sinon un `<span class="...--inactive">` avec `data-future-url`. Aucune réécriture nécessaire le jour où la page est créée → il suffit d'ajouter le slug dans `Routes`.

```php
echo conditionalLink('/metro/station/concorde/', 'Concorde', 'station-link');
echo conditionalLinkOpen($url, 'card');  echo "..."; echo conditionalLinkClose($url);
echo stationLink('Châtelet');           // sucre : Routes::stationUrl + conditionalLink
```

`Routes::stationSlug($name)` translittère un nom de station vers son slug canonique (`"Hôtel de Ville"` → `"hotel-de-ville"`, retire les parenthèses, etc.).

## Helpers globaux à connaître

Tous chargés via `bootstrap.php` puis `helpers.php`.

- `e($s)` — `htmlspecialchars` court
- `url($path)` — URL absolue depuis chemin relatif (`Config::get('site.url')` + path)
- `asset($path)` — wrapper assets (cache-busting futur)
- `component($name, $props)` — alias `Template::component()`
- `dateFr($date = null, $format = 'long_with_day')` — date FR sans `strftime` (`"vendredi 2 mai 2026"` ou `"2 mai 2026"` avec `'short'`). Locale-safe, indépendant de l'hébergeur.
- `pastilleCorresp($mode, $line, $color, $size = 'default')` — SVG inline réutilisable pour pastille de correspondance ligne. `$mode` : `"M"`/`"RER"`/`"T"`/`"TRANS"`. `$size` : `small`/`inline`/`default`/`large`.
- `getLineSchedule($lineSlug)` — charge la section `schedule` de `data/lines/{slug}.json`, cachée en mémoire. Évite la duplication d'horaires dans les JSON station.
- `conditionalLink* / stationLink` — voir section Routes ci-dessus.

## Configuration

`Config::get('site.url')`, `Config::all('nav')`. Notation pointée jusqu'à profondeur arbitraire. Les fichiers `config/*.php` retournent un `array`.

`secrets.php` n'est **jamais** commité : créé directement sur le serveur (FTP) à partir de `secrets.example.php`. Contient la clé API PRIM.

## Particularités à retenir

1. **Pas de framework, pas de Composer** : si tu veux ajouter un `vendor/`, repense d'abord (Parsedown est vendored manuellement).
2. **JSON = source de vérité** : ne pas dupliquer les données dans les templates. Les pages station tirent leurs horaires des JSON ligne via `getLineSchedule()`.
3. **Mode/code en minuscules** dans les slugs : `metro-1`, `metro-3bis`, `rer-a`. URLs en minuscules (`/metro/ligne-1`).
4. **URLs canoniques** : une station = une URL, peu importe le nombre de lignes (anti duplicate content).
5. **Liens conditionnels partout** : cocon SEO posé en avance, activation par ajout de slug dans `Routes`.
6. **CSS bundle + CSS dédié** : `bundle.css` global, `addStylesheet()` pour CSS lourd spécifique à un type de page.
7. **AdSense désactivé par défaut** (`config/ads.php`), 4 slots déjà câblés, activation par flag.
8. **Analytics lazy** : GA4 chargé après interaction utilisateur ou 5s, derrière Consent Mode v2.
9. **Pages ligne = 16 sections** assemblées dans `pages/line-metro.php` à partir de `components/line/*.php`. Chaque composant prend `['line' => $line]` en prop.
10. **Tout est en français** : commentaires, contenus, noms de variables métier (`$ligneCode`, `$pastille`...). Les classes/méthodes du noyau restent en anglais.
