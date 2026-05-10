# Stratégie de monétisation — BougeaParis.fr

**Statut : ANTICIPATION ARCHITECTURALE — pas d'implémentation active.**

## 4 zones publicitaires placeholder dans le template station

Le template `templates/pages/station-metro.php` intègre dès
maintenant 4 `<div class="ad-zone">` vides, positionnées
stratégiquement entre les sections existantes. **Tant qu'elles
sont vides**, elles sont masquées via `:empty { display: none }`
côté CSS — aucun impact sur le rendu actuel ni le PageSpeed.

| Zone | Position | Slot AdSense (futur) | Logique éditoriale |
|---|---|---|---|
| **post-hero** | Après hero, avant intro SEO | `data-ad-slot="post-hero"` | Visibilité maximale haut de page |
| **mid-content** | Entre Plan et Itinéraires | `data-ad-slot="mid-content"` | Pause naturelle entre transactionnel et exploratoire |
| **pre-footer-content** | Entre FAQ et Maillage | `data-ad-slot="pre-footer-content"` | Avant l'engagement de fin |
| **pre-maillage** | Juste avant le bloc « Continuer votre exploration » | `data-ad-slot="pre-maillage"` | Capture le scroll de fin de page |

## CSS

`assets/css/station.css` :

```css
.ad-zone {
    margin: 2rem 0;
    min-height: 90px; /* prévention CLS quand AdSense charge */
    text-align: center;
    overflow: hidden;
}
.ad-zone:empty {
    display: none; /* masqué tant que vide (V1) */
}
@media (min-width: 1024px) {
    .ad-zone--debug:empty {
        display: block;
        background: #f0f0f0;
        min-height: 90px;
        position: relative;
    }
    .ad-zone--debug:empty::before {
        content: "📢 Future zone AdSense";
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        color: #999;
        font-size: 0.85rem;
    }
}
```

**Mode debug** : ajouter la classe `ad-zone--debug` à une zone
pour la voir en mode rectangle gris pendant le développement.

## Phases d'activation

1. **Phase 0 (NOW)** : zones placeholder en place + masquées.
   Aucun code AdSense chargé. PageSpeed inchangé.
2. **Phase 1 — Attendre le trafic** : avant de demander AdSense,
   atteindre **min. 5 000 visiteurs uniques / mois** (cible
   AdSense pour acceptation). Concentrer l'effort sur la
   production de contenu (305 stations + clusters thématiques).
3. **Phase 2 — Demande d'approbation AdSense** :
   - Vérifier que toutes les pages ont du contenu original riche
     (≥ 1500 mots).
   - Mentions légales + politique de confidentialité (RGPD)
     déjà OK ✓.
   - Demander la validation manuelle Google AdSense.
4. **Phase 3 — Activation** :
   - Charger le script AdSense en `defer` ou `async` via Consent
     Mode v2 (déjà actif sur le site).
   - Insérer les `<ins class="adsbygoogle">` dans les 4 zones.
   - Activer la classe `.ad-zone--debug` ponctuellement pour
     valider visuellement les emplacements.
5. **Phase 4 — Optimisation** :
   - Mesurer RPM (revenu pour 1000 vues) par zone.
   - A/B tester la position mid-content (parfois avant POIs
     plutôt qu'avant Itinéraires).
   - Ajuster densité (4 zones max par page recommandé Google).

## Alternatives complémentaires à AdSense

| Solution | Type | Pertinence BougeaParis |
|---|---|---|
| **Booking.com (affiliation)** | Hôtels près des stations | ⭐⭐⭐ Très pertinent — hub touristique |
| **Tiqets / GetYourGuide** | Billets monuments | ⭐⭐⭐ Capture trafic POIs (Grande Arche, Tour Eiffel) |
| **Trainline / SNCF Connect** | Billets train | ⭐⭐ Pour `/tarifs/aeroports/` et `/transilien/` |
| **Airbnb** | Logements | ⭐⭐ Quartiers touristiques |
| **Vente directe** | Espaces sponsorisés | ⭐⭐⭐⭐ Long terme, négocié au cas par cas |

À étudier en parallèle d'AdSense, pas en remplacement (revenus
souvent complémentaires).

## Règles AdSense à respecter

- **Politique de contenu** : pas de contenu adulte, violent,
  drogue, alcool excessif. ✓ BougeaParis OK.
- **Densité publicitaire** : max 30 % d'écran couvert par les
  pubs. 4 zones × 250px ≈ 1000px sur 5000px de page = 20 %. ✓
- **Pas de clic incitatif** : ne jamais demander aux utilisateurs
  de cliquer sur les pubs.
- **Position du contenu principal** : pas masqué par les pubs.
  ✓ Toutes les pubs sont entre sections, pas au-dessus du fold.
- **Mobile-first** : les zones doivent être responsives.
  `min-height: 90px` posé pour éviter le CLS.

## Mesures Lighthouse à surveiller post-activation

| Métrique | Avant AdSense | Après AdSense (cible) |
|---|---|---|
| **LCP** | ~1.5 s | < 2.5 s (toléré pour AdSense en defer) |
| **CLS** | 0 | ≤ 0.1 (grâce au `min-height: 90px`) |
| **TBT** | 30 ms | < 200 ms |
| **Performance score** | 98 | ≥ 90 |

Si Performance < 90 après AdSense : envisager d'enlever 1 zone
(probablement `pre-footer-content` qui a le moins de visibilité).

## Composants à activer le moment venu

1. `templates/layout/base.php` : ajouter le `<script async
   src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXX">`
   conditionnellement (Consent Mode v2 actif).
2. `config/ads.php` (déjà partiellement présent) : injecter
   `enabled => true` + `publisher_id` + `slot_ids`.
3. `templates/pages/station-metro.php` : remplacer les
   `<div class="ad-zone"></div>` vides par
   `<div class="ad-zone"><ins class="adsbygoogle" data-ad-client
   ="ca-pub-XXX" data-ad-slot="YYY" data-ad-format="auto"
   data-full-width-responsive="true"></ins></div>`.

## Calendrier estimé

| Phase | Date cible | Préalables |
|---|---|---|
| Phase 0 | 2026-05-10 ✅ | Fait |
| Phase 1 (trafic 5k UV/mois) | Q4 2026 | Production 60+ stations, GSC optimisé |
| Phase 2 (demande AdSense) | Q1 2027 | Phase 1 atteinte |
| Phase 3 (activation) | Q1 2027 + 2-4 sem | Validation Google |
| Phase 4 (optimisation) | Q2 2027 | 2-3 mois de données |
