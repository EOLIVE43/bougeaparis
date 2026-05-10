# Stratégie d'internationalisation (i18n) — BougeaParis.fr

**Statut : ANTICIPATION ARCHITECTURALE — pas d'implémentation active.**

Ce document fixe l'architecture cible pour les futures versions
**anglaise (EN)** et éventuellement **espagnole (ES)** du site.
Le but est de pouvoir activer plus tard sans toucher aux 305+
pages stations + pages éditoriales déjà produites.

## Architecture URL cible

Pattern **sous-dossier de langue** (recommandé Google pour le
SEO multilingue, Hreflang facile, partage de domaine, etc.).

| FR (par défaut) | EN | ES |
|---|---|---|
| `/` | `/en/` | `/es/` |
| `/metro/` | `/en/metro/` | `/es/metro/` |
| `/metro/ligne-1/` | `/en/metro/line-1/` | `/es/metro/linea-1/` |
| `/metro/station/chatelet/` | `/en/metro/station/chatelet/` | `/es/metro/estacion/chatelet/` |
| `/tarifs/` | `/en/fares/` | `/es/tarifas/` |
| `/tarifs/metro/` | `/en/fares/metro/` | `/es/tarifas/metro/` |
| `/tarifs/aeroports/` | `/en/fares/airports/` | `/es/tarifas/aeropuertos/` |
| `/info-trafic/` | `/en/live-traffic/` | `/es/info-trafico/` |
| `/a-propos/` | `/en/about/` | `/es/acerca-de/` |
| `/mentions-legales/` | `/en/legal/` | `/es/aviso-legal/` |
| `/contact/` | `/en/contact/` | `/es/contacto/` |

**Slugs stations** : conservés à l'identique (`chatelet`,
`la-defense-grande-arche`) — ce sont des noms propres,
internationalement reconnus.

**Slugs lignes** : `ligne-1` → `line-1` / `linea-1` (segment
traduit dans l'URL).

## Stratégie de traduction

| Type de contenu | Méthode | Validation |
|---|---|---|
| Hero / intro / FAQ / trivia / history | **IA + relecture humaine** | Auteur bilingue ou natif |
| Données factuelles (correspondances, sorties, horaires) | **Réutilisation directe** (chiffres et noms ne changent pas) | — |
| Schema.org | **Multilingue via inLanguage + sameAs Wikipedia EN/ES** | — |
| Métadonnées SEO (title, description) | **Rédaction humaine** (mots-clés différents par langue) | Auteur bilingue |
| Pastilles ligne (1, A, T2…) | **Identiques** (codes universels IDFM) | — |

## Pattern routage PHP cible

Préfixe de langue détecté dans `index.php` avant routage :

```php
$lang = 'fr'; // par défaut
if (preg_match('#^/(en|es)(/.*|$)#', $path, $m)) {
    $lang = $m[1];
    $path = $m[2] ?: '/';
}
// reste du routing identique, mais charge data['i18n'][$lang]
// si présent, sinon fallback FR.
```

**Routes::$active** : étendre avec patterns `/en/...` et
`/es/...` ou détecter le préfixe automatiquement.

## Format JSON station — champ `i18n`

Chaque JSON station prévoit dès maintenant un champ `i18n`
optionnel (initialement `null`, rempli au cas par cas) :

```json
{
  "slug": "chatelet",
  "name": "Châtelet",
  "name_full": "Châtelet — Métro & RER",
  ...
  "i18n": {
    "en": null,
    "es": null
  }
}
```

Quand on traduit, le champ devient :

```json
"i18n": {
  "en": {
    "name_full": "Châtelet — Metro & RER",
    "hero": {
      "tagline": "The busiest metro station in Paris",
      "description": "..."
    },
    "intro_paragraphs": ["...", "..."],
    "faq": [...],
    "trivia": [...],
    "history": {...},
    "practical_tips": [...]
  },
  "es": null
}
```

Champs **non-traduits** (correspondances, exits, schedule) :
fallback automatique sur les valeurs FR par défaut.

## Format JSON ligne — même pattern

```json
{
  "code": "1", "slug": "metro-1",
  "intros": {...},
  "i18n": {
    "en": { "intros": {...} },
    "es": null
  }
}
```

## Hreflang

À injecter dans `<head>` de chaque page (template
`layout/base.php` étendu) quand i18n actif :

```html
<link rel="alternate" hreflang="fr" href="https://bougeaparis.fr/...">
<link rel="alternate" hreflang="en" href="https://bougeaparis.fr/en/...">
<link rel="alternate" hreflang="es" href="https://bougeaparis.fr/es/...">
<link rel="alternate" hreflang="x-default" href="https://bougeaparis.fr/...">
```

Côté `Seo::renderHead()`, ajouter une méthode
`setAlternates(['en' => $url, 'es' => $url])` qui rend ces
balises.

## Schema.org

- `WebPage.inLanguage` = `fr-FR` / `en-US` / `es-ES` selon la page
- `BreadcrumbList` : maintenu, traduit selon la langue
- `FAQPage` : `name` et `text` traduits
- `SubwayStation.sameAs` : ajouter Wikipedia EN/ES quand dispo
  (`https://en.wikipedia.org/wiki/Châtelet_(Paris_Métro)`)

## Composants à modifier le moment venu

| Composant | Modification requise |
|---|---|
| `core/Template.php` | Accepter `$lang` en propriété, passer aux partials |
| `core/Seo.php` | Méthode `setAlternates()` + `setLanguage()` |
| `core/helpers.php` | Helper `t($key)` pour les chaînes UI traduites |
| `templates/layout/base.php` | `<html lang="...">` dynamique + balises hreflang |
| `templates/components/breadcrumb.php` | Labels traduits (Accueil → Home → Inicio) |
| `templates/components/station/*.php` | Lecture champ `$station['i18n'][$lang]` avec fallback FR |
| `templates/pages/*.php` | Idem pour les pages éditoriales (ces dernières probablement ré-écrites en EN, pas générées du JSON) |
| `Routes.php` | Patterns regex étendus avec préfixes optionnels `^/(en|es)?/...` |
| `index.php` | Détection préfixe + dispatch sur le bon Template |

## Phases d'activation

1. **Phase 0 (NOW)** : tous les JSON station/ligne ont déjà
   le champ `i18n` vide. Ce document existe.
2. **Phase 1** : implémenter le routage `/en/` (refonte
   `index.php` + `Routes` + helpers `t()`). Tester sur 1 page.
3. **Phase 2** : traduction de la page d'accueil + 1 station
   (Châtelet) + 1 hub tarifs comme pilote EN.
4. **Phase 3** : traduction des 5 stations LOT 1, 16 lignes
   métro, 3 pages tarifs.
5. **Phase 4** : scaling 305 stations en EN (probablement avec
   un workflow IA de traduction + relecture).
6. **Phase 5** : ouverture ES (même cycle).

## Points d'attention

- **URLs canoniques** : chaque langue a sa canonique propre
  (pas de redirection FR ↔ EN).
- **Sitemap** : XML multilingue (`<xhtml:link rel="alternate"
  hreflang="...">`).
- **Robots / Indexation** : laisser FR + EN + ES indexés en
  parallèle (pas de noindex sur EN).
- **Devise** : prix en € sur toutes les langues (Île-de-France
  Mobilités est € par essence). Pas de conversion USD.
- **Contenu factuel à risque de variation** : tarifs IDFM
  changent annuellement → mettre à jour `transit-pricing.json`
  une seule fois pour toutes les langues (les chiffres sont
  les mêmes).

## Décisions à trancher avant Phase 1

- [ ] Slug stations en EN : `chatelet` ou `châtelet` ? (UTF-8 OK
  mais pratique : conserver ASCII).
- [ ] Slug lignes RER : `rer-a` reste-t-il `rer-a` en EN, ou
  devient `rer-a` (identique car nom propre) ?
- [ ] Page tarifs : `/en/fares/` ou `/en/tickets/` ? (selon
  recherche mots-clés).
- [ ] Métriques SEO en EN : utiliser Ahrefs/SemRush pour les
  titres optimisés.
