# Auto-update des dates rédactionnelles

## Objectif

Mettre à jour **automatiquement** le champ `meta.dates.updated` des fichiers `data/lines/*.json` à chaque push qui contient des **modifications rédactionnelles**.

→ Honnête envers Google : la date "Dernière mise à jour" change uniquement quand le contenu change vraiment.
→ Pas de "fake updates" qui pourraient pénaliser le site.
→ Aucune intervention manuelle nécessaire.

## Architecture

```
Tu modifies data/lines/metro-1.json (ex: ajout d'un POI)
              ↓
git commit + git push origin main
              ↓
GitHub Action 'auto-update-dates.yml' déclenchée
              ↓
Script PHP scripts/update-line-dates.php :
  1. Compare la version actuelle avec HEAD~1
  2. Si changement rédactionnel détecté → MAJ meta.dates.updated
  3. Si pas de changement rédactionnel → ne rien faire
              ↓
Si MAJ effectuée : commit auto "[auto-dates]" pushé sur main
```

## Champs surveillés

### ✅ MAJ automatique si modification de :

| Chemin JSON | Description |
|---|---|
| `intros.*` | Toutes les intros de section (introduction, plan, stations...) |
| `history` | Timeline, anecdotes, chiffres clés |
| `accessibility` | Équipements, conseils PMR |
| `fares.main_fares` | 4 tarifs principaux (Ticket, Navigo Mensuel...) |
| `fares.additional_fares` | 5 tarifs additionnels |
| `works.current_works` | Travaux en cours |
| `works.upcoming_works` | Travaux à venir |
| `faq` | Questions/réponses |
| `points_of_interest` | POI (monuments, musées...) |
| `popular_routes` | Itinéraires populaires |
| `tourist_routes` | Itinéraires touristiques |
| `tourism` | Données tourisme |
| `meta.primary_author.bio` | Bio Ludo |
| `meta.primary_author.expertise_tags` | Tags d'expertise Ludo |
| `meta.co_author.bio` | Bio Élodie |
| `meta.co_author.contributed_sections` | Sections d'Élodie |
| `meta.sources` | Sources externes |

### ❌ Pas de MAJ si modification de :

- `meta.dates` (sinon boucle infinie)
- `color`, `color_text`, `color_light` (techniques)
- `seo` (techniques)
- `fares.last_check`, `fares.valid_since` (techniques de scraping)
- `quick_actions` (configuration UI)
- Métadonnées d'images générées automatiquement par les scripts

## Exemples concrets

### Cas 1 : Tu ajoutes un POI

```diff
{
  "points_of_interest": {
    "monuments": {
      "items": [
+       { "name": "Tour Saint-Jacques", ... }
      ]
    }
  }
}
```

→ ✅ Action déclenchée → `meta.dates.updated` passe à aujourd'hui.

### Cas 2 : Tu modifies une intro

```diff
{
  "intros": {
-   "introduction": "La ligne 1 est la première...",
+   "introduction": "La ligne 1 du métro parisien, inaugurée en 1900..."
  }
}
```

→ ✅ Action déclenchée → MAJ.

### Cas 3 : Le script Wikimedia ajoute des photos

```diff
{
  "points_of_interest": {
    "monuments": {
      "items": [
        {
          "name": "Arc de Triomphe",
+         "image": { "src": "/assets/images/poi/...", ... }
        }
      ]
    }
  }
}
```

→ ✅ Action déclenchée (`points_of_interest` est surveillé) → MAJ.

⚠️ **Cas particulier** : si tu veux que le script Wikimedia ne déclenche PAS de MAJ de date, ajoute `[skip-auto-dates]` dans le message de commit.

### Cas 4 : Tu changes uniquement la couleur de la ligne

```diff
{
- "color": "#FFCD00",
+ "color": "#FECC0A"
}
```

→ ❌ Action ignore (champ technique non surveillé) → pas de MAJ.

### Cas 5 : Le script PRIM met à jour le trafic

→ ❌ Le trafic est en JSON séparé (`/data/traffic/YYYY-MM-DD.json`), pas dans `data/lines/*.json`. Pas de MAJ déclenchée.

## Utilisation manuelle (en local)

Tu peux tester le script sans GitHub :

```bash
# Voir ce qui serait modifié sans rien écrire
php scripts/update-line-dates.php --dry-run

# Lancer en réel (nécessite que tu sois dans un dossier git avec HEAD~1 disponible)
php scripts/update-line-dates.php
```

## Sécurité contre les boucles infinies

Le commit auto fait par l'action contient `[auto-dates]` dans son message.

L'action est configurée pour **NE PAS se déclencher** sur les commits qui contiennent `[auto-dates]` :

```yaml
if: "!contains(github.event.head_commit.message, '[auto-dates]')"
```

→ Pas de risque de boucle infinie.

## Permissions GitHub

L'action a besoin du droit `contents: write` pour pousser le commit auto. C'est configuré dans le workflow :

```yaml
permissions:
  contents: write
```

## Coût (GitHub Actions)

- Repository **public** = minutes Actions **illimitées**
- Action légère : ~30 secondes par push
- Coût : **0 €**

## Désactivation

Pour désactiver temporairement l'action :

1. Renommer le fichier en `.disabled` :
   ```bash
   mv .github/workflows/auto-update-dates.yml .github/workflows/auto-update-dates.yml.disabled
   ```
2. Commit et push.

Pour la réactiver, retirer `.disabled` du nom du fichier.

## Limites connues

### Premier push après création
Quand un fichier est ajouté pour la première fois, il n'a pas de version précédente dans git → pas de MAJ déclenchée. C'est normal : on utilise `meta.dates.published` à la création, pas `meta.dates.updated`.

### Comparaison via HEAD~1
Le script compare avec `HEAD~1` (le commit précédent). Si tu pushes plusieurs commits d'un coup, seuls les changements du **dernier commit** sont détectés. Pour les changements d'un push avec plusieurs commits, il faudrait un mécanisme plus complexe (comparer avec le base commit du push).

→ En pratique, ça marche très bien : on pousse généralement commit par commit.

## Évolutions futures

- [ ] Support multi-fichiers (stations, articles blog...)
- [ ] Historique des modifications dans un changelog auto
- [ ] Notification Slack/Discord lors de mises à jour majeures
- [ ] Détection des changements significatifs (filtrer les corrections de typo)
