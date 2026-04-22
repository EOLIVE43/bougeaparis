# BougeaParis.fr

Guide independant des transports en commun a Paris et en Ile-de-France.

> **Se deplacer. Visiter.**

## Stack technique

- **Langage** : PHP 8.1+ pur (pas de framework lourd)
- **Hebergement** : o2switch (heure.o2switch.net)
- **Donnees** : JSON statique + API PRIM (Ile-de-France Mobilites)
- **Blog** : articles en Markdown versionnes sur GitHub
- **Recherche** : cote client avec MiniSearch (sans base de donnees)
- **Deploiement** : GitHub Actions -> FTP o2switch
- **Design** : CSS natif avec design tokens, pas de framework

## Architecture

```
bougeaparis/
|
|-- .github/
|   `-- workflows/
|       `-- deploy.yml         # Deploiement automatique vers o2switch
|
|-- public_html/                # Dossier deploye sur le serveur
|   |
|   |-- index.php               # Front controller unique
|   |-- .htaccess               # URLs propres + cache + securite
|   |-- robots.txt
|   |-- sitemap.xml
|   |
|   |-- config/
|   |   |-- site.php            # Nom, slogan, logo, URL, couleurs
|   |   |-- nav.php             # Menus header + footer
|   |   |-- seo.php             # Parametres SEO par defaut
|   |   |-- ads.php             # Config AdSense (desactive par defaut)
|   |   |-- authors.php         # Ludo + Elodie
|   |   |-- app.php             # API, cache, timezone
|   |   |-- secrets.example.php # Template cles API (a copier en secrets.php sur serveur)
|   |   `-- secrets.php         # [A CREER SUR LE SERVEUR - non commite]
|   |
|   |-- core/                   # Classes du noyau PHP
|   |   |-- bootstrap.php       # Autoload + helpers globaux
|   |   |-- Config.php          # Chargement config
|   |   |-- Template.php        # Moteur de rendu
|   |   `-- Seo.php             # Balises meta + schema.org
|   |
|   |-- templates/              # Vues (HTML/PHP pur)
|   |   |-- layout/
|   |   |   |-- base.php        # Squelette HTML complet
|   |   |   |-- header.php      # Logo + menu
|   |   |   `-- footer.php      # 4 colonnes + mention non-officiel
|   |   |-- components/         # Composants reutilisables (a venir)
|   |   |-- pages/
|   |   |   |-- home.php
|   |   |   |-- metro-hub.php
|   |   |   |-- rer-hub.php
|   |   |   |-- bus-hub.php
|   |   |   |-- tramway-hub.php
|   |   |   |-- aeroports-hub.php
|   |   |   |-- transilien-hub.php
|   |   |   |-- blog-index.php
|   |   |   |-- about.php
|   |   |   |-- contact.php
|   |   |   |-- legal.php
|   |   |   |-- privacy.php
|   |   |   |-- author-ludo.php
|   |   |   |-- author-elodie.php
|   |   |   `-- 404.php
|   |   `-- ads/
|   |       |-- slot-header.php
|   |       |-- slot-in-article.php
|   |       |-- slot-sidebar.php
|   |       `-- slot-footer.php
|   |
|   |-- assets/
|   |   |-- css/
|   |   |   |-- tokens.css      # Variables (couleurs, typo, espacements)
|   |   |   |-- base.css        # Reset + typographie
|   |   |   |-- layout.css      # Header, footer, grilles
|   |   |   |-- components.css  # Boutons, cards, badges
|   |   |   `-- ads.css
|   |   |-- js/
|   |   |   `-- main.js         # Menu burger + base JS
|   |   `-- img/
|   |       |-- logo/           # logo.svg, favicon.svg, logo-compact.svg
|   |       `-- authors/        # ludo.svg, elodie.svg
|   |
|   |-- data/                   # JSON statiques (lignes, stations, POI)
|   |
|   |-- api/
|   |   |-- cache/              # Cache fichiers (non commite)
|   |   |-- prim-proxy.php      # [Livraison 4]
|   |   |-- autocomplete.php    # [Livraison 4]
|   |   `-- itinerary.php       # [Livraison 4]
|   |
|   `-- [dossiers pour URLs hubs : /metro/, /rer/, /bus/, etc.]
|
|-- .gitignore
`-- README.md
```

## Installation initiale

### 1. Cloner le repo en local

```bash
git clone git@github.com:VOTRE-USERNAME/bougeaparis.git
cd bougeaparis
```

### 2. Configurer les secrets sur GitHub

Aller dans **Settings > Secrets and variables > Actions** du repo GitHub et creer ces 3 secrets :

| Nom du secret | Valeur |
|---|---|
| `FTP_SERVER` | `heure.o2switch.net` |
| `FTP_USERNAME` | `deploy-github@bougeaparis.fr` |
| `FTP_PASSWORD` | [le mot de passe FTP genere dans cPanel o2switch] |

### 3. Configurer la cle API PRIM sur le serveur

La cle API PRIM ne doit **JAMAIS** etre commitee sur GitHub. Elle doit etre creee **directement sur le serveur** via FTP (une seule fois).

**Procedure :**

1. Se connecter en FTP a o2switch (via FileZilla, Cyberduck, ou cPanel > Gestionnaire de fichiers)
2. Aller dans `/public_html/config/`
3. Copier le fichier `secrets.example.php` en `secrets.php` (meme dossier)
4. Editer `secrets.php` et remplacer `COLLER_ICI_VOTRE_CLE_API_PRIM` par votre vraie cle API
5. Sauvegarder

Contenu du fichier `secrets.php` a creer :

```php
<?php
return [
    'prim_api_key' => 'votre-cle-api-prim-ici',
    'navitia_api_key' => '',
];
```

### 4. Creer le dossier de cache avec permissions

Via FTP ou cPanel, creer le dossier `public_html/api/cache/` s'il n'existe pas et s'assurer qu'il est en chmod 755 (ecriture par le serveur).

### 5. Premier deploiement

```bash
git add .
git commit -m "Initial commit - Livraison 1"
git push origin main
```

Le workflow GitHub Actions va se declencher automatiquement et deployer le site sur o2switch via FTP. Suivre l'avancement dans l'onglet **Actions** de GitHub.

Apres 1 a 2 minutes, le site est en ligne sur https://bougeaparis.fr.

## Developpement local

Pour travailler en local, il faut un serveur PHP. Le plus simple :

```bash
cd public_html
php -S localhost:8000
```

Puis ouvrir http://localhost:8000 dans le navigateur.

## Activer AdSense

Lorsque vous serez pret a monetiser le site :

1. Obtenir votre Publisher ID AdSense (ca-pub-xxx)
2. Ouvrir `public_html/config/ads.php`
3. Passer `enabled` a `true`
4. Coller votre Publisher ID dans `publisher_id`
5. Creer vos emplacements publicitaires sur Google AdSense et coller chaque `slot_id`
6. Commit + push -> les pubs apparaissent automatiquement sur tout le site

## Respect du cahier des charges

### Architecture decouplee

- **Contenu** : dans `config/` et `data/` (modifiables sans toucher au design)
- **Presentation** : dans `assets/css/` et `templates/`
- **Code** : dans `core/` et `index.php`
- Aucun style inline, aucun texte en dur dans les templates

### Monetisation AdSense

- 4 emplacements pre-cables : header, in-article, sidebar, footer
- Activation en modifiant un seul fichier (`config/ads.php`)
- Invisible tant qu'il n'est pas active

### SEO et Google Discover

- HTTPS force via .htaccess
- URLs propres et descriptives
- Balises meta completes sur chaque page (title, description, OG, Twitter, canonical)
- `max-image-preview:large` pour Google Discover
- Schema.org sur toutes les pages (WebSite, Organization, BreadcrumbList, Person pour auteurs)
- Sitemap.xml
- Mobile-first (responsive design)
- Performance optimisee (cache navigateur 1 an pour assets, gzip)
- Pages E-E-A-T : A propos, Contact, Mentions legales, Confidentialite, pages auteurs
- Accessibilite (skip-link, aria-labels, semantique HTML5)

## Charte visuelle

- **Couleur principale** : `#0F6E56` (teal)
- **Couleur hover** : `#085041`
- **Fond clair** : `#E1F5EE`
- **Police** : system-ui (stack native)
- **Couleurs des lignes** : couleurs officielles IDFM (donnees publiques)

## Roadmap

- [x] **Livraison 1** : Noyau, structure, 6 pages hubs, SEO, deploiement
- [ ] **Livraison 2** : Widget recherche itineraire + home enrichie
- [ ] **Livraison 3** : Proxy PRIM + autocomplete + itineraires
- [ ] **Livraison 4** : Cocon Metro (16 lignes + stations)
- [ ] **Livraison 5** : Blog Markdown + generation auto quotidienne
- [ ] **Livraison 6** : Cocons RER, Bus, Tram, Aeroports, Transilien

## Licence

(c) BougeaParis.fr - Site independant. Tous droits reserves.
