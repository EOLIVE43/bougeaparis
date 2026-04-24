# Livraison 4.2 — Auto-génération blog trafic

## À construire

### 1. ImageService.php (core/)
Service centralisé pour récupération d'images automatique.

**Sources :**
- **Unsplash API** — photos réelles (articles trafic, hubs lignes)
  - Clé API stockée dans GitHub Secrets + config/secrets.php (exclu FTP)
  - Rate limit : 50 req/h (suffisant pour 2-3 articles/jour)
  - Cacher les résultats dans /api/cache/unsplash/
  - Stocker nom photographe dans front-matter `image_credit`

- **Replicate API** — génération IA
  - Pour illustrations/visuels de marque (pas de photo pertinente)
  - Coût : ~0.003-0.01 $/image
  - Modèles candidats : Flux Schnell (rapide), SDXL

**Workflow :**
1. Script PRIM génère article du jour
2. Appel ImageService::fetch($keywords, $source)
3. Téléchargement + compression (cible <300 Ko, >1200px)
4. Upload FTP dans /assets/images/{category}/
5. Chemin injecté dans front-matter du .md

### 2. Script PRIM quotidien
- GitHub Actions cron @ 5h55 (pour publication 6h)
- Appel PRIM API → récupération trafic + perturbations
- Génération dual output :
  - 1 article blog global (Markdown)
  - 1 JSON par ligne (/data/traffic/YYYY-MM-DD.json)
- Appel ImageService pour illustration
- Commit + push → déploiement auto

### 3. Composant traffic-widget
- Encart "Aujourd'hui sur la ligne X" sur pages froides
- Lit JSON du jour filtré par ligne
- Lien vers article global

## Secrets à configurer dans GitHub

- UNSPLASH_ACCESS_KEY
- REPLICATE_API_TOKEN
- PRIM_API_KEY (déjà en place ?)

## Notes

- Repo public → Actions illimitées (OK pour cron quotidien)
- config/secrets.php exclu du FTP (cf deploy.yml)
- Respecter Core Web Vitals : images optimisées, lazy load
