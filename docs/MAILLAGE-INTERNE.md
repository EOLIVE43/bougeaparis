# Règle de maillage interne — BougeaParis.fr

Ce document fixe la règle de placement des liens internes sur les
pages publiques. Il s'applique à toutes les pages, en particulier
les pages station (305 cibles) et ligne (16 + RER).

## Principe

> **Les liens internes vivent dans les composants structurels,
> JAMAIS dans le texte rédactionnel narratif.**

Le texte narratif (intro SEO, anecdotes, FAQ, histoire, descriptions)
reste propre, lisible, sans liens pollueurs. Le maillage interne est
porté par les composants structurels (pastilles, cards, listes,
breadcrumbs, navigation) où il est ergonomique et attendu.

## ✅ Maillage interne OUI

Composants où les liens internes sont posés :

| Composant | Pattern | URL cible |
|---|---|---|
| Pastilles métro / RER | `<a class="correspondance-line-badge">` | `/metro/ligne-N/`, `/rer/rer-X/` |
| Pastilles tram / transilien / **bus** | idem (Routes::exists) | `/tramway/tN/`, `/transilien/transilien-X/`, `/bus/ligne-N/` |
| Cards POIs | `<a>` autour de l'image + nom | `/{categorie}/{slug}/` (futur) |
| Cards stations adjacentes | `<a class="adjacent-station-name">` | `/metro/station/{slug}/` |
| Cards itinéraires (titre) | `<a>` dans `<h4 data-future-url>` | `/itineraires/station-X/X-vers-Y/` |
| Hub link itinéraires | `<a class="itineraires-hub-link__btn">` | `/itineraires/station-X/` |
| Breadcrumbs | `<a>` chaque segment | `/{ancetre}/` |
| Quick-links | `<a class="quick-link">` | varié |
| Tableau horaires | `<a>` sur badge ligne | `/metro/ligne-N/` |

## ❌ Maillage interne NON

Sections où les liens internes sont **interdits** :

- `intro_paragraphs` — texte SEO long, narratif
- `faq.answer` — réponse rédactionnelle
- `practical_tips` — conseils
- `history.paragraphs` — narration historique
- `trivia.content` — anecdotes éditoriales
- `hero.description` — pitch d'accroche
- `seo.description` — meta description

Si l'auteur veut **insister** sur un mot-clé dans ces zones, il
peut utiliser `<strong>` ou `<em>` (rendu via `richText()`),
mais **pas un lien**.

## Pattern « lien progressif » via `Routes::exists()`

Pour anticiper les pages futures sans casser les URLs présentes,
on pose le lien systématiquement dans le composant structurel,
mais on délègue l'activation à la liste blanche `Routes::$active`.

```php
$url = '/bus/ligne-' . strtolower($code) . '/';
if (Routes::exists(rtrim($url, '/'))) {
    // Page existe → <a href> cliquable
    echo '<a href="' . e($url) . '" class="badge">' . e($code) . '</a>';
} else {
    // Page n'existe pas → <span> statique avec data-future-url
    // pour traçabilité du cocon SEO posé en avance.
    echo '<span class="badge" data-future-url="' . e($url) . '">'
       . e($code) . '</span>';
}
```

**Bénéfice** : le jour où la page `/bus/ligne-73/` est créée, il
suffit d'ajouter le slug dans `core/Routes.php::$active`. **Aucune
réécriture de page** n'est nécessaire — toutes les 305 pages
station qui mentionnent le bus 73 deviennent automatiquement
cliquables.

## Helpers disponibles

Dans `core/bootstrap.php` (déjà chargés via autoload + helpers) :

- `Routes::exists($path)` — booléen, accepte URL exacte ou pattern regex
- `conditionalLink($url, $label, $class)` — sucre `<a>` ou `<span>`
- `conditionalLinkOpen($url, $class)` / `conditionalLinkClose($url)` — pour wrapper du contenu HTML complexe
- `stationLink($name, $class)` — sucre `Routes::stationUrl + conditionalLink`

## Activation d'un nouveau cluster

Quand un nouveau cluster est livré (ex. cluster Bus), 3 actions
suffisent pour propager le maillage à tout le site :

1. Ajouter les routes dans `Routes::$active` (URLs ou patterns regex).
2. Ajouter les slugs spécifiques (ex. `Routes::$activeBusLines`).
3. Vérifier sur 1-2 pages station que les pastilles deviennent cliquables.

Ce sont les **seuls** endroits à modifier — pas de search/replace
sur les 305 pages station.

## Rappels SEO

- Un lien interne dans un composant structurel = ancre prévisible,
  facile à crawler.
- Un lien dans une phrase narrative = bruit pour le lecteur,
  signal SEO faible (Google déprécie les ancres opportunistes
  intra-paragraphe depuis 2022).
- Le texte rédactionnel doit être **lu**, pas **scanné** —
  préserver la lisibilité prime sur l'ajout d'ancres.

## Historique

- 2026-05-09 : règle posée, application initiale sur la station
  La Défense (commit `bd4c044` puis pattern Routes::exists() sur
  pastilles bus + titres cards itinéraires).
- Hub link itinéraires + pastilles métro/RER/tram/transilien
  utilisent déjà ce pattern depuis la genèse du projet.
