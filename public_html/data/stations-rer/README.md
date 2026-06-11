# data/stations-rer/

Fichiers JSON des stations RER. Convention (T16) :

- Nom de fichier : `{slug}.json` où slug = `rer-{nomstation}`
- Format aligné sur `data/stations/` (mêmes champs : `slug`, `name`, `name_full`, `lines`, `arrondissement`, `address`, `latitude`, `longitude`, `hero`, etc.)
- Champ `lines[]` : type `"rer"`, codes en majuscule (`"A"`, `"B"`, `"C"`, `"D"`, `"E"`)
- Champ `metro_correspondences[]` : codes métro (pour info reverse)
- `published: true` pour activer la route `/rer/station/{slug}/` + sitemap
