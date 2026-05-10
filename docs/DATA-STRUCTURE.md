# Architecture des données station — BougeaParis.fr

## Philosophie : data canonique flat + presentation par URL

> **Une station = un fichier JSON unique** dans `data/stations/{slug}.json`,
> contenant **TOUS les modes** desservis (métro + RER + Tramway + Transilien
> + Bus). Les **URLs publiques** restent organisées **par mode** pour le SEO.

### Pourquoi flat (et pas indexé par ligne)

BougeaParis.fr est un site **multimodal**, pas seulement métro. Une station
comme **Châtelet** (5 lignes métro + 3 RER) ou **La Défense** (1 métro + 2
RER + 1 tramway + 2 Transilien) est une **entité unique géographique**, pas
N copies indexées par ligne.

Pattern aligné sur les standards de l'industrie :
- **Wikipedia** : 1 article par station, indépendant de la ligne
- **Wikidata** : 1 entité Q par station (Q216357 = Grande Arche, peu importe
  qu'elle soit servie par L1, RER A, T2…)
- **IDFM** / **RATP** : station = entité primaire dans leurs API publiques

### Structure du fichier JSON

```
public_html/
└── data/
    └── stations/
        ├── chatelet.json                    ← 1 fichier, 5 lignes métro + 3 RER
        ├── la-defense-grande-arche.json     ← 1 fichier, métro + 2 RER + tram + 2 Transilien
        ├── charles-de-gaulle-etoile.json    (futur)
        └── ...
```

**0 sous-dossier par ligne**. Le path d'un JSON station est canonique :
`data/stations/{slug}.json` — quel que soit le nombre de modes desservis.

## Format JSON station

Chaque JSON station contient (champs principaux) :

| Champ | Type | Description |
|---|---|---|
| `slug` | string | Slug canonique unique (`chatelet`, `la-defense-grande-arche`) |
| `name` | string | Nom court (`Châtelet`, `La Défense`) |
| `name_full` | string | Nom complet pour H1 (`Châtelet — Métro & RER`) |
| `arrondissement` / `commune` | string | Localisation administrative |
| `address` | string | Adresse postale principale |
| `latitude`, `longitude` | float | GPS (WGS84) |
| `tariff_zone` | int 1-5 | Zone tarifaire IDFM |
| `is_major_hub` | bool | Hub majeur (active le bloc maillage « hubs similaires ») |
| `lines` | array | **Lignes métro** desservant la station (code, slug, color) |
| `rer_correspondences` | array | RER desservant la station (code, walking_minutes) |
| `tram_correspondences` | array | Tramways (code, walking_minutes, destinations) |
| `transilien_correspondences` | array | Transilien SNCF (code, destinations) |
| `bus_correspondences` | object | `{ diurne: [], nocturne: [], regional: [] }` |
| `adjacent_stations` | object | Indexé par slug ligne : `{prev: {...}, next: {...}}` |
| `hero` | object | tagline + description (rendu hero) |
| `hero_image` | object | url Wikimedia + alt + author + license + local_versions (si générés) |
| `intro_paragraphs` | array | 3 paragraphes SEO |
| `services` | object | wifi / toilets / atm / ratp_office / left_luggage / shopping_dining (structuré pour personnalisation contenu) |
| `safety` | object | level / agents / police / tips / notes |
| `nearby_pois` | array | POIs Wikidata avec image_url locale + crédits |
| `popular_itineraries` | array | 6-8 destinations populaires avec lignes/durée/changements |
| `exits` | array | Sorties numérotées avec address_full + sector |
| `exit_sectors` | object | Regroupement sectoriel des sorties |
| `history.title` / `history.paragraphs` | object | Histoire de la station |
| `trivia` | array | « Le saviez-vous » (5-6 anecdotes) |
| `faq` | array | 8-12 questions/réponses |
| `practical_tips` | array | 3-5 conseils voyageur |
| `accessibility` | object | Audit PMR (audit_status: verified/pending) |
| `i18n` | object | `{en: null, es: null}` (anticipation traductions, voir `docs/I18N-STRATEGY.md`) |

Tous les champs sauf `slug`, `name`, `latitude`, `longitude`, `lines` sont
optionnels. Les composants templates skippent proprement si vide.

### Exemple : Châtelet (multi-lignes centrales)

```json
{
  "slug": "chatelet",
  "name": "Châtelet",
  "name_full": "Châtelet — Métro & RER",
  "arrondissement": "1er",
  "commune": "Paris (75001)",
  "tariff_zone": 1,
  "is_major_hub": true,
  "latitude": 48.8585,
  "longitude": 2.347,
  "lines": [
    {"type": "metro", "code": "1",  "slug": "metro-1",  "color": "#FFCD00"},
    {"type": "metro", "code": "4",  "slug": "metro-4",  "color": "#A0006E"},
    {"type": "metro", "code": "7",  "slug": "metro-7",  "color": "#F19FBA"},
    {"type": "metro", "code": "11", "slug": "metro-11", "color": "#704B1C"},
    {"type": "metro", "code": "14", "slug": "metro-14", "color": "#62259D"}
  ],
  "rer_correspondences": [
    {"code": "A", "color": "#E2231A", "walking_minutes": 3},
    {"code": "B", "color": "#5291CE", "walking_minutes": 3},
    {"code": "D", "color": "#02864B", "walking_minutes": 3}
  ],
  ...
}
```

Note : Châtelet n'a pas de `tram_correspondences`, `transilien_correspondences`
ni `bus_correspondences` (pas de bus à proprement parler à cette station
souterraine). Champs absents → blocs skip propre côté template.

### Exemple : La Défense (terminus multimodal)

```json
{
  "slug": "la-defense-grande-arche",
  "name": "La Défense",
  "name_full": "La Défense — Grande Arche",
  "commune": "Puteaux (92)",
  "tariff_zone": 3,
  "is_major_hub": true,
  "lines": [
    {"type": "metro", "code": "1", "slug": "metro-1", "color": "#FFCD00"}
  ],
  "rer_correspondences": [
    {"code": "A", "color": "#E2231A", "walking_minutes": 2},
    {"code": "E", "color": "#C28FC4", "walking_minutes": 3}
  ],
  "tram_correspondences": [
    {"code": "2", "color": "#cead2c", "walking_minutes": 4, "destinations": "Pont de Bezons ↔ Porte de Versailles"}
  ],
  "transilien_correspondences": [
    {"code": "L", "color": "#7A99C9", "destinations": "Saint-Lazare ↔ Cergy / Versailles RD"},
    {"code": "U", "color": "#D41367", "destinations": "La Défense ↔ La Verrière"}
  ],
  "bus_correspondences": {
    "diurne":   ["73", "141", "144", "159", "174", "178", "258", "275", "276", "278", "360"],
    "nocturne": ["N24", "N53"],
    "regional": []
  }
}
```

## URLs publiques par mode (V1 = métro)

Le routage PHP (`public_html/index.php`) lit le JSON station selon l'URL :

| URL | Template | JSON lu |
|---|---|---|
| `/metro/station/chatelet/` | `station-metro.php` | `data/stations/chatelet.json` |
| `/metro/station/la-defense-grande-arche/` | `station-metro.php` | idem |
| `/rer/station/chatelet/` (V2) | `station-rer.php` (futur) | même fichier |
| `/transilien/station/saint-lazare/` (V2) | `station-transilien.php` (futur) | même fichier |

**Une seule source de vérité par station.** Si on ouvre la page RER d'une
station, on lit le même JSON. Le template adapte juste l'angle de
présentation (focus métro vs focus RER vs focus tramway).

## Cas d'usage croisés

La structure flat permet des cas d'usage transversaux faciles à implémenter :

### `/visiter/monuments/{tag}/` (V2 future)
Lit toutes les stations qui ont un POI taggué :
```php
foreach (glob('data/stations/*.json') as $f) {
    $s = json_decode(file_get_contents($f), true);
    foreach ($s['nearby_pois'] ?? [] as $poi) {
        if ($poi['name'] === 'Tour Eiffel') {
            $stationsServantTourEiffel[] = $s['slug'];
        }
    }
}
```

### `/itineraires/{from}/{to}/` (V2 future)
Lit 2 stations :
```php
$from = json_decode(file_get_contents("data/stations/$fromSlug.json"), true);
$to   = json_decode(file_get_contents("data/stations/$toSlug.json"), true);
// Comparaison lignes communes, calcul correspondances
```

### `/info-trafic/` (existant)
Itère sur toutes les stations pour identifier celles affectées par les
perturbations API IDFM PRIM.

### Sitemap auto (futur)
Liste toutes les stations actives via `glob('data/stations/*.json')` pour
générer les URLs publiques `/metro/station/{slug}/`.

## Maillage interne et hubs

`data/global/major-hubs.json` (registre central) référence les hubs majeurs
par leur slug **canonique** (= slug du JSON station). Aucune indirection
métro-X/.

```json
{
  "chatelet": {"type": "central", "similar": ["gare-de-lyon", "saint-lazare"]},
  "la-defense-grande-arche": {"type": "business", "similar": ["chatelet", "auber"]}
}
```

## Cohérence avec les autres data flat

| Catégorie | Path | Pattern |
|---|---|---|
| **Stations** | `data/stations/{slug}.json` | flat, multimodal |
| **Lignes métro** | `data/lines/metro-{code}.json` | indexé par code (16 lignes uniques) |
| **Gares parisiennes** | `data/gares/{slug}.json` | flat |
| **POIs partagés** | `data/poi-registry.json` (registre) | central |
| **Tarifs IDFM** | `data/global/transit-pricing.json` | source unique |
| **Hubs majeurs** | `data/global/major-hubs.json` | source unique |

Les **lignes** restent indexées par code (16 entrées fixes : metro-1,
metro-2, …, metro-14, metro-3bis, metro-7bis). Les **stations** sont à
plat car leur cardinalité (~310 cibles) est trop grande pour une
indexation par ligne et leur multi-mode justifie l'unicité par fichier.

## Workflow auto-deploy

`.github/workflows/auto-deploy-station.yml` lit directement
`data/stations/{slug}.json` :
- **Trigger** : `paths: 'public_html/data/stations/*.json'` (motif simple,
  pas `**/`)
- **Détection slug** : `git diff` extrait le filename, slug = `basename`
- **Validation** : `validate-station.php --slug={slug}`
- **Pas de paramètre `--line=X`** : le fichier station contient déjà
  toutes les lignes desservies.

Voir `docs/AUTO-DEPLOY-STATIONS.md` pour le pipeline complet.

## Migration historique

Cette structure flat est la structure **originale** du projet. Aucune
migration `metro-X/{slug}.json → {slug}.json` n'a été nécessaire — les
2 stations livrées (Châtelet, La Défense) ont toujours été à plat depuis
leur production. Ce document fixe la philosophie pour éviter qu'une
production future ne tombe accidentellement dans le pattern indexé par
ligne.

## Justification long-terme

| Élément | Coût flat (NOW) | Coût indexé par ligne (alternatif) |
|---|---|---|
| 2 stations existantes | 0 (déjà flat) | 2 dossiers + 2 fichiers redondants |
| 305 stations futures | 1 fichier par station | 305-700 fichiers (multi-lignes dupliquent) |
| Refactor station multi-ligne | rien | mise à jour de N fichiers (1 par ligne) |
| Maillage interne (hub similaires) | slug canonique direct | nécessite indirection |
| URLs futures `/rer/station/X/` | même fichier | duplication ou refactor lourd |
| Cas d'usage croisés (POIs, itinéraires) | trivial | jointures complexes |

**Décision** : structure flat conservée, philosophie documentée pour
prévenir toute dérive future.
