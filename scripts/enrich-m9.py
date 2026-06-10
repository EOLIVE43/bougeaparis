#!/usr/bin/env python3
"""Enrichit M9 — 23 stations T0 (LIGNE 9 = LA DERNIÈRE)."""
import json
from pathlib import Path
ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    "pont-de-sevres": {
        "addr": "Quai du Point-du-Jour, 92100 Boulogne-Billancourt", "arr": "Boulogne-Billancourt (92)",
        "seo": "Station Pont de Sèvres, terminus ouest M9 à Boulogne-Billancourt (92). Île Seguin et Seine Musicale (2017, Shigeru Ban) à proximité.",
        "tagline": "M9 — terminus ouest, Île Seguin, Seine Musicale",
        "hero_desc": "Station <strong>Pont de Sèvres</strong>, <strong>terminus ouest de la M9</strong>, à <strong>Boulogne-Billancourt</strong> (Hauts-de-Seine, 92). Ouverte le <strong>3 octobre 1934</strong>. À proximité du <strong>Pont de Sèvres</strong>, de l'<strong>Île Seguin</strong> et de <strong>La Seine Musicale</strong> (2017, Shigeru Ban).",
        "intros": [
            "La station <strong>Pont de Sèvres</strong> est <strong>terminus ouest de la M9</strong>, à <strong>Boulogne-Billancourt</strong> (Hauts-de-Seine, 92). Bus 52, 72, 123, 126, 175, 179, 279, 426, 467.",
            "Ouverte le <strong>3 octobre 1934</strong> avec le <strong>prolongement de la M9</strong> de Porte de Saint-Cloud à Pont de Sèvres.",
            "À proximité : le <strong>Pont de Sèvres</strong> sur la Seine, l'<strong>Île Seguin</strong> (anciennes <strong>usines Renault</strong>, reconvertie en <strong>quartier culturel</strong>), <strong>La Seine Musicale</strong> (2017, architecte japonais <strong>Shigeru Ban</strong>)."
        ],
        "hist_title": "1934 : terminus ouest et Île Seguin",
        "hist": [
            "La station Pont de Sèvres est <strong>inaugurée le 3 octobre 1934</strong> avec le <strong>prolongement de la M9</strong>.",
            "L'<strong>Île Seguin</strong>, à proximité, fut le siège des <strong>usines Renault</strong> de <strong>1929 à 1992</strong>. <strong>30 000 ouvriers</strong> à son apogée. <strong>Symbole de l'industrie automobile française</strong>.",
            "L'île est <strong>reconvertie en quartier culturel</strong> depuis les années 2010. <strong>La Seine Musicale</strong>, <strong>auditorium</strong> conçu par <strong>Shigeru Ban</strong> (Pritzker 2014), <strong>inaugurée en 2017</strong>. <strong>1 150 places</strong>, <strong>acoustique exceptionnelle</strong>. <strong>Boulogne-Billancourt</strong> (~120 000 habitants), <strong>plus grande commune des Hauts-de-Seine</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Pont de Sèvres ?", "Uniquement la <strong>M9</strong> (terminus ouest). Bus 52, 72, 123, 126, 175, 179, 279, 426, 467."),
            ("Quand a-t-elle ouvert ?", "Le <strong>3 octobre 1934</strong>."),
            ("Pour l'Île Seguin ?", "<strong>~10 min à pied</strong>. Anciennes usines Renault."),
            ("Pour La Seine Musicale ?", "<strong>~12 min à pied</strong>. Auditorium Shigeru Ban (2017)."),
            ("Pour Paris centre ?", "<strong>M9 directe</strong> vers République (~30 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Île Seguin</strong> à 10 min : ancien fief Renault reconverti.",
            "<strong>La Seine Musicale</strong> à 12 min : auditorium Shigeru Ban (2017).",
            "<strong>Boulogne-Billancourt</strong> commune dynamique 92.",
            "Pour <strong>République</strong> : <strong>M9 directe</strong> (~30 min).",
            "Zone tarifaire <strong>2</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("🏭", "Île Seguin et usines Renault (1929-1992)", "L'<strong>Île Seguin</strong>, à 10 min à pied, fut le <strong>siège des usines Renault</strong> de <strong>1929 à 1992</strong>. <strong>30 000 ouvriers</strong> à son apogée. <strong>Symbole de l'industrie automobile française</strong>. <strong>Fermée en 1992</strong>, démolie en 2005. <strong>Reconvertie en quartier culturel</strong> depuis les années 2010 : <strong>La Seine Musicale</strong> (2017), nouveaux <strong>quartiers résidentiels et tertiaires</strong>."),
            ("🎵", "La Seine Musicale (2017), Shigeru Ban", "<strong>La Seine Musicale</strong>, à 12 min à pied, est <strong>inaugurée le 22 avril 2017</strong>. Œuvre de l'<strong>architecte japonais Shigeru Ban</strong> (<strong>Prix Pritzker 2014</strong>) et <strong>Jean de Gastines</strong>. <strong>Auditorium en forme d'œuf</strong>, <strong>structure en bois</strong>. <strong>1 150 places</strong>, <strong>acoustique exceptionnelle</strong> (Nagata Acoustics). <strong>Voile photovoltaïque</strong> mobile. Accueille l'<strong>Insula Orchestra</strong> de Laurence Equilbey.")
        ],
        "itin": [
            ("Île Seguin", "pont-de-sevres", "à pied", "10 min à pied", 10),
            ("La Seine Musicale", "pont-de-sevres", "à pied", "12 min à pied", 12),
            ("Billancourt", "billancourt", "M9", "M9 directe (1 station)", 2),
            ("Parc des Princes", "porte-de-saint-cloud", "M9", "M9 directe (3 stations)", 7),
            ("République", "republique", "M9", "M9 directe (~30 min)", 30),
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (~16 min)", 16)
        ]
    },
    "billancourt": {
        "addr": "Rue Marcel-Bontemps, 92100 Boulogne-Billancourt", "arr": "Boulogne-Billancourt (92)",
        "seo": "Station Billancourt (M9) à Boulogne-Billancourt (92). Quartier industriel reconverti. Île Seguin proche.",
        "tagline": "M9 — Billancourt, ancien quartier industriel",
        "hero_desc": "Station <strong>Billancourt</strong> à <strong>Boulogne-Billancourt</strong> (Hauts-de-Seine, 92). Desservie par la <strong>M9</strong>, ouverte le <strong>3 octobre 1934</strong>. Ancien <strong>quartier industriel</strong> reconverti.",
        "intros": [
            "La station <strong>Billancourt</strong> est implantée à <strong>Boulogne-Billancourt</strong> (Hauts-de-Seine, 92). Elle est desservie par la <strong>M9</strong>, entre <strong>Pont de Sèvres</strong> (1 station) et <strong>Marcel Sembat</strong> (1 station). Bus 52, 175, 179, 279, 389.",
            "Ouverte le <strong>3 octobre 1934</strong> avec le <strong>prolongement de la M9</strong>.",
            "Le nom <strong>Billancourt</strong> rappelle l'<strong>ancien village de Billancourt</strong>, fusionné avec <strong>Boulogne-sur-Seine</strong> en <strong>1924</strong> pour former <strong>Boulogne-Billancourt</strong>. Quartier marqué par l'<strong>industrie automobile</strong> (usines Renault de l'Île Seguin)."
        ],
        "hist_title": "1934 : ancien village de Billancourt",
        "hist": [
            "La station Billancourt est <strong>inaugurée le 3 octobre 1934</strong> avec le <strong>prolongement de la M9</strong>.",
            "Le nom <strong>Billancourt</strong> rappelle l'<strong>ancien village de Billancourt</strong>, fusionné avec <strong>Boulogne-sur-Seine</strong> en <strong>1924</strong> pour former <strong>Boulogne-Billancourt</strong>. Étymologie : du latin <em>Bilenni curtis</em>, « domaine de Bilenne ».",
            "Quartier marqué au <strong>XXe siècle</strong> par l'<strong>industrie automobile</strong> avec les <strong>usines Renault</strong> de l'<strong>Île Seguin</strong> (1929-1992). <strong>Reconversion progressive</strong> en <strong>quartier résidentiel et tertiaire</strong> depuis les années 1990."
        ],
        "faq": [
            ("Quelle ligne dessert Billancourt ?", "Uniquement la <strong>M9</strong>. Bus 52, 175, 179, 279, 389."),
            ("Quand a-t-elle ouvert ?", "Le <strong>3 octobre 1934</strong>."),
            ("Pour l'Île Seguin ?", "<strong>~10 min à pied</strong>."),
            ("Pour la Seine Musicale ?", "<strong>~12 min à pied</strong>."),
            ("Pour Trocadéro et Tour Eiffel ?", "<strong>M9 directe</strong> (~14 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Île Seguin</strong> à 10 min à pied : ancien fief Renault.",
            "<strong>La Seine Musicale</strong> à 12 min à pied.",
            "Pour <strong>Trocadéro et Tour Eiffel</strong> : <strong>M9 directe</strong>.",
            "Pour <strong>République</strong> : <strong>M9 directe</strong>.",
            "Zone tarifaire <strong>2</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("🏭", "Boulogne-Billancourt, fusion 1924", "<strong>Boulogne-Billancourt</strong>, ~120 000 habitants, est née de la <strong>fusion en 1924</strong> des communes de <strong>Boulogne-sur-Seine</strong> et de <strong>Billancourt</strong>. <strong>Plus grande commune des Hauts-de-Seine</strong> par sa population. Au <strong>XXe siècle</strong>, ville industrielle célèbre pour les <strong>usines Renault</strong> sur l'<strong>île Seguin</strong>. Aujourd'hui, ~120 000 habitants, l'une des plus importantes communes d'Île-de-France."),
            ("🎬", "Billancourt et cinéma", "<strong>Boulogne-Billancourt</strong> a longtemps été un <strong>haut lieu du cinéma français</strong>. <strong>Studios de Billancourt</strong> (1924-1992), où furent tournés de nombreux films de <strong>Jean Renoir</strong>, <strong>Marcel Carné</strong>, <strong>Jean-Luc Godard</strong>. <strong>Studios désaffectés en 1992</strong>, remplacés par des <strong>logements et bureaux</strong>.")
        ],
        "itin": [
            ("Île Seguin", "pont-de-sevres", "à pied", "10 min à pied", 10),
            ("La Seine Musicale", "pont-de-sevres", "à pied", "12 min à pied", 12),
            ("Pont de Sèvres (terminus)", "pont-de-sevres", "M9", "M9 directe (1 station)", 2),
            ("Marcel Sembat", "marcel-sembat", "M9", "M9 directe (1 station)", 2),
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (~14 min)", 14),
            ("République", "republique", "M9", "M9 directe (~28 min)", 28)
        ]
    },
    "marcel-sembat": {
        "addr": "Avenue Édouard-Vaillant, 92100 Boulogne-Billancourt", "arr": "Boulogne-Billancourt (92)",
        "seo": "Station Marcel Sembat (M9) à Boulogne-Billancourt (92). Hommage à Marcel Sembat (1862-1922), homme politique et journaliste français.",
        "tagline": "M9 — Marcel Sembat, Boulogne-Billancourt",
        "hero_desc": "Station <strong>Marcel Sembat</strong> à <strong>Boulogne-Billancourt</strong> (Hauts-de-Seine, 92). Desservie par la <strong>M9</strong>, ouverte le <strong>3 octobre 1934</strong>. Hommage à <strong>Marcel Sembat</strong> (<strong>1862-1922</strong>), <strong>homme politique et journaliste français</strong>.",
        "intros": [
            "La station <strong>Marcel Sembat</strong> est implantée à <strong>Boulogne-Billancourt</strong> (Hauts-de-Seine, 92). Elle est desservie par la <strong>M9</strong>, entre <strong>Billancourt</strong> (1 station) et <strong>Porte de Saint-Cloud</strong> (1 station). Bus 123, 126, 175, 179.",
            "Ouverte le <strong>3 octobre 1934</strong> avec le <strong>prolongement de la M9</strong>.",
            "Le nom <strong>Marcel Sembat</strong> rend hommage à <strong>Marcel Sembat</strong> (<strong>1862-1922</strong>), <strong>homme politique et journaliste français</strong>. <strong>Député socialiste</strong> de la Seine. <strong>Ministre des Travaux publics</strong> (1914-1916)."
        ],
        "hist_title": "1934 : Marcel Sembat et journalisme",
        "hist": [
            "La station Marcel Sembat est <strong>inaugurée le 3 octobre 1934</strong> avec le <strong>prolongement de la M9</strong>.",
            "Le nom <strong>Marcel Sembat</strong> rend hommage à <strong>Marcel Sembat</strong> (<strong>19 octobre 1862 - 5 septembre 1922</strong>), <strong>homme politique et journaliste français</strong>. <strong>Avocat</strong>, puis <strong>député socialiste</strong> de la Seine de 1893 à 1922.",
            "<strong>Cofondateur du journal La Petite République</strong>. <strong>Ministre des Travaux publics</strong> sous Viviani et Briand (1914-1916). <strong>Auteur</strong> d'ouvrages sur la <strong>question sociale</strong>. <strong>Collectionneur d'art</strong>, sa collection enrichit plusieurs musées."
        ],
        "faq": [
            ("Quelle ligne dessert Marcel Sembat ?", "Uniquement la <strong>M9</strong>. Bus 123, 126, 175, 179."),
            ("Qui est Marcel Sembat ?", "<strong>Marcel Sembat</strong> (1862-1922), <strong>homme politique et journaliste</strong>. <strong>Député socialiste</strong>. <strong>Ministre des Travaux publics</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>3 octobre 1934</strong>."),
            ("Pour Porte de Saint-Cloud (Parc des Princes) ?", "<strong>M9 directe</strong> (1 station)."),
            ("Pour Pont de Sèvres ?", "<strong>M9 directe</strong> (2 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "Quartier <strong>Boulogne-Billancourt</strong> résidentiel.",
            "Pour <strong>Parc des Princes</strong> : <strong>M9 → Porte de Saint-Cloud</strong>.",
            "Pour <strong>Trocadéro</strong> et <strong>Tour Eiffel</strong> : <strong>M9 directe</strong>.",
            "Pour <strong>République</strong> : <strong>M9 directe</strong>.",
            "Zone tarifaire <strong>2</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("📰", "Marcel Sembat, député socialiste", "<strong>Marcel Sembat</strong> (1862-1922), <strong>avocat, homme politique et journaliste français</strong>. <strong>Député socialiste</strong> de la Seine de 1893 à 1922. <strong>Cofondateur du journal La Petite République</strong>. <strong>Ministre des Travaux publics</strong> dans les gouvernements <strong>Viviani et Briand</strong> (1914-1916). <strong>Auteur</strong> d'ouvrages sur la <strong>question sociale</strong>. <strong>Collectionneur d'art</strong>."),
            ("🏛️", "Boulogne-Billancourt, ville culturelle", "<strong>Boulogne-Billancourt</strong> est aujourd'hui une <strong>commune dynamique</strong> des Hauts-de-Seine. ~120 000 habitants. <strong>Mairie</strong>, <strong>musée Albert-Kahn</strong> (autochromes), <strong>Belvédère</strong>, <strong>Bois de Boulogne</strong> à proximité.")
        ],
        "itin": [
            ("Porte de Saint-Cloud", "porte-de-saint-cloud", "M9", "M9 directe (1 station)", 2),
            ("Parc des Princes (PSG)", "porte-de-saint-cloud", "M9", "M9 directe (1 station)", 5),
            ("Billancourt", "billancourt", "M9", "M9 directe (1 station)", 2),
            ("Pont de Sèvres (terminus)", "pont-de-sevres", "M9", "M9 directe (2 stations)", 4),
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (~12 min)", 12),
            ("République", "republique", "M9", "M9 directe (~26 min)", 26)
        ]
    },
    "porte-de-saint-cloud": {
        "addr": "Place de la Porte de Saint-Cloud, 75016 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Porte de Saint-Cloud (M9) place de la Porte de Saint-Cloud dans le 16e. Parc des Princes (PSG), Stade Jean-Bouin (rugby).",
        "tagline": "M9 — Parc des Princes, PSG",
        "hero_desc": "Station <strong>Porte de Saint-Cloud</strong> sur la <strong>place de la Porte de Saint-Cloud</strong> dans le <strong>16e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>29 septembre 1923</strong>. À proximité du <strong>Parc des Princes</strong> (stade du <strong>PSG</strong>) et du <strong>Stade Jean-Bouin</strong>.",
        "intros": [
            "La station <strong>Porte de Saint-Cloud</strong> est implantée sur la <strong>place de la Porte de Saint-Cloud</strong>, à la <strong>limite sud-ouest du 16e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Marcel Sembat</strong> (1 station, banlieue) et <strong>Exelmans</strong> (1 station). Bus 22, 32, 62, 72, 123, 126, 175, 189, 289, 389, PC1.",
            "Ouverte le <strong>29 septembre 1923</strong> comme <strong>terminus sud-ouest de la M9</strong> (jusqu'à l'extension de 1934 à Pont de Sèvres).",
            "À proximité : le <strong>Parc des Princes</strong>, <strong>stade emblématique du Paris Saint-Germain</strong> (PSG). <strong>Stade Jean-Bouin</strong> à proximité (rugby, <strong>Stade Français Paris</strong>)."
        ],
        "hist_title": "1923 : Parc des Princes (1972, Taillibert)",
        "hist": [
            "La station Porte de Saint-Cloud est <strong>inaugurée le 29 septembre 1923</strong> comme <strong>terminus sud-ouest de la M9</strong>.",
            "Le <strong>Parc des Princes</strong>, à proximité, est le <strong>stade emblématique du Paris Saint-Germain</strong> (PSG). <strong>48 712 places</strong>. <strong>Inauguré en 1972</strong>, conçu par l'architecte <strong>Roger Taillibert</strong> (auteur du stade olympique de Montréal).",
            "Le <strong>Stade Jean-Bouin</strong>, à proximité, est le <strong>stade du Stade Français Paris</strong> (rugby). <strong>20 000 places</strong>. <strong>Reconstruit en 2013</strong> par <strong>Rudy Ricciotti</strong>. Architecture <strong>contemporaine</strong> avec <strong>résille en béton blanc</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Porte de Saint-Cloud ?", "Uniquement la <strong>M9</strong>. Bus 22, 32, 62, 72, 123, 126, 175, 189, 289, 389, PC1."),
            ("Pour le Parc des Princes ?", "<strong>~5 min à pied</strong>. Stade du PSG, 48 712 places."),
            ("Pour le Stade Jean-Bouin ?", "<strong>~7 min à pied</strong>. Stade Français Paris (rugby)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>29 septembre 1923</strong>."),
            ("Pour Trocadéro et Tour Eiffel ?", "<strong>M9 directe</strong> (~10 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Parc des Princes</strong> à 5 min : stade emblématique du PSG.",
            "<strong>Stade Jean-Bouin</strong> à 7 min : Stade Français Paris (rugby).",
            "Pour <strong>Trocadéro</strong> et <strong>Tour Eiffel</strong> : <strong>M9 directe</strong>.",
            "Pour <strong>République</strong> : <strong>M9 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⚽", "Parc des Princes, stade du PSG (1972)", "Le <strong>Parc des Princes</strong>, à 5 min à pied, est le <strong>stade emblématique du Paris Saint-Germain</strong> (PSG). <strong>48 712 places</strong>. <strong>Inauguré en 1972</strong>, conçu par l'architecte <strong>Roger Taillibert</strong> (auteur du stade olympique de Montréal 1976). <strong>Architecture monolithique en béton</strong>. Accueille les <strong>matchs du PSG</strong> en Ligue 1 et Champions League, ainsi que les <strong>matchs internationaux de rugby</strong> (XV de France)."),
            ("🏉", "Stade Jean-Bouin, Stade Français Paris", "Le <strong>Stade Jean-Bouin</strong>, à 7 min à pied, est le <strong>stade du Stade Français Paris</strong> (rugby). <strong>20 000 places</strong>. <strong>Reconstruit en 2013</strong> par l'architecte <strong>Rudy Ricciotti</strong> (Pritzker 2006). Architecture <strong>contemporaine</strong> avec <strong>résille en béton blanc</strong> autour du stade. Tient son nom de <strong>Jean Bouin</strong> (1888-1914), <strong>athlète français</strong>.")
        ],
        "itin": [
            ("Parc des Princes", "porte-de-saint-cloud", "à pied", "5 min à pied", 5),
            ("Stade Jean-Bouin", "porte-de-saint-cloud", "à pied", "7 min à pied", 7),
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (~10 min)", 10),
            ("Exelmans", "exelmans", "M9", "M9 directe (1 station)", 2),
            ("République", "republique", "M9", "M9 directe (~24 min)", 24),
            ("Marcel Sembat (Boulogne)", "marcel-sembat", "M9", "M9 directe (1 station)", 2)
        ]
    },
    "exelmans": {
        "addr": "Boulevard Exelmans, 75016 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Exelmans (M9) boulevard Exelmans dans le 16e. Hommage au maréchal Exelmans. Quartier Auteuil résidentiel.",
        "tagline": "M9 — Maréchal Exelmans, 16e Auteuil",
        "hero_desc": "Station <strong>Exelmans</strong> sur le <strong>boulevard Exelmans</strong> dans le <strong>16e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>8 novembre 1922</strong>. Hommage à <strong>Rémy Joseph Isidore Exelmans</strong> (<strong>1775-1852</strong>), <strong>maréchal de France</strong>.",
        "intros": [
            "La station <strong>Exelmans</strong> est implantée sur le <strong>boulevard Exelmans</strong> dans le <strong>16e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Porte de Saint-Cloud</strong> (1 station) et <strong>Michel-Ange - Molitor</strong> (1 station). Bus 22, 62, 72.",
            "Ouverte le <strong>8 novembre 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "Le nom <strong>Exelmans</strong> rend hommage à <strong>Rémy Joseph Isidore Exelmans</strong> (<strong>1775-1852</strong>), <strong>général d'Empire</strong> puis <strong>maréchal de France</strong>. Quartier résidentiel chic du <strong>16e arrondissement</strong>."
        ],
        "hist_title": "1922 : Exelmans, maréchal d'Empire",
        "hist": [
            "La station Exelmans est <strong>inaugurée le 8 novembre 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "Le nom <strong>Exelmans</strong> rend hommage à <strong>Rémy Joseph Isidore Exelmans</strong> (<strong>13 novembre 1775 - 22 juillet 1852</strong>), <strong>général d'Empire</strong> puis <strong>maréchal de France</strong>. <strong>Officier de cavalerie</strong>.",
            "<strong>Aide de camp du général Murat</strong>, puis <strong>du roi Joseph d'Espagne</strong>. <strong>Suivi Napoléon</strong> aux Cent-Jours. <strong>Pair de France</strong> sous la Restauration. <strong>Maréchal de France</strong> en <strong>1851</strong> sous Louis-Napoléon Bonaparte."
        ],
        "faq": [
            ("Quelle ligne dessert Exelmans ?", "Uniquement la <strong>M9</strong>. Bus 22, 62, 72."),
            ("Qui est Exelmans ?", "<strong>Rémy Joseph Isidore Exelmans</strong> (1775-1852), <strong>maréchal de France</strong> sous Louis-Napoléon Bonaparte."),
            ("Quand a-t-elle ouvert ?", "Le <strong>8 novembre 1922</strong>."),
            ("Pour le Parc des Princes ?", "<strong>M9 directe</strong> (1 station vers Porte de Saint-Cloud)."),
            ("Pour Roland-Garros ?", "<strong>M9 → Michel-Ange - Molitor + M10</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier résidentiel chic du <strong>16e Auteuil</strong>.",
            "Pour <strong>Parc des Princes</strong> : <strong>M9 directe</strong> (1 station).",
            "Pour <strong>Roland-Garros</strong> : <strong>M9 + M10</strong>.",
            "Pour <strong>Trocadéro et Tour Eiffel</strong> : <strong>M9 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎖️", "Exelmans, maréchal de France 1851", "<strong>Rémy Joseph Isidore Exelmans</strong> (1775-1852), <strong>général d'Empire</strong> puis <strong>maréchal de France</strong>. <strong>Officier de cavalerie</strong>. <strong>Aide de camp du général Murat</strong>, puis <strong>du roi Joseph d'Espagne</strong>. <strong>Suivi Napoléon</strong> aux Cent-Jours après Waterloo. <strong>Pair de France</strong> sous la Restauration. <strong>Maréchal de France</strong> en <strong>1851</strong> sous Louis-Napoléon Bonaparte. <strong>Sénateur</strong> sous le Second Empire."),
            ("🏘️", "16e arrondissement Auteuil", "Le <strong>16e arrondissement</strong> est l'un des <strong>plus résidentiels et chic</strong> de Paris. <strong>~165 000 habitants</strong>. Comprend les anciens villages d'<strong>Auteuil</strong> et <strong>Passy</strong>, rattachés à Paris en <strong>1860</strong>. Plusieurs <strong>institutions majeures</strong> : <strong>Roland-Garros</strong>, <strong>Parc des Princes</strong>, <strong>Bois de Boulogne</strong>, <strong>Maison de la Radio</strong>.")
        ],
        "itin": [
            ("Parc des Princes", "porte-de-saint-cloud", "M9", "M9 directe (1 station)", 5),
            ("Roland-Garros", "porte-d-auteuil", "M9 + M10", "M9 → Michel-Ange - Molitor + M10", 10),
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (~8 min)", 8),
            ("Michel-Ange - Molitor (M9+M10)", "michel-ange-molitor", "M9", "M9 directe (1 station)", 2),
            ("République", "republique", "M9", "M9 directe (~22 min)", 22),
            ("Mairie de Montreuil (terminus est)", "mairie-de-montreuil", "M9", "M9 directe (~40 min)", 40)
        ]
    },
    "jasmin": {
        "addr": "Rue Jasmin, 75016 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Jasmin (M9) rue Jasmin dans le 16e. Hommage à Jasmin (1798-1864), poète occitan. Quartier Auteuil chic.",
        "tagline": "M9 — Jasmin, poète occitan",
        "hero_desc": "Station <strong>Jasmin</strong> sur la <strong>rue Jasmin</strong> dans le <strong>16e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>8 novembre 1922</strong>. Hommage à <strong>Jacques Boé dit Jasmin</strong> (<strong>1798-1864</strong>), <strong>poète occitan</strong>.",
        "intros": [
            "La station <strong>Jasmin</strong> est implantée sur la <strong>rue Jasmin</strong> dans le <strong>16e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Michel-Ange - Auteuil</strong> (1 station) et <strong>Ranelagh</strong> (1 station). Bus 22, 32, 52.",
            "Ouverte le <strong>8 novembre 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "Le nom <strong>Jasmin</strong> rend hommage à <strong>Jacques Boé dit Jasmin</strong> (<strong>1798-1864</strong>), <strong>poète occitan</strong> et <strong>perruquier d'Agen</strong>. <strong>Figure du renouveau de la langue d'oc</strong>. Quartier résidentiel chic du <strong>16e Auteuil</strong>."
        ],
        "hist_title": "1922 : Jasmin, poète d'Agen",
        "hist": [
            "La station Jasmin est <strong>inaugurée le 8 novembre 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "Le nom <strong>Jasmin</strong> rend hommage à <strong>Jacques Boé dit Jasmin</strong> (<strong>6 mars 1798 - 4 octobre 1864</strong>), <strong>poète occitan</strong>. <strong>Perruquier d'Agen</strong>, autodidacte.",
            "<strong>Figure du renouveau de la langue d'oc</strong> au XIXe siècle. <strong>Recueils de poésie en occitan gascon</strong> : <em>Las Papilhotas</em> (<strong>1835-1842</strong>). <strong>Tournées de récitations</strong> en France. Précurseur du <strong>Félibrige</strong> de Frédéric Mistral. Le quartier d'<strong>Auteuil</strong>, ancien village rattaché à Paris en <strong>1860</strong>, conserve son atmosphère résidentielle chic."
        ],
        "faq": [
            ("Quelle ligne dessert Jasmin ?", "Uniquement la <strong>M9</strong>. Bus 22, 32, 52."),
            ("Qui est Jasmin ?", "<strong>Jacques Boé dit Jasmin</strong> (1798-1864), <strong>poète occitan</strong>. Précurseur du <strong>renouveau de la langue d'oc</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>8 novembre 1922</strong>."),
            ("Pour le musée Marmottan Monet ?", "<strong>M9 → Ranelagh</strong> ou <strong>La Muette</strong>."),
            ("Pour Trocadéro ?", "<strong>M9 directe</strong> (~5 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier résidentiel chic du <strong>16e Auteuil</strong>.",
            "Pour <strong>musée Marmottan Monet</strong> : <strong>M9 → Ranelagh</strong> (2 stations).",
            "Pour <strong>Trocadéro et Tour Eiffel</strong> : <strong>M9 directe</strong>.",
            "Pour <strong>République</strong> : <strong>M9 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("📜", "Jasmin, perruquier-poète occitan", "<strong>Jacques Boé dit Jasmin</strong> (1798-1864), <strong>poète occitan</strong> d'Agen. <strong>Perruquier de profession</strong>, <strong>autodidacte</strong>. <strong>Figure du renouveau de la langue d'oc</strong> au XIXe siècle. <strong>Recueils de poésie en occitan gascon</strong> : <em><strong>Las Papilhotas</strong></em> (<strong>1835-1842</strong>), publication en <strong>4 volumes</strong>. <strong>Tournées de récitations</strong> en France, célébré par <strong>Sainte-Beuve</strong> et <strong>Lamartine</strong>. <strong>Précurseur du Félibrige</strong> fondé par <strong>Frédéric Mistral</strong> en 1854."),
            ("🏘️", "Village d'Auteuil", "Le quartier d'<strong>Auteuil</strong>, ancien <strong>village rattaché à Paris en 1860</strong>, conserve une <strong>atmosphère résidentielle chic</strong>. De nombreux <strong>artistes et écrivains</strong> y ont vécu : <strong>Marcel Proust</strong>, <strong>Léon Daudet</strong>, <strong>Léon Bloy</strong>. <strong>Église Notre-Dame d'Auteuil</strong> (1880), <strong>Villa Montmorency</strong>.")
        ],
        "itin": [
            ("Musée Marmottan Monet", "la-muette", "M9", "M9 directe (2 stations)", 5),
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (~5 min)", 5),
            ("Ranelagh", "ranelagh", "M9", "M9 directe (1 station)", 2),
            ("Michel-Ange - Auteuil", "michel-ange-auteuil", "M9", "M9 directe (1 station)", 2),
            ("République", "republique", "M9", "M9 directe (~20 min)", 20),
            ("Roland-Garros", "porte-d-auteuil", "M9 + M10", "M9 → Michel-Ange + M10", 10)
        ]
    },
    "ranelagh": {
        "addr": "Avenue Mozart, 75016 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Ranelagh (M9) avenue Mozart dans le 16e. Jardin du Ranelagh et Musée Marmottan-Monet (plus grande collection Claude Monet au monde).",
        "tagline": "M9 — Jardin du Ranelagh, Musée Marmottan-Monet",
        "hero_desc": "Station <strong>Ranelagh</strong> sur l'<strong>avenue Mozart</strong> dans le <strong>16e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>8 novembre 1922</strong>. À proximité : le <strong>Jardin du Ranelagh</strong> et le <strong>Musée Marmottan-Monet</strong> (<strong>plus grande collection Claude Monet au monde</strong>).",
        "intros": [
            "La station <strong>Ranelagh</strong> est implantée sur l'<strong>avenue Mozart</strong> dans le <strong>16e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Jasmin</strong> (1 station) et <strong>La Muette</strong> (1 station). Bus 22, 32, 52.",
            "Ouverte le <strong>8 novembre 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "À proximité : le <strong>Jardin du Ranelagh</strong> et le <strong>Musée Marmottan-Monet</strong>, qui abrite la <strong>plus grande collection au monde d'œuvres de Claude Monet</strong>, dont <em><strong>Impression, soleil levant</strong></em> (1872), <strong>œuvre fondatrice de l'impressionnisme</strong>."
        ],
        "hist_title": "1922 : Jardin du Ranelagh et impressionnisme",
        "hist": [
            "La station Ranelagh est <strong>inaugurée le 8 novembre 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "Le nom <strong>Ranelagh</strong> rappelle le <strong>Jardin du Ranelagh</strong>, créé en <strong>1747</strong> à l'imitation des <strong>jardins londoniens de Ranelagh</strong> (du nom du <strong>vicomte de Ranelagh</strong>, propriétaire). <strong>Lieu de bals et fêtes</strong> sous Louis XV et Louis XVI. Transformé en <strong>jardin public</strong> sous le Second Empire.",
            "Le <strong>Musée Marmottan-Monet</strong>, à proximité (2 rue Louis-Boilly), abrite la <strong>plus grande collection au monde d'œuvres de Claude Monet</strong>. <strong>Inauguré en 1934</strong>, légué à l'<strong>Académie des Beaux-Arts</strong> par <strong>Paul Marmottan</strong>. <strong>Don de Michel Monet</strong> (fils du peintre) en <strong>1966</strong> : 165 œuvres. <em><strong>Impression, soleil levant</strong></em> (1872) y est conservé."
        ],
        "faq": [
            ("Quelle ligne dessert Ranelagh ?", "Uniquement la <strong>M9</strong>. Bus 22, 32, 52."),
            ("Pour le Musée Marmottan-Monet ?", "<strong>~5 min à pied</strong>. Plus grande collection Monet au monde."),
            ("Pour le Jardin du Ranelagh ?", "<strong>~3 min à pied</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>8 novembre 1922</strong>."),
            ("Pour Trocadéro et Tour Eiffel ?", "<strong>M9 directe</strong> (~5 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Musée Marmottan-Monet</strong> à 5 min : plus grande collection Monet au monde.",
            "<strong>Jardin du Ranelagh</strong> à 3 min à pied.",
            "Pour <strong>Trocadéro et Tour Eiffel</strong> : <strong>M9 directe</strong>.",
            "Quartier résidentiel chic d'<strong>Auteuil-Passy</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎨", "Musée Marmottan-Monet et Impressionnisme", "Le <strong>Musée Marmottan-Monet</strong>, à 5 min à pied (2 rue Louis-Boilly), abrite la <strong>plus grande collection au monde d'œuvres de Claude Monet</strong>. <strong>Inauguré en 1934</strong>. <strong>Don de Michel Monet</strong> (fils du peintre) en <strong>1966</strong> : <strong>165 œuvres</strong>. <em><strong>Impression, soleil levant</strong></em> (1872), <strong>œuvre fondatrice de l'impressionnisme</strong> (donna son nom au mouvement), y est conservée. Aussi collection de la famille <strong>Marmottan</strong> (Premier Empire). <strong>Volé en 1985</strong>, retrouvé en 1990."),
            ("🌳", "Jardin du Ranelagh (1747)", "Le <strong>Jardin du Ranelagh</strong>, à 3 min à pied, est créé en <strong>1747</strong> à l'imitation des <strong>jardins londoniens de Ranelagh</strong>. Nom hérité du <strong>vicomte de Ranelagh</strong>. <strong>Lieu de bals et fêtes</strong> sous <strong>Louis XV et Louis XVI</strong>. Transformé en <strong>jardin public</strong> sous le <strong>Second Empire</strong>. Aujourd'hui parc paisible avec <strong>aire de jeux</strong> et <strong>marionnettes</strong>.")
        ],
        "itin": [
            ("Musée Marmottan-Monet", "ranelagh", "à pied", "5 min à pied", 5),
            ("Jardin du Ranelagh", "ranelagh", "à pied", "3 min à pied", 3),
            ("La Muette", "la-muette", "M9", "M9 directe (1 station)", 2),
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (~5 min)", 5),
            ("Champs-Élysées", "franklin-d-roosevelt", "M9", "M9 directe (~10 min)", 10),
            ("République", "republique", "M9", "M9 directe (~18 min)", 18)
        ]
    },
    "la-muette": {
        "addr": "Chaussée de la Muette, 75016 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station La Muette (M9) chaussée de la Muette dans le 16e. Ancien château de la Muette, parc et Musée Marmottan-Monet à proximité.",
        "tagline": "M9 — La Muette, ancien château royal",
        "hero_desc": "Station <strong>La Muette</strong> sur la <strong>chaussée de la Muette</strong> dans le <strong>16e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>8 novembre 1922</strong>. Nom rappelant l'<strong>ancien château de la Muette</strong>. À proximité du <strong>Musée Marmottan-Monet</strong>.",
        "intros": [
            "La station <strong>La Muette</strong> est implantée sur la <strong>chaussée de la Muette</strong> dans le <strong>16e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Ranelagh</strong> (1 station) et <strong>Rue de la Pompe</strong> (1 station). Bus 22, 32, 52, 63, 70.",
            "Ouverte le <strong>8 novembre 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "Le nom <strong>La Muette</strong> rappelle l'<strong>ancien château de la Muette</strong>, <strong>résidence royale</strong> de <strong>Charles IX à Louis XV</strong>. <strong>Détruit en 1920</strong>. À proximité : le <strong>parc de la Muette</strong> et le <strong>Musée Marmottan-Monet</strong>."
        ],
        "hist_title": "1922 : ancien château royal de la Muette",
        "hist": [
            "La station La Muette est <strong>inaugurée le 8 novembre 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "Le nom <strong>La Muette</strong> rappelle l'<strong>ancien château de la Muette</strong>, <strong>résidence royale</strong> et <strong>pavillon de chasse</strong> situé à la lisière du <strong>Bois de Boulogne</strong>. <strong>Charles IX</strong> y séjourna. <strong>Louis XV</strong> le fit reconstruire.",
            "<strong>Lieu du premier vol en montgolfière habité</strong> au monde le <strong>21 novembre 1783</strong> avec <strong>Pilâtre de Rozier</strong> et le <strong>marquis d'Arlandes</strong> en présence de <strong>Louis XVI</strong>. <strong>Détruit en 1920</strong>. Le <strong>Musée Marmottan-Monet</strong> est à proximité dans l'ancien parc."
        ],
        "faq": [
            ("Quelle ligne dessert La Muette ?", "Uniquement la <strong>M9</strong>. Bus 22, 32, 52, 63, 70."),
            ("Qu'est-ce que le château de la Muette ?", "<strong>Ancien château royal</strong>, <strong>résidence royale</strong> et <strong>pavillon de chasse</strong>. Charles IX, Louis XV. <strong>Détruit en 1920</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>8 novembre 1922</strong>."),
            ("Pour le Musée Marmottan-Monet ?", "<strong>~3 min à pied</strong>."),
            ("Pour Trocadéro ?", "<strong>M9 directe</strong> (~3 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Musée Marmottan-Monet</strong> à 3 min : plus grande collection Monet au monde.",
            "<strong>Jardin du Ranelagh</strong> à proximité.",
            "Pour <strong>Trocadéro et Tour Eiffel</strong> : <strong>M9 directe</strong>.",
            "Quartier résidentiel chic <strong>Auteuil-Passy</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("👑", "Château de la Muette, résidence royale", "L'<strong>ancien château de la Muette</strong> était une <strong>résidence royale</strong> et un <strong>pavillon de chasse</strong> situé à la lisière du <strong>Bois de Boulogne</strong>. <strong>Charles IX</strong> y séjourna. <strong>Louis XV</strong> le fit reconstruire. <strong>Lieu du premier vol en montgolfière habité au monde</strong> le <strong>21 novembre 1783</strong> avec <strong>Jean-François Pilâtre de Rozier</strong> et le <strong>marquis d'Arlandes</strong> en présence de <strong>Louis XVI</strong>, Marie-Antoinette et Benjamin Franklin. <strong>Détruit en 1920</strong>."),
            ("🎈", "Premier vol en montgolfière (21 novembre 1783)", "Le <strong>21 novembre 1783</strong>, dans le <strong>jardin du château de la Muette</strong>, <strong>Jean-François Pilâtre de Rozier</strong> et le <strong>marquis d'Arlandes</strong> effectuent le <strong>premier vol habité au monde en montgolfière</strong>. <strong>25 min</strong> de vol, <strong>~9 km</strong> parcourus jusqu'à la <strong>Butte-aux-Cailles</strong>. Démonstration des <strong>frères Montgolfier</strong> en présence de <strong>Louis XVI</strong>, <strong>Marie-Antoinette</strong> et <strong>Benjamin Franklin</strong>.")
        ],
        "itin": [
            ("Musée Marmottan-Monet", "la-muette", "à pied", "3 min à pied", 3),
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (~3 min)", 3),
            ("Jardin du Ranelagh", "ranelagh", "M9", "M9 directe (1 station)", 2),
            ("Rue de la Pompe", "rue-de-la-pompe", "M9", "M9 directe (1 station)", 2),
            ("Champs-Élysées", "franklin-d-roosevelt", "M9", "M9 directe (~8 min)", 8),
            ("République", "republique", "M9", "M9 directe (~16 min)", 16)
        ]
    },
    "rue-de-la-pompe": {
        "addr": "Rue de la Pompe, 75016 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Rue de la Pompe (M9) rue de la Pompe dans le 16e. Quartier Passy résidentiel chic. Nom évoquant l'ancienne pompe à eau.",
        "tagline": "M9 — rue de la Pompe, Passy chic",
        "hero_desc": "Station <strong>Rue de la Pompe</strong> sur la <strong>rue de la Pompe</strong> dans le <strong>16e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>27 mai 1922</strong>. Nom évoquant l'<strong>ancienne pompe à eau</strong> qui alimentait le <strong>château de la Muette</strong>.",
        "intros": [
            "La station <strong>Rue de la Pompe</strong> est implantée sur la <strong>rue de la Pompe</strong> dans le <strong>16e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>La Muette</strong> (1 station) et <strong>Trocadéro</strong> (1 station). Bus 52, 63, 70.",
            "Ouverte le <strong>27 mai 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "Le nom <strong>Rue de la Pompe</strong> rappelle l'<strong>ancienne pompe à eau</strong> qui alimentait le <strong>château de la Muette</strong> au XVIIIe siècle, pompant l'eau de la Seine. Quartier <strong>résidentiel chic</strong> du <strong>16e Passy</strong>."
        ],
        "hist_title": "1922 : pompe XVIIIe et Passy",
        "hist": [
            "La station Rue de la Pompe est <strong>inaugurée le 27 mai 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "Le nom <strong>Rue de la Pompe</strong> rappelle l'<strong>ancienne pompe à eau</strong> qui alimentait le <strong>château de la Muette</strong> au <strong>XVIIIe siècle</strong>. La pompe, située sur la rue, <strong>élevait l'eau de la Seine</strong> jusqu'au château. <strong>Disparue lors de l'urbanisation</strong> du quartier au XIXe siècle.",
            "Le quartier de <strong>Passy</strong>, ancien <strong>village rattaché à Paris en 1860</strong>, est aujourd'hui un <strong>quartier résidentiel chic</strong> du <strong>16e arrondissement</strong>. De nombreux <strong>artistes et écrivains</strong> y ont vécu : <strong>Honoré de Balzac</strong> (Maison de Balzac), <strong>Claude Debussy</strong>, <strong>Marcel Proust</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Rue de la Pompe ?", "Uniquement la <strong>M9</strong>. Bus 52, 63, 70."),
            ("D'où vient le nom Rue de la Pompe ?", "De l'<strong>ancienne pompe à eau</strong> qui alimentait le <strong>château de la Muette</strong> au XVIIIe siècle."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 mai 1922</strong>."),
            ("Pour Trocadéro et Tour Eiffel ?", "<strong>M9 directe</strong> (1 station)."),
            ("Pour Maison de Balzac ?", "<strong>M9 → Passy + à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier résidentiel chic de <strong>Passy</strong> (16e).",
            "Pour <strong>Trocadéro et Tour Eiffel</strong> : <strong>M9 directe</strong> (1 station).",
            "Pour <strong>Maison de Balzac</strong> : <strong>M9 → Passy + à pied</strong>.",
            "Pour <strong>Musée Marmottan-Monet</strong> : <strong>M9 → La Muette</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("💧", "Ancienne pompe à eau du château", "La <strong>rue de la Pompe</strong> doit son nom à une <strong>ancienne pompe à eau</strong> qui se trouvait sur la voie au <strong>XVIIIe siècle</strong>. Cette pompe <strong>élevait l'eau de la Seine</strong> pour alimenter le <strong>château de la Muette</strong>, résidence royale située à proximité. <strong>Système hydraulique</strong> typique des <strong>parcs et châteaux royaux</strong> de l'Ancien Régime. <strong>Disparue lors de l'urbanisation</strong> du quartier au XIXe siècle."),
            ("🏘️", "Quartier Passy chic et artistique", "Le quartier de <strong>Passy</strong>, autour de la station, est un <strong>quartier résidentiel chic</strong> du <strong>16e arrondissement</strong>. <strong>Ancien village rattaché à Paris en 1860</strong>. De nombreux <strong>artistes et écrivains</strong> y ont vécu : <strong>Honoré de Balzac</strong> (<strong>Maison de Balzac</strong> à proximité), <strong>Claude Debussy</strong>, <strong>Marcel Proust</strong>, <strong>Édouard Manet</strong>. <strong>Cimetière de Passy</strong> où reposent <strong>Édouard Manet</strong>, <strong>Berthe Morisot</strong>, <strong>Claude Debussy</strong>.")
        ],
        "itin": [
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (1 station)", 2),
            ("Maison de Balzac", "passy", "M9 + M6", "M9 → Trocadéro + M6 à Passy", 8),
            ("Musée Marmottan-Monet", "la-muette", "M9", "M9 directe (1 station)", 2),
            ("Champs-Élysées", "franklin-d-roosevelt", "M9", "M9 directe (~6 min)", 6),
            ("République", "republique", "M9", "M9 directe (~14 min)", 14),
            ("Mairie de Montreuil (terminus)", "mairie-de-montreuil", "M9", "M9 directe (~32 min)", 32)
        ]
    },
    "iena": {
        "addr": "Place d'Iéna, 75016 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Iéna (M9) place d'Iéna dans le 16e. Musée Guimet (Arts Asiatiques) à la sortie. Trocadéro et Tour Eiffel proches.",
        "tagline": "M9 — Musée Guimet, Arts Asiatiques",
        "hero_desc": "Station <strong>Iéna</strong> sur la <strong>place d'Iéna</strong> dans le <strong>16e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>27 mai 1922</strong>. À la sortie : le <strong>Musée national des arts asiatiques - Guimet</strong> (1889), l'un des <strong>plus importants musées d'arts asiatiques d'Europe</strong>.",
        "intros": [
            "La station <strong>Iéna</strong> est implantée sur la <strong>place d'Iéna</strong> dans le <strong>16e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Trocadéro</strong> (1 station) et <strong>Alma - Marceau</strong> (1 station). Bus 32, 63, 82.",
            "Ouverte le <strong>27 mai 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "Le nom <strong>Iéna</strong> rend hommage à la <strong>bataille d'Iéna</strong> (<strong>14 octobre 1806</strong>), <strong>victoire de Napoléon</strong> sur l'<strong>armée prussienne</strong>. À la sortie : le <strong>Musée national des arts asiatiques - Guimet</strong>, l'un des <strong>plus importants musées d'arts asiatiques d'Europe</strong>."
        ],
        "hist_title": "1922 : bataille d'Iéna et Musée Guimet",
        "hist": [
            "La station Iéna est <strong>inaugurée le 27 mai 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "Le nom <strong>Iéna</strong> rend hommage à la <strong>bataille d'Iéna</strong> (<strong>14 octobre 1806</strong>), <strong>victoire décisive de Napoléon</strong> sur l'<strong>armée prussienne</strong>. La <strong>bataille d'Auerstaedt</strong>, simultanée, complète la victoire. <strong>Effondrement de la Prusse</strong>. <strong>Traité de Tilsit</strong> (1807).",
            "Le <strong>Musée national des arts asiatiques - Guimet</strong>, à la sortie, est l'un des <strong>plus importants musées d'arts asiatiques d'Europe</strong>. <strong>Fondé en 1879 à Lyon</strong> par <strong>Émile Guimet</strong>. <strong>Installé à Paris en 1889</strong> place d'Iéna. <strong>Plus de 60 000 œuvres</strong> : Inde, Asie du Sud-Est, Chine, Japon, Corée, Tibet, Afghanistan. <strong>Bouddhas, statues, peintures, céramiques, textiles</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Iéna ?", "Uniquement la <strong>M9</strong>. Bus 32, 63, 82."),
            ("Pour le Musée Guimet ?", "<strong>Sortie directe</strong>. ~60 000 œuvres d'arts asiatiques."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 mai 1922</strong>."),
            ("Qu'est-ce que la bataille d'Iéna ?", "<strong>Victoire de Napoléon</strong> sur l'armée prussienne, <strong>14 octobre 1806</strong>."),
            ("Pour Trocadéro et Tour Eiffel ?", "<strong>M9 directe</strong> (1 station, ~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Musée Guimet</strong> à la sortie : un des plus grands musées d'arts asiatiques d'Europe.",
            "Pour <strong>Trocadéro et Tour Eiffel</strong> : <strong>M9 directe</strong>.",
            "Pour <strong>Palais de Tokyo</strong> et <strong>Musée d'Art Moderne</strong> : <strong>M9 → Alma-Marceau</strong>.",
            "Pour <strong>Champs-Élysées</strong> : <strong>M9 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Musée Guimet (1889)", "Le <strong>Musée national des arts asiatiques - Guimet</strong>, à la sortie de la station, est <strong>fondé en 1879 à Lyon</strong> par <strong>Émile Guimet</strong> (1836-1918), <strong>industriel et orientaliste</strong>. <strong>Installé à Paris</strong> en <strong>1889</strong> place d'Iéna. <strong>Plus de 60 000 œuvres</strong> couvrant l'<strong>Asie</strong> : Inde, Asie du Sud-Est, Chine, Japon, Corée, Tibet, Afghanistan, Pakistan. <strong>Bouddhas, statues, peintures, céramiques, textiles, manuscrits</strong>. <strong>L'un des plus importants musées d'arts asiatiques au monde</strong>."),
            ("⚔️", "Bataille d'Iéna (14 octobre 1806)", "La <strong>bataille d'Iéna</strong>, le <strong>14 octobre 1806</strong>, est une <strong>victoire décisive de Napoléon Ier</strong> sur l'<strong>armée prussienne</strong>. La <strong>bataille d'Auerstaedt</strong>, simultanée (à 25 km), complète la victoire. <strong>Effondrement de la Prusse</strong>. La <strong>Grande Armée</strong> entre à <strong>Berlin</strong> le 27 octobre 1806. <strong>Décret de Berlin</strong> (21 novembre) instaurant le <strong>blocus continental</strong> contre l'Angleterre. <strong>Traité de Tilsit</strong> (juillet 1807) consacre la domination napoléonienne en Europe.")
        ],
        "itin": [
            ("Musée Guimet", "iena", "à pied", "Sortie directe", 2),
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (1 station)", 3),
            ("Palais de Tokyo (Art Moderne)", "alma-marceau", "M9", "M9 directe (1 station)", 3),
            ("Champs-Élysées", "franklin-d-roosevelt", "M9", "M9 directe (~5 min)", 5),
            ("République", "republique", "M9", "M9 directe (~14 min)", 14),
            ("Bastille", "bastille", "M9 + M1", "M9 → République + M1 ou via Franklin", 18)
        ]
    },
    "alma-marceau": {
        "addr": "Avenue du Président-Wilson, 75008 Paris", "arr": "8e arrondissement (Paris)",
        "seo": "Station Alma - Marceau (M9) avenue du Président-Wilson dans le 8e. Pont de l'Alma, Place de l'Alma, Flame of Liberty (mémorial Lady Diana).",
        "tagline": "M9 — Alma, Pont de l'Alma, mémorial Lady Diana",
        "hero_desc": "Station <strong>Alma - Marceau</strong> sur l'<strong>avenue du Président-Wilson</strong> dans le <strong>8e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>27 mai 1922</strong>. À proximité du <strong>Pont de l'Alma</strong>, de la <strong>Place de l'Alma</strong> et de la <strong>Flame of Liberty</strong> (mémorial informel à <strong>Lady Diana</strong>).",
        "intros": [
            "La station <strong>Alma - Marceau</strong> est implantée sur l'<strong>avenue du Président-Wilson</strong> dans le <strong>8e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Iéna</strong> (1 station) et <strong>Franklin D. Roosevelt</strong> (1 station). Bus 42, 63, 72, 80, 92.",
            "Ouverte le <strong>27 mai 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "Le nom <strong>Alma</strong> rend hommage à la <strong>bataille de l'Alma</strong> (<strong>20 septembre 1854</strong>), <strong>victoire alliée</strong> pendant la <strong>guerre de Crimée</strong>. <strong>Marceau</strong> rend hommage au <strong>général François Séverin Marceau-Desgraviers</strong> (<strong>1769-1796</strong>). À proximité : le <strong>Pont de l'Alma</strong> et la <strong>Flame of Liberty</strong>."
        ],
        "hist_title": "1922 : Alma 1854 et Flame of Liberty 1989",
        "hist": [
            "La station Alma - Marceau est <strong>inaugurée le 27 mai 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "Le nom <strong>Alma</strong> rend hommage à la <strong>bataille de l'Alma</strong> (<strong>20 septembre 1854</strong>), <strong>victoire des alliés franco-britanniques-ottomans</strong> sur l'<strong>armée russe</strong> pendant la <strong>guerre de Crimée</strong>. <strong>Marceau</strong> rend hommage au <strong>général François Séverin Marceau-Desgraviers</strong> (<strong>1769-1796</strong>), <strong>héros de la Révolution française</strong>.",
            "À proximité : le <strong>Pont de l'Alma</strong>, célèbre pour son <strong>zouave</strong> dont la position par rapport à la Seine sert d'indicateur des crues. La <strong>Flame of Liberty</strong> (<strong>1989</strong>), réplique de la torche de la <strong>Statue de la Liberté</strong>, offerte par l'<strong>International Herald Tribune</strong> en hommage à l'amitié franco-américaine, est devenue le <strong>mémorial informel de Lady Diana</strong> après son <strong>accident mortel</strong> dans le tunnel sous le pont le <strong>31 août 1997</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Alma - Marceau ?", "Uniquement la <strong>M9</strong>. Bus 42, 63, 72, 80, 92."),
            ("Pour le Pont de l'Alma ?", "<strong>~3 min à pied</strong>."),
            ("Pour la Flame of Liberty / Mémorial Lady Diana ?", "<strong>Sortie directe</strong>. Place de l'Alma."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 mai 1922</strong>."),
            ("Pour le Palais de Tokyo ?", "<strong>~5 min à pied</strong> via avenue du Président-Wilson."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Flame of Liberty</strong> à la sortie : mémorial informel de Lady Diana.",
            "<strong>Pont de l'Alma</strong> à 3 min : célèbre zouave indicateur des crues.",
            "<strong>Palais de Tokyo</strong> et <strong>Musée d'Art Moderne</strong> à 5 min à pied.",
            "<strong>Théâtre des Champs-Élysées</strong> (1913, Auguste Perret) à 5 min.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🔥", "Flame of Liberty et Lady Diana", "La <strong>Flame of Liberty</strong>, à la sortie de la station, est une <strong>réplique en taille réelle de la flamme</strong> de la <strong>Statue de la Liberté</strong> de New York. <strong>Inaugurée en 1989</strong>, offerte par l'<strong>International Herald Tribune</strong> en hommage à l'amitié franco-américaine. Elle est devenue le <strong>mémorial informel de Diana, princesse de Galles</strong>, après son <strong>accident mortel</strong> dans le <strong>tunnel sous le pont de l'Alma</strong> le <strong>31 août 1997</strong>. <strong>Fleurs, messages et photos</strong> y sont régulièrement déposés."),
            ("🌊", "Zouave du Pont de l'Alma, indicateur des crues", "Le <strong>Pont de l'Alma</strong>, à 3 min à pied, est célèbre pour sa <strong>statue de zouave</strong> sculptée par <strong>Georges Diébolt</strong> en <strong>1856</strong>. La <strong>position de l'eau de la Seine par rapport au zouave</strong> sert d'<strong>indicateur populaire des crues</strong>. <strong>Aux pieds</strong> : Seine basse. <strong>Aux genoux</strong> : crue moyenne. <strong>À la taille</strong> : crue importante (1995, 2018). <strong>Aux épaules</strong> : crue exceptionnelle (1910).")
        ],
        "itin": [
            ("Flame of Liberty / Mémorial Diana", "alma-marceau", "à pied", "Sortie directe", 1),
            ("Pont de l'Alma", "alma-marceau", "à pied", "3 min à pied", 3),
            ("Palais de Tokyo / Musée Art Moderne", "iena", "M9 + à pied", "Avenue Président-Wilson (5 min)", 5),
            ("Théâtre des Champs-Élysées", "alma-marceau", "à pied", "5 min à pied", 5),
            ("Champs-Élysées", "franklin-d-roosevelt", "M9", "M9 directe (1 station)", 2),
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (2 stations)", 4)
        ]
    },
    "saint-philippe-du-roule": {
        "addr": "Rue du Faubourg-Saint-Honoré, 75008 Paris", "arr": "8e arrondissement (Paris)",
        "seo": "Station Saint-Philippe-du-Roule (M9) rue du Faubourg-Saint-Honoré dans le 8e. Église Saint-Philippe-du-Roule (1784, Chalgrin).",
        "tagline": "M9 — église Saint-Philippe-du-Roule (1784)",
        "hero_desc": "Station <strong>Saint-Philippe-du-Roule</strong> sur la <strong>rue du Faubourg-Saint-Honoré</strong> dans le <strong>8e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>27 mai 1922</strong>. À la sortie : l'<strong>église Saint-Philippe-du-Roule</strong> (<strong>1784</strong>, architecte <strong>Jean-François Chalgrin</strong>).",
        "intros": [
            "La station <strong>Saint-Philippe-du-Roule</strong> est implantée sur la <strong>rue du Faubourg-Saint-Honoré</strong> dans le <strong>8e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Franklin D. Roosevelt</strong> (1 station) et <strong>Miromesnil</strong> (1 station). Bus 22, 28, 43, 52, 80, 84, 93.",
            "Ouverte le <strong>27 mai 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "À la sortie : l'<strong>église Saint-Philippe-du-Roule</strong>, <strong>édifice néo-classique</strong> construit de <strong>1774 à 1784</strong> par <strong>Jean-François Chalgrin</strong>, architecte de l'<strong>Arc de Triomphe</strong>."
        ],
        "hist_title": "1922 : église Saint-Philippe-du-Roule (1784)",
        "hist": [
            "La station Saint-Philippe-du-Roule est <strong>inaugurée le 27 mai 1922</strong> avec le tronçon initial de la <strong>M9</strong>.",
            "L'<strong>église Saint-Philippe-du-Roule</strong>, à la sortie, est un <strong>édifice religieux néo-classique</strong> construit de <strong>1774 à 1784</strong> par l'architecte <strong>Jean-François Chalgrin</strong> (<strong>1739-1811</strong>). Style <strong>basilical antique</strong> avec <strong>portique à colonnade ionique</strong>.",
            "<strong>Chalgrin</strong> est célèbre pour avoir conçu l'<strong>Arc de Triomphe de l'Étoile</strong> (1806). <strong>Inscrite aux monuments historiques en 1976</strong>. Le quartier autour de la station fait partie du <strong>Faubourg Saint-Honoré</strong>, axe historique des <strong>boutiques de luxe</strong> (<strong>palais de l'Élysée</strong>, ambassades, maisons de mode)."
        ],
        "faq": [
            ("Quelle ligne dessert Saint-Philippe-du-Roule ?", "Uniquement la <strong>M9</strong>. Bus 22, 28, 43, 52, 80, 84, 93."),
            ("Qu'est-ce que l'église Saint-Philippe-du-Roule ?", "<strong>Édifice néo-classique</strong> construit de <strong>1774 à 1784</strong> par <strong>Jean-François Chalgrin</strong> (architecte de l'Arc de Triomphe)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 mai 1922</strong>."),
            ("Pour le Faubourg Saint-Honoré ?", "<strong>Sortie directe</strong>."),
            ("Pour les Champs-Élysées ?", "<strong>M9 directe</strong> (1 station, ~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Église Saint-Philippe-du-Roule</strong> à la sortie : néo-classique 1784 (Chalgrin).",
            "<strong>Faubourg Saint-Honoré</strong> : boutiques de luxe.",
            "<strong>Palais de l'Élysée</strong> à 5 min à pied (Présidence République).",
            "Pour <strong>Champs-Élysées</strong> : <strong>M9 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⛪", "Église Saint-Philippe-du-Roule (1774-1784)", "L'<strong>église Saint-Philippe-du-Roule</strong>, à la sortie, est un <strong>édifice religieux néo-classique</strong> construit de <strong>1774 à 1784</strong> par l'architecte <strong>Jean-François Chalgrin</strong> (<strong>1739-1811</strong>). Style <strong>basilical antique</strong>, inspiration des <strong>basiliques romaines paléochrétiennes</strong>. <strong>Portique à colonnade ionique</strong>, <strong>nef à colonnes</strong>. <strong>Inscrite aux monuments historiques en 1976</strong>. <strong>Chalgrin</strong> est également l'architecte de l'<strong>Arc de Triomphe de l'Étoile</strong> (1806)."),
            ("💎", "Faubourg Saint-Honoré, luxe parisien", "Le <strong>Faubourg Saint-Honoré</strong>, à la sortie de la station, est l'un des <strong>axes historiques du luxe parisien</strong>. <strong>Boutiques de mode et joaillerie</strong> (Hermès, Chanel, Boucheron, Cartier), <strong>palais de l'Élysée</strong> (Présidence de la République depuis 1873), <strong>nombreuses ambassades</strong>, <strong>hôtels particuliers</strong>. <strong>Axe royal</strong> historique entre <strong>Louvre et Versailles</strong>.")
        ],
        "itin": [
            ("Église Saint-Philippe-du-Roule", "saint-philippe-du-roule", "à pied", "Sortie directe", 1),
            ("Faubourg Saint-Honoré (luxe)", "saint-philippe-du-roule", "à pied", "Sortie directe", 2),
            ("Palais de l'Élysée", "miromesnil", "à pied", "5 min à pied", 5),
            ("Champs-Élysées", "franklin-d-roosevelt", "M9", "M9 directe (1 station)", 2),
            ("Madeleine", "madeleine", "M9 + M8", "M9 → Miromesnil + M8", 6),
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (~6 min)", 6)
        ]
    },
    "saint-augustin": {
        "addr": "Boulevard Haussmann, 75008 Paris", "arr": "8e arrondissement (Paris)",
        "seo": "Station Saint-Augustin (M9) boulevard Haussmann dans le 8e. Église Saint-Augustin (1860-1871, Baltard), édifice éclectique du Second Empire.",
        "tagline": "M9 — église Saint-Augustin (Baltard, 1871)",
        "hero_desc": "Station <strong>Saint-Augustin</strong> sur le <strong>boulevard Haussmann</strong> dans le <strong>8e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>27 mai 1923</strong>. À la sortie : l'<strong>église Saint-Augustin</strong> (<strong>1860-1871</strong>, <strong>Victor Baltard</strong>), <strong>édifice éclectique du Second Empire</strong>.",
        "intros": [
            "La station <strong>Saint-Augustin</strong> est implantée sur le <strong>boulevard Haussmann</strong> dans le <strong>8e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Miromesnil</strong> (1 station) et <strong>Havre - Caumartin</strong> (1 station). Bus 22, 28, 32, 43, 84, 93, 94.",
            "Ouverte le <strong>27 mai 1923</strong>.",
            "À la sortie : l'<strong>église Saint-Augustin</strong>, <strong>édifice éclectique du Second Empire</strong> construit de <strong>1860 à 1871</strong> par <strong>Victor Baltard</strong>. <strong>Architecture mêlant néo-Renaissance et néo-byzantin</strong>. <strong>Dôme spectaculaire</strong>."
        ],
        "hist_title": "1923 : église Baltard (1871)",
        "hist": [
            "La station Saint-Augustin est <strong>inaugurée le 27 mai 1923</strong>.",
            "L'<strong>église Saint-Augustin</strong>, à la sortie, est un <strong>édifice religieux éclectique</strong> construit de <strong>1860 à 1871</strong> par <strong>Victor Baltard</strong> (<strong>1805-1874</strong>), <strong>architecte du Second Empire</strong>. <strong>Style néo-Renaissance et néo-byzantin</strong>.",
            "<strong>Architecture innovante</strong> avec <strong>charpente métallique</strong> dissimulée derrière les <strong>pierres de taille</strong>. <strong>Dôme central</strong> spectaculaire. <strong>Baltard</strong> est également célèbre pour les <strong>Halles centrales de Paris</strong> (1854-1874, détruites en 1971). <strong>Inscrite aux monuments historiques en 1979</strong>. Sur le boulevard Haussmann."
        ],
        "faq": [
            ("Quelle ligne dessert Saint-Augustin ?", "Uniquement la <strong>M9</strong>. Bus 22, 28, 32, 43, 84, 93, 94."),
            ("Qu'est-ce que l'église Saint-Augustin ?", "<strong>Édifice éclectique du Second Empire</strong> construit de <strong>1860 à 1871</strong> par <strong>Victor Baltard</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 mai 1923</strong>."),
            ("Pour le boulevard Haussmann ?", "<strong>Sortie directe</strong>."),
            ("Pour Saint-Lazare ?", "<strong>~5 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Église Saint-Augustin</strong> à la sortie : édifice Baltard éclectique 1871.",
            "<strong>Boulevard Haussmann</strong> : axe haussmannien.",
            "Pour <strong>Galeries Lafayette</strong> : <strong>M9 directe</strong> (2 stations).",
            "Pour <strong>Gare Saint-Lazare</strong> : ~5 min à pied.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⛪", "Église Saint-Augustin (1860-1871, Baltard)", "L'<strong>église Saint-Augustin</strong>, à la sortie, est un <strong>édifice religieux éclectique</strong> construit de <strong>1860 à 1871</strong> par <strong>Victor Baltard</strong> (<strong>1805-1874</strong>), <strong>architecte du Second Empire</strong>. <strong>Style néo-Renaissance et néo-byzantin</strong> mêlés. <strong>Architecture innovante</strong> avec <strong>charpente métallique</strong> dissimulée derrière les <strong>pierres de taille</strong>. <strong>Dôme central spectaculaire</strong>. <strong>Inscrite aux monuments historiques en 1979</strong>. <strong>Baltard</strong> est également célèbre pour les <strong>Halles centrales de Paris</strong> (1854-1874, démolies en 1971)."),
            ("🏛️", "Boulevard Haussmann et Second Empire", "Le <strong>boulevard Haussmann</strong>, à la sortie de la station, est l'un des <strong>axes emblématiques du Paris haussmannien</strong>. <strong>Tracé sous Napoléon III</strong> entre <strong>1857 et 1927</strong> par le <strong>baron Haussmann</strong>. <strong>Longueur 2,5 km</strong>. Bordé de <strong>grands magasins</strong> (Galeries Lafayette, Printemps Haussmann), d'<strong>immeubles haussmanniens</strong> caractéristiques (façades en pierre de taille, balcons filants).")
        ],
        "itin": [
            ("Église Saint-Augustin", "saint-augustin", "à pied", "Sortie directe", 1),
            ("Galeries Lafayette", "chaussee-d-antin-la-fayette", "M9", "M9 directe (2 stations)", 4),
            ("Gare Saint-Lazare", "saint-lazare", "à pied", "5 min à pied", 5),
            ("Madeleine", "madeleine", "M9 + M8", "M9 → Havre-Caumartin + à pied", 6),
            ("Opéra Garnier", "opera", "M9 + M8", "M9 → Chaussée d'Antin + à pied", 8),
            ("Champs-Élysées", "franklin-d-roosevelt", "M9", "M9 directe (~6 min)", 6)
        ]
    },
    "saint-ambroise": {
        "addr": "Boulevard Voltaire, 75011 Paris", "arr": "11e arrondissement (Paris)",
        "seo": "Station Saint-Ambroise (M9) boulevard Voltaire dans le 11e. Église Saint-Ambroise (1869, Théodore Ballu), édifice néo-Renaissance.",
        "tagline": "M9 — église Saint-Ambroise (Ballu, 1869)",
        "hero_desc": "Station <strong>Saint-Ambroise</strong> sur le <strong>boulevard Voltaire</strong> dans le <strong>11e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>10 décembre 1933</strong>. À la sortie : l'<strong>église Saint-Ambroise</strong> (<strong>1869</strong>, <strong>Théodore Ballu</strong>), <strong>édifice néo-Renaissance</strong>.",
        "intros": [
            "La station <strong>Saint-Ambroise</strong> est implantée sur le <strong>boulevard Voltaire</strong> dans le <strong>11e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Oberkampf</strong> (1 station) et <strong>Voltaire</strong> (1 station). Bus 56, 61, 76, 96.",
            "Ouverte le <strong>10 décembre 1933</strong> avec le <strong>prolongement de la M9</strong>.",
            "À la sortie : l'<strong>église Saint-Ambroise</strong>, <strong>édifice religieux néo-Renaissance</strong> construit de <strong>1863 à 1869</strong> par l'architecte <strong>Théodore Ballu</strong> (1817-1885), également auteur de l'<strong>église de la Sainte-Trinité</strong> (Trinité M12)."
        ],
        "hist_title": "1933 : église néo-Renaissance Ballu",
        "hist": [
            "La station Saint-Ambroise est <strong>inaugurée le 10 décembre 1933</strong> avec le <strong>prolongement de la M9</strong>.",
            "L'<strong>église Saint-Ambroise</strong>, à la sortie, est un <strong>édifice religieux néo-Renaissance</strong> construit de <strong>1863 à 1869</strong> par l'architecte <strong>Théodore Ballu</strong> (<strong>1817-1885</strong>). <strong>Façade à clocher-porche</strong> avec <strong>deux flèches</strong>. <strong>Inscrite aux monuments historiques en 1984</strong>.",
            "<strong>Théodore Ballu</strong> est également l'architecte de l'<strong>église de la Sainte-Trinité</strong> (1867, M12) et de l'<strong>Hôtel de Ville de Paris</strong> (reconstruit après l'incendie de la Commune 1871). Le quartier autour de la station fait partie du <strong>11e arrondissement</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Saint-Ambroise ?", "Uniquement la <strong>M9</strong>. Bus 56, 61, 76, 96."),
            ("Qu'est-ce que l'église Saint-Ambroise ?", "<strong>Édifice néo-Renaissance</strong> construit de <strong>1863 à 1869</strong> par <strong>Théodore Ballu</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>10 décembre 1933</strong>."),
            ("Pour République ?", "<strong>M9 directe</strong> (2 stations)."),
            ("Pour Bastille ?", "<strong>M9 + M5</strong> via Oberkampf ou Voltaire."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Église Saint-Ambroise</strong> à la sortie : édifice Ballu néo-Renaissance 1869.",
            "<strong>Boulevard Voltaire</strong> : axe haussmannien.",
            "Pour <strong>République</strong> : <strong>M9 directe</strong>.",
            "Pour <strong>Bastille</strong> : <strong>M9 + M5</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⛪", "Église Saint-Ambroise (1863-1869, Ballu)", "L'<strong>église Saint-Ambroise</strong>, à la sortie, est un <strong>édifice religieux néo-Renaissance</strong> construit de <strong>1863 à 1869</strong> par l'architecte <strong>Théodore Ballu</strong> (<strong>1817-1885</strong>). <strong>Façade à clocher-porche</strong> avec <strong>deux flèches</strong>. <strong>Inscrite aux monuments historiques en 1984</strong>. <strong>Ballu</strong> est également l'architecte de l'<strong>église de la Sainte-Trinité</strong> (1867, M12) et de l'<strong>Hôtel de Ville de Paris</strong> (reconstruit après l'incendie de la Commune 1871)."),
            ("🏛️", "11e arrondissement contrastes", "Le <strong>11e arrondissement</strong> (~150 000 habitants) est historiquement un <strong>quartier populaire et ouvrier</strong>. <strong>Faubourg Saint-Antoine</strong> traditionnellement <strong>quartier des artisans du meuble</strong>. À partir des années 1990, <strong>gentrification</strong> avec installation de <strong>bars, restaurants tendance</strong> autour des rues <strong>Oberkampf, Jean-Pierre Timbaud, Saint-Maur</strong>.")
        ],
        "itin": [
            ("Église Saint-Ambroise", "saint-ambroise", "à pied", "Sortie directe", 1),
            ("République", "republique", "M9", "M9 directe (2 stations)", 4),
            ("Oberkampf (vie nocturne)", "oberkampf", "M9", "M9 directe (1 station)", 2),
            ("Bastille", "bastille", "M9 + M5", "M9 → Oberkampf + M5", 8),
            ("Voltaire", "voltaire", "M9", "M9 directe (1 station)", 2),
            ("Champs-Élysées", "franklin-d-roosevelt", "M9", "M9 directe (~16 min)", 16)
        ]
    },
    "voltaire": {
        "addr": "Boulevard Voltaire, 75011 Paris", "arr": "11e arrondissement (Paris)",
        "seo": "Station Voltaire (M9) boulevard Voltaire dans le 11e. Hommage à Voltaire (1694-1778), philosophe et écrivain français des Lumières.",
        "tagline": "M9 — Voltaire, philosophe des Lumières",
        "hero_desc": "Station <strong>Voltaire</strong> sur le <strong>boulevard Voltaire</strong> dans le <strong>11e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>10 décembre 1933</strong>. Hommage à <strong>François-Marie Arouet dit Voltaire</strong> (<strong>1694-1778</strong>), <strong>écrivain et philosophe français des Lumières</strong>.",
        "intros": [
            "La station <strong>Voltaire</strong> est implantée sur le <strong>boulevard Voltaire</strong> dans le <strong>11e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Saint-Ambroise</strong> (1 station) et <strong>Charonne</strong> (1 station). Bus 46, 56, 61, 76, 96.",
            "Ouverte le <strong>10 décembre 1933</strong> avec le <strong>prolongement de la M9</strong>.",
            "Le nom <strong>Voltaire</strong> rend hommage à <strong>François-Marie Arouet dit Voltaire</strong> (<strong>1694-1778</strong>), <strong>écrivain, philosophe et historien français</strong> des <strong>Lumières</strong>. <strong>Membre de l'Académie française</strong> (1746). Inhumé au <strong>Panthéon</strong> en <strong>1791</strong>."
        ],
        "hist_title": "1933 : Voltaire, philosophe des Lumières",
        "hist": [
            "La station Voltaire est <strong>inaugurée le 10 décembre 1933</strong> avec le <strong>prolongement de la M9</strong>.",
            "Le nom <strong>Voltaire</strong> rend hommage à <strong>François-Marie Arouet dit Voltaire</strong> (<strong>21 novembre 1694 - 30 mai 1778</strong>), <strong>écrivain, philosophe, historien et homme d'esprit français</strong>. <strong>Figure majeure des Lumières</strong>.",
            "<strong>Membre de l'Académie française</strong> en <strong>1746</strong>. Œuvres : <em>Lettres philosophiques</em> (1734), <em>Candide</em> (1759), <em>Dictionnaire philosophique</em> (1764). <strong>Engagement contre le fanatisme</strong> et l'<strong>intolérance religieuse</strong> (affaire Calas, 1762). <strong>Inhumé au Panthéon</strong> le <strong>11 juillet 1791</strong>, lors de la Révolution française."
        ],
        "faq": [
            ("Quelle ligne dessert Voltaire ?", "Uniquement la <strong>M9</strong>. Bus 46, 56, 61, 76, 96."),
            ("Qui est Voltaire ?", "<strong>François-Marie Arouet dit Voltaire</strong> (1694-1778), <strong>écrivain, philosophe et historien français des Lumières</strong>. Auteur de <em>Candide</em> (1759)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>10 décembre 1933</strong>."),
            ("Pour Nation ?", "<strong>M9 directe</strong> (3 stations)."),
            ("Pour République ?", "<strong>M9 directe</strong> (3 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Boulevard Voltaire</strong> : axe haussmannien tracé en 1862.",
            "Pour <strong>Bastille</strong> : <strong>M9 + M5</strong> via Oberkampf.",
            "Pour <strong>Nation</strong> : <strong>M9 directe</strong> (3 stations).",
            "Quartier <strong>11e</strong> en gentrification : bars, restaurants.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("📚", "Voltaire, figure majeure des Lumières", "<strong>François-Marie Arouet dit Voltaire</strong> (1694-1778), <strong>écrivain, philosophe, historien et homme d'esprit français</strong>. <strong>Figure majeure des Lumières</strong>. <strong>Académicien</strong> (1746). Œuvres : <em>Lettres philosophiques</em> (1734), <em>Candide</em> (1759), <em>Dictionnaire philosophique</em> (1764), <em>Zadig</em> (1747). <strong>Engagement contre le fanatisme</strong> et l'<strong>intolérance religieuse</strong> : <strong>affaire Calas</strong> (1762, fait reconnaître innocence d'un protestant exécuté), <strong>affaire Sirven</strong>, <strong>affaire La Barre</strong>. <strong>Inhumé au Panthéon</strong> le <strong>11 juillet 1791</strong> lors de la Révolution française."),
            ("🏛️", "Boulevard Voltaire (1862)", "Le <strong>boulevard Voltaire</strong>, tracé sous le <strong>Second Empire</strong>, est l'un des <strong>grands axes haussmanniens</strong> du nord-est parisien. <strong>Long de 2,6 km</strong>, il relie la <strong>place de la République</strong> à la <strong>place de la Nation</strong>. <strong>Tracé en 1862</strong> sous Napoléon III. <strong>Renommé Voltaire</strong> en 1879. Bordé d'<strong>immeubles haussmanniens</strong>.")
        ],
        "itin": [
            ("République", "republique", "M9", "M9 directe (3 stations)", 6),
            ("Nation", "nation", "M9", "M9 directe (3 stations)", 6),
            ("Bastille", "bastille", "M9 + M5", "M9 → Oberkampf + M5", 8),
            ("Père Lachaise", "pere-lachaise", "M9 + M2", "M9 → Nation + M2", 10),
            ("Champs-Élysées", "franklin-d-roosevelt", "M9", "M9 directe (~14 min)", 14),
            ("Mairie de Montreuil (terminus)", "mairie-de-montreuil", "M9", "M9 directe (~20 min)", 20)
        ]
    },
    "charonne": {
        "addr": "Boulevard Voltaire, 75011 Paris", "arr": "11e arrondissement (Paris)",
        "seo": "Station Charonne (M9) boulevard Voltaire dans le 11e. Quartier Charonne, ancien village rattaché à Paris en 1860.",
        "tagline": "M9 — Charonne, ancien village",
        "hero_desc": "Station <strong>Charonne</strong> sur le <strong>boulevard Voltaire</strong> dans le <strong>11e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>10 décembre 1933</strong>. Ancien <strong>village de Charonne</strong>, rattaché à Paris en <strong>1860</strong>.",
        "intros": [
            "La station <strong>Charonne</strong> est implantée sur le <strong>boulevard Voltaire</strong> dans le <strong>11e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Voltaire</strong> (1 station) et <strong>Rue des Boulets</strong> (1 station). Bus 46, 61, 76.",
            "Ouverte le <strong>10 décembre 1933</strong>.",
            "Le nom <strong>Charonne</strong> rappelle l'<strong>ancien village de Charonne</strong>, <strong>rattaché à Paris en 1860</strong>. <strong>Étymologie</strong> : du latin <em>Karonna</em> (lieu-dit gallo-romain)."
        ],
        "hist_title": "1933 : Charonne, ancien village",
        "hist": [
            "La station Charonne est <strong>inaugurée le 10 décembre 1933</strong>.",
            "Le nom <strong>Charonne</strong> rappelle l'<strong>ancien village de Charonne</strong>, <strong>rattaché à Paris en 1860</strong> avec d'autres communes périphériques. <strong>Étymologie</strong> : du latin <em>Karonna</em>.",
            "Au <strong>XIXe siècle</strong>, <strong>quartier populaire et ouvrier</strong>. Aujourd'hui <strong>quartier en gentrification</strong>. <strong>Rue de Charonne</strong> à proximité, axe commerçant historique. <strong>Église Saint-Germain-de-Charonne</strong> (XIIIe-XVe siècles), <strong>l'une des plus anciennes églises de Paris</strong>, à courte distance."
        ],
        "faq": [
            ("Quelle ligne dessert Charonne ?", "Uniquement la <strong>M9</strong>. Bus 46, 61, 76."),
            ("Quand a-t-elle ouvert ?", "Le <strong>10 décembre 1933</strong>."),
            ("Qu'est-ce que Charonne ?", "<strong>Ancien village</strong> rattaché à Paris en <strong>1860</strong>, aujourd'hui quartier populaire du 11e/20e."),
            ("Pour l'église Saint-Germain-de-Charonne ?", "<strong>~10 min à pied</strong>."),
            ("Pour Nation ?", "<strong>M9 directe</strong> (2 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Église Saint-Germain-de-Charonne</strong> (XIIIe-XVe) à 10 min : l'une des plus anciennes de Paris.",
            "<strong>Rue de Charonne</strong> : axe commerçant historique.",
            "Pour <strong>Nation</strong> : <strong>M9 directe</strong> (2 stations).",
            "Pour <strong>Père Lachaise</strong> : <strong>M9 + M2</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⛪", "Église Saint-Germain-de-Charonne", "L'<strong>église Saint-Germain-de-Charonne</strong>, à 10 min à pied, est <strong>l'une des plus anciennes églises de Paris</strong>. <strong>XIIIe-XVe siècles</strong>. <strong>Style gothique</strong>. Située dans le <strong>20e arrondissement</strong>. <strong>Cimetière de Charonne</strong> attenant, l'<strong>un des deux derniers cimetières paroissiaux de Paris</strong> (avec celui du Calvaire à Montmartre). <strong>Inscrite aux monuments historiques</strong>."),
            ("🏘️", "Village de Charonne", "Le <strong>village de Charonne</strong>, ancien village rattaché à Paris en <strong>1860</strong>. <strong>Étymologie</strong> : du latin <em>Karonna</em>. Quartier <strong>populaire et ouvrier</strong> au XIXe siècle. Aujourd'hui <strong>en gentrification</strong> avec installation de <strong>bars, restaurants tendance</strong>. <strong>Bistrots historiques</strong> sur la <strong>rue de Charonne</strong>.")
        ],
        "itin": [
            ("Église Saint-Germain-de-Charonne", "charonne", "à pied", "10 min à pied", 10),
            ("Voltaire", "voltaire", "M9", "M9 directe (1 station)", 2),
            ("Nation", "nation", "M9", "M9 directe (2 stations)", 4),
            ("Père Lachaise", "pere-lachaise", "M9 + M2", "M9 → Nation + M2", 8),
            ("Bastille", "bastille", "M9 + M5", "M9 → Oberkampf + M5", 10),
            ("République", "republique", "M9", "M9 directe (~10 min)", 10)
        ]
    },
    "rue-des-boulets": {
        "addr": "Boulevard Voltaire, 75011 Paris", "arr": "11e arrondissement (Paris)",
        "seo": "Station Rue des Boulets (M9) boulevard Voltaire dans le 11e. Quartier 11e populaire.",
        "tagline": "M9 — rue des Boulets, 11e populaire",
        "hero_desc": "Station <strong>Rue des Boulets</strong> sur le <strong>boulevard Voltaire</strong> dans le <strong>11e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>10 décembre 1933</strong>. Quartier populaire du <strong>11e</strong>.",
        "intros": [
            "La station <strong>Rue des Boulets</strong> est implantée sur le <strong>boulevard Voltaire</strong> dans le <strong>11e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Charonne</strong> (1 station) et <strong>Nation</strong> (1 station). Bus 46, 56, 86.",
            "Ouverte le <strong>10 décembre 1933</strong>.",
            "Le nom <strong>Rue des Boulets</strong> rappelle la <strong>rue des Boulets</strong> à proximité. Étymologie évoquant peut-être les <strong>fonderies</strong> ou <strong>fabriques de boulets de canon</strong> qui occupaient le quartier au XIXe siècle."
        ],
        "hist_title": "1933 : rue des Boulets et 11e populaire",
        "hist": [
            "La station Rue des Boulets est <strong>inaugurée le 10 décembre 1933</strong>.",
            "Le nom <strong>Rue des Boulets</strong> évoque peut-être les <strong>fonderies</strong> ou <strong>fabriques de boulets de canon</strong> qui occupaient le quartier au XIXe siècle, ou <strong>boulots</strong> (peupliers).",
            "Le quartier autour de la station fait partie du <strong>11e arrondissement</strong>, secteur <strong>populaire et résidentiel</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Rue des Boulets ?", "Uniquement la <strong>M9</strong>. Bus 46, 56, 86."),
            ("Quand a-t-elle ouvert ?", "Le <strong>10 décembre 1933</strong>."),
            ("D'où vient le nom Rue des Boulets ?", "Évoque peut-être les <strong>fonderies</strong> ou <strong>fabriques de boulets de canon</strong> du XIXe siècle."),
            ("Pour Nation ?", "<strong>M9 directe</strong> (1 station)."),
            ("Pour Bastille ?", "<strong>M9 + M5</strong> via Oberkampf."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier <strong>11e populaire</strong>.",
            "Pour <strong>Nation</strong> : <strong>M9 directe</strong> (1 station).",
            "Pour <strong>Bastille</strong> : <strong>M9 + M5</strong>.",
            "Pour <strong>République</strong> : <strong>M9 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏘️", "Boulevard Voltaire et axe est-ouest", "Le <strong>boulevard Voltaire</strong>, sur lequel se trouve la station, est tracé sous le <strong>Second Empire</strong> (1862). <strong>Long de 2,6 km</strong>, il relie la <strong>place de la République</strong> à la <strong>place de la Nation</strong>. <strong>Renommé Voltaire</strong> en 1879. <strong>Axe est-ouest majeur</strong> du <strong>11e arrondissement</strong>."),
            ("🏛️", "11e arrondissement, faubourg ouvrier", "Le <strong>11e arrondissement</strong> (~150 000 habitants) est historiquement un <strong>quartier populaire et ouvrier</strong>. <strong>Faubourg Saint-Antoine</strong>, ancien quartier des <strong>artisans du meuble</strong>. À partir des années 1990, <strong>gentrification</strong> avec installation de <strong>bars, restaurants tendance</strong> autour des rues <strong>Oberkampf, Jean-Pierre Timbaud, Saint-Maur</strong>.")
        ],
        "itin": [
            ("Nation", "nation", "M9", "M9 directe (1 station)", 2),
            ("Charonne", "charonne", "M9", "M9 directe (1 station)", 2),
            ("Voltaire", "voltaire", "M9", "M9 directe (2 stations)", 4),
            ("Père Lachaise", "pere-lachaise", "M9 + M2", "M9 → Nation + M2", 7),
            ("Bastille", "bastille", "M9 + M5", "M9 → Oberkampf + M5", 12),
            ("République", "republique", "M9", "M9 directe (~12 min)", 12)
        ]
    },
    "buzenval": {
        "addr": "Rue d'Avron, 75020 Paris", "arr": "20e arrondissement (Paris)",
        "seo": "Station Buzenval (M9) rue d'Avron dans le 20e. Hommage à la bataille de Buzenval (1871). Quartier Charonne.",
        "tagline": "M9 — Buzenval, bataille de 1871",
        "hero_desc": "Station <strong>Buzenval</strong> sur la <strong>rue d'Avron</strong> dans le <strong>20e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>10 décembre 1933</strong>. Hommage à la <strong>bataille de Buzenval</strong> (<strong>19 janvier 1871</strong>) pendant le <strong>siège de Paris</strong>.",
        "intros": [
            "La station <strong>Buzenval</strong> est implantée sur la <strong>rue d'Avron</strong> dans le <strong>20e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Nation</strong> (1 station) et <strong>Maraîchers</strong> (1 station). Bus 56, 76, 86.",
            "Ouverte le <strong>10 décembre 1933</strong>.",
            "Le nom <strong>Buzenval</strong> rend hommage à la <strong>bataille de Buzenval</strong> (<strong>19 janvier 1871</strong>), <strong>dernière sortie</strong> des Français pendant le <strong>siège de Paris</strong> lors de la <strong>guerre franco-prussienne</strong> de 1870-1871. <strong>Échec</strong>."
        ],
        "hist_title": "1933 : Buzenval, dernière sortie 1871",
        "hist": [
            "La station Buzenval est <strong>inaugurée le 10 décembre 1933</strong>.",
            "Le nom <strong>Buzenval</strong> rend hommage à la <strong>bataille de Buzenval</strong> (<strong>19 janvier 1871</strong>), <strong>dernière grande sortie</strong> des troupes françaises pendant le <strong>siège de Paris</strong> lors de la <strong>guerre franco-prussienne de 1870-1871</strong>.",
            "<strong>Tentative de percée</strong> du général <strong>Trochu</strong> contre les <strong>Prussiens</strong>. <strong>Échec coûteux</strong> avec <strong>~4 000 morts ou blessés</strong> côté français. Précipite la <strong>capitulation de Paris</strong> (28 janvier 1871). Le quartier autour de la station fait partie du <strong>20e arrondissement</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Buzenval ?", "Uniquement la <strong>M9</strong>. Bus 56, 76, 86."),
            ("Qu'est-ce que la bataille de Buzenval ?", "<strong>Dernière grande sortie</strong> des troupes françaises pendant le <strong>siège de Paris</strong> (1870-1871). <strong>19 janvier 1871</strong>. Échec coûteux."),
            ("Quand a-t-elle ouvert ?", "Le <strong>10 décembre 1933</strong>."),
            ("Pour Nation ?", "<strong>M9 directe</strong> (1 station)."),
            ("Pour Père Lachaise ?", "<strong>M9 + M2</strong> via Nation."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier <strong>20e populaire</strong> de <strong>Charonne</strong>.",
            "Pour <strong>Nation</strong> : <strong>M9 directe</strong> (1 station).",
            "Pour <strong>Cours de Vincennes</strong> et <strong>Bois de Vincennes</strong> : <strong>M9 → Nation</strong>.",
            "Pour <strong>Père Lachaise</strong> : <strong>M9 + M2</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⚔️", "Bataille de Buzenval (19 janvier 1871)", "La <strong>bataille de Buzenval</strong>, le <strong>19 janvier 1871</strong>, est la <strong>dernière grande sortie</strong> des troupes françaises pendant le <strong>siège de Paris</strong> lors de la <strong>guerre franco-prussienne de 1870-1871</strong>. <strong>Tentative de percée</strong> du général <strong>Louis-Jules Trochu</strong> (gouverneur militaire de Paris) contre les <strong>Prussiens</strong> à <strong>Buzenval</strong> (Hauts-de-Seine). <strong>Échec coûteux</strong> avec <strong>~4 000 morts ou blessés</strong> côté français, <strong>~600</strong> côté prussien. Précipite la <strong>capitulation de Paris</strong> (28 janvier 1871) et l'<strong>armistice</strong>."),
            ("🏘️", "20e arrondissement populaire", "Le <strong>20e arrondissement</strong> (~195 000 habitants) est historiquement un <strong>quartier populaire et multi-ethnique</strong> de Paris. Comprend les anciens villages de <strong>Ménilmontant, Belleville, Charonne</strong>. <strong>Cimetière du Père Lachaise</strong> à proximité. <strong>Parc de Belleville</strong> avec <strong>vue panoramique sur Paris</strong>.")
        ],
        "itin": [
            ("Nation", "nation", "M9", "M9 directe (1 station)", 2),
            ("Cours de Vincennes", "nation", "M9 + à pied", "M9 → Nation + à pied", 5),
            ("Père Lachaise", "pere-lachaise", "M9 + M2", "M9 → Nation + M2", 7),
            ("Bois de Vincennes", "porte-doree", "M9 + bus", "M9 → Nation + bus 56", 12),
            ("Bastille", "bastille", "M9 + M1", "M9 → Nation + M1", 12),
            ("République", "republique", "M9", "M9 directe (~14 min)", 14)
        ]
    },
    "maraichers": {
        "addr": "Boulevard Davout, 75020 Paris", "arr": "20e arrondissement (Paris)",
        "seo": "Station Maraîchers (M9) boulevard Davout dans le 20e. Quartier 20e résidentiel, à la limite du périphérique.",
        "tagline": "M9 — Maraîchers, 20e résidentiel",
        "hero_desc": "Station <strong>Maraîchers</strong> sur le <strong>boulevard Davout</strong> dans le <strong>20e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>10 décembre 1933</strong>. Quartier résidentiel du <strong>20e</strong>, à la <strong>limite du périphérique</strong>.",
        "intros": [
            "La station <strong>Maraîchers</strong> est implantée sur le <strong>boulevard Davout</strong> dans le <strong>20e arrondissement</strong>. Elle est desservie par la <strong>M9</strong>, entre <strong>Buzenval</strong> (1 station) et <strong>Porte de Montreuil</strong> (1 station). Bus 26, 64, 76.",
            "Ouverte le <strong>10 décembre 1933</strong>.",
            "Le nom <strong>Maraîchers</strong> rappelle la <strong>rue des Maraîchers</strong> et les <strong>anciennes activités maraîchères</strong> du quartier au XIXe siècle, qui alimentaient les Halles de Paris."
        ],
        "hist_title": "1933 : Maraîchers et 20e populaire",
        "hist": [
            "La station Maraîchers est <strong>inaugurée le 10 décembre 1933</strong>.",
            "Le nom <strong>Maraîchers</strong> rappelle les <strong>anciennes activités maraîchères</strong> du quartier au <strong>XIXe siècle</strong>. <strong>Plaines des Maraîchers</strong> alimentaient en <strong>légumes frais</strong> les <strong>Halles centrales de Paris</strong>.",
            "Le quartier autour de la station fait partie du <strong>20e arrondissement</strong>, secteur <strong>résidentiel et populaire</strong>. À courte distance : le <strong>boulevard périphérique</strong> et la <strong>commune de Montreuil</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Maraîchers ?", "Uniquement la <strong>M9</strong>. Bus 26, 64, 76."),
            ("Quand a-t-elle ouvert ?", "Le <strong>10 décembre 1933</strong>."),
            ("D'où vient le nom Maraîchers ?", "Des <strong>anciennes activités maraîchères</strong> du quartier au XIXe siècle qui alimentaient les Halles de Paris."),
            ("Pour Porte de Montreuil ?", "<strong>M9 directe</strong> (1 station)."),
            ("Pour Nation ?", "<strong>M9 directe</strong> (2 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier résidentiel du <strong>20e</strong>.",
            "Pour <strong>Porte de Montreuil</strong> et <strong>marché aux puces</strong> : <strong>M9 directe</strong>.",
            "Pour <strong>Nation</strong> : <strong>M9 directe</strong>.",
            "Pour <strong>Père Lachaise</strong> : <strong>M9 + M2</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🥬", "Maraîchers, plaine légumière du XIXe", "Le quartier des <strong>Maraîchers</strong>, autour de la station, doit son nom aux <strong>anciennes activités maraîchères</strong> du <strong>XIXe siècle</strong>. <strong>Plaines des Maraîchers</strong> alimentaient en <strong>légumes frais</strong> les <strong>Halles centrales de Paris</strong> (Baltard, 1854-1971). <strong>Choux, salades, poireaux, betteraves</strong>. <strong>Maraîchage intensif</strong> typique de la <strong>périphérie parisienne</strong> avant l'urbanisation."),
            ("🚇", "Boulevard Davout, Maréchaux", "Le <strong>boulevard Davout</strong>, sur lequel se trouve la station, fait partie des <strong>boulevards des Maréchaux</strong> tracés sous le <strong>Second Empire</strong> sur l'ancienne <strong>enceinte de Thiers</strong>. <strong>Renommés en hommage aux maréchaux d'Empire</strong> : <strong>Davout, Soult, Lefebvre, etc.</strong> <strong>Tramway T3b</strong> à proximité.")
        ],
        "itin": [
            ("Porte de Montreuil", "porte-de-montreuil", "M9", "M9 directe (1 station)", 2),
            ("Buzenval", "buzenval", "M9", "M9 directe (1 station)", 2),
            ("Nation", "nation", "M9", "M9 directe (2 stations)", 4),
            ("Père Lachaise", "pere-lachaise", "M9 + M2", "M9 → Nation + M2", 8),
            ("Bastille", "bastille", "M9 + M1", "M9 → Nation + M1", 14),
            ("République", "republique", "M9", "M9 directe (~16 min)", 16)
        ]
    },
    "porte-de-montreuil": {
        "addr": "Place de la Porte de Montreuil, 75020 Paris", "arr": "20e arrondissement (Paris)",
        "seo": "Station Porte de Montreuil (M9) place de la Porte de Montreuil dans le 20e. Marché aux Puces de la Porte de Montreuil. Tramway T3b.",
        "tagline": "M9 + T3b — Marché aux Puces Porte de Montreuil",
        "hero_desc": "Station <strong>Porte de Montreuil</strong> sur la <strong>place de la Porte de Montreuil</strong> dans le <strong>20e arrondissement</strong>. Desservie par la <strong>M9</strong>, ouverte le <strong>10 décembre 1933</strong>. À la sortie : le <strong>Marché aux Puces de la Porte de Montreuil</strong>. Correspondance <strong>tramway T3b</strong>.",
        "intros": [
            "La station <strong>Porte de Montreuil</strong> est implantée sur la <strong>place de la Porte de Montreuil</strong>, à la <strong>limite est du 20e arrondissement</strong>. Elle est desservie par la <strong>M9</strong> et le <strong>tramway T3b</strong>. Bus 26, 57, 102, 122, 351.",
            "Ouverte le <strong>10 décembre 1933</strong>.",
            "À la sortie : le <strong>Marché aux Puces de la Porte de Montreuil</strong>, l'un des <strong>trois grands marchés aux puces parisiens</strong> avec Saint-Ouen et Vanves. <strong>Tramway T3b</strong> en correspondance directe."
        ],
        "hist_title": "1933 : marché aux puces et T3b",
        "hist": [
            "La station Porte de Montreuil est <strong>inaugurée le 10 décembre 1933</strong>.",
            "Le <strong>Marché aux Puces de la Porte de Montreuil</strong>, à la sortie, est l'un des <strong>trois grands marchés aux puces parisiens</strong> avec <strong>Saint-Ouen</strong> et <strong>Vanves</strong>. Ouvert depuis les <strong>années 1860</strong>. <strong>~400 exposants</strong>. <strong>Brocante, vêtements d'occasion, livres, vinyles, jouets, mobilier</strong>. <strong>Ouvert samedi, dimanche et lundi</strong>.",
            "Le <strong>tramway T3b</strong>, en correspondance, est <strong>inauguré le 15 décembre 2012</strong> comme <strong>prolongement du T3a</strong> sur les <strong>boulevards des Maréchaux</strong> à l'est. <strong>~14 km</strong> entre <strong>Porte de Vincennes</strong> et <strong>Porte d'Asnières</strong> (prolongation 2018)."
        ],
        "faq": [
            ("Quelles lignes desservent Porte de Montreuil ?", "<strong>M9</strong> et <strong>tramway T3b</strong>. Bus 26, 57, 102, 122, 351."),
            ("Quand a-t-elle ouvert ?", "Le <strong>10 décembre 1933</strong>."),
            ("Pour le marché aux puces ?", "<strong>Sortie directe</strong>. Ouvert samedi, dimanche, lundi."),
            ("Pour Montreuil (93) ?", "<strong>M9 directe</strong> vers <strong>Robespierre</strong> ou <strong>Croix de Chavaux</strong>."),
            ("Pour Nation ?", "<strong>M9 directe</strong> (3 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Marché aux Puces</strong> à la sortie : ~400 exposants, samedi/dimanche/lundi.",
            "<strong>Brocante, vêtements occasion, livres, vinyles, jouets, mobilier</strong>.",
            "<strong>Tramway T3b</strong> en correspondance directe.",
            "Pour <strong>Montreuil (93)</strong> : <strong>M9 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🛍️", "Marché aux Puces de la Porte de Montreuil", "Le <strong>Marché aux Puces de la Porte de Montreuil</strong>, à la sortie de la station, est l'un des <strong>trois grands marchés aux puces parisiens</strong> avec <strong>Saint-Ouen</strong> et <strong>Vanves</strong>. Ouvert depuis les <strong>années 1860</strong>. <strong>~400 exposants</strong>. <strong>Brocante, vêtements d'occasion, livres, vinyles, jouets, mobilier</strong>. <strong>Atmosphère populaire</strong>, <strong>prix attractifs</strong>. <strong>Ouvert samedi, dimanche et lundi</strong> matin."),
            ("🚊", "Tramway T3b (2012)", "Le <strong>tramway T3b</strong>, en correspondance, est <strong>inauguré le 15 décembre 2012</strong> comme <strong>prolongement du T3a</strong> sur les <strong>boulevards des Maréchaux</strong> à l'est. <strong>~14 km</strong> entre <strong>Porte de Vincennes</strong> et <strong>Porte d'Asnières</strong> (prolongation 2018). <strong>~150 000 voyageurs/jour</strong>.")
        ],
        "itin": [
            ("Marché aux Puces de Montreuil", "porte-de-montreuil", "à pied", "Sortie directe", 2),
            ("Tramway T3b", "porte-de-montreuil", "T3b", "Correspondance directe", 1),
            ("Robespierre (Montreuil 93)", "robespierre", "M9", "M9 directe (1 station)", 2),
            ("Mairie de Montreuil (terminus)", "mairie-de-montreuil", "M9", "M9 directe (3 stations)", 6),
            ("Nation", "nation", "M9", "M9 directe (3 stations)", 6),
            ("République", "republique", "M9", "M9 directe (~18 min)", 18)
        ]
    },
    "robespierre": {
        "addr": "Avenue de la République, 93100 Montreuil", "arr": "Montreuil (93)",
        "seo": "Station Robespierre (M9) à Montreuil (93). Quartier Montreuil. Hommage à Maximilien Robespierre, homme politique de la Révolution.",
        "tagline": "M9 — Robespierre, Montreuil 93",
        "hero_desc": "Station <strong>Robespierre</strong> à <strong>Montreuil</strong> (Seine-Saint-Denis, 93). Desservie par la <strong>M9</strong>, ouverte le <strong>14 octobre 1937</strong>. Hommage à <strong>Maximilien Robespierre</strong> (<strong>1758-1794</strong>), <strong>homme politique français</strong> de la <strong>Révolution</strong>.",
        "intros": [
            "La station <strong>Robespierre</strong> est implantée à <strong>Montreuil</strong> (Seine-Saint-Denis, 93). Elle est desservie par la <strong>M9</strong>, entre <strong>Porte de Montreuil</strong> (1 station) et <strong>Croix de Chavaux</strong> (1 station). Bus 102, 122.",
            "Ouverte le <strong>14 octobre 1937</strong> avec le <strong>prolongement de la M9</strong> à Mairie de Montreuil.",
            "Le nom <strong>Robespierre</strong> rend hommage à <strong>Maximilien François Marie Isidore de Robespierre</strong> (<strong>1758-1794</strong>), <strong>homme politique français</strong> de la <strong>Révolution française</strong>. <strong>Avocat</strong>, <strong>député du Tiers État aux États généraux</strong> de 1789, <strong>membre de la Convention</strong>."
        ],
        "hist_title": "1937 : Robespierre et Révolution",
        "hist": [
            "La station Robespierre est <strong>inaugurée le 14 octobre 1937</strong> avec le <strong>prolongement de la M9</strong> à <strong>Mairie de Montreuil</strong>.",
            "Le nom <strong>Robespierre</strong> rend hommage à <strong>Maximilien François Marie Isidore de Robespierre</strong> (<strong>6 mai 1758 - 28 juillet 1794</strong>), <strong>homme politique français</strong> de la <strong>Révolution française</strong>. <strong>Avocat</strong> à Arras.",
            "<strong>Député du Tiers État aux États généraux</strong> de 1789, puis <strong>membre de la Convention</strong>. <strong>Surnommé « l'Incorruptible »</strong>. <strong>Figure majeure de la Révolution</strong>. <strong>Membre du Comité de salut public</strong>. <strong>Montreuil</strong> (~110 000 habitants), <strong>commune populaire</strong> de la <strong>Seine-Saint-Denis</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Robespierre ?", "Uniquement la <strong>M9</strong>. Bus 102, 122."),
            ("Qui est Robespierre ?", "<strong>Maximilien Robespierre</strong> (1758-1794), <strong>homme politique français</strong> de la <strong>Révolution</strong>. <strong>Surnommé « l'Incorruptible »</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>14 octobre 1937</strong>."),
            ("Pour Mairie de Montreuil ?", "<strong>M9 directe</strong> (2 stations)."),
            ("Pour Nation ?", "<strong>M9 directe</strong> (4 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier <strong>Montreuil</strong> (Seine-Saint-Denis 93).",
            "Pour <strong>Mairie de Montreuil</strong> (terminus) : <strong>M9 directe</strong> (2 stations).",
            "Pour <strong>Marché aux puces Montreuil</strong> : <strong>M9 → Porte de Montreuil</strong>.",
            "Pour <strong>Nation</strong> : <strong>M9 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Seine-Saint-Denis."
        ],
        "trivia": [
            ("📜", "Robespierre, figure révolutionnaire", "<strong>Maximilien Robespierre</strong> (1758-1794), <strong>homme politique français</strong> de la <strong>Révolution française</strong>. <strong>Avocat</strong> à Arras. <strong>Député du Tiers État aux États généraux</strong> de 1789, puis <strong>membre de la Convention</strong>. <strong>Membre du Comité de salut public</strong>. <strong>Surnommé « l'Incorruptible »</strong>. <strong>Figure majeure</strong> de la Révolution française."),
            ("🏘️", "Montreuil (93), ville populaire dynamique", "<strong>Montreuil</strong> (~110 000 habitants), commune du <strong>Seine-Saint-Denis</strong>. <strong>Ville populaire et dynamique</strong>, <strong>4e commune la plus peuplée d'Île-de-France</strong>. Anciennement <strong>quartier de pêchers</strong> (fameux <strong>pêches de Montreuil</strong> du XIXe siècle). Aujourd'hui <strong>haut lieu de la culture alternative parisienne</strong>, avec de nombreux <strong>ateliers d'artistes</strong>, <strong>théâtres</strong>, <strong>collectifs</strong>.")
        ],
        "itin": [
            ("Mairie de Montreuil (terminus)", "mairie-de-montreuil", "M9", "M9 directe (2 stations)", 4),
            ("Croix de Chavaux", "croix-de-chavaux", "M9", "M9 directe (1 station)", 2),
            ("Marché aux puces Montreuil", "porte-de-montreuil", "M9", "M9 directe (1 station)", 2),
            ("Nation", "nation", "M9", "M9 directe (4 stations)", 8),
            ("République", "republique", "M9", "M9 directe (~20 min)", 20),
            ("Mairie de Montreuil (terminus)", "mairie-de-montreuil", "M9", "M9 directe (2 stations)", 4)
        ]
    },
    "croix-de-chavaux": {
        "addr": "Place de la Croix de Chavaux, 93100 Montreuil", "arr": "Montreuil (93)",
        "seo": "Station Croix de Chavaux (M9) à Montreuil (93). Centre commerçant de Montreuil. Quartier populaire de Montreuil.",
        "tagline": "M9 — Croix de Chavaux, Montreuil centre",
        "hero_desc": "Station <strong>Croix de Chavaux</strong> à <strong>Montreuil</strong> (Seine-Saint-Denis, 93). Desservie par la <strong>M9</strong>, ouverte le <strong>14 octobre 1937</strong>. <strong>Centre commerçant</strong> de Montreuil.",
        "intros": [
            "La station <strong>Croix de Chavaux</strong> est implantée à <strong>Montreuil</strong> (Seine-Saint-Denis, 93). Elle est desservie par la <strong>M9</strong>, entre <strong>Robespierre</strong> (1 station) et <strong>Mairie de Montreuil</strong> (1 station, terminus). Bus 102, 122, 127.",
            "Ouverte le <strong>14 octobre 1937</strong> avec le <strong>prolongement de la M9</strong>.",
            "Le nom <strong>Croix de Chavaux</strong> rappelle la <strong>place de la Croix de Chavaux</strong> à proximité. <strong>Centre commerçant historique</strong> de Montreuil."
        ],
        "hist_title": "1937 : Croix de Chavaux et Montreuil centre",
        "hist": [
            "La station Croix de Chavaux est <strong>inaugurée le 14 octobre 1937</strong> avec le <strong>prolongement de la M9</strong>.",
            "Le nom <strong>Croix de Chavaux</strong> rappelle la <strong>place de la Croix de Chavaux</strong>, ancienne <strong>croix de chemin</strong> au carrefour des routes vers <strong>Montreuil, Bagnolet et Romainville</strong>.",
            "Le quartier autour de la station est le <strong>centre commerçant historique</strong> de <strong>Montreuil</strong>. <strong>Marché de la Croix de Chavaux</strong>, <strong>commerces de proximité</strong>, <strong>restaurants</strong>. Quartier en <strong>gentrification progressive</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Croix de Chavaux ?", "Uniquement la <strong>M9</strong>. Bus 102, 122, 127."),
            ("Quand a-t-elle ouvert ?", "Le <strong>14 octobre 1937</strong>."),
            ("Pour Mairie de Montreuil (terminus) ?", "<strong>M9 directe</strong> (1 station)."),
            ("Pour Marché aux puces Montreuil ?", "<strong>M9 → Porte de Montreuil</strong> (2 stations)."),
            ("Pour Nation ?", "<strong>M9 directe</strong> (5 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Centre commerçant historique</strong> de Montreuil.",
            "<strong>Marché de la Croix de Chavaux</strong> à proximité.",
            "Pour <strong>Mairie de Montreuil (terminus)</strong> : <strong>M9 directe</strong>.",
            "Pour <strong>Marché aux puces Montreuil</strong> : <strong>M9 → Porte de Montreuil</strong>.",
            "Zone tarifaire <strong>3</strong>, Seine-Saint-Denis."
        ],
        "trivia": [
            ("🛍️", "Croix de Chavaux, centre Montreuil", "La <strong>place de la Croix de Chavaux</strong>, autour de la station, est le <strong>centre commerçant historique de Montreuil</strong>. <strong>Marché de la Croix de Chavaux</strong> (mardi, vendredi, dimanche), <strong>commerces de proximité</strong>, <strong>restaurants</strong>. Ancienne <strong>croix de chemin</strong> au carrefour des routes médiévales vers <strong>Montreuil, Bagnolet et Romainville</strong>."),
            ("🎭", "Montreuil culturelle", "<strong>Montreuil</strong> (~110 000 habitants), commune du <strong>Seine-Saint-Denis</strong>. <strong>4e commune la plus peuplée d'Île-de-France</strong>. <strong>Haut lieu de la culture alternative parisienne</strong> : <strong>théâtre Berthelot</strong>, <strong>Comédie de Montreuil</strong>, <strong>Théâtre des Roches</strong>, <strong>Méliès</strong> (cinéma art et essai), nombreux <strong>ateliers d'artistes</strong>.")
        ],
        "itin": [
            ("Mairie de Montreuil (terminus)", "mairie-de-montreuil", "M9", "M9 directe (1 station)", 2),
            ("Robespierre", "robespierre", "M9", "M9 directe (1 station)", 2),
            ("Marché aux puces Montreuil", "porte-de-montreuil", "M9", "M9 directe (2 stations)", 4),
            ("Nation", "nation", "M9", "M9 directe (5 stations)", 10),
            ("République", "republique", "M9", "M9 directe (~22 min)", 22),
            ("Champs-Élysées", "franklin-d-roosevelt", "M9", "M9 directe (~30 min)", 30)
        ]
    },
    "mairie-de-montreuil": {
        "addr": "Place Jean-Jaurès, 93100 Montreuil", "arr": "Montreuil (93)",
        "seo": "Station Mairie de Montreuil, terminus est M9 à Montreuil (93). Hôtel de ville de Montreuil. Quartier Bel-Air. 4e commune Île-de-France.",
        "tagline": "M9 — terminus est, Mairie de Montreuil",
        "hero_desc": "Station <strong>Mairie de Montreuil</strong>, <strong>terminus est de la M9</strong>, à <strong>Montreuil</strong> (Seine-Saint-Denis, 93). Ouverte le <strong>14 octobre 1937</strong>. À la sortie : l'<strong>hôtel de ville de Montreuil</strong>.",
        "intros": [
            "La station <strong>Mairie de Montreuil</strong> est le <strong>terminus est de la M9</strong>, à <strong>Montreuil</strong> (Seine-Saint-Denis, 93). Bus 102, 121, 122, 127, 322, 351.",
            "Ouverte le <strong>14 octobre 1937</strong> avec le <strong>prolongement de la M9</strong> de Porte de Montreuil à Mairie de Montreuil.",
            "À la sortie : l'<strong>hôtel de ville de Montreuil</strong>, en plein centre de la commune. <strong>Montreuil</strong> (~110 000 habitants), <strong>4e commune la plus peuplée d'Île-de-France</strong>."
        ],
        "hist_title": "1937 : terminus est Montreuil",
        "hist": [
            "La station Mairie de Montreuil est <strong>inaugurée le 14 octobre 1937</strong> comme <strong>terminus est de la M9</strong>, avec le <strong>prolongement de la M9</strong> de Porte de Montreuil à Mairie de Montreuil.",
            "<strong>Montreuil</strong> (~110 000 habitants), <strong>commune du Seine-Saint-Denis</strong>. <strong>4e commune la plus peuplée d'Île-de-France</strong> après Paris, Boulogne-Billancourt et Saint-Denis. Anciennement <strong>quartier de pêchers</strong> (célèbres <strong>pêches de Montreuil</strong> du XIXe siècle).",
            "Aujourd'hui <strong>haut lieu de la culture alternative parisienne</strong>, avec de nombreux <strong>ateliers d'artistes</strong>, <strong>théâtres</strong> (Méliès, Berthelot), <strong>collectifs culturels</strong>. <strong>Maire Patrice Bessac</strong> (parti communiste français) depuis 2014."
        ],
        "faq": [
            ("Quelles lignes desservent Mairie de Montreuil ?", "Uniquement la <strong>M9</strong> (terminus est). Bus 102, 121, 122, 127, 322, 351."),
            ("Quand a-t-elle ouvert ?", "Le <strong>14 octobre 1937</strong>."),
            ("Combien d'habitants à Montreuil ?", "<strong>~110 000 habitants</strong>, <strong>4e commune la plus peuplée d'Île-de-France</strong>."),
            ("Pour le centre Montreuil ?", "<strong>Sortie directe</strong>."),
            ("Pour Paris centre ?", "<strong>M9 directe</strong> vers République (~25 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Hôtel de ville de Montreuil</strong> à la sortie.",
            "<strong>4e commune la plus peuplée d'Île-de-France</strong>.",
            "<strong>Haut lieu de la culture alternative parisienne</strong> : ateliers, théâtres.",
            "Pour <strong>Marché aux puces Montreuil</strong> : <strong>M9 → Porte de Montreuil</strong>.",
            "Zone tarifaire <strong>3</strong>, Seine-Saint-Denis."
        ],
        "trivia": [
            ("🍑", "Pêches de Montreuil, fierté du XIXe", "<strong>Montreuil</strong> fut au <strong>XIXe siècle</strong> célèbre pour ses <strong>pêches de Montreuil</strong>. <strong>Murs à pêches</strong>, technique unique d'<strong>arboriculture en espalier</strong> contre des <strong>murs blanchis à la chaux</strong> qui <strong>accumulaient la chaleur</strong>. <strong>~300 ha de murs</strong> dans la commune. <strong>Pêches haut de gamme</strong> servies à la <strong>cour de Louis XIV</strong> et exportées en Angleterre. <strong>Quelques murs préservés</strong> aujourd'hui, classés monument historique."),
            ("🎭", "Montreuil culturelle alternative", "<strong>Montreuil</strong> est aujourd'hui un <strong>haut lieu de la culture alternative parisienne</strong>. <strong>~5 000 artistes</strong> y habitent. <strong>Nombreux ateliers</strong>, <strong>théâtres</strong> (<strong>Le Méliès</strong> cinéma art et essai, <strong>Théâtre Berthelot</strong>, <strong>Comédie de Montreuil</strong>, <strong>Nouveau Théâtre de Montreuil</strong>), <strong>collectifs culturels</strong>. <strong>Festival international du film de Montreuil</strong>.")
        ],
        "itin": [
            ("Centre de Montreuil", "mairie-de-montreuil", "à pied", "Sortie directe", 2),
            ("Croix de Chavaux", "croix-de-chavaux", "M9", "M9 directe (1 station)", 2),
            ("Marché aux puces Montreuil", "porte-de-montreuil", "M9", "M9 directe (3 stations)", 6),
            ("Nation", "nation", "M9", "M9 directe (6 stations)", 12),
            ("République", "republique", "M9", "M9 directe (~25 min)", 25),
            ("Champs-Élysées", "franklin-d-roosevelt", "M9", "M9 directe (~32 min)", 32)
        ]
    }
}

def enrich(slug, c):
    p = STATIONS / f"{slug}.json"
    d = json.loads(p.read_text())
    d["published"] = True
    d.pop("_doc", None); d.pop("_todo", None)
    d["address"] = c["addr"]
    d["arrondissement"] = c["arr"]
    if "(Paris)" in c["arr"]:
        d["tariff_zone"] = 1; d["tariff_zone_context"] = "Paris intra-muros"; d["commune"] = "Paris"
    elif "(92)" in c["arr"]:
        d["tariff_zone"] = 2; d["tariff_zone_context"] = "Hauts-de-Seine (92), zone tarifaire 2"
        d["commune"] = c["arr"].split(" (")[0]
    elif "(93)" in c["arr"]:
        d["tariff_zone"] = 3; d["tariff_zone_context"] = "Seine-Saint-Denis (93), zone tarifaire 3"
        d["commune"] = c["arr"].split(" (")[0]
    else:
        d["tariff_zone"] = 1; d["tariff_zone_context"] = "Paris intra-muros"; d["commune"] = "Paris"
    d["seo"] = {"description": c["seo"]}
    d["hero"] = {"tagline": c["tagline"], "description": c["hero_desc"]}
    d["intro_paragraphs"] = c["intros"]
    d["history"] = {"title": c["hist_title"], "paragraphs": c["hist"]}
    d["faq"] = [{"question": q, "answer": a} for q, a in c["faq"]]
    d["practical_tips"] = c["tips"]
    d["trivia"] = [{"icon": ic, "title": t, "content": txt} for ic, t, txt in c["trivia"]]
    d["popular_itineraries"] = [
        {"destination_name": dn, "destination_slug": ds, "destination_full_name": f"{d['name']} → {dn.split(' via')[0]}",
         "lines_used": [lu] if not isinstance(lu, list) else lu, "lines_label": ll,
         "duration_minutes": dur, "changes_count": 1 if " + " in lu else 0,
         "search_volume_estimate": "high", "future_url": f"/itineraires/station-{slug}/{slug}-vers-{ds}/"}
        for (dn, ds, lu, ll, dur) in c["itin"]
    ]
    if "hero_image" in d: d["hero_image"]["keep_hero"] = True
    if not d.get("services"):
        d["services"] = {
            "wifi": {"available": False, "location_detail": "", "coverage_detail": ""},
            "toilets": {"public_paid": {"available": False}, "public_free": {"available": False, "location": "", "access": ""}},
            "atm": {"available": True, "banks_count_estimate": "rares", "locations": []},
            "ratp_office": {"available": False, "location": "", "services": ""},
            "left_luggage": {"ratp_available": False, "third_party": []},
            "shopping_dining": {"main_location": "", "details": "Commerces de quartier.", "secondary": ""}
        }
    if not d.get("safety") or not d.get("safety", {}).get("tips"):
        d["safety"] = {
            "audit_status": "pending", "audit_date": None, "level": "", "agents": None, "police": None,
            "tips": ["Station métro Paris — vigilance pickpockets standard.", "Affluence variable selon heures de pointe."],
            "notes": "Audit RATP/IDFM spécifique non disponible."
        }
    if not d.get("accessibility"):
        d["accessibility"] = {
            "audit_status": "pending", "audit_date": None, "level": "",
            "stats": {"elevators_count": 0, "accessible_lines": 0, "total_lines": len(d.get("lines",[]))},
            "details": "Accessibilité à vérifier."
        }
    p.write_text(json.dumps(d, indent=4, ensure_ascii=False) + "\n")
    print(f"✓ {slug}")

if __name__ == "__main__":
    for slug, c in CONTENT.items():
        try: enrich(slug, c)
        except Exception as e: print(f"✗ {slug}: {e}")
