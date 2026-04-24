# Livraison 4.2 — Auto-génération blog trafic

> **Statut :** Stratégie validée, prêt pour coding
> **Dernière mise à jour :** 24 avril 2026

---

## 🎯 Stratégie éditoriale validée

### Décisions prises (24 avril 2026)

- **Mode publication :** Full auto, sans validation humaine quotidienne
- **Fréquence :** 1 article par jour strict (365/an)
- **Modèle IA :** Claude Sonnet 4.5 (~30€/an estimé pour 365 articles)
- **Objectif principal :** SEO longue traîne + signal de freshness
- **Objectif secondaire :** Discover en bonus (pas d'obsession)

### Positionnement assumé

BougeaParis.fr se positionne comme **site de référence automatisé** sur les
transports franciliens, pas comme média concurrent du Parisien ou 20 Minutes.
Le quotidien nourrit le SEO longue traîne et la fraîcheur du site ; les pièces
éditoriales plus ambitieuses (Tier 2/3) viendront en complément plus tard.

### Plafond réaliste accepté

Un pipeline full auto bien fait peut viser ~10-20k visiteurs/jour max sur le
trafic Discover. Au-delà, il faudrait de la rédaction humaine type média
traditionnel. Ce plafond est **assumé consciemment**.

---

## 📝 Règles de rédaction (pour le prompt Claude)

### Structure cible par article

- Longueur : **600-900 mots minimum**
- Structure type :
  1. H1 : titre accrocheur basé sur l'événement le plus marquant du jour
  2. "Ce qu'il faut retenir" : 3-5 bullet points TL;DR
  3. "État du réseau ligne par ligne" : statuts avec contexte
  4. "Focus du jour" : 100-200 mots sur la perturbation principale
  5. "Travaux en cours cette semaine" : synthèse + liens internes
  6. "Nos conseils" : itinéraires alternatifs, rappels utiles
  7. "À suivre" : anticipation courte des jours suivants

### Ton et style

- Journalistique, factuel, neutre
- Formulations humaines : "notre rédaction", "selon IDFM", "à cette heure"
- Beaucoup de conditionnels, zéro extrapolation hasardeuse
- Citation systématique de PRIM / IDFM comme source de vérité
- Vocabulaire riche, varié d'un jour à l'autre
- Zéro boilerplate identique (sinon pénalité Google)

### Disclaimer obligatoire en pied d'article

> *Cet article s'appuie sur les données officielles d'Île-de-France Mobilités
> (PRIM). Les informations sont vérifiées et complétées par la rédaction en
> cas d'événement majeur.*

**🚫 Ne JAMAIS mentionner "automatique" ou "généré par IA" dans le disclaimer.**
La transparence se fait sur la **source des données** (PRIM), pas sur le mode
de production. Cette formulation est techniquement vraie (supervision via code,
prompt, angles) et protège le E-E-A-T sans s'auto-saboter.

---

## 🔄 Les 7 angles éditoriaux tournants

Un angle différent chaque jour de la semaine pour casser la répétition et
donner à Discover + SEO 7 raisons différentes de pousser les articles.

| Jour | Angle | Focus éditorial |
|---|---|---|
| Lundi | "Les lignes à éviter cette semaine" | Anticipation hebdo |
| Mardi | "Zoom travaux" | Chantiers en cours |
| Mercredi | "Chiffres du trafic" | Data et contexte |
| Jeudi | "L'histoire derrière [l'événement]" | Analyse d'actu |
| Vendredi | "Préparer votre week-end transports" | Pratique week-end |
| Samedi | "Trajets culturels et loisirs" | Tourisme (co-signature Élodie) |
| Dimanche | "Bilan hebdomadaire + anticipation" | Récap et projection |

À affiner lors du coding avec prompts spécifiques pour chaque angle.

---

## 🔒 Sécurités à construire dès le départ

### 1. Panic button
Un secret GitHub `DISABLE_AUTO_PUBLICATION` qui, quand activé (`true`), stoppe
la publication automatique. Le workflow GitHub Actions vérifie ce secret au
début et exit si désactivé. Utile en voyage, maintenance, ou si bug détecté.

### 2. Fallback si PRIM down
Si l'API PRIM plante à 5h55, le script génère un article **neutre et factuel**
("Consultez le site officiel IDFM pour l'état du trafic en temps réel") plutôt
que rien ou n'importe quoi. Préserve le signal de freshness sans risque.

### 3. Log de publication
Fichier `data/articles-log.json` trackant pour chaque jour :
- Date/heure de génération
- Statut (succès, échec, fallback)
- Nombre de mots généré
- Angle utilisé
- Temps de génération Claude
- Coût estimé

### 4. Monitoring (page admin simple)
Page `/admin/articles/` (protégée par mot de passe serveur) qui liste les
articles publiés avec :
- Date de publication
- Angle éditorial
- Nombre de mots
- Bouton "dépublier" (passe en `noindex` + retire du sitemap)

---

## ⚠️ Risques acceptés lucidement

### Risque 1 — Erreur factuelle ponctuelle
Claude peut se tromper (chiffre faux, durée mal estimée, mauvaise ligne).
**Mitigation :** prompt extrêmement prudent, conditionnels systématiques,
citation des sources, aucune affirmation sans donnée PRIM derrière.

### Risque 2 — Pénalité Google si qualité baisse
L'IA sans contrôle qualité peut devenir repetitive et pénalisée.
**Mitigation :** rotation des 7 angles, vocabulaire riche demandé, structure
qui varie, monitoring régulier des performances dans GSC.

### Risque 3 — Plafond de trafic Discover
Full auto bien fait = ~10-20k visiteurs/jour max sur Discover.
**Accepté :** stratégie "site de référence" plutôt que "média concurrent".

---

## 🏗️ Architecture technique à construire

### Fichiers PHP (public_html/core/)

- **`ArticleGenerator.php`** — orchestrateur : PRIM → Claude → Markdown → commit
- **`PrimClient.php`** — API PRIM avec cache (perturbations 5 min, static 30j)
- **`ClaudeClient.php`** — API Anthropic avec retry, gestion erreurs, logging
- **`ImageService.php`** — Unsplash (v1) + fallback banque perso (v2)
- **`AngleRotator.php`** — rotation des 7 angles selon jour de la semaine

### Configuration (public_html/config/)

- **`secrets.php`** — clés API (déjà exclu du FTP dans deploy.yml ✅)
- **`angles.php`** — définition des 7 angles + prompts spécifiques
- **`banned-terms.php`** — mots interdits pour variété ("vraiment", "incroyable", etc.)

### Données (public_html/data/)

- **`traffic/YYYY-MM-DD.json`** — JSON quotidien par ligne (dual output avec article)
- **`articles-log.json`** — log de publication complet

### CI/CD (.github/workflows/)

- **`generate-daily-article.yml`** — cron @ 5h55 UTC (publication 6h CEST)

### Actifs à prévoir (public_html/assets/images/)

- `info-trafic/fallback-prim-down.jpg` — image générique quand PRIM indisponible
- `info-trafic/generic-perturbation.jpg` — fallback thématique
- Début d'une banque perso (photos prises par Ludovic)

---

## 🔐 Secrets GitHub à créer

Avant de commencer à coder :

| Secret | Source | Statut |
|---|---|---|
| `ANTHROPIC_API_KEY` | https://console.anthropic.com/ | ⏳ À créer |
| `UNSPLASH_ACCESS_KEY` | Déjà en possession | ✅ À copier |
| `PRIM_API_KEY` | Déjà en possession | ✅ À copier |
| `DISABLE_AUTO_PUBLICATION` | Valeur : `false` par défaut | ⏳ À créer |

---

## 💰 Budget estimé

| Poste | Coût annuel |
|---|---|
| Claude Sonnet 4.5 (365 articles × ~0.08 €) | ~30 € |
| Unsplash API (free tier, 50 req/h) | 0 € |
| PRIM API (free tier, IDFM) | 0 € |
| GitHub Actions (repo public, minutes illimitées) | 0 € |
| Hébergement o2switch | Déjà payé |
| **TOTAL L4.2** | **~30 €/an** |

---

## 📅 Planning cible

### Semaine 1 — Préparation
- Création des 3 secrets GitHub
- Prompt Claude optimisé (7 angles)
- AngleRotator + test local

### Semaine 2 — Coding cœur
- ClaudeClient + PrimClient + tests unitaires
- ArticleGenerator orchestrateur
- Test local avec données PRIM réelles

### Semaine 3 — Intégration
- ImageService (Unsplash)
- GitHub Action cron
- Panic button + fallback PRIM
- Monitoring /admin/articles/

### Semaine 4 — Test en conditions réelles
- Run 7 jours consécutifs en dev
- Lecture critique de chaque article
- Ajustement du prompt par angle
- Validation de la qualité et variété

### Semaine 5+ — Production
- Premier article live en prod
- Surveillance GSC quotidienne les 2 premières semaines
- Ajustements fins selon performances

---

## 🚀 Post-L4.2 (horizon 3-6 mois)

- **Tier 2 hebdomadaire** : 1-2 articles/semaine rédigés manuellement (Ludo/Élodie),
  plus ambitieux (1200-1800 mots), visant clairement Discover
- **Tier 3 mensuel** : dossiers evergreen (2500-4000 mots) pour autorité SEO
- **Banque photo perso** : 200-300 photos prises par Ludovic sur 2-3 week-ends
- **Candidature Google News Publisher Center** (quand ~30 articles publiés)
- **Newsletter quotidienne** basée sur l'article du jour
- **Push RSS** pour les aggrégateurs
