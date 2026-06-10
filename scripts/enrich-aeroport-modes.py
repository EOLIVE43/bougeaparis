#!/usr/bin/env python3
"""Crée les pages détail mode-aéroport (14 pages).

Structure : public_html/data/aeroports/{aeroport}/{mode}.json
Rendues par template aeroport-mode.php via route /aeroports/{aeroport}/{mode}/
"""
import json
from pathlib import Path
ROOT = Path(__file__).parent.parent
AERO = ROOT / "public_html" / "data" / "aeroports"


def page(aero_slug, aero_name, aero_iata, mode_slug, mode_label, color,
         h1, seo_title, seo_desc, tagline, intros, quick_facts,
         itineraire, horaires, tarifs, itin_paris, pois, alternatives, faq):
    return {
        "published": True,
        "aeroport_slug": aero_slug,
        "aeroport_name": aero_name,
        "aeroport_iata": aero_iata,
        "mode_slug": mode_slug,
        "mode_label": mode_label,
        "color": color,
        "h1": h1,
        "seo": {"title": seo_title, "description": seo_desc},
        "tagline": tagline,
        "intro_paragraphs": intros,
        "quick_facts": quick_facts,
        "itineraire": itineraire,
        "horaires": horaires,
        "tarifs": tarifs,
        "itineraires_paris": itin_paris,
        "pois": pois,
        "alternatives": alternatives,
        "faq": [{"question": q, "answer": a} for q, a in faq],
    }


# Couleurs par mode
COL = {
    "metro": "#7C4E9B",   # violet (M14)
    "bus": "#E5B100",     # jaune
    "rer": "#0064B0",     # bleu RER
    "tramway": "#00913F", # vert tram
    "taxi": "#222222",    # noir
    "navette": "#9A4DD0", # violet navette
    "train": "#D02D2D",   # rouge train
    "tgv": "#C61E4D",     # rouge TGV
    "voiture": "#555555", # gris
    "cdgval": "#007AB7",  # bleu CDG
    "orlyval": "#00ADEF", # bleu Orlyval
}


PAGES = []

# ============ ORLY (5 pages) ============

# Orly — Métro ligne 14 (LA RÉVOLUTION 2024)
PAGES.append(("paris-orly", "metro", page(
    aero_slug="paris-orly", aero_name="Paris-Orly", aero_iata="ORY",
    mode_slug="metro", mode_label="Métro ligne 14",
    color=COL["metro"],
    h1="Métro 14 pour Orly : durée 25 min, prix 2,15 € (depuis juin 2024)",
    seo_title="Métro 14 Orly : durée, prix, horaires 2026 — Châtelet → Aéroport d'Orly 25 min",
    seo_desc="Métro ligne 14 vers Aéroport d'Orly depuis juin 2024 : 25 min depuis Châtelet, 2,15 €, fréquence 4 min. Horaires 5h30-00h15. Stations, terminaux.",
    tagline="🆕 Liaison directe depuis juin 2024 — 2,15 € seulement",
    intros=[
        "Depuis le <strong>24 juin 2024</strong>, la <strong>ligne 14 du métro parisien</strong> est <strong>prolongée jusqu'à l'aéroport Paris-Orly</strong>. Cette extension révolutionne l'accès à Orly : <strong>25 minutes depuis Châtelet</strong>, <strong>2,15 € seulement</strong> (tarif ticket t+ standard), <strong>fréquence toutes les 4 minutes</strong> en heure de pointe.",
        "C'est désormais la <strong>solution la plus rapide et la moins chère</strong> pour rejoindre Orly depuis le centre de Paris. Elle remplace l'ancien <strong>Orlyval + RER B</strong> (13,25 €) et le <strong>Orlybus</strong> (11,50 €) pour la plupart des trajets.",
        "Le terminus <strong>Aéroport d'Orly</strong> dessert directement les <strong>terminaux Orly 1, 2, 3 et 4</strong> via un parcours piéton couvert balisé."
    ],
    quick_facts=[
        {"value": "25 min", "label": "depuis Châtelet"},
        {"value": "2,15 €", "label": "ticket t+"},
        {"value": "4 min", "label": "fréquence pointe"},
        {"value": "05h30 → 00h15", "label": "amplitude"},
    ],
    itineraire={
        "h2": "Itinéraire détaillé : Paris → Aéroport d'Orly en métro 14",
        "paragraphs": [
            "Depuis le centre de Paris, prenez la <strong>ligne 14 du métro</strong> en direction de <strong>Aéroport d'Orly</strong> (terminus sud)."
        ],
        "steps": [
            "Prendre la <strong>M14</strong> direction <strong>« Aéroport d'Orly »</strong> depuis une des stations centrales (Châtelet, Gare de Lyon, Saint-Lazare, Madeleine, Pyramides, Olympiades).",
            "Le trajet est <strong>entièrement automatique</strong>, sans changement.",
            "Descendre au terminus <strong>« Aéroport d'Orly »</strong>.",
            "Suivre la signalétique <strong>« Terminaux »</strong> via le parcours piéton couvert.",
            "Compter <strong>5 à 10 min</strong> à pied selon le terminal (Orly 1, 2, 3 ou 4)."
        ]
    },
    horaires={
        "h2": "Horaires du métro 14 vers Orly",
        "paragraphs": [
            "Le métro 14 fonctionne <strong>tous les jours</strong>, y compris dimanches et jours fériés. <strong>Amplitude horaire complète</strong> : du premier au dernier train, environ 18h45 de service par jour.",
            "La <strong>fréquence varie selon l'heure</strong> : 4 min en heure de pointe, jusqu'à 8 min en heure creuse."
        ],
        "table": {
            "headers": ["Jour", "Premier train", "Dernier train"],
            "rows": [
                ["Lundi-jeudi", "05h30", "00h15"],
                ["Vendredi-samedi", "05h30", "01h15"],
                ["Dimanche", "05h45", "00h15"],
            ]
        }
    },
    tarifs={
        "h2": "Tarifs métro 14 vers Orly",
        "paragraphs": [
            "Le <strong>ticket métro standard</strong> (ticket t+) à <strong>2,15 €</strong> est valable pour le trajet vers Orly.",
            "Le <strong>pass Navigo</strong> (semaine, mois, jour, Découverte) couvre intégralement le trajet sans supplément. La station <strong>Aéroport d'Orly</strong> est en <strong>zone 4</strong>."
        ],
        "table": {
            "headers": ["Titre", "Prix", "Conditions"],
            "rows": [
                ["Ticket t+ unitaire", "2,15 €", "Trajet simple"],
                ["Carnet de 10", "17,35 €", "Tickets à l'unité"],
                ["Navigo Easy", "Recharge ticket", "Carte rechargeable"],
                ["Navigo Semaine zones 1-5", "30,75 €", "Inclut Orly"],
                ["Navigo Mois zones 1-5", "86,40 €", "Inclut Orly"],
                ["Navigo Jour", "12,00 €", "Tout zone, jour"],
            ]
        }
    },
    itin_paris=[
        {"depart": "Châtelet", "station_slug": "chatelet", "duration": "25 min", "trajet": "M14 directe, sans changement."},
        {"depart": "Gare de Lyon", "station_slug": "gare-de-lyon", "duration": "22 min", "trajet": "M14 directe."},
        {"depart": "Saint-Lazare", "station_slug": "saint-lazare", "duration": "30 min", "trajet": "M14 directe."},
        {"depart": "Madeleine", "station_slug": "madeleine", "duration": "27 min", "trajet": "M14 directe."},
        {"depart": "Gare du Nord", "station_slug": "gare-du-nord", "duration": "32 min", "trajet": "RER B + M14 (correspondance Châtelet)."},
        {"depart": "Opéra", "station_slug": "opera", "duration": "30 min", "trajet": "M8 (1 station) → Madeleine + M14."},
        {"depart": "Montparnasse", "station_slug": "montparnasse-bienvenue", "duration": "32 min", "trajet": "M4 → Châtelet + M14."},
    ],
    pois=[
        {"name": "Station Aéroport d'Orly", "description": "Terminus sud de la M14, accès direct aux terminaux Orly 1-4 via parcours piéton couvert."},
        {"name": "Terminal Orly 1", "description": "Vueling, easyJet, Transavia (low-cost). ~7 min à pied depuis la station."},
        {"name": "Terminal Orly 2", "description": "Air France court-courrier, French Bee, Corsair. ~5 min à pied."},
        {"name": "Terminal Orly 3", "description": "Air France long-courrier, KLM, Delta, SkyTeam. ~10 min à pied."},
        {"name": "Terminal Orly 4", "description": "Wizz Air, Ryanair, Volotea (low-cost). ~12 min à pied."},
    ],
    alternatives=[
        {"label": "Orlybus", "url": "/aeroports/paris-orly/bus/", "note": "35 min depuis Denfert, 11,50 €."},
        {"label": "RER B + Orlyval", "url": "/aeroports/paris-orly/rer/", "note": "40 min depuis Châtelet, 13,25 €."},
        {"label": "Tramway T7", "url": "/aeroports/paris-orly/tramway/", "note": "30 min depuis Villejuif, 2,15 €."},
        {"label": "Taxi forfait", "url": "/aeroports/paris-orly/taxi/", "note": "35 min, 36 € / 44 € selon rive."},
    ],
    faq=[
        ("La ligne 14 du métro va-t-elle vraiment à Orly ?", "<strong>Oui depuis le 24 juin 2024</strong>. Terminus <strong>Aéroport d'Orly</strong>. <strong>25 min depuis Châtelet</strong>, <strong>2,15 €</strong>."),
        ("Combien coûte le métro 14 pour Orly ?", "<strong>2,15 €</strong> (ticket t+ standard) ou compris dans le <strong>pass Navigo zones 1-5</strong>. Tarif identique aux autres trajets métro."),
        ("Quel est le temps de trajet métro 14 Châtelet → Orly ?", "<strong>25 minutes</strong> entre Châtelet et Aéroport d'Orly. Compter <strong>5 à 12 min supplémentaires</strong> à pied selon le terminal de destination."),
        ("Quelle est la fréquence de la ligne 14 vers Orly ?", "<strong>Toutes les 4 minutes</strong> en heure de pointe, <strong>8 min</strong> en heure creuse. Service automatique."),
        ("À quelle heure est le premier métro 14 pour Orly ?", "<strong>05h30</strong> du lundi au samedi, <strong>05h45</strong> le dimanche."),
        ("À quelle heure est le dernier métro 14 depuis Orly ?", "<strong>00h15</strong> du lundi au jeudi et dimanche, <strong>01h15</strong> le vendredi et samedi."),
        ("Le métro 14 dessert-il tous les terminaux d'Orly ?", "<strong>Oui</strong>. La station <strong>Aéroport d'Orly</strong> est reliée à tous les terminaux (Orly 1, 2, 3, 4) par un <strong>parcours piéton couvert</strong>."),
    ]
)))

# Orly — Bus (Orlybus + 183 + 285)
PAGES.append(("paris-orly", "bus", page(
    aero_slug="paris-orly", aero_name="Paris-Orly", aero_iata="ORY",
    mode_slug="bus", mode_label="Bus",
    color=COL["bus"],
    h1="Bus pour Orly : Orlybus, 183, 285 — horaires et tarifs 2026",
    seo_title="Bus Orly : Orlybus depuis Denfert (35 min, 11,50 €), 183, 285 — horaires 2026",
    seo_desc="Bus pour Aéroport Paris-Orly : Orlybus depuis Denfert-Rochereau (35 min, 11,50 €), bus 183 depuis Porte de Choisy (2,15 €), bus 285 depuis Villejuif. Horaires, tarifs.",
    tagline="Orlybus 35 min depuis Denfert-Rochereau — 11,50 €",
    intros=[
        "Trois <strong>bus desservent l'aéroport Paris-Orly</strong> depuis Paris. Le plus rapide est l'<strong>Orlybus</strong>, ligne directe depuis <strong>Denfert-Rochereau</strong> (Paris 14e). Les bus <strong>183</strong> et <strong>285</strong> offrent des alternatives plus économiques mais plus longues.",
        "Depuis le <strong>24 juin 2024</strong>, le <strong>métro 14</strong> a transformé l'accès à Orly et est désormais souvent plus rapide et économique que les bus. Mais l'<strong>Orlybus</strong> reste un choix pertinent depuis le sud parisien (Denfert)."
    ],
    quick_facts=[
        {"value": "35 min", "label": "Orlybus (Denfert)"},
        {"value": "11,50 €", "label": "Orlybus"},
        {"value": "2,15 €", "label": "Bus 183/285"},
        {"value": "15 min", "label": "fréquence"},
    ],
    itineraire={
        "h2": "Itinéraires bus Paris → Orly",
        "paragraphs": [
            "Selon votre quartier de départ, choisissez le bus le mieux adapté :"
        ],
        "steps": [
            "<strong>Orlybus</strong> : depuis <strong>Denfert-Rochereau</strong> (14e), arrêt bus dédié devant la gare RER B / M4 / M6. Bus direct vers Orly, <strong>35 min</strong>.",
            "<strong>Bus 183</strong> : depuis <strong>Porte de Choisy</strong> (M7 terminus). Trajet via avenue Stalingrad. <strong>45 min</strong>, ticket t+ <strong>2,15 €</strong>.",
            "<strong>Bus 285</strong> : depuis <strong>Villejuif - Louis Aragon</strong> (M7 terminus + T7). Bus économique. <strong>30 min</strong>, ticket t+ <strong>2,15 €</strong>."
        ]
    },
    horaires={
        "h2": "Horaires des bus Paris → Orly",
        "paragraphs": [
            "L'<strong>Orlybus</strong> circule tous les jours. <strong>Bus de jour</strong> entre 05h35 et 00h30. Pas de service de nuit."
        ],
        "table": {
            "headers": ["Bus", "Premier départ", "Dernier départ", "Fréquence"],
            "rows": [
                ["Orlybus", "05h35", "00h30", "15 min"],
                ["183", "05h30", "00h30", "20 min"],
                ["285", "05h00", "00h00", "15-30 min"],
            ]
        }
    },
    tarifs={
        "h2": "Tarifs bus pour Orly",
        "paragraphs": [
            "L'<strong>Orlybus</strong> nécessite un <strong>billet spécifique</strong> à 11,50 €. Les bus 183 et 285 acceptent le <strong>ticket t+ standard</strong> à 2,15 €.",
            "Le <strong>pass Navigo zones 1-5</strong> couvre intégralement l'Orlybus et les bus 183/285."
        ],
        "table": {
            "headers": ["Bus", "Billet", "Prix"],
            "rows": [
                ["Orlybus", "Billet Orlybus", "11,50 €"],
                ["183", "Ticket t+", "2,15 €"],
                ["285", "Ticket t+", "2,15 €"],
                ["Tous bus", "Navigo zones 1-5", "Inclus"],
            ]
        }
    },
    itin_paris=[
        {"depart": "Denfert-Rochereau", "station_slug": "denfert-rochereau", "duration": "35 min", "trajet": "Orlybus directe."},
        {"depart": "Porte de Choisy", "station_slug": "porte-de-choisy", "duration": "45 min", "trajet": "Bus 183 directe."},
        {"depart": "Villejuif - Louis Aragon", "station_slug": "villejuif-louis-aragon", "duration": "30 min", "trajet": "Bus 285 ou tramway T7."},
        {"depart": "Châtelet", "station_slug": "chatelet", "duration": "55 min", "trajet": "M4 → Denfert + Orlybus."},
        {"depart": "Gare Montparnasse", "station_slug": "montparnasse-bienvenue", "duration": "45 min", "trajet": "M6 → Denfert + Orlybus."},
    ],
    pois=[
        {"name": "Arrêt Orlybus - Aérogare Sud", "description": "Devant Orly 1-2-3."},
        {"name": "Arrêt Bus 183 - Aérogare Sud", "description": "Terminaux Orly 1-2."},
    ],
    alternatives=[
        {"label": "Métro ligne 14", "url": "/aeroports/paris-orly/metro/", "note": "🆕 25 min depuis Châtelet, 2,15 € (depuis juin 2024)."},
        {"label": "RER B + Orlyval", "url": "/aeroports/paris-orly/rer/", "note": "40 min depuis Châtelet, 13,25 €."},
        {"label": "Tramway T7", "url": "/aeroports/paris-orly/tramway/", "note": "30 min depuis Villejuif, 2,15 €."},
        {"label": "Taxi forfait", "url": "/aeroports/paris-orly/taxi/", "note": "36 € / 44 € selon rive."},
    ],
    faq=[
        ("Combien coûte l'Orlybus ?", "<strong>11,50 €</strong> le billet aller simple. Compris dans le <strong>pass Navigo zones 1-5</strong>."),
        ("Combien de temps Denfert → Orly en Orlybus ?", "<strong>35 minutes</strong> en conditions normales."),
        ("Quelle est la différence entre Orlybus et bus 183 ?", "L'<strong>Orlybus</strong> est un bus direct payant (11,50 €) depuis Denfert, plus rapide. Le <strong>bus 183</strong> est un bus standard moins cher (2,15 € ticket t+) depuis Porte de Choisy, plus lent."),
        ("Le bus 183 va-t-il à Orly ?", "<strong>Oui</strong>, depuis <strong>Porte de Choisy</strong> (M7). 45 min, 2,15 €."),
        ("Quels sont les horaires de l'Orlybus ?", "Premier départ <strong>05h35</strong>, dernier <strong>00h30</strong>. Fréquence <strong>15 min</strong>."),
        ("Y a-t-il un bus de nuit pour Orly ?", "<strong>Non</strong>. L'Orlybus s'arrête à 00h30. Pour la nuit : taxi ou VTC."),
    ]
)))

# Orly — RER B + Orlyval
PAGES.append(("paris-orly", "rer", page(
    aero_slug="paris-orly", aero_name="Paris-Orly", aero_iata="ORY",
    mode_slug="rer", mode_label="RER B + Orlyval",
    color=COL["rer"],
    h1="RER B + Orlyval pour Orly : 40 min depuis Châtelet, 13,25 €",
    seo_title="RER B Orly : durée 40 min, prix 13,25 € via Orlyval — horaires 2026",
    seo_desc="RER B vers Aéroport Paris-Orly via Orlyval : 40 min depuis Châtelet, 13,25 €. Correspondance Antony. Horaires, prix, alternatives.",
    tagline="40 min depuis Châtelet via Antony + Orlyval",
    intros=[
        "Le <strong>RER B</strong> combiné à l'<strong>Orlyval</strong> (navette automatique) reliait jusqu'en juin 2024 le plus rapidement Paris à <strong>Aéroport Paris-Orly</strong>. Depuis l'arrivée du <strong>métro 14</strong>, cette solution reste utile mais plus chère et plus longue.",
            "Le trajet nécessite une <strong>correspondance à Antony</strong> (RER B) où l'on emprunte l'<strong>Orlyval</strong>, monorail automatique reliant Antony aux terminaux Orly. <strong>Prix combiné : 13,25 €</strong>. <strong>Durée totale : 40 min</strong> depuis Châtelet."
    ],
    quick_facts=[
        {"value": "40 min", "label": "Châtelet → Orly"},
        {"value": "13,25 €", "label": "billet combiné"},
        {"value": "7 min", "label": "Orlyval fréquence"},
        {"value": "06h00 → 23h35", "label": "Orlyval"},
    ],
    itineraire={
        "h2": "Itinéraire RER B + Orlyval vers Orly",
        "paragraphs": [
            "Le trajet se compose en <strong>deux étapes</strong> avec une correspondance à Antony."
        ],
        "steps": [
            "Prendre le <strong>RER B</strong> direction sud (Saint-Rémy-lès-Chevreuse / Robinson) depuis une station centrale (Châtelet, Gare du Nord, Saint-Michel, Denfert).",
            "Descendre à la gare <strong>Antony</strong> (environ 25 min depuis Châtelet).",
            "Suivre la signalétique <strong>« Orlyval »</strong> dans la gare d'Antony.",
            "Prendre l'<strong>Orlyval</strong> (monorail automatique) vers Orly — durée 7 min.",
            "L'Orlyval dessert <strong>Orly 4</strong>, <strong>Orly 1-2-3</strong> (selon le service)."
        ]
    },
    horaires={
        "h2": "Horaires RER B et Orlyval",
        "paragraphs": [
            "Le <strong>RER B</strong> circule de <strong>04h53 à 00h15</strong>. L'<strong>Orlyval</strong> circule de <strong>06h00 à 23h35</strong> environ — attention, l'Orlyval s'arrête plus tôt que le RER B."
        ],
        "table": {
            "headers": ["Service", "Premier", "Dernier", "Fréquence"],
            "rows": [
                ["RER B", "04h53", "00h15", "10 min"],
                ["Orlyval", "06h00", "23h35", "7 min"],
            ]
        }
    },
    tarifs={
        "h2": "Tarifs RER B + Orlyval pour Orly",
        "paragraphs": [
            "Le <strong>billet combiné RER B + Orlyval</strong> coûte <strong>13,25 €</strong>. L'<strong>Orlyval seul</strong> coûte <strong>11,30 €</strong> (depuis Antony)."
        ],
        "table": {
            "headers": ["Titre", "Prix", "Conditions"],
            "rows": [
                ["Billet RER B + Orlyval", "13,25 €", "Trajet combiné"],
                ["Orlyval seul", "11,30 €", "Depuis Antony"],
                ["Navigo zones 1-5", "Inclus", "Couvre RER B + Orlyval"],
            ]
        }
    },
    itin_paris=[
        {"depart": "Châtelet - Les Halles", "station_slug": "chatelet", "duration": "40 min", "trajet": "RER B → Antony + Orlyval."},
        {"depart": "Gare du Nord", "station_slug": "gare-du-nord", "duration": "45 min", "trajet": "RER B direct."},
        {"depart": "Saint-Michel - Notre-Dame", "station_slug": "saint-michel-notre-dame", "duration": "40 min", "trajet": "RER B direct."},
        {"depart": "Denfert-Rochereau", "station_slug": "denfert-rochereau", "duration": "30 min", "trajet": "RER B + Orlyval."},
        {"depart": "Aéroport CDG", "station_slug": "", "duration": "1h25", "trajet": "RER B (changement) + Orlyval."},
    ],
    pois=[
        {"name": "Gare d'Antony", "description": "Correspondance RER B → Orlyval. Suivre signalétique « Orlyval »."},
        {"name": "Station Orlyval - Orly 4", "description": "Terminaux low-cost (Wizz Air, Ryanair)."},
        {"name": "Station Orlyval - Orly 1-2-3", "description": "Terminaux Air France et autres."},
    ],
    alternatives=[
        {"label": "Métro ligne 14", "url": "/aeroports/paris-orly/metro/", "note": "🆕 25 min depuis Châtelet, 2,15 € (depuis juin 2024)."},
        {"label": "Orlybus", "url": "/aeroports/paris-orly/bus/", "note": "35 min depuis Denfert, 11,50 €."},
        {"label": "Tramway T7", "url": "/aeroports/paris-orly/tramway/", "note": "30 min depuis Villejuif, 2,15 €."},
        {"label": "Taxi forfait", "url": "/aeroports/paris-orly/taxi/", "note": "35 min, 36 € / 44 € selon rive."},
    ],
    faq=[
        ("Combien coûte le RER B vers Orly ?", "<strong>13,25 €</strong> billet combiné RER B + Orlyval. <strong>Compris dans le pass Navigo zones 1-5</strong>."),
        ("Combien de temps RER B vers Orly ?", "<strong>40 min</strong> depuis Châtelet via Antony + Orlyval."),
        ("Le RER B est-il direct vers Orly ?", "<strong>Non</strong>. Correspondance obligatoire à <strong>Antony</strong> avec l'Orlyval."),
        ("Qu'est-ce que l'Orlyval ?", "<strong>Monorail automatique</strong> reliant <strong>Antony (RER B)</strong> aux <strong>terminaux d'Orly</strong>. <strong>7 min</strong> de trajet."),
        ("À quelle heure le dernier Orlyval ?", "<strong>23h35</strong>. Attention, l'Orlyval s'arrête plus tôt que le RER B."),
        ("Métro 14 ou RER B pour Orly ?", "<strong>Métro 14</strong> est <strong>plus rapide (25 min vs 40 min) et moins cher (2,15 € vs 13,25 €)</strong> depuis Châtelet. RER B reste utile depuis Gare du Nord ou banlieue sud."),
    ]
)))

# Orly — Tramway T7
PAGES.append(("paris-orly", "tramway", page(
    aero_slug="paris-orly", aero_name="Paris-Orly", aero_iata="ORY",
    mode_slug="tramway", mode_label="Tramway T7",
    color=COL["tramway"],
    h1="Tramway T7 pour Orly : option économique 2,15 € depuis Villejuif",
    seo_title="Tramway T7 Orly : durée 30 min, prix 2,15 € depuis Villejuif — horaires 2026",
    seo_desc="Tramway T7 vers Aéroport Paris-Orly : 30 min depuis Villejuif-Louis Aragon (M7), 2,15 €. Solution économique via métro 7. Horaires, prix.",
    tagline="Option économique 2,15 € depuis Villejuif (M7 terminus)",
    intros=[
        "Le <strong>tramway T7</strong> est une <strong>option économique</strong> pour rejoindre l'<strong>aéroport Paris-Orly</strong> depuis le sud parisien. Il relie <strong>Villejuif - Louis Aragon</strong> (terminus de la M7) à <strong>Athis-Mons</strong> en passant par <strong>Orly</strong>.",
        "Inauguré en <strong>2013</strong>, le T7 dessert l'aéroport <strong>Orly 1-2-3</strong>. Prix : <strong>2,15 €</strong> (ticket t+ standard). Durée : <strong>30 min depuis Villejuif</strong>. Le T7 est moins direct que le métro 14 mais utile depuis le 13e arrondissement ou le sud parisien via la M7."
    ],
    quick_facts=[
        {"value": "30 min", "label": "depuis Villejuif"},
        {"value": "2,15 €", "label": "ticket t+"},
        {"value": "8 min", "label": "fréquence"},
        {"value": "T7 stations", "label": "21 stations"},
    ],
    itineraire={
        "h2": "Itinéraire tramway T7 Paris → Orly",
        "paragraphs": [
            "Le trajet en T7 nécessite d'abord de rejoindre <strong>Villejuif - Louis Aragon</strong>, terminus sud de la <strong>ligne 7 du métro</strong>."
        ],
        "steps": [
            "Prendre la <strong>M7</strong> direction <strong>Villejuif - Louis Aragon</strong> depuis une station centrale (Opéra, Châtelet, Place d'Italie).",
            "Descendre au terminus <strong>Villejuif - Louis Aragon</strong>.",
            "Suivre la signalétique <strong>« Tramway T7 »</strong> dans la station.",
            "Prendre le <strong>T7</strong> direction <strong>Athis-Mons</strong> (terminus est).",
            "Descendre à la station <strong>Aéroport d'Orly</strong> (durée 30 min depuis Villejuif).",
            "Suivre la signalétique vers les <strong>terminaux Orly 1-2-3</strong>."
        ]
    },
    horaires={
        "h2": "Horaires tramway T7 Orly",
        "paragraphs": [
            "Le <strong>T7</strong> circule tous les jours, avec une amplitude horaire similaire au métro."
        ],
        "table": {
            "headers": ["Jour", "Premier", "Dernier", "Fréquence"],
            "rows": [
                ["Lundi-jeudi", "05h25", "00h15", "8 min"],
                ["Vendredi-samedi", "05h25", "01h15", "8 min"],
                ["Dimanche", "05h45", "00h15", "10 min"],
            ]
        }
    },
    tarifs={
        "h2": "Tarifs tramway T7 pour Orly",
        "paragraphs": [
            "Le <strong>ticket t+ standard</strong> à <strong>2,15 €</strong> est valable. Le pass Navigo couvre intégralement le T7."
        ],
        "table": {
            "headers": ["Titre", "Prix"],
            "rows": [
                ["Ticket t+ unitaire", "2,15 €"],
                ["Carnet 10 tickets", "17,35 €"],
                ["Navigo Semaine zones 1-5", "30,75 €"],
                ["Navigo Jour", "12,00 €"],
            ]
        }
    },
    itin_paris=[
        {"depart": "Villejuif - Louis Aragon", "station_slug": "villejuif-louis-aragon", "duration": "30 min", "trajet": "T7 directe."},
        {"depart": "Place d'Italie", "station_slug": "place-d-italie", "duration": "45 min", "trajet": "M7 → Villejuif + T7."},
        {"depart": "Châtelet", "station_slug": "chatelet", "duration": "55 min", "trajet": "M7 → Villejuif + T7."},
        {"depart": "Opéra", "station_slug": "opera", "duration": "55 min", "trajet": "M7 → Villejuif + T7."},
    ],
    pois=[
        {"name": "Station Aéroport d'Orly (T7)", "description": "Arrêt aéroport. Accès Orly 1-2-3 à pied."},
        {"name": "Station Villejuif - Louis Aragon", "description": "Terminus M7 + tramway T7. Hub multimodal."},
    ],
    alternatives=[
        {"label": "Métro ligne 14", "url": "/aeroports/paris-orly/metro/", "note": "🆕 25 min depuis Châtelet, 2,15 €."},
        {"label": "Orlybus", "url": "/aeroports/paris-orly/bus/", "note": "35 min, 11,50 €."},
        {"label": "RER B + Orlyval", "url": "/aeroports/paris-orly/rer/", "note": "40 min, 13,25 €."},
        {"label": "Taxi forfait", "url": "/aeroports/paris-orly/taxi/", "note": "36 € / 44 €."},
    ],
    faq=[
        ("Le tramway T7 va-t-il à Orly ?", "<strong>Oui</strong>. Le T7 dessert <strong>Aéroport d'Orly</strong> (terminaux 1-2-3) depuis <strong>Villejuif - Louis Aragon</strong>."),
        ("Combien coûte le T7 pour Orly ?", "<strong>2,15 €</strong> (ticket t+ standard). Compris dans le <strong>pass Navigo zones 1-5</strong>."),
        ("Combien de temps T7 Villejuif → Orly ?", "<strong>30 minutes</strong> environ."),
        ("Quel est l'itinéraire complet métro + T7 ?", "Prenez la <strong>M7 jusqu'à Villejuif - Louis Aragon</strong>, puis <strong>T7 direction Athis-Mons</strong> jusqu'à <strong>Aéroport d'Orly</strong>."),
        ("Métro 14 ou T7 pour Orly ?", "<strong>Métro 14</strong> est plus rapide (25 min vs 30 min depuis Villejuif). Le <strong>T7</strong> reste utile si vous êtes proche de la M7 (Villejuif, 13e arrondissement)."),
    ]
)))

# Orly — Taxi
PAGES.append(("paris-orly", "taxi", page(
    aero_slug="paris-orly", aero_name="Paris-Orly", aero_iata="ORY",
    mode_slug="taxi", mode_label="Taxi",
    color=COL["taxi"],
    h1="Taxi Paris → Orly : forfait 36 € / 44 € (rive gauche / droite)",
    seo_title="Taxi Orly : forfait 36 € rive gauche, 44 € rive droite — 35 min trajet 2026",
    seo_desc="Taxi Paris → Aéroport Paris-Orly : tarif forfaitaire 36 € rive gauche, 44 € rive droite. Durée 35 min. VTC Uber, Bolt alternatifs.",
    tagline="Forfait réglementé 36 € rive gauche / 44 € rive droite",
    intros=[
        "Le <strong>taxi parisien</strong> applique un <strong>tarif forfaitaire réglementé</strong> pour les courses entre Paris intra-muros et l'<strong>aéroport Paris-Orly</strong>. Tarif <strong>moins cher qu'à CDG</strong> en raison de la proximité (14 km contre 25 km).",
        "<strong>Durée moyenne : 35 min</strong> en conditions normales, jusqu'à 60 min en heure de pointe. <strong>Réservation à l'avance possible</strong> (G7, Taxis Bleus) avec supplément de 7 €."
    ],
    quick_facts=[
        {"value": "36 €", "label": "rive gauche"},
        {"value": "44 €", "label": "rive droite"},
        {"value": "35 min", "label": "durée moyenne"},
        {"value": "14 km", "label": "distance"},
    ],
    itineraire={
        "h2": "Comment prendre un taxi pour Orly",
        "paragraphs": [
            "Plusieurs options pour prendre un taxi vers Orly :"
        ],
        "steps": [
            "<strong>Station de taxi</strong> : disponibles devant les gares (Châtelet, Gare de Lyon, Gare du Nord, Montparnasse) et grandes places.",
            "<strong>Hélés dans la rue</strong> si le voyant est vert.",
            "<strong>Réservation par téléphone</strong> : G7 (3607), Taxis Bleus (3609), Alpha Taxis. Supplément de réservation : 7 €.",
            "<strong>Application mobile</strong> : G7, Bolt Taxis, Le Taxi.",
            "<strong>Confirmer le forfait</strong> avec le chauffeur avant le départ : 36 € rive gauche / 44 € rive droite."
        ]
    },
    horaires={},
    tarifs={
        "h2": "Tarifs taxi Paris → Orly (2024)",
        "paragraphs": [
            "Le <strong>tarif forfaitaire</strong> couvre la course pour <strong>tout passager + bagages</strong>. <strong>Pas de supplément</strong> pour les bagages."
        ],
        "table": {
            "headers": ["Trajet", "Tarif forfait", "Note"],
            "rows": [
                ["Paris Rive Gauche → Orly", "36 €", "5e, 6e, 7e, 13e, 14e, 15e arr."],
                ["Paris Rive Droite → Orly", "44 €", "Autres arrondissements."],
                ["Supplément 5e passager", "+ 5,50 €", "Au-delà de 4 passagers."],
                ["Supplément animal", "Variable", "Selon chauffeur."],
                ["Réservation par téléphone", "+ 7 €", "Optionnel."],
                ["Pourboire (recommandé)", "5-10 %", "Non obligatoire."],
            ]
        }
    },
    itin_paris=[
        {"depart": "Châtelet (rive droite)", "station_slug": "chatelet", "duration": "35 min", "trajet": "Taxi 44 €."},
        {"depart": "Gare de Lyon (rive droite)", "station_slug": "gare-de-lyon", "duration": "30 min", "trajet": "Taxi 44 €."},
        {"depart": "Saint-Germain (rive gauche)", "station_slug": "saint-germain-des-pres", "duration": "30 min", "trajet": "Taxi 36 €."},
        {"depart": "Montparnasse (rive gauche)", "station_slug": "montparnasse-bienvenue", "duration": "25 min", "trajet": "Taxi 36 €."},
        {"depart": "Gare du Nord (rive droite)", "station_slug": "gare-du-nord", "duration": "40 min", "trajet": "Taxi 44 €."},
    ],
    pois=[
        {"name": "Station taxi - Orly 1", "description": "Sortie « Arrivées », niveau 0."},
        {"name": "Station taxi - Orly 4", "description": "Sortie « Arrivées »."},
    ],
    alternatives=[
        {"label": "Métro ligne 14", "url": "/aeroports/paris-orly/metro/", "note": "🆕 25 min depuis Châtelet, 2,15 € (12 fois moins cher !)."},
        {"label": "Orlybus", "url": "/aeroports/paris-orly/bus/", "note": "35 min depuis Denfert, 11,50 €."},
        {"label": "RER B + Orlyval", "url": "/aeroports/paris-orly/rer/", "note": "40 min, 13,25 €."},
    ],
    faq=[
        ("Combien coûte un taxi Paris → Orly ?", "<strong>36 €</strong> depuis la <strong>Rive Gauche</strong>, <strong>44 €</strong> depuis la <strong>Rive Droite</strong>. <strong>Tarif forfaitaire réglementé</strong>."),
        ("Combien de temps en taxi Paris → Orly ?", "<strong>~35 min</strong> en conditions normales. <strong>~60 min</strong> aux heures de pointe."),
        ("Le forfait taxi est-il pour tous les passagers ?", "<strong>Oui</strong>, le forfait couvre <strong>4 passagers + bagages</strong>. <strong>5e passager : +5,50 €</strong>."),
        ("Combien coûte un VTC Paris → Orly ?", "<strong>30 à 60 €</strong> selon trafic et heure (Uber, Bolt). Prix dynamique."),
        ("Faut-il réserver le taxi à l'avance ?", "<strong>Non</strong>. Mais la réservation par téléphone est possible avec <strong>7 € de supplément</strong>."),
        ("Le pourboire est-il obligatoire ?", "<strong>Non</strong>. Pourboire de <strong>5 à 10 %</strong> est apprécié si vous êtes satisfait."),
    ]
)))


# ============ CDG (5 pages) ============

# CDG — RER B
PAGES.append(("paris-charles-de-gaulle", "rer-b", page(
    aero_slug="paris-charles-de-gaulle", aero_name="Paris-Charles de Gaulle", aero_iata="CDG",
    mode_slug="rer-b", mode_label="RER B",
    color=COL["rer"],
    h1="RER B pour Charles de Gaulle : 35 min depuis Châtelet, 11,80 €",
    seo_title="RER B CDG : durée 35 min, prix 11,80 €, fréquence 10 min — horaires 2026",
    seo_desc="RER B vers Paris-Charles de Gaulle : 35 min depuis Châtelet, 11,80 €, fréquence 10 min. Horaires 04h53-00h15. Stations CDG 1 et CDG 2 TGV.",
    tagline="Solution la plus rapide — 35 min Châtelet → CDG",
    intros=[
        "Le <strong>RER B</strong> est la <strong>solution la plus rapide</strong> pour rejoindre l'<strong>aéroport Paris-Charles de Gaulle</strong> depuis le centre de Paris. <strong>35 minutes depuis Châtelet - Les Halles</strong>, avec arrêts à <strong>Gare du Nord</strong>, <strong>Saint-Michel - Notre-Dame</strong> et <strong>Denfert-Rochereau</strong>.",
        "<strong>Prix du billet : 11,80 €</strong> en 2024-2025 (compris dans le pass Navigo zones 1-5). <strong>Fréquence : toutes les 10 à 20 minutes</strong> selon l'heure. <strong>Deux gares</strong> dans l'aéroport : Aéroport CDG 1 (Terminal 1 via CDGVAL) et Aéroport CDG 2 TGV (Terminaux 2A-2F)."
    ],
    quick_facts=[
        {"value": "35 min", "label": "depuis Châtelet"},
        {"value": "11,80 €", "label": "billet plein tarif"},
        {"value": "10-20 min", "label": "fréquence"},
        {"value": "04h53 → 00h15", "label": "amplitude"},
    ],
    itineraire={
        "h2": "Itinéraire RER B Paris → CDG",
        "paragraphs": [
            "Le RER B est <strong>direct vers CDG</strong> depuis les stations centrales. <strong>Pas de changement</strong>, mais <strong>vérifiez la destination du train</strong>."
        ],
        "steps": [
            "Repérer la <strong>destination du train</strong> sur les panneaux : « <strong>Aéroport CDG 2 TGV</strong> » ou « <strong>Mitry-Claye</strong> » (certains s'arrêtent avant CDG).",
            "Monter à bord d'un RER B direction nord.",
            "Le trajet dessert <strong>Châtelet</strong>, <strong>Gare du Nord</strong>, puis l'aéroport.",
            "Descendre à <strong>Aéroport CDG 1</strong> (pour le Terminal 1 via CDGVAL) ou <strong>Aéroport CDG 2 TGV</strong> (pour les Terminaux 2A à 2F).",
            "Suivre la signalétique <strong>« Terminaux »</strong>."
        ]
    },
    horaires={
        "h2": "Horaires RER B vers CDG",
        "paragraphs": [
            "Le <strong>RER B</strong> circule de <strong>04h53 à 00h15</strong>. <strong>Service de nuit</strong> assuré par les bus N140 et N143 (consulter la page bus)."
        ],
        "table": {
            "headers": ["Jour", "Premier train", "Dernier train"],
            "rows": [
                ["Lundi-jeudi", "04h53", "00h15"],
                ["Vendredi-samedi", "04h53", "01h00"],
                ["Dimanche", "05h00", "00h15"],
            ]
        }
    },
    tarifs={
        "h2": "Tarifs RER B Paris → CDG",
        "paragraphs": [
            "Le <strong>billet RER B Paris → CDG</strong> coûte <strong>11,80 €</strong> en 2024-2025. <strong>Pas de gratuité enfants</strong> (sauf -4 ans). Le <strong>pass Navigo zones 1-5</strong> couvre intégralement le trajet."
        ],
        "table": {
            "headers": ["Titre", "Prix", "Conditions"],
            "rows": [
                ["Billet aéroport plein tarif", "11,80 €", "Aller simple"],
                ["Billet enfant 4-9 ans", "5,90 €", "Demi-tarif"],
                ["Navigo Semaine zones 1-5", "30,75 €", "Inclut CDG"],
                ["Navigo Mois zones 1-5", "86,40 €", "Inclut CDG"],
                ["Navigo Jour", "12,00 €", "Tout zone"],
                ["Pass Paris Visite (1-5 zones)", "29,90 €/jour", "Pass touristique 1 jour"],
            ]
        }
    },
    itin_paris=[
        {"depart": "Châtelet - Les Halles", "station_slug": "chatelet", "duration": "35 min", "trajet": "RER B directe nord."},
        {"depart": "Gare du Nord", "station_slug": "gare-du-nord", "duration": "30 min", "trajet": "RER B directe."},
        {"depart": "Saint-Michel - Notre-Dame", "station_slug": "saint-michel-notre-dame", "duration": "40 min", "trajet": "RER B directe."},
        {"depart": "Denfert-Rochereau", "station_slug": "denfert-rochereau", "duration": "45 min", "trajet": "RER B directe."},
        {"depart": "Aéroport d'Orly", "station_slug": "", "duration": "1h20", "trajet": "Orlyval + RER B (changement Antony)."},
        {"depart": "Disneyland Paris", "station_slug": "", "duration": "55 min", "trajet": "RER A → Châtelet + RER B."},
    ],
    pois=[
        {"name": "Gare Aéroport CDG 1", "description": "Pour Terminal 1 (Paul Andreu). Connexion CDGVAL."},
        {"name": "Gare Aéroport CDG 2 TGV", "description": "Pour Terminaux 2A à 2F. Connexion TGV intégrée."},
        {"name": "CDGVAL", "description": "Métro automatique gratuit reliant CDG 1, CDG 2, CDG 3, parkings PR-PX."},
    ],
    alternatives=[
        {"label": "Roissybus", "url": "/aeroports/paris-charles-de-gaulle/bus/", "note": "60-75 min depuis Opéra, 16,60 €."},
        {"label": "Taxi forfait", "url": "/aeroports/paris-charles-de-gaulle/taxi/", "note": "60 min, 56 € rive droite / 65 € rive gauche."},
        {"label": "TGV gare CDG-TGV", "url": "/aeroports/paris-charles-de-gaulle/tgv/", "note": "Depuis Lille, Bruxelles, Marseille..."},
    ],
    faq=[
        ("Combien coûte le RER B vers CDG ?", "<strong>11,80 €</strong> en 2024-2025. Compris dans le <strong>pass Navigo zones 1-5</strong>."),
        ("Combien de temps Châtelet → CDG en RER B ?", "<strong>35 minutes</strong> en conditions normales."),
        ("Le RER B est-il direct vers CDG ?", "<strong>Oui</strong>. Vérifiez la destination du train : « <strong>Aéroport CDG 2 TGV</strong> » ou « <strong>Mitry-Claye</strong> » (certains s'arrêtent avant CDG)."),
        ("Quelle gare RER B pour quel terminal ?", "<strong>Aéroport CDG 1</strong> pour le <strong>Terminal 1</strong> (+ CDGVAL). <strong>Aéroport CDG 2 TGV</strong> pour les <strong>Terminaux 2A à 2F</strong>."),
        ("À quelle heure le premier RER B vers CDG ?", "<strong>04h53</strong>. Le service de nuit est assuré par les <strong>bus N140 et N143</strong>."),
        ("À quelle heure le dernier RER B depuis CDG ?", "<strong>00h15</strong>. Au-delà : bus de nuit N140/N143."),
    ]
)))

# CDG — Bus (Roissybus + 350/351 + nuit)
PAGES.append(("paris-charles-de-gaulle", "bus", page(
    aero_slug="paris-charles-de-gaulle", aero_name="Paris-Charles de Gaulle", aero_iata="CDG",
    mode_slug="bus", mode_label="Bus",
    color=COL["bus"],
    h1="Bus pour CDG : Roissybus, bus 350/351, bus de nuit N140/N143",
    seo_title="Bus CDG : Roissybus 60 min Opéra, 350/351 économiques — horaires 2026",
    seo_desc="Bus pour Paris-Charles de Gaulle : Roissybus depuis Opéra (60-75 min, 16,60 €), bus 350 et 351 économiques (2,15 €), bus de nuit N140/N143. Horaires.",
    tagline="Roissybus 60 min depuis Opéra — 16,60 €",
    intros=[
        "Plusieurs <strong>bus desservent l'aéroport Paris-Charles de Gaulle</strong>. Le <strong>Roissybus</strong>, ligne directe depuis l'Opéra, est le plus pratique. Les <strong>bus 350 et 351</strong> offrent des alternatives plus économiques mais plus longues. La nuit, les <strong>bus N140 et N143</strong> assurent le service.",
        "Les bus sont une <strong>solution intéressante</strong> notamment si vous résidez dans le 9e arrondissement (Opéra), le 10e (Gare de l'Est) ou aux abords de la Nation."
    ],
    quick_facts=[
        {"value": "60-75 min", "label": "Roissybus"},
        {"value": "16,60 €", "label": "Roissybus"},
        {"value": "2,15 €", "label": "Bus 350/351"},
        {"value": "Nuit OK", "label": "N140/N143"},
    ],
    itineraire={
        "h2": "Itinéraires bus Paris → CDG",
        "paragraphs": [
            "Selon votre quartier, choisissez le bus le mieux adapté :"
        ],
        "steps": [
            "<strong>Roissybus</strong> : depuis <strong>Opéra</strong> (Paris 9e, rue Scribe). Bus direct, <strong>60 à 75 min</strong>, <strong>16,60 €</strong>.",
            "<strong>Bus 350</strong> : depuis <strong>Gare de l'Est</strong>. Bus standard, <strong>75 min</strong>, <strong>2,15 €</strong> (ticket t+).",
            "<strong>Bus 351</strong> : depuis <strong>Place de la Nation</strong>. <strong>75-90 min</strong>, <strong>2,15 €</strong>.",
            "<strong>Bus N140 / N143</strong> (nuit) : depuis <strong>Châtelet</strong> et <strong>Gare de l'Est</strong>. Service nocturne 01h00-05h00."
        ]
    },
    horaires={
        "h2": "Horaires bus CDG",
        "paragraphs": [
            "Le <strong>Roissybus</strong> circule de <strong>05h15 à 00h30</strong>. Les <strong>bus 350/351</strong> de <strong>05h30 à 00h30</strong>. Les <strong>bus de nuit N140/N143</strong> prennent le relais."
        ],
        "table": {
            "headers": ["Bus", "Premier", "Dernier", "Fréquence"],
            "rows": [
                ["Roissybus", "05h15", "00h30", "15 min"],
                ["350", "05h30", "00h30", "30 min"],
                ["351", "05h30", "00h30", "30 min"],
                ["N140 (nuit)", "01h00", "05h00", "30-60 min"],
                ["N143 (nuit)", "01h00", "05h00", "30-60 min"],
            ]
        }
    },
    tarifs={
        "h2": "Tarifs bus pour CDG",
        "paragraphs": [
            "Le <strong>Roissybus</strong> nécessite un <strong>billet spécifique</strong> à 16,60 €. Les bus 350/351 et nuit acceptent le <strong>ticket t+ standard</strong> à 2,15 €. Le <strong>pass Navigo</strong> couvre tous les bus."
        ],
        "table": {
            "headers": ["Bus", "Billet", "Prix"],
            "rows": [
                ["Roissybus", "Billet Roissybus", "16,60 €"],
                ["350 / 351", "Ticket t+", "2,15 €"],
                ["N140 / N143", "Ticket t+", "2,15 €"],
                ["Tous bus", "Navigo zones 1-5", "Inclus"],
            ]
        }
    },
    itin_paris=[
        {"depart": "Opéra", "station_slug": "opera", "duration": "60-75 min", "trajet": "Roissybus directe (rue Scribe)."},
        {"depart": "Gare de l'Est", "station_slug": "gare-de-l-est", "duration": "75 min", "trajet": "Bus 350 directe."},
        {"depart": "Place de la Nation", "station_slug": "nation", "duration": "75-90 min", "trajet": "Bus 351 directe."},
        {"depart": "Châtelet", "station_slug": "chatelet", "duration": "1h05 (jour) / 1h15 (nuit)", "trajet": "M3/M4 → Opéra + Roissybus, ou N140 nuit."},
    ],
    pois=[
        {"name": "Arrêt Roissybus - Opéra", "description": "Rue Scribe (à côté de l'Opéra Garnier)."},
        {"name": "Arrêt Bus CDG", "description": "Devant les terminaux 1, 2 et 3."},
    ],
    alternatives=[
        {"label": "RER B", "url": "/aeroports/paris-charles-de-gaulle/rer-b/", "note": "35 min depuis Châtelet, 11,80 € (plus rapide)."},
        {"label": "TGV", "url": "/aeroports/paris-charles-de-gaulle/tgv/", "note": "Depuis Lille, Bruxelles, Marseille..."},
        {"label": "Taxi forfait", "url": "/aeroports/paris-charles-de-gaulle/taxi/", "note": "56 € / 65 €."},
    ],
    faq=[
        ("Combien coûte le Roissybus ?", "<strong>16,60 €</strong> billet aller simple. <strong>Compris dans le pass Navigo</strong>."),
        ("Combien de temps Opéra → CDG en Roissybus ?", "<strong>60 à 75 minutes</strong> selon le trafic."),
        ("Le bus 350 va-t-il à CDG ?", "<strong>Oui</strong> depuis la <strong>Gare de l'Est</strong>. 75 min, 2,15 € (ticket t+)."),
        ("Y a-t-il un bus de nuit pour CDG ?", "<strong>Oui</strong>. <strong>N140 et N143</strong> circulent de <strong>01h00 à 05h00</strong>. Tarif ticket t+ 2,15 €."),
        ("Roissybus ou RER B pour CDG ?", "<strong>RER B</strong> est plus rapide (35 min vs 60-75 min) et moins cher (11,80 € vs 16,60 €). <strong>Roissybus</strong> est plus pratique si vous partez du quartier de l'Opéra."),
    ]
)))

# CDG — TGV
PAGES.append(("paris-charles-de-gaulle", "tgv", page(
    aero_slug="paris-charles-de-gaulle", aero_name="Paris-Charles de Gaulle", aero_iata="CDG",
    mode_slug="tgv", mode_label="TGV",
    color=COL["tgv"],
    h1="TGV vers Charles de Gaulle : gare Aéroport-CDG-TGV intégrée Terminal 2",
    seo_title="TGV CDG : gare Aéroport-Charles de Gaulle-TGV — destinations directes 2026",
    seo_desc="Gare TGV intégrée à l'aéroport Paris-Charles de Gaulle (Terminal 2). Destinations directes : Lille, Bruxelles, Londres, Marseille, Bordeaux, Nantes. Horaires.",
    tagline="Gare TGV intégrée au Terminal 2",
    intros=[
        "L'aéroport <strong>Paris-Charles de Gaulle</strong> dispose d'une <strong>gare TGV intégrée</strong> au <strong>Terminal 2</strong>, opérationnelle depuis <strong>1994</strong>. Cette gare permet d'arriver directement à l'aéroport en TGV depuis plusieurs grandes villes françaises et européennes.",
        "<strong>Destinations directes</strong> : Lille, Bruxelles (Eurostar via correspondance), Londres (via Lille), Marseille, Lyon, Bordeaux, Nantes, Rennes, Strasbourg. Connexion <strong>CDGVAL</strong> vers les autres terminaux (CDG 1, CDG 3)."
    ],
    quick_facts=[
        {"value": "1994", "label": "ouverture gare"},
        {"value": "10+", "label": "destinations directes"},
        {"value": "Terminal 2", "label": "emplacement"},
        {"value": "CDGVAL", "label": "vers T1, T3"},
    ],
    itineraire={
        "h2": "Arrivée TGV à CDG",
        "paragraphs": [
            "La gare <strong>Aéroport Charles de Gaulle 2 TGV</strong> est située au cœur du <strong>Terminal 2</strong>, entre les modules 2C-2D-2E-2F."
        ],
        "steps": [
            "Descendre du TGV à la gare <strong>Aéroport Charles de Gaulle 2 TGV</strong>.",
            "Si votre vol part du <strong>Terminal 2A-F</strong> : suivre la signalétique directe.",
            "Si votre vol part du <strong>Terminal 1</strong> ou <strong>Terminal 3</strong> : prendre le <strong>CDGVAL</strong> (métro automatique gratuit, 4 min de fréquence).",
            "Prévoir <strong>15 à 30 min</strong> entre l'arrivée TGV et l'enregistrement vol."
        ]
    },
    horaires={
        "h2": "Destinations TGV depuis CDG",
        "paragraphs": [
            "Liaisons TGV directes vers les <strong>grandes métropoles françaises et européennes</strong> :"
        ],
        "table": {
            "headers": ["Destination", "Durée", "Fréquence"],
            "rows": [
                ["Lille", "50 min", "Plusieurs/jour"],
                ["Bruxelles (via Lille)", "1h35", "Plusieurs/jour"],
                ["Marseille", "3h30", "Plusieurs/jour"],
                ["Lyon", "2h", "Plusieurs/jour"],
                ["Bordeaux", "3h", "Plusieurs/jour"],
                ["Nantes", "3h30", "1-2/jour"],
                ["Rennes", "2h30", "1-2/jour"],
                ["Strasbourg", "2h20", "Plusieurs/jour"],
            ]
        }
    },
    tarifs={
        "h2": "Tarifs TGV vers CDG",
        "paragraphs": [
            "Les <strong>tarifs TGV varient</strong> fortement selon l'avance de réservation, la classe et la période. <strong>Réservation recommandée</strong> 1 à 3 mois à l'avance pour bénéficier des meilleurs prix.",
            "Comptez en moyenne : <strong>Lille</strong> 30-80 €, <strong>Marseille</strong> 50-150 €, <strong>Lyon</strong> 35-100 €, <strong>Bordeaux</strong> 50-130 €."
        ]
    },
    itin_paris=[
        {"depart": "Lille", "station_slug": "", "duration": "50 min", "trajet": "TGV directe."},
        {"depart": "Bruxelles", "station_slug": "", "duration": "1h35", "trajet": "Thalys/Eurostar (via Lille)."},
        {"depart": "Marseille", "station_slug": "", "duration": "3h30", "trajet": "TGV directe."},
        {"depart": "Lyon Part-Dieu", "station_slug": "", "duration": "2h", "trajet": "TGV directe."},
        {"depart": "Bordeaux Saint-Jean", "station_slug": "", "duration": "3h", "trajet": "TGV directe."},
    ],
    pois=[
        {"name": "Gare Aéroport Charles de Gaulle 2 TGV", "description": "Gare TGV intégrée au Terminal 2. Construite en 1994."},
        {"name": "Connexion CDGVAL", "description": "Métro automatique gratuit vers Terminal 1 et Terminal 3."},
    ],
    alternatives=[
        {"label": "RER B", "url": "/aeroports/paris-charles-de-gaulle/rer-b/", "note": "Depuis Paris : 35 min, 11,80 €."},
        {"label": "Roissybus", "url": "/aeroports/paris-charles-de-gaulle/bus/", "note": "Depuis Opéra : 60 min, 16,60 €."},
        {"label": "Taxi forfait", "url": "/aeroports/paris-charles-de-gaulle/taxi/", "note": "56 € / 65 €."},
    ],
    faq=[
        ("Y a-t-il un TGV direct à CDG ?", "<strong>Oui</strong>. <strong>Gare TGV intégrée au Terminal 2</strong> (depuis 1994). Liaisons directes vers Lille, Marseille, Lyon, Bordeaux, Nantes, Strasbourg."),
        ("Le TGV CDG est-il accessible depuis Bruxelles ?", "<strong>Oui</strong>, via <strong>Thalys / Eurostar</strong> (avec changement à Lille). <strong>1h35</strong>."),
        ("Quelle gare TGV à l'aéroport CDG ?", "<strong>Aéroport Charles de Gaulle 2 TGV</strong>, intégrée au Terminal 2."),
        ("Combien de temps pour aller du TGV à l'avion ?", "<strong>15 à 30 minutes</strong> selon le terminal. Si terminal 2A-2F : direct. Si terminal 1 ou 3 : via CDGVAL."),
        ("Combien coûte un TGV Lille → CDG ?", "<strong>30 à 80 €</strong> selon avance et période. Réservation recommandée."),
    ]
)))

# CDG — Taxi
PAGES.append(("paris-charles-de-gaulle", "taxi", page(
    aero_slug="paris-charles-de-gaulle", aero_name="Paris-Charles de Gaulle", aero_iata="CDG",
    mode_slug="taxi", mode_label="Taxi",
    color=COL["taxi"],
    h1="Taxi Paris → CDG : forfait 56 € / 65 € (rive droite / gauche)",
    seo_title="Taxi CDG : forfait 56 € rive droite, 65 € rive gauche — 60 min trajet 2026",
    seo_desc="Taxi Paris → Aéroport Paris-Charles de Gaulle : tarif forfaitaire 56 € rive droite, 65 € rive gauche. Durée 60 min. VTC Uber, Bolt alternatifs.",
    tagline="Forfait réglementé 56 € rive droite / 65 € rive gauche",
    intros=[
        "Le <strong>taxi parisien</strong> applique un <strong>tarif forfaitaire réglementé</strong> pour les courses entre Paris intra-muros et l'<strong>aéroport Paris-Charles de Gaulle</strong>.",
        "<strong>Durée moyenne : 60 min</strong> en conditions normales, jusqu'à 90 min en heure de pointe. Le forfait couvre <strong>4 passagers + bagages</strong>."
    ],
    quick_facts=[
        {"value": "56 €", "label": "rive droite"},
        {"value": "65 €", "label": "rive gauche"},
        {"value": "60 min", "label": "durée moyenne"},
        {"value": "25 km", "label": "distance"},
    ],
    itineraire={
        "h2": "Comment prendre un taxi pour CDG",
        "paragraphs": [
            "Plusieurs options pour prendre un taxi vers CDG :"
        ],
        "steps": [
            "<strong>Station de taxi</strong> : disponibles devant les grandes gares (Châtelet, Gare de Lyon, Gare du Nord, Saint-Lazare).",
            "<strong>Réservation par téléphone</strong> : G7 (3607), Taxis Bleus (3609). Supplément 7 €.",
            "<strong>Application mobile</strong> : G7, Bolt Taxis, Le Taxi.",
            "<strong>Confirmer le forfait</strong> avec le chauffeur avant départ : 56 € rive droite, 65 € rive gauche."
        ]
    },
    horaires={},
    tarifs={
        "h2": "Tarifs taxi Paris → CDG (2024)",
        "paragraphs": [
            "<strong>Tarif forfaitaire</strong> couvre la course pour tout passager + bagages."
        ],
        "table": {
            "headers": ["Trajet", "Tarif forfait", "Note"],
            "rows": [
                ["Paris Rive Droite → CDG", "56 €", "1er-4e, 8e-12e, 16e-20e arr."],
                ["Paris Rive Gauche → CDG", "65 €", "5e-7e, 13e-15e arr."],
                ["Supplément 5e passager", "+ 5,50 €", "Au-delà de 4 passagers."],
                ["Réservation par téléphone", "+ 7 €", "Optionnel."],
            ]
        }
    },
    itin_paris=[
        {"depart": "Châtelet (rive droite)", "station_slug": "chatelet", "duration": "60 min", "trajet": "Taxi 56 €."},
        {"depart": "Gare de Lyon (rive droite)", "station_slug": "gare-de-lyon", "duration": "55 min", "trajet": "Taxi 56 €."},
        {"depart": "Saint-Germain (rive gauche)", "station_slug": "saint-germain-des-pres", "duration": "65 min", "trajet": "Taxi 65 €."},
        {"depart": "Montparnasse (rive gauche)", "station_slug": "montparnasse-bienvenue", "duration": "70 min", "trajet": "Taxi 65 €."},
        {"depart": "Gare du Nord (rive droite)", "station_slug": "gare-du-nord", "duration": "50 min", "trajet": "Taxi 56 €."},
    ],
    pois=[
        {"name": "Station taxi - Terminal 1", "description": "Sortie « Arrivées », niveau 0."},
        {"name": "Station taxi - Terminal 2", "description": "Devant chaque module (2A-2F)."},
        {"name": "Station taxi - Terminal 3", "description": "Sortie « Arrivées »."},
    ],
    alternatives=[
        {"label": "RER B", "url": "/aeroports/paris-charles-de-gaulle/rer-b/", "note": "35 min depuis Châtelet, 11,80 € (5x moins cher !)."},
        {"label": "Roissybus", "url": "/aeroports/paris-charles-de-gaulle/bus/", "note": "60-75 min depuis Opéra, 16,60 €."},
        {"label": "TGV gare CDG", "url": "/aeroports/paris-charles-de-gaulle/tgv/", "note": "Depuis Lille, Bruxelles, Marseille."},
    ],
    faq=[
        ("Combien coûte un taxi Paris → CDG ?", "<strong>56 €</strong> depuis la <strong>Rive Droite</strong>, <strong>65 €</strong> depuis la <strong>Rive Gauche</strong>. <strong>Tarif forfaitaire réglementé</strong>."),
        ("Combien de temps en taxi Paris → CDG ?", "<strong>~60 min</strong> en conditions normales. <strong>~90 min</strong> aux heures de pointe."),
        ("Le forfait taxi couvre combien de passagers ?", "<strong>4 passagers</strong> + bagages. <strong>5e passager : +5,50 €</strong>."),
        ("Combien coûte un VTC Paris → CDG ?", "<strong>40 à 80 €</strong> selon trafic et heure (Uber, Bolt). Prix dynamique."),
        ("Comment réserver un taxi pour CDG ?", "Par téléphone (<strong>G7 : 3607</strong>, <strong>Taxis Bleus : 3609</strong>) avec 7 € de supplément, ou via application (G7, Bolt Taxis)."),
    ]
)))

# CDG — CDGVAL
PAGES.append(("paris-charles-de-gaulle", "cdgval", page(
    aero_slug="paris-charles-de-gaulle", aero_name="Paris-Charles de Gaulle", aero_iata="CDG",
    mode_slug="cdgval", mode_label="CDGVAL",
    color=COL["cdgval"],
    h1="CDGVAL : navette inter-terminaux gratuite à Charles de Gaulle",
    seo_title="CDGVAL CDG : navette gratuite inter-terminaux — horaires 2026",
    seo_desc="CDGVAL est le métro automatique gratuit à Paris-Charles de Gaulle, reliant les Terminaux 1, 2, 3 et les parkings. Fréquence 4 min, 24h/24.",
    tagline="Métro automatique gratuit — 24h/24",
    intros=[
        "Le <strong>CDGVAL</strong> est un <strong>métro automatique gratuit</strong> qui circule à l'intérieur de l'aéroport <strong>Paris-Charles de Gaulle</strong>. Il relie les <strong>3 terminaux</strong> (T1, T2, T3) et les <strong>parkings longue durée</strong> (PR-PX).",
        "<strong>Service 24h/24</strong>, <strong>fréquence toutes les 4 minutes</strong>. <strong>Gratuit</strong> pour tous les voyageurs et accompagnants. Inauguré en <strong>2007</strong>."
    ],
    quick_facts=[
        {"value": "Gratuit", "label": "tarif"},
        {"value": "24h/24", "label": "service"},
        {"value": "4 min", "label": "fréquence"},
        {"value": "5 stations", "label": "réseau"},
    ],
    itineraire={
        "h2": "Comment utiliser le CDGVAL",
        "paragraphs": [
            "Le CDGVAL fonctionne comme un <strong>petit métro automatique</strong>, sans conducteur, à fréquence très élevée."
        ],
        "steps": [
            "Suivre la signalétique <strong>« CDGVAL »</strong> ou <strong>« Inter-terminaux »</strong>.",
            "Aucun ticket nécessaire. <strong>Accès libre</strong>.",
            "Monter dans la prochaine rame (fréquence 4 min).",
            "Descendre à la station correspondant à votre terminal ou parking.",
            "Compter <strong>8 min maximum</strong> entre les terminaux 1 et 2."
        ]
    },
    horaires={
        "h2": "Horaires CDGVAL",
        "paragraphs": [
            "Service <strong>24h/24</strong>, <strong>7 jours/7</strong>. Fréquence réduite la nuit (8-10 min)."
        ],
        "table": {
            "headers": ["Période", "Fréquence"],
            "rows": [
                ["Journée (05h-23h)", "4 min"],
                ["Soir (23h-01h)", "5 min"],
                ["Nuit (01h-05h)", "8-10 min"],
            ]
        }
    },
    tarifs={
        "h2": "Tarif CDGVAL",
        "paragraphs": [
            "Le <strong>CDGVAL est entièrement gratuit</strong>. Aucun ticket ou pass requis."
        ]
    },
    itin_paris=[
        {"depart": "Terminal 1 (T1)", "station_slug": "", "duration": "8 min", "trajet": "CDGVAL → T2."},
        {"depart": "Terminal 2 - gare TGV/RER", "station_slug": "", "duration": "4 min", "trajet": "CDGVAL → T3."},
        {"depart": "Terminal 3 (low-cost)", "station_slug": "", "duration": "8 min", "trajet": "CDGVAL → T1."},
        {"depart": "Parkings longue durée PR-PX", "station_slug": "", "duration": "10-15 min", "trajet": "CDGVAL → tous terminaux."},
    ],
    pois=[
        {"name": "Station CDGVAL - Terminal 1", "description": "Niveau accès, suivre signalétique « CDGVAL »."},
        {"name": "Station CDGVAL - Terminal 2", "description": "Au cœur de la gare TGV/RER 2."},
        {"name": "Station CDGVAL - Terminal 3", "description": "Accès direct au Terminal 3 low-cost."},
        {"name": "Station CDGVAL - Parking longue durée", "description": "Stations PR-PX."},
    ],
    alternatives=[
        {"label": "RER B", "url": "/aeroports/paris-charles-de-gaulle/rer-b/", "note": "Depuis Paris : 35 min, 11,80 €."},
        {"label": "Bus aéroport", "url": "/aeroports/paris-charles-de-gaulle/bus/", "note": "Roissybus / 350 / 351."},
    ],
    faq=[
        ("Le CDGVAL est-il payant ?", "<strong>Non</strong>. <strong>Entièrement gratuit</strong>. Aucun ticket requis."),
        ("Le CDGVAL fonctionne-t-il la nuit ?", "<strong>Oui, 24h/24</strong>. Fréquence réduite la nuit (8-10 min)."),
        ("Combien de temps T1 → T2 en CDGVAL ?", "<strong>8 minutes</strong>."),
        ("Le CDGVAL relie-t-il les parkings ?", "<strong>Oui</strong>. Stations <strong>PR</strong> et <strong>PX</strong> pour les parkings longue durée."),
        ("Le CDGVAL a-t-il un conducteur ?", "<strong>Non</strong>, c'est un <strong>métro automatique</strong> sans conducteur."),
    ]
)))


# ============ BEAUVAIS (3 pages) ============

# Beauvais — Navette
PAGES.append(("paris-beauvais-tille", "navette", page(
    aero_slug="paris-beauvais-tille", aero_name="Paris-Beauvais", aero_iata="BVA",
    mode_slug="navette", mode_label="Navette",
    color=COL["navette"],
    h1="Navette Paris-Beauvais : Porte Maillot, 75 min, 17 € (officielle)",
    seo_title="Navette Beauvais Porte Maillot : 75 min, 17 € — horaires Ryanair, Wizz Air 2026",
    seo_desc="Navette officielle Paris ↔ Aéroport Paris-Beauvais depuis Porte Maillot : 75 min, 17 €. Coordonnée aux vols Ryanair et Wizz Air. Horaires, réservation.",
    tagline="Solution recommandée — Porte Maillot ↔ Beauvais 75 min 17 €",
    intros=[
        "La <strong>navette officielle</strong> est la <strong>solution recommandée</strong> pour rejoindre l'<strong>aéroport Paris-Beauvais</strong>. Elle part de la <strong>Porte Maillot</strong> (Paris 17e) et arrive directement aux terminaux T1 et T2.",
        "Cette navette est <strong>coordonnée avec les vols Ryanair et Wizz Air</strong> : horaires synchronisés sur les arrivées et départs. <strong>Durée 75 min</strong>, <strong>prix 17 € aller simple</strong> (30 € aller-retour). <strong>Réservation en ligne fortement recommandée</strong>."
    ],
    quick_facts=[
        {"value": "75 min", "label": "Porte Maillot ↔ BVA"},
        {"value": "17 €", "label": "aller simple"},
        {"value": "30 €", "label": "aller-retour"},
        {"value": "Coordonnée", "label": "aux vols"},
    ],
    itineraire={
        "h2": "Itinéraire navette Paris → Beauvais",
        "paragraphs": [
            "La navette officielle est <strong>la seule liaison directe</strong> entre Paris et l'aéroport Paris-Beauvais."
        ],
        "steps": [
            "Se rendre à la <strong>Porte Maillot</strong> (Paris 17e). Accès en <strong>métro 1</strong> ou <strong>RER C</strong>.",
            "Trouver le <strong>parking Pershing</strong> (Boulevard Pershing) où sont stationnées les navettes.",
            "<strong>Réservation préalable</strong> en ligne très fortement recommandée (sur le site officiel) — places limitées en cas de vol bondé.",
            "Monter dans la navette indiquant le numéro de votre vol.",
            "Durée du trajet : <strong>75 minutes</strong> via l'<strong>autoroute A16</strong>.",
            "Arrivée au <strong>T1 ou T2</strong> selon votre compagnie."
        ]
    },
    horaires={
        "h2": "Horaires navette Beauvais",
        "paragraphs": [
            "Les horaires sont <strong>coordonnés aux vols Ryanair et Wizz Air</strong>. Pas de fréquence fixe : les départs s'enchaînent en fonction des arrivées et départs avions."
        ],
        "table": {
            "headers": ["Information", "Détail"],
            "rows": [
                ["Premier départ Porte Maillot", "Vers 05h00"],
                ["Dernier départ Porte Maillot", "Vers 23h00"],
                ["Fréquence", "Coordonnée aux vols"],
                ["Arrivée à Beauvais avant vol", "3h avant départ recommandé"],
                ["Retour Beauvais → Paris", "Selon vol d'arrivée"],
            ]
        }
    },
    tarifs={
        "h2": "Tarifs navette Paris-Beauvais",
        "paragraphs": [
            "<strong>Tarif unique</strong>, indépendant de l'âge et de la classe."
        ],
        "table": {
            "headers": ["Titre", "Prix"],
            "rows": [
                ["Aller simple", "17 €"],
                ["Aller-retour", "30 €"],
                ["Enfant 3-11 ans", "10 €"],
                ["Enfant -2 ans", "Gratuit"],
                ["Bagages", "Inclus"],
            ]
        }
    },
    itin_paris=[
        {"depart": "Porte Maillot (départ navette)", "station_slug": "porte-maillot", "duration": "75 min", "trajet": "Navette directe BVA."},
        {"depart": "Charles de Gaulle - Étoile", "station_slug": "charles-de-gaulle-etoile", "duration": "1h25", "trajet": "M1 → Porte Maillot + navette."},
        {"depart": "Châtelet", "station_slug": "chatelet", "duration": "1h45", "trajet": "M1 → Porte Maillot + navette."},
        {"depart": "Gare du Nord", "station_slug": "gare-du-nord", "duration": "1h40", "trajet": "RER A/B/E → Étoile + M1 + navette."},
        {"depart": "Aéroport CDG", "station_slug": "", "duration": "1h55", "trajet": "RER B → Châtelet + M1 + navette (pas optimal)."},
    ],
    pois=[
        {"name": "Parking Pershing - Porte Maillot", "description": "Point de départ de toutes les navettes."},
        {"name": "Terminal T1 Beauvais", "description": "Vol Ryanair principalement."},
        {"name": "Terminal T2 Beauvais", "description": "Wizz Air et autres low-cost."},
    ],
    alternatives=[
        {"label": "Train Paris-Nord + bus", "url": "/aeroports/paris-beauvais-tille/train/", "note": "TER 1h15 + bus 15 min, 14-22 €."},
        {"label": "Taxi", "url": "/aeroports/paris-beauvais-tille/taxi/", "note": "90 min, 180-250 € (très onéreux)."},
    ],
    faq=[
        ("Comment aller à Paris-Beauvais depuis Paris ?", "<strong>Navette officielle</strong> depuis <strong>Porte Maillot</strong> : <strong>75 min</strong>, <strong>17 €</strong> aller simple. <strong>Réservation en ligne recommandée</strong>."),
        ("Où prendre la navette Beauvais à Paris ?", "<strong>Porte Maillot</strong>, parking Pershing. Accès en <strong>M1</strong> ou <strong>RER C</strong>."),
        ("Combien coûte la navette Beauvais ?", "<strong>17 €</strong> aller simple, <strong>30 €</strong> aller-retour. Enfant 3-11 ans : <strong>10 €</strong>."),
        ("Faut-il réserver la navette Beauvais ?", "<strong>Très fortement recommandé</strong>. Places limitées en cas de vol bondé."),
        ("Combien de temps Porte Maillot → Beauvais ?", "<strong>75 minutes</strong> via l'<strong>autoroute A16</strong>."),
        ("La navette est-elle coordonnée aux vols ?", "<strong>Oui</strong>. Horaires synchronisés avec les <strong>arrivées et départs Ryanair / Wizz Air</strong>."),
        ("Combien de temps avant le vol arriver à Beauvais ?", "<strong>3 heures avant le départ du vol</strong> est recommandé. Comptez 75 min de navette + 3h check-in/sécurité = 4h15 avant le vol."),
    ]
)))

# Beauvais — Train
PAGES.append(("paris-beauvais-tille", "train", page(
    aero_slug="paris-beauvais-tille", aero_name="Paris-Beauvais", aero_iata="BVA",
    mode_slug="train", mode_label="Train",
    color=COL["train"],
    h1="Train Paris → Beauvais : TER Paris-Nord + bus, 1h45 trajet total",
    seo_title="Train Beauvais : TER Paris-Nord 1h15 + bus aéroport 15 min — alternative navette",
    seo_desc="Train Paris → Aéroport Paris-Beauvais : TER depuis Gare du Nord (1h15) + bus 12/14 (15 min). Alternative à la navette. Horaires, prix.",
    tagline="TER Paris-Nord 1h15 + bus 15 min — alternative",
    intros=[
        "Une <strong>alternative à la navette officielle</strong> est de prendre un <strong>TER depuis la Gare du Nord</strong> jusqu'à <strong>Beauvais SNCF</strong>, puis un <strong>bus</strong> vers l'aéroport.",
        "<strong>Solution plus lente et moins fiable</strong> que la navette, mais utile si vous arrivez en train à la Gare du Nord. <strong>Durée totale : 1h45 à 2h</strong>. <strong>Prix : 14 à 22 €</strong> (TER + bus)."
    ],
    quick_facts=[
        {"value": "1h45-2h", "label": "durée totale"},
        {"value": "14-22 €", "label": "prix combiné"},
        {"value": "TER", "label": "Paris-Nord ↔ Beauvais"},
        {"value": "Bus 12/14", "label": "vers aéroport"},
    ],
    itineraire={
        "h2": "Itinéraire train + bus Paris → Beauvais",
        "paragraphs": [
            "Le trajet se compose en <strong>deux étapes</strong> : TER puis bus."
        ],
        "steps": [
            "Se rendre à la <strong>Gare du Nord</strong> (Paris 10e).",
            "Prendre un <strong>TER direction Beauvais</strong>. Durée : <strong>1h15</strong>. <strong>Pas tous les trains</strong> vont à Beauvais — vérifier les horaires SNCF.",
            "Arriver à la <strong>Gare SNCF de Beauvais</strong>.",
            "Sortir de la gare et prendre le <strong>bus 12 ou 14</strong> en direction de l'aéroport. Durée : <strong>15 minutes</strong>.",
            "Arrivée aux terminaux <strong>T1 ou T2</strong>."
        ]
    },
    horaires={
        "h2": "Horaires TER Paris-Nord ↔ Beauvais",
        "paragraphs": [
            "<strong>TER fréquent</strong> en journée, plus rare le soir et la nuit. <strong>Premier train</strong> vers 05h45, <strong>dernier train</strong> vers 23h00."
        ],
        "table": {
            "headers": ["Service", "Premier", "Dernier", "Fréquence"],
            "rows": [
                ["TER Paris-Nord → Beauvais", "05h45", "23h00", "1h"],
                ["Bus 12/14 Beauvais Gare → Aéroport", "05h30", "23h30", "30-60 min"],
            ]
        }
    },
    tarifs={
        "h2": "Tarifs train Paris → Beauvais",
        "paragraphs": [
            "Le <strong>TER</strong> est moins cher que la navette mais plus long. <strong>Réservation à l'avance</strong> peut permettre de bénéficier de tarifs réduits."
        ],
        "table": {
            "headers": ["Trajet", "Prix"],
            "rows": [
                ["TER Paris-Nord → Beauvais SNCF (2e classe)", "10 à 18 €"],
                ["TER 1re classe", "18 à 28 €"],
                ["Bus 12 ou 14 (Beauvais ville)", "4 €"],
                ["Total combiné", "14-22 €"],
            ]
        }
    },
    itin_paris=[
        {"depart": "Gare du Nord", "station_slug": "gare-du-nord", "duration": "1h45-2h", "trajet": "TER + bus."},
        {"depart": "Châtelet", "station_slug": "chatelet", "duration": "2h", "trajet": "M4 → Gare du Nord + TER + bus."},
        {"depart": "Saint-Lazare", "station_slug": "saint-lazare", "duration": "2h", "trajet": "M3/M12 → Gare du Nord + TER + bus."},
    ],
    pois=[
        {"name": "Gare du Nord (Paris)", "description": "Plus grande gare d'Europe par trafic. Départ TER Beauvais."},
        {"name": "Gare SNCF de Beauvais", "description": "Au centre-ville de Beauvais, à 8 km de l'aéroport."},
        {"name": "Bus 12 ou 14 (RTBL)", "description": "Bus de Beauvais ville reliant la gare SNCF à l'aéroport."},
    ],
    alternatives=[
        {"label": "Navette officielle", "url": "/aeroports/paris-beauvais-tille/navette/", "note": "75 min depuis Porte Maillot, 17 € (recommandé)."},
        {"label": "Taxi", "url": "/aeroports/paris-beauvais-tille/taxi/", "note": "90 min, 180-250 € (très onéreux)."},
    ],
    faq=[
        ("Y a-t-il un train direct Paris → Beauvais ?", "<strong>Non</strong>. <strong>TER Paris-Nord ↔ Beauvais SNCF</strong> (1h15), puis <strong>bus 12/14</strong> vers l'aéroport (15 min)."),
        ("Combien coûte le train Paris → Beauvais ?", "<strong>TER 2e classe : 10 à 18 €</strong>. Total combiné train + bus : <strong>14 à 22 €</strong>."),
        ("Combien de temps train + bus Paris → Beauvais ?", "<strong>1h45 à 2h</strong> selon les correspondances."),
        ("Le TER Beauvais est-il fréquent ?", "<strong>Toutes les heures environ</strong> en journée. Plus rare le soir."),
        ("Train ou navette pour Beauvais ?", "<strong>Navette officielle</strong> est plus rapide (75 min vs 2h) et plus fiable. <strong>Train</strong> est utile uniquement si vous arrivez ou repartez de la Gare du Nord en train."),
    ]
)))

# Beauvais — Taxi
PAGES.append(("paris-beauvais-tille", "taxi", page(
    aero_slug="paris-beauvais-tille", aero_name="Paris-Beauvais", aero_iata="BVA",
    mode_slug="taxi", mode_label="Taxi",
    color=COL["taxi"],
    h1="Taxi Paris → Beauvais : ~250 € pour 85 km (à éviter sauf groupe)",
    seo_title="Taxi Beauvais : ~250 € depuis Paris, 90 min — alternative VTC, navette",
    seo_desc="Taxi Paris → Aéroport Paris-Beauvais : 180-250 €, 90 min trajet (85 km hors d'Île-de-France). Alternative VTC, navette officielle 17 €.",
    tagline="180-250 € pour 90 min — à éviter sauf urgence",
    intros=[
        "Le <strong>taxi</strong> est une option <strong>très onéreuse</strong> pour rejoindre l'<strong>aéroport Paris-Beauvais</strong> en raison de la distance : <strong>85 km</strong>, hors d'Île-de-France.",
        "<strong>Pas de tarif forfaitaire</strong>. <strong>Prix estimé : 180 à 250 €</strong> selon trafic et heure. À <strong>éviter sauf urgence</strong> ou <strong>groupe</strong> (partage des frais). Pour la plupart des voyageurs, la <strong>navette officielle</strong> à 17 € est bien plus économique."
    ],
    quick_facts=[
        {"value": "180-250 €", "label": "prix estimé"},
        {"value": "90 min", "label": "durée"},
        {"value": "85 km", "label": "distance"},
        {"value": "Hors IDF", "label": "tarif élevé"},
    ],
    itineraire={
        "h2": "Comment prendre un taxi pour Beauvais",
        "paragraphs": [
            "Le taxi vers Beauvais n'est <strong>pas une option courante</strong> en raison du coût élevé."
        ],
        "steps": [
            "<strong>Réservation préalable obligatoire</strong> auprès d'une compagnie de taxi (G7, Taxis Bleus) ou VTC longue distance.",
            "Confirmer le <strong>prix estimé</strong> avant le départ : <strong>180 à 250 €</strong>.",
            "Trajet via <strong>autoroute A16</strong>. <strong>Péage : ~3,80 €</strong> (inclus dans le prix).",
            "Durée : <strong>~90 minutes</strong> en conditions normales."
        ]
    },
    horaires={},
    tarifs={
        "h2": "Tarifs taxi Paris → Beauvais",
        "paragraphs": [
            "<strong>Pas de tarif forfaitaire</strong>. Prix au compteur ou estimé selon la compagnie."
        ],
        "table": {
            "headers": ["Service", "Prix"],
            "rows": [
                ["Taxi Paris → Beauvais (estimé)", "180-250 €"],
                ["VTC Uber / Bolt (longue distance)", "120-200 €"],
                ["Péage A16 (inclus)", "~3,80 €"],
                ["Heure de pointe", "+ 10-30 %"],
            ]
        }
    },
    itin_paris=[
        {"depart": "Paris centre", "station_slug": "chatelet", "duration": "90 min", "trajet": "Taxi via A16."},
        {"depart": "Aéroport CDG", "station_slug": "", "duration": "75 min", "trajet": "Taxi direct (~150 €)."},
        {"depart": "Aéroport Orly", "station_slug": "", "duration": "1h45", "trajet": "Taxi long trajet (~250 €)."},
    ],
    pois=[
        {"name": "Station taxi - Aéroport Beauvais", "description": "Devant le Terminal T1 et T2."},
    ],
    alternatives=[
        {"label": "Navette officielle", "url": "/aeroports/paris-beauvais-tille/navette/", "note": "75 min depuis Porte Maillot, 17 € (15x moins cher !)."},
        {"label": "Train + bus", "url": "/aeroports/paris-beauvais-tille/train/", "note": "TER + bus depuis Gare du Nord, 14-22 €."},
    ],
    faq=[
        ("Combien coûte un taxi Paris → Beauvais ?", "<strong>180 à 250 €</strong> selon trafic et heure. <strong>Très onéreux</strong> en raison des <strong>85 km</strong>."),
        ("Combien de temps en taxi Paris → Beauvais ?", "<strong>~90 minutes</strong> via l'autoroute A16."),
        ("Combien coûte un VTC Paris → Beauvais ?", "<strong>120 à 200 €</strong> selon la demande (Uber, Bolt)."),
        ("Y a-t-il un forfait taxi Paris → Beauvais ?", "<strong>Non</strong>. Beauvais est <strong>hors d'Île-de-France</strong>, pas de tarif forfaitaire réglementé."),
        ("Navette ou taxi pour Beauvais ?", "<strong>Navette officielle</strong> à <strong>17 €</strong> est <strong>15 fois moins chère</strong> que le taxi (~250 €). Privilégier sauf groupe de 6+ personnes."),
    ]
)))


def write_page(aero_slug, mode_slug, data):
    aero_dir = AERO / aero_slug
    aero_dir.mkdir(parents=True, exist_ok=True)
    p = aero_dir / f"{mode_slug}.json"
    p.write_text(json.dumps(data, indent=4, ensure_ascii=False) + "\n")
    print(f"✓ {aero_slug}/{mode_slug}")


if __name__ == "__main__":
    for aero, mode, data in PAGES:
        try: write_page(aero, mode, data)
        except Exception as e: print(f"✗ {aero}/{mode}: {e}")
    print(f"\nTotal : {len(PAGES)} pages mode")
