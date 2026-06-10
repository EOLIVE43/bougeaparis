#!/usr/bin/env python3
"""Crée/met à jour les 3 fiches détail aéroports parisiens avec hero_image
et sections H2 SEO (intentions de recherche GKP)."""
import json
from pathlib import Path
ROOT = Path(__file__).parent.parent
AERO = ROOT / "public_html" / "data" / "aeroports"
AERO.mkdir(parents=True, exist_ok=True)


def hero_image(slug, alt, author, license_, source_url):
    return {
        "url": f"https://bougeaparis.fr/assets/img/aeroports/{slug}/source/wikimedia.jpg",
        "alt": alt,
        "width": 1200,
        "height": 675,
        "source": "wikimedia",
        "credit": {
            "author": author,
            "license": license_,
            "license_url": "https://creativecommons.org/licenses/by-sa/4.0",
            "source_url": source_url
        },
        "keep_hero": True,
        "local_versions": {
            "avif": {str(w): f"/assets/img/aeroports/{slug}/{slug}-{w}.avif" for w in (400, 800, 1200, 1600)},
            "webp": {str(w): f"/assets/img/aeroports/{slug}/{slug}-{w}.webp" for w in (400, 800, 1200, 1600)},
            "jpg":  {str(w): f"/assets/img/aeroports/{slug}/{slug}-{w}.jpg"  for w in (400, 800, 1200, 1600)},
        }
    }


CONTENT = {
    "paris-charles-de-gaulle": {
        "name": "Paris-Charles de Gaulle",
        "full_name": "Aéroport Paris-Charles de Gaulle (CDG / Roissy)",
        "city": "Roissy-en-France", "department": "Val-d'Oise (95)",
        "distance_paris_km": 25, "iata": "CDG", "icao": "LFPG",
        "terminals": ["T1", "T2A", "T2B", "T2C", "T2D", "T2E", "T2F", "T2G", "T3"],
        "annual_traffic": "~67 millions", "rank_europe": 2, "rank_world": 9,
        "opened": "8 mars 1974", "operator": "Groupe ADP",
        "h1": "Aéroport Paris-Charles de Gaulle (CDG) : guide d'accès complet",
        "seo_title": "Aéroport Paris-Charles de Gaulle (CDG/Roissy) : accès RER B, Roissybus, taxi 2026",
        "seo_description": "Comment aller à l'aéroport Paris-Charles de Gaulle (CDG / Roissy) depuis Paris : RER B 35 min, Roissybus 60 min, taxi forfait 56€/65€. Terminaux, prix et durées 2026.",
        "tagline": "2e aéroport d'Europe — Roissy-en-France (25 km nord-est Paris)",
        "hero_desc": "<strong>Aéroport Paris-Charles de Gaulle</strong> (CDG / Roissy), à <strong>25 km au nord-est de Paris</strong>, dans le <strong>Val-d'Oise</strong> (95). <strong>2e aéroport d'Europe</strong> et <strong>9e mondial</strong> avec <strong>~67 millions de passagers</strong> par an. Inauguré le <strong>8 mars 1974</strong>. Exploité par le <strong>Groupe ADP</strong>.",
        "hero_image": hero_image(
            "paris-charles-de-gaulle",
            "Vue aérienne de l'aéroport Paris-Charles de Gaulle (CDG / Roissy)",
            "Wilfredor",
            "CC0",
            "https://commons.wikimedia.org/wiki/File:Charles_de_Gaulle_International_Airport_in_France.jpg"
        ),
        "intro_paragraphs": [
            "L'<strong>aéroport Paris-Charles de Gaulle</strong>, communément appelé <strong>Roissy-CDG</strong>, est le <strong>plus grand aéroport de France</strong> et le <strong>2e d'Europe</strong> après London-Heathrow. Situé à <strong>25 km au nord-est de Paris</strong>, sur la commune de <strong>Roissy-en-France</strong> (Val-d'Oise, 95).",
            "<strong>Inauguré le 8 mars 1974</strong>, il porte le nom du <strong>général Charles de Gaulle</strong> (1890-1970), fondateur de la <strong>Cinquième République</strong>. Exploité par le <strong>Groupe ADP</strong> (Aéroports de Paris). <strong>~67 millions de passagers/an</strong> (2023), <strong>~480 000 mouvements d'avions</strong>.",
            "L'aéroport comporte <strong>3 terminaux principaux</strong> : <strong>Terminal 1</strong> (architecture circulaire iconique, 1974, Paul Andreu), <strong>Terminal 2</strong> (modules 2A à 2G), <strong>Terminal 3</strong> (low-cost). Le <strong>CDGVAL</strong> (métro automatique gratuit) relie les terminaux entre eux. <strong>Gare TGV Aéroport-CDG</strong> intégrée au Terminal 2."
        ],
        "sections": [
            {
                "h2": "RER B : la ligne directe vers Charles de Gaulle",
                "anchor": "rer-b",
                "paragraphs": [
                    "Le <strong>RER B</strong> est la <strong>solution la plus rapide</strong> pour rejoindre l'aéroport <strong>Paris-Charles de Gaulle</strong> depuis le centre de Paris. <strong>35 min depuis Châtelet - Les Halles</strong>, avec arrêts intermédiaires à <strong>Gare du Nord</strong>, <strong>Saint-Michel - Notre-Dame</strong>, <strong>Denfert-Rochereau</strong>.",
                    "<strong>Prix du billet</strong> : <strong>11,80 €</strong> à <strong>13,00 €</strong> selon le sens. Compris dans le <strong>pass Navigo Découverte zones 1-5</strong>. Trains toutes les <strong>10 à 20 minutes</strong> selon l'heure.",
                    "<strong>Deux gares</strong> dans l'aéroport : <strong>Aéroport CDG 1</strong> (Terminal 1 via CDGVAL) et <strong>Aéroport CDG 2 TGV</strong> (Terminaux 2A-2F, gare directe). <strong>Premier train à 04h53, dernier à 00h15</strong>."
                ],
                "table": {
                    "headers": ["Critère", "Valeur"],
                    "rows": [
                        ["Durée depuis Châtelet", "35 min"],
                        ["Prix billet", "11,80 € - 13,00 €"],
                        ["Fréquence", "10-20 min"],
                        ["Premier train", "04h53"],
                        ["Dernier train", "00h15"]
                    ]
                }
            },
            {
                "h2": "Roissybus : bus direct depuis Opéra",
                "anchor": "roissybus",
                "paragraphs": [
                    "Le <strong>Roissybus</strong> est un <strong>bus direct</strong> exploité par la <strong>RATP</strong> reliant la <strong>place de l'Opéra</strong> (Paris 9e, rue Scribe) à l'<strong>aéroport Paris-Charles de Gaulle</strong>.",
                    "<strong>Durée : 60 à 75 min</strong> selon le trafic. <strong>Prix : 16,60 €</strong>. <strong>Fréquence : toutes les 15 min</strong>. Premier départ <strong>05h15</strong>, dernier <strong>00h30</strong>. Idéal depuis le <strong>quartier de l'Opéra</strong> ou les <strong>Grands Boulevards</strong>."
                ],
                "table": {
                    "headers": ["Critère", "Valeur"],
                    "rows": [
                        ["Depuis", "Opéra (Paris 9e)"],
                        ["Durée", "60-75 min"],
                        ["Prix", "16,60 €"],
                        ["Fréquence", "15 min"]
                    ]
                }
            },
            {
                "h2": "Bus 350 et 351 : options économiques",
                "anchor": "bus-350-351",
                "paragraphs": [
                    "Pour rejoindre <strong>Paris-Charles de Gaulle</strong> à <strong>petit prix</strong>, les <strong>bus 350</strong> (Gare de l'Est) et <strong>351</strong> (Place de la Nation) sont les options les <strong>moins chères</strong>.",
                    "<strong>Prix : 2,00 €</strong> (ticket t+ standard). <strong>Durée : 75 à 90 min</strong>. <strong>Fréquence : 30 min</strong>. Plus longs mais accessibles avec un simple ticket métro."
                ]
            },
            {
                "h2": "Taxi à CDG : forfait Paris ↔ aéroport",
                "anchor": "taxi",
                "paragraphs": [
                    "Le <strong>taxi parisien</strong> applique un <strong>tarif forfaitaire réglementé</strong> pour les courses entre Paris intra-muros et <strong>Paris-Charles de Gaulle</strong>.",
                    "<strong>Tarifs forfait 2024</strong> : <strong>56 €</strong> depuis la <strong>Rive Droite</strong>, <strong>65 €</strong> depuis la <strong>Rive Gauche</strong>. Validez le forfait avec le chauffeur avant le départ. <strong>Durée : ~60 min</strong> en conditions normales, jusqu'à 90 min aux heures de pointe.",
                    "<strong>VTC</strong> (Uber, Bolt, Heetch) : <strong>40 à 80 €</strong> selon trafic et heure. Prix variable, à comparer."
                ]
            },
            {
                "h2": "TGV vers CDG : gare Aéroport-Charles de Gaulle-TGV",
                "anchor": "tgv",
                "paragraphs": [
                    "L'aéroport CDG dispose d'une <strong>gare TGV intégrée</strong> au <strong>Terminal 2</strong>, opérationnelle depuis <strong>1994</strong>.",
                    "Liaisons TGV directes : <strong>Lille</strong>, <strong>Bruxelles</strong>, <strong>Londres</strong>, <strong>Marseille</strong>, <strong>Bordeaux</strong>, <strong>Nantes</strong>, <strong>Strasbourg</strong>. Connexion <strong>CDGVAL</strong> vers les autres terminaux."
                ]
            },
            {
                "h2": "Terminaux Charles de Gaulle (T1, T2A-G, T3)",
                "anchor": "terminaux",
                "paragraphs": [
                    "L'aéroport compte <strong>3 terminaux principaux</strong> répartis sur un vaste site."
                ],
                "table": {
                    "headers": ["Terminal", "Compagnies principales", "Année"],
                    "rows": [
                        ["T1", "Star Alliance (Lufthansa, United, Turkish)", "1974 (Paul Andreu)"],
                        ["T2A / T2C", "SkyTeam (Delta, Korean Air)", "1982-1991"],
                        ["T2E / T2F", "Air France + SkyTeam", "1999-2008"],
                        ["T2G", "Air France court-courrier", "2008"],
                        ["T3", "Low-cost (Vueling, easyJet, Transavia)", "1990"]
                    ]
                }
            },
            {
                "h2": "CDGVAL : navette inter-terminaux gratuite",
                "anchor": "cdgval",
                "paragraphs": [
                    "Le <strong>CDGVAL</strong> est un <strong>métro automatique gratuit</strong> reliant les <strong>3 terminaux</strong> entre eux et les <strong>parkings PR-PX</strong>. <strong>Fréquence : 4 min</strong>. <strong>24h/24</strong>."
                ]
            },
            {
                "h2": "Tableau comparatif des modes d'accès CDG",
                "anchor": "comparatif",
                "table": {
                    "headers": ["Mode", "Depuis", "Durée", "Prix"],
                    "rows": [
                        ["RER B", "Châtelet", "35 min", "11,80 €"],
                        ["Roissybus", "Opéra", "60-75 min", "16,60 €"],
                        ["Bus 350/351", "Gare Est / Nation", "75-90 min", "2,00 €"],
                        ["Taxi", "Paris", "60 min", "56 € / 65 €"],
                        ["VTC", "Paris", "50 min", "40-80 €"],
                        ["TGV", "Lille, Bruxelles…", "Variable", "Variable"]
                    ]
                }
            }
        ],
        "history": [
            "L'<strong>aéroport Paris-Charles de Gaulle</strong> est conçu dès <strong>1957</strong> pour remplacer <strong>Paris-Orly</strong> devenu trop petit. Travaux entamés en <strong>1966</strong>. <strong>Inauguré le 8 mars 1974</strong> par le président <strong>Valéry Giscard d'Estaing</strong>.",
            "Le <strong>Terminal 1</strong>, conçu par <strong>Paul Andreu</strong>, est un <strong>chef-d'œuvre d'architecture aéroportuaire</strong> avec sa <strong>forme circulaire</strong> et ses <strong>tubes vitrés</strong>. <strong>Style années 1970</strong> préservé.",
            "Le <strong>Terminal 2</strong>, mis en service progressivement de <strong>1982 à 2008</strong>, est constitué de <strong>7 modules</strong> (2A à 2G). <strong>Gare TGV Aéroport-CDG</strong> intégrée en <strong>1994</strong>."
        ],
        "faq": [
            ("Comment aller à CDG depuis Paris ?", "<strong>RER B</strong> (35 min/11,80€) est le plus rapide. <strong>Roissybus</strong> (60-75 min/16,60€). <strong>Taxi forfait</strong> : 56€ Rive Droite / 65€ Rive Gauche."),
            ("Quel terminal pour Air France ?", "<strong>Terminal 2E, 2F</strong> ou <strong>2G</strong>. Vérifiez votre billet pour le sous-terminal exact."),
            ("Combien coûte le RER B vers CDG ?", "<strong>11,80 €</strong> en 2024-2025 (12,80 € selon évolution). Compris dans le pass Navigo zones 1-5."),
            ("Combien de temps en taxi Paris → CDG ?", "<strong>~60 min</strong> en conditions normales. <strong>~90 min</strong> aux heures de pointe (8h-10h, 17h-20h)."),
            ("Y a-t-il un train TGV à CDG ?", "<strong>Oui</strong>. <strong>Gare TGV Aéroport-CDG</strong> au Terminal 2. Liaisons vers Lille, Bruxelles, Londres, Marseille, Bordeaux."),
            ("Le RER B est-il direct vers CDG ?", "<strong>Oui</strong> depuis Châtelet, Gare du Nord, Saint-Michel et Denfert. Vérifiez la destination du train : « Aéroport CDG 2 TGV » ou « Mitry-Claye ».")
        ],
        "nearby_pois": [
            {"name": "Roissy-en-France (village)", "description": "Commune de <strong>2 700 habitants</strong> donnant son nom à l'aéroport. Église Saint-Eloi (XIIe siècle).", "distance_km": 5},
            {"name": "Parc Astérix", "description": "Parc d'attractions sur le thème de la <strong>BD d'Astérix</strong> (1989). 2e parc d'attractions de France.", "distance_km": 15},
            {"name": "Disneyland Paris", "description": "Parc d'attractions <strong>Disney</strong> (1992). 1er parc d'attractions d'Europe.", "distance_km": 50}
        ]
    },
    "paris-orly": {
        "name": "Paris-Orly",
        "full_name": "Aéroport Paris-Orly (ORY)",
        "city": "Orly", "department": "Val-de-Marne (94)",
        "distance_paris_km": 14, "iata": "ORY", "icao": "LFPO",
        "terminals": ["Orly 1", "Orly 2", "Orly 3", "Orly 4"],
        "annual_traffic": "~33 millions", "rank_europe": 11, "rank_world": 50,
        "opened": "1932 (site actuel 1961)", "operator": "Groupe ADP",
        "h1": "Aéroport Paris-Orly (ORY) : guide d'accès complet (métro 14, bus, RER)",
        "seo_title": "Aéroport Paris-Orly (ORY) : métro 14, Orlybus, Orlyval, taxi 2026",
        "seo_description": "Comment aller à l'aéroport Paris-Orly depuis Paris : ligne 14 du métro (25 min, 2,15€ depuis juin 2024), Orlybus 35 min, Orlyval + RER B, tramway T7, taxi forfait 36€/44€.",
        "tagline": "M14 depuis juin 2024 — 14 km sud Paris",
        "hero_desc": "<strong>Aéroport Paris-Orly</strong> (ORY), à <strong>14 km au sud de Paris</strong>, dans le <strong>Val-de-Marne</strong> (94). <strong>2e aéroport d'Île-de-France</strong> avec <strong>~33 millions de passagers</strong> par an. Inauguré en <strong>1932</strong>, site actuel <strong>1961</strong>. Depuis <strong>juin 2024</strong>, accessible par la <strong>ligne 14 du métro</strong>.",
        "hero_image": hero_image(
            "paris-orly",
            "Vue aérienne de l'aéroport Paris-Orly",
            "Bacon Noodles (Wikipedia)",
            "Domaine public",
            "https://commons.wikimedia.org/wiki/File:Paris-Orly_Aerial.jpg"
        ),
        "intro_paragraphs": [
            "L'<strong>aéroport Paris-Orly</strong>, communément appelé <strong>Orly</strong>, est le <strong>2e aéroport d'Île-de-France</strong> avec <strong>~33 millions de passagers par an</strong>. Situé à <strong>seulement 14 km au sud de Paris</strong>, sur la commune d'<strong>Orly</strong> (Val-de-Marne, 94).",
            "<strong>Révolution 2024</strong> : depuis le <strong>24 juin 2024</strong>, l'aéroport est <strong>directement accessible depuis le centre de Paris en métro</strong> grâce au <strong>prolongement de la ligne 14</strong>. <strong>~25 min depuis Châtelet</strong>. Cette extension change radicalement l'accès à Orly.",
            "<strong>Historiquement le premier aéroport parisien</strong>. Ouvert en <strong>1932</strong>. Site actuel reconstruit en <strong>1961</strong> avec création de l'<strong>aérogare Sud</strong> par <strong>Henri Vicariot</strong>. <strong>4 terminaux</strong> (Orly 1 à 4 depuis la fusion de 2019). Exploité par le <strong>Groupe ADP</strong>."
        ],
        "sections": [
            {
                "h2": "Métro ligne 14 vers Orly : la nouvelle liaison directe (2024)",
                "anchor": "metro-14",
                "paragraphs": [
                    "Depuis le <strong>24 juin 2024</strong>, l'<strong>aéroport Paris-Orly</strong> est <strong>directement accessible depuis le centre de Paris en métro</strong> grâce au <strong>prolongement sud de la ligne 14</strong>. Cette ouverture transforme radicalement l'accès à Orly et en fait la <strong>solution la plus rapide et économique</strong>.",
                    "<strong>Durée : 25 min depuis Châtelet</strong>. <strong>Prix : 2,15 €</strong> (ticket t+ ou pass Navigo zones 1-5). <strong>Fréquence : 4 min en pointe</strong>. Premier train <strong>05h30</strong>, dernier <strong>00h15</strong>.",
                    "La ligne 14, <strong>entièrement automatique</strong>, dessert : <strong>Saint-Lazare</strong>, <strong>Madeleine</strong>, <strong>Pyramides</strong>, <strong>Châtelet</strong>, <strong>Gare de Lyon</strong>, <strong>Bercy</strong>, <strong>Bibliothèque François Mitterrand</strong>, <strong>Olympiades</strong>, puis terminus <strong>Aéroport d'Orly</strong>.",
                    "Cette ligne est aussi <strong>la plus économique</strong> de toutes les options Paris → Orly. Elle remplace progressivement Orlyval (RER B + navette) pour la plupart des voyageurs."
                ],
                "table": {
                    "headers": ["Critère", "Valeur"],
                    "rows": [
                        ["Durée depuis Châtelet", "25 min"],
                        ["Prix billet", "2,15 €"],
                        ["Fréquence", "4 min (pointe)"],
                        ["Premier train", "05h30"],
                        ["Dernier train", "00h15"],
                        ["Station finale", "Aéroport d'Orly"]
                    ]
                }
            },
            {
                "h2": "Bus pour Orly : Orlybus, 183, 285",
                "anchor": "bus",
                "paragraphs": [
                    "Plusieurs <strong>bus desservent l'aéroport Paris-Orly</strong> depuis différents quartiers de Paris.",
                    "L'<strong>Orlybus</strong> est le bus direct emblématique reliant <strong>Denfert-Rochereau</strong> (Paris 14e) à <strong>Orly</strong>. <strong>Durée : 35 min</strong>. <strong>Prix : 11,50 €</strong>. <strong>Fréquence : 15 min</strong>. Premier départ <strong>05h35</strong>, dernier <strong>00h30</strong>.",
                    "Le <strong>bus 183</strong> relie <strong>Porte de Choisy</strong> à Orly (45 min, 2,15€). Le <strong>bus 285</strong> dessert Orly depuis Villejuif Louis Aragon. Solutions économiques mais plus longues."
                ],
                "table": {
                    "headers": ["Bus", "Depuis", "Durée", "Prix"],
                    "rows": [
                        ["Orlybus", "Denfert-Rochereau", "35 min", "11,50 €"],
                        ["183", "Porte de Choisy", "45 min", "2,15 €"],
                        ["285", "Villejuif - Louis Aragon", "30 min", "2,15 €"]
                    ]
                }
            },
            {
                "h2": "RER B + Orlyval vers Orly",
                "anchor": "rer-b-orlyval",
                "paragraphs": [
                    "Avant l'arrivée de la <strong>ligne 14 du métro</strong> en juin 2024, la combinaison <strong>RER B + Orlyval</strong> était la solution la plus rapide vers Orly. Elle reste utilisable.",
                    "Le <strong>RER B</strong> dessert la <strong>gare d'Antony</strong>, où il faut prendre l'<strong>Orlyval</strong>, train automatique sur monorail reliant Antony aux terminaux d'Orly.",
                    "<strong>Durée totale : 40 min depuis Châtelet</strong>. <strong>Prix combiné : 13,25 €</strong>. Solution intéressante depuis le sud de Paris ou la banlieue sud."
                ],
                "table": {
                    "headers": ["Critère", "Valeur"],
                    "rows": [
                        ["Durée totale", "40 min"],
                        ["Prix combiné", "13,25 €"],
                        ["RER B fréquence", "10 min"],
                        ["Orlyval fréquence", "7 min"]
                    ]
                }
            },
            {
                "h2": "Tramway T7 vers Orly : option économique",
                "anchor": "tramway-t7",
                "paragraphs": [
                    "Le <strong>tramway T7</strong> relie <strong>Villejuif - Louis Aragon</strong> (terminus M7) à <strong>Athis-Mons</strong> en passant par <strong>Orly</strong>.",
                    "<strong>Durée : 30 min depuis Villejuif</strong>. <strong>Prix : 2,15 €</strong> (ticket t+). <strong>Fréquence : 8 min</strong>. Solution intéressante depuis le sud parisien via la <strong>ligne 7 du métro</strong>."
                ]
            },
            {
                "h2": "Taxi à Orly : forfait 2024",
                "anchor": "taxi",
                "paragraphs": [
                    "Le <strong>taxi</strong> applique un <strong>tarif forfaitaire réglementé</strong> pour les courses entre Paris intra-muros et <strong>Paris-Orly</strong>.",
                    "<strong>Tarifs forfait 2024</strong> : <strong>36 €</strong> depuis la <strong>Rive Gauche</strong>, <strong>44 €</strong> depuis la <strong>Rive Droite</strong>. <strong>Durée : ~35 min</strong> en conditions normales. Moins cher et plus rapide que le forfait CDG.",
                    "<strong>VTC</strong> (Uber, Bolt) : <strong>30 à 60 €</strong> selon trafic et heure."
                ]
            },
            {
                "h2": "Terminaux Orly (1, 2, 3, 4)",
                "anchor": "terminaux",
                "paragraphs": [
                    "Depuis la <strong>fusion de 2019</strong>, l'aéroport est organisé en <strong>4 terminaux</strong> numérotés Orly 1 à 4 (auparavant : Sud et Ouest)."
                ],
                "table": {
                    "headers": ["Terminal", "Compagnies principales", "Origine"],
                    "rows": [
                        ["Orly 1", "Vueling, easyJet, Transavia (low-cost)", "ex-Sud"],
                        ["Orly 2", "Air France court-courrier, French Bee, Corsair", "ex-Sud"],
                        ["Orly 3", "Air France long-courrier, KLM, Delta", "ex-Ouest"],
                        ["Orly 4", "Compagnies low-cost (Wizz Air, Ryanair, Volotea)", "ex-Ouest"]
                    ]
                }
            },
            {
                "h2": "Tableau comparatif des modes d'accès Orly",
                "anchor": "comparatif",
                "table": {
                    "headers": ["Mode", "Depuis", "Durée", "Prix"],
                    "rows": [
                        ["Métro 14 🆕", "Châtelet", "25 min", "2,15 €"],
                        ["Orlybus", "Denfert-Rochereau", "35 min", "11,50 €"],
                        ["RER B + Orlyval", "Châtelet", "40 min", "13,25 €"],
                        ["Tramway T7", "Villejuif (M7)", "30 min", "2,15 €"],
                        ["Bus 183", "Porte de Choisy", "45 min", "2,15 €"],
                        ["Taxi forfait", "Paris", "35 min", "36 € / 44 €"]
                    ]
                }
            }
        ],
        "history": [
            "L'<strong>aéroport d'Orly</strong> ouvre en <strong>1932</strong> sur l'<strong>aérodrome de Villeneuve-Orly</strong>. Devient <strong>aéroport commercial principal</strong> de Paris dans l'<strong>entre-deux-guerres</strong>.",
            "Site actuel <strong>reconstruit en 1961</strong> avec création de l'<strong>aérogare Sud</strong> par <strong>Henri Vicariot</strong>. Architecture moderne avec <strong>verrière monumentale</strong>. <strong>Aérogare Ouest</strong> en <strong>1971</strong>.",
            "Avec l'<strong>ouverture de CDG en 1974</strong>, Orly devient le <strong>2e aéroport parisien</strong>. <strong>Fusion des aérogares Sud et Ouest</strong> en <strong>2019</strong>, numérotation Orly 1 à 4. <strong>Prolongement de la ligne 14 du métro</strong> en <strong>juin 2024</strong>."
        ],
        "faq": [
            ("La ligne 14 du métro va-t-elle vraiment à Orly ?", "<strong>Oui depuis le 24 juin 2024</strong>. Terminus <strong>Aéroport d'Orly</strong>. <strong>25 min depuis Châtelet</strong>, <strong>2,15 €</strong>. Solution la plus rapide et économique."),
            ("Comment aller à Orly depuis Paris ?", "<strong>Métro 14</strong> 🆕 (25 min/2,15€). <strong>Orlybus</strong> (35 min depuis Denfert, 11,50€). <strong>RER B + Orlyval</strong> (40 min, 13,25€). <strong>Tramway T7</strong> (30 min depuis Villejuif). <strong>Taxi</strong> forfait 36€ Rive Gauche / 44€ Rive Droite."),
            ("Combien coûte le métro pour Orly ?", "<strong>2,15 €</strong> (ticket t+) ou compris dans le <strong>pass Navigo</strong>. Tarif identique aux autres trajets métro."),
            ("Combien coûte un taxi de Paris à Orly ?", "<strong>36 €</strong> depuis la Rive Gauche, <strong>44 €</strong> depuis la Rive Droite. <strong>Tarif forfaitaire réglementé</strong>."),
            ("Quel terminal pour Air France à Orly ?", "<strong>Orly 2</strong> (court-courrier) ou <strong>Orly 3</strong> (long-courrier)."),
            ("L'Orlyval fonctionne-t-il encore ?", "<strong>Oui</strong>, l'<strong>Orlyval</strong> (RER B + navette) continue de fonctionner. Néanmoins, le <strong>métro 14</strong> est désormais plus rapide et économique pour la plupart des voyageurs.")
        ],
        "nearby_pois": [
            {"name": "Villejuif - Louis Aragon (M7)", "description": "Terminus M7 + tramway T7 vers Orly. <strong>Hub multimodal</strong> du Val-de-Marne.", "distance_km": 5},
            {"name": "Centre commercial Belle Épine", "description": "<strong>Centre commercial</strong> majeur (1971). ~200 boutiques.", "distance_km": 3},
            {"name": "Parc départemental du Coteau", "description": "Parc départemental de <strong>13 hectares</strong>.", "distance_km": 2}
        ]
    },
    "paris-beauvais-tille": {
        "name": "Paris-Beauvais",
        "full_name": "Aéroport Paris-Beauvais-Tillé (BVA)",
        "city": "Beauvais", "department": "Oise (60)",
        "distance_paris_km": 85, "iata": "BVA", "icao": "LFOB",
        "terminals": ["T1", "T2"],
        "annual_traffic": "~5,7 millions", "rank_europe": "Hors top 50", "rank_world": "Hors top 100",
        "opened": "1936 (commercial 1956)", "operator": "SAGEB (concession)",
        "h1": "Aéroport Paris-Beauvais-Tillé (BVA) : guide d'accès complet (navette, train, taxi)",
        "seo_title": "Aéroport Paris-Beauvais (BVA) : navette Porte Maillot, Ryanair, Wizz Air 2026",
        "seo_description": "Comment aller à l'aéroport Paris-Beauvais (BVA, low-cost Ryanair / Wizz Air) depuis Paris : navette officielle Porte Maillot 75 min 17€, train Paris-Nord 1h30, taxi.",
        "tagline": "Aéroport low-cost — 85 km nord de Paris (Oise 60)",
        "hero_desc": "<strong>Aéroport Paris-Beauvais-Tillé</strong> (BVA), à <strong>85 km au nord de Paris</strong>, dans l'<strong>Oise</strong> (60). <strong>Aéroport low-cost</strong> principalement utilisé par <strong>Ryanair</strong> et <strong>Wizz Air</strong>. <strong>~5,7 millions de passagers</strong> par an. Accès depuis Paris par <strong>navette officielle</strong> (75 min, 17€).",
        "hero_image": hero_image(
            "paris-beauvais-tille",
            "Vue générale de l'aéroport Paris-Beauvais-Tillé",
            "Remi Mathis",
            "CC BY-SA 3.0",
            "https://commons.wikimedia.org/wiki/File:Beauvais-Till%C3%A9_Airport_-_general_view.JPG"
        ),
        "intro_paragraphs": [
            "L'<strong>aéroport Paris-Beauvais-Tillé</strong> (BVA), situé à <strong>85 km au nord de Paris</strong> dans le département de l'<strong>Oise</strong> (60), est un <strong>aéroport low-cost</strong> principalement utilisé par <strong>Ryanair</strong> et <strong>Wizz Air</strong>. <strong>~5,7 millions de passagers/an</strong> (2023).",
            "<strong>Important</strong> : malgré son nom commercial, l'aéroport est <strong>hors d'Île-de-France</strong>. <strong>Trajet Paris ↔ Beauvais : ~75 min en navette</strong>. L'appellation « Paris-Beauvais » a fait l'objet de <strong>condamnations DGCCRF</strong> en 2019 pour <strong>pratique commerciale trompeuse</strong>.",
            "<strong>2 terminaux</strong> (T1 Ryanair, T2 Wizz Air et autres low-cost). <strong>Pas de gare TGV</strong> ni de <strong>connexion métro/RER directe</strong>. Accès Paris : <strong>navette officielle</strong> (Porte Maillot, 17€), train Paris-Nord + bus, voiture (A16)."
        ],
        "sections": [
            {
                "h2": "Navette officielle Paris-Beauvais : Porte Maillot",
                "anchor": "navette",
                "paragraphs": [
                    "La <strong>navette officielle</strong> est la <strong>solution recommandée</strong> pour rejoindre l'<strong>aéroport Paris-Beauvais</strong> depuis Paris. Elle est <strong>coordonnée avec les vols</strong> Ryanair et Wizz Air.",
                    "<strong>Départ : Porte Maillot</strong> (Paris 17e, parking Pershing). <strong>Durée : 75 min</strong>. <strong>Prix : 17 € aller simple, 30 € aller-retour</strong>. <strong>Réservation en ligne recommandée</strong> sur le site officiel.",
                    "<strong>Fréquence : coordonnée aux vols</strong> (1 à 2 départs par heure selon le trafic aéroport). Premier départ vers <strong>05h00</strong>, dernier vers <strong>23h00</strong>."
                ],
                "table": {
                    "headers": ["Critère", "Valeur"],
                    "rows": [
                        ["Départ Paris", "Porte Maillot"],
                        ["Durée", "75 min"],
                        ["Prix aller simple", "17 €"],
                        ["Prix aller-retour", "30 €"],
                        ["Réservation", "Site officiel recommandé"]
                    ]
                }
            },
            {
                "h2": "Train Paris-Nord + bus : option alternative",
                "anchor": "train-bus",
                "paragraphs": [
                    "Une <strong>alternative à la navette</strong> consiste à prendre un <strong>TER</strong> depuis la <strong>Gare du Nord</strong> à Paris jusqu'à la <strong>gare SNCF de Beauvais</strong>, puis un <strong>bus</strong> vers l'aéroport.",
                    "<strong>TER Paris-Nord ↔ Beauvais</strong> : <strong>1h15 à 1h30</strong> selon le train. <strong>Prix : 10 à 18 €</strong> selon la classe et l'avance de réservation. Puis <strong>bus 12 ou 14</strong> vers l'aéroport (15 min, 4 €).",
                    "<strong>Durée totale : 1h45 à 2h</strong>. <strong>Plus lent et moins fiable que la navette</strong> mais utile si vous arrivez ou repartez en train de la Gare du Nord."
                ]
            },
            {
                "h2": "Taxi pour Paris-Beauvais : longue distance",
                "anchor": "taxi",
                "paragraphs": [
                    "Le <strong>taxi</strong> est une option <strong>très onéreuse</strong> pour rejoindre <strong>Beauvais</strong> en raison de la distance.",
                    "<strong>Pas de tarif forfaitaire</strong>. <strong>Prix estimé : 180 à 250 €</strong> selon trafic et heure. <strong>Durée : ~90 min</strong>. À éviter sauf urgence ou groupe (partage des frais)."
                ]
            },
            {
                "h2": "Voiture personnelle vers Beauvais : autoroute A16",
                "anchor": "voiture",
                "paragraphs": [
                    "L'<strong>autoroute A16</strong> relie Paris (Porte de la Chapelle) à Beauvais en <strong>~80 min</strong>. <strong>Péage : ~3,80 €</strong>.",
                    "<strong>Parkings aéroport payants</strong> : 15 à 25 € par jour selon le terminal et la durée. <strong>Réservation en ligne</strong> recommandée pour bénéficier de tarifs réduits."
                ]
            },
            {
                "h2": "Compagnies low-cost à Beauvais : Ryanair, Wizz Air",
                "anchor": "compagnies",
                "paragraphs": [
                    "<strong>Paris-Beauvais</strong> est un aéroport <strong>spécialisé low-cost</strong>. Principales compagnies :",
                    "<strong>Ryanair</strong> (base parisienne depuis 1997, T1) : destinations européennes (Dublin, Bruxelles, Rome, Madrid, Barcelone, Porto, Édimbourg, Cracovie). <strong>Wizz Air</strong> (T2) : Europe de l'Est (Budapest, Bucarest, Varsovie, Sofia). <strong>Volotea</strong> et autres low-cost ponctuelles."
                ]
            },
            {
                "h2": "Tableau comparatif des modes d'accès Beauvais",
                "anchor": "comparatif",
                "table": {
                    "headers": ["Mode", "Depuis", "Durée", "Prix"],
                    "rows": [
                        ["Navette officielle", "Porte Maillot", "75 min", "17 €"],
                        ["TER + bus", "Gare du Nord", "1h45-2h", "14-22 €"],
                        ["Voiture", "Paris", "80 min", "Péage 3,80 € + parking"],
                        ["Taxi", "Paris", "90 min", "180-250 €"]
                    ]
                }
            }
        ],
        "history": [
            "L'<strong>aéroport de Beauvais-Tillé</strong> est <strong>créé en 1936</strong> à des fins militaires. Devient <strong>aéroport commercial en 1956</strong>.",
            "<strong>Essor low-cost</strong> à partir de <strong>1997</strong> avec l'arrivée de <strong>Ryanair</strong> qui en fait sa <strong>base parisienne</strong>. Trafic décuplé : <strong>~250 000 passagers en 1997, ~5,7 millions en 2023</strong>.",
            "<strong>Controverses sur l'appellation « Paris-Beauvais »</strong> : la <strong>DGCCRF</strong> condamna l'aéroport en <strong>2019</strong> pour <strong>pratique commerciale trompeuse</strong>. <strong>Concession</strong> exploitée par la <strong>SAGEB</strong>."
        ],
        "faq": [
            ("Comment aller à Paris-Beauvais depuis Paris ?", "<strong>Navette officielle</strong> depuis Porte Maillot : 75 min, <strong>17 €</strong> aller simple. <strong>Réservation en ligne recommandée</strong>."),
            ("L'aéroport de Beauvais est-il vraiment à Paris ?", "<strong>Non</strong>. L'aéroport est à <strong>85 km de Paris</strong>, dans l'<strong>Oise</strong> (60), <strong>hors d'Île-de-France</strong>. L'appellation « Paris-Beauvais » a fait l'objet de <strong>condamnations DGCCRF</strong> (2019)."),
            ("Quelles compagnies utilisent Beauvais ?", "<strong>Ryanair</strong> (base parisienne, T1), <strong>Wizz Air</strong> (T2), <strong>Volotea</strong>, autres compagnies low-cost."),
            ("Y a-t-il un train direct Paris ↔ Beauvais ?", "<strong>Non</strong>. <strong>TER Paris-Nord ↔ Beauvais SNCF</strong> (1h15), puis bus 12/14 vers l'aéroport (15 min). Solution lente."),
            ("Combien de temps en taxi Paris ↔ Beauvais ?", "<strong>~90 min</strong>. Coût : <strong>180 à 250 €</strong> (pas de tarif forfaitaire)."),
            ("Quels sont les horaires de la navette Beauvais ?", "Premier départ vers <strong>05h00</strong>, dernier vers <strong>23h00</strong>. <strong>Coordonnée aux vols</strong> Ryanair et Wizz Air. Consultez le site officiel.")
        ],
        "nearby_pois": [
            {"name": "Cathédrale Saint-Pierre de Beauvais", "description": "<strong>Cathédrale gothique</strong> XIIIe siècle, <strong>plus haut chœur gothique au monde</strong> (48,5 m).", "distance_km": 8},
            {"name": "Centre-ville Beauvais", "description": "Ville préfecture de l'<strong>Oise</strong>, <strong>~55 000 habitants</strong>. Mosaïque romaine, musée MUDO.", "distance_km": 8},
            {"name": "Forêt de Compiègne", "description": "<strong>Forêt royale</strong> historique (14 000 ha).", "distance_km": 50}
        ]
    }
}


def write_aeroport(slug, c):
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
        "h1": c["h1"],
        "seo": {"title": c["seo_title"], "description": c["seo_description"]},
        "hero": {"tagline": c["tagline"], "description": c["hero_desc"]},
        "hero_image": c["hero_image"],
        "intro_paragraphs": c["intro_paragraphs"],
        "sections": c["sections"],
        "history": c["history"],
        "faq": [{"question": q, "answer": a} for q, a in c["faq"]],
        "nearby_pois": c["nearby_pois"],
        "published": True,
    }
    p.write_text(json.dumps(d, indent=4, ensure_ascii=False) + "\n")
    print(f"✓ {slug}")


if __name__ == "__main__":
    for slug, c in CONTENT.items():
        try: write_aeroport(slug, c)
        except Exception as e: print(f"✗ {slug}: {e}")
