# Système POI — architecture cross-lignes

État au **2026-05-07**, refactor v2.0.0.

## Vue d'ensemble

Un POI est un point d'intérêt (monument, musée, quartier, gare) référencé sur une ou plusieurs pages ligne (`/metro/ligne-X/`). Pour éviter doublons d'assets et incohérence visuelle entre lignes, les POIs accessibles depuis ≥ 2 lignes sont **mutualisés** dans un dossier `shared/` et référencés via un registre central.

## Structure des assets

```
public_html/assets/images/poi/
├── shared/                 ← POIs accessibles depuis ≥ 2 lignes
│   ├── tour-saint-jacques.webp
│   ├── tour-saint-jacques-thumb.webp
│   ├── gare-du-nord.webp
│   └── ... (~26 POIs)
├── monuments/              ← POIs single-ligne par catégorie
│   ├── notre-dame.webp     (Cité, ligne 4 uniquement)
│   └── ...
├── gares/
├── musees/
├── quartiers/
└── jardins/
```

**Règle** : un POI dont la station est desservie par ≥ 2 lignes du métro parisien → `shared/`. Sinon → catégorie thématique.

## Registre central — `public_html/data/poi-registry.json`

Source unique de vérité pour les POIs shared. Schéma :

```json
{
  "version": "1.0",
  "updated_at": "2026-05-07",
  "pois": {
    "tour-saint-jacques": {
      "name": "Tour Saint-Jacques",
      "asset": "shared/tour-saint-jacques.webp",
      "thumb": "shared/tour-saint-jacques-thumb.webp",
      "wikimedia_source": {
        "file": "Wikimedia Commons",
        "url": "https://commons.wikimedia.org/wiki/...",
        "author": "Cormac",
        "license": "CC BY-SA 2.0",
        "license_url": "https://creativecommons.org/licenses/by-sa/2.0",
        "fetched_at": "2026-05-06"
      },
      "stations": ["Châtelet"],
      "lines": ["metro-1", "metro-4", "metro-7", "metro-11", "metro-14"],
      "categories": ["monuments"],
      "alt": "Tour Saint-Jacques à Paris, station Châtelet",
      "source_line": "metro-4"
    }
  }
}
```

Le registre est **lu au runtime** par :
1. `scripts/fetch-poi-images.php` (mode `shared_asset`) — résolution de l'asset
2. `templates/pages/sources.php` — génération auto des attributions Wikimedia

## Modes supportés dans `poi-overrides.json`

```json
{
  "_format": {
    "skip":            "bool — pas d'image, fallback emoji",
    "shared_asset":    "bool — résout depuis poi-registry.json (registry_key)",
    "registry_key":    "string — clé dans pois{} du registre",
    "wikimedia_file":  "string — fichier Commons précis (bypass scoring)",
    "wikimedia_query": "string — query custom pour search",
    "wikimedia_blocklist": "array — termes à pénaliser",
    "local_image":     "bool — fichier WebP uploadé manuellement"
  },
  "tour-saint-jacques": {
    "shared_asset": true,
    "registry_key": "tour-saint-jacques",
    "_comment": "POI mutualisé via poi-registry.json"
  }
}
```

**Cascade des modes** dans `fetch-poi-images.php` (ordre d'évaluation) :
1. `skip` → pas d'image, cleanup destructif
2. `shared_asset` ⇐ **NOUVEAU** v2.0.0 — résout via registry, pas de fetch
3. `local_image` → utilise un fichier uploadé manuellement
4. `wikimedia_file` → forcer un fichier Commons précis
5. `wikimedia_query` + `wikimedia_blocklist` → search + scoring custom
6. (default) → search avec `$poi['name'] + ' Paris'`

## Diagramme de flux

```
Run workflow Fetch POI Images
        │
        ▼
fetch-poi-images.php charge poi-overrides.json
        │
        ▼
Pour chaque POI dans data/lines/metro-{N}.json :
        │
        ├── override "shared_asset" ? → loadPoiRegistry() → vérifie fichier physique → affecte $poi['image'] avec paths /shared/
        │
        ├── override "skip" ? → cleanup
        │
        ├── override "wikimedia_file" ? → fetch fichier précis
        │
        ├── override "wikimedia_query" ? → search custom
        │
        └── default → search "{poi.name} Paris"
        │
        ▼
Workflow GitHub Actions commit auto $poi['image'] dans metro-{N}.json
        │
        ▼
Page /metro/ligne-{N}/ rend $poi['image']['src']
```

## Procédure pour ajouter un nouveau POI shared

1. **Identifier** un POI accessible depuis ≥ 2 lignes (consulter `data/lines/metro-*.json` pour les correspondances officielles à la station du POI).
2. **Ajouter une entrée** dans `public_html/data/poi-registry.json` sous `pois.{slug}` avec : name, asset, thumb, wikimedia_source, stations, lines, categories, alt, source_line.
3. **Placer le fichier** physique dans `public_html/assets/images/poi/shared/{slug}.webp` (et `-thumb.webp` si workflow le génère). Soit via run Fetch POI ciblé, soit upload manuel cPanel.
4. **Ajouter un override** dans `poi-overrides.json` : `"{slug}": { "shared_asset": true, "registry_key": "{slug}" }`.
5. **Mettre à jour les JSON lignes** qui référencent ce POI : ajouter une entrée `points_of_interest[*].items[*]` avec le slug. L'`image.src` sera ré-affecté au prochain run du workflow Fetch POI.
6. Re-run workflow Fetch POI sur les lignes concernées (mode=apply, force=false suffit, le shared_asset bypasse le fetch).
7. Vérifier visuellement sur les pages ligne concernées + `/sources/` (attribution apparaît auto).

## Convention de nommage des slugs

- **kebab-case strict** : minuscules, tirets, pas d'apostrophes ni accents
- Exemple : `Gare de l'Est` → slug `gare-de-l-est` (et non `gare-de-lest`)
- Préserver la sémantique : `goutte-d-or` (apostrophe → tiret), `gare-de-l-est` (l' → l-)
- Pas d'espaces, pas de caractères spéciaux, pas de `_` (underscores)
- Cohérence avec `station_slug` dans les JSON ligne : aligner les conventions

## POIs single-ligne (non shared)

Restent dans la structure thématique actuelle :
```
public_html/assets/images/poi/{theme}/{slug}.webp
```

Pas d'override `shared_asset` requis. Le fetch normal s'applique.

Exemple : Notre-Dame (station Cité, ligne 4 uniquement) → `/poi/monuments/notre-dame.webp`.

## Page `/sources/` — attribution auto

Le template `templates/pages/sources.php` lit en cascade :
1. `poi-registry.json` — POIs shared (1 entrée par POI, pas par ligne)
2. JSON lignes — POIs solo + heros lignes
3. JSON stations — heros stations

Les credits Wikimedia (auteur, licence, URL, date) sont aggregés et affichés dans la section `#credits-photos` de la page `/sources/`. Plus jamais d'oubli d'attribution, mise à jour auto dès qu'un POI est ajouté.

## Logs et debug

Run `php scripts/fetch-poi-images.php --line=metro-4 --apply` :
```
→ Tour Saint-Jacques
  ↪  shared_asset → shared/tour-saint-jacques.webp (lignes : metro-1, metro-4, metro-7, metro-11, metro-14)
```

Erreurs explicites (pas de fallback silencieux) :
- `shared_asset : registry_key 'X' introuvable dans poi-registry.json`
- `shared_asset : fichier physique manquant : /assets/images/poi/shared/X.webp`

## Versioning

- **v1.x** : POIs ligne-par-ligne, fetch redondant, doublons assets
- **v2.0.0** (2026-05-07) : registre central, mode shared_asset, mutualisation 26 POIs, source unique pour /sources/
