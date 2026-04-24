# Livraison 4.2 — Auto-génération blog trafic

> **Statut :** Stratégie validée, prêt pour coding
> **Dernière mise à jour :** 24 avril 2026

---

## 🎯 Stratégie éditoriale validée

### Décisions prises (24 avril 2026)

- **Mode publication :** Full auto, sans validation humaine quotidienne
- **Fréquence :** 1 article par jour strict (365/an)
- **Modèle IA :** Claude Sonnet 4.5 (~30€/an estimé pour 365 articles)
- **Scope éditorial :** **Option B** — Métro + RER + Tramway + Transilien + Bus Paris RATP
- **Objectif principal :** SEO longue traîne + signal de freshness
- **Objectif secondaire :** Discover en bonus (pas d'obsession)
- **Monétisation :** AdSense intégré **dès le design** (Approche A)

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

## 💰 Stratégie monétisation AdSense (Approche A)

### Principe directeur

AdSense est pensé et structuré **dès la génération de l'article**, pas
retrofitté après. Les emplacements sont définis dans le template PHP et dans
le prompt Claude, avec un système de toggle permettant d'activer AdSense
uniquement quand le compte sera validé.

### Pattern de placement validé (4 emplacements)

```
1. AD SLOT "header"       → Entre breadcrumb et titre
                             Format : 970×250 desktop / 320×100 mobile
2. AD SLOT "in-article-1" → Après la section "Ce qu'il faut retenir"
                             Format : 336×280 / Responsive mobile
3. AD SLOT "in-article-2" → Après la section "Focus du jour"
                             Format : 336×280 / Responsive mobile
4. AD SLOT "footer"       → Après le partage social, avant la bio auteur
                             Format : Responsive leaderboard
```

### Règles de design AdSense

- Maximum 3 annonces display above the fold
- Ratio contenu/pub < 30% visible d'un coup
- Lazy loading obligatoire sur les in-article
- Breakpoint mobile : encarts passent en pleine largeur sous 640px
- Consent Mode v2 : encarts se chargent uniquement apres opt-in RGPD
- Aucun encart au-dessus du titre H1

### Phases d'activation

**Phase 1 — Sans AdSense actif (aujourd'hui → ~30 articles publies)**
- Les `.ad-slot` s'affichent vides (CSS `:empty` gere l'invisibilite)
- Structure en place, zero impact visuel
- Le toggle `config/ads.php` est a `enabled: false`

**Phase 2 — Candidature AdSense (apres ~30 articles, ~1-2 mois)**
- Candidature sur https://www.google.com/adsense
- Validation 1-4 semaines par Google
- Obtention Publisher ID (`ca-pub-XXXXXXX`)
- Creation des 4 slots dans l'interface AdSense

**Phase 3 — AdSense actif**
- Injection des IDs dans `config/ads.php` + passage a `enabled: true`
- Les `.ad-slot` se remplissent automatiquement
- Monitoring des revenus via le dashboard AdSense

### Revenus estimes (indicatif)

| Metrique | Annee 1 | Annee 2 |
|---|---|---|
| Pageviews/article moyen | 300-800 | 1 000-3 000 |
| RPM AdSense secteur info FR | 2-4 € | 3-5 € |
| Revenu annuel estime | 300-1 500 € | 3 000-10 000 € |

Cout de production annuel : ~30 € Claude + hebergement = **ROI positif des an 1**
si trafic > 200 pageviews/article.

---

## 📝 Regles de redaction (pour le prompt Claude)

### Structure cible par article

- Longueur : **600-900 mots minimum**
- Structure type :
  1. H1 : titre accrocheur base sur l'evenement le plus marquant du jour
  2. "Ce qu'il faut retenir" : 3-5 bullet points TL;DR
  3. **Marqueur `<!-- ad-slot: in-article-1 -->`**
  4. "Etat du reseau ligne par ligne" : statuts avec contexte
  5. "Focus du jour" : 100-200 mots sur la perturbation principale
  6. **Marqueur `<!-- ad-slot: in-article-2 -->`**
  7. "Travaux en cours cette semaine" : synthese + liens internes
  8. "Nos conseils" : itineraires alternatifs, rappels utiles
  9. "A suivre" : anticipation courte des jours suivants

### Ton et style

- Journalistique, factuel, neutre
- Formulations humaines : "notre redaction", "selon IDFM", "a cette heure"
- Beaucoup de conditionnels, zero extrapolation hasardeuse
- Citation systematique de PRIM / IDFM comme source de verite
- Vocabulaire riche, varie d'un jour a l'autre
- Zero boilerplate identique (sinon penalite Google)

### Disclaimer obligatoire en pied d'article

> *Cet article s'appuie sur les donnees officielles d'Ile-de-France Mobilites
> (PRIM). Les informations sont verifiees et completees par la redaction en
> cas d'evenement majeur.*

**🚫 Ne JAMAIS mentionner "automatique" ou "genere par IA" dans le disclaimer.**
La transparence se fait sur la **source des donnees** (PRIM), pas sur le mode
de production. Cette formulation est techniquement vraie (supervision via code,
prompt, angles) et protege le E-E-A-T sans s'auto-saboter.

---

## 🔄 Les 7 angles editoriaux tournants

Un angle different chaque jour de la semaine pour casser la repetition et
donner a Discover + SEO 7 raisons differentes de pousser les articles.

| Jour | Angle | Focus editorial |
|---|---|---|
| Lundi | "Les lignes a eviter cette semaine" | Anticipation hebdo |
| Mardi | "Zoom travaux" | Chantiers en cours |
| Mercredi | "Chiffres du trafic" | Data et contexte |
| Jeudi | "L'histoire derriere [l'evenement]" | Analyse d'actu |
| Vendredi | "Preparer votre week-end transports" | Pratique week-end |
| Samedi | "Trajets culturels et loisirs" | Tourisme (co-signature Elodie) |
| Dimanche | "Bilan hebdomadaire + anticipation" | Recap et projection |

A affiner lors du coding avec prompts specifiques pour chaque angle.

---

## 🚇 Scope editorial (Option B validee)

### Modes couverts

- 🚇 Metro (toutes les lignes 1 a 14, 3bis, 7bis)
- 🚆 RER (A, B, C, D, E)
- 🚋 Tramway (T1-T13)
- 🚂 Transilien (H, J, K, L, N, P, R, U)
- 🚌 Bus Paris RATP (reseau `network:IDFM:Operator_100`, ~130 lignes)

### Volume estime

Sur un jour moyen (observe le 24 avril 2026) :
- **~190 perturbations** dans le scope Option B
- Dont ~146 BLOQUANTES, ~52 PERTURBEES
- Repartition : Bus Paris (75%), Transilien (13%), RER (9%), Metro (5%), Tram (4%)

### Filtrage a 2 couches

**Couche 1 — Dans l'article Claude :**
- Toutes les perturbations Metro/RER/Tram/Transilien (~60)
- Seulement les BLOQUANTES des Bus Paris (~100)
- Total envoye a Claude : ~150 max → ~15k tokens input → ~0,05€ par appel

**Couche 2 — Dans les JSON par ligne (dual output) :**
- Pour chaque ligne impactee, `data/traffic/YYYY-MM-DD-{line}.json`
- Contient toutes les perturbations (pas seulement les graves)
- Alimente les widgets "Aujourd'hui sur la ligne X" sur les pages froides
- Zero cout Claude (donnees brutes)

---

## 🔒 Securites a construire des le depart

### 1. Panic button
Secret GitHub `DISABLE_AUTO_PUBLICATION` (actuellement `false`). Si passe a
`true`, le workflow exit des la premiere etape. Utile en voyage, maintenance,
ou si bug detecte.

### 2. Fallback si PRIM down
Si l'API PRIM plante a 5h55, le script genere un article **neutre et factuel**
("Consultez le site officiel IDFM pour l'etat du trafic en temps reel") plutot
que rien ou n'importe quoi. Preserve le signal de freshness sans risque.

### 3. Fallback si Claude API down
Si l'API Anthropic plante, le script peut :
- Retry 2x avec delai exponentiel
- Si toujours en echec : utiliser un template de fallback basique (sans IA)
- Log l'incident dans `articles-log.json`

### 4. Log de publication
Fichier `data/articles-log.json` trackant pour chaque jour :
- Date/heure de generation
- Statut (succes, echec, fallback PRIM, fallback Claude)
- Nombre de mots genere
- Angle utilise
- Temps de generation Claude (ms)
- Cout estime (tokens input/output)
- Nombre de perturbations prises en compte

### 5. Monitoring (page admin simple)
Page `/admin/articles/` (protegee par mot de passe serveur) qui liste les
articles publies avec :
- Date de publication
- Angle editorial
- Nombre de mots
- Bouton "depublier" (passe en `noindex` + retire du sitemap)

---

## ⚠️ Risques acceptes lucidement

### Risque 1 — Erreur factuelle ponctuelle
Claude peut se tromper (chiffre faux, duree mal estimee, mauvaise ligne).
**Mitigation :** prompt extremement prudent, conditionnels systematiques,
citation des sources, aucune affirmation sans donnee PRIM derriere.

### Risque 2 — Penalite Google si qualite baisse
L'IA sans controle qualite peut devenir repetitive et penalisee.
**Mitigation :** rotation des 7 angles, vocabulaire riche demande, structure
qui varie, monitoring regulier des performances dans GSC.

### Risque 3 — Plafond de trafic Discover
Full auto bien fait = ~10-20k visiteurs/jour max sur Discover.
**Accepte :** strategie "site de reference" plutot que "media concurrent".

### Risque 4 — AdSense penalite pour contenu IA
Google AdSense tolere l'IA, mais peut desapprouver si la qualite baisse ou
si les annonces sont mal placees.
**Mitigation :** respect strict des regles (3 ads max above-the-fold,
pas de clic accidentel, consent RGPD, lazy loading).

---

## 🏗️ Architecture technique a construire

### Fichiers PHP (public_html/core/)

- **`ArticleGenerator.php`** — orchestrateur : PRIM → Claude → Markdown → commit
- **`PrimClient.php`** — API PRIM avec cache (perturbations 5 min, static 30j)
- **`DisruptionFilter.php`** — filtrage par date + mode + severite (Option B)
- **`DisruptionFormatter.php`** — nettoyage HTML, groupement par ligne, structure compacte
- **`ClaudeClient.php`** — API Anthropic avec retry + gestion erreurs + logging
- **`AngleRotator.php`** — rotation des 7 angles editoriaux selon jour
- **`ImageService.php`** — Unsplash + fallback banque perso
- **`AdInjector.php`** — ⭐ remplace `<!-- ad-slot: X -->` par le code AdSense (ou rien)

### Configuration (public_html/config/)

- **`secrets.php`** — cles API (deja exclu du FTP dans deploy.yml ✅)
- **`angles.php`** — definition des 7 angles + prompts specifiques
- **`ads.php`** — ⭐ config AdSense (publisher ID, slots, enabled toggle)
- **`banned-terms.php`** — mots interdits pour variete
- **`networks.php`** — mapping `networkId` → nom lisible (Operator_100 = RATP Paris)

### Donnees (public_html/data/)

- **`traffic/YYYY-MM-DD.json`** — JSON global du jour (dual output)
- **`traffic/YYYY-MM-DD-{line-slug}.json`** — JSON par ligne pour widgets
- **`articles-log.json`** — log de publication complet
- **`lines-reference.json`** — cache du referentiel ILICO (refresh hebdo)

### CI/CD (.github/workflows/)

- **`generate-daily-article.yml`** — cron @ 5h55 UTC (publication 6h CEST)

### Actifs a prevoir (public_html/assets/images/)

- `info-trafic/fallback-prim-down.jpg` — image generique si PRIM indisponible
- `info-trafic/generic-perturbation.jpg` — fallback thematique
- `info-trafic/weekly-summary.jpg` — pour les dimanches
- Debut d'une banque perso (photos prises par Ludovic)

### Modifications templates existants

- **`templates/pages/info-trafic-article.php`** :
  - Ajout de la zone `.ad-slot--header` entre breadcrumb et titre
  - Ajout de la zone `.ad-slot--footer` apres partage, avant bio auteur
  - Ajout de l'appel `AdInjector::inject($article->getHtml())` dans le corps

---

## 🔐 Secrets GitHub (tous crees ✅)

| Secret | Utilite | Statut |
|---|---|---|
| `ANTHROPIC_API_KEY` | API Claude | ✅ Cree |
| `UNSPLASH_ACCESS_KEY` | API Unsplash (images) | ✅ Cree |
| `PRIM_API_KEY` | API IDFM PRIM | ✅ Cree |
| `DISABLE_AUTO_PUBLICATION` | Panic button | ✅ Cree (false) |
| `FTP_SERVER/USERNAME/PASSWORD` | Deploiement o2switch | ✅ Existants |

---

## 📡 API PRIM — Infos techniques validees (24 avril 2026)

### Endpoint principal

```
GET https://prim.iledefrance-mobilites.fr/marketplace/disruptions_bulk/disruptions/v2
Header : apikey: <PRIM_API_KEY>
```

### Quota

- Cle "nouvel utilisateur" : **1000 req/jour**, 5 req/sec
- Consommation estimee : ~5 appels/jour (article + tests)
- Marge enorme

### Structure de la reponse

```json
{
  "disruptions": [...],        // 1028 perturbations (tout IDF)
  "lines": [...],              // 988 lignes avec impacts
  "lastUpdatedDate": "..."
}
```

### Champs cles par perturbation

- `id` — UUID
- `applicationPeriods[].begin/end` — periodes (format `YYYYMMDDTHHMMSS`)
- `lastUpdate` — derniere MAJ
- `cause` — `TRAVAUX`, `PERTURBATION`, `INFORMATION`
- `severity` — `BLOQUANTE`, `PERTURBEE`, `INFORMATION`
- `tags` — categorisation
- `title` — titre court (avec emojis)
- `message` — description HTML (a nettoyer)
- `impactedSections[]` — portions de ligne impactees
- `shortMessage` — resume court

### Mapping network → nom lisible

- `network:IDFM:Operator_100` → RATP Bus Paris (130 lignes)
- Autres networks → reseaux bus banlieue (a documenter au fil de l'eau)

---

## 💰 Budget estime

| Poste | Cout annuel |
|---|---|
| Claude Sonnet 4.5 (365 articles × ~0.08 €) | ~30 € |
| Unsplash API (free tier, 50 req/h) | 0 € |
| PRIM API (free tier, 1000 req/jour) | 0 € |
| GitHub Actions (repo public, minutes illimitees) | 0 € |
| Hebergement o2switch | Deja paye |
| **TOTAL L4.2** | **~30 €/an** |

Revenus AdSense attendus (an 1) : **300-1 500 €** → **ROI positif**.

---

## 📅 Planning cible

### Semaine 1 — Fondations PRIM
- [x] Secrets GitHub (Anthropic, Unsplash, PRIM, Panic)
- [x] Analyse API PRIM + validation structure JSON
- [ ] **`PrimClient.php`** + test standalone
- [ ] **`DisruptionFilter.php`** + tests unitaires

### Semaine 2 — Traitement + Claude
- [ ] `DisruptionFormatter.php` (nettoyage HTML, regroupement)
- [ ] `AngleRotator.php` + `config/angles.php`
- [ ] `ClaudeClient.php` avec prompt editorial V1

### Semaine 3 — Monetisation + Image
- [ ] **`AdInjector.php`** + `config/ads.php` (Approche A)
- [ ] Modification `info-trafic-article.php` (zones ad-slot header/footer)
- [ ] `ImageService.php` (Unsplash seulement en V1)

### Semaine 4 — Orchestration + CI/CD
- [ ] `ArticleGenerator.php` (orchestrateur complet)
- [ ] `generate-daily-article.yml` (cron GitHub Actions)
- [ ] Test 7 jours consecutifs en mode dev (noindex temporaire)

### Semaine 5 — Production
- [ ] Relecture critique des 7 articles de test
- [ ] Ajustement prompt par angle si besoin
- [ ] Passage en production + monitoring GSC

### Mois 2 — AdSense
- [ ] Candidature AdSense (~30 articles accumules)
- [ ] Injection IDs + passage `enabled: true`

---

## 🚀 Post-L4.2 (horizon 3-6 mois)

- **Tier 2 hebdomadaire** : 1-2 articles/semaine rediges manuellement (Ludo/Elodie),
  plus ambitieux (1200-1800 mots), visant clairement Discover
- **Tier 3 mensuel** : dossiers evergreen (2500-4000 mots) pour autorite SEO
- **Banque photo perso** : 200-300 photos prises par Ludovic sur 2-3 week-ends
- **Candidature Google News Publisher Center** (quand ~30 articles publies)
- **Newsletter quotidienne** basee sur l'article du jour
- **Push RSS** pour les aggregateurs
- **Encart trafic temps reel** sur home + pages hub (widget dynamique)
