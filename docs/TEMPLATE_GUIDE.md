# TEMPLATE_GUIDE — Production éditoriale stations métro (industrialisation T2/T3)

**Document vivant** consigne les **patterns + règles validés** pendant le pilote
end-to-end Opéra (mai 2026) pour application en autonomie sur les ~290 stations
restantes (T2 + T3). À chaque nouvelle station, suivre ce guide pas à pas avec
le quality gate `scripts/diff-station-wikipedia.php` en filet automatique.

> **Statut** : en construction (sections 1, 2, 3 figées ; sections 4-10 à venir
> au fur et à mesure du pilote Opéra).

## Principe directeur T0 — Source ou rien

**Avant toutes les règles transversales, ce principe prime :**

> Toute donnée factuelle (date, nom, numéro, statut binaire, créneau horaire, jour
> de fermeture, prix, durée) doit être **sourcée au moment de la rédaction**. Les
> formulations atténuées (« notamment », « environ », « sauf X », « parmi les plus
> Y ») ne sont **PAS** un substitut à la vérification. Si pas de source disponible :
> formulation neutre OU champ marqué `_todo[]` pour vérification ultérieure.
> **Jamais d'affirmation déguisée.**

Cas pratiques pour identifier une violation T0 :
- "Le musée est ouvert tous les jours sauf le mardi" → si pas vérifié → **violation T0**
- "Plusieurs lignes de bus desservent la station" → factuel neutre, **OK T0**
- "notamment les bus 20, 22, 27" sans vérif GTFS/IDFM → **violation T0** (le parapluie 'notamment' ne couvre pas)
- "5h30 → 1h15" en se basant sur convention RATP réseau → **OK T0** car formule générique réseau explicitée

Pour les sources acceptées :
- Wikipédia FR (infobox + corps article) — source secondaire OK
- Wikidata SPARQL avec Q-ID validé — source primaire structurée
- IDFM GTFS (`scripts/cache-gtfs/idfm-gtfs/`) — source primaire transport
- Page station officielle IDFM ou RATP — source primaire
- Documents `docs/PMR-AUDIT.md`, `docs/POI-SYSTEM.md` — sources internes validées

---

## Règles transversales (s'appliquent à toutes les sections)

| # | Règle | Justification |
|---|---|---|
| T1 | **Bannir chiffres voyageurs non sourcés** ("des dizaines de milliers", "très fréquentée", "plusieurs millions"). Si pas de source IDFM officielle datée → ne pas affirmer de volume. | Précision SEO + E-E-A-T |
| T2 | **PMR = vérification ACTIVE** sur Wikipédia FR (infobox "Accessibilité") puis cross-check `docs/PMR-AUDIT.md` pour les lignes auditées (L3bis, L7bis, L14 à ce jour). JAMAIS hypothèse "à valider par quality gate". Phase 1.4 diff-wikipedia **ne couvre PAS le PMR**. | Donnée critique voyageur, faux positif inacceptable |
| T3 | **Dates d'ouverture des lignes** : pour CHAQUE ligne mentionnée, date exacte (JJ MM AAAA) + contexte 1re section ("première section X — Y"). Pas juste l'année. | Précision SEO + vérifiable Wikipedia |
| T4 | **Distinction PMR critique** (cf. `PMR-AUDIT.md`) : "ascenseurs publics opérationnels" ≠ "conformité PMR norme 2005". Ne jamais confondre les 2 métriques. | Bug L3bis évité historiquement |
| T5 | **Bus correspondances** : liste **non-exhaustive** ("notamment les 20, 29, 69, 76, 87, 91"). Bannir liste exhaustive (RATP change la cartographie). | Maintenabilité + cohérence Bastille pattern |
| T6 | **Audit Wikipédia/RATP daté** dans le JSON pour PMR et accessibility : `"audit_date": "YYYY-MM-DD"`. | Traçabilité E-E-A-T |
| T7 | **Pas d'opinion** : factuel sec uniquement. Bannir "magnifique", "spectaculaire", "incontournable", "à ne pas manquer". | Style éditorial + SEO informationnel |
| T8 | **Audit JSON post-écriture** : aucune clé top-level dupliquée. À vérifier après chaque section (le pattern Edit peut dupliquer si l'old_string n'inclut pas la clé fermante). Bloquer le commit sinon. | Garde-fou apprentissage friction Section 2 Opéra |
| T9 | **STRICT sans exception** : aucun nom d'autre station métro/RER dans **aucune** section éditoriale (intro, history, faq, trivia, tips, services, safety, accessibility). Si contexte historique appelle mention, **termes génériques** ("les autres grandes stations centrales", "le réseau parisien naissant", "les nœuds multiples du début XXe"). Exception **BÂTIMENTS homonymes** : OK avec désambiguïsation explicite par contexte ("l'**église de la Madeleine**", "la **gare Saint-Lazare**", "l'**Opéra Bastille** (bâtiment inauguré en 1989)") — test décisif : "le bâtiment" peut-il remplacer le nom sans perte ? Si oui → autorisé. | Cohérence cluster + évite cannibalisation SEO. Bypassed mecaniquement par audit manuel relecture (regex naïf est trop large). |
| **T9-bis** | **Exception terminus (figée Section 5)** : les noms de stations terminus sont autorisés UNIQUEMENT dans le contexte « ligne X (direction TERMINUS_A ou TERMINUS_B) » ou « direction TERMINUS ». Hors ce contexte, T9 strict s'applique. | Convention RATP/IDFM officielle, mot-clé SEO « métro X direction Y » légitime, pas de cannibalisation entre page station et entité terminus. |
| **T11** | **Données bus** : tout numéro de bus doit être issu d'une source vérifiable (GTFS IDFM arrêts <300m, ou page station IDFM officielle). **Connaissance générale = banni**. Si pas de source au moment de la rédaction : formulation neutre « plusieurs lignes de bus RATP » sans citer de numéros. | Sur 300 stations × 6 numéros = 1800 affirmations non vérifiées sinon. T0 en application. |
| **T11-superlatifs** | **Pas de superlatifs non sourcés** (cf. Section 4) : bannir "figure parmi les opéras les plus visités au monde", "monument incontournable", "chef-d'œuvre". Remplacer par formulation factuelle défendable ou chiffre sourcé daté. | T0 en application. |
| **T12** | **Liens sortants interdits vers concurrents directs** : `bonjour-ratp.fr`, `ratp.fr`, `idfm.fr`, `iledefrance-mobilites.fr`, `citymapper.com`, `navitia.io`, `maps.google.com` en tant que destination cliquable (`<a href>`). **Mention textuelle neutre OK** si fonctionnellement utile (sans nommer le concurrent par son nom commercial). **Sources audit T0 en _doc/commentaire PHP/JSON tolérées** (non affichées au visiteur). **Autorisés** : Wikipédia, sites officiels POIs, data.gouv.fr, paris.fr. **Préco rédaction** : ramener le visiteur vers une page BougeaParis (rétention) plutôt que rediriger vers concurrent. | Positionnement BougeaParis = alternative indépendante, pas agrégateur de liens vers concurrents. Cohérence E-E-A-T + UX. |
| T10 | **`<strong>` vs `<em>`** : `<strong>` sur les **entités factuelles** (nom station, lignes, monuments, dates clés). `<em>` sur les **expressions patrimoniales/SEO de zone** (*axe historique*, *Grands Boulevards*, *Paris haussmannien*, *Marais*). | Sémantique HTML + cohérence visuelle |

---

## Section 1 — `seo.description`

### Pattern (figé)

```
Station {NOM} (Métro {LIGNES}) sous/près de {POINT LOCALISATION} : correspondances, sorties, plan, accès {3 POIs ranked par notoriété + densité touristique}.
```

### Règles

- **Longueur cible** : **≤ 145 chars** (safe mobile Discover + Google SERP)
  - Tolérance jusqu'à 150 chars si déjà aligné LOT 1/2 (cf. Concorde/Bastille = 150)
- **POIs** : exactement **3**, ordre par notoriété décroissante
- **Mots-clés SEO de zone** à inclure si pertinent : *Grands Boulevards*, *Champs-Élysées*, *Marais*, *axe historique*, etc.
- **Préposition** : `sous` si station vraiment sous le lieu, `près de` sinon (factuel)
- **Validation** : factuel via Phase 1.4 `scripts/diff-station-wikipedia.php`

### Exemple validé (Opéra)

```
Station Opéra (Métro 3, 7, 8) sous la place de l'Opéra : correspondances, sorties, plan, accès Palais Garnier, Galeries Lafayette, Grands Boulevards.
```
**149 chars** — POIs : Palais Garnier > Galeries Lafayette > Grands Boulevards (notoriété + densité touristique)

### Autres exemples LOT 1/2 (référence)

- Concorde (150c) : `Station Concorde (Métro 1, 8, 12) sous la place de la Concorde : correspondances, sorties, plan, accès Champs-Élysées, Tuileries, obélisque de Louxor.`
- Bastille (150c) : `Station Bastille (Métro 1, 5, 8) sous la place de la Bastille : correspondances, sorties, plan, accès Opéra Bastille, Port de l'Arsenal, Coulée verte.`

---

## Section 2 — `hero.tagline` + `hero.description`

### Pattern `hero.tagline` (figé)

```
Sous {POINT LOCALISATION} — Lignes {L1}, {L2} et {L3} au cœur {CONTEXTE QUARTIER}
```

### Règles tagline

- **Longueur** : 15-18 mots (corridor LOT 1/2 = 17 mots)
- **Tiret cadratin** `—` (pas tiret simple `-`)
- 2 lignes : "Lignes A et B" (sans virgule). 3+ lignes : "Lignes A, B et C"
- `{POINT LOCALISATION}` : généralement le lieu emblématique au-dessus de la station ("la place de X", "le pont de X", "le boulevard X")
- `{CONTEXTE QUARTIER}` : capture un **mot-clé SEO de zone** ("historique de Paris", "de l'est parisien", "des Grands Boulevards", "du Marais", "des Champs-Élysées")
- **Variantes anticipées** :
  - Terminus : "À l'entrée de Paris — ..." si pertinent
  - Gare multimodale : "Sous la gare X — ..." pour les hubs

### Pattern `hero.description` (figé)

Structure 3 phrases, **~75-85 mots** (corridor LOT 1/2 strict : Bastille 80, Concorde 75).

```
P1 : Située sous {QUALIFICATIF EMBLÉMATIQUE} {LIEU}, la <strong>station X</strong> 
     dessert les <strong>lignes A, B et C du métro</strong>.

P2 : Ouverte en {ANNÉE_1RE_LIGNE} sur la ligne {N} [+ contexte 1re section si pertinent], 
     elle [se trouve / marque / accompagne] {LOCALISATION SPÉCIFIQUE / 
     FAIT HISTORIQUE MAJEUR ATTACHÉ AU LIEU}.

P3 : Aujourd'hui, {PATRIMOINE/QUARTIER ACTUEL} est dominé(e) par 
     <strong>{MONUMENT/INSTITUTION CLÉ}</strong> ({ANNÉE/DATE}) 
     [+ second monument si pertinent], faisant de cette station 
     {QUALIFICATIF GÉO} du {ZONE} parisien.
```

### Règles description

- `<strong>` **obligatoire** sur :
  - "station X" (1 fois en P1)
  - "lignes A, B et C du métro" (1 fois en P1)
  - monument(s) clé(s) mentionnés en P3
- `<em>` autorisé sur expressions patrimoniales identifiantes
- **Année d'ouverture obligatoire** en P2 + **numéro de la 1re ligne historique** ("Ouverte en 1904 sur la ligne 3" — pas juste "Ouverte en 1904")
- **Au moins 1 fait factuel daté** dans P2 ou P3
- Règles transversales T1 (voyageurs), T7 (pas d'opinion), T10 (strong/em) s'appliquent

### Exemple validé (Opéra)

**Tagline (16 mots, 79 chars)** :
```
Sous la place de l'Opéra — Lignes 3, 7 et 8 au cœur des Grands Boulevards
```

**Description (79 mots)** :
```
Située sous l'une des places les plus visitées du quartier des grands magasins, la <strong>station Opéra</strong> dessert les <strong>lignes 3, 7 et 8 du métro</strong>. Ouverte en 1904 sur la ligne 3, elle se trouve face au <strong>Palais Garnier</strong> (1875), chef-d'œuvre du Second Empire conçu par Charles Garnier. Aujourd'hui, la place dessinée sous Haussmann marque le carrefour des <em>Grands Boulevards</em> et l'entrée du quartier shopping (Galeries Lafayette, Printemps), faisant de cette station un nœud touristique majeur du centre parisien.
```

---

## Section 6 — `trivia` + `practical_tips` + `nearby_pois.description`

### 6A — `trivia` (5 par défaut, **min 3, idéal 5**)

**Pattern** : `{icon emoji unicode, title 8-12 mots, content 60-100 mots}`. Anecdote factuelle sourcée, **JAMAIS** inventée.

**Règles T0 renforcées (figées Section 6, finalisées après pilote Opéra)** :
| Règle | Détail |
|---|---|
| Nombre | **Minimum 3, idéal 5**. Si pas 5 sources fiables disponibles au moment de la rédaction : publier 3 ou 4 plutôt qu'inventer une 5e. `_todo` de la station peut signaler "+1 trivia à ajouter quand source disponible". |
| Chaque trivia | Cite **AU MOINS une date ou donnée chiffrée vérifiable** |
| URL source | Chaque trivia doit être **sourçable par URL Wikipédia précise** (FR ou EN). URL listée dans `_todo` de la station pour audit. |
| Folklore banni | Bannir « On dit que », « La légende veut », « Selon certains », « Il paraît » — **folklore non vérifiable interdit** |
| `icon` | 1 emoji unicode représentatif (🎨🎭📚🏰💎🏛️⚖️📜🗽🎤🏬🌆) |
| `title` | Phrase factuelle ou accroche évocatrice, **PAS** de "Le saviez-vous ?" générique. 8-12 mots. |
| `content` | 80-100 mots. T0 strict : tout fait vérifiable Wikipédia FR/EN. |
| `<strong>` | Sur dates, noms, chiffres clés |
| **Quality gate** | Phase 1.4 `diff-station-wikipedia` doit passer ≥90 sur la section trivia avant publi |

**Justification** : trivia = segment le plus repris sur réseaux sociaux + Discover. Erreur ici = dégâts disproportionnés sur E-E-A-T du domaine.

### 6B — `practical_tips` (6 par défaut)

**Pattern** : liste de strings, **30-50 mots/tip**, conseils voyageur factuels.

**Règles renforcées (figées Section 6)** :
| Règle | Détail |
|---|---|
| Nombre | **6 par défaut**. Pas d'optionnel. |
| **Forme impérative concrète** | Obligatoire : « Empruntez X », « Évitez Y entre Hh-Hh », « Privilégiez Z si… », « Prévoyez N min ». **Pas de description passive** |
| Bannir vagues | **« généralement », « souvent », « parfois »** = tip vague = tip inutile |
| Données changeantes | Horaires magasin, prix, événements : uniquement si **sourcées ET datées** (sinon renvoi calendrier officiel) |
| Pas d'opinion | « magnifique », « à ne pas manquer » bannis (T7) |
| Pas d'autre station nommée | T9 strict. Termes génériques OK |
| _todo | Liste les tips à re-vérifier annuellement (saisonnalité, événements récurrents) |

**Couverture typique** : (1) heures de pointe correspondances, (2) ambiance horaire/jours, (3) alternative PMR/poussettes, (4) destination + axe SEO, (5) trajet quartier alternatif, (6) calendrier événements / source officielle.

### Règle de publication POI (figée Section 6)

**Aucun POI top 5 ne peut être inscrit dans `{slug}.json` tant qu'il n'a pas été fact-checké par WebFetch ou consultation source primaire.** Le statut « à fact-checker » dans un commentaire de code n'est JAMAIS une raison valide pour pousser une description en prod. Workflow obligatoire avant écriture :
1. WebFetch Wikipédia FR du POI
2. Cross-check chaque chiffre/date/nom propre
3. Réécrire avec précisions issues du fetch (jamais "à confirmer" en attente)
4. URL Wikipédia listée dans `_todo` de la station

### 6C — `nearby_pois.description` (règle hiérarchisée corrigée)

**Pattern strict (figé Section 6, corrigé après préco refusée)** :

| POI rang | Critère | Format affichage |
|---|---|---|
| **Top 5** | Notoriété Wikipédia FR + distance <400m du `parent_station` | **Description rédigée auditée T0**, **50-70 mots**, ≥1 fait daté sourcé Wikipédia FR par description |
| **POIs 6 à N** | Reste (Q-IDs auto via build-station-pois) | **PAS de description en prose**. Affichage structuré : nom + distance à pied + lien Wikipedia sortant. Activation différée jusqu'à `diff-station-wikipedia` étendu aux POIs (Phase 1.4 V2 backlog). |

**Règles top 5** :
| Règle | Détail |
|---|---|
| Longueur | **50-70 mots** (legèrement plus longue que LOT 1/2 ~140 chars pour permettre 1 fait daté propre) |
| Contenu | Date(s) clé(s) + architecte/fondateur + fait identitaire principal |
| T0 strict | Tout chiffre/date/nom sourcé Wikipédia. Pas de superlatif (« emblématique », « mythique », « incontournable » — bannis) |
| `<strong>` / `<em>` | **Non utilisés** dans POI descriptions (texte court, pas de mise en valeur HTML) |
| Source | URL Wikipédia FR du POI listée dans `_todo` de la station |

**POIs 6 à N — pattern structuré (futur)** :
```json
{ "wikidata_id": "Q...", "name": "...", "category": "...", 
  "description": null,  // ← explicitement null, non rédigé en V1
  "wikipedia_url": "https://fr.wikipedia.org/wiki/...",
  "nearest_exit": {...} }
```

Le template d'affichage (`templates/components/station/poi-nearby.php`) devra gérer le cas `description = null` → afficher seulement nom + distance + lien Wikipedia (en V1.4 V2 backlog).

**Justification** : sur 300 stations × 7 POIs secondaires = 2100 descriptions auto-publiées non auditées = catastrophe E-E-A-T. Pattern hiérarchisé évite définitivement ce piège.

---

## Section 10 — Quality gate Phase 1.4 + flip published

### Process figé clôture pilote / batch T1+

**Étape obligatoire** avant tout flip `published: true` sur une station :

```bash
php scripts/diff-station-wikipedia.php --slug=<station>
```

### Seuils décision publication

| Score | Verdict | Décision |
|---|---|---|
| ≥ 90 | **pass** | Flip `published: true` autorisé direct |
| 70-89 | **warning marginal** | Audit factuel humain des flags. Si flags = limites couverture diff-wikipedia (et non erreurs factuelles), flip autorisé avec note. Sinon corriger. |
| < 70 | **fail** | Flip **bloqué**. Corriger les anomalies HIGH/MEDIUM avant. |

### Audit factuel humain (warning marginal 70-89)

Pour chaque flag (contradicted/partial/not_found), vérifier :
- **Est-ce une vraie erreur factuelle ?** → Corriger dans le JSON
- **Est-ce une limite de couverture diff-wikipedia ?** (fait correct mais pas dans les sources fetched) → Accepter, noter dans `_todo` pour Backlog E

### Limite connue diff-wikipedia (Backlog E)

`diff-station-wikipedia.php` fetch les POIs déclarés + entités thématiques fréquentes du contenu. **Ne fetch PAS** :
- Pages Wikipédia "Ligne X du métro de Paris" (où sont les dates exactes ouverture des lignes)
- Pages Wikipédia "Personnage historique" (où sont les détails biographiques)
- Pages Wikipédia "Place X" si non POI déclaré

**Conséquence** : dates précises type "19 octobre 1904" sortent en **partial** (année trouvée, date exacte non), noms type "Marc Chagall" / "Georges-Eugène Haussmann" sortent en **not_found** (cités dans le contenu mais pas dans les POIs fetched). Ce ne sont **PAS** des erreurs factuelles.

### Exemple validé (Opéra pilote)

Score : **89/100 (warning marginal)**
- Contradicted : 0 ✓ (après fix 200→213 m Place Vendôme)
- Verified : 70 (couverture haute)
- Partials : 6 (3 dates métro 1904/1913/1916 × 2 occurrences) — limite Backlog E
- Not found : 3 (Haussmann ×2 + Chagall) — limite Backlog E

**Audit humain** : 6/6 partiels = dates Wikipédia confirmées (Ligne 3/8/7 du métro de Paris articles), 3/3 not_found = noms Wikipédia confirmés (article Marc Chagall, article Haussmann). 1/6 fix appliqué (Vendôme 200→213 m). **Pas d'erreur factuelle restante.**

**Décision pilote** : score 89 warning marginal **accepté**, flip `published: true` reporté en autre session après livraison Backlog D (refacto template services.php pour 3-statuts, sinon rendu cassé en prod).

---

### Backlog F — Migration JSONs LOT 1/2 vers schéma 3-statuts services

**Priorité : NICE TO HAVE post-publi Opéra** (déplacée depuis Backlog D scope initial).

**Spec** :
- Convertir les 7 JSONs LOT 1/2 (`available: true/false` legacy) vers schéma 3-statuts (`status: verified_present/verified_absent` + `value: true/false` + `audit_date`)
- Script Python ou PHP `scripts/migrate-services-3statuts.php` à créer
- Rétrocompat 100% côté template grâce aux helpers normalize* (Backlog D point 1 livré) → **non bloquant** pour publi

**Effort estimé** : ~1h (script + tests + commit 7 JSONs migrés).

### Backlog G — Checks `validate-station.php` enrichis

**Priorité : NICE TO HAVE batch T2** (déplacée depuis Backlog D scope initial — skip ce soir).

**Spec** :
- Ajouter contrôles enum sur `services.*.status` (pending/verified_absent/verified_present)
- Ajouter contrôle enum sur `safety.audit_status` (pending/verified/outdated)
- Ajouter warning si `_todo[]` non vide ET `published: true` (incite finalisation dette)
- Tous en mode `$strictIfPublished` (Backlog D pattern)

**Effort estimé** : 30 min + tests régression sur les 7 LOT 1/2 + Opéra.

### Backlog J — T12 suite (extension scope retrait concurrents)

**Priorité : NICE TO HAVE post-pilote** (pas bloquant batch T1, concerne contenus existants).

Détecté lors du grep final Tâche 2 du pipeline matinal 2026-05-21.

**Sous-chantiers** :

1. **Reformulation 2 articles blog** `content/info-trafic/*.md` mentionnant Citymapper + Google Maps + IDFM comme apps recommandées. Violation T12 strict côté contenu publié.
   - Fichiers : `2026-05-12-bulletin-zoom-travaux.md`, `2026-05-04-bulletin-semaine-a-venir.md`
   - Estim : 30-45 min (relecture + reformulation avec redirection BougeaParis interne)

2. **Investigation lien sortant `$fares['source_url']`** dans `templates/components/line/tarifs.php:117` + `templates/components/station/tarifs.php:184`. Si URL effective = `iledefrance-mobilites.fr` → violation T12. Soit retrait du lien sortant, soit reformulation "Source officielle : Île-de-France Mobilités" sans `href` cliquable.
   - Estim : 15-30 min (audit URL + correction template)

3. **(Bonus)** Étendre `scripts/validate-station.php` pour détecter liens sortants vers domaines concurrents (`idfm.fr`, `citymapper.com`, etc.) en mode warning ou error selon contexte.
   - Estim : 1h

**Note** : à traiter avant batch T1 idéalement, ou en parallèle des stations futures. Backlog tracé, pas d'urgence ce soir.

---

### Backlog H — Industrialisation pattern hero pour 299 stations restantes

**Priorité : BLOQUANT batch T1** (à confirmer avant publi station T1 N°2).

**Validation conceptuelle Solution 1B sur Opéra** : les variantes hero (jpg/webp/avif × tailles) sont **COMMITÉES** dans le repo pour garantir leur présence prod indépendamment de Wikimedia (workflow CI redondant pour audit, pas critique).

**Spec post-pilote** :
- Adapter `scripts/build-station-hero.php` pour systématiquement remplir `assets/img/stations/{slug}/` ET `hero_image` dans le JSON
- Adapter `.gitignore` : exceptions par station ajoutées au fur et à mesure des publis (ou wildcard global si pattern stabilisé)
- Estim long-terme : **~500 Mo de binaires sur 300 stations** (1.6 Mo × 300). Acceptable repo GitHub free (limite ~5 Go).
- Documenter ce pattern dans `docs/AUTO-DEPLOY-STATIONS.md` post-confirmation

**Justification** : sans ce pattern, chaque publi station dépend de Wikimedia CI = ~1-3% risque flake. À l'échelle 300 stations, garantie production prioritaire vs économie de quelques Mo de repo.

### Backlog E — Extension `scripts/diff-station-wikipedia.php` couverture

**Priorité : NICE TO HAVE batch T2** (pas bloquant publi, ne casse rien si différé).

**Spec** :
- Étendre `identifyWikiTargets()` pour fetcher en plus des POIs déjà identifiés :
  - Pages "Ligne X du métro de Paris" mentionnées dans `lines[]` (pour valider dates ouverture précises)
  - Pages Wikipédia des **personnages historiques** mentionnés dans `history.paragraphs` (extraction par regex + filtres stopwords)
  - Pages Wikipédia des **places nommées** mentionnées dans `intro_paragraphs` qui ne sont pas dans `nearby_pois`
- Cap fetches à 25 sources/station (vs 19 actuel) pour éviter explosion temps
- Cache 24h prod
- Devrait faire passer Opéra de 89 → ~95 (pass clean)

**Effort estimé** : 1h-1h30.

**Justification non-bloquant** : score 89 warning marginal est acceptable pour publi T1 (audit humain confirme pas d'erreur factuelle). Backlog E améliore la qualité du gate, mais le contenu est déjà T0 strict.

---

## Récap final pilote Opéra (2026-05-13 → 2026-05-20)

### Production éditoriale (10/10 sections)

| # | Section | Statut Opéra | Pattern figé TEMPLATE_GUIDE |
|---|---|---|---|
| 1 | `seo.description` | ✅ 149 chars | "Station X (Métro N…) sous Y : correspondances, sorties, plan, accès A, B, C." |
| 2 | `hero.tagline` + `hero.description` | ✅ 16 + 79 mots | "Sous {LIEU} — Lignes A, B et C au cœur {ZONE SEO}" + 3 phrases factuelles |
| 3 | `intro_paragraphs` (3) | ✅ 111+99+119 mots | §1 IDENTITÉ → §2 HISTOIRE → §3 RÉSEAU+PMR (T0 strict) |
| 4 | `history.title` + paragraphes (3) | ✅ 7 mots + 111+97+97 mots | T1/T2 toujours 3§ ; T3 fallback 2§ |
| 5 | `faq` (8 Q/R) | ✅ 64-99 mots/réponse | Typologie Q1-Q8 + Q3 PMR + Q4 horaires conv RATP + T11 bus neutre |
| 6 | `trivia` (4) + `practical_tips` (6) + POI desc top 5 | ✅ tous T0 strict | Trivia min 3 idéal 5 + tips impératif + POIs 6-N description: null |
| 7 | `services` + `safety` + `accessibility` | ✅ 3-statuts + pending + verified | Default prudent null/pending + double métrique PMR + audit_date ISO |
| 8 | `popular_itineraries` (8) | ✅ Option B "snippet + lien" | Destinations POIs/BÂTIMENTS/axes SEO (T9 strict) + lines_label SHORT |
| 9 | `arrondissement` + `address` | ✅ stubs humains audités | Format Bastille strict + BAN/La Poste officiel UN seul CP |
| 10 | Quality gate + flip published | ✅ exécuté, ⏳ flip reporté | Pass ≥ 90, warning 70-89 audit humain, fail < 70 |

### Principes + règles figés (~900 lignes TEMPLATE_GUIDE)

- **Principe T0** : Source ou rien — toute donnée factuelle sourcée au moment de la rédaction
- **11 règles transversales** : T1-T11 + T9-bis (exception terminus T9 en contexte direction)
- **12 leçons fact-check internalisées** (Chedanne vs Chanut, Hardouin-Mansart Vendôme, Garnier 5 mai 1862, Mac Mahon inauguration, Oller Olympia, etc.)

### 5 backlogs techniques tracés

| Backlog | Spec | Priorité |
|---|---|---|
| A | `scripts/build-station-bus.php` GTFS 300m | BLOQUANT batch T2 |
| B | `scripts/build-station-services.php` IDFM page | BLOQUANT batch T2 |
| C | Audit safety sources officielles (pas heuristique) | NICE TO HAVE batch T2 |
| D | Refacto template services.php + migration JSONs LOT 1/2 + validate-station tolérance squelette | **BLOQUANT batch T1 + flip Opéra** |
| E | Extension diff-wikipedia.php couverture (lignes + personnages) | NICE TO HAVE batch T2 |

### Métriques pilote

- **Durée** : 8 jours calendaires (2026-05-13 mid-pilote intermédiaire → 2026-05-20 clôture)
- **Tours validation A++** : ~30 (10 sections × ~3 propositions/validations en moyenne)
- **Commits pilote** : 3 (mid-pilote 0722a3a + sections 7-10 744dea3 + clôture)
- **WebFetch sources Wikipédia FR** : 12 (Palais Garnier, Place Vendôme, Galeries Lafayette ×2, Église Madeleine, Olympia ×2, RER A, RER B, Opéra métro, Sacré-Cœur, Accessibilité métro)
- **Anomalies fact-check détectées + corrigées** : 12 (Chedanne/Chanut, Vendôme octogonal→carré-pans-coupés, Garnier dates, Madeleine Huvé/Vignon, Olympia date+fondateur, Vendôme 200→213m)
- **Score quality gate final** : 89/100 warning marginal (audit humain confirme 0 erreur factuelle restante)

### Prochaines étapes (post-pilote)

1. **Refacto TEMPLATE_GUIDE.md** (Tâche #14, BLOQUANT batch T1) — réorganiser en 6 parties logiques
2. **Backlog D** (~2h, BLOQUANT flip Opéra + batch T1) — refacto template services + migration JSONs LOT 1/2 + validate-station tolérance squelette
3. **Flip published:true Opéra** (1 commit) — publication finale après Backlog D
4. **Batch T1** : 12 stations icônes restantes (Gare du Nord, Gare de Lyon, Saint-Lazare métro, Montparnasse-Bienvenüe, Madeleine, République, Nation, Trocadéro, Saint-Paul, Hôtel de Ville, Abbesses, Cité)
5. **Backlogs A + B** (BLOQUANT T2) avant batch T2 stations secondaires

---

## Section 9 — `arrondissement` + `address` (stubs humains audités T0)

Ces 2 champs sont des **stubs humains** post-bootstrap : `bootstrap-station.php` les laisse vides (`""`) pour audit manuel. Aucune heuristique géographique (bbox lat/lon) ne les remplit automatiquement — la précision compte trop pour fauter aux frontières d'arrondissement.

### Règles figées Section 9

**1. `arrondissement`** : énumère les arrondissements **réellement traversés** par la station (frontière administrative).

Format Bastille (standard LOT 2) : `"4e, 11e, 12e"` (séparateur **virgule + espace**, format ordinal abrégé sans le mot "arrondissements").

- **1 seul arrondissement** : `"4e"` (sans pluriel)
- **2+ arrondissements** : `"9e, 2e"` (avec virgule, **pas slash**)
- **Station hors-Paris** : `"Puteaux (92)"` (format commune (département))

**Variante slash historique** (Étoile : `"8e/16e/17e"`) : à uniformiser vers Bastille standard lors de la migration JSONs LOT 1/2 (Backlog D ou migration séparée).

**2. `address`** : adresse postale officielle (référentiel BAN / La Poste). **UN SEUL code postal** par adresse, jamais hybride.

Format Bastille (standard LOT 2) : `"Place de la Bastille, 75011 Paris"`

- Pattern : `"{Lieu emblématique}, {CP} Paris"`
- Source obligatoire : adresse-data-gouv (BAN) ou La Poste, **pas une intuition géographique**
- Si la BAN renvoie un CP qui ne correspond pas à l'arrondissement dominant : **c'est la BAN qui fait foi**, pas une intuition (T0 strict)

**3. Séparation des préoccupations** :
- `arrondissement` = administratif réel (multi possible, frontières chevauchantes)
- `address` = postal officiel (unique, immuable)
- **Pas de redondance** : le chevauchement administratif est capturé dans `arrondissement`, pas doublé dans `address`

### Pré-requis bootstrap-station V2

Future enrichissement bootstrap-station.php (V2 backlog) :
- Reverse-geocoding via `api-adresse.data.gouv.fr` sur les coordonnées du `parent_station` GTFS
- Récupère address + arrondissement (champ `municipality` ou `citycode`)
- Pré-remplit le squelette, l'humain valide ensuite

**V1 actuel** : stubs vides + audit humain post-bootstrap. Géré dans `_todo[]`.

### Exemple validé (Opéra)

- `arrondissement` : `"9e, 2e"` (place de l'Opéra à cheval, format Bastille strict)
- `address` : `"Place de l'Opéra, 75009 Paris"` (CP officiel BAN, côté Palais Garnier 9e)

---

## Section 8 — `popular_itineraries` (pattern Option B "snippet + lien")

### Pattern figé Option B

**Décision architecturale** : on **n'expose pas la prose détaillée** des correspondances dans le composant station (multiplie violations T9 + erreurs T0). On expose un **snippet court + lien** vers la page dédiée `/itineraires/{slug-origine}-vers-{destination_slug}/` (Phase 3 cocon).

**Structure JSON figée** :
```json
{
    "destination_name": "<POI/BÂTIMENT/quartier/axe SEO — JAMAIS station métro pure>",
    "destination_slug": "<slug POI ≠ slug station homonyme>",
    "destination_full_name": "<NomStation> → <destination>",
    "lines_used": ["M3", "RER A", "à pied", "funiculaire", ...],
    "lines_label": "<SHORT : codes lignes + nb correspondances + terminus direction si T9-bis>",
    "duration_minutes": <int>,
    "changes_count": <int>,
    "search_volume_estimate": "high" | "medium" | "low",
    "future_url": "/itineraires/station-<slug>/<slug>-vers-<destination_slug>/"
}
```

### Règles dérivées Section 8

| Règle | Détail |
|---|---|
| **Nombre** | **8 par défaut**. Acceptable 6-10 selon richesse réelle d'itinéraires top SEO. |
| **`destination_name` (T9 strict)** | POIs (Tour Eiffel, Louvre, Sacré-Cœur, Disneyland), gares en BÂTIMENT (gare Saint-Lazare, gare du Nord), aéroports, axes SEO (Champs-Élysées, Forum des Halles), quartiers ("Marais", "Quartier latin"). **JAMAIS** noms de stations métro purs. |
| **`destination_slug`** | Slug du **POI/quartier**, distinct du slug d'éventuelle station homonyme. Ex : `forum-des-halles` ≠ `chatelet-les-halles` (station). |
| **`lines_label` SHORT** | Codes lignes + nombre de correspondances + terminus en contexte direction si T9-bis. **AUCUNE station intermédiaire nommée**. La prose détaillée appartient à la page `/itineraires/…/`. |
| **Terminus T9-bis** | OK de citer un terminus en contexte direction (ex : "RER A direction La Défense", "RER A direction Marne-la-Vallée — Chessy", "RER B direction Aéroport CDG 2 TGV"). **Cross-check Wikipédia obligatoire**. Erreur classique : citer une station intermédiaire comme terminus (cas Étoile RER A = faux, terminus = La Défense). |
| **BÂTIMENTS homonymes** | "Aéroport CDG 2 TGV" = BÂTIMENT gare TGV + terminus RER B : OK. "Marne-la-Vallée — Chessy" = terminus RER A + gare TGV : OK. Désambiguïsation explicite par contexte (T9 exception bâtiment). |
| **`duration_minutes`** | `int` brut dans JSON. Affichage "~XX min" dans label si non sourcé IDFM/Citymapper. **±20%** acceptable si pas de source. Trajets **> 30 min** : source officielle obligatoire (CDG, Disneyland, Versailles…). |
| **`changes_count`** | Nombre de correspondances. 0 = direct. |
| **`search_volume_estimate`** | `high`/`medium`/`low` heuristique SEO Paris. Top intent : CDG, Louvre, Tour Eiffel, Disneyland, Champs-Élysées, Forum Halles. |
| **`future_url`** | Pattern `/itineraires/station-{slug}/{slug}-vers-{destination_slug}/`. **Inactif** en V1 — rampe vers Phase 3 cocon. |

### Convention `future_url` (figée)

URL anticipée d'une page qui n'existe pas encore (Phase 3 cocon `/itineraires/`). Permet de pré-définir le maillage interne futur sans casser le rendu actuel. Le front affiche le lien si la page existe, sinon ne rend pas le lien (helper `conditionalLink` Phase 1.3 figé).

### Ordre des entrées (figé)

Tri par **notoriété/intent SEO descendant** (`search_volume_estimate: high → medium → low`). Pas par durée. Justification : les utilisateurs cliquent en haut de liste → mettre les destinations à plus haute intention en premier.

### Exemple validé (Opéra, 8 itinéraires)

Cf. `public_html/data/stations/opera.json` :
1. Tour Eiffel (high) · 2. Louvre (high) · 3. Champs-Élysées (high) · 4. Aéroport CDG (high) · 5. Disneyland Paris (high) · 6. Sacré-Cœur (medium) · 7. Forum des Halles (high mais utilité moindre) · 8. Gare Saint-Lazare (medium)

**Audit T9** : 8/8 lines_label propres, aucun terme banni (Auber/Étoile/Châtelet/Motte-Picquet/Bir-Hakeim/Madeleine/Pigalle/etc.). 3 terminus T9-bis utilisés : La Défense, Marne-la-Vallée — Chessy (×2), Aéroport CDG 2 TGV, tous confirmés Wikipédia.

---

## Section 7 — `services` + `safety` + `accessibility`

3 sous-sections distinctes mais interdépendantes. **Toutes** doivent respecter T0 strict + audit_date ISO + double métrique PMR. Default booléen prudent : `null`/`pending` jamais `true` par hypothèse.

### 7A — `services` (schéma 3-statuts par sous-clé)

**Pattern figé** (par sous-clé binaire) :

```json
"<service>": {
    "status": "pending",            // enum : pending | verified_absent | verified_present
    "value": null,                  // null | false | true
    "source": null,                 // URL ou référence (RATP, IDFM, Wikipédia FR)
    "audit_date": null,             // YYYY-MM-DD (si status != pending)
    "_note": "..."                  // contexte audit ou backlog
}
```

**Logique de rendu front (à implémenter Backlog D point 1)** :
- `status: pending` → "À vérifier" OU non affiché (UI sobre)
- `status: verified_absent` → "Non disponible" (sourcé + daté)
- `status: verified_present` → "Disponible" + détails (sourcé + daté)

**Structure complète services** (6 catégories) :
```json
"services": {
    "wifi":         { ...schéma 3-statuts... },
    "toilets":      { "public_paid": {...3-statuts...}, "public_free": {...3-statuts + location/access...} },
    "atm":          { ...3-statuts + banks_count_estimate + locations[]... },
    "ratp_office":  { ...3-statuts + location + services... },
    "left_luggage": { "ratp": {...3-statuts...}, "third_party": [] },
    "shopping_dining": { "main_location": "...", "details": "...", "secondary": "..." }
}
```

**Règles figées 7A** :
| Règle | Détail |
|---|---|
| Default prudent | `status: pending`, `value: null` partout — **JAMAIS `true` par hypothèse** |
| `audit_date` | Obligatoire dès `status != pending`, ISO YYYY-MM-DD, date réelle audit |
| Sources | RATP page station-services, IDFM page station, audits internes datés |
| `shopping_dining` | Structure descriptive (pas binaire) — rempli avec POIs voisins fact-checkés Section 6 |
| `left_luggage` | Structure imbriquée : `ratp` (3-statuts) + `third_party` (liste opérateurs externes Nannybag/Bounce) — homogène avec les autres services, pas de préfixe ad-hoc |

### 7B — `safety` (audit_status enum + tips factuels neutres)

**Pattern figé** :

```json
"safety": {
    "audit_status": "pending" | "verified" | "outdated",
    "audit_date": null | "YYYY-MM-DD",
    "level": "" | "standard" | "vigilant" | "renforcé",
    "agents": null | true | false,
    "police": null | true | false,
    "tips": [...3-5 entrées factuelles neutres...],
    "notes": ""
}
```

**Règles figées 7B** :
| Règle | Détail |
|---|---|
| `agents` / `police` | `null` par défaut (pas `false`). Le `null` signale "non audité", `false` est une affirmation factuelle |
| `level` | Vide par défaut. Sourcer RATP audit ou pratique observée. **Pas d'heuristique** "quartier touristique = vigilant" (Backlog C strict) |
| `tips` | 3-5 tips factuels neutres dérivés du contexte quartier (pickpockets axes touristiques, vigilance heures tardives, événements politiques). **Pas d'opinion** T7 |
| `notes` | 1 phrase synthèse + sourcement explicite |

### 7C — `accessibility` (double métrique PMR + verified obligatoire)

**Pattern figé** :

```json
"accessibility": {
    "audit_status": "verified",
    "audit_date": "YYYY-MM-DD",
    "level": "non-conforme" | "partiellement-accessible" | "accessible",
    "stats": {
        "elevators_count": N,           // Ascenseurs publics opérationnels (PMR + poussettes + bagages + seniors)
        "accessible_lines": N,          // Lignes conformes norme PMR 2005
        "total_lines": N
    },
    "details": "...",
    "source": "URL Wikipédia FR + RATP plan PMR officiel"
}
```

**Règles figées 7C** :
| Règle | Détail |
|---|---|
| **Double métrique PMR** | `elevators_count` (ascenseurs publics opérationnels) ≠ `accessible_lines` (conformité norme PMR 2005). **JAMAIS confondre** (cf. `docs/PMR-AUDIT.md`). Une station peut avoir des ascenseurs mais ne pas être conforme PMR 2005. |
| Sources | Wikipédia FR infobox "Accessibilité" + cross-check RATP plan PMR + `docs/PMR-AUDIT.md` pour lignes auditées (L3bis, L7bis, L14 à ce jour) |
| `audit_status` | Toujours `verified` après fact-check (différent de `services` et `safety` qui peuvent rester `pending`) |
| `audit_date` | ISO YYYY-MM-DD obligatoire |
| Alternative PMR | Si station non-PMR, mentionner une **LIGNE alternative PMR** pertinente géographiquement (ligne 14, RER A, etc.). Citer une LIGNE n'est PAS une violation T9 (T9 interdit les noms de stations). |
| `details` | Décrire le déficit + alternative + sourcement explicite |
| `level` semantics | `non-conforme` = 0 ascenseur OU 0 ligne conforme. `partiellement-accessible` = ascenseurs mais non conformes 2005. `accessible` = conformité totale norme 2005. |

### Exemple validé (Opéra)

Cf. `public_html/data/stations/opera.json` :
- `services` : 5 catégories binaires en `pending` (Backlog B traitera), `shopping_dining` rempli (POIs voisins fact-checkés)
- `safety` : `audit_status: pending`, agents/police `null`, 4 tips factuels neutres
- `accessibility` : `verified` 2026-05-20, `level: non-conforme`, `stats: {0, 0, 3}`, source Wikipédia FR explicite

---

## Section 5 — `faq` (8 Q/R par défaut, +1-4 opt si justifiées)

### Activation FAQ optionnelles

**Les FAQ optionnelles ne s'activent QUE si la station a une particularité narrative justifiée** (hub RER+métro+bus, terminus aéroport, station historiquement fermée, MH classée, art mural notable, etc.). **Pas de FAQ optionnelle "pour étoffer"**.

### Typologie Q1-Q8 (récurrente, à appliquer dans l'ordre)

| # | Type Q | Cible SEO |
|---|---|---|
| Q1 | Combien de lignes desservent X ? | informationnel |
| Q2 | Comment accéder au POI #1 depuis la station ? | transactionnel (sortie + min à pied) |
| Q3 | Station X est-elle accessible aux PMR ? | informationnel critique |
| Q4 | Quels sont les horaires du 1er et du dernier métro ? | transactionnel |
| Q5 | Comment rejoindre le POI #2 ? | transactionnel |
| Q6 | Où se trouve le POI #3 / monument identitaire ? | informationnel |
| Q7 | Quelle sortie pour le quartier/axe SEO ? | transactionnel multi-axes |
| Q8 | Particularité historique/architecturale | informationnel patrimonial |

**Optionnelles (justifiées uniquement)** :
| Q9 *opt* | Combien de sorties compte la station ? | si ≥6 sorties |
| Q10 *opt* | Particularité station (décor, profondeur, MH) | si MH/art/record |
| Q11 *opt* | Consignes à bagages ? | si transit/touristique majeur |
| Q12 *opt* | Quels sont les itinéraires populaires depuis X ? | si T1 avec `popular_itineraries[]` ≥ 6 entrées — réponse ≤60 mots + rampe vers `/itineraires/X-vers-Y/` |

### Pattern réponse (figé)

```
[1re phrase = RÉPONSE DIRECTE FACTUELLE] (Google scanne en premier pour Featured Snippet)
[CONTEXTE PRATIQUE] (sortie + distance + minutes à pied + référence sourcée)
[PRÉCISION SECONDAIRE OU AUDIT DATÉ] (référence officielle, fallback IDFM/RATP)
```

### Règles dérivées Section 5

| Règle | Détail |
|---|---|
| Longueur | **50-90 mots / réponse** (sweet spot Featured Snippet ~50, Q POI majeur peut aller jusqu'à 99) |
| 1re phrase | Réponse directe (Google scanne en premier pour Featured Snippet) |
| Format Q | Comme un humain tape sur Google : "Comment X ?", "Où Y ?", "Quels Z ?". Pas de "Quelle est l'histoire de…" (trop large) |
| `<strong>` | Sur **chiffres clés** (horaires, nb sorties, distances, années) + nom du POI cible + statut PMR |
| `<em>` | Expressions identifiantes patrimoniales (rare en FAQ) |
| **Q3 PMR** | Oui/Non explicite + audit Wikipédia daté + alternative ligne 14 ou plan PMR RATP (T9 strict : ne pas nommer de station alternative) |
| **Q4 Horaires** | Si données IDFM officielles dispos = précision. Sinon = formulation générique RATP réseau (5h30 → 1h15 semaine, 2h15 ven/sam/veille fêtes). PAS d'invention d'horaires spécifiques (T0). |
| **Q2/Q5/Q6 POI** | Sortie numérotée OU décrite + distance en m + temps à pied. Adresses précises vérifiables Wikipédia |
| **Q7 Quartier** | Indiquer axe (rue, boulevard) + repère temps à pied. T9 strict |
| **Bus** | T11 strict : neutre "plusieurs lignes RATP" tant que Backlog A non livré |
| Pas de "ça dépend" | Sans alternative précise → reformuler ou ne pas répondre |
| BÂTIMENTS homonymes | T9 + désambiguïsation explicite par contexte |

### Exemple validé (Opéra, 8 FAQ)

Cf. `public_html/data/stations/opera.json` — 8 FAQ Q1-Q8 totalisant 625 mots (corridor 400-720), tous sourcés Wikipédia/IDFM/convention RATP.

---

## Section 4 — `history` (title + paragraphes)

### Pattern `history.title` (figé)

```
{QUALIFICATIF URBANISTIQUE/HISTORIQUE} sous/au cœur de/face à {MONUMENT OU LIEU EMBLÉMATIQUE}
```

**Pas de superlatifs d'opinion** (pas de "chef-d'œuvre", "merveilleux", "incroyable" — règles transversales T7 + T11).

**Variantes valides** :
- Combinaison urbanisme + monument : "Un carrefour haussmannien sous le Palais Garnier" (Opéra)
- Angle évocateur : "Au pied d'une forteresse devenue place révolutionnaire" (Bastille)
- Spécificité datée : "Une station du tout premier métro parisien (1900)" (Concorde)
- Longueur : **7-10 mots**

### Pattern `history.paragraphs` (figé)

Structure thématique séquencée **§1 LIEU AVANT → §2 INAUGURATIONS LIGNES → §3 PATRIMOINE CONTEMPORAIN**.

**§1 — HISTOIRE DU LIEU AVANT LA STATION**
- Forteresse / place dessinée / événements pré-métro
- Si histoire pré-station limitée (post-1850 sans événement majeur) : peut commencer directement par la création urbanistique récente (cas Opéra : §1 = création haussmannienne 1864)

**§2 — INAUGURATIONS DES LIGNES MÉTRO**
- Chronologie des arrivées, dates exactes (JJ MM AAAA) + contexte sections
- Rôle historique de la station dans le réseau parisien
- Termes génériques si comparaison ("nœuds triples du début XXe") — pas de noms d'autres stations (règle T9 strict)

**§3 — MONUMENTS / PATRIMOINE CONTEMPORAIN AU-DESSUS**
- Palais, colonnes, opéras, églises majeures attachés au lieu
- Dates inauguration + architectes (avec préfixe rôle) + commanditaires
- Classement monument historique si applicable

### Règles nombre de paragraphes

- **T1/T2 = TOUJOURS 3 paragraphes** (pas un confort de prod, standard cluster)
- **Fallback 2§ réservé aux T3** sans patrimoine OU sans histoire pré-métro documentée
- Exemple LOT 1 (Concorde) avec 2§ = exception légitime (richesse historique concentrée sur métro + Schein 1991)

### Règles dérivées (en plus des transversales)

| Règle | Détail |
|---|---|
| Longueur §i | **100-130 mots** (corridor LOT 1/2) |
| Total | 250-400 mots selon nb paragraphes |
| Dates | Date complète (JJ MM AAAA) pour ouverture chaque ligne, inauguration monuments, événements historiques majeurs |
| Architecte/préfet/personnage | **Préfixe rôle obligatoire** ("le prévôt Hugues Aubriot", "l'architecte Charles Garnier", "le préfet Georges-Eugène Haussmann") |
| `<strong>` | Dates clés, monuments, personnages historiques principaux |
| `<em>` | Expressions identifiantes (*Trois Glorieuses*, *Second Empire*, *Révolution française*, *Belle Époque*) |
| BÂTIMENTS homonymes (T9) | Test décisif "le bâtiment" + désambiguïsation explicite par contexte. Cf. T9 ci-dessus |
| Faits vérifiables | TOUS les chiffres/dates/noms doivent passer Phase 1.4 `diff-station-wikipedia` |

### Exemple validé (Opéra)

- **title** : "Un carrefour haussmannien sous le Palais Garnier" (7 mots)
- **§1** (111 mots) : création haussmannienne 1860-1864 + axes voirie + Second Empire
- **§2** (97 mots) : M3 19/10/1904 + M8 13/07/1913 + M7 04/08/1916 — "nœuds triples du début XXe" (T9 strict)
- **§3** (97 mots) : Palais Garnier 5/01/1875 + Charles Garnier + Marc Chagall 1964 + classement MH 1923
- **Total** : 305 mots (corridor 250-400 ✓)

### Règle T11 ajout — Pas de superlatifs non sourcés

**Bannir** :
- "figure parmi les opéras les plus visités au monde" (sans chiffre/source)
- "monument incontournable", "à ne pas manquer", "chef-d'œuvre"
- "spectaculaire", "magnifique", "exceptionnel"

**Remplacer par** :
- Formulation factuelle défendable : "figure parmi les institutions lyriques majeures d'Europe" (factuel + comparaison régionale précise)
- Chiffre sourcé daté si dispo : "accueille X visiteurs par an selon [source officielle DATE]"
- Suppression si pas de fait pour étayer

---

## Section 3 — `intro_paragraphs` (3 paragraphes)

### Pattern (figé)

Structure thématique séquencée **§1 IDENTITÉ → §2 HISTOIRE → §3 POSITION RÉSEAU**.

**§1 — IDENTITÉ STATION**
```
La <strong>station X</strong> est l'un(e) des [QUALIFICATIF SEO] du métro parisien.
Située sous {LIEU/POINT EMBLÉMATIQUE}, à la jonction des {ARRONDISSEMENTS}, elle
dessert {N} lignes — la <strong>ligne A</strong>, ouverte le {DATE} [+ contexte
1re section], la <strong>ligne B</strong> arrivée le {DATE} et la <strong>ligne
C</strong> le {DATE}. Elle constitue {QUALIFICATIF GÉO} du <em>{ZONE} parisien</em>,
en correspondance avec {NOMBREUX/CERTAINES} lignes de bus (notamment les {LISTE 5-6 BUS
si pertinent}) et à proximité immédiate du/de la {3-4 POIs MAJEURS}.
```

**§2 — HISTOIRE / CONTEXTE DU LIEU**
```
[Phrase d'accroche sur le lieu : qu'a-t-il été / représenté historiquement].
[Dates clés multiples : création, transformation, événement marquant — TOUS
vérifiables Wikipedia].
[Personnages historiques liés : architectes, prévôts, urbanistes — uniquement si
factuel vérifiable].
```

**§3 — POSITION RÉSEAU / SPÉCIFICITÉ / ACCESSIBILITÉ**
```
Avec ses {N} lignes de métro ({CODES}) [+ RER si pertinent] et son {densité bus /
correspondances tram / etc.}, la <strong>station X</strong> est {QUALIFICATIF RÉSEAU}
de {ZONE GÉO}. Elle est à la fois {USAGE TOURISTIQUE} et {USAGE QUOTIDIEN}. Sa
position {GÉO STRATÉGIQUE} en fait également {POINT DE PIVOT vers terminus/zones
desservies}. Attention : {STATUT PMR vérifié actif sur Wikipédia FR + cross-check
PMR-AUDIT.md} (audit Wikipédia FR / RATP {DATE-DU-JOUR}).
```

### Règles intro_paragraphs

- **Longueur** : 110-135 mots par paragraphe, **total 350-400 mots**
- **§3 doit TOUJOURS terminer sur statut PMR explicite** (jamais omettre, même si "à vérifier")
  - Si donnée Wikipédia FR claire → "aucune des N lignes n'est accessible aux PMR à X — aucun ascenseur ne dessert les quais (audit Wikipédia FR / RATP YYYY-MM-DD)"
  - Si donnée incertaine → "Statut PMR à vérifier — consulter la page station IDFM" + marquer dans `_todo` pour intervention humaine
  - Pour les lignes auditées (L3bis, L7bis, L14) : utiliser les données précises de `docs/PMR-AUDIT.md`
- **Dates ouverture** : règle transversale T3 (date exacte + contexte 1re section)
- **Personnages historiques** : préfixés de leur rôle ("le préfet Haussmann", "l'architecte Charles Garnier", "le prévôt Hugues Aubriot")
- Règles transversales T1 (voyageurs), T7 (opinion), T9 (pas d'autres stations citées), T10 (strong/em) s'appliquent

### Exemple validé (Opéra)

**§1 (111 mots)** : voir `public_html/data/stations/opera.json`

**§2 (99 mots)** : voir `public_html/data/stations/opera.json`

**§3 (119 mots)** : voir `public_html/data/stations/opera.json`

**Total Opéra = 329 mots** — légèrement sous le corridor 350-400 mais validé manuellement (§2 raccourci par règle T9 "pas d'autre station citée").

---

## Workflow application T2/T3 (à finaliser)

Après chaque station bootstrappée :

1. `php scripts/bootstrap-station.php --slug=X` (sections A+B)
2. Production éditoriale sections C **en appliquant ce TEMPLATE_GUIDE** (sections 1-10)
3. `php scripts/diff-station-wikipedia.php --slug=X` (quality gate factuel)
4. Audit JSON : `python3 -c "import json,re; d=open('public_html/data/stations/X.json').read(); keys=re.findall(r'^    \"([a-z_]+)\":', d, re.M); from collections import Counter; print({k:v for k,v in Counter(keys).items() if v>1})"`
5. Validation manuelle PMR si lignes non auditées (cf. `PMR-AUDIT.md`)
6. Flip `"published": true` dans le JSON
7. `git push` → workflow CI gère hero AVIF/WebP/JPG + Lighthouse + FTP

## Backlog dette technique post-pilote

> Backlog A et B sont **BLOQUANT batch T2**. Backlog D est **BLOQUANT batch T1**
> (avant flip published:true sur Opéra). Backlog C est nice-to-have batch T2.

### Backlog A — `scripts/build-station-bus.php` (T11 application)

**Priorité : BLOQUANT batch T2.**

**Spec** :
- Parse GTFS IDFM (`cache-gtfs/idfm-gtfs/`)
- Buffer 300m autour du `parent_station` de chaque station
- Identifier les arrêts bus (`location_type=0` avec routes de `route_type=3`)
- Mapping `route_short_name` (ex "20", "22") via `routes.txt`
- Filtrage agency RATP (vs autres opérateurs) via `agency_id`
- Sortie : champ `bus_correspondences` JSON enrichi `{diurne:["20","22",…], nocturne:["N15"], regional:[]}`
- Intégration au bootstrap V2 (appel sous-process après build-station-pois)
- **Batch correctif** des 13 stations T1 publiées avec formulation neutre (Opéra inclus)

**Justification** : règle T11 figée nécessite implémentation. Sans script, formulation neutre Option B s'applique sur T1 ; mais T2 (30 stations) ne tolère pas la perte de mot-clé SEO bus à cette échelle.

**Effort estimé** : ~30-50 lignes PHP + tests sur 3 stations échantillon → ~1h dev + 30 min validation.

### Backlog B — `scripts/build-station-services.php` (Section 7 application)

**Priorité : BLOQUANT batch T2.**

**Spec** :
- Parse page IDFM officielle de chaque station (URL canonique IDFM)
- Cross-check page station-services RATP si dispo
- Récupère pour chaque service : `wifi`, `toilets.public_paid`, `toilets.public_free`, `atm`, `ratp_office`, `left_luggage.ratp`
- Mise à jour `status: verified_present|verified_absent` + `value: true|false` + `audit_date: <date_run>` + `source: <URL fetched>`
- Intégration au bootstrap V2 (appel sous-process après build-station-pois)
- **Batch correctif** des 13 stations T1 publiées + retro des 7 LOT 1/2 (cf. Backlog D)

**Effort estimé** : ~80-150 lignes PHP (scraping HTML IDFM) + tests sur 3 stations → ~1h30 dev.

### Backlog C — Audit safety (sources officielles)

**Priorité : NICE TO HAVE batch T2.**

**Spec** :
- Sources requises : **communiqués RATP datés** + **presse locale datée**
- Si pas de source : `audit_status` reste `pending`, `level` reste vide
- **PAS d'heuristique automatique** "quartier touristique = vigilant" — affirmation infondée et potentiellement stigmatisante. Soit source officielle, soit pas d'étiquetage.
- Re-audit annuel minimum

**Effort estimé** : audit manuel + recherche presse, ~30 min par station = non automatisable à 300.

### Backlog D — Refacto template services + migration JSONs LOT 1/2 + validate-station tolérance squelette

**Priorité : BLOQUANT batch T1 (avant flip published:true sur Opéra).**

**Chantier dédié post-pilote**, ~2h. Sans ça, Opéra avec nouveau schéma 3-statuts cassera son affichage services en prod.

**Scope (3 points)** :

1. **Refacto `templates/components/station/services.php`** (~30 min)
   - Lire `services.<key>.status` enum (3-statuts) au lieu de `services.<key>.available` booléen
   - Logique d'affichage par statut : `pending` → "À vérifier" ou non affiché ; `verified_absent` → "Non disponible" + source ; `verified_present` → "Disponible" + détails + source
   - Adapter `left_luggage` à structure imbriquée (`ratp` + `third_party`)

2. **Migration des 7 JSONs LOT 1/2 vers schéma 3-statuts services** (~1h)
   - `available: true` → `status: verified_present` + `value: true` + `audit_date: <date_audit_existante>` ou `<date_commit_initial>` si pas d'audit_date
   - `available: false` → `status: verified_absent` + `value: false` + idem
   - Préserver tous les autres champs (location_detail, coverage_detail, etc.)
   - Script de migration `scripts/migrate-services-3statuts.php` à créer + lancer sur les 7 + cleanup

3. **Adapter `scripts/validate-station.php`** pour tolérance squelette pré-publi (~30 min)
   - Lire `$d['published']` au début (cohérent avec garde-fou Phase 1.3 routing)
   - **Si `published: false`** (squelette en review) : les champs ci-dessous deviennent **warnings**, pas erreurs critiques
     - `address` (stub humain — remplissage manuel post-bootstrap)
     - `hero_image` (généré par workflow CI au flip published:true)
     - `arrondissement` (stub humain)
     - `services.*.status: pending` (Backlog B traitera)
     - `safety.audit_status: pending` (Backlog C traitera)
     - `_todo[]` non vide (signal explicite "travail en cours")
   - **Si `published: true`** : ces champs redeviennent erreurs bloquantes (cohérence E-E-A-T page exposée)
   - **Tout autre champ vide** (slug, name, lines, lat/lon, etc.) reste erreur critique dans les 2 cas

**Justification scope 3** : friction connue depuis Phase 1.1 bootstrap. `auto-deploy-station.yml` job "Validation JSON" échoue sur tout squelette (address vide + hero_image null). Cohérent avec garde-fou Phase 1.3 routing : un squelette `published: false` est par définition incomplet et ne sert pas de page.

**Effort total Backlog D** : ~2h (refacto template 30 min + migration 7 JSONs 1h + validate-station 30 min).

---

## Leçons fact-check pilote Opéra (à internaliser pour T2)

Précisions issues du fact-check WebFetch Wikipédia FR ; valeur de référence pour les futures stations T1+ :

| Sujet | Avant fact-check | Après fact-check |
|---|---|---|
| Galeries Lafayette coupole | Ferdinand Chanut architecte coupole | **Georges Chedanne** dirige la coupole ; Chanut = agencement seulement |
| Galeries Lafayette hauteur | 33 m (erreur reportée) | **43 m** confirmé |
| Place Vendôme forme | Octogonale | **Carrée à pans coupés** aux angles |
| Place Vendôme statue | Vague "ancienne statue royale" | **Statue équestre Louis XIV par François Girardon**, commande Louvois, abattue **10 août 1792** |
| Madeleine architecte | Pierre-Alexandre Vignon seul | Vignon mort **1828**, achevé par **Jean-Jacques-Marie Huvé** |
| Madeleine plan | "Plan rectangulaire" | **Plan périptère gréco-romain** |
| Garnier construction | "13 ans (1862-1875)" | **Début 1861, pose officielle 5 mai 1862, inauguration 5 janvier 1875** → 14 ans / 13 ans selon référence |
| Garnier inauguration | Pas de président mentionné | **En présence du président Patrice de Mac Mahon** |
| Olympia inauguration | "Fin XIXe siècle" | **11 avril 1893** (construction depuis 1888) |
| Olympia fondateur | Mention vague | **Joseph Oller** (créateur du Pari mutuel et du Moulin-Rouge) |
| Olympia statut | Risque superlatif | **"Plus ancien music-hall de Paris encore en activité"** = FAIT vérifié article, pas opinion |
| Le Fantôme de l'Opéra | "publié en 1910" | **Feuilleton dès 1909, volume en 1910** |

**Méta-leçon** : la connaissance générale d'un rédacteur (LLM ou humain) **n'est PAS T0**. Toute affirmation factuelle doit passer par fetch source primaire avant publication, même si elle "paraît évidente".

---

## Anticipation Section 7 (services + safety + accessibility)

Règles attendues à figer Section 7 :
- **`audit_date` obligatoire** sur chaque sous-section (services, safety, accessibility). Format ISO `YYYY-MM-DD`.
- **Données changeantes dans le temps** (ascenseur cassé, Vélib fermé, agence RATP fermée) : audit_status `pending`/`verified`/`outdated`. Re-audit annuel minimum.
- **PMR** : double métrique cf. `docs/PMR-AUDIT.md` (ascenseurs publics opérationnels vs conformité PMR norme 2005). Jamais confondre.
- **Safety** : agents/police = booléens sourcés (RATP audit ou Wikipédia). Pas d'hypothèse.
- **Stats `accessibility.stats`** : elevators_count + accessible_lines + total_lines. Pour lignes auditées (L3bis, L7bis, L14) : valeurs précises de `PMR-AUDIT.md`.

---

## Frictions détectées pendant pilote Opéra (à corriger en batch après pilote)

1. **`printSummary` bootstrap-station** affiche 0 exits/0 pois alors que sous-process les ont remplis → ne relit pas le JSON post-sous-process
2. **`validate-station.php` trop strict** : flagge "address vide" + "hero_image absent" comme erreurs pour un squelette → devrait être warnings + flag `--allow-skeleton`
3. **POI Q-ID "musée Grévin" Q1265070** flaggé par validate comme non-correspondant — soit FP validate, soit bug `build-station-pois` (à investiguer)
4. **Edit duplicate key** (Section 2) : mon Edit a momentanément dupliqué `description` car l'old_string ne fermait pas l'objet → garde-fou T8 ajouté
5. **WebFetch RATP 403** : impossible de cross-checker la liste PMR officielle directement → Wikipédia FR comme source secondaire OK (pattern LOT 1/2)
