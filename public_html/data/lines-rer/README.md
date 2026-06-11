# data/lines-rer/

Fichiers JSON des fiches lignes RER. Convention (T16) :

- Nom de fichier : `rer-{a|b|c|d|e}.json`
- Format aligné sur `data/lines/metro-*.json` (mêmes champs : `code`, `mode`, `color`, `seo`, `intros`, `schedule`, `stations`, `popular_routes`, `tourism`, etc.)
- Champ `mode` : `"rer"` (au lieu de `"metro"`)
- Champ `code` : une lettre majuscule (`"A"`, `"B"`, `"C"`, `"D"`, `"E"`)
- `published: true` pour activer la route `/rer/ligne-{code}/` + sitemap
