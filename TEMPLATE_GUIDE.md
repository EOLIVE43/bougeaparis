# TEMPLATE_GUIDE — BougeaParis.fr

Conventions transverses pour les templates et les données.

## T16 — Cluster RER : convention slugs

Tous les slugs de stations RER suivent le pattern :

    rer-{nom-de-la-station}

Exemples :
- `rer-chatelet-les-halles`
- `rer-auber`
- `rer-saint-michel-notre-dame`
- `rer-nation`
- `rer-marne-la-vallee-chessy`

Pas de cannibalisation avec métro — URLs et slugs systématiquement distincts :
- `/metro/station/chatelet/` (métro M1, M4, M7, M11, M14)
- `/rer/station/rer-chatelet-les-halles/` (RER A, B, D)

Helpers title centralisés (chargés via `core/bootstrap.php`) :
- `bp_title_station_rer($name, $lines)` → `"RER Châtelet — Les Halles (A, B, D) : plan et horaires"`
- `bp_title_ligne_rer($code)` → `"Ligne B du RER : plan, stations et horaires"`

Routes dynamiques :
- `/rer/station/{slug}/` → `public_html/data/stations-rer/{slug}.json` (published: true)
- `/rer/ligne-{a|b|c|d|e}/` → `public_html/data/lines-rer/rer-{a..e}.json` (published: true)

Templates :
- `public_html/templates/pages/station-rer.php` (basé sur `station-metro.php`)
- `public_html/templates/pages/line-rer.php` (basé sur `line-metro.php`)

Sitemap : scan automatique via `scripts/generate-sitemap.php` (sections 3.4e + 3.4f).

Priorités sitemap :
- Stations RER : `0.8` (changefreq weekly)
- Lignes RER : `0.9` (changefreq weekly)
