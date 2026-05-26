# Auto-déploiement des stations — workflow GitHub Actions

## Vue d'ensemble

Pipeline automatique qui produit une station métro **sans intervention
manuelle** après commit du JSON station. Réduit le temps Ludovic de
~30-45 min/station à 0 min/station.

**Trigger** :
- Push sur `main` modifiant `public_html/data/stations/*.json`
- Manuel via `workflow_dispatch` (input : `station_slug`)

**Workflow** : `.github/workflows/auto-deploy-station.yml`

## Pipeline en 3 jobs

### Job 1 — Validation JSON (`validate`)

Lance `scripts/validate-station.php --check-wikidata --json` :

| Vérification | Erreur ou warning |
|---|---|
| Champs critiques (slug, name, address, GPS, lines, intro_paragraphs, faq, history) | ❌ erreur |
| Coordonnées GPS dans Île-de-France (lat 48.5-49.0, lon 1.8-2.7) | ❌ erreur |
| `hero_image.url` + `alt` présents | ❌ erreur |
| `hero_image.credit.author` + `license` présents | ⚠️ warning (attribution) |
| Pour chaque POI : `wikidata_id` au format `Q\d+` | ❌ erreur |
| Pour chaque POI : Wikidata wbgetentities + label/aliases match le `name` | ❌ erreur (anti-bug Q-IDs inventés) |
| Pour chaque POI : GPS dans 1500m autour de la station | ⚠️ warning |
| `accessibility.audit_status === 'verified'` | ⚠️ warning |
| `tariff_zone` renseigné | ⚠️ warning |

**Heuristique de match Q-ID** (3 stratégies, une suffit) :
1. `name` complet apparaît dans label / description / aliases.
2. Au moins un mot ≥ 4 chars du `name` apparaît dans le haystack.
3. Si `name` est court (≤ 6 chars, lettres seules) → match sur initiales
   du label (ex: « CNIT » matche « **C**entre **N**ouvelles **I**ndustries
   **T**echnologies »).

### Job 2 — Génération assets (`generate-assets`)

- **Hero** : `php scripts/build-station-hero.php --station={slug}`
  → 12 variantes AVIF/WebP/JPG × 4 tailles dans
  `public_html/assets/img/stations/{slug}/`. Skippable via input
  `skip_hero=true` (utile si déjà uploadé manuellement).
- **POIs** : V1 = manuel (les POIs des 2 stations existantes ont été
  fetchés ad-hoc via Python). V2 = `php scripts/build-station-pois.php`
  + `php scripts/fetch-poi-images.php --station={slug}` (à activer
  quand le pipeline POI station-aware sera mature).
- **Upload FTP** : action `SamKirkland/FTP-Deploy-Action@v4.3.5`
  pousse `assets/img/stations/{slug}/` vers o2switch en FTPS.
  Pas de `dangerous-clean-slate` (préserve les autres stations).

### Job 3 — Lighthouse (`lighthouse`)

- Wait 30s pour propagation FTP.
- HTTP 200 check sur l'URL station.
- Lighthouse mobile + report dans GitHub Actions Summary (perf, a11y,
  BP, SEO + LCP, CLS, TBT, FCP).

## Secrets GitHub Actions requis

Vérifier dans `Settings > Secrets and variables > Actions` :

- `FTP_SERVER` (ex: `ftpc.cluster0XX.hosting.ovh.net`)
- `FTP_USERNAME`
- `FTP_PASSWORD`

Ces secrets existent déjà (utilisés par `deploy.yml` pour le
déploiement complet du repo). Le workflow auto-deploy-station les
réutilise.

## Lancer manuellement

Onglet **Actions** GitHub → **Auto-deploy station** → **Run workflow** :

- Slug : `la-defense-grande-arche`
- Skip hero : `false` (par défaut, met à jour le hero) ou `true` si
  déjà uploadé manuellement et qu'on veut juste re-valider.

## Trigger automatique

Push sur `main` modifiant `public_html/data/stations/*.json` →
workflow déclenché automatiquement. Le slug est détecté via
`git diff HEAD~1 HEAD`.

## Apprentissages intégrés

### 1. Bug Q-IDs Wikidata (incident La Défense, mai 2026)

Lors de la production manuelle de La Défense, **5 Q-IDs sur 8
étaient inventés** dans le JSON station, ce qui a déclenché le
téléchargement d'images complètement non liées (« Cousteau1972 »,
« Musée Calvet », etc.). Le validator avec `--check-wikidata`
détecte désormais ce bug en amont du déploiement.

### 2. Bug routage o2switch (incident `.htaccess`, mai 2026)

Le `.htaccess` `public_html/` doit toujours contenir le bloc
`mod_rewrite` front-controller. Le workflow auto-deploy-station
**ne touche JAMAIS au `.htaccess`** — il ne pousse que les fichiers
images dans `assets/img/stations/{slug}/`.

### 3. Bug a11y heading-order (mai 2026)

Pas de saut H2 → H4 sans H3 intermédiaire. Pas vérifié par le
workflow (on s'appuie sur Lighthouse en post-deploy pour repérer).
Si Lighthouse a11y < 95 → investigation manuelle.

### 4. Bug hotlink Wikimedia POIs (mai 2026)

Le composant `templates/components/station/poi-nearby.php` lit
désormais `image_url` qui pointe vers une URL **locale**
(`/assets/images/poi/monuments/{slug}.webp`). Le bug du hotlink
`Special:FilePath` est résolu côté composant. Le workflow ne fait
qu'uploader les fichiers vers o2switch.

## Troubleshooting

### Validation échoue sur un POI Q-ID

→ Vérifier le Q-ID via `https://www.wikidata.org/wiki/Q12345`.
Confirmer que le label fr ou en contient le nom du POI ou un
acronyme. Si le label semble incohérent : le Q-ID est probablement
faux, chercher le bon via `wbsearchentities`.

Localement :
```bash
php scripts/validate-station.php --slug={slug} --check-wikidata
```

### Hero generation échoue

→ Vérifier que `hero_image.url` (Wikimedia `Special:FilePath`)
répond 200 ou 302 :
```bash
curl -I "$HERO_URL"
```

→ Outils image requis (cross-platform depuis migration sips →
ImageMagick) :

| Outil | Rôle | Linux | macOS |
|---|---|---|---|
| `magick` ou `convert` | Resize JPG | `apt install imagemagick` | `brew install imagemagick` (fallback `sips` natif si IM absent) |
| `cwebp` | Conversion WebP | `apt install webp` | `brew install webp` |
| `avifenc` | Conversion AVIF | `apt install libavif-bin` | `brew install libavif` |

Le script `build-station-hero.php` détecte automatiquement
`magick` (IM 7) ou `convert` (IM 6) ; à défaut, fallback `sips`
(macOS legacy). Le workflow CI installe ImageMagick par défaut.

Si Hero échoue : vérifier dans le log du job 2 la ligne
`ERREUR resize {w} (tool=…, code=…)`. Code 1 = problème
ImageMagick (souvent disk full ou policy.xml restrictif).

### Upload FTP échoue

→ Vérifier les secrets FTP_*. Si `Connection refused` : o2switch
peut avoir une IP rate-limit, retry après quelques minutes.

### Lighthouse échoue ou timeout

→ Souvent dû à un cache CDN initial post-deploy. Re-run le job
manuellement. Si récurrent : augmenter le `sleep 30` à `sleep 60`.

## Phase 1 vs Phase 2 du pipeline POI

**Phase 1 (V1, actuelle)** : POIs gérés au cas par cas — Claude
Code écrit le JSON station avec POIs validés via
`wbsearchentities`, puis fetch ad-hoc des images via script Python
local. Workflow sert essentiellement pour le hero + Lighthouse.

**Phase 2 (V2, à venir)** : pipeline POI fully station-aware via
`build-station-pois.php` (génère le champ `nearby_pois` via SPARQL
Wikidata) + `fetch-poi-images.php --station={slug}` (télécharge
les images via P18 + crop 16:9 + WebP/AVIF). À activer dans le
workflow quand le pipeline POI sera testé sur 5+ stations.

## Backlog H — Stratégie gitignore heros stations (2026-05-26)

**Décision (Option A)** : les variantes hero AVIF/WebP/JPG × 4 tailles
(`public_html/assets/img/stations/{slug}/{slug}-{400,800,1200,1600}.{avif,webp,jpg}`)
sont **trackées par défaut dans git**, plus aucune règle d'ignore ni
d'exception par station. Le repo redevient source de vérité unique.

**Avant** : `.gitignore` bloquait globalement
`public_html/assets/img/stations/*/*.{avif,webp,jpg}` avec exception
explicite pour la seule station Opéra (pilote Solution 1B). Les 7 autres
stations publiées avaient leurs variantes en prod o2switch (uploadées
FTP par le workflow CI) mais **absentes du repo** — drift silencieux
entre prod et git.

**Après** : un `git clone` frais reconstruit l'intégralité du périmètre
servi en prod, sans dépendre d'un upload FTP historique ni d'une
regénération depuis Wikimedia. Repro 100% garantie.

**Conséquence opérationnelle** :
- **Repo reproductible** : `git clone` + `php -S` → site complet en local,
  toutes stations avec hero local AVIF/WebP/JPG. Aucun trou.
- **Prod ↔ git synchronisés** : un commit hero arrive en prod via
  `deploy.yml` (FTP général). Plus de désync possible.
- **Estim repo** : ~1.6 Mo × 300 stations = ~500 Mo de binaires
  long-terme. Acceptable repo GitHub free (limite ~5 Go).

**Commit auto via CI** : le step `Commit assets generated` du workflow
`auto-deploy-station.yml` (job `generate-assets`) détecte les variantes
nouvellement générées par `build-station-hero.php` et les commit
automatiquement sur `main` avec le tag `[auto-station]`. Aucun anti-loop
n'est nécessaire : le trigger workflow filtre sur
`public_html/data/stations/*.json`, un commit `[auto-station]` ne touche
que `assets/img/stations/{slug}/` et `assets/images/poi/`, donc pas de
boucle naturelle.

**Rétro-traitement des 8 stations publiées** : étape H.4 séparée, commit
unique des variantes locales des 7 stations LOT 1/2 + Bastille
(régénération nécessaire pour celle-ci, jamais générée localement).

## ROI

| Étape | Avant (manuel Ludovic) | Après (workflow) |
|---|---|---|
| Validation JSON | 5 min mental (relecture) | 30s auto (validate-station.php) |
| Génération hero local | 5 min | 0 min (CI runner) |
| Upload FTP hero (12 fichiers) | 10 min | 30s auto (FTP-Deploy-Action) |
| Test PageSpeed | 5 min | 1 min auto (Lighthouse CI) |
| Indexation GSC | 5 min | (à automatiser V3) |
| **Total/station** | **~30-45 min Ludovic** | **~0 min Ludovic, 5 min CI** |

Sur 305 stations futures = **~150-230h Ludovic économisées**.
Setup workflow = ~2-3h. **ROI ≈ 50-75×**.

## Évolutions futures

- **V2 POIs auto** : activer `build-station-pois.php` +
  `fetch-poi-images.php` dans le job Génération.
- **V3 indexation GSC** : appel automatique à l'API Search Console
  pour soumettre l'URL après deploy.
- **V4 sitemap auto** : régénération du `sitemap.xml` à chaque
  nouvelle station ajoutée.
- **V5 notif email** : ping Ludovic en cas de Lighthouse < 95.
