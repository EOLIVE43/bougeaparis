# Système d'intros uniques par ligne

## Pourquoi ?

Les pages de lignes (16 lignes de métro + RER + tramway) partagent une **structure HTML identique**. Sans précautions, Google détecterait du **duplicate content** et pénaliserait toutes les pages au classement.

**Solution** : chaque page utilise des textes d'intro **uniques** rédigés avec des **structures de phrases différentes**.

## Architecture

### Stockage des textes
Chaque ligne a son propre JSON dans `data/lines/{lineId}.json` avec un champ `intros` :

```json
{
  "code": "1",
  "terminus_a": "La Défense",
  "terminus_b": "Château de Vincennes",
  "intros": {
    "introduction_title": "colonne vertébrale du métro parisien",
    "introduction": "<p>...250-300 mots...</p>",
    "plan": "100-130 mots",
    "stations": "80-110 mots",
    "horaires": "110-140 mots",
    "trafic": "100-130 mots"
  }
}
```

### Lecture par les partials
Chaque partial PHP lit son intro depuis le JSON, avec un **fallback générique** si non défini :

```php
<?php if (!empty($line['intros']['plan'])): ?>
  <p><?= $line['intros']['plan'] ?></p>
<?php else: ?>
  <p>Découvrez le <strong>plan de la ligne <?= $line['code'] ?></strong>...</p>
<?php endif; ?>
```

→ **Sécurité** : si le texte n'est pas encore généré pour une ligne, un fallback minimal s'affiche (le site ne casse pas).

### Génération des textes uniques
Le script `scripts/generate-line-intros.php` appelle l'API Claude pour produire les textes.

#### Stratégie anti-duplicate

1. **4 styles d'écriture** répartis sur les lignes :
   - **Direct** : phrases affirmatives, va à l'essentiel
   - **Conversationnel** : vouvoiement, plus chaleureux
   - **Pratique** : verbes d'action, utilité user
   - **Informatif** : ton neutre, encyclopédique

2. **Variables uniques** mentionnées dans chaque texte :
   - Numéro/code de ligne (5-7 occurrences variées)
   - Terminus A et B (mots uniques par ligne)
   - Variantes : "ligne X", "métro X", "métro de la ligne X"

3. **Densité de mots-clés** sans bourrage :
   - Gras (`<strong>`) UNIQUEMENT sur les mots-clés SEO
   - Pas de gras sur les chiffres ni les phrases descriptives

## Utilisation du script

### Prérequis
- PHP 7.4+ avec extension `curl`
- Variable d'environnement `ANTHROPIC_API_KEY` définie
- Au moins les champs `code`, `terminus_a`, `terminus_b`, `stations_count` dans le JSON

### Commandes

```bash
# Mode dry-run : voir les prompts sans appeler l'API (gratuit)
php scripts/generate-line-intros.php --dry-run

# Générer les intros manquantes pour toutes les lignes
php scripts/generate-line-intros.php

# Générer pour une seule ligne
php scripts/generate-line-intros.php --line=metro-1

# Forcer la régénération même si les intros existent déjà
php scripts/generate-line-intros.php --line=metro-1 --force
```

### Coût estimé

- ~5 sections × 16 lignes = 80 appels API
- ~2000 tokens par appel (prompt + réponse)
- Modèle Sonnet 4.5 : ~$3/Mtoken input + ~$15/Mtoken output
- **Coût total estimé : ~5€ pour les 16 lignes complètes**

À refaire seulement si on change la structure des prompts.

### Sécurité

⚠️ **NE JAMAIS COMMITER LA CLÉ API**.

- En local : `export ANTHROPIC_API_KEY="sk-ant-..."`
- Sur o2switch : ajouter en variable d'environnement (.htaccess SetEnv)
- Sur GitHub Actions : utiliser un Secret nommé `ANTHROPIC_API_KEY`

## Sauvegarde et versioning

Le script **écrit immédiatement chaque intro générée dans le JSON**. Si le script plante au milieu, les textes déjà générés sont conservés.

Les JSON sont versionnés dans Git → modifications historisées.

## Workflow recommandé

1. **Développement initial** : intros rédigées manuellement pour la ligne 1 (référence)
2. **Génération** : `php scripts/generate-line-intros.php` pour les 15 autres
3. **Relecture** : passage humain rapide pour valider la qualité
4. **Commit** : versionnage des textes dans Git
5. **Mise à jour** : si une ligne change (ex: prolongation, automatisation), régénérer uniquement cette ligne
