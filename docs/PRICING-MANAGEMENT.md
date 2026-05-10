# Gestion des tarifs IDFM — BougeaParis.fr

## Source unique de vérité

`public_html/data/global/transit-pricing.json` est le **seul** fichier
qui contient les tarifs IDFM (tickets, carnets, Navigo, gratuités,
zones tarifaires).

Toutes les pages station (305 cibles) lisent ce JSON via le helper
`transit_pricing()` (`core/helpers.php`). **Aucun prix en dur** n'est
toléré dans les templates ou le code applicatif.

## Mise à jour annuelle (procédure)

Les tarifs IDFM changent en général au **1er janvier** de chaque
année. À chaque mise à jour :

1. Vérifier les nouveaux tarifs sur [iledefrance-mobilites.fr/titres-et-tarifs](https://www.iledefrance-mobilites.fr/titres-et-tarifs)
2. Éditer `public_html/data/global/transit-pricing.json` :
   - Bloc `_meta.version` → nouvelle version (ex. `"2027-01-01"`)
   - Bloc `_meta.valid_from` → date d'entrée en vigueur (ex. `"2027-01-01"`)
   - Bloc `_meta.valid_to` → date de validité fin année (ex. `"2027-12-31"`)
   - Bloc `_meta.last_verified` → date du jour
   - Tous les `price_eur` modifiés
3. Tester en local : `php -S 127.0.0.1:8888 -t public_html public_html/index.php`
   puis ouvrir `/metro/station/la-defense-grande-arche/` et vérifier
   que les nouveaux prix apparaissent.
4. Commit + push (la workflow Deploy o2switch propage automatiquement).

**Important** : un seul fichier à modifier, propagation immédiate
sur les 305 pages station.

## Format des prix

Le helper `format_price($priceEur)` (dans `core/helpers.php`)
convertit un `float` en chaîne FR :
- `2.15` → `« 2,15 € »` (espace fine UTF-8 entre nombre et symbole)
- `0.00` → `« Gratuit »` (par défaut, sauf `format_price(0.0, false)`)

Pas de manipulation manuelle des prix dans les templates.

## Garde-fou expiration

Si la date du jour dépasse `_meta.valid_to`, le composant `tarifs.php`
affiche un avertissement orange en bas de section :
> **⚠️ Mise à jour annuelle requise** (les tarifs en cours de validité
> ont peut-être expiré, à recouper IDFM).

Un workflow GitHub Actions vérifie également cette date 1 fois par
mois (`.github/workflows/check-pricing-expiration.yml`) et marque
le run en `::warning::` si expiré.

## Personnalisation par station

Chaque JSON station peut déclarer un champ optionnel `tariff_zone`
(int, 1-5 selon zone IDFM) :
- Zone 1 : Paris intra-muros
- Zone 2 : petite couronne (92, 93, 94 limitrophes)
- Zone 3 : banlieue proche (Puteaux, Issy, Saint-Denis…)
- Zone 4-5 : grande couronne

Le composant `tarifs.php` adapte alors l'introduction (recommandation
Navigo Découverte si zone > 1, mention zone 1 sinon) sans dupliquer
les prix.

## Zones tarifaires LOT 1

| Station | Commune | Zone |
|---|---|---|
| La Défense — Grande Arche | Puteaux (92) | **3** |
| Charles de Gaulle — Étoile | Paris 8/16/17 | **1** |
| Concorde | Paris 8 | **1** |
| Tuileries | Paris 1 | **1** |
| Palais Royal — Musée du Louvre | Paris 1 | **1** |

## Format JSON détaillé

```json
{
  "_meta": {
    "version": "2026-01-01",
    "valid_from": "2026-01-01",
    "valid_to": "2026-12-31",
    "source_url": "https://www.iledefrance-mobilites.fr/titres-et-tarifs",
    "last_verified": "2026-05-10"
  },
  "tickets": {
    "ticket_t_plus": {
      "name": "Ticket t+",
      "icon": "🎫",
      "price_eur": 2.15,
      "type": "unitaire",
      "valid_for": "2 heures, métro/RER intra-Paris, correspondances illimitées",
      "ideal_for": "Voyage occasionnel"
    },
    ...
  },
  "passes": {
    "navigo_decouverte": {
      "card_price_eur": 5.00,
      "weekly_price_eur": 30.75,
      "monthly_price_eur": 88.80,
      ...
    }
  },
  "free_categories": [...],
  "zones": { "1": "Paris intra-muros", ... }
}
```

## Migration depuis l'ancien `data/tarifs.json`

L'ancien fichier `data/tarifs.json` (utilisé par le hub `/tarifs/`
historique) reste en place pour ne pas casser les pages existantes.
Le nouveau fichier `data/global/transit-pricing.json` est la
**source unique** pour les pages station.

À termes (V2), unifier en faisant pointer le hub `/tarifs/` aussi
vers `data/global/transit-pricing.json` et supprimer l'ancien.
