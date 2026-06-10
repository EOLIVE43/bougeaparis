#!/usr/bin/env python3
"""Crée les 3 fiches détail aéroports parisiens (CDG, Orly, Beauvais)."""
import json
from pathlib import Path
ROOT = Path(__file__).parent.parent
AERO = ROOT / "public_html" / "data" / "aeroports"
AERO.mkdir(parents=True, exist_ok=True)

CONTENT = {
    "paris-charles-de-gaulle": {
        "name": "Paris-Charles de Gaulle",
        "full_name": "Aéroport Paris-Charles de Gaulle (CDG / Roissy)",
        "city": "Roissy-en-France",
        "department": "Val-d'Oise (95)",
        "distance_paris_km": 25,
        "iata": "CDG",
        "icao": "LFPG",
        "terminals": ["T1", "T2A", "T2B", "T2C", "T2D", "T2E", "T2F", "T2G", "T3"],
        "annual_traffic": "~67 millions",
        "rank_europe": 2,
        "rank_world": 9,
        "opened": "8 mars 1974",
        "operator": "Groupe ADP",
        "seo_title": "Aéroport Paris-Charles de Gaulle (CDG/Roissy) : accès, transports 2026",
        "seo_description": "Comment aller à l'aéroport Paris-Charles de Gaulle (CDG/Roissy) depuis Paris : RER B, Roissybus, taxi forfait, navettes. Terminaux, prix et durées.",
        "tagline": "2e aéroport d'Europe — Roissy-en-France",
        "hero_desc": "<strong>Aéroport Paris-Charles de Gaulle</strong> (CDG / Roissy), à <strong>25 km au nord-est de Paris</strong>, dans le <strong>Val-d'Oise</strong> (95). <strong>2e aéroport d'Europe</strong> et <strong>9e mondial</strong> avec <strong>~67 millions de passagers</strong> par an. Inauguré le <strong>8 mars 1974</strong>. Exploité par le <strong>Groupe ADP</strong>.",
        "intro_paragraphs": [
            "L'<strong>aéroport Paris-Charles de Gaulle</strong>, communément appelé <strong>Roissy-CDG</strong>, est le <strong>plus grand aéroport de France</strong> et le <strong>2e d'Europe</strong> après London-Heathrow. Situé à <strong>25 km au nord-est de Paris</strong>, sur la commune de <strong>Roissy-en-France</strong> (Val-d'Oise, 95).",
            "<strong>Inauguré le 8 mars 1974</strong>, il porte le nom du <strong>général Charles de Gaulle</strong> (1890-1970), fondateur de la <strong>Cinquième République</strong>. Exploité par le <strong>Groupe ADP</strong> (Aéroports de Paris). <strong>~67 millions de passagers/an</strong> (2023), <strong>~480 000 mouvements d'avions</strong>.",
            "L'aéroport comporte <strong>3 terminaux principaux</strong> : <strong>Terminal 1</strong> (architecture circulaire iconique, 1974), <strong>Terminal 2</strong> (modules 2A à 2G), <strong>Terminal 3</strong> (low-cost). Le <strong>CDGVAL</strong> (métro automatique gratuit) relie les terminaux entre eux. <strong>Gare TGV Aéroport-CDG</strong> dans le Terminal 2."
        ],
        "history": [
            "L'<strong>aéroport Paris-Charles de Gaulle</strong> est conçu dès <strong>1957</strong> pour remplacer <strong>Paris-Orly</strong> devenu trop petit. Travaux entamés en <strong>1966</strong>. <strong>Inauguré le 8 mars 1974</strong> par le président <strong>Valéry Giscard d'Estaing</strong>.",
            "Le <strong>Terminal 1</strong>, conçu par l'architecte <strong>Paul Andreu</strong>, est un <strong>chef-d'œuvre d'architecture aéroportuaire</strong> avec sa <strong>forme circulaire</strong> et ses <strong>tubes vitrés</strong>. <strong>Capacité 10 millions de passagers/an</strong>. Style années 1970 préservé.",
            "Le <strong>Terminal 2</strong>, mis en service progressivement de <strong>1982 à 2008</strong>, est constitué de <strong>7 modules</strong> (2A à 2G). <strong>Gare TGV Aéroport-CDG</strong> intégrée en <strong>1994</strong> (LGV Nord). Accès direct vers <strong>Lille, Bruxelles, Londres, Marseille</strong>. <strong>Effondrement partiel du Terminal 2E</strong> en <strong>mai 2004</strong> (4 morts), reconstruction et réouverture en 2008."
        ],
        "access": {
            "rer_b": {
                "name": "RER B",
                "from": "Châtelet - Les Halles, Gare du Nord, Saint-Michel - Notre-Dame, Denfert-Rochereau",
                "time_min": 35,
                "price_eur": "11,80 à 13,00",
                "frequency_min": 10,
                "first_train": "04h53",
                "last_train": "00h15",
                "stops": ["Aéroport CDG 1", "Aéroport CDG 2 TGV"],
                "note": "Solution la plus rapide depuis le centre de Paris. Compris dans le pass Navigo zones 1-5."
            },
            "roissybus": {
                "name": "Roissybus",
                "from": "Opéra (place de l'Opéra, rue Scribe)",
                "time_min": 60,
                "price_eur": "16,60",
                "frequency_min": 15,
                "first_bus": "05h15",
                "last_bus": "00h30",
                "note": "Bus direct exploité par la RATP. Idéal depuis le 9e arrondissement."
            },
            "bus_350_351": {
                "name": "Bus 350 / 351",
                "from": "Gare de l'Est (350) / Place de la Nation (351)",
                "time_min": 75,
                "price_eur": "2,00",
                "frequency_min": 30,
                "note": "Solution la plus économique mais la plus longue."
            },
            "taxi": {
                "name": "Taxi",
                "from": "Paris intra-muros",
                "time_min": 60,
                "price_eur": "56 (Rive Droite) / 65 (Rive Gauche)",
                "note": "Tarif forfaitaire réglementé. Validez le forfait avec le chauffeur avant le départ."
            },
            "vtc": {
                "name": "VTC (Uber, Bolt, Heetch)",
                "from": "Paris intra-muros",
                "time_min": 50,
                "price_eur": "40 à 80 selon trafic et heure",
                "note": "Application mobile. Prix variable selon la demande."
            },
            "tgv": {
                "name": "TGV (Gare Aéroport-CDG-TGV)",
                "from": "Lille, Bruxelles, Londres, Marseille, Bordeaux",
                "time_min": "Variable",
                "note": "Gare TGV intégrée au Terminal 2 (1994). Connexion CDGVAL vers les autres terminaux."
            }
        },
        "terminals_detail": [
            {"code": "T1", "compagnies": "Star Alliance (Lufthansa, Air Canada, United, Turkish Airlines)", "year": 1974, "architect": "Paul Andreu"},
            {"code": "T2A/T2C", "compagnies": "SkyTeam (Air France, Delta, Korean Air, Aeroflot)", "year": "1982-1991"},
            {"code": "T2E/T2F", "compagnies": "Air France principales destinations + SkyTeam", "year": "1999-2008"},
            {"code": "T2G", "compagnies": "Air France court-courrier", "year": 2008},
            {"code": "T3", "compagnies": "Low-cost (Vueling, easyJet, Transavia)", "year": 1990}
        ],
        "faq": [
            ("Comment aller à CDG depuis Paris ?", "<strong>RER B</strong> (35 min depuis Châtelet, 11,80€) est le plus rapide. <strong>Roissybus</strong> (60 min depuis Opéra, 16,60€). <strong>Taxi</strong> forfait : 56€ (Rive Droite) / 65€ (Rive Gauche)."),
            ("Quel terminal pour Air France ?", "<strong>Terminal 2E, 2F</strong> ou <strong>2G</strong>. Vérifiez votre billet."),
            ("Combien coûte le RER B vers CDG ?", "<strong>11,80€</strong> billet plein tarif (12,80€ depuis CDG selon évolution tarifaire 2024-2025). Compris dans le pass Navigo zones 1-5."),
            ("Combien de temps en taxi de Paris à CDG ?", "<strong>~60 min</strong> en conditions normales. <strong>~90 min</strong> aux heures de pointe."),
            ("Y a-t-il des hôtels à CDG ?", "<strong>Oui</strong>. Hilton, Sheraton, Citizen M, Novotel, Mercure aux Terminaux 1, 2, et zone aéroportuaire."),
            ("Quand a-t-il été inauguré ?", "Le <strong>8 mars 1974</strong> par Valéry Giscard d'Estaing.")
        ],
        "nearby_pois": [
            {"name": "Roissy-en-France (village)", "description": "Commune de <strong>2 700 habitants</strong> donnant son nom à l'aéropoort. Église Saint-Eloi (XIIe siècle).", "distance_km": 5},
            {"name": "Parc Astérix", "description": "Parc d'attractions sur le thème de la <strong>BD d'Astérix</strong> (1989). 2e parc d'attractions de France après Disneyland.", "distance_km": 15},
            {"name": "Disneyland Paris", "description": "Parc d'attractions de <strong>Disney</strong> (1992). 1er parc d'attractions d'Europe.", "distance_km": 50}
        ]
    },
    "paris-orly": {
        "name": "Paris-Orly",
        "full_name": "Aéroport Paris-Orly (ORY)",
        "city": "Orly",
        "department": "Val-de-Marne (94)",
        "distance_paris_km": 14,
        "iata": "ORY",
        "icao": "LFPO",
        "terminals": ["Orly 1", "Orly 2", "Orly 3", "Orly 4"],
        "annual_traffic": "~33 millions",
        "rank_europe": 11,
        "rank_world": 50,
        "opened": "1932 (site actuel 1961)",
        "operator": "Groupe ADP",
        "seo_title": "Aéroport Paris-Orly (ORY) : accès, transports 2026, M14 depuis 2024",
        "seo_description": "Comment aller à l'aéroport Paris-Orly depuis Paris : métro 14 (depuis 2024), Orlyval+RER B, Orlybus, taxi forfait. Terminaux 1, 2, 3, 4.",
        "tagline": "2e aéroport Île-de-France — M14 depuis 2024",
        "hero_desc": "<strong>Aéroport Paris-Orly</strong> (ORY), à <strong>14 km au sud de Paris</strong>, dans le <strong>Val-de-Marne</strong> (94). <strong>2e aéroport d'Île-de-France</strong> avec <strong>~33 millions de passagers</strong> par an. Inauguré en <strong>1932</strong>, site actuel <strong>1961</strong>. Depuis <strong>juin 2024</strong>, accessible par la <strong>ligne 14 du métro</strong>.",
        "intro_paragraphs": [
            "L'<strong>aéroport Paris-Orly</strong>, communément appelé <strong>Orly</strong>, est le <strong>2e aéroport d'Île-de-France</strong> avec <strong>~33 millions de passagers par an</strong>. Situé à <strong>seulement 14 km au sud de Paris</strong>, sur la commune d'<strong>Orly</strong> (Val-de-Marne, 94).",
            "<strong>Historiquement le premier aéroport parisien</strong>. Ouvert en <strong>1932</strong> sur l'<strong>aérodrome de Villeneuve-Orly</strong>. Site actuel reconstruit en <strong>1961</strong> avec la création de l'<strong>aérogare Sud</strong>. Exploité par le <strong>Groupe ADP</strong>.",
            "<strong>Révolution 2024</strong> : depuis le <strong>24 juin 2024</strong>, l'aéroport est <strong>directement accessible depuis le centre de Paris en métro</strong> grâce au <strong>prolongement de la ligne 14</strong>. <strong>~25 min depuis Châtelet</strong>. Cette extension change radicalement l'accès à Orly."
        ],
        "history": [
            "L'<strong>aéroport d'Orly</strong> ouvre en <strong>1932</strong> sur l'<strong>aérodrome militaire de Villeneuve-Orly</strong>. Devient <strong>aéroport commercial principal</strong> de Paris dans l'<strong>entre-deux-guerres</strong>.",
            "Site actuel <strong>reconstruit en 1961</strong> avec création de l'<strong>aérogare Sud</strong> (architecte <strong>Henri Vicariot</strong>). Architecture moderne avec <strong>verrière monumentale</strong>. <strong>Aérogare Ouest</strong> en 1971.",
            "Avec l'<strong>ouverture de Charles de Gaulle en 1974</strong>, Orly devient le <strong>2e aéroport parisien</strong>. <strong>Fusion des aérogares Sud et Ouest</strong> en <strong>2019</strong> avec création de la <strong>numérotation Orly 1, 2, 3, 4</strong>. <strong>Extension de la ligne 14 du métro</strong> en <strong>juin 2024</strong> : révolution de l'accès."
        ],
        "access": {
            "metro_14": {
                "name": "Métro Ligne 14 (depuis juin 2024)",
                "from": "Châtelet, Gare de Lyon, Saint-Lazare, Olympiades, Bibliothèque François Mitterrand",
                "time_min": 25,
                "price_eur": "2,15 (ticket t+ ou Navigo zones 1-5)",
                "frequency_min": 4,
                "first_train": "05h30",
                "last_train": "00h15",
                "stops": ["Aéroport d'Orly"],
                "note": "🆕 NOUVEAU 2024. Solution la plus rapide et la plus économique depuis le centre de Paris. Compris dans le pass Navigo."
            },
            "orlyval_rer_b": {
                "name": "Orlyval + RER B",
                "from": "Châtelet - Les Halles, Denfert-Rochereau",
                "time_min": 40,
                "price_eur": "13,25",
                "frequency_min": 7,
                "first_train": "06h00 (Orlyval)",
                "last_train": "23h35 (Orlyval)",
                "note": "Train automatique reliant Orly à la gare RER B d'Antony. Combiné avec le RER B."
            },
            "orlybus": {
                "name": "Orlybus",
                "from": "Denfert-Rochereau",
                "time_min": 35,
                "price_eur": "11,50",
                "frequency_min": 15,
                "first_bus": "05h35",
                "last_bus": "00h30",
                "note": "Bus direct depuis Denfert. Idéal depuis le 14e arrondissement."
            },
            "tramway_t7": {
                "name": "Tramway T7",
                "from": "Villejuif - Louis Aragon (M7)",
                "time_min": 30,
                "price_eur": "2,15",
                "frequency_min": 8,
                "note": "Solution économique depuis le sud parisien via M7."
            },
            "taxi": {
                "name": "Taxi",
                "from": "Paris intra-muros",
                "time_min": 35,
                "price_eur": "36 (Rive Gauche) / 44 (Rive Droite)",
                "note": "Tarif forfaitaire réglementé. Plus rapide que CDG depuis Paris."
            },
            "vtc": {
                "name": "VTC (Uber, Bolt, Heetch)",
                "from": "Paris intra-muros",
                "time_min": 30,
                "price_eur": "30 à 60 selon trafic",
                "note": "Application mobile."
            }
        },
        "terminals_detail": [
            {"code": "Orly 1", "compagnies": "Vueling, easyJet, Transavia, low-cost", "year": "2019 (ex-Sud)"},
            {"code": "Orly 2", "compagnies": "Air France court-courrier, French Bee, Corsair", "year": "2019 (ex-Sud)"},
            {"code": "Orly 3", "compagnies": "Air France long-courrier, KLM, Delta, SkyTeam", "year": "2019 (ex-Ouest)"},
            {"code": "Orly 4", "compagnies": "Compagnies low-cost (Wizz Air, Ryanair, Volotea)", "year": "2019 (ex-Ouest)"}
        ],
        "faq": [
            ("Comment aller à Orly depuis Paris ?", "<strong>Ligne 14 du métro</strong> 🆕 (25 min depuis Châtelet, 2,15€). <strong>Orlyval + RER B</strong> (40 min, 13,25€). <strong>Orlybus</strong> (35 min depuis Denfert, 11,50€). <strong>Taxi</strong> forfait 36€ (Rive Gauche) / 44€ (Rive Droite)."),
            ("La ligne 14 va-t-elle vraiment à Orly ?", "<strong>Oui depuis le 24 juin 2024</strong>. Station <strong>Aéroport d'Orly</strong> (terminus sud). <strong>25 min depuis Châtelet</strong>. Solution la plus rapide et économique."),
            ("Combien coûte un taxi de Paris à Orly ?", "<strong>36€</strong> (Rive Gauche) ou <strong>44€</strong> (Rive Droite). <strong>Tarif forfaitaire réglementé</strong>."),
            ("Quel terminal pour Air France à Orly ?", "<strong>Orly 2</strong> (court-courrier) ou <strong>Orly 3</strong> (long-courrier)."),
            ("Combien de passagers à Orly ?", "<strong>~33 millions</strong> par an (2023). <strong>2e aéroport d'Île-de-France</strong>."),
            ("Quand l'aéroport a-t-il été inauguré ?", "<strong>1932</strong> initialement. <strong>Site actuel 1961</strong>.")
        ],
        "nearby_pois": [
            {"name": "Villejuif - Louis Aragon (M7)", "description": "Terminus M7 + tramway T7 vers Orly. <strong>Hub multimodal</strong> du Val-de-Marne.", "distance_km": 5},
            {"name": "Centre commercial Belle Épine", "description": "<strong>Centre commercial</strong> majeur du Val-de-Marne (1971). ~200 boutiques.", "distance_km": 3},
            {"name": "Parc départemental du Coteau", "description": "Parc départemental de <strong>13 hectares</strong> à proximité.", "distance_km": 2}
        ]
    },
    "paris-beauvais-tille": {
        "name": "Paris-Beauvais",
        "full_name": "Aéroport Paris-Beauvais-Tillé (BVA)",
        "city": "Beauvais",
        "department": "Oise (60)",
        "distance_paris_km": 85,
        "iata": "BVA",
        "icao": "LFOB",
        "terminals": ["T1", "T2"],
        "annual_traffic": "~5,7 millions",
        "rank_europe": "Hors top 50",
        "rank_world": "Hors top 100",
        "opened": "1936 (commercial 1956)",
        "operator": "SAGEB (concession)",
        "seo_title": "Aéroport Paris-Beauvais (BVA) : accès, navette, Ryanair, Wizz Air 2026",
        "seo_description": "Comment aller à l'aéroport Paris-Beauvais (BVA, low-cost Ryanair / Wizz Air) depuis Paris : navette officielle Porte Maillot 75 min 17€, train, taxi.",
        "tagline": "Aéroport low-cost — 85 km nord de Paris",
        "hero_desc": "<strong>Aéroport Paris-Beauvais-Tillé</strong> (BVA), à <strong>85 km au nord de Paris</strong>, dans l'<strong>Oise</strong> (60). <strong>Aéroport low-cost</strong> principalement utilisé par <strong>Ryanair</strong> et <strong>Wizz Air</strong>. <strong>~5,7 millions de passagers</strong> par an. Accessible depuis Paris par <strong>navette officielle</strong> (75 min, ~17€).",
        "intro_paragraphs": [
            "L'<strong>aéroport Paris-Beauvais-Tillé</strong> (BVA), situé à <strong>85 km au nord de Paris</strong> dans le département de l'<strong>Oise</strong> (60), est un <strong>aéroport low-cost</strong> principalement utilisé par <strong>Ryanair</strong> et <strong>Wizz Air</strong>. <strong>~5,7 millions de passagers/an</strong> (2023).",
            "<strong>Ouvert en 1936</strong> à des fins militaires, devient aéroport <strong>commercial en 1956</strong>. Connu sous le nom <strong>commercial « Paris-Beauvais »</strong> bien que la ville de Paris soit à <strong>85 km</strong>. Cette appellation a fait l'objet de <strong>controverses</strong> juridiques (DGCCRF condamnation en 2019).",
            "<strong>2 terminaux</strong> (T1, T2). Accessible depuis Paris uniquement par <strong>navette officielle</strong> (Porte Maillot, 75 min, ~17€) ou <strong>en voiture</strong>. <strong>Pas de gare TGV</strong> ni de <strong>connexion métro/RER directe</strong>. Petite gare SNCF de Beauvais à 8 km."
        ],
        "history": [
            "L'<strong>aéroport de Beauvais-Tillé</strong> est <strong>créé en 1936</strong> à des fins militaires. Devient <strong>aéroport commercial en 1956</strong>. Reste un <strong>petit aéroport régional</strong> jusqu'aux années 1990.",
            "<strong>Essor low-cost</strong> à partir de <strong>1997</strong> avec l'arrivée de <strong>Ryanair</strong> qui en fait sa <strong>base parisienne</strong>. <strong>Wizz Air</strong> rejoint en 2007. Trafic décuplé : <strong>~250 000 passagers en 1997, ~5,7 millions en 2023</strong>.",
            "<strong>Controverses sur l'appellation « Paris-Beauvais »</strong> : la <strong>DGCCRF</strong> condamna l'aéroport en <strong>2019</strong> pour <strong>pratique commerciale trompeuse</strong> (la ville de Paris est à 85 km, hors d'Île-de-France). Décision confirmée en appel. <strong>Concession</strong> exploitée par la <strong>SAGEB</strong> (Société aéroportuaire de Gestion et d'Exploitation de Beauvais)."
        ],
        "access": {
            "navette": {
                "name": "Navette officielle Aéroport Paris-Beauvais",
                "from": "Porte Maillot (Paris 17e)",
                "time_min": 75,
                "price_eur": "17,00 (aller simple) / 30,00 (aller-retour)",
                "frequency_min": "Coordonnée aux vols",
                "note": "Solution recommandée. Coordonnée avec les vols Ryanair et Wizz Air. <strong>Réservation en ligne</strong> recommandée."
            },
            "train_bus": {
                "name": "Train Paris-Nord + bus",
                "from": "Gare du Nord",
                "time_min": 90,
                "price_eur": "10 à 18 (TER) + 4 (bus)",
                "frequency_min": 60,
                "note": "TER vers <strong>Beauvais SNCF</strong> (1h15), puis <strong>bus 12 ou 14</strong> vers l'aéroport (15 min). Plus lent et moins fiable que la navette."
            },
            "taxi": {
                "name": "Taxi",
                "from": "Paris intra-muros",
                "time_min": 90,
                "price_eur": "180 à 250",
                "note": "<strong>Pas de tarif forfaitaire</strong>. <strong>Très onéreux</strong> en raison de la distance."
            },
            "voiture": {
                "name": "Voiture personnelle",
                "from": "Paris",
                "time_min": 80,
                "price_eur": "Variable (péage A16 ~3,80€ + parking)",
                "note": "<strong>Autoroute A16</strong> nord. Parkings aéroport payants (15-25€/jour)."
            }
        },
        "terminals_detail": [
            {"code": "T1", "compagnies": "Ryanair principalement", "year": "2003"},
            {"code": "T2", "compagnies": "Wizz Air, Volotea, divers low-cost", "year": "2010"}
        ],
        "faq": [
            ("Comment aller à Paris-Beauvais depuis Paris ?", "<strong>Navette officielle</strong> depuis Porte Maillot : 75 min, <strong>17€</strong> aller simple. <strong>Réservation en ligne</strong> recommandée."),
            ("L'aéroport de Beauvais est-il vraiment à Paris ?", "<strong>Non</strong>. L'aéroport est à <strong>85 km de Paris</strong>, dans l'<strong>Oise</strong> (60), <strong>hors d'Île-de-France</strong>. L'appellation « Paris-Beauvais » a fait l'objet de <strong>condamnations DGCCRF</strong> (2019)."),
            ("Quelles compagnies utilisent Beauvais ?", "<strong>Ryanair</strong> (base parisienne), <strong>Wizz Air</strong>, <strong>Volotea</strong>, autres compagnies low-cost."),
            ("Y a-t-il un train direct Paris ↔ Beauvais ?", "<strong>Non</strong>. <strong>TER Paris-Nord ↔ Beauvais SNCF</strong> (1h15), puis bus 12/14 vers l'aéroport (15 min). Solution lente."),
            ("Combien de temps en taxi Paris ↔ Beauvais ?", "<strong>~90 min</strong>. Coût : <strong>180 à 250€</strong> (pas de tarif forfaitaire)."),
            ("Combien de passagers à Beauvais ?", "<strong>~5,7 millions</strong> par an (2023). Aéroport low-cost.")
        ],
        "nearby_pois": [
            {"name": "Cathédrale Saint-Pierre de Beauvais", "description": "<strong>Cathédrale gothique</strong> XIIIe siècle, <strong>plus haut chœur gothique au monde</strong> (48,5 m). Centre-ville Beauvais.", "distance_km": 8},
            {"name": "Centre-ville Beauvais", "description": "Ville préfecture de l'<strong>Oise</strong>, <strong>~55 000 habitants</strong>. Mosaïque romaine, musée du MUDO.", "distance_km": 8},
            {"name": "Forêt de Compiègne", "description": "Vaste <strong>forêt royale</strong> à proximité (14 000 ha).", "distance_km": 50}
        ]
    }
}

def enrich(slug, c):
    p = AERO / f"{slug}.json"
    d = {
        "slug": slug,
        "name": c["name"],
        "full_name": c["full_name"],
        "city": c["city"],
        "department": c["department"],
        "distance_paris_km": c["distance_paris_km"],
        "iata": c["iata"],
        "icao": c["icao"],
        "terminals": c["terminals"],
        "annual_traffic": c["annual_traffic"],
        "rank_europe": c["rank_europe"],
        "rank_world": c["rank_world"],
        "opened": c["opened"],
        "operator": c["operator"],
        "seo": {
            "title": c["seo_title"],
            "description": c["seo_description"]
        },
        "hero": {
            "tagline": c["tagline"],
            "description": c["hero_desc"]
        },
        "intro_paragraphs": c["intro_paragraphs"],
        "history": c["history"],
        "access": c["access"],
        "terminals_detail": c["terminals_detail"],
        "faq": [{"question": q, "answer": a} for q, a in c["faq"]],
        "nearby_pois": c["nearby_pois"],
        "published": True,
        "hero_image": {
            "url": f"https://bougeaparis.fr/assets/img/aeroports/{slug}/source/wikimedia.jpg",
            "alt": f"Vue de l'{c['full_name']}",
            "credit": {
                "license": "CC BY-SA",
                "source": "Wikimedia Commons"
            }
        }
    }
    p.write_text(json.dumps(d, indent=4, ensure_ascii=False) + "\n")
    print(f"✓ {slug}")

if __name__ == "__main__":
    for slug, c in CONTENT.items():
        try: enrich(slug, c)
        except Exception as e: print(f"✗ {slug}: {e}")
