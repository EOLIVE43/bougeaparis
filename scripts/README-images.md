# Script de récupération photos POI

## Objectif

Industrialiser la récupération des photos pour tous les POI (Points of Interest) du site BougeàParis.fr depuis Wikimedia Commons, avec watermark BougeàParis.fr et conformité légale (attribution).

## Workflow

```
Pour chaque POI dans data/lines/*.json :
  1. 🔍 Cherche sur Wikimedia Commons API
  2. 📥 Sélectionne la meilleure photo (taille, qualité)
  3. ⬇️  Télécharge l'image originale
  4. ✂️  Crop au format 16:9 (recommandation Discover)
  5. 📐 Redimensionne : 1200×675 (full) + 600×338 (thumb)
  6. 🎨 Applique le watermark :
       - Bandeau bas teal "B bougeàparis.fr · Se déplacer. Visiter."
       - Bandeau haut overlay : nom du POI
  7. 🗜️  Optimise en WebP qualité 85
  8. 💾 Sauvegarde dans /assets/images/poi/{categorie}/{slug}.webp
  9. 📝 Met à jour le JSON avec chemins + attribution
```

## Prérequis

- PHP 7.4+ avec extensions :
  - `curl` (requêtes HTTP)
  - `gd` ou `imagick` (manipulation d'images)
  - `json`
  - `mbstring`
- 100-200 Mo d'espace disque pour les images

## Utilisation

```bash
# Voir les options
php scripts/fetch-poi-images.php --help

# Mode dry-run : simulation sans télécharger
php scripts/fetch-poi-images.php --dry-run

# Toutes les photos manquantes (défaut)
php scripts/fetch-poi-images.php

# Une seule ligne
php scripts/fetch-poi-images.php --line=metro-1

# Un seul POI
php scripts/fetch-poi-images.php --line=metro-1 --poi=arc-de-triomphe

# Forcer la régénération (écrase les images existantes)
php scripts/fetch-poi-images.php --line=metro-1 --force
```

## Format de stockage

### Hiérarchie des fichiers

```
/assets/images/poi/
├── monuments/
│   ├── arc-de-triomphe.webp           (1200×675, watermarqué)
│   ├── arc-de-triomphe-thumb.webp     (600×338, sans watermark)
│   ├── place-de-la-concorde.webp
│   └── ...
├── musees/
│   ├── louvre.webp
│   └── ...
├── jardins/
└── quartiers/
```

### Mise à jour du JSON

Pour chaque POI, le JSON est enrichi automatiquement :

```json
{
  "name": "Arc de Triomphe",
  "slug": "arc-de-triomphe",
  "image": {
    "src": "/assets/images/poi/monuments/arc-de-triomphe.webp",
    "thumb": "/assets/images/poi/monuments/arc-de-triomphe-thumb.webp",
    "alt": "Arc de Triomphe à Paris, station Charles de Gaulle - Étoile",
    "width": 1200,
    "height": 675,
    "credit": {
      "author": "Benh LIEU SONG",
      "source": "Wikimedia Commons",
      "license": "CC BY-SA 4.0",
      "license_url": "https://creativecommons.org/licenses/by-sa/4.0/",
      "wikimedia_url": "https://commons.wikimedia.org/wiki/File:..."
    }
  }
}
```

## Compatibilité Discover

Les images respectent les recommandations Google Discover 2026 :

- ✅ Format **WebP** (supporté Discover)
- ✅ Résolution **1200×675px** = ratio 16:9 recommandé
- ✅ Qualité **85** = équilibre poids/qualité
- ✅ Sujet centré dans le crop
- ✅ Pas de texte sur les bords

⚠️ **Attention** : depuis la mise à jour Discover de février 2026, **les photos originales sont préférées aux photos stock**. Les photos Wikimedia sont acceptables mais pas optimales. Pour les POI les plus stratégiques, **remplacer progressivement par tes propres photos**.

## Conformité légale (CC BY-SA)

### Obligations

1. **Citer le photographe** ✓ (stocké dans `credit.author`)
2. **Citer la licence** ✓ (CC BY-SA avec lien)
3. **Indiquer les modifications** ✓ (watermark = transformation)
4. **ShareAlike** : les images modifiées sont aussi en CC BY-SA

### Affichage de l'attribution

L'attribution est affichée :

- **Sur la page POI** (en bas de la photo, gris clair 11px) :
  > Photo : Benh LIEU SONG · Wikimedia Commons · CC BY-SA 4.0
- **Sur la page `/credits-photos/`** (liste exhaustive de toutes les attributions)

## Politesse envers Wikimedia

- ✓ User-Agent personnalisé identifiant BougeàParis.fr
- ✓ Délai 0.8s entre chaque requête (respect rate limits)
- ✓ User-Agent contient un email de contact

## Limites connues

### Photos peu connues
Certains POI mineurs (ex: petits musées, jardins peu connus) n'ont pas de bonnes photos sur Wikimedia. Le script les ignore et garde le placeholder coloré.

### Qualité variable
Wikimedia accepte des contributions amateurs. Certaines photos sont médiocres. Le script trie par taille mais ne juge pas la qualité visuelle.

→ **Solution** : revue manuelle après le batch, remplacement des photos médiocres.

### Watermark basique
Le watermark utilise les fonts builtin de GD (5px-15px). Pour un rendu pro avec Inter Bold, il faudrait :
- Utiliser `imagettftext()` avec une vraie font (`Inter-Bold.ttf`)
- Ou passer à ImageMagick avec `-font` option

→ **À améliorer en v2** quand on aura besoin d'un rendu plus pro.

## Déploiement

### En local

```bash
cd /home/claude/preview/bougeaparis
php scripts/fetch-poi-images.php --line=metro-1
```

### Sur o2switch (production)

Via SSH :
```bash
ssh user@bougeaparis.fr
cd /home/USER/public_html
php scripts/fetch-poi-images.php
```

### Via GitHub Actions (industrialisation)

Pas recommandé pour ce script car :
- Volume de téléchargement élevé
- Repository public → tout le monde verrait les heures de batch

→ **À lancer en local** depuis ton poste, puis git push des images générées.

## Évolutions futures

- [ ] Support ImageMagick (meilleur crop)
- [ ] Font Inter Bold pour watermark pro (imagettftext)
- [ ] Génération AVIF en plus de WebP (meilleure compression)
- [ ] Détection des photos floues / mal cadrées (rejet auto)
- [ ] Mise à jour incrémentale (re-download si Wikimedia a une meilleure photo)
- [ ] Multi-photos par POI (galerie sur la page POI individuelle)
