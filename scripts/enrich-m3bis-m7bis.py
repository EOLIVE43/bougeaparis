#!/usr/bin/env python3
"""Enrichit M3bis+M7bis JSONs avec contenu T0 Wikipedia FR (mode condense)."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    # ====== M3BIS — 3 nouvelles + Père-Lachaise déjà publié ======
    "gambetta": {
        "addr": "Place Gambetta, 75020 Paris", "arr": "20e (Paris)",
        "seo": "Station Gambetta : terminus est M3 et terminus sud M3bis dans le 20e arr., place Gambetta avec Mairie du 20e, accès Cimetière du Père-Lachaise et hôpital Tenon.",
        "tagline": "M3 + M3bis — terminus est M3 et sud M3bis, Mairie du 20e",
        "hero_desc": "Station <strong>Gambetta</strong> sur la <strong>place Gambetta</strong> dans le <strong>20e arrondissement</strong>. Terminus est de la <strong>M3</strong> (ouverte 25 janvier 1905) et <strong>terminus sud de la M3bis</strong> (ouverte 27 mars 1971, originellement branche M3 vers Porte des Lilas, séparée en ligne autonome). À la sortie : la <strong>Mairie du 20e arrondissement</strong> et un accès rapproché au <strong>Cimetière du Père-Lachaise</strong>.",
        "intros": [
            "La station <strong>Gambetta</strong> est située dans le <strong>20e arrondissement de Paris</strong>, sur la <strong>place Gambetta</strong>. Elle est desservie par <strong>2 lignes</strong> : <strong>M3</strong> (terminus est, Pont de Levallois ↔ Gambetta) et <strong>M3bis</strong> (terminus sud, Gambetta ↔ Porte des Lilas). Bus 26, 60, 61, 64, 69, 96.",
            "La station <strong>M3</strong> est inaugurée le <strong>25 janvier 1905</strong> avec le tronçon Père Lachaise ↔ Villiers. Elle deviendra terminus est de la M3 en 1921. La <strong>M3bis</strong> est créée le <strong>27 mars 1971</strong> par <strong>séparation de la branche Porte des Lilas ↔ Gambetta de la M3 historique</strong> — devient ligne autonome.",
            "À <strong>5 min à pied</strong> : la <strong>Mairie du 20e arrondissement</strong> (1865-1877, architecte Claude Naissant, style éclectique néo-Renaissance). À <strong>10 min</strong> : l'entrée principale du <strong>Cimetière du Père-Lachaise</strong> (1804, ~70 ha, ~1 million de sépultures, monument funéraire le plus visité au monde — Chopin, Wilde, Morrison, Piaf, etc.). À <strong>5 min</strong> : <strong>hôpital Tenon</strong> (AP-HP)."
        ],
        "hist_title": "1905 : M3, 1971 : création M3bis (séparation branche)",
        "hist": [
            "La station <strong>Gambetta</strong> est inaugurée le <strong>25 janvier 1905</strong> avec le tronçon Père Lachaise ↔ Villiers de la M3. Devient <strong>terminus est de la M3</strong> en 1921.",
            "Le <strong>27 mars 1971</strong>, la <strong>M3bis est créée par séparation</strong> : la <strong>branche Gambetta ↔ Porte des Lilas</strong> de la M3 historique devient une <strong>ligne autonome courte</strong> (4 stations). Cas unique du réseau parisien : ligne créée non par construction nouvelle mais par <strong>scission administrative</strong>. La M3 perd sa branche est et s'arrête désormais à Gambetta.",
            "Le nom <strong>Gambetta</strong> commémore <strong>Léon Gambetta</strong> (1838-1882), <strong>homme politique français</strong>, leader de la <strong>défense nationale en 1870-1871</strong> (gouvernement de défense de Paris pendant le siège prussien), <strong>fondateur de la IIIe République</strong>. <strong>Symbole de la République</strong>. Statue équestre place Gambetta.",
            "À 5 min : la <strong>Mairie du 20e arrondissement</strong>, construite entre <strong>1865 et 1877</strong> par <strong>Claude Naissant</strong>. Style éclectique néo-Renaissance. Lieu institutionnel du 20e (~ 200 000 habitants, l'un des arrondissements les plus peuplés et populaires de Paris).",
            "À 10 min : l'<strong>entrée principale du Cimetière du Père-Lachaise</strong>, créé en <strong>1804</strong> par Napoléon. <strong>~70 hectares</strong>, <strong>~1 million de sépultures</strong>. <strong>Monument funéraire le plus visité au monde</strong> (~3,5 millions de visiteurs/an)."
        ],
        "faq": [
            ("Quelles lignes desservent Gambetta ?", "<strong>M3</strong> (terminus est) et <strong>M3bis</strong> (terminus sud)."),
            ("Pourquoi le nom Gambetta ?", "De <strong>Léon Gambetta</strong> (1838-1882), homme politique français, leader de la défense nationale en 1870-1871 et fondateur de la <strong>IIIe République</strong>."),
            ("Qu'est-ce que la M3bis ?", "Ligne autonome courte (4 stations) créée le <strong>27 mars 1971</strong> par <strong>séparation de la branche Gambetta ↔ Porte des Lilas de la M3</strong> historique. Cas unique du réseau parisien."),
            ("Où est le Père-Lachaise ?", "<strong>10 min à pied</strong> direction sud. Entrée principale boulevard de Ménilmontant. <strong>1804</strong>, ~70 ha, ~1 million de sépultures, monument funéraire le plus visité au monde."),
            ("Comment aller au centre de Paris ?", "<strong>M3 directe</strong> : ~15 min jusqu'à Opéra (10 stations vers l'ouest)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Stations historiques 1905/1971.")
        ],
        "tips": [
            "<strong>Mairie du 20e</strong> à 5 min — bâtiment historique 1865-1877.",
            "<strong>Père-Lachaise</strong> à 10 min — monument funéraire le plus visité au monde.",
            "<strong>Hôpital Tenon</strong> à 5 min.",
            "Pour <strong>Opéra</strong> : M3 directe (~15 min).",
            "Pour <strong>Porte des Lilas</strong> : M3bis directe (~6 min)."
        ],
        "trivia": [
            ("🚇", "M3bis (1971) — cas unique de scission de ligne", "La <strong>M3bis</strong> est créée le <strong>27 mars 1971</strong> par <strong>séparation</strong> de la branche est de la M3 (Gambetta ↔ Porte des Lilas, 4 stations) — <strong>cas unique du réseau parisien</strong> de ligne créée par <strong>scission administrative</strong> et non par construction nouvelle. La M3 historique avait initialement une branche en Y à Gambetta : un tronçon principal vers Père-Lachaise / Opéra / Levallois, et une branche annexe vers Porte des Lilas. La séparation en 1971 simplifie l'exploitation, mais crée une ligne très courte (1,3 km) à faible fréquentation."),
            ("🇫🇷", "Léon Gambetta — fondateur de la IIIe République", "<strong>Léon Gambetta</strong> (1838-1882), <strong>homme politique français</strong>, leader de la <strong>défense nationale française pendant la guerre franco-prussienne 1870-1871</strong> (gouvernement de défense de Paris pendant le siège prussien). Évacué de Paris en <strong>ballon le 7 octobre 1870</strong>, célèbre épisode. Considéré comme l'un des <strong>fondateurs de la IIIe République</strong>. Mort prématurément à 44 ans (accident d'arme à feu, gangrène). Statue équestre place Gambetta. Panthéonisé en 1920.")
        ],
        "itin": [
            ("Mairie du 20e", "mairie-20e", "à pied", "5 min direct", 5),
            ("Père-Lachaise (entrée principale)", "pere-lachaise-cimetiere", "à pied", "10 min sud", 10),
            ("Opéra via M3", "opera", "M3", "M3 direction Pont de Levallois", 15),
            ("Porte des Lilas via M3bis", "porte-des-lilas", "M3bis", "M3bis terminus nord", 6),
            ("République via M3", "republique", "M3", "M3 direction Pont de Levallois", 12),
            ("Hôpital Tenon", "hopital-tenon", "à pied", "5 min direct", 5)
        ]
    },
    "porte-des-lilas": {
        "addr": "Place du Maquis du Vercors, 75019 Paris", "arr": "19e (Paris)",
        "seo": "Station Porte des Lilas : terminus M3bis + M11 dans le 19e arr. (à la limite de la commune des Lilas, 93). Cimetière des Lilas, Stade Nautique de Paris.",
        "tagline": "M3bis + M11 — double terminus du nord-est parisien",
        "hero_desc": "Station <strong>Porte des Lilas</strong> à la <strong>limite du 19e arrondissement</strong> et de la commune des <strong>Lilas</strong> (Seine-Saint-Denis, 93). Desservie par <strong>M3bis</strong> (terminus nord, ouverte 27 novembre 1921) et <strong>M11</strong> (terminus est jusqu'au prolongement Rosny-sous-Bois prévu en 2024-2025, ouverte 28 avril 1935). <strong>Double terminus</strong> rare du réseau parisien.",
        "intros": [
            "La station <strong>Porte des Lilas</strong> est située à la <strong>limite du 19e arrondissement de Paris</strong> et de la commune des <strong>Lilas</strong> (Seine-Saint-Denis, 93). Elle est desservie par <strong>2 lignes</strong> : <strong>M3bis</strong> (terminus nord, Gambetta ↔ Porte des Lilas) et <strong>M11</strong> (Châtelet ↔ Rosny - Bois-Perrier, terminus est avant prolongement 2024-2025). Bus 48, 61, 64, 96, 105, 115, 129, 170.",
            "La station <strong>M11</strong> ouvre le <strong>28 avril 1935</strong> avec la M11 originelle (Châtelet ↔ Porte des Lilas). La station <strong>M3bis</strong> existait depuis le <strong>27 novembre 1921</strong> (à l'époque branche de la M3, séparée en M3bis en 1971). <strong>Double terminus</strong>, rare configuration du réseau parisien.",
            "À <strong>5 min à pied</strong> : la commune des <strong>Lilas</strong> (~22 000 habitants, Seine-Saint-Denis). À <strong>10 min</strong> : le <strong>Cimetière des Lilas</strong> et le futur <strong>Stade Nautique de Paris</strong> (prévu pour les Olympiades urbaines)."
        ],
        "hist_title": "1921 : M3bis (branche M3), 1935 : M11, double terminus",
        "hist": [
            "La station <strong>Porte des Lilas</strong> ouvre le <strong>27 novembre 1921</strong> avec la <strong>branche est de la M3</strong> (Gambetta ↔ Porte des Lilas, 4 stations). En <strong>1971</strong>, cette branche devient une ligne autonome appelée <strong>M3bis</strong> (cas unique de scission de ligne).",
            "La station <strong>M11</strong> est ajoutée le <strong>28 avril 1935</strong> avec l'ouverture de la M11 originelle (Châtelet ↔ Porte des Lilas, 9 stations). Configuration : <strong>terminus est de la M11</strong>, avec voies de retournement et garage. La M11 sera prolongée vers <strong>Rosny - Bois-Perrier (Grand Paris Express)</strong> en 2024-2025.",
            "<strong>Double terminus</strong> M3bis + M11, configuration rare et unique du réseau parisien. La station accueille aussi historiquement des <strong>quais déclassés</strong> non utilisés par les voyageurs (vestiges de configurations passées).",
            "La <strong>commune des Lilas</strong> à 5 min est l'une des plus petites communes de la première couronne (~22 000 habitants). Nom inspiré des <strong>lilas qui parfumaient l'ancien village rural</strong> au XIXe siècle. Quartier résidentiel.",
            "Futur : le <strong>Stade Nautique de Paris</strong>, prévu à proximité pour accueillir activités aquatiques liées aux Olympiades urbaines."
        ],
        "faq": [
            ("Quelles lignes desservent Porte des Lilas ?", "<strong>M3bis</strong> (terminus nord) et <strong>M11</strong> (terminus est avant prolongement Rosny 2024-2025). Bus 48, 61, 64, 96, 105, 115, 129, 170."),
            ("C'est où Les Lilas ?", "Commune des <strong>Hauts-de-Seine</strong>... <strong>Non, des Seine-Saint-Denis (93)</strong>. ~22 000 habitants. Nom inspiré des <strong>lilas qui parfumaient l'ancien village rural</strong> au XIXe siècle."),
            ("Pourquoi un double terminus ?", "<strong>M3bis et M11 se terminent toutes deux ici</strong>. Configuration rare et historique. M3bis : terminus depuis 1921. M11 : terminus est jusqu'au prolongement vers Rosny - Bois-Perrier (Grand Paris Express, 2024-2025)."),
            ("Comment aller à Châtelet ?", "<strong>M11 directe</strong> : ~20 min (8 stations vers l'ouest)."),
            ("Comment aller à Gambetta ?", "<strong>M3bis directe</strong> : ~6 min (3 stations vers le sud)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Stations historiques 1921/1935.")
        ],
        "tips": [
            "<strong>Commune des Lilas</strong> à 5 min — village historique 93.",
            "Pour <strong>Châtelet</strong> : M11 directe (~20 min).",
            "Pour <strong>Gambetta</strong> : M3bis directe (~6 min).",
            "Pour <strong>République</strong> : M11 directe.",
            "Quartier limite Paris/banlieue — différents tarifs si on traverse."
        ],
        "trivia": [
            ("🚇", "Double terminus M3bis + M11 — rare configuration", "Porte des Lilas est l'une des <strong>rares stations à double terminus</strong> du métro parisien : la <strong>M3bis</strong> y termine au nord, et la <strong>M11</strong> y termine à l'est. Configuration unique pour 2 lignes différentes. La M11 sera prolongée à <strong>Rosny - Bois-Perrier</strong> dans le cadre du <strong>Grand Paris Express</strong> en 2024-2025, ce qui mettra fin au statut de terminus est de la M11."),
            ("🌸", "Les Lilas — origine du nom rurale (XIXe)", "La <strong>commune des Lilas</strong> à 5 min de la station tire son nom des <strong>lilas qui parfumaient l'ancien village rural</strong> au XIXe siècle. Avant l'annexion de la zone par Paris et la construction des fortifications de Thiers (1841-1844), le territoire était occupé par des <strong>vergers et plantations de lilas</strong>, fournissant le marché parisien en fleurs et fruits. <strong>Annexée à Paris</strong> en 1860 (en partie), reste commune indépendante. ~22 000 habitants aujourd'hui.")
        ],
        "itin": [
            ("Châtelet via M11", "chatelet", "M11", "M11 direction Châtelet (8 stations)", 20),
            ("Gambetta via M3bis", "gambetta", "M3bis", "M3bis terminus sud (3 stations)", 6),
            ("République via M11", "republique", "M11", "M11 direction Châtelet", 14),
            ("Les Lilas centre", "les-lilas-centre", "à pied", "5 min sortie nord", 5),
            ("Cimetière des Lilas", "cimetiere-lilas", "à pied", "10 min direction nord", 10),
            ("Hôtel de Ville via M11", "hotel-de-ville", "M11", "M11 direction Châtelet (10 stations)", 22)
        ]
    },
    "saint-fargeau": {
        "addr": "Avenue Gambetta / rue Pelleport, 75020 Paris", "arr": "20e (Paris)",
        "seo": "Station Saint-Fargeau : M3bis pure dans le 20e arr., quartier Pelleport. Petite station résidentielle entre Gambetta et Pelleport (futur arrêt à venir).",
        "tagline": "M3bis — quartier résidentiel Pelleport",
        "hero_desc": "Station <strong>Saint-Fargeau</strong> sur la M3bis, ouverte le <strong>27 novembre 1921</strong>. Située dans le <strong>20e arrondissement</strong>, sous l'<strong>avenue Gambetta</strong> à proximité de la <strong>rue Pelleport</strong>. Petite station résidentielle de la ligne annexe M3bis (4 stations au total). Nom du <strong>square Saint-Fargeau</strong> proche.",
        "intros": [
            "La station <strong>Saint-Fargeau</strong> est située dans le <strong>20e arrondissement de Paris</strong>, sous l'<strong>avenue Gambetta</strong> à proximité de la <strong>rue Pelleport</strong>. Elle est desservie uniquement par la <strong>M3bis</strong> (Gambetta ↔ Porte des Lilas), entre <strong>Pelleport</strong> (1 station nord) et <strong>Gambetta</strong> (1 station sud). Bus 60, 64, 102.",
            "Ouverte le <strong>27 novembre 1921</strong> avec la branche Gambetta ↔ Porte des Lilas de la M3 (devenue M3bis en 1971).",
            "Le nom <strong>Saint-Fargeau</strong> vient du <strong>square Saint-Fargeau</strong> à proximité, lui-même nommé d'après <strong>Louis-Michel Lepeletier de Saint-Fargeau</strong> (1760-1793), homme politique français, conventionnel, président de l'Assemblée constituante, assassiné lors de la Révolution française. Quartier résidentiel et tranquille du 20e."
        ],
        "hist_title": "1921 : branche M3 vers Porte des Lilas",
        "hist": [
            "La station <strong>Saint-Fargeau</strong> est inaugurée le <strong>27 novembre 1921</strong> avec la <strong>branche est de la M3</strong> (Gambetta ↔ Porte des Lilas, 4 stations). Configuration souterraine simple, 2 voies / 2 quais latéraux.",
            "Le <strong>27 mars 1971</strong>, cette branche devient une <strong>ligne autonome</strong> appelée <strong>M3bis</strong>. Saint-Fargeau est l'une des 4 stations de la M3bis (avec Gambetta, Pelleport, Porte des Lilas).",
            "Le nom vient du <strong>square Saint-Fargeau</strong> à proximité, baptisé d'après <strong>Louis-Michel Lepeletier de Saint-Fargeau</strong> (1760-1793), homme politique français, <strong>conventionnel</strong>, <strong>président de l'Assemblée constituante</strong>. Vota la <strong>mort de Louis XVI</strong> (21 janvier 1793). <strong>Assassiné le lendemain</strong> par un garde du corps royaliste (Philippe Nicolas Marie de Pâris). Considéré comme l'un des <strong>premiers martyrs républicains</strong>.",
            "Le quartier autour est <strong>résidentiel et tranquille</strong>, peu connu des touristes. Commerces de proximité, peu d'attractions majeures. Fréquentation très faible (la M3bis a la plus basse fréquentation du réseau parisien, ~1,5 millions/an pour les 4 stations cumulées)."
        ],
        "faq": [
            ("Quelle ligne dessert Saint-Fargeau ?", "Uniquement la <strong>M3bis</strong>. Bus 60, 64, 102."),
            ("Pourquoi le nom Saint-Fargeau ?", "Du <strong>square Saint-Fargeau</strong> à proximité, nommé d'après <strong>Louis-Michel Lepeletier de Saint-Fargeau</strong> (1760-1793), conventionnel républicain, assassiné le 21 janvier 1793 pour avoir voté la mort de Louis XVI."),
            ("Comment aller à Châtelet ?", "<strong>M3bis vers Gambetta + M3</strong> : ~25 min total."),
            ("Comment aller à Père-Lachaise ?", "<strong>M3bis vers Gambetta</strong> + à pied : ~10 min."),
            ("Comment aller à Porte des Lilas ?", "<strong>M3bis directe</strong> : 2 stations (~4 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station historique 1921.")
        ],
        "tips": [
            "<strong>Square Saint-Fargeau</strong> à proximité — espace vert local.",
            "Pour <strong>Gambetta</strong> : M3bis directe (1 station).",
            "Pour <strong>Père-Lachaise</strong> : M3bis vers Gambetta + à pied (~10 min total).",
            "Quartier résidentiel — peu de commerces touristiques.",
            "M3bis : ligne la plus courte et la moins fréquentée du métro parisien."
        ],
        "trivia": [
            ("⚖️", "Louis-Michel Lepeletier de Saint-Fargeau (1760-1793)", "Le nom <strong>Saint-Fargeau</strong> vient de <strong>Louis-Michel Lepeletier de Saint-Fargeau</strong> (1760-1793), <strong>homme politique français</strong> de la Révolution. <strong>Conventionnel</strong>, <strong>président de l'Assemblée constituante</strong>. Vota la <strong>mort de Louis XVI</strong> (21 janvier 1793). <strong>Assassiné le lendemain</strong> dans un restaurant du Palais-Royal par un <strong>garde du corps royaliste</strong> (Philippe Nicolas Marie de Pâris). Considéré comme l'un des <strong>premiers martyrs républicains</strong>. <strong>Inhumé au Panthéon</strong> (transféré 1793, retiré 1795 lors de la Restauration). Statue à la Convention."),
            ("🚇", "M3bis — ligne la plus courte et la moins fréquentée", "La <strong>M3bis</strong>, sur laquelle se trouve Saint-Fargeau, est la <strong>plus courte ligne du métro parisien</strong> (1,3 km, 4 stations). C'est aussi la <strong>moins fréquentée</strong> (~1,5 millions de voyageurs/an cumulés sur les 4 stations, soit ~3 fois moins que la station moyenne du réseau). Statut de ligne « annexe ». Service par <strong>navette automatique</strong> aux heures creuses. À l'étude : prolongement vers <strong>Place des Fêtes</strong> pour interconnecter M3bis et M7bis, mais projet non concrétisé.")
        ],
        "itin": [
            ("Gambetta via M3bis", "gambetta", "M3bis", "M3bis terminus sud (1 station)", 2),
            ("Porte des Lilas via M3bis", "porte-des-lilas", "M3bis", "M3bis terminus nord (2 stations)", 4),
            ("Pelleport via M3bis", "pelleport", "M3bis", "M3bis direction Porte des Lilas (1 station)", 2),
            ("Père-Lachaise (Cimetière)", "pere-lachaise-cimetiere", "M3bis + à pied", "M3bis → Gambetta + 10 min à pied", 16),
            ("Châtelet via M3bis + M3", "chatelet", "M3bis + M3", "M3bis → Gambetta + M3 direction Pont de Levallois", 27),
            ("Opéra via M3bis + M3", "opera", "M3bis + M3", "M3bis → Gambetta + M3", 19)
        ]
    },
    # ====== M7BIS — 9 stations ======
    "louis-blanc": {
        "addr": "Bd de la Villette / av. Louis Blanc, 75010 Paris", "arr": "10e (Paris)",
        "seo": "Station Louis Blanc : M7 + M7bis terminus dans le 10e arr., quartier multi-ethnique. Point de séparation des branches sud (Mairie d'Ivry / Villejuif Louis Aragon) et nord-est (Boucle M7bis).",
        "tagline": "M7 + M7bis — terminus boucle nord-est",
        "hero_desc": "Station <strong>Louis Blanc</strong> dans le <strong>10e arrondissement</strong>, à l'intersection du boulevard de la Villette et de l'avenue Louis Blanc. Desservie par <strong>M7</strong> (ouverte 5 novembre 1910) et <strong>M7bis</strong> (terminus, ouverte 18 janvier 1911). La M7bis est la <strong>branche en boucle</strong> de la M7 vers les Buttes-Chaumont et Pré Saint-Gervais. Quartier multi-ethnique animé.",
        "intros": [
            "La station <strong>Louis Blanc</strong> est située dans le <strong>10e arrondissement de Paris</strong>, à l'intersection du <strong>boulevard de la Villette</strong> et de l'<strong>avenue Louis Blanc</strong>. Elle est desservie par <strong>2 lignes</strong> : <strong>M7</strong> (La Courneuve - 8 Mai 1945 ↔ Villejuif-Louis Aragon / Mairie d'Ivry) et <strong>M7bis</strong> (terminus, Louis Blanc ↔ Pré Saint-Gervais en boucle). Bus 26, 54, 65.",
            "La station <strong>M7</strong> ouvre le <strong>5 novembre 1910</strong> avec le tronçon Porte de la Villette ↔ Opéra de la M7. La <strong>M7bis</strong> ouvre le <strong>18 janvier 1911</strong> comme branche annexe — devient ligne autonome en <strong>1967</strong>. La M7bis a une configuration particulière : <strong>en boucle</strong>, sans terminus traditionnel.",
            "Le quartier autour est l'un des plus <strong>multi-ethniques de Paris</strong>, à proximité de la <strong>gare de l'Est</strong> et du quartier des immigrations (notamment indienne, sri-lankaise et pakistanaise rue du Faubourg-Saint-Denis et rue Cail). Affluence forte heures de pointe."
        ],
        "hist_title": "1910 : M7, 1911 : branche M7bis (ligne autonome 1967)",
        "hist": [
            "La station <strong>M7</strong> ouvre le <strong>5 novembre 1910</strong> avec le tronçon <strong>Porte de la Villette ↔ Opéra</strong> de la M7 (à l'époque ligne 10 selon ancienne nomenclature).",
            "La <strong>branche annexe</strong> M7bis (Louis Blanc ↔ Pré Saint-Gervais) ouvre le <strong>18 janvier 1911</strong>. Conçue comme une branche secondaire de la M7 pour desservir le quartier des Buttes-Chaumont. Particularité : <strong>configuration en boucle</strong>, sans terminus traditionnel — les trains font un parcours circulaire puis repartent.",
            "Le <strong>3 décembre 1967</strong>, la branche M7bis devient une <strong>ligne autonome</strong> (séparation administrative similaire à celle de la M3bis en 1971). Louis Blanc reste le <strong>terminus de la M7bis</strong>.",
            "Le nom <strong>Louis Blanc</strong> commémore <strong>Louis Blanc</strong> (1811-1882), <strong>homme politique français</strong> et <strong>journaliste</strong> du XIXe siècle. <strong>Théoricien socialiste</strong>, défenseur du <strong>droit au travail</strong> et de l'<strong>État social</strong>. Membre du gouvernement provisoire de 1848.",
            "Le quartier autour est l'un des plus <strong>multi-ethniques de Paris</strong> : <strong>diaspora indienne, sri-lankaise et pakistanaise</strong> rue du Faubourg-Saint-Denis et rue Cail (à 10 min). Restaurants, épiceries, salons de coiffure. Phénomène urbain unique en Europe avec le Chinatown du 13e."
        ],
        "faq": [
            ("Quelles lignes desservent Louis Blanc ?", "<strong>M7</strong> (1910) et <strong>M7bis</strong> (terminus, 1911 — ligne autonome depuis 1967). Bus 26, 54, 65."),
            ("Qu'est-ce que la M7bis ?", "<strong>Ligne autonome courte</strong> du métro parisien (8 stations, ~3 km), terminus à Louis Blanc, parcours en <strong>boucle</strong> via Buttes-Chaumont et Pré Saint-Gervais. Branche annexe historique de la M7 (1911), devenue ligne autonome en 1967."),
            ("Qui est Louis Blanc ?", "<strong>Louis Blanc</strong> (1811-1882), <strong>homme politique français et journaliste</strong> du XIXe siècle. <strong>Théoricien socialiste</strong>, défenseur du <strong>droit au travail</strong> et de l'<strong>État social</strong>. Membre du gouvernement provisoire de 1848. Pose les bases du socialisme français."),
            ("Comment aller à Châtelet ?", "<strong>M7 directe</strong> : ~12 min (6 stations vers le sud)."),
            ("Comment aller aux Buttes-Chaumont ?", "<strong>M7bis directe</strong> : ~6 min (3 stations en boucle)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Stations historiques 1910/1911.")
        ],
        "tips": [
            "<strong>Quartier multi-ethnique</strong> rue du Faubourg-Saint-Denis et rue Cail à 10 min.",
            "Pour <strong>Châtelet</strong> : M7 directe (~12 min).",
            "Pour <strong>Buttes-Chaumont</strong> : M7bis directe (~6 min).",
            "Pour <strong>Pyramides</strong> (M7 → M14) : M7 directe (~8 min).",
            "Quartier dense en restaurants asiatiques (Inde, Sri Lanka, Pakistan)."
        ],
        "trivia": [
            ("🚇", "M7bis — ligne autonome en boucle (1967)", "La <strong>M7bis</strong>, terminus à Louis Blanc, est l'une des <strong>2 lignes courtes du métro parisien</strong> (avec la M3bis). <strong>8 stations, ~3 km, parcours en boucle</strong> via Buttes-Chaumont et Pré Saint-Gervais. Particularité : <strong>configuration en boucle</strong>, sans terminus traditionnel — les trains font un parcours circulaire puis repartent. Branche annexe historique de la M7 ouverte en <strong>1911</strong>, devenue <strong>ligne autonome le 3 décembre 1967</strong>. ~3 millions de voyageurs/an, l'une des moins fréquentées du réseau."),
            ("🇮🇳", "Quartier indien/sri-lankais — rue du Faubourg-Saint-Denis", "Le quartier autour est l'un des plus <strong>multi-ethniques de Paris</strong>. À <strong>10 min</strong> : la <strong>rue du Faubourg-Saint-Denis</strong> et la <strong>rue Cail</strong> concentrent la <strong>diaspora indienne, sri-lankaise et pakistanaise</strong> de Paris. <strong>Restaurants indiens et sri-lankais</strong>, <strong>épiceries asiatiques</strong> (riz, épices, fruits), <strong>salons de coiffure</strong>, <strong>boutiques de saris</strong>. Plus grande concentration sud-asiatique d'Europe continentale. Phénomène urbain unique avec le Chinatown du 13e (Olympiades).")
        ],
        "itin": [
            ("Châtelet via M7", "chatelet", "M7", "M7 direction Mairie d'Ivry (6 stations)", 12),
            ("Buttes-Chaumont via M7bis", "buttes-chaumont", "M7bis", "M7bis (3 stations boucle)", 6),
            ("Gare de l'Est via M7", "gare-de-l-est", "M7", "M7 direction Mairie d'Ivry (2 stations)", 4),
            ("Pré Saint-Gervais via M7bis", "pre-saint-gervais", "M7bis", "M7bis terminus boucle", 10),
            ("Opéra via M7", "opera", "M7", "M7 direction Mairie d'Ivry (5 stations)", 10),
            ("Quartier indien (rue Faubourg-Saint-Denis)", "quartier-indien", "à pied", "10 min direct", 10)
        ]
    },
    "jaures": {
        "addr": "Av. Jean Jaurès / bd de la Villette, 75019 Paris", "arr": "19e (Paris)",
        "seo": "Station Jaurès : M2 + M5 + M7bis dans le 19e arr. Aérienne magnifique sur le canal de l'Ourcq, bassin de la Villette et port de plaisance Paris-Arsenal.",
        "tagline": "M2 + M5 + M7bis — aérienne sur le canal de l'Ourcq",
        "hero_desc": "Station <strong>Jaurès</strong> dans le <strong>19e arrondissement</strong>, sur l'avenue Jean Jaurès. Desservie par <strong>3 lignes</strong> : <strong>M2</strong> (ouverte 31 janvier 1903, aérienne sur viaduc), <strong>M5</strong> (ouverte 17 décembre 1942) et <strong>M7bis</strong> (ouverte 18 janvier 1911, terminus alternatif). Vue <strong>magnifique aérienne sur le canal de l'Ourcq</strong> et le <strong>bassin de la Villette</strong> (port de plaisance Paris-Arsenal).",
        "intros": [
            "La station <strong>Jaurès</strong> est située dans le <strong>19e arrondissement de Paris</strong>, sur l'<strong>avenue Jean Jaurès</strong> à l'intersection du boulevard de la Villette. Elle est desservie par <strong>3 lignes</strong> : <strong>M2</strong> (Porte Dauphine ↔ Nation, aérienne ici sur viaduc), <strong>M5</strong> (Bobigny - Pablo Picasso ↔ Place d'Italie) et <strong>M7bis</strong> (terminus, Louis Blanc ↔ Pré Saint-Gervais). Bus 26, 48, 75.",
            "La station <strong>M2</strong> ouvre le <strong>31 janvier 1903</strong> sur le viaduc aérien de la M2 (Villiers ↔ Bagnolet). La <strong>M7bis</strong> est ajoutée le <strong>18 janvier 1911</strong> comme branche annexe. La <strong>M5</strong> arrive le <strong>17 décembre 1942</strong> avec le prolongement vers Église de Pantin. La station devient ainsi un <strong>hub multi-modal majeur du nord-est parisien</strong>.",
            "La station offre une <strong>vue magnifique aérienne</strong> depuis les quais M2 : sur le <strong>canal de l'Ourcq</strong>, le <strong>bassin de la Villette</strong> (15 hectares, port de plaisance Paris-Arsenal) et la <strong>Rotonde de la Villette</strong> (1788, Claude-Nicolas Ledoux). Lieu emblématique du nord-est parisien, popularisé depuis les années 2010 (cafés, restaurants, péniches sur le canal)."
        ],
        "hist_title": "1903 : M2 aérienne, 1911 : M7bis, 1942 : M5 (hub)",
        "hist": [
            "La station <strong>M2</strong> ouvre le <strong>31 janvier 1903</strong> avec le prolongement de la M2 vers Bagnolet, sur le <strong>viaduc aérien</strong> caractéristique. Vue spectaculaire sur le canal de l'Ourcq et le bassin de la Villette.",
            "La <strong>branche M7bis</strong> est inaugurée le <strong>18 janvier 1911</strong> comme branche annexe de la M7 (devient ligne autonome en 1967). Jaurès devient station de correspondance.",
            "Le <strong>17 décembre 1942</strong>, la <strong>M5</strong> arrive avec le prolongement de la M5 (Gare du Nord ↔ Église de Pantin). La station devient un <strong>hub 3 lignes</strong> du nord-est parisien.",
            "Le nom <strong>Jaurès</strong> commémore <strong>Jean Jaurès</strong> (1859-1914), <strong>homme politique français</strong>, <strong>fondateur du Parti socialiste français unifié (SFIO)</strong> en 1905. <strong>Pacifiste convaincu</strong>, opposé à la guerre. <strong>Assassiné le 31 juillet 1914</strong> au café du Croissant (rue Montmartre) par Raoul Villain, 3 jours avant le début de la Première Guerre mondiale. Considéré comme l'un des plus grands orateurs de la Troisième République.",
            "Le quartier autour, le <strong>bassin de la Villette</strong> (15 ha, port de plaisance Paris-Arsenal), a connu une <strong>revitalisation majeure dans les années 2010</strong> : aménagement des quais, péniches restaurants, cafés, MK2 cinéma de plein air, jeux nautiques. Lieu emblématique du nord-est parisien."
        ],
        "faq": [
            ("Quelles lignes desservent Jaurès ?", "<strong>M2</strong> (aérienne sur viaduc), <strong>M5</strong> et <strong>M7bis</strong> (terminus). Bus 26, 48, 75."),
            ("Pourquoi la M2 est-elle aérienne ?", "Le tronçon Anvers ↔ La Chapelle de la M2 est <strong>aérien sur viaduc</strong> pour franchir la déclivité de Montmartre. Jaurès est sur ce tronçon aérien — vue magnifique sur le canal de l'Ourcq depuis les quais."),
            ("Qui est Jean Jaurès ?", "<strong>Jean Jaurès</strong> (1859-1914), <strong>homme politique français</strong>, <strong>fondateur du Parti socialiste français unifié (SFIO)</strong> en 1905. <strong>Pacifiste</strong>. <strong>Assassiné le 31 juillet 1914</strong> au café du Croissant, 3 jours avant la Première Guerre mondiale."),
            ("Qu'est-ce que le bassin de la Villette ?", "<strong>15 hectares</strong> d'eau, <strong>port de plaisance Paris-Arsenal</strong>, partie du canal de l'Ourcq. Revitalisé dans les années 2010 : péniches restaurants, MK2 cinéma de plein air, jeux nautiques."),
            ("Comment aller à Châtelet ?", "<strong>M7bis vers Louis Blanc + M7</strong> : ~16 min."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Stations historiques 1903-1942.")
        ],
        "tips": [
            "<strong>Vue aérienne</strong> depuis les quais M2 — canal de l'Ourcq et bassin de la Villette.",
            "<strong>Bassin de la Villette</strong> à 5 min — péniches restaurants, cinéma plein air.",
            "<strong>Rotonde de la Villette</strong> (Ledoux 1788) à 10 min — restaurant chic.",
            "Pour <strong>Stalingrad</strong> : M2 ou M5 directe (1 station).",
            "Pour <strong>Châtelet</strong> : M7bis vers Louis Blanc + M7."
        ],
        "trivia": [
            ("🌉", "Vue aérienne sur le canal de l'Ourcq", "La station <strong>M2 à Jaurès est aérienne sur viaduc</strong>, configuration unique pour traverser la déclivité de Montmartre. Vue spectaculaire depuis les quais : <strong>canal de l'Ourcq</strong>, <strong>bassin de la Villette</strong> (15 ha de port de plaisance), <strong>Rotonde de la Villette</strong> (Ledoux 1788), et l'<strong>est parisien</strong>. Photographies emblématiques du métro parisien."),
            ("✊", "Jean Jaurès — assassiné 3 jours avant la guerre 1914", "<strong>Jean Jaurès</strong> (1859-1914), <strong>fondateur du Parti socialiste français unifié (SFIO)</strong>, est l'une des figures les plus marquantes du socialisme français. <strong>Orateur exceptionnel</strong>, <strong>pacifiste convaincu</strong>, il s'est opposé à la <strong>Première Guerre mondiale</strong> jusqu'à son dernier souffle. <strong>Assassiné le 31 juillet 1914</strong> à 21h40 au café du Croissant (rue Montmartre) par <strong>Raoul Villain</strong> (nationaliste). <strong>3 jours avant le déclenchement de la Première Guerre mondiale</strong> (3 août 1914). Panthéonisé en 1924.")
        ],
        "itin": [
            ("Stalingrad via M2", "stalingrad", "M2", "M2 direction Porte Dauphine (1 station)", 2),
            ("Châtelet via M7bis + M7", "chatelet", "M7bis + M7", "M7bis → Louis Blanc + M7", 16),
            ("Père-Lachaise via M2", "pere-lachaise", "M2", "M2 direction Nation (5 stations)", 11),
            ("Buttes-Chaumont via M7bis", "buttes-chaumont", "M7bis", "M7bis (2 stations boucle)", 4),
            ("Bassin de la Villette", "bassin-villette", "à pied", "5 min sud", 5),
            ("Bobigny via M5", "bobigny", "M5", "M5 direction Bobigny", 20)
        ]
    },
    "bolivar": {
        "addr": "Av. Simón Bolívar / av. Mathurin Moreau, 75019 Paris", "arr": "19e (Paris)",
        "seo": "Station Bolívar : M7bis pure dans le 19e arr., avenue Simón Bolívar. Proche des Buttes-Chaumont. Quartier résidentiel calme du 19e.",
        "tagline": "M7bis — quartier Buttes-Chaumont",
        "hero_desc": "Station <strong>Bolívar</strong> sur la M7bis, ouverte le <strong>18 janvier 1911</strong>. Située dans le <strong>19e arrondissement</strong>, à l'intersection de l'<strong>avenue Simón Bolívar</strong> et de l'avenue Mathurin Moreau. Nommée d'après <strong>Simón Bolívar</strong> (1783-1830), <strong>libérateur de l'Amérique du Sud</strong>. Proche des <strong>Buttes-Chaumont</strong>.",
        "intros": [
            "La station <strong>Bolívar</strong> est située dans le <strong>19e arrondissement de Paris</strong>, à l'intersection de l'<strong>avenue Simón Bolívar</strong> et de l'avenue Mathurin Moreau. Elle est desservie uniquement par la <strong>M7bis</strong> (boucle Louis Blanc ↔ Pré Saint-Gervais), entre <strong>Jaurès</strong> (1 station vers le sud, M2+M5) et <strong>Buttes-Chaumont</strong> (1 station vers le nord). Bus 75.",
            "Ouverte le <strong>18 janvier 1911</strong> avec la branche M7bis (devenue ligne autonome en 1967). Le nom <strong>Bolívar</strong> commémore <strong>Simón Bolívar</strong> (1783-1830), <strong>libérateur de l'Amérique du Sud</strong> et <strong>père fondateur de plusieurs républiques</strong>.",
            "Quartier <strong>résidentiel calme</strong> du 19e, accessible aux Buttes-Chaumont (5 min à pied). Affluence quotidienne modérée."
        ],
        "hist_title": "1911 : M7bis, et Simón Bolívar libérateur",
        "hist": [
            "La station <strong>Bolívar</strong> ouvre le <strong>18 janvier 1911</strong> avec la <strong>branche annexe M7bis</strong> (Louis Blanc ↔ Pré Saint-Gervais, à l'époque branche M7).",
            "Le <strong>3 décembre 1967</strong>, la M7bis devient une <strong>ligne autonome</strong>.",
            "Le nom <strong>Bolívar</strong> commémore <strong>Simón Bolívar</strong> (1783-1830), <strong>libérateur de l'Amérique du Sud</strong>. <strong>Né à Caracas (Venezuela)</strong>, il mène les <strong>guerres d'indépendance</strong> contre l'empire espagnol (1810-1825) et libère <strong>Venezuela, Colombie, Équateur, Pérou, Bolivie</strong> (qui porte son nom). <strong>Père fondateur de la « Grande Colombie »</strong> (1819-1830), république unifiée éphémère.",
            "L'avenue <strong>Simón Bolívar</strong> a été ouverte au XIXe siècle dans le 19e arrondissement, dans le cadre du développement urbain post-Haussmann. Renommée en hommage au libérateur lors d'une période de relations diplomatiques renforcées entre la France et l'Amérique latine.",
            "Quartier autour : <strong>résidentiel calme</strong> du 19e, proche des Buttes-Chaumont (5 min à pied). Commerces de proximité, peu d'attractions touristiques majeures."
        ],
        "faq": [
            ("Quelle ligne dessert Bolívar ?", "Uniquement la <strong>M7bis</strong>. Bus 75."),
            ("Qui est Simón Bolívar ?", "<strong>Simón Bolívar</strong> (1783-1830), <strong>libérateur de l'Amérique du Sud</strong>. Mena les guerres d'indépendance contre l'empire espagnol (1810-1825). Libéra Venezuela, Colombie, Équateur, Pérou, Bolivie. Père fondateur de la « Grande Colombie »."),
            ("Comment aller aux Buttes-Chaumont ?", "<strong>M7bis directe</strong> : 1 station vers le nord (~2 min) OU 5 min à pied."),
            ("Comment aller à Châtelet ?", "<strong>M7bis vers Louis Blanc + M7</strong> : ~14 min."),
            ("Comment aller à Jaurès ?", "<strong>M7bis directe</strong> : 1 station vers le sud (~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station historique 1911.")
        ],
        "tips": [
            "<strong>Buttes-Chaumont</strong> à 5 min à pied — parc emblématique du 19e.",
            "Pour <strong>Jaurès</strong> (M2+M5+M7bis) : M7bis directe (1 station).",
            "Pour <strong>Châtelet</strong> : M7bis → Louis Blanc + M7.",
            "Quartier résidentiel calme — peu de commerces immédiats.",
            "Avenue Simón Bolívar — large axe résidentiel."
        ],
        "trivia": [
            ("🇻🇪", "Simón Bolívar (1783-1830) — libérateur de l'Amérique du Sud", "<strong>Simón Bolívar</strong> (1783-1830), <strong>né à Caracas (Venezuela)</strong>, est le <strong>libérateur de l'Amérique du Sud</strong>. Mène les <strong>guerres d'indépendance</strong> contre l'empire espagnol (1810-1825). Libère <strong>Venezuela, Colombie, Équateur, Pérou, Bolivie</strong> (qui porte son nom). <strong>Père fondateur de la « Grande Colombie »</strong> (1819-1830), république unifiée éphémère. Considéré comme l'un des plus grands libérateurs de l'histoire avec Garibaldi et Washington. <strong>Mort à Santa Marta en 1830</strong> dans la pauvreté et la déception (la Grande Colombie se désagrégeait). Statue équestre dans la plupart des capitales sud-américaines.")
        ],
        "itin": [
            ("Buttes-Chaumont via M7bis", "buttes-chaumont", "M7bis", "M7bis (1 station)", 2),
            ("Jaurès via M7bis", "jaures", "M7bis", "M7bis (1 station)", 2),
            ("Châtelet via M7bis + M7", "chatelet", "M7bis + M7", "M7bis → Louis Blanc + M7", 14),
            ("Place des Fêtes via M7bis", "place-des-fetes", "M7bis", "M7bis (3 stations boucle)", 6),
            ("Stalingrad via M7bis + M2", "stalingrad", "M7bis + M2", "M7bis → Jaurès + M2", 4),
            ("Parc des Buttes-Chaumont", "parc-buttes-chaumont", "à pied", "5 min nord-est", 5)
        ]
    },
    "buttes-chaumont": {
        "addr": "Av. Simón Bolívar / Av. Mathurin Moreau, 75019 Paris", "arr": "19e (Paris)",
        "seo": "Station Buttes-Chaumont : M7bis pure dans le 19e arr., accès direct au Parc des Buttes-Chaumont (5e plus grand parc parisien, Haussmann/Alphand 1867, Temple de la Sibylle).",
        "tagline": "M7bis — Parc des Buttes-Chaumont (Haussmann 1867)",
        "hero_desc": "Station <strong>Buttes-Chaumont</strong> ouverte le <strong>18 janvier 1911</strong> avec la M7bis. Située dans le <strong>19e arrondissement</strong>, dessert le <strong>Parc des Buttes-Chaumont</strong> à la sortie, <strong>5e plus grand parc intra-muros de Paris</strong> (25 hectares). Créé en <strong>1867</strong> par <strong>Haussmann et le paysagiste Alphand</strong>. Caractéristiques : <strong>lac artificiel</strong>, <strong>île avec falaise de 30 m</strong>, <strong>Temple de la Sibylle</strong> au sommet.",
        "intros": [
            "La station <strong>Buttes-Chaumont</strong> est située dans le <strong>19e arrondissement de Paris</strong>, à l'entrée sud du <strong>Parc des Buttes-Chaumont</strong>. Elle est desservie uniquement par la <strong>M7bis</strong>, entre <strong>Bolívar</strong> (1 station sud) et <strong>Botzaris</strong> (1 station nord-est). Bus 26, 75.",
            "Ouverte le <strong>18 janvier 1911</strong> avec la branche M7bis (devenue ligne autonome en 1967).",
            "À la sortie : le <strong>Parc des Buttes-Chaumont</strong>, l'un des <strong>plus beaux parcs de Paris</strong>. <strong>25 hectares</strong>, créé entre <strong>1864 et 1867</strong> sous <strong>Haussmann</strong> par le paysagiste <strong>Jean-Charles Alphand</strong>. Caractéristiques uniques : <strong>lac artificiel</strong> (~1,5 ha), <strong>île centrale avec falaise de 30 m</strong>, <strong>Temple de la Sibylle</strong> (copie réduite du temple de Tivoli) au sommet de l'île, <strong>cascade artificielle</strong>, <strong>pont suspendu</strong>. Aménagé sur une ancienne carrière de gypse et décharge."
        ],
        "hist_title": "1864-1867 : Haussmann/Alphand sur une ancienne carrière",
        "hist": [
            "La station <strong>Buttes-Chaumont</strong> ouvre le <strong>18 janvier 1911</strong> avec la branche M7bis (Louis Blanc ↔ Pré Saint-Gervais). M7bis devient ligne autonome en 1967.",
            "Le <strong>Parc des Buttes-Chaumont</strong> est l'un des <strong>parcs les plus emblématiques de Paris</strong>. <strong>25 hectares</strong>, créé entre <strong>1864 et 1867</strong> sous <strong>Haussmann</strong> dans le cadre des grands aménagements parisiens de Napoléon III, par le paysagiste <strong>Jean-Charles Alphand</strong> (1817-1891, ingénieur en chef des promenades de Paris).",
            "<strong>Tour de force technique</strong> : aménagé sur une <strong>ancienne carrière de gypse</strong> (XVIIe-XIXe) et une <strong>décharge</strong>. Le site, autrefois lugubre et qualifié de <em>« mont chauve »</em> (d'où Chaumont), est transformé en parc paysager spectaculaire.",
            "Éléments caractéristiques : <strong>lac artificiel</strong> (~1,5 ha) creusé par Alphand, <strong>île centrale avec falaise rocheuse de 30 m</strong>, <strong>Temple de la Sibylle</strong> (1867) au sommet de l'île — copie réduite du <strong>temple de Vesta à Tivoli (Italie)</strong>, <strong>cascade artificielle</strong> alimentée par le canal de l'Ourcq, <strong>pont suspendu</strong>, <strong>pont des Suicidés</strong> (filets de sécurité installés au XXe).",
            "Inauguré le <strong>1er avril 1867</strong> pour l'<strong>Exposition universelle</strong> de Paris. <strong>5e plus grand parc intra-muros de Paris</strong> (après les Bois de Boulogne et Vincennes périphériques, puis Tuileries et Luxembourg pour les jardins centraux historiques). Très fréquenté par les habitants du 19e et touristes parisiens."
        ],
        "faq": [
            ("Quelle ligne dessert Buttes-Chaumont ?", "Uniquement la <strong>M7bis</strong>. Bus 26, 75."),
            ("Qu'est-ce que les Buttes-Chaumont ?", "<strong>Parc paysager de 25 hectares</strong> dans le 19e arrondissement de Paris. Créé entre <strong>1864 et 1867</strong> sous Haussmann par le paysagiste <strong>Alphand</strong>. <strong>Tour de force technique</strong> : aménagé sur une ancienne carrière de gypse et décharge."),
            ("Qu'est-ce que le Temple de la Sibylle ?", "<strong>Temple antique</strong> situé au sommet de l'île du lac. <strong>Copie réduite du temple de Vesta à Tivoli (Italie)</strong>. Construit en 1867 pour l'Exposition universelle. Lieu romantique emblématique."),
            ("Comment accéder au parc ?", "Sortie directe de la station — entrée sud du parc. Le parc a 5 entrées au total. Ouvert tous les jours, gratuit. Horaires variables selon saison."),
            ("Comment aller à Châtelet ?", "<strong>M7bis vers Louis Blanc + M7</strong> : ~14 min."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station historique 1911.")
        ],
        "tips": [
            "<strong>Parc des Buttes-Chaumont</strong> à la sortie — l'un des plus beaux parcs de Paris.",
            "<strong>Temple de la Sibylle</strong> au sommet de l'île — montée 10 min, vue panoramique.",
            "<strong>Cascade artificielle</strong> et grotte aménagée à visiter.",
            "Pour <strong>Châtelet</strong> : M7bis → Louis Blanc + M7.",
            "Pour <strong>Stalingrad</strong> : M7bis → Jaurès + M2."
        ],
        "trivia": [
            ("🌳", "Parc des Buttes-Chaumont — sur une ancienne carrière (1867)", "Le <strong>Parc des Buttes-Chaumont</strong> à la sortie de la station est l'un des <strong>plus emblématiques de Paris</strong>. <strong>25 hectares</strong>, créé entre <strong>1864 et 1867</strong> sous <strong>Haussmann</strong> par le paysagiste <strong>Jean-Charles Alphand</strong>. <strong>Tour de force technique</strong> : aménagé sur une <strong>ancienne carrière de gypse</strong> et une <strong>décharge</strong>. Le site, autrefois lugubre (« mont chauve », d'où Chaumont), est transformé en parc paysager spectaculaire. <strong>Inauguré le 1er avril 1867 pour l'Exposition universelle</strong> de Paris. Lac artificiel de 1,5 ha, île avec falaise de 30 m, Temple de la Sibylle au sommet, cascade artificielle."),
            ("🏛️", "Temple de la Sibylle (1867) — copie de Tivoli", "Au sommet de l'île centrale du lac, le <strong>Temple de la Sibylle</strong> est l'un des éléments les plus reconnaissables du parc. <strong>Copie réduite du temple de Vesta à Tivoli</strong> (près de Rome, Italie). Construit en <strong>1867</strong> pour l'<strong>Exposition universelle</strong>. <strong>10 colonnes corinthiennes</strong> en pierre artificielle. Sommet à <strong>30 m au-dessus du lac</strong>. Vue panoramique sur le parc, le 19e arrondissement et l'est parisien. Lieu romantique emblématique des promenades parisiennes.")
        ],
        "itin": [
            ("Parc des Buttes-Chaumont (entrée sud)", "parc-buttes-chaumont", "à pied", "Sortie directe", 1),
            ("Temple de la Sibylle", "temple-sibylle", "à pied", "Au sommet de l'île (10 min depuis entrée)", 10),
            ("Châtelet via M7bis + M7", "chatelet", "M7bis + M7", "M7bis → Louis Blanc + M7", 14),
            ("Jaurès via M7bis", "jaures", "M7bis", "M7bis (2 stations)", 4),
            ("Place des Fêtes via M7bis", "place-des-fetes", "M7bis", "M7bis (2 stations)", 4),
            ("Botzaris via M7bis", "botzaris", "M7bis", "M7bis (1 station)", 2)
        ]
    },
    "botzaris": {
        "addr": "Av. Mathurin Moreau / rue Botzaris, 75019 Paris", "arr": "19e (Paris)",
        "seo": "Station Botzaris : M7bis pure dans le 19e arr., sud-est du parc des Buttes-Chaumont. Nommée d'après Markos Botzaris, héros grec de l'indépendance.",
        "tagline": "M7bis — sud-est Buttes-Chaumont",
        "hero_desc": "Station <strong>Botzaris</strong> ouverte le <strong>18 janvier 1911</strong> avec la M7bis. Située dans le <strong>19e arrondissement</strong>, dessert le <strong>sud-est du Parc des Buttes-Chaumont</strong> et le quartier <strong>Mouzaïa</strong>. Nommée d'après <strong>Markos Botzaris</strong> (1788-1823), héros grec de la guerre d'indépendance hellénique.",
        "intros": [
            "La station <strong>Botzaris</strong> est située dans le <strong>19e arrondissement de Paris</strong>, à l'intersection de l'avenue Mathurin Moreau et de la rue Botzaris. Elle est desservie uniquement par la <strong>M7bis</strong>, entre <strong>Buttes-Chaumont</strong> (1 station sud-ouest) et <strong>Place des Fêtes</strong> (1 station est). Bus 26, 60.",
            "Ouverte le <strong>18 janvier 1911</strong> avec la branche M7bis. Le nom <strong>Botzaris</strong> commémore <strong>Markos Botzaris</strong> (1788-1823), <strong>héros de la guerre d'indépendance grecque</strong> contre l'Empire ottoman. Statue à Athènes.",
            "Le quartier autour est partagé entre l'<strong>accès sud-est au Parc des Buttes-Chaumont</strong> (5 min) et le <strong>quartier Mouzaïa</strong> (10 min) — quartier remarquable pour ses <strong>petites maisons individuelles</strong>, configuration urbaine rare à Paris."
        ],
        "hist_title": "1911 : M7bis, et Markos Botzaris héros grec",
        "hist": [
            "La station <strong>Botzaris</strong> ouvre le <strong>18 janvier 1911</strong> avec la branche annexe M7bis (Louis Blanc ↔ Pré Saint-Gervais).",
            "Le <strong>3 décembre 1967</strong>, la M7bis devient ligne autonome.",
            "Le nom <strong>Botzaris</strong> commémore <strong>Markos Botzaris</strong> (1788-1823), <strong>héros de la guerre d'indépendance grecque</strong> (1821-1829) contre l'<strong>Empire ottoman</strong>. <strong>Chef souliote</strong> (Souliotes : population guerrière de l'Épire). <strong>Mort héroïquement à la bataille de Karpenissi</strong> le 21 août 1823. Statue à Athènes (place Klaftmonos). <strong>Hommage de la France à la cause grecque</strong>, qui mobilisait largement les intellectuels romantiques européens (Victor Hugo, Lord Byron).",
            "Le quartier autour est partagé entre 2 zones :",
            "- À 5 min : <strong>sud-est du Parc des Buttes-Chaumont</strong>, entrée alternative au parc.",
            "- À 10 min : le <strong>quartier Mouzaïa</strong>, remarquable pour ses <strong>petites maisons individuelles</strong> construites au début du XXe siècle. Configuration urbaine <strong>rare à Paris intra-muros</strong> — habituellement les immeubles haussmanniens dominent. Quartier prisé pour son charme villageois."
        ],
        "faq": [
            ("Quelle ligne dessert Botzaris ?", "Uniquement la <strong>M7bis</strong>. Bus 26, 60."),
            ("Qui est Markos Botzaris ?", "<strong>Markos Botzaris</strong> (1788-1823), <strong>héros de la guerre d'indépendance grecque</strong> contre l'Empire ottoman. <strong>Chef souliote</strong>. <strong>Mort héroïquement à la bataille de Karpenissi</strong> le 21 août 1823. Statue à Athènes."),
            ("Comment accéder aux Buttes-Chaumont ?", "<strong>5 min à pied</strong> direction sud-ouest — entrée sud-est du parc."),
            ("Qu'est-ce que le quartier Mouzaïa ?", "Quartier remarquable pour ses <strong>petites maisons individuelles</strong> construites au début du XXe siècle. <strong>Configuration urbaine rare à Paris intra-muros</strong>. Charme villageois."),
            ("Comment aller à Châtelet ?", "<strong>M7bis vers Louis Blanc + M7</strong> : ~16 min."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station historique 1911.")
        ],
        "tips": [
            "<strong>Sud-est des Buttes-Chaumont</strong> à 5 min — entrée alternative.",
            "<strong>Quartier Mouzaïa</strong> à 10 min — petites maisons rares à Paris.",
            "Pour <strong>Place des Fêtes</strong> (M7bis+M11) : M7bis (1 station).",
            "Pour <strong>Châtelet</strong> : M7bis → Louis Blanc + M7.",
            "Quartier résidentiel calme du 19e."
        ],
        "trivia": [
            ("🇬🇷", "Markos Botzaris (1788-1823) — héros de l'indépendance grecque", "<strong>Markos Botzaris</strong> (1788-1823), <strong>héros de la guerre d'indépendance grecque</strong> contre l'Empire ottoman (1821-1829). <strong>Chef souliote</strong> (Souliotes : population guerrière de l'Épire, en Grèce de l'Ouest). <strong>Mort héroïquement à la bataille de Karpenissi</strong> le 21 août 1823. Statue à Athènes (place Klaftmonos). Sa mort a profondément marqué les intellectuels romantiques européens : <strong>Victor Hugo lui consacre un poème</strong> dans <em>Les Orientales</em> (1829), <strong>Lord Byron</strong> meurt à Missolonghi en 1824 pour la cause grecque. Le nom de la rue Botzaris (1830) symbolise l'engagement français en faveur de l'indépendance grecque."),
            ("🏘️", "Quartier Mouzaïa — petites maisons rares à Paris", "À <strong>10 min</strong> : le <strong>quartier Mouzaïa</strong>, remarquable pour ses <strong>petites maisons individuelles</strong> construites au début du XXe siècle dans le 19e arrondissement. <strong>Configuration urbaine rare à Paris intra-muros</strong> — habituellement dominé par les immeubles haussmanniens. Les maisons Mouzaïa, mitoyennes ou semi-mitoyennes, créent une ambiance <strong>villageoise</strong>. Quartier prisé aujourd'hui, prix immobilier très élevé. Décor de plusieurs films français.")
        ],
        "itin": [
            ("Sud-est Buttes-Chaumont", "buttes-chaumont-sud-est", "à pied", "5 min direct", 5),
            ("Quartier Mouzaïa", "quartier-mouzaia", "à pied", "10 min nord-est", 10),
            ("Buttes-Chaumont via M7bis", "buttes-chaumont", "M7bis", "M7bis (1 station)", 2),
            ("Place des Fêtes via M7bis", "place-des-fetes", "M7bis", "M7bis (1 station)", 2),
            ("Châtelet via M7bis + M7", "chatelet", "M7bis + M7", "M7bis → Louis Blanc + M7", 16),
            ("Jaurès via M7bis", "jaures", "M7bis", "M7bis (3 stations boucle)", 6)
        ]
    },
    "place-des-fetes": {
        "addr": "Place des Fêtes, 75019 Paris", "arr": "19e (Paris)",
        "seo": "Station Place des Fêtes : M7bis + M11 dans le 19e arr. Place des Fêtes (tours d'habitation années 70). Marché alimentaire animé. Quartier populaire du 19e.",
        "tagline": "M7bis + M11 — Place des Fêtes du 19e",
        "hero_desc": "Station <strong>Place des Fêtes</strong> dans le <strong>19e arrondissement</strong>, sous la <strong>Place des Fêtes</strong>. Desservie par <strong>M7bis</strong> (ouverte 18 janvier 1911) et <strong>M11</strong> (ouverte 28 avril 1935). À la sortie : la <strong>Place des Fêtes</strong> elle-même, entourée de <strong>tours d'habitation des années 1970</strong>. <strong>Marché alimentaire</strong> animé 3 jours/semaine. Quartier populaire et multi-culturel du 19e.",
        "intros": [
            "La station <strong>Place des Fêtes</strong> est située dans le <strong>19e arrondissement de Paris</strong>, sous la <strong>Place des Fêtes</strong>. Elle est desservie par <strong>2 lignes</strong> : <strong>M7bis</strong> (boucle Louis Blanc ↔ Pré Saint-Gervais) et <strong>M11</strong> (Châtelet ↔ Rosny - Bois-Perrier). Bus 48, 60, 96.",
            "La station <strong>M7bis</strong> ouvre le <strong>18 janvier 1911</strong> avec la branche M7bis (devenue ligne autonome en 1967). La station <strong>M11</strong> est ajoutée le <strong>28 avril 1935</strong> avec l'ouverture de la M11 originelle (Châtelet ↔ Porte des Lilas).",
            "À la sortie : la <strong>Place des Fêtes</strong> elle-même, place rectangulaire bordée de <strong>tours d'habitation des années 1970</strong> (reconstruction urbanistique brutaliste typique). <strong>Marché alimentaire</strong> animé le mardi, vendredi et dimanche. Quartier populaire et <strong>multi-culturel du 19e</strong>, avec présence des communautés magrébine, africaine et asiatique."
        ],
        "hist_title": "1911 : M7bis, 1935 : M11, et reconstruction années 70",
        "hist": [
            "La <strong>Place des Fêtes</strong> a une histoire singulière. Au <strong>XIXe siècle</strong>, c'était le <strong>cœur du village rural de Belleville</strong>, place où se tenaient les <strong>fêtes patronales et marchés</strong> (d'où le nom). Annexée à Paris en <strong>1860</strong>.",
            "La station <strong>M7bis</strong> ouvre le <strong>18 janvier 1911</strong> avec la branche annexe M7bis. La station <strong>M11</strong> est ajoutée le <strong>28 avril 1935</strong> avec la M11 originelle.",
            "Dans les <strong>années 1960-1970</strong>, la Place des Fêtes subit une <strong>profonde transformation urbanistique</strong>. Le quartier ancien, jugé insalubre, est <strong>partiellement démoli</strong> et reconstruit en <strong>tours d'habitation</strong> selon les principes urbanistiques modernistes. <strong>~3 500 logements</strong> construits, dont plusieurs tours de 25 étages. Cas typique des <strong>Grands Ensembles parisiens</strong> intra-muros, contemporains des quartiers des Olympiades (13e) et de la Goutte d'Or (18e).",
            "Aujourd'hui, le quartier est <strong>populaire et multi-culturel</strong> : présence des communautés <strong>magrébine, africaine et asiatique</strong>, commerces ethniques, restaurants. <strong>Marché alimentaire</strong> animé sur la place (mardi, vendredi, dimanche). Quartier en mutation lente vers la gentrification.",
            "À 5 min à pied : le <strong>Parc des Buttes-Chaumont</strong> (entrée nord-est)."
        ],
        "faq": [
            ("Quelles lignes desservent Place des Fêtes ?", "<strong>M7bis</strong> et <strong>M11</strong>. Bus 48, 60, 96."),
            ("Qu'est-ce que la Place des Fêtes ?", "Place rectangulaire bordée de <strong>tours d'habitation des années 1970</strong> (reconstruction urbanistique brutaliste). <strong>Marché alimentaire</strong> animé 3 jours/semaine (mardi, vendredi, dimanche). Quartier populaire et multi-culturel."),
            ("Pourquoi le nom Place des Fêtes ?", "Au XIXe siècle, c'était la <strong>place centrale du village rural de Belleville</strong>, où se tenaient les <strong>fêtes patronales et marchés</strong>. Annexée à Paris en 1860."),
            ("Comment aller aux Buttes-Chaumont ?", "<strong>5 min à pied</strong> direction sud-ouest — entrée nord-est du parc. Plus rapide : M7bis (2 stations)."),
            ("Comment aller à Châtelet ?", "<strong>M11 directe</strong> : ~16 min (5 stations vers l'ouest)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Stations historiques 1911/1935.")
        ],
        "tips": [
            "<strong>Marché alimentaire</strong> mardi/vendredi/dimanche.",
            "<strong>Buttes-Chaumont</strong> à 5 min à pied OU M7bis (2 stations).",
            "Pour <strong>Châtelet</strong> : M11 directe (~16 min).",
            "Pour <strong>République</strong> : M11 directe (~10 min).",
            "Quartier multi-culturel — restaurants ethniques."
        ],
        "trivia": [
            ("🎪", "Origine villageoise — fêtes patronales de Belleville", "Au <strong>XIXe siècle</strong>, la <strong>Place des Fêtes</strong> était le <strong>cœur du village rural de Belleville</strong>, place où se tenaient les <strong>fêtes patronales et marchés hebdomadaires</strong> (d'où le nom). Belleville était alors une <strong>commune indépendante de Paris</strong>, viticole et populaire. <strong>Annexée à Paris en 1860</strong> par Napoléon III (avec Charonne, Belleville, Grenelle, etc.). Le caractère villageois disparaît progressivement avec l'urbanisation haussmannienne, puis avec la reconstruction des années 1970."),
            ("🏢", "Tours années 1970 — reconstruction urbanistique brutaliste", "Dans les <strong>années 1960-1970</strong>, le quartier ancien autour de la Place des Fêtes est <strong>partiellement démoli</strong> et reconstruit selon les <strong>principes urbanistiques modernistes</strong>. <strong>~3 500 logements</strong> construits, dont plusieurs <strong>tours de 25 étages</strong>. <strong>Architecture brutaliste typique</strong> des Grands Ensembles parisiens intra-muros. Contemporain et similaire au quartier des Olympiades (13e) et à la Goutte d'Or (18e). <strong>Patrimoine urbanistique controversé</strong> : apprécié pour son audace, critiqué pour sa déshumanisation. Programme de rénovation partielle en cours.")
        ],
        "itin": [
            ("Buttes-Chaumont via M7bis", "buttes-chaumont", "M7bis", "M7bis (2 stations)", 4),
            ("Châtelet via M11", "chatelet", "M11", "M11 direction Châtelet (5 stations)", 16),
            ("République via M11", "republique", "M11", "M11 direction Châtelet (3 stations)", 10),
            ("Pré Saint-Gervais via M7bis", "pre-saint-gervais", "M7bis", "M7bis (1 station)", 2),
            ("Porte des Lilas via M11", "porte-des-lilas", "M11", "M11 direction Porte des Lilas (1 station)", 2),
            ("Marché Place des Fêtes", "marche-place-fetes", "à pied", "Sortie directe (mar/ven/dim)", 1)
        ]
    },
    "pre-saint-gervais": {
        "addr": "Rue Manin / rue du Pré-Saint-Gervais, 75019 Paris", "arr": "19e (Paris)",
        "seo": "Station Pré Saint-Gervais : M7bis terminus dans le 19e arr., à la limite de la commune du Pré-Saint-Gervais (93). Réservoir des Lilas à proximité.",
        "tagline": "M7bis — terminus boucle nord-est",
        "hero_desc": "Station <strong>Pré Saint-Gervais</strong> sur la M7bis, ouverte le <strong>18 janvier 1911</strong>. Située dans le <strong>19e arrondissement</strong>, à la limite de la commune du <strong>Pré-Saint-Gervais</strong> (Seine-Saint-Denis, 93). <strong>Terminus traditionnel</strong> de la M7bis (avant la boucle de retournement vers Botzaris). À proximité : le <strong>Réservoir des Lilas</strong> et les hauteurs nord-est de Paris.",
        "intros": [
            "La station <strong>Pré Saint-Gervais</strong> est située dans le <strong>19e arrondissement de Paris</strong>, à la limite de la commune du <strong>Pré-Saint-Gervais</strong> (Seine-Saint-Denis, 93). Elle est desservie uniquement par la <strong>M7bis</strong> (terminus traditionnel avant la boucle), entre <strong>Place des Fêtes</strong> (1 station vers le sud-ouest) et <strong>Danube</strong> (1 station via la boucle). Bus 48, 60, 61, 75.",
            "Ouverte le <strong>18 janvier 1911</strong> avec la branche annexe M7bis (Louis Blanc ↔ Pré Saint-Gervais, configuration historique en cul-de-sac). Devient ligne autonome en 1967.",
            "Le nom commémore la <strong>commune du Pré-Saint-Gervais</strong> (Seine-Saint-Denis 93, ~17 000 habitants), limitrophe du 19e. <strong>Origine villageoise</strong> : ancien village rural agricole. À proximité : le <strong>Réservoir des Lilas</strong>, réservoir d'eau potable de Paris construit en 1865-1869."
        ],
        "hist_title": "1911 : terminus M7bis, et la commune du Pré-Saint-Gervais",
        "hist": [
            "La station <strong>Pré Saint-Gervais</strong> ouvre le <strong>18 janvier 1911</strong> comme <strong>terminus de la branche M7bis</strong> (Louis Blanc ↔ Pré Saint-Gervais). Configuration historique en <strong>cul-de-sac</strong> avec voies de retournement.",
            "Le <strong>3 décembre 1967</strong>, la M7bis devient ligne autonome. Configuration <strong>en boucle</strong> via Botzaris ↔ Danube ajoutée plus tard pour faciliter la circulation.",
            "Le nom commémore la <strong>commune du Pré-Saint-Gervais</strong>, située en Seine-Saint-Denis (93), limitrophe du 19e arrondissement parisien. Commune de <strong>~17 000 habitants</strong>. <strong>Origine villageoise agricole</strong> : « Pré » = prairie, « Saint-Gervais » = patron de l'église locale (Gervais, martyr chrétien du Ier siècle).",
            "À proximité : le <strong>Réservoir des Lilas</strong>, <strong>réservoir d'eau potable de Paris</strong> construit entre <strong>1865 et 1869</strong> sous Haussmann pour alimenter le quartier nord-est. <strong>Capacité : ~110 000 m³</strong>. Encore en service aujourd'hui pour Eau de Paris.",
            "Le quartier autour est <strong>résidentiel calme</strong> du 19e, accessible aux Buttes-Chaumont (10 min). Fréquentation modérée."
        ],
        "faq": [
            ("Quelle ligne dessert Pré Saint-Gervais ?", "Uniquement la <strong>M7bis</strong> (terminus traditionnel avant la boucle Botzaris ↔ Danube). Bus 48, 60, 61, 75."),
            ("Quelle est la commune ?", "À la <strong>limite du 19e arrondissement</strong> et de la commune du <strong>Pré-Saint-Gervais</strong> (Seine-Saint-Denis 93, ~17 000 habitants)."),
            ("Pourquoi le nom Pré Saint-Gervais ?", "« Pré » = prairie (origine villageoise agricole). « Saint-Gervais » = <strong>patron de l'église locale</strong> (Gervais, martyr chrétien du Ier siècle, fêté avec son frère Protais le 19 juin). Commune historique."),
            ("Qu'est-ce que le Réservoir des Lilas ?", "<strong>Réservoir d'eau potable de Paris</strong> construit entre <strong>1865 et 1869</strong> sous Haussmann pour alimenter le quartier nord-est. <strong>~110 000 m³</strong>. Encore en service aujourd'hui (Eau de Paris)."),
            ("Comment aller à Châtelet ?", "<strong>M7bis vers Louis Blanc + M7</strong> : ~18 min."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station historique 1911.")
        ],
        "tips": [
            "<strong>Commune du Pré-Saint-Gervais (93)</strong> à 5 min — village historique.",
            "<strong>Réservoir des Lilas</strong> à 10 min — patrimoine industriel.",
            "Pour <strong>Buttes-Chaumont</strong> : M7bis (3 stations boucle).",
            "Pour <strong>Châtelet</strong> : M7bis → Louis Blanc + M7.",
            "Quartier résidentiel calme — peu de commerces touristiques."
        ],
        "trivia": [
            ("💧", "Réservoir des Lilas (1865-1869) — patrimoine hydraulique", "À <strong>10 min</strong> de la station, le <strong>Réservoir des Lilas</strong> est l'un des <strong>réservoirs d'eau potable historiques de Paris</strong>. Construit entre <strong>1865 et 1869</strong> sous <strong>Haussmann</strong> dans le cadre de la <strong>modernisation du réseau d'eau parisien</strong> (Aqueduc de la Dhuis, Aqueduc de la Vanne). <strong>Capacité : ~110 000 m³</strong>. Encore <strong>en service aujourd'hui</strong> par Eau de Paris. Bâtiment industriel partiellement classé. Témoin de l'<strong>ingénierie hydraulique du Second Empire</strong>."),
            ("🚇", "Configuration M7bis : terminus + boucle (1967)", "<strong>Pré Saint-Gervais</strong> est le <strong>terminus traditionnel</strong> de la M7bis depuis 1911 (configuration originelle Louis Blanc ↔ Pré Saint-Gervais en cul-de-sac). En <strong>1967</strong>, la M7bis devient ligne autonome et adopte une <strong>configuration en boucle</strong> : les trains poursuivent depuis Pré Saint-Gervais vers <strong>Danube</strong> et <strong>Place des Fêtes</strong> avant de revenir vers Louis Blanc. <strong>Cas unique du réseau parisien</strong>.")
        ],
        "itin": [
            ("Châtelet via M7bis + M7", "chatelet", "M7bis + M7", "M7bis → Louis Blanc + M7", 18),
            ("Buttes-Chaumont via M7bis", "buttes-chaumont", "M7bis", "M7bis boucle (3 stations)", 6),
            ("Place des Fêtes via M7bis", "place-des-fetes", "M7bis", "M7bis (1 station)", 2),
            ("Commune du Pré-Saint-Gervais", "pre-saint-gervais-commune", "à pied", "5 min direct", 5),
            ("Réservoir des Lilas", "reservoir-lilas", "à pied", "10 min direct", 10),
            ("Stalingrad via M7bis + M2", "stalingrad", "M7bis + M2", "M7bis → Jaurès + M2", 12)
        ]
    },
    "danube": {
        "addr": "Rue de la Mouzaïa / rue de Crimée, 75019 Paris", "arr": "19e (Paris)",
        "seo": "Station Danube : M7bis pure dans le 19e arr. Quartier Mouzaïa (petites maisons rares à Paris). Rue Miguel-Hidalgo et villas pavillonnaires.",
        "tagline": "M7bis — quartier Mouzaïa pavillonnaire",
        "hero_desc": "Station <strong>Danube</strong> ouverte le <strong>18 janvier 1911</strong> avec la M7bis. Située dans le <strong>19e arrondissement</strong>, à l'intersection de la rue de la Mouzaïa et de la rue de Crimée. Dessert le <strong>quartier Mouzaïa</strong>, remarquable pour ses <strong>petites maisons individuelles</strong> et <strong>villas pavillonnaires</strong> — configuration urbaine rare à Paris intra-muros. Nom du <strong>fleuve Danube</strong> (Europe centrale).",
        "intros": [
            "La station <strong>Danube</strong> est située dans le <strong>19e arrondissement de Paris</strong>, à l'intersection de la <strong>rue de la Mouzaïa</strong> et de la rue de Crimée. Elle est desservie uniquement par la <strong>M7bis</strong>, entre <strong>Pré Saint-Gervais</strong> (1 station via la boucle) et <strong>Botzaris</strong> (1 station via la boucle). Bus 60, 75.",
            "Ouverte le <strong>18 janvier 1911</strong> avec la branche annexe M7bis. Le nom <strong>Danube</strong> vient du <strong>fleuve Danube</strong> (2 850 km, Europe centrale), qui traverse 10 pays — l'un des plus longs fleuves d'Europe.",
            "La station dessert le <strong>quartier Mouzaïa</strong>, remarquable pour ses <strong>petites maisons individuelles</strong> et <strong>villas pavillonnaires</strong> construites au début du XXe siècle. <strong>Configuration urbaine rare à Paris intra-muros</strong> — habituellement les immeubles haussmanniens et grands ensembles dominent. <strong>Rue Miguel-Hidalgo</strong> (nommée d'après le père de l'indépendance mexicaine, 1753-1811) est l'une des plus emblématiques du quartier."
        ],
        "hist_title": "Le quartier Mouzaïa — maisons rares à Paris",
        "hist": [
            "La station <strong>Danube</strong> ouvre le <strong>18 janvier 1911</strong> avec la branche annexe M7bis (Louis Blanc ↔ Pré Saint-Gervais). M7bis devient ligne autonome en 1967.",
            "Le nom <strong>Danube</strong> vient du <strong>fleuve Danube</strong> (2 850 km, Europe centrale, traverse Allemagne, Autriche, Slovaquie, Hongrie, Croatie, Serbie, Bulgarie, Roumanie, Moldavie, Ukraine). L'un des plus longs fleuves d'Europe.",
            "La station dessert le <strong>quartier Mouzaïa</strong>, remarquable urbanistiquement. Au début du XXe siècle, ce secteur de l'ancien village de Belleville (annexé à Paris en 1860) a été <strong>partiellement loti en petites parcelles</strong> pour des <strong>maisons individuelles et villas pavillonnaires</strong>. Concept urbanistique alors original à Paris, inspiré du <strong>mouvement des cités-jardins</strong> britanniques (Ebenezer Howard).",
            "<strong>~250 maisons individuelles</strong> sur le quartier, sur des rues étroites et calmes. <strong>Rue Miguel-Hidalgo</strong>, <strong>villa du Progrès</strong>, <strong>villa des Lilas</strong>, etc. Plusieurs ont des <strong>jardinets</strong>, configuration <strong>quasi-rurale</strong> au sein de Paris.",
            "Aujourd'hui, le <strong>quartier Mouzaïa est très prisé</strong> par les habitants parisiens cherchant un cadre de vie atypique. <strong>Prix immobilier très élevé</strong> (~10 000 €/m² malgré la périphérie). Lieu de tournage de plusieurs films français. Charme villageois exceptionnel."
        ],
        "faq": [
            ("Quelle ligne dessert Danube ?", "Uniquement la <strong>M7bis</strong>. Bus 60, 75."),
            ("Pourquoi le nom Danube ?", "Du <strong>fleuve Danube</strong> (2 850 km, Europe centrale), l'un des plus longs fleuves d'Europe. La rue Danube et la rue voisine de la Mouzaïa ont été baptisées au XIXe siècle avec des noms géographiques européens (Crimée, Bessarabie, etc.)."),
            ("Qu'est-ce que le quartier Mouzaïa ?", "<strong>Quartier remarquable</strong> pour ses <strong>petites maisons individuelles</strong> et <strong>villas pavillonnaires</strong> construites au début du XXe siècle. <strong>~250 maisons</strong> sur des rues étroites. <strong>Configuration urbaine rare à Paris intra-muros</strong>. Charme quasi-rural. Très prisé aujourd'hui."),
            ("Qui est Miguel Hidalgo ?", "<strong>Miguel Hidalgo y Costilla</strong> (1753-1811), prêtre catholique mexicain. <strong>Père fondateur de l'indépendance du Mexique</strong> (cri de Dolores, 16 septembre 1810). Exécuté en 1811. <strong>Héros national mexicain</strong>. La rue Miguel-Hidalgo à Paris commémore l'amitié franco-mexicaine."),
            ("Comment aller aux Buttes-Chaumont ?", "<strong>M7bis directe</strong> : 2 stations (~4 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station historique 1911.")
        ],
        "tips": [
            "<strong>Quartier Mouzaïa</strong> à pied — petites maisons et villas rares à Paris.",
            "<strong>Rue Miguel-Hidalgo</strong> à pied — l'une des plus charmantes du quartier.",
            "<strong>Villas pavillonnaires</strong> — promenade urbanistique unique.",
            "Pour <strong>Buttes-Chaumont</strong> : M7bis (2 stations).",
            "Pour <strong>Châtelet</strong> : M7bis → Louis Blanc + M7."
        ],
        "trivia": [
            ("🏘️", "Quartier Mouzaïa — cités-jardins parisiennes (XXe)", "Le <strong>quartier Mouzaïa</strong> autour de la station Danube est l'un des quartiers les plus <strong>urbanistiquement remarquables de Paris intra-muros</strong>. Au début du XXe siècle, ce secteur a été <strong>loti en petites parcelles</strong> pour des <strong>maisons individuelles et villas pavillonnaires</strong>. Concept inspiré du <strong>mouvement des cités-jardins britanniques</strong> (Ebenezer Howard, 1898). <strong>~250 maisons</strong> sur rues étroites : <strong>rue Miguel-Hidalgo, villa du Progrès, villa des Lilas</strong>, etc. <strong>Configuration urbaine rare à Paris</strong> (habituellement dominé par les immeubles haussmanniens). Très prisé aujourd'hui (~10 000 €/m²). Charme quasi-rural."),
            ("🇲🇽", "Miguel Hidalgo (1753-1811) — père de l'indépendance mexicaine", "La <strong>rue Miguel-Hidalgo</strong> emblématique du quartier Mouzaïa commémore <strong>Miguel Hidalgo y Costilla</strong> (1753-1811), <strong>prêtre catholique mexicain</strong>. <strong>Père fondateur de l'indépendance du Mexique</strong> : le <strong>16 septembre 1810</strong>, il lance le <strong>« Cri de Dolores »</strong> appelant à la révolte contre la couronne espagnole — événement fondateur de la nation mexicaine, <strong>fête nationale du Mexique</strong>. <strong>Exécuté en 1811</strong> par les royalistes. <strong>Héros national mexicain</strong>. Statue à Mexico (Monumento de la Independencia).")
        ],
        "itin": [
            ("Buttes-Chaumont via M7bis", "buttes-chaumont", "M7bis", "M7bis (2 stations boucle)", 4),
            ("Pré Saint-Gervais via M7bis", "pre-saint-gervais", "M7bis", "M7bis (1 station)", 2),
            ("Châtelet via M7bis + M7", "chatelet", "M7bis + M7", "M7bis → Louis Blanc + M7", 18),
            ("Place des Fêtes via M7bis", "place-des-fetes", "M7bis", "M7bis (2 stations boucle)", 4),
            ("Rue Miguel-Hidalgo", "rue-miguel-hidalgo", "à pied", "5 min direct", 5),
            ("Botzaris via M7bis", "botzaris", "M7bis", "M7bis (1 station)", 2)
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
        d["tariff_zone"] = 1
        d["tariff_zone_context"] = "Paris intra-muros"
        d["commune"] = "Paris"
    else:
        d["tariff_zone"] = 2
        d["tariff_zone_context"] = "Première couronne (zone 2)"
        d["commune"] = c["arr"].split(" (")[0]
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
    if not d.get("services"):
        d["services"] = {
            "wifi": {"available": False, "location_detail": "", "coverage_detail": ""},
            "toilets": {"public_paid": {"available": False}, "public_free": {"available": False, "location": "", "access": ""}},
            "atm": {"available": True, "banks_count_estimate": "rares", "locations": []},
            "ratp_office": {"available": False, "location": "", "services": ""},
            "left_luggage": {"ratp_available": False, "third_party": []},
            "shopping_dining": {"main_location": "", "details": "Commerces de quartier autour.", "secondary": ""}
        }
    if not d.get("safety") or not d.get("safety", {}).get("tips"):
        d["safety"] = {
            "audit_status": "pending", "audit_date": None, "level": "", "agents": None, "police": None,
            "tips": ["Station historique du métro parisien — vigilance pickpockets standard.", "Affluence variable selon heures de pointe."],
            "notes": "Audit RATP/IDFM spécifique non disponible."
        }
    if not d.get("accessibility"):
        d["accessibility"] = {
            "audit_status": "pending", "audit_date": None, "level": "",
            "stats": {"elevators_count": 0, "accessible_lines": 0, "total_lines": len(d.get("lines",[]))},
            "details": "Accessibilité PMR partielle (stations historiques)."
        }
    p.write_text(json.dumps(d, indent=4, ensure_ascii=False) + "\n")
    print(f"✓ {slug}")

if __name__ == "__main__":
    for slug, c in CONTENT.items():
        try: enrich(slug, c)
        except Exception as e: print(f"✗ {slug}: {e}", file=sys.stderr)
