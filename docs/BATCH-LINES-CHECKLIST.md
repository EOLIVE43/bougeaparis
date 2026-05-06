# Batch des 16 lignes métro Paris — Checklist de production

**État au 2026-05-06** : ligne 1 publiée et indexée (PageSpeed 97/100/100/100). 15 lignes restantes à enrichir et publier.

## Ordre de production validé (priorité fréquentation 2026)

1. **Ligne 14** — 820k voy/jour (la plus fréquentée du réseau, JO Paris 2024, prolongement Orly)
2. **Ligne 4** — 803k voy/jour (axe nord-sud, Châtelet, gares majeures, automatisée 2022)
3. **Ligne 13** — 612k voy/jour (sur-fréquentée, beaucoup de "info trafic")
4. **Ligne 7** — 597k voy/jour (la plus longue, sites touristiques, 38 stations)
5. **Ligne 6** — 388k voy/jour (aérienne, Bir-Hakeim, Tour Eiffel)
6. **Ligne 9** — 567k voy/jour
7. **Ligne 8** — 425k voy/jour
8. **Ligne 5** — 467k voy/jour
9. **Ligne 12** — 285k voy/jour (Montmartre, Pigalle)
10. **Ligne 2** — 478k voy/jour (Sacré-Cœur, Étoile)
11. **Ligne 11** — 234k voy/jour (prolongement Rosny 2024)
12. **Ligne 3** — 423k voy/jour
13. **Ligne 10** — 169k voy/jour
14. **Ligne 3bis** — 17k voy/jour
15. **Ligne 7bis** — 32k voy/jour (en dernier, faible trafic)

## Pipeline standard par ligne (7 étapes)

Pour chaque ligne, dans l'ordre :

```
[ ] 1. JSON bootstrappé          (php scripts/bootstrap-line.php --line=N)
[ ] 2. JSON enrichi éditorialement (intros, history, faq, points_of_interest, related_articles)
[ ] 3. Image hero sourcée         (Wikimedia, validation manuelle Ludo)
[ ] 4. Variantes générées         (php scripts/build-line-hero.php --line=N --pick="File:...")
[ ] 5. Push GitHub                (déploiement auto via .github/workflows/deploy.yml)
[ ] 6. Test PageSpeed             (cible 95+ desktop & mobile, AAA contrast)
[ ] 7. Indexation Search Console  (URL inspection → "Demander l'indexation")
```

---

## Checklist par ligne

### Ligne 14 (J1) — 820k voy/jour

- [ ] 1. JSON bootstrappé `php scripts/bootstrap-line.php --line=14`
- [ ] 2. Enrichissement éditorial
  - [ ] intros (16 paragraphes SEO)
  - [ ] history.paragraphs + timeline (mise en service 1998, prolongement Orly 2024, JO 2024)
  - [ ] faq (10-12 questions clés)
  - [ ] points_of_interest (Bibliothèque F. Mitterrand, Saint-Denis Pleyel, etc.)
  - [ ] tourism (lieux à voir + photos Wikimedia)
  - [ ] tourist_routes (parcours thématiques)
  - [ ] popular_routes (trajets fréquents)
  - [ ] accessibility (PMR — totalement accessible, repère ligne)
  - [ ] works (travaux récemment terminés / en cours)
  - [ ] related_articles (liens vers /info-trafic/...)
- [ ] 3. Hero sourcé Wikimedia (search MP14 + stations iconiques L14)
- [ ] 4. Variantes générées (12 fichiers AVIF/WebP/JPG)
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test (mobile + desktop)
- [ ] 7. Indexation Search Console

### Ligne 4 (J2) — 803k voy/jour

- [ ] 1. JSON bootstrappé `php scripts/bootstrap-line.php --line=4`
- [ ] 2. Enrichissement éditorial
- [ ] 3. Hero (MP14 CC, Châtelet, Saint-Sulpice)
- [ ] 4. Variantes générées
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test
- [ ] 7. Indexation Search Console

### Ligne 13 (J3) — 612k voy/jour

- [ ] 1. JSON bootstrappé `php scripts/bootstrap-line.php --line=13`
- [ ] 2. Enrichissement (note : trafic souvent perturbé = page "info trafic" stratégique)
- [ ] 3. Hero
- [ ] 4. Variantes
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test
- [ ] 7. Indexation Search Console

### Ligne 7 (J4) — 597k voy/jour

- [ ] 1. JSON bootstrappé `php scripts/bootstrap-line.php --line=7`
- [ ] 2. Enrichissement (38 stations, plus longue ligne — POI nombreux)
- [ ] 3. Hero
- [ ] 4. Variantes
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test
- [ ] 7. Indexation Search Console

### Ligne 6 (J5) — 388k voy/jour

- [ ] 1. JSON bootstrappé `php scripts/bootstrap-line.php --line=6`
- [ ] 2. Enrichissement (aérienne, Bir-Hakeim, Tour Eiffel — angles photo iconiques)
- [ ] 3. Hero
- [ ] 4. Variantes
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test
- [ ] 7. Indexation Search Console

### Ligne 9 (J6) — 567k voy/jour

- [ ] 1. JSON bootstrappé
- [ ] 2. Enrichissement
- [ ] 3. Hero
- [ ] 4. Variantes
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test
- [ ] 7. Indexation Search Console

### Ligne 8 (J7) — 425k voy/jour

- [ ] 1. JSON bootstrappé
- [ ] 2. Enrichissement
- [ ] 3. Hero
- [ ] 4. Variantes
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test
- [ ] 7. Indexation Search Console

### Ligne 5 (J8) — 467k voy/jour

- [ ] 1. JSON bootstrappé
- [ ] 2. Enrichissement
- [ ] 3. Hero
- [ ] 4. Variantes
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test
- [ ] 7. Indexation Search Console

### Ligne 12 (J9) — 285k voy/jour

- [ ] 1. JSON bootstrappé
- [ ] 2. Enrichissement (Montmartre, Pigalle, Concorde — angle touristique fort)
- [ ] 3. Hero
- [ ] 4. Variantes
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test
- [ ] 7. Indexation Search Console

### Ligne 2 (J10) — 478k voy/jour

- [ ] 1. JSON bootstrappé
- [ ] 2. Enrichissement (Sacré-Cœur via Anvers, Étoile)
- [ ] 3. Hero
- [ ] 4. Variantes
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test
- [ ] 7. Indexation Search Console

### Ligne 11 (J11) — 234k voy/jour

- [ ] 1. JSON bootstrappé (note : prolongement Rosny 2024 — terminus_b = Rosny — Bois-Perrier)
- [ ] 2. Enrichissement
- [ ] 3. Hero
- [ ] 4. Variantes
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test
- [ ] 7. Indexation Search Console

### Ligne 3 (J12) — 423k voy/jour

- [ ] 1. JSON bootstrappé
- [ ] 2. Enrichissement
- [ ] 3. Hero
- [ ] 4. Variantes
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test
- [ ] 7. Indexation Search Console

### Ligne 10 (J13) — 169k voy/jour

- [ ] 1. JSON bootstrappé
- [ ] 2. Enrichissement
- [ ] 3. Hero
- [ ] 4. Variantes
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test
- [ ] 7. Indexation Search Console

### Ligne 3bis (J14) — 17k voy/jour

- [ ] 1. JSON bootstrappé `--line=3bis` (4 stations seulement)
- [ ] 2. Enrichissement (contenu plus court, POI limités)
- [ ] 3. Hero (peut-être station Pelleport, Saint-Fargeau)
- [ ] 4. Variantes
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test
- [ ] 7. Indexation Search Console

### Ligne 7bis (J15) — 32k voy/jour

- [ ] 1. JSON bootstrappé `--line=7bis`
- [ ] 2. Enrichissement (8 stations, ligne en boucle Y)
- [ ] 3. Hero
- [ ] 4. Variantes
- [ ] 5. Push GitHub
- [ ] 6. PageSpeed test
- [ ] 7. Indexation Search Console

---

## Pièges identifiés / recommandations

### Bootstrap script
- **Ne jamais relancer `bootstrap-line.php` sur un JSON déjà enrichi** sauf en mode `--dry-run` pour audit. Le script ne devrait pas écraser, mais en cas de doute, faire un `git diff` avant `git add`.
- Les **stubs vides** (`history`, `faq`, `points_of_interest`, etc.) ne déclenchent pas de rendu côté template (les composants line/* gèrent les vides). Une ligne en stubs reste navigable mais peu informative.

### Hero image
- **Avant chaque run** de `build-line-hero.php`, ajouter une entrée `LINE_STRATEGY[$N]` dans le script avec :
  - Catégories Wikimedia spécifiques (ex: `Category:MP 14 (Paris metro)` pour L14)
  - Search queries (ex: `MP14 Bibliothèque France Mitterrand`)
  - `keywords_bonus` pour le scoring (matériel roulant + stations iconiques de la ligne)
- Le matériel roulant **change selon la ligne** :
  - L1 = MP 05, L4/11/14 = MP 14, L6/11 = MP 73 (historique), L2/3/5/9 = MF 67/77, L8/10 = MF 67, L7/13 = MF 77
  - Vérifier sur Wikipedia avant de chercher

### PageSpeed — points d'attention
- **Contraste WCAG AA** sur les blocs `--inactive` (déjà résolu via `#595959 + bg #F8F9FA + dashed border` dans `line.css`) — préservé.
- **CLS=0** : les `<img>` dans `<picture>` doivent toujours porter `width="..."` et `height="..."` explicites. Le partial `hero.php` les pose automatiquement depuis `hero_image.width/height`.
- **LCP** : le `<link rel="preload" imagesrcset>` est généré dans `line-metro.php` quand `hero_image.local_versions.avif` existe. Vérifier que le pipeline image écrit bien les 4 tailles AVIF.

### Schedule
- Les 15 lignes ont déjà un `schedule` valide (audit du commit). Le bootstrap ne le touche pas.

### Daily riders
- Les valeurs dans `DAILY_RIDERS` du bootstrap sont **approximatives 2026** (sources publiques IDFM/RATP). Affiner à partir des dossiers de presse trimestriels si la précision compte (les valeurs sont affichées dans le hero comme "750K voyageurs/jour").

### Indexation
- Le toggle `'line_pages_noindex' => false` est en place depuis le 2026-05-06. **Toute nouvelle ligne pushée sera automatiquement indexable** (pas de toggle individuel).
- Penser à **soumettre chaque nouvelle URL** dans Google Search Console après push pour forcer le crawl initial.

### Déploiement
- `.github/workflows/deploy.yml` est durci (timeout 15min, concurrency lock, paths-ignore .md). Surveiller l'onglet Actions à chaque push.
- En cas de freeze runner : cancel + re-run, ou upload manuel cPanel des fichiers modifiés en fallback.

---

## Outillage en place

| Script / fichier | Rôle |
|---|---|
| `scripts/bootstrap-line.php` | Pré-remplir un metro-X.json (mécanique + stubs) |
| `scripts/build-line-hero.php` | Recherche Wikimedia + génération AVIF/WebP/JPG |
| `templates/components/line/hero.php` | Render hero avec `<picture>` + content card |
| `templates/components/line/*.php` | 16 sections page ligne (déjà testées sur L1) |
| `assets/css/line.css` | CSS dédié aux pages ligne |
| `.github/workflows/deploy.yml` | Déploiement FTPS auto sur push main |
| `config/site.php` `line_pages_noindex` | Toggle indexation (false = indexable) |
