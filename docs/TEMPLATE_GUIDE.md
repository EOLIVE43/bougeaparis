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

## Backlog dette technique post-pilote (BLOQUANT démarrage T2)

> Les éléments ci-dessous doivent être livrés **avant le démarrage de Phase 2 T2**
> (les 30 stations T2 ne démarrent pas sans cette dette payée).

### Backlog A — `scripts/build-station-bus.php` (T11 application)

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
