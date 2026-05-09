# Audit PMR transversal — métro parisien

État au **2026-05-09**, post-correction L3bis (commit `8980fa9`)
et post-publication L7bis (commit `edd1221`).

## Contexte

Suite au bug critique L3bis (« 0 ascenseurs » alors que 6 ascenseurs
publics opérationnels sur 4 stations), audit factuel transversal
recommandé pour les 14 lignes restantes du batch.

## Distinction critique des deux métriques

| Métrique | Définition | Cas L3bis | Cas L14 |
|---|---|---|---|
| **Ascenseurs publics opérationnels** | Utilisables par tous (PMR, poussettes, bagages, seniors) | 6 (édicules Plumet 1922) | 84 |
| **Stations conformes PMR norme 2005** | Largeurs, signalétique tactile, espacement quai-train conformes | 0 | 21 (100%) |

Ces deux métriques ne doivent JAMAIS être confondues.

## État audit

| Ligne | Statut audit | Confiance valeurs JSON | Source |
|---|---|---|---|
| L1 | ⏳ Non audité | Moyenne (auto 2012, plausible mais à vérifier) | — |
| L2 | ⏳ Non audité | Plausible (1900-1903, 4 stations aériennes escaliers) | — |
| L3 | ⏳ Non audité | Plausible (1904-1937 historique) | — |
| **L3bis** | ✅ Audité | Haute (6 asc Plumet 1922 confirmés) | Wikipedia Pelleport, Saint-Fargeau, PdL |
| L4 | ⏳ Non audité | Moyenne (auto 2022, modernisation en cours) | — |
| L5 | ⏳ Non audité | Plausible | — |
| L6 | ⏳ Non audité | Plausible (viaduc aérien escaliers obligatoires) | — |
| L7 | ⏳ Non audité | Plausible | — |
| **L7bis** | ✅ Audité | Haute (5 asc confirmés Pré-SG, Jaurès, Place des Fêtes) | Wikipedia stations |
| L8 | ⏳ Non audité | Plausible | — |
| L9 | ⏳ Non audité | Plausible | — |
| L10 | ⏳ Non audité | Plausible (historique 1923) | — |
| L11 | ⚠️ **Priorité audit** | Risque sous-estimation | Pyrénées/Jourdain/Place Fêtes profondes = ascenseurs probables |
| L12 | ⏳ Non audité | Plausible | — |
| L13 | ⏳ Non audité | Plausible (modernisation MF19 prévue) | — |
| L14 | ✅ Confirmé brief | Haute (100% PMR origine 1998) | Public |

## Ligne 11 — risque sous-estimation

Architecture similaire à L3bis et L7bis pour certaines stations
historiques à grande profondeur (carrières de gypse, terrains
instables). Stations à vérifier impérativement :

- **Pyrénées** : profondeur, ascenseur probable
- **Jourdain** : profondeur, ascenseur probable
- **Place des Fêtes** : très profonde (24 m), ascenseur historique
  confirmé via audit L7bis (correspondance L11)
- **Télégraphe** : la plus haute en altitude du réseau, profondeur
  inverse à Belleville

Stations neuves prolongement Rosny 2024 (PMR conformes par
construction) :
- Liberté, Place Carnot, Hôpital de Montreuil, Romainville-Carnot,
  La Dhuys, Coteaux Beauclair, Rosny – Bois-Perrier (7 stations
  PMR strict)

JSON actuel L11 : 7 PMR / 15 ascenseurs / 37%. **Possiblement
sous-estimé** sur la métrique « ascenseurs publics » (les
historiques Pyrénées/Jourdain/Place Fêtes/Télégraphe ne semblent
pas comptés).

## Méthodologie audit factuel

Pour chaque ligne, vérifier sur Wikipedia :

1. Page ligne : `https://fr.wikipedia.org/wiki/Ligne_X_du_métro_de_Paris`
   - Section « Accessibilité » si présente
2. Si insuffisant, audit station par station :
   - `https://fr.wikipedia.org/wiki/Nom_station_(métro_de_Paris)`
   - Section « Accessibilité » de chaque page
3. Recouper avec :
   - IDFM officiel : <https://www.iledefrance-mobilites.fr/>
   - RATP officiel : <https://www.ratp.fr/>
   - Application Bonjour RATP (liste ascenseurs en service)

## Apprentissages bug L3bis (à NE PAS reproduire)

1. **Ne JAMAIS afficher 0 ascenseurs si des ascenseurs existent**
   — c'est une INFORMATION CRITIQUE pour PMR/parents/seniors.

2. **Distinction obligatoire dans l'UI** :
   - « Stations conformes norme PMR 2005 » : N
   - « Ascenseurs publics opérationnels (tous usages) » : M

   Le template `templates/components/line/accessibilite.php` a été
   mis à jour en ce sens (commit `8980fa9`).

3. **Bloc descriptif** : expliquer pourquoi la conformité 2005
   est plus restrictive que la simple présence d'ascenseurs
   (largeur, signalétique tactile, espacement quai-train, etc.).

## Apprentissages pour pages stations L1 à venir

Pour le LOT 1 stations L1 (5 stations majeures), checklist PMR
factuelle station par station :

| Station | Ascenseurs publics | PMR conforme 2005 | Source à vérifier |
|---|---|---|---|
| La Défense — Grande Arche | À vérifier (terminus moderne) | Probable oui | Wikipedia La Défense (métro) |
| Charles de Gaulle — Étoile | À vérifier (correspondance L2/L6/RER A modernisée) | Partiel probable | Wikipedia Étoile |
| Concorde | À vérifier (correspondance L8/L12 historiques) | Probablement non | Wikipedia Concorde |
| Tuileries | À vérifier (1900-1908 historique) | Probablement non | Wikipedia Tuileries |
| Palais Royal — Musée du Louvre | À vérifier (correspondance L7) | À vérifier | Wikipedia Palais Royal |

**Recommandation** : pour chaque station produite LOT 1, audit
PMR factuel via la section « Accessibilité » de la page Wikipedia
station avant de remplir le bloc accessibility.

## Recommandation Ludo

L'audit complet des 14 lignes nécessite **2-3 jours de travail
soutenu** (brief explicite). Approche recommandée par ordre de
priorité :

1. **L11** (priorité 1, risque sous-estimation 4 stations
   historiques profondes — Pyrénées, Jourdain, Place des Fêtes,
   Télégraphe)
2. **L1, L4** (priorité 2, lignes automatisées, valeurs
   probablement sous-estimées)
3. **L7, L9** (priorité 3, lignes longues à risque modéré)
4. **L2, L3, L5, L6, L8, L10, L12, L13** (priorité 4, valeurs
   plausibles à plausibilité moyenne)

L'audit station-par-station via Wikipedia est manuel et
chronophage — un agent Explore dédié pourrait industrialiser
cette tâche en délégant à un sub-agent (parallélisation).

## Cohérence naming « 3bis » / « 7bis »

Audit récent (commits `8980fa9` et `edd1221`) : les codes JSON
ont été uniformisés sur **« 3bis »** et **« 7bis »** (orthographe
complète Wikipedia/RATP/IDFM).

Avant correction :
- L3bis JSON : `code: "3B"`, `name: "Ligne 3B"`
- L7bis JSON : `code: "7B"`, `name: "Ligne 7B"`

Après :
- L3bis JSON : `code: "3bis"`, `name: "Ligne 3bis"`
- L7bis JSON : `code: "7bis"`, `name: "Ligne 7bis"`

Render local validé : 79 occurrences « ligne 3bis » / 0 « ligne
3B » sur la page L3bis, 82 / 0 sur la page L7bis.

## Status code

- ✅ Template `accessibilite.php` distingue les 2 métriques
  (commit `8980fa9`)
- ✅ Helper `darkenForWhiteText()` pour les pastilles RER
  (commit `131f43a`)
- ✅ Naming « bis » uniformisé sur L3bis et L7bis
- ⏳ Audit factuel station-par-station des 14 lignes restantes
  (différé, méthodologie documentée ci-dessus)
