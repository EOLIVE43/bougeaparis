#!/usr/bin/env python3
"""Enrichit M7 — 25 stations T0 (biographies sensibles neutralisées)."""
import json
from pathlib import Path
ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    "la-courneuve-8-mai-1945": {
        "addr": "Avenue Roger-Salengro, 93120 La Courneuve", "arr": "La Courneuve (93)",
        "seo": "Station La Courneuve - 8 Mai 1945, terminus nord M7 à La Courneuve (93). Tramway T1 en correspondance.",
        "tagline": "M7 — terminus nord, La Courneuve",
        "hero_desc": "Station <strong>La Courneuve - 8 Mai 1945</strong>, <strong>terminus nord de la M7</strong>, à <strong>La Courneuve</strong> (Seine-Saint-Denis, 93). Ouverte le <strong>6 mai 1987</strong>. Correspondance <strong>tramway T1</strong>.",
        "intros": [
            "La station <strong>La Courneuve - 8 Mai 1945</strong> est <strong>terminus nord de la M7</strong>, située à <strong>La Courneuve</strong> (Seine-Saint-Denis, 93). Bus 150, 152, 250, 251, tramway T1.",
            "Ouverte le <strong>6 mai 1987</strong> avec le <strong>prolongement de la M7</strong> de <strong>Fort d'Aubervilliers à La Courneuve</strong>.",
            "Le nom rappelle la <strong>date du 8 mai 1945</strong>, fin de la Seconde Guerre mondiale en Europe. À proximité : le <strong>parc départemental Georges-Valbon</strong> (anciennement parc de la Courneuve), <strong>2e plus grand parc d'Île-de-France</strong> (~417 hectares)."
        ],
        "hist_title": "1987 : terminus nord M7",
        "hist": [
            "La station est <strong>inaugurée le 6 mai 1987</strong> avec le <strong>prolongement de la M7</strong> de <strong>Fort d'Aubervilliers à La Courneuve - 8 Mai 1945</strong>.",
            "Le nom rappelle la <strong>date du 8 mai 1945</strong>, jour de la <strong>signature de la capitulation allemande</strong> à Reims, marquant la <strong>fin de la Seconde Guerre mondiale en Europe</strong>.",
            "<strong>La Courneuve</strong> (~40 000 habitants), commune de la <strong>Seine-Saint-Denis</strong>. À proximité : le <strong>parc départemental Georges-Valbon</strong> (~417 hectares), <strong>2e plus grand parc d'Île-de-France</strong> après le Bois de Boulogne. <strong>Tramway T1</strong> en correspondance."
        ],
        "faq": [
            ("Quelles lignes desservent La Courneuve - 8 Mai 1945 ?", "<strong>M7</strong> (terminus nord) + <strong>tramway T1</strong>. Bus 150, 152, 250, 251."),
            ("Quand a-t-elle ouvert ?", "Le <strong>6 mai 1987</strong>."),
            ("Pour le parc Georges-Valbon ?", "<strong>~5 min à pied</strong>. ~417 hectares, 2e plus grand parc IDF."),
            ("Pour Paris centre ?", "<strong>M7 directe</strong> vers Châtelet (~25 min)."),
            ("Pour Saint-Denis ?", "<strong>Tramway T1</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Parc Georges-Valbon</strong> à 5 min : 2e plus grand parc d'Île-de-France.",
            "<strong>Tramway T1</strong> en correspondance.",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong> (~25 min).",
            "Pour <strong>Stade de France</strong> : T1 ou bus.",
            "Zone tarifaire <strong>3</strong>, Seine-Saint-Denis."
        ],
        "trivia": [
            ("🌳", "Parc Georges-Valbon, 417 hectares", "Le <strong>parc départemental Georges-Valbon</strong>, à 5 min à pied, est le <strong>2e plus grand parc d'Île-de-France</strong> après le Bois de Boulogne. <strong>417 hectares</strong>. Anciennement <strong>parc départemental de la Courneuve</strong>, renommé en hommage à <strong>Georges Valbon</strong> (1924-2007), <strong>maire de Bobigny</strong>. Lac, allées, parcours sportifs, équipements de loisirs."),
            ("🚊", "Tramway T1 historique", "Le <strong>tramway T1</strong>, en correspondance, est le <strong>premier tramway moderne d'Île-de-France</strong>. <strong>Inauguré le 6 juillet 1992</strong> entre Bobigny - Pablo Picasso et Saint-Denis. <strong>~270 000 voyageurs/jour</strong>. Dessert plusieurs communes de la Seine-Saint-Denis et les Hauts-de-Seine.")
        ],
        "itin": [
            ("Parc Georges-Valbon", "la-courneuve-8-mai-1945", "à pied", "Sortie + 5 min", 5),
            ("Tramway T1", "la-courneuve-8-mai-1945", "T1", "Correspondance directe", 1),
            ("Stade de France", "stade-de-france-saint-denis", "T1 + RER", "T1 + RER B", 15),
            ("Châtelet", "chatelet", "M7", "M7 directe (~25 min)", 25),
            ("Opéra", "opera", "M7", "M7 directe (~22 min)", 22),
            ("Gare de l'Est", "gare-de-l-est", "M7", "M7 directe (~18 min)", 18)
        ]
    },
    "fort-d-aubervilliers": {
        "addr": "Avenue Jean-Jaurès, 93300 Aubervilliers", "arr": "Aubervilliers (93)",
        "seo": "Station Fort d'Aubervilliers (M7) à Aubervilliers (93). Ancien fort militaire construit en 1843. Cabaret Sauvage à proximité.",
        "tagline": "M7 — Fort d'Aubervilliers, ancien ouvrage Thiers",
        "hero_desc": "Station <strong>Fort d'Aubervilliers</strong> à <strong>Aubervilliers</strong> (Seine-Saint-Denis, 93). Desservie par la <strong>M7</strong>, ouverte le <strong>4 octobre 1979</strong>. À proximité du <strong>Fort d'Aubervilliers</strong> (1843), ancien ouvrage militaire du système Thiers.",
        "intros": [
            "La station <strong>Fort d'Aubervilliers</strong> est implantée à <strong>Aubervilliers</strong> (Seine-Saint-Denis, 93). Elle est desservie par la <strong>M7</strong>, entre <strong>La Courneuve - 8 Mai 1945</strong> (1 station, terminus) et <strong>Aubervilliers - Pantin - Quatre Chemins</strong> (1 station). Bus 150, 152, 234, 250, 251.",
            "Ouverte le <strong>4 octobre 1979</strong> avec le <strong>prolongement de la M7</strong> de <strong>Porte de la Villette à Fort d'Aubervilliers</strong>.",
            "À proximité : le <strong>Fort d'Aubervilliers</strong>, ancien ouvrage militaire construit en <strong>1843</strong> dans le cadre du <strong>système de défense Thiers</strong>. Cet <strong>ensemble de 16 forts</strong> formait une ceinture autour de Paris pour la protéger."
        ],
        "hist_title": "1979 : prolongement et fort Thiers",
        "hist": [
            "La station est <strong>inaugurée le 4 octobre 1979</strong> avec le <strong>prolongement de la M7</strong> de <strong>Porte de la Villette à Fort d'Aubervilliers</strong>.",
            "Le <strong>Fort d'Aubervilliers</strong>, à proximité, est construit en <strong>1843</strong> dans le cadre du <strong>système de défense Thiers</strong>. Cet <strong>ensemble de 16 forts</strong>, conçu par <strong>Adolphe Thiers</strong> (1797-1877, président du Conseil 1840), formait une <strong>ceinture défensive autour de Paris</strong>, à environ <strong>2 km</strong> au-delà de l'enceinte de Thiers (mur de 1841-1845).",
            "Le fort servit lors de la <strong>guerre franco-prussienne de 1870-1871</strong> et de la <strong>Commune de Paris</strong>. <strong>Désaffecté militairement</strong> au XXe siècle. Aujourd'hui, partiellement reconverti en <strong>espaces culturels</strong> et <strong>logements</strong>. Le <strong>Cabaret Sauvage</strong>, salle de concerts emblématique, est à proximité dans le parc de la Villette."
        ],
        "faq": [
            ("Quelle ligne dessert Fort d'Aubervilliers ?", "Uniquement la <strong>M7</strong>. Bus 150, 152, 234, 250, 251."),
            ("Quand a-t-elle ouvert ?", "Le <strong>4 octobre 1979</strong>."),
            ("Qu'est-ce que le Fort d'Aubervilliers ?", "Ancien <strong>ouvrage militaire</strong> construit en <strong>1843</strong> dans le cadre du <strong>système Thiers</strong> (16 forts autour de Paris)."),
            ("Pour le Cabaret Sauvage ?", "<strong>M7 → Porte de la Villette</strong> + à pied (~15 min total)."),
            ("Pour Châtelet ?", "<strong>M7 directe</strong> (~22 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Fort d'Aubervilliers</strong> à proximité : ouvrage Thiers de 1843.",
            "<strong>Cabaret Sauvage</strong> (Villette) : <strong>M7 → Porte de la Villette</strong>.",
            "<strong>Aubervilliers centre</strong> à proximité.",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Seine-Saint-Denis."
        ],
        "trivia": [
            ("🏰", "Système Thiers, 16 forts (1840-1846)", "Le <strong>système Thiers</strong> est un <strong>ensemble de fortifications</strong> protégeant Paris construit de <strong>1840 à 1846</strong> à l'initiative d'<strong>Adolphe Thiers</strong>. <strong>16 forts</strong> (dont Fort d'Aubervilliers, Fort de Romainville, Fort de Vincennes, Fort de Charenton, Fort d'Ivry, Fort de Bicêtre) formant une <strong>ceinture défensive à 2 km</strong> au-delà du <strong>mur d'enceinte de Thiers</strong>. <strong>Démontés progressivement</strong> au XXe siècle après la <strong>cession aux communes</strong> en 1919."),
            ("🎭", "Aubervilliers culturelle", "<strong>Aubervilliers</strong> (~85 000 habitants), commune de la <strong>Seine-Saint-Denis</strong>, accueille plusieurs <strong>institutions culturelles</strong> : <strong>Théâtre de la Commune</strong> (centre dramatique national), <strong>La Maladrerie</strong> (cité d'artistes), <strong>Laboratoires d'Aubervilliers</strong> (art contemporain). Ville en transformation depuis les années 2000, accueillant la <strong>Sorbonne Paris Nord</strong> (campus Condorcet).")
        ],
        "itin": [
            ("Fort d'Aubervilliers", "fort-d-aubervilliers", "à pied", "Sortie directe", 5),
            ("Parc de la Villette", "porte-de-la-villette", "M7", "M7 directe (2 stations)", 5),
            ("La Courneuve - 8 Mai 1945", "la-courneuve-8-mai-1945", "M7", "M7 directe (1 station)", 2),
            ("Gare du Nord", "gare-du-nord", "M7 + à pied", "M7 → Stalingrad + bus", 18),
            ("Châtelet", "chatelet", "M7", "M7 directe (~22 min)", 22),
            ("Opéra", "opera", "M7", "M7 directe (~20 min)", 20)
        ]
    },
    "aubervilliers-pantin-quatre-chemins": {
        "addr": "Avenue Jean-Jaurès, 93500 Pantin", "arr": "Pantin (93)",
        "seo": "Station Aubervilliers - Pantin - Quatre Chemins (M7) à la limite de Pantin et Aubervilliers (93). Hub commerçant des Quatre Chemins.",
        "tagline": "M7 — Quatre Chemins, Aubervilliers/Pantin",
        "hero_desc": "Station <strong>Aubervilliers - Pantin - Quatre Chemins</strong> à la limite de <strong>Pantin</strong> et <strong>Aubervilliers</strong> (Seine-Saint-Denis, 93). Desservie par la <strong>M7</strong>, ouverte le <strong>4 octobre 1979</strong>. Quartier commerçant historique des <strong>Quatre Chemins</strong>.",
        "intros": [
            "La station <strong>Aubervilliers - Pantin - Quatre Chemins</strong> est implantée sur l'<strong>avenue Jean-Jaurès</strong>, à la <strong>limite de Pantin et d'Aubervilliers</strong> (Seine-Saint-Denis, 93). Elle est desservie par la <strong>M7</strong>, entre <strong>Fort d'Aubervilliers</strong> (1 station) et <strong>Porte de la Villette</strong> (1 station). Bus 150, 170, 173, 234, 249, 330.",
            "Ouverte le <strong>4 octobre 1979</strong> avec le <strong>prolongement de la M7</strong> de Porte de la Villette à Fort d'Aubervilliers.",
            "Le nom <strong>Quatre Chemins</strong> rappelle le <strong>carrefour historique</strong> formé par <strong>quatre voies</strong> à la limite des deux communes. Quartier <strong>populaire et commerçant</strong> depuis le XIXe siècle."
        ],
        "hist_title": "1979 : prolongement et carrefour des Quatre Chemins",
        "hist": [
            "La station est <strong>inaugurée le 4 octobre 1979</strong> avec le <strong>prolongement de la M7</strong>.",
            "Le quartier des <strong>Quatre Chemins</strong> tire son nom du <strong>carrefour historique</strong> formé par <strong>quatre voies</strong> à la limite de <strong>Pantin</strong> et d'<strong>Aubervilliers</strong>. Quartier <strong>populaire et commerçant</strong> depuis le <strong>XIXe siècle</strong>.",
            "<strong>Pantin</strong> (~58 000 habitants) et <strong>Aubervilliers</strong> (~85 000 habitants) sont deux communes dynamiques de la <strong>Seine-Saint-Denis</strong>. Quartier en pleine <strong>transformation urbaine</strong> avec de <strong>nouveaux logements</strong> et la <strong>Cité du Cinéma</strong> à proximité."
        ],
        "faq": [
            ("Quelle ligne dessert Aubervilliers - Pantin - Quatre Chemins ?", "Uniquement la <strong>M7</strong>. Bus 150, 170, 173, 234, 249, 330."),
            ("Quand a-t-elle ouvert ?", "Le <strong>4 octobre 1979</strong>."),
            ("Qu'est-ce que le quartier des Quatre Chemins ?", "<strong>Carrefour historique</strong> formé par quatre voies à la limite de Pantin et Aubervilliers. Quartier <strong>populaire et commerçant</strong>."),
            ("Pour Châtelet ?", "<strong>M7 directe</strong> (~20 min)."),
            ("Pour Aubervilliers centre ?", "À courte distance."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Quartier commerçant des Quatre Chemins</strong> : <strong>marchés et commerces multi-ethniques</strong>.",
            "<strong>Aubervilliers</strong> et <strong>Pantin</strong> à proximité.",
            "Pour <strong>Parc de la Villette</strong> : <strong>M7 directe</strong> (1 station).",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong> (~20 min).",
            "Zone tarifaire <strong>3</strong>, Seine-Saint-Denis."
        ],
        "trivia": [
            ("🛍️", "Quatre Chemins, commerce multi-ethnique", "Le quartier des <strong>Quatre Chemins</strong>, à la limite de <strong>Pantin et Aubervilliers</strong>, est un <strong>haut lieu du commerce multi-ethnique</strong> du nord-est parisien. <strong>Marchés à ciel ouvert</strong>, <strong>épiceries asiatiques, africaines, maghrébines</strong>, <strong>fast-foods internationaux</strong>. <strong>Atmosphère cosmopolite</strong> animée."),
            ("🎬", "Cité du Cinéma à proximité", "La <strong>Cité du Cinéma</strong>, à proximité (Saint-Denis - La Plaine), est un <strong>complexe de studios cinématographiques</strong> inauguré en <strong>2012</strong>. Construite par <strong>Luc Besson</strong> dans une <strong>ancienne centrale électrique EDF</strong>. <strong>9 studios de tournage</strong>, écoles de cinéma, post-production. Surface : <strong>62 000 m²</strong>.")
        ],
        "itin": [
            ("Parc de la Villette", "porte-de-la-villette", "M7", "M7 directe (1 station)", 2),
            ("Fort d'Aubervilliers", "fort-d-aubervilliers", "M7", "M7 directe (1 station)", 2),
            ("Stalingrad", "stalingrad", "M7", "M7 directe (3 stations)", 6),
            ("Gare de l'Est", "gare-de-l-est", "M7", "M7 directe (~12 min)", 12),
            ("Châtelet", "chatelet", "M7", "M7 directe (~20 min)", 20),
            ("Opéra", "opera", "M7", "M7 directe (~18 min)", 18)
        ]
    },
    "porte-de-la-villette": {
        "addr": "Avenue Corentin-Cariou, 75019 Paris", "arr": "19e arrondissement (Paris)",
        "seo": "Station Porte de la Villette (M7) avenue Corentin-Cariou dans le 19e. Parc de la Villette, Cité des Sciences et de l'Industrie, Géode.",
        "tagline": "M7 — Parc de la Villette, Cité des Sciences",
        "hero_desc": "Station <strong>Porte de la Villette</strong> sur l'<strong>avenue Corentin-Cariou</strong> dans le <strong>19e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>5 novembre 1910</strong>. À la sortie : le <strong>parc de la Villette</strong>, la <strong>Cité des Sciences et de l'Industrie</strong> et la <strong>Géode</strong>.",
        "intros": [
            "La station <strong>Porte de la Villette</strong> est implantée sur l'<strong>avenue Corentin-Cariou</strong> dans le <strong>19e arrondissement</strong>. Elle est desservie par la <strong>M7</strong>, entre <strong>Aubervilliers - Pantin - Quatre Chemins</strong> (1 station) et <strong>Corentin Cariou</strong> (1 station). Bus 75, 139, 150, 152, tramway T3b.",
            "Ouverte le <strong>5 novembre 1910</strong> avec le tronçon initial de la <strong>M7</strong>.",
            "À la sortie : le <strong>parc de la Villette</strong>, <strong>3e plus grand parc parisien</strong> (~55 hectares), inauguré en <strong>1987</strong> sur les anciennes <strong>halles aux bestiaux et abattoirs de la Villette</strong>. Abrite la <strong>Cité des Sciences et de l'Industrie</strong>, la <strong>Géode</strong>, la <strong>Philharmonie de Paris</strong>, le <strong>Zénith</strong>."
        ],
        "hist_title": "1910 : Villette, anciens abattoirs, parc moderne",
        "hist": [
            "La station Porte de la Villette est <strong>inaugurée le 5 novembre 1910</strong> sur le tronçon initial de la <strong>M7</strong> (Opéra ↔ Porte de la Villette).",
            "Le quartier de la <strong>Villette</strong> est marqué au XIXe-XXe siècle par les <strong>halles aux bestiaux et abattoirs de la Villette</strong>, construits sous <strong>Napoléon III en 1867</strong> par <strong>Adolphe Carlier</strong>. Centre majeur du <strong>commerce de la viande</strong> à Paris. <strong>Fermeture en 1974</strong>.",
            "Le <strong>parc de la Villette</strong>, inauguré en <strong>1987</strong>, est un <strong>parc thématique culturel et scientifique</strong> de <strong>55 hectares</strong>. <strong>3e plus grand parc parisien</strong>. Conçu par l'architecte <strong>Bernard Tschumi</strong>. Abrite la <strong>Cité des Sciences et de l'Industrie</strong> (1986), la <strong>Géode</strong> (1985), la <strong>Philharmonie de Paris</strong> (2015, Jean Nouvel), le <strong>Zénith de Paris</strong> (1984), la <strong>Cité de la Musique</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Porte de la Villette ?", "<strong>M7</strong> et <strong>tramway T3b</strong>. Bus 75, 139, 150, 152."),
            ("Pour le parc de la Villette ?", "<strong>Sortie directe</strong>. 55 hectares, 3e plus grand parc parisien."),
            ("Pour la Cité des Sciences ?", "<strong>~5 min à pied</strong> dans le parc."),
            ("Pour la Géode ?", "<strong>~5 min à pied</strong> dans le parc."),
            ("Pour la Philharmonie ?", "<strong>~10 min à pied</strong> dans le parc."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Cité des Sciences et de l'Industrie</strong> à 5 min : plus grand musée scientifique d'Europe.",
            "<strong>Géode</strong> à 5 min : salle de cinéma sphérique IMAX (36 m de diamètre).",
            "<strong>Philharmonie de Paris</strong> (Jean Nouvel, 2015) à 10 min.",
            "<strong>Tramway T3b</strong> en correspondance.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🔬", "Cité des Sciences et de l'Industrie", "La <strong>Cité des Sciences et de l'Industrie</strong>, à 5 min à pied, est le <strong>plus grand musée scientifique d'Europe</strong>. <strong>Inaugurée le 13 mars 1986</strong> par le président <strong>François Mitterrand</strong>. Conçue par l'architecte <strong>Adrien Fainsilber</strong> sur l'emplacement des <strong>anciens abattoirs de la Villette</strong>. <strong>150 000 m²</strong>, <strong>~2 millions de visiteurs par an</strong>. Expositions permanentes (Explora) et temporaires, planétarium, sous-marin Argonaute."),
            ("🎵", "Philharmonie de Paris (2015)", "La <strong>Philharmonie de Paris</strong>, à 10 min à pied, est inaugurée le <strong>14 janvier 2015</strong>. Œuvre de l'architecte <strong>Jean Nouvel</strong>. <strong>Salle de 2 400 places</strong> avec <strong>acoustique exceptionnelle</strong> (Yasuhisa Toyota). Façade aluminisée caractéristique. Concerts classiques, jazz, musiques du monde. <strong>Cité de la Musique</strong> (1995, Christian de Portzamparc) à proximité.")
        ],
        "itin": [
            ("Cité des Sciences", "porte-de-la-villette", "à pied", "Parc Villette (5 min)", 5),
            ("Géode", "porte-de-la-villette", "à pied", "Parc Villette (5 min)", 5),
            ("Philharmonie de Paris", "porte-de-pantin", "M5 + à pied", "Parc Villette (10 min)", 10),
            ("Châtelet", "chatelet", "M7", "M7 directe (~16 min)", 16),
            ("Opéra", "opera", "M7", "M7 directe (~14 min)", 14),
            ("Gare de l'Est", "gare-de-l-est", "M7", "M7 directe (~8 min)", 8)
        ]
    },
    "corentin-cariou": {
        "addr": "Avenue Corentin-Cariou, 75019 Paris", "arr": "19e arrondissement (Paris)",
        "seo": "Station Corentin Cariou (M7) avenue Corentin-Cariou dans le 19e. Quartier La Villette résidentiel.",
        "tagline": "M7 — avenue Corentin-Cariou, 19e",
        "hero_desc": "Station <strong>Corentin Cariou</strong> sur l'<strong>avenue Corentin-Cariou</strong> dans le <strong>19e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>5 novembre 1910</strong>. Initialement nommée <strong>« Pont de Flandre »</strong>. Renommée en hommage à <strong>Corentin Cariou</strong> (<strong>1898-1942</strong>), <strong>militant et homme politique français</strong>.",
        "intros": [
            "La station <strong>Corentin Cariou</strong> est implantée sur l'<strong>avenue Corentin-Cariou</strong> dans le <strong>19e arrondissement</strong>. Elle est desservie par la <strong>M7</strong>, entre <strong>Porte de la Villette</strong> (1 station) et <strong>Crimée</strong> (1 station). Bus 54, 60, 75.",
            "Ouverte le <strong>5 novembre 1910</strong> sous le nom <strong>« Pont de Flandre »</strong>. <strong>Renommée Corentin Cariou</strong> en <strong>1946</strong>.",
            "Le nom <strong>Corentin Cariou</strong> rend hommage à <strong>Corentin Cariou</strong> (<strong>1898-1942</strong>), <strong>militant et homme politique français</strong>. Quartier <strong>résidentiel</strong> du <strong>19e</strong>, à proximité du <strong>parc de la Villette</strong>."
        ],
        "hist_title": "1910-1946 : Pont de Flandre renommée Corentin Cariou",
        "hist": [
            "La station est <strong>inaugurée le 5 novembre 1910</strong> sous le nom <strong>« Pont de Flandre »</strong>, sur le tronçon initial de la <strong>M7</strong>.",
            "<strong>Renommée Corentin Cariou</strong> en <strong>1946</strong>. Le nom rend hommage à <strong>Corentin Cariou</strong> (<strong>1898-1942</strong>), <strong>militant français</strong>. <strong>Conseiller municipal de Paris</strong> pour le 19e arrondissement.",
            "Le quartier autour de la station fait partie du <strong>19e arrondissement</strong>, à proximité du <strong>parc de la Villette</strong>, du <strong>canal de l'Ourcq</strong> et du <strong>quartier Stalingrad</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Corentin Cariou ?", "Uniquement la <strong>M7</strong>. Bus 54, 60, 75."),
            ("Quel était l'ancien nom ?", "<strong>« Pont de Flandre »</strong> (1910-1946)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>, renommée en <strong>1946</strong>."),
            ("Pour le parc de la Villette ?", "<strong>M7 directe</strong> vers Porte de la Villette (1 station)."),
            ("Pour Stalingrad ?", "<strong>M7 directe</strong> (2 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier <strong>résidentiel</strong> du 19e.",
            "Pour <strong>parc de la Villette</strong> : <strong>M7 directe</strong>.",
            "Pour <strong>Stalingrad</strong> et <strong>canal de l'Ourcq</strong> : <strong>M7 directe</strong>.",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🚇", "Renommée en 1946", "La station, inaugurée en <strong>1910</strong> sous le nom <strong>« Pont de Flandre »</strong> en référence au <strong>pont de Flandre</strong> sur le <strong>canal de l'Ourcq</strong>, est <strong>renommée en 1946</strong>. Cette pratique de <strong>renommage</strong> des stations après 1945 fut courante."),
            ("🛶", "Canal de l'Ourcq à proximité", "Le <strong>canal de l'Ourcq</strong>, à proximité de la station, est un <strong>canal historique</strong> creusé sous <strong>Napoléon Ier</strong> (1802-1822) pour amener de l'<strong>eau potable</strong> à Paris depuis la <strong>rivière Ourcq</strong>. <strong>108 km de long</strong>. Aujourd'hui, axe de <strong>promenade</strong> et de <strong>navigation de plaisance</strong>. Quartier en transformation avec de <strong>nouveaux quartiers</strong> le long du canal.")
        ],
        "itin": [
            ("Parc de la Villette", "porte-de-la-villette", "M7", "M7 directe (1 station)", 2),
            ("Canal de l'Ourcq", "corentin-cariou", "à pied", "Sortie + canal (5 min)", 5),
            ("Stalingrad", "stalingrad", "M7", "M7 directe (2 stations)", 4),
            ("Gare de l'Est", "gare-de-l-est", "M7", "M7 directe (~10 min)", 10),
            ("Châtelet", "chatelet", "M7", "M7 directe (~14 min)", 14),
            ("Opéra", "opera", "M7", "M7 directe (~12 min)", 12)
        ]
    },
    "crimee": {
        "addr": "Rue de Crimée, 75019 Paris", "arr": "19e arrondissement (Paris)",
        "seo": "Station Crimée (M7) rue de Crimée dans le 19e. Quartier La Villette résidentiel. Canal de l'Ourcq à proximité.",
        "tagline": "M7 — rue de Crimée, 19e",
        "hero_desc": "Station <strong>Crimée</strong> sur la <strong>rue de Crimée</strong> dans le <strong>19e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>5 novembre 1910</strong>. Nommée d'après la <strong>guerre de Crimée</strong> (1853-1856).",
        "intros": [
            "La station <strong>Crimée</strong> est implantée sur la <strong>rue de Crimée</strong> dans le <strong>19e arrondissement</strong>. Elle est desservie par la <strong>M7</strong>, entre <strong>Corentin Cariou</strong> (1 station) et <strong>Riquet</strong> (1 station). Bus 54, 60.",
            "Ouverte le <strong>5 novembre 1910</strong> sur le tronçon initial de la <strong>M7</strong>.",
            "Le nom <strong>Crimée</strong> rappelle la <strong>guerre de Crimée</strong> (<strong>1853-1856</strong>), conflit opposant la <strong>France et le Royaume-Uni à la Russie</strong>. Quartier résidentiel du <strong>19e</strong>, à proximité du <strong>canal de l'Ourcq</strong>."
        ],
        "hist_title": "1910 : rue et guerre de Crimée",
        "hist": [
            "La station Crimée est <strong>inaugurée le 5 novembre 1910</strong> sur le tronçon initial de la <strong>M7</strong>.",
            "Le nom <strong>Crimée</strong> rappelle la <strong>guerre de Crimée</strong> (<strong>1853-1856</strong>), conflit opposant la <strong>coalition franco-britannique-ottomane à la Russie</strong>. Victoires alliées à <strong>l'Alma</strong> (1854), <strong>Sébastopol</strong> (1855), <strong>Malakoff</strong> (1855). <strong>Traité de Paris</strong> (30 mars 1856).",
            "La <strong>rue de Crimée</strong>, longue de <strong>2,7 km</strong>, traverse le <strong>19e arrondissement</strong>. Ouverte en <strong>1851</strong> sous le nom <strong>« rue de la Villette »</strong>, renommée <strong>« Crimée »</strong> en <strong>1864</strong> en hommage à la victoire militaire."
        ],
        "faq": [
            ("Quelle ligne dessert Crimée ?", "Uniquement la <strong>M7</strong>. Bus 54, 60."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>."),
            ("Qu'est-ce que la guerre de Crimée ?", "<strong>Conflit 1853-1856</strong> opposant la <strong>coalition franco-britannique-ottomane à la Russie</strong>. Victoires françaises (Alma, Sébastopol, Malakoff)."),
            ("Pour le canal de l'Ourcq ?", "<strong>~5 min à pied</strong>."),
            ("Pour Châtelet ?", "<strong>M7 directe</strong> (~12 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier résidentiel du <strong>19e</strong>.",
            "<strong>Canal de l'Ourcq</strong> à 5 min à pied.",
            "Pour <strong>parc de la Villette</strong> : <strong>M7 → Porte de la Villette</strong>.",
            "Pour <strong>Stalingrad</strong> : <strong>M7 directe</strong> (1 station).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⚔️", "Guerre de Crimée (1853-1856)", "La <strong>guerre de Crimée</strong> (1853-1856) oppose la <strong>coalition franco-britannique-ottomane</strong> à la <strong>Russie</strong>. Le conflit éclate après des tensions sur la <strong>protection des Lieux saints</strong> à Jérusalem. <strong>Batailles majeures</strong> : <strong>Alma</strong> (20 septembre 1854), <strong>siège de Sébastopol</strong> (1854-1855), <strong>Malakoff</strong> (8 septembre 1855). <strong>Victoire des alliés</strong>. <strong>Traité de Paris</strong> (30 mars 1856) signé sous le Second Empire."),
            ("🛶", "Canal de l'Ourcq, axe historique", "Le <strong>canal de l'Ourcq</strong>, à 5 min à pied, est un <strong>canal historique</strong> creusé sous <strong>Napoléon Ier</strong> (1802-1822). <strong>108 km de long</strong>, il amène de l'<strong>eau potable</strong> à Paris depuis la <strong>rivière Ourcq</strong>. <strong>Aménagé en promenade</strong> à partir des années 2000. Quartier en pleine <strong>requalification urbaine</strong>.")
        ],
        "itin": [
            ("Canal de l'Ourcq", "crimee", "à pied", "5 min à pied", 5),
            ("Parc de la Villette", "porte-de-la-villette", "M7", "M7 directe (2 stations)", 4),
            ("Stalingrad", "stalingrad", "M7", "M7 directe (1 station)", 2),
            ("Gare de l'Est", "gare-de-l-est", "M7", "M7 directe (~8 min)", 8),
            ("Châtelet", "chatelet", "M7", "M7 directe (~12 min)", 12),
            ("Opéra", "opera", "M7", "M7 directe (~10 min)", 10)
        ]
    },
    "riquet": {
        "addr": "Boulevard de la Villette, 75019 Paris", "arr": "19e arrondissement (Paris)",
        "seo": "Station Riquet (M7) boulevard de la Villette dans le 19e. Hommage à Pierre-Paul Riquet, ingénieur du canal du Midi (XVIIe).",
        "tagline": "M7 — Pierre-Paul Riquet, canal du Midi",
        "hero_desc": "Station <strong>Riquet</strong> sur le <strong>boulevard de la Villette</strong> dans le <strong>19e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>5 novembre 1910</strong>. Hommage à <strong>Pierre-Paul Riquet</strong> (<strong>1609-1680</strong>), <strong>ingénieur français</strong>, concepteur du <strong>canal du Midi</strong>.",
        "intros": [
            "La station <strong>Riquet</strong> est implantée sur le <strong>boulevard de la Villette</strong> dans le <strong>19e arrondissement</strong>. Elle est desservie par la <strong>M7</strong>, entre <strong>Crimée</strong> (1 station) et <strong>Stalingrad</strong> (1 station). Bus 54, 60.",
            "Ouverte le <strong>5 novembre 1910</strong> sur le tronçon initial de la <strong>M7</strong>.",
            "Le nom <strong>Riquet</strong> rend hommage à <strong>Pierre-Paul Riquet</strong> (<strong>1609-1680</strong>), <strong>ingénieur français</strong>, <strong>concepteur du canal du Midi</strong> (1666-1681), <strong>chef-d'œuvre d'ingénierie hydraulique</strong> du XVIIe siècle."
        ],
        "hist_title": "1910 : ingénieur du canal du Midi",
        "hist": [
            "La station Riquet est <strong>inaugurée le 5 novembre 1910</strong> sur le tronçon initial de la <strong>M7</strong>.",
            "Le nom <strong>Riquet</strong> rend hommage à <strong>Pierre-Paul Riquet</strong> (<strong>29 juin 1609 - 1er octobre 1680</strong>), <strong>ingénieur français</strong>, <strong>concepteur du canal du Midi</strong>. Né à <strong>Béziers</strong>.",
            "Le <strong>canal du Midi</strong> est un <strong>chef-d'œuvre d'ingénierie hydraulique du XVIIe siècle</strong>. <strong>240 km de long</strong>, reliant la <strong>Garonne</strong> (Toulouse) à la <strong>mer Méditerranée</strong> (Sète). Construit de <strong>1666 à 1681</strong> sous l'impulsion de <strong>Colbert</strong>. Riquet finança une grande partie de l'ouvrage. <strong>Inscrit au patrimoine mondial de l'UNESCO en 1996</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Riquet ?", "Uniquement la <strong>M7</strong>. Bus 54, 60."),
            ("Qui est Pierre-Paul Riquet ?", "<strong>Pierre-Paul Riquet</strong> (1609-1680), <strong>ingénieur français</strong>, <strong>concepteur du canal du Midi</strong> (1666-1681)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>."),
            ("Qu'est-ce que le canal du Midi ?", "<strong>Chef-d'œuvre d'ingénierie du XVIIe</strong>, 240 km reliant la Garonne à la Méditerranée. <strong>UNESCO 1996</strong>."),
            ("Pour Stalingrad ?", "<strong>M7 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier résidentiel du <strong>19e</strong>.",
            "Pour <strong>Stalingrad</strong> et <strong>canal de l'Ourcq</strong> : <strong>M7 directe</strong>.",
            "Pour <strong>parc de la Villette</strong> : <strong>M7 → Porte de la Villette</strong>.",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏗️", "Canal du Midi (1666-1681)", "Le <strong>canal du Midi</strong>, conçu par <strong>Pierre-Paul Riquet</strong>, est l'un des <strong>plus grands chefs-d'œuvre d'ingénierie hydraulique</strong> du <strong>XVIIe siècle</strong>. <strong>240 km</strong> reliant la <strong>Garonne</strong> (Toulouse) à la <strong>Méditerranée</strong> (Sète). Construit de <strong>1666 à 1681</strong> sous l'impulsion de <strong>Colbert</strong>, ministre de Louis XIV. <strong>328 ouvrages d'art</strong> (ponts, écluses, aqueducs). <strong>Inscrit au patrimoine mondial de l'UNESCO en 1996</strong>."),
            ("💰", "Riquet et son investissement personnel", "<strong>Pierre-Paul Riquet</strong> (1609-1680), <strong>fermier des gabelles</strong> (collecteur d'impôt sur le sel), <strong>investit sa fortune personnelle</strong> dans le projet du canal. Il <strong>vendit ses biens</strong> et <strong>maria sa fille</strong> pour réunir les fonds. <strong>Mort en 1680</strong>, <strong>8 mois avant l'achèvement</strong> du canal (mai 1681). Son <strong>nom est gravé</strong> sur de nombreux ouvrages du canal.")
        ],
        "itin": [
            ("Stalingrad", "stalingrad", "M7", "M7 directe (1 station)", 2),
            ("Canal de l'Ourcq", "stalingrad", "M7 + à pied", "Via Stalingrad", 5),
            ("Parc de la Villette", "porte-de-la-villette", "M7", "M7 directe (3 stations)", 6),
            ("Gare de l'Est", "gare-de-l-est", "M7", "M7 directe (~6 min)", 6),
            ("Châtelet", "chatelet", "M7", "M7 directe (~10 min)", 10),
            ("Opéra", "opera", "M7", "M7 directe (~8 min)", 8)
        ]
    },
    "chateau-landon": {
        "addr": "Rue du Faubourg-Saint-Martin, 75010 Paris", "arr": "10e arrondissement (Paris)",
        "seo": "Station Château-Landon (M7) rue du Faubourg-Saint-Martin dans le 10e. Gare de l'Est à 5 min à pied. Quartier 10e résidentiel.",
        "tagline": "M7 — Château-Landon, 10e résidentiel",
        "hero_desc": "Station <strong>Château-Landon</strong> sur la <strong>rue du Faubourg-Saint-Martin</strong> dans le <strong>10e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>5 novembre 1910</strong>. À <strong>5 min à pied de la gare de l'Est</strong>.",
        "intros": [
            "La station <strong>Château-Landon</strong> est implantée sur la <strong>rue du Faubourg-Saint-Martin</strong> dans le <strong>10e arrondissement</strong>. Elle est desservie par la <strong>M7</strong>, entre <strong>Louis Blanc</strong> (1 station) et <strong>Gare de l'Est</strong> (1 station). Bus 38, 43, 47.",
            "Ouverte le <strong>5 novembre 1910</strong> sur le tronçon initial de la <strong>M7</strong>.",
            "Le nom <strong>Château-Landon</strong> rappelle la <strong>rue du Château-Landon</strong> à proximité. Étymologie évoquant un <strong>ancien château</strong> du quartier (probable origine médiévale). Quartier <strong>résidentiel</strong> du <strong>10e</strong>, à <strong>5 min à pied de la gare de l'Est</strong>."
        ],
        "hist_title": "1910 : Faubourg Saint-Martin et 10e",
        "hist": [
            "La station Château-Landon est <strong>inaugurée le 5 novembre 1910</strong> sur le tronçon initial de la <strong>M7</strong>.",
            "Le nom <strong>Château-Landon</strong> rappelle la <strong>rue du Château-Landon</strong> à proximité, dont l'étymologie évoque un <strong>ancien château médiéval</strong> du quartier (aujourd'hui disparu).",
            "Le quartier autour de la station fait partie du <strong>10e arrondissement</strong>, secteur résidentiel proche des <strong>gares de l'Est et du Nord</strong>. Quartier <strong>populaire et multi-ethnique</strong>. Le <strong>Couvent des Récollets</strong> (1604), aujourd'hui <strong>Maison de l'Architecture</strong>, est à proximité."
        ],
        "faq": [
            ("Quelle ligne dessert Château-Landon ?", "Uniquement la <strong>M7</strong>. Bus 38, 43, 47."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>."),
            ("Pour la gare de l'Est ?", "<strong>~5 min à pied</strong> ou <strong>M7 directe</strong> (1 station)."),
            ("Pour la gare du Nord ?", "<strong>~10 min à pied</strong>."),
            ("Pour le couvent des Récollets ?", "<strong>~5 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Gare de l'Est</strong> à 5 min à pied.",
            "<strong>Gare du Nord</strong> à 10 min à pied.",
            "<strong>Couvent des Récollets</strong> (Maison de l'Architecture) à 5 min.",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Couvent des Récollets (1604)", "Le <strong>couvent des Récollets</strong>, à 5 min à pied, est un <strong>ancien couvent franciscain</strong> construit en <strong>1604</strong>. Devenu <strong>hôpital militaire</strong> au XIXe, puis abandonné. <strong>Restauré dans les années 2000</strong>, il abrite aujourd'hui la <strong>Maison de l'Architecture en Île-de-France</strong>. <strong>Jardin</strong> ouvert au public."),
            ("🏘️", "10e arrondissement, gares et multi-ethnicité", "Le <strong>10e arrondissement</strong> (~92 000 habitants) est marqué par la présence de <strong>deux grandes gares</strong> (<strong>Gare du Nord</strong> et <strong>Gare de l'Est</strong>), parmi les <strong>plus fréquentées d'Europe</strong>. Quartier <strong>multi-ethnique</strong> (« Petit Inde » rue du Faubourg-Saint-Denis, communautés turque, kurde, africaine).")
        ],
        "itin": [
            ("Gare de l'Est", "gare-de-l-est", "M7", "M7 directe (1 station)", 2),
            ("Gare du Nord", "gare-du-nord", "M7 + à pied", "10 min à pied", 10),
            ("Couvent des Récollets", "chateau-landon", "à pied", "5 min à pied", 5),
            ("Châtelet", "chatelet", "M7", "M7 directe (~8 min)", 8),
            ("Opéra", "opera", "M7", "M7 directe (~6 min)", 6),
            ("République", "republique", "M7", "M7 directe (3 stations)", 6)
        ]
    },
    "poissonniere": {
        "addr": "Boulevard de Magenta, 75009 Paris", "arr": "9e arrondissement (Paris)",
        "seo": "Station Poissonnière (M7) boulevard de Magenta dans le 9e. Nom évoquant l'ancien chemin des marchands de poisson de la mer du Nord.",
        "tagline": "M7 — Poissonnière, ancien chemin marchand",
        "hero_desc": "Station <strong>Poissonnière</strong> sur le <strong>boulevard de Magenta</strong> dans le <strong>9e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>5 novembre 1910</strong>. Nom rappelant l'ancien <strong>chemin des marchands de poisson</strong> reliant les <strong>côtes de la Manche</strong> à Paris.",
        "intros": [
            "La station <strong>Poissonnière</strong> est implantée sur le <strong>boulevard de Magenta</strong> dans le <strong>9e arrondissement</strong>. Elle est desservie par la <strong>M7</strong>, entre <strong>Gare de l'Est</strong> (1 station) et <strong>Cadet</strong> (1 station). Bus 32, 38, 39, 42, 48.",
            "Ouverte le <strong>5 novembre 1910</strong> sur le tronçon initial de la <strong>M7</strong>.",
            "Le nom <strong>Poissonnière</strong> rappelle la <strong>rue Poissonnière</strong> et le <strong>boulevard Poissonnière</strong> à proximité. Ces voies rappellent l'<strong>ancien chemin des marchands de poisson</strong> qui acheminaient leur marchandise des <strong>côtes de la Manche</strong> (Dieppe) aux <strong>Halles de Paris</strong>."
        ],
        "hist_title": "1910 : ancien chemin du poisson",
        "hist": [
            "La station Poissonnière est <strong>inaugurée le 5 novembre 1910</strong> sur le tronçon initial de la <strong>M7</strong>.",
            "Le nom <strong>Poissonnière</strong> rappelle l'<strong>ancien chemin des marchands de poisson</strong>. Au <strong>Moyen Âge</strong> et sous l'<strong>Ancien Régime</strong>, le poisson de mer (notamment harengs et morues) était acheminé depuis les <strong>ports de la Manche</strong> (<strong>Dieppe</strong>, <strong>Le Havre</strong>, <strong>Boulogne</strong>) jusqu'aux <strong>Halles de Paris</strong> par un chemin appelé <strong>« chemin de la marée »</strong> ou <strong>« voie Poissonnière »</strong>.",
            "L'arrivée du poisson, organisée en <strong>convois rapides</strong> appelés <strong>« chasse-marée »</strong>, permettait de garantir la <strong>fraîcheur</strong> du produit. Le boulevard Poissonnière marque l'<strong>entrée historique</strong> de ces convois dans Paris depuis le nord."
        ],
        "faq": [
            ("Quelle ligne dessert Poissonnière ?", "Uniquement la <strong>M7</strong>. Bus 32, 38, 39, 42, 48."),
            ("D'où vient le nom Poissonnière ?", "De l'<strong>ancien chemin des marchands de poisson</strong> qui acheminaient harengs et morues depuis la <strong>Manche</strong> vers les <strong>Halles de Paris</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>."),
            ("Qu'est-ce que le « chasse-marée » ?", "Convoi rapide de transport de poisson frais depuis la côte vers Paris."),
            ("Pour Opéra ?", "<strong>M7 directe</strong> (3 stations, ~6 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Boulevard Poissonnière</strong> : axe haussmannien.",
            "Pour <strong>Galeries Lafayette</strong> : <strong>M7 → Chaussée d'Antin</strong>.",
            "Pour <strong>Opéra Garnier</strong> : <strong>M7 directe</strong> (3 stations).",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🐟", "Chemin de la marée et chasse-marée", "Au <strong>Moyen Âge</strong> et sous l'<strong>Ancien Régime</strong>, le <strong>chemin de la marée</strong> ou <strong>voie Poissonnière</strong> permettait d'acheminer rapidement le <strong>poisson de mer</strong> (harengs, morues) depuis les <strong>ports de la Manche</strong> (Dieppe, Le Havre, Boulogne) aux <strong>Halles de Paris</strong>. Les convois rapides étaient appelés <strong>« chasse-marée »</strong>. <strong>Réseau de relais</strong> et de <strong>chevaux frais</strong> garantissait la <strong>vitesse</strong>. <strong>Pratique attestée depuis le XIIe siècle</strong>."),
            ("🏘️", "Boulevard Poissonnière, axe haussmannien", "Le <strong>boulevard Poissonnière</strong>, à proximité de la station, fait partie des <strong>Grands Boulevards</strong> tracés sous <strong>Louis XIV</strong> à partir de <strong>1670</strong>, élargis sous <strong>Haussmann</strong>. <strong>Centre nerveux</strong> de la <strong>Belle Époque</strong> et du <strong>XXe siècle parisien</strong> : <strong>théâtres</strong> (Rex, Grand Rex), <strong>cinémas</strong>, <strong>cafés</strong>.")
        ],
        "itin": [
            ("Galeries Lafayette", "chaussee-d-antin-la-fayette", "M7", "M7 directe (2 stations)", 4),
            ("Opéra Garnier", "opera", "M7", "M7 directe (3 stations)", 6),
            ("Grand Rex (cinéma)", "bonne-nouvelle", "M8 ou à pied", "5 min à pied", 5),
            ("Châtelet", "chatelet", "M7", "M7 directe (~6 min)", 6),
            ("Gare de l'Est", "gare-de-l-est", "M7", "M7 directe (1 station)", 2),
            ("République", "republique", "M7", "M7 directe (~5 min)", 5)
        ]
    },
    "cadet": {
        "addr": "Rue La Fayette, 75009 Paris", "arr": "9e arrondissement (Paris)",
        "seo": "Station Cadet (M7) rue La Fayette dans le 9e. Hommage à la famille Cadet, marchands du XVIIIe. Grand Orient de France à proximité.",
        "tagline": "M7 — Cadet, famille de marchands XVIIIe",
        "hero_desc": "Station <strong>Cadet</strong> sur la <strong>rue La Fayette</strong> dans le <strong>9e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>5 novembre 1910</strong>. Hommage à la <strong>famille Cadet</strong>, <strong>marchands du XVIIIe siècle</strong>. À proximité du <strong>Grand Orient de France</strong> (siège maçonnique).",
        "intros": [
            "La station <strong>Cadet</strong> est implantée sur la <strong>rue La Fayette</strong> dans le <strong>9e arrondissement</strong>. Elle est desservie par la <strong>M7</strong>, entre <strong>Poissonnière</strong> (1 station) et <strong>Le Peletier</strong> (1 station). Bus 26, 32, 42, 43, 48, 49, 67.",
            "Ouverte le <strong>5 novembre 1910</strong> sur le tronçon initial de la <strong>M7</strong>.",
            "Le nom <strong>Cadet</strong> rend hommage à la <strong>famille Cadet</strong>, <strong>marchands jardiniers du XVIIIe siècle</strong>. À proximité : le <strong>Grand Orient de France</strong>, <strong>siège de la principale obédience maçonnique française</strong> depuis 1853."
        ],
        "hist_title": "1910 : famille Cadet et Grand Orient",
        "hist": [
            "La station Cadet est <strong>inaugurée le 5 novembre 1910</strong> sur le tronçon initial de la <strong>M7</strong>.",
            "Le nom <strong>Cadet</strong> rend hommage à la <strong>famille Cadet</strong>, <strong>marchands jardiniers</strong> qui possédaient des terrains dans le quartier au <strong>XVIIIe siècle</strong>. La <strong>rue Cadet</strong>, à proximité, conserve leur nom.",
            "À courte distance : le <strong>Grand Orient de France</strong> (<strong>16 rue Cadet</strong>), <strong>siège de la principale obédience maçonnique française</strong>. <strong>Installé rue Cadet en 1853</strong>. <strong>Musée de la Franc-Maçonnerie</strong> ouvert au public. La <strong>franc-maçonnerie française</strong> est représentée par plusieurs obédiences, le <strong>Grand Orient</strong> étant la <strong>plus ancienne</strong> (1773)."
        ],
        "faq": [
            ("Quelle ligne dessert Cadet ?", "Uniquement la <strong>M7</strong>. Bus 26, 32, 42, 43, 48, 49, 67."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>."),
            ("D'où vient le nom Cadet ?", "De la <strong>famille Cadet</strong>, <strong>marchands jardiniers du XVIIIe siècle</strong>."),
            ("Pour le Grand Orient de France ?", "<strong>~5 min à pied</strong> (16 rue Cadet). Musée de la Franc-Maçonnerie ouvert au public."),
            ("Pour Opéra ?", "<strong>M7 directe</strong> (2 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Grand Orient de France</strong> à 5 min à pied : musée de la Franc-Maçonnerie.",
            "<strong>Galeries Lafayette</strong> à 10 min à pied ou <strong>M7 directe</strong>.",
            "Pour <strong>Opéra Garnier</strong> : <strong>M7 directe</strong> (2 stations).",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Grand Orient de France (1773)", "Le <strong>Grand Orient de France</strong>, à 5 min à pied (16 rue Cadet), est la <strong>plus ancienne obédience maçonnique</strong> française. <strong>Fondé en 1773</strong>. <strong>Installé rue Cadet en 1853</strong>. <strong>Hôtel du Grand Orient</strong> construit en 1881. <strong>Musée de la Franc-Maçonnerie</strong> ouvert au public : <strong>tabliers, sceaux, objets symboliques</strong>, présentation des <strong>obédiences françaises</strong>."),
            ("🌳", "Famille Cadet, marchands jardiniers", "La <strong>famille Cadet</strong>, à laquelle la station rend hommage, était une <strong>famille de marchands jardiniers</strong> du <strong>XVIIIe siècle</strong>. Plusieurs membres se distinguèrent : <strong>Louis-Claude Cadet de Gassicourt</strong> (1731-1799), <strong>chimiste et apothicaire</strong>, <strong>découvreur de l'acide arsénieux</strong>. Le quartier, alors <strong>périphérique de Paris</strong>, était occupé par des <strong>marécages et jardins maraîchers</strong>.")
        ],
        "itin": [
            ("Grand Orient de France", "cadet", "à pied", "Rue Cadet (5 min)", 5),
            ("Galeries Lafayette", "chaussee-d-antin-la-fayette", "M7", "M7 directe (1 station)", 2),
            ("Opéra Garnier", "opera", "M7", "M7 directe (2 stations)", 4),
            ("Châtelet", "chatelet", "M7", "M7 directe (~6 min)", 6),
            ("Gare de l'Est", "gare-de-l-est", "M7", "M7 directe (3 stations)", 6),
            ("Pigalle", "pigalle", "M7 + M2", "M7 → Le Peletier + à pied", 8)
        ]
    },
    "le-peletier": {
        "addr": "Rue La Fayette, 75009 Paris", "arr": "9e arrondissement (Paris)",
        "seo": "Station Le Peletier (M7) rue La Fayette dans le 9e. Hommage à Louis-Michel le Peletier de Saint-Fargeau. Quartier Opéra proche.",
        "tagline": "M7 — Le Peletier, 9e proche Opéra",
        "hero_desc": "Station <strong>Le Peletier</strong> sur la <strong>rue La Fayette</strong> dans le <strong>9e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>5 novembre 1910</strong>. Hommage à <strong>Louis-Michel le Peletier de Saint-Fargeau</strong> (<strong>1760-1793</strong>).",
        "intros": [
            "La station <strong>Le Peletier</strong> est implantée sur la <strong>rue La Fayette</strong> dans le <strong>9e arrondissement</strong>. Elle est desservie par la <strong>M7</strong>, entre <strong>Cadet</strong> (1 station) et <strong>Chaussée d'Antin - La Fayette</strong> (1 station). Bus 26, 32, 42, 43, 48, 49, 67.",
            "Ouverte le <strong>5 novembre 1910</strong> sur le tronçon initial de la <strong>M7</strong>.",
            "Le nom <strong>Le Peletier</strong> rend hommage à <strong>Louis-Michel le Peletier de Saint-Fargeau</strong> (<strong>1760-1793</strong>), <strong>magistrat et homme politique français</strong>. <strong>Député de la noblesse</strong> aux <strong>États généraux de 1789</strong>, rallié au tiers état."
        ],
        "hist_title": "1910 : Le Peletier de Saint-Fargeau",
        "hist": [
            "La station Le Peletier est <strong>inaugurée le 5 novembre 1910</strong> sur le tronçon initial de la <strong>M7</strong>.",
            "Le nom <strong>Le Peletier</strong> rend hommage à <strong>Louis-Michel le Peletier de Saint-Fargeau</strong> (<strong>29 mai 1760 - 20 janvier 1793</strong>), <strong>magistrat et homme politique français</strong>. <strong>Député de la noblesse</strong> aux <strong>États généraux de 1789</strong>, il se rallie au <strong>tiers état</strong>.",
            "Le quartier autour de la station fait partie du <strong>9e arrondissement</strong>, proche de l'<strong>Opéra Garnier</strong>. À courte distance : les <strong>Galeries Lafayette</strong> et le <strong>Printemps</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Le Peletier ?", "Uniquement la <strong>M7</strong>. Bus 26, 32, 42, 43, 48, 49, 67."),
            ("Qui est Le Peletier ?", "<strong>Louis-Michel le Peletier de Saint-Fargeau</strong> (1760-1793), <strong>magistrat et homme politique</strong>. <strong>Député aux États généraux de 1789</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>."),
            ("Pour les Galeries Lafayette ?", "<strong>~5 min à pied</strong>."),
            ("Pour Opéra ?", "<strong>M7 directe</strong> (2 stations, ~4 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Galeries Lafayette</strong> et <strong>Printemps</strong> à 5 min à pied.",
            "Pour <strong>Opéra Garnier</strong> : <strong>M7 directe</strong> (2 stations).",
            "<strong>Quartier 9e shopping et théâtres</strong>.",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("📜", "Le Peletier, député aux États généraux", "<strong>Louis-Michel le Peletier de Saint-Fargeau</strong> (1760-1793), <strong>magistrat et homme politique français</strong>. <strong>Premier président du Parlement de Paris</strong>. <strong>Député de la noblesse aux États généraux de 1789</strong>, il <strong>se rallie au tiers état</strong>. <strong>Député de l'Yonne</strong> à la Convention. <strong>Vote la mort du roi</strong> Louis XVI (21 janvier 1793)."),
            ("🏛️", "Grands Boulevards à proximité", "Le quartier autour de la station <strong>Le Peletier</strong> fait partie des <strong>Grands Boulevards</strong>, axe central de la <strong>Belle Époque parisienne</strong>. <strong>Théâtres</strong> (Mogador, Folies Bergère à proximité), <strong>cafés historiques</strong>, <strong>passages couverts</strong> (passage Verdeau, passage Jouffroy).")
        ],
        "itin": [
            ("Galeries Lafayette", "chaussee-d-antin-la-fayette", "M7", "M7 directe (1 station)", 2),
            ("Printemps Haussmann", "havre-caumartin", "M7 + M9", "M7 → Chaussée d'Antin + M9", 5),
            ("Opéra Garnier", "opera", "M7", "M7 directe (2 stations)", 4),
            ("Folies Bergère", "le-peletier", "à pied", "Rue Richer (5 min)", 5),
            ("Châtelet", "chatelet", "M7", "M7 directe (~6 min)", 6),
            ("Pigalle", "pigalle", "M2 + à pied", "À pied (10 min) ou M7 + M2", 10)
        ]
    },
    "chaussee-d-antin-la-fayette": {
        "addr": "Boulevard Haussmann, 75009 Paris", "arr": "9e arrondissement (Paris)",
        "seo": "Station Chaussée d'Antin - La Fayette (M7+M9) boulevard Haussmann. Galeries Lafayette face à la sortie. Hub shopping majeur Paris.",
        "tagline": "M7 + M9 — Galeries Lafayette, hub shopping",
        "hero_desc": "Station <strong>Chaussée d'Antin - La Fayette</strong>, hub <strong>M7 + M9</strong>, sur le <strong>boulevard Haussmann</strong> dans le <strong>9e arrondissement</strong>. <strong>Galeries Lafayette Haussmann</strong> face à la sortie. Quais <strong>M7</strong> ouverts en <strong>1910</strong>, quais <strong>M9</strong> en <strong>1923</strong>.",
        "intros": [
            "La station <strong>Chaussée d'Antin - La Fayette</strong> est implantée sur le <strong>boulevard Haussmann</strong>, à l'angle de la <strong>rue La Fayette</strong>, dans le <strong>9e arrondissement</strong>. Elle est desservie par les <strong>lignes 7 et 9</strong> du métro parisien, formant un <strong>hub shopping majeur</strong>. Bus 20, 21, 22, 26, 27, 29, 32, 43, 52, 53, 66, 68, 80, 81, 84, 94, 95.",
            "Quais <strong>M7</strong> ouverts le <strong>5 novembre 1910</strong> avec le tronçon initial de la M7. Quais <strong>M9</strong> ouverts le <strong>27 mai 1923</strong> avec le prolongement Trocadéro ↔ Saint-Augustin.",
            "À la sortie : les <strong>Galeries Lafayette Haussmann</strong>, l'un des <strong>plus célèbres grands magasins</strong> au monde. Avec sa <strong>célèbre coupole néo-byzantine</strong> (1912, Ferdinand Chanut, 33 m de haut). À courte distance : le <strong>Printemps Haussmann</strong>."
        ],
        "hist_title": "1910-1923 : hub M7/M9 et Galeries Lafayette",
        "hist": [
            "Les quais <strong>ligne 7</strong> sont <strong>inaugurés le 5 novembre 1910</strong> avec le tronçon initial de la M7. Les quais <strong>ligne 9</strong> ouvrent le <strong>27 mai 1923</strong>.",
            "Le nom <strong>Chaussée d'Antin</strong> rappelle l'<strong>ancien chemin de la chaussée d'Antin</strong>, voie historique tracée au <strong>XVIIIe siècle</strong>. <strong>La Fayette</strong> rend hommage au <strong>marquis de La Fayette</strong> (1757-1834), <strong>héros des indépendances américaine et française</strong>.",
            "Les <strong>Galeries Lafayette Haussmann</strong>, face à la sortie, sont fondées en <strong>1893</strong> par <strong>Théophile Bader</strong>. Leur <strong>célèbre coupole néo-byzantine</strong>, dessinée par <strong>Ferdinand Chanut</strong>, est inaugurée en <strong>1912</strong>. <strong>33 mètres de haut</strong>, vitraux de <strong>Jacques Gruber</strong>. <strong>Classée monument historique en 1975</strong>. <strong>~37 millions de visiteurs/an</strong>."
        ],
        "faq": [
            ("Quelles lignes desservent Chaussée d'Antin - La Fayette ?", "<strong>M7</strong> et <strong>M9</strong>. Hub shopping majeur."),
            ("Pour les Galeries Lafayette ?", "<strong>Sortie directe</strong>. Célèbre coupole néo-byzantine de 1912."),
            ("Pour le Printemps Haussmann ?", "<strong>~3 min à pied</strong>."),
            ("Pour Opéra Garnier ?", "<strong>~5 min à pied</strong> ou <strong>M7 directe</strong>."),
            ("Quand a-t-elle ouvert ?", "Quais M7 : <strong>5 novembre 1910</strong>. Quais M9 : <strong>27 mai 1923</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Galeries Lafayette Haussmann</strong> à la sortie : coupole néo-byzantine 1912, 37 millions de visiteurs/an.",
            "<strong>Printemps Haussmann</strong> à 3 min à pied.",
            "<strong>Opéra Garnier</strong> à 5 min à pied.",
            "<strong>Gare Saint-Lazare</strong> à 10 min à pied.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🛍️", "Galeries Lafayette Haussmann (1893)", "Les <strong>Galeries Lafayette Haussmann</strong>, face à la sortie, sont l'un des <strong>plus célèbres grands magasins au monde</strong>. Fondées en <strong>1893</strong> par <strong>Théophile Bader</strong> et <strong>Alphonse Kahn</strong>. Leur <strong>célèbre coupole néo-byzantine</strong>, dessinée par l'architecte <strong>Ferdinand Chanut</strong>, est inaugurée le <strong>15 octobre 1912</strong>. <strong>33 mètres de haut</strong>, vitraux de <strong>Jacques Gruber</strong> (Art Nouveau). <strong>Classée monument historique en 1975</strong>. <strong>~37 millions de visiteurs/an</strong>."),
            ("🇺🇸", "La Fayette, héros des deux mondes", "Le nom <strong>La Fayette</strong> rend hommage à <strong>Gilbert du Motier, marquis de La Fayette</strong> (<strong>1757-1834</strong>), <strong>héros de l'indépendance américaine</strong> et de la Révolution française. <strong>Engagé volontaire dans l'armée continentale</strong> de Washington en <strong>1777</strong> à 19 ans. <strong>Major-général américain</strong>. Acteur clé de la <strong>victoire de Yorktown</strong> (1781). <strong>Surnommé « héros des deux mondes »</strong>. <strong>Inhumé au cimetière de Picpus</strong>, sa tombe ornée d'un <strong>drapeau américain</strong>.")
        ],
        "itin": [
            ("Galeries Lafayette", "chaussee-d-antin-la-fayette", "à pied", "Sortie directe", 1),
            ("Printemps Haussmann", "havre-caumartin", "M9", "M9 directe (1 station)", 2),
            ("Opéra Garnier", "opera", "à pied", "5 min à pied", 5),
            ("Gare Saint-Lazare", "saint-lazare", "M9", "M9 directe (2 stations)", 4),
            ("Châtelet", "chatelet", "M7", "M7 directe (~5 min)", 5),
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (~14 min)", 14)
        ]
    },
    "sully-morland": {
        "addr": "Boulevard Henri-IV, 75004 Paris", "arr": "4e arrondissement (Paris)",
        "seo": "Station Sully - Morland (M7) boulevard Henri-IV dans le 4e. Hommage au duc de Sully et au maréchal Morland. Île Saint-Louis à proximité.",
        "tagline": "M7 — Sully (ministre Henri IV) et Île Saint-Louis",
        "hero_desc": "Station <strong>Sully - Morland</strong> sur le <strong>boulevard Henri-IV</strong> dans le <strong>4e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>26 avril 1930</strong>. Hommage au <strong>duc de Sully</strong> (<strong>1559-1641</strong>), ministre d'Henri IV. À proximité de l'<strong>Île Saint-Louis</strong> et du <strong>quartier du Marais sud</strong>.",
        "intros": [
            "La station <strong>Sully - Morland</strong> est implantée sur le <strong>boulevard Henri-IV</strong> dans le <strong>4e arrondissement</strong>. Elle est desservie par la <strong>M7</strong>, entre <strong>Pont Marie</strong> (1 station) et <strong>Jussieu</strong> (1 station). Bus 67, 86, 87.",
            "Ouverte le <strong>26 avril 1930</strong> avec le <strong>prolongement de la M7</strong> de <strong>Pont Marie à Place Monge</strong>.",
            "Le nom <strong>Sully</strong> rend hommage à <strong>Maximilien de Béthune, duc de Sully</strong> (<strong>1559-1641</strong>), <strong>ministre des Finances et conseiller d'Henri IV</strong>. <strong>Morland</strong> rend hommage à <strong>François Louis de Morland</strong> (<strong>1771-1809</strong>), <strong>colonel des chasseurs à cheval</strong>. À courte distance : l'<strong>Île Saint-Louis</strong>."
        ],
        "hist_title": "1930 : Sully, ministre d'Henri IV",
        "hist": [
            "La station Sully - Morland est <strong>inaugurée le 26 avril 1930</strong> avec le <strong>prolongement de la M7</strong> de Pont Marie à Place Monge.",
            "Le nom <strong>Sully</strong> rend hommage à <strong>Maximilien de Béthune, duc de Sully</strong> (<strong>13 décembre 1559 - 22 décembre 1641</strong>), <strong>ministre français</strong> et <strong>conseiller d'Henri IV</strong>. <strong>Surintendant des Finances</strong> (1598-1611), il <strong>redresse les finances royales</strong> après les <strong>guerres de Religion</strong>. <strong>Pacificateur</strong>, il développe l'<strong>agriculture</strong> (« labourage et pâturage sont les deux mamelles de la France »).",
            "<strong>Morland</strong> rend hommage à <strong>François Louis de Morland</strong> (<strong>1771-1809</strong>), <strong>colonel des chasseurs à cheval de la Garde impériale</strong> sous Napoléon. <strong>Mort à la bataille d'Austerlitz</strong> (1805). À courte distance : l'<strong>Île Saint-Louis</strong>, l'une des <strong>deux îles habitées de la Seine</strong>, célèbre pour ses <strong>hôtels particuliers du XVIIe</strong> et ses <strong>glaces Berthillon</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Sully - Morland ?", "Uniquement la <strong>M7</strong>. Bus 67, 86, 87."),
            ("Qui est Sully ?", "<strong>Maximilien de Béthune, duc de Sully</strong> (1559-1641), <strong>ministre et conseiller d'Henri IV</strong>. <strong>Surintendant des Finances</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>26 avril 1930</strong>."),
            ("Pour l'Île Saint-Louis ?", "<strong>~3 min à pied</strong> via le pont de Sully."),
            ("Pour Notre-Dame de Paris ?", "<strong>~10 min à pied</strong> via les ponts."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Île Saint-Louis</strong> à 3 min : hôtels particuliers XVIIe, glaces Berthillon.",
            "<strong>Notre-Dame de Paris</strong> à 10 min à pied.",
            "<strong>Place des Vosges</strong> à 10 min à pied (Marais).",
            "Pour <strong>Bastille</strong> : <strong>~5 min à pied</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("👑", "Sully, le « ministre du roi Henri IV »", "<strong>Maximilien de Béthune, duc de Sully</strong> (1559-1641), <strong>ministre français</strong> et <strong>plus proche conseiller d'Henri IV</strong>. <strong>Surintendant des Finances</strong> (1598-1611), il <strong>redresse les finances royales</strong> après les <strong>guerres de Religion</strong>. <strong>Pacificateur</strong>, partisan du <strong>développement agricole</strong>. <strong>Maréchal de France</strong> en 1634. Ses <strong>« Économies royales »</strong> sont une <strong>source historique majeure</strong> sur le règne d'Henri IV. Inhumé dans l'<strong>église de Nogent-le-Rotrou</strong>."),
            ("🍦", "Île Saint-Louis et Berthillon", "L'<strong>Île Saint-Louis</strong>, à 3 min à pied, est l'une des <strong>deux îles habitées</strong> de la <strong>Seine</strong> à Paris. <strong>Aménagée au XVIIe siècle</strong> sous <strong>Louis XIII</strong> par <strong>Christophe Marie</strong>. Conserve une <strong>atmosphère résidentielle préservée</strong> avec ses <strong>hôtels particuliers Louis XIII</strong> (hôtel de Lauzun, hôtel Lambert). Les <strong>glaces Berthillon</strong> (29 rue Saint-Louis-en-l'Île), fondées en <strong>1954</strong>, sont les <strong>plus célèbres de Paris</strong>.")
        ],
        "itin": [
            ("Île Saint-Louis (Berthillon)", "pont-marie", "à pied", "Pont de Sully (3 min)", 3),
            ("Notre-Dame de Paris", "cite", "à pied", "Via les ponts (10 min)", 10),
            ("Place des Vosges", "saint-paul", "à pied", "10 min via Marais", 10),
            ("Bastille", "bastille", "à pied", "5 min à pied", 5),
            ("Châtelet", "chatelet", "M7", "M7 directe (~5 min)", 5),
            ("Opéra Garnier", "opera", "M7", "M7 directe (~9 min)", 9)
        ]
    },
    "place-monge": {
        "addr": "Place Monge, 75005 Paris", "arr": "5e arrondissement (Paris)",
        "seo": "Station Place Monge (M7) place Monge dans le 5e. Hommage à Gaspard Monge, mathématicien. Quartier Latin, Jardin des Plantes.",
        "tagline": "M7 — Gaspard Monge, mathématicien et Quartier Latin",
        "hero_desc": "Station <strong>Place Monge</strong> sur la <strong>place Monge</strong> dans le <strong>5e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>26 avril 1930</strong>. Hommage à <strong>Gaspard Monge</strong> (<strong>1746-1818</strong>), <strong>mathématicien français</strong>, fondateur de la <strong>géométrie descriptive</strong>.",
        "intros": [
            "La station <strong>Place Monge</strong> est implantée sur la <strong>place Monge</strong> dans le <strong>5e arrondissement</strong>, au cœur du <strong>Quartier Latin</strong>. Elle est desservie par la <strong>M7</strong>, entre <strong>Jussieu</strong> (1 station) et <strong>Censier - Daubenton</strong> (1 station). Bus 47.",
            "Ouverte le <strong>26 avril 1930</strong> avec le <strong>prolongement de la M7</strong>.",
            "Le nom <strong>Monge</strong> rend hommage à <strong>Gaspard Monge, comte de Péluse</strong> (<strong>1746-1818</strong>), <strong>mathématicien français</strong>, fondateur de la <strong>géométrie descriptive</strong>. <strong>Cofondateur de l'École polytechnique</strong> (1794). À proximité : le <strong>Jardin des Plantes</strong>, les <strong>Arènes de Lutèce</strong>."
        ],
        "hist_title": "1930 : Monge, fondateur de la géométrie descriptive",
        "hist": [
            "La station Place Monge est <strong>inaugurée le 26 avril 1930</strong> avec le <strong>prolongement de la M7</strong>.",
            "Le nom <strong>Monge</strong> rend hommage à <strong>Gaspard Monge, comte de Péluse</strong> (<strong>10 mai 1746 - 28 juillet 1818</strong>), <strong>mathématicien français</strong>. Né à <strong>Beaune</strong>. <strong>Fondateur de la géométrie descriptive</strong>, branche des mathématiques permettant la <strong>représentation graphique</strong> d'objets en trois dimensions sur un plan.",
            "<strong>Membre de l'Académie des sciences</strong> en 1780. <strong>Ministre de la Marine</strong> sous la Convention (1792). <strong>Cofondateur de l'École polytechnique</strong> en <strong>1794</strong> avec <strong>Lazare Carnot</strong>. <strong>Sénateur sous l'Empire</strong>. À proximité : le <strong>Jardin des Plantes</strong> (1626), les <strong>Arènes de Lutèce</strong> (Ier-IIe siècle, vestiges gallo-romains)."
        ],
        "faq": [
            ("Quelle ligne dessert Place Monge ?", "Uniquement la <strong>M7</strong>. Bus 47."),
            ("Qui est Gaspard Monge ?", "<strong>Gaspard Monge</strong> (1746-1818), <strong>mathématicien français</strong>, <strong>fondateur de la géométrie descriptive</strong>. <strong>Cofondateur de l'École polytechnique</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>26 avril 1930</strong>."),
            ("Pour le Jardin des Plantes ?", "<strong>~5 min à pied</strong>."),
            ("Pour les Arènes de Lutèce ?", "<strong>~3 min à pied</strong>. Vestiges gallo-romains."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Arènes de Lutèce</strong> à 3 min : vestiges gallo-romains (Ier-IIe siècle).",
            "<strong>Jardin des Plantes</strong> à 5 min : Muséum d'Histoire Naturelle.",
            "<strong>Quartier Latin</strong> : Sorbonne, librairies, cafés.",
            "<strong>Mosquée de Paris</strong> à 7 min à pied.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("📐", "Monge et la géométrie descriptive", "<strong>Gaspard Monge</strong> (1746-1818), <strong>mathématicien français</strong> et <strong>fondateur de la géométrie descriptive</strong>. Cette <strong>branche des mathématiques</strong> permet la <strong>représentation graphique précise</strong> d'objets en trois dimensions sur un plan (deux vues : élévation et plan). <strong>Application majeure dans l'ingénierie, l'architecture, l'industrie</strong>. <strong>Cofondateur de l'École polytechnique</strong> en <strong>1794</strong> avec <strong>Lazare Carnot</strong>. <strong>Ministre de la Marine</strong> sous la Convention. <strong>Sénateur sous l'Empire</strong>."),
            ("🏛️", "Arènes de Lutèce (Ier-IIe siècle)", "Les <strong>Arènes de Lutèce</strong>, à 3 min à pied, sont l'un des <strong>vestiges gallo-romains</strong> les plus importants de Paris. Construites au <strong>Ier siècle</strong> après J.-C. <strong>Amphithéâtre</strong> pouvant accueillir <strong>15 000 spectateurs</strong>. Combats de gladiateurs et représentations théâtrales. <strong>Redécouvert en 1869</strong> lors du percement de la <strong>rue Monge</strong>. <strong>Restauré</strong> au début du XXe siècle. Aujourd'hui square public.")
        ],
        "itin": [
            ("Arènes de Lutèce", "place-monge", "à pied", "Rue Monge (3 min)", 3),
            ("Jardin des Plantes", "jussieu", "M7 + à pied", "M7 → Jussieu + à pied", 5),
            ("Mosquée de Paris", "place-monge", "à pied", "Place du Puits-de-l'Ermite (7 min)", 7),
            ("Sorbonne", "cluny-la-sorbonne", "M7 + M10", "M7 → Jussieu + M10", 10),
            ("Notre-Dame de Paris", "saint-michel-notre-dame", "M7 + à pied", "À pied (15 min)", 15),
            ("Châtelet", "chatelet", "M7", "M7 directe (~8 min)", 8)
        ]
    },
    "censier-daubenton": {
        "addr": "Rue Censier, 75005 Paris", "arr": "5e arrondissement (Paris)",
        "seo": "Station Censier - Daubenton (M7) rue Censier dans le 5e. Hommage à Louis Jean-Marie Daubenton, naturaliste. Mosquée de Paris à proximité.",
        "tagline": "M7 — Daubenton, naturaliste et Mosquée de Paris",
        "hero_desc": "Station <strong>Censier - Daubenton</strong> sur la <strong>rue Censier</strong> dans le <strong>5e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>15 février 1931</strong>. Hommage à <strong>Louis Jean-Marie Daubenton</strong> (<strong>1716-1800</strong>), <strong>naturaliste français</strong>. <strong>Mosquée de Paris</strong> à proximité.",
        "intros": [
            "La station <strong>Censier - Daubenton</strong> est implantée sur la <strong>rue Censier</strong> dans le <strong>5e arrondissement</strong>. Elle est desservie par la <strong>M7</strong>, entre <strong>Place Monge</strong> (1 station) et <strong>Les Gobelins</strong> (1 station). Bus 47, 89.",
            "Ouverte le <strong>15 février 1931</strong> avec le <strong>prolongement de la M7</strong> de <strong>Place Monge à Porte d'Italie</strong>.",
            "Le nom <strong>Daubenton</strong> rend hommage à <strong>Louis Jean-Marie Daubenton</strong> (<strong>1716-1800</strong>), <strong>naturaliste français</strong>, <strong>collaborateur de Buffon</strong> à l'<strong>Histoire naturelle</strong>. À proximité : la <strong>Mosquée de Paris</strong> (1926) et le <strong>Jardin des Plantes</strong>."
        ],
        "hist_title": "1931 : prolongement et naturaliste Daubenton",
        "hist": [
            "La station Censier - Daubenton est <strong>inaugurée le 15 février 1931</strong> avec le <strong>prolongement de la M7</strong> de <strong>Place Monge à Porte d'Italie</strong>.",
            "Le nom <strong>Daubenton</strong> rend hommage à <strong>Louis Jean-Marie Daubenton</strong> (<strong>29 mai 1716 - 1er janvier 1800</strong>), <strong>naturaliste français</strong>. <strong>Collaborateur de Buffon</strong> à l'<strong>Histoire naturelle</strong> (1749-1789). <strong>Membre de l'Académie des sciences</strong>. <strong>Garde du Cabinet du roi</strong> au <strong>Jardin du Roi</strong> (futur Muséum). <strong>Professeur d'histoire naturelle</strong> au Collège de France et à l'École vétérinaire d'Alfort.",
            "À proximité : la <strong>Grande Mosquée de Paris</strong>, <strong>inaugurée le 15 juillet 1926</strong> en hommage aux <strong>soldats musulmans</strong> tombés pendant la <strong>Première Guerre mondiale</strong>. Architecture <strong>hispano-mauresque</strong>. <strong>Patio</strong>, <strong>salle de prière</strong>, <strong>hammam</strong>, <strong>restaurant</strong>, <strong>salon de thé</strong>. Le <strong>Jardin des Plantes</strong> et le <strong>Muséum d'Histoire Naturelle</strong> sont également à proximité."
        ],
        "faq": [
            ("Quelle ligne dessert Censier - Daubenton ?", "Uniquement la <strong>M7</strong>. Bus 47, 89."),
            ("Qui est Daubenton ?", "<strong>Louis Jean-Marie Daubenton</strong> (1716-1800), <strong>naturaliste français</strong>, <strong>collaborateur de Buffon</strong> à l'<strong>Histoire naturelle</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>15 février 1931</strong>."),
            ("Pour la Mosquée de Paris ?", "<strong>~5 min à pied</strong>. Inaugurée en 1926, architecture hispano-mauresque."),
            ("Pour le Jardin des Plantes ?", "<strong>~7 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Mosquée de Paris</strong> à 5 min : architecture hispano-mauresque (1926).",
            "<strong>Jardin des Plantes</strong> et <strong>Muséum d'Histoire Naturelle</strong> à 7 min.",
            "<strong>Marché Maubert</strong> et <strong>Quartier Latin</strong> à proximité.",
            "Pour <strong>Place d'Italie</strong> : <strong>M7 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🐎", "Daubenton, naturaliste de l'Histoire naturelle", "<strong>Louis Jean-Marie Daubenton</strong> (1716-1800), <strong>naturaliste français</strong>, <strong>collaborateur de Buffon</strong> à l'<strong>Histoire naturelle, générale et particulière</strong> (1749-1804). Daubenton rédigea les <strong>descriptions anatomiques détaillées</strong> des animaux pour les <strong>36 volumes</strong> de l'œuvre. <strong>Garde du Cabinet du roi</strong> au <strong>Jardin du Roi</strong> (futur Muséum d'Histoire Naturelle). <strong>Premier directeur</strong> du <strong>Muséum</strong> en 1793. <strong>Introduction des mérinos</strong> en France."),
            ("🕌", "Mosquée de Paris (1926)", "La <strong>Grande Mosquée de Paris</strong>, à 5 min à pied, est <strong>inaugurée le 15 juillet 1926</strong> par le <strong>président Gaston Doumergue</strong>. <strong>Architecture hispano-mauresque</strong>, inspirée de l'<strong>Alhambra de Grenade</strong>. Construite en hommage aux <strong>70 000 soldats musulmans</strong> tombés pour la France pendant la <strong>Première Guerre mondiale</strong>. <strong>Minaret</strong> de 33 m. <strong>Patio</strong>, <strong>salle de prière</strong>, <strong>hammam</strong>, <strong>restaurant</strong>, <strong>salon de thé</strong>. <strong>Classée monument historique en 1983</strong>.")
        ],
        "itin": [
            ("Mosquée de Paris", "place-monge", "à pied", "5 min à pied", 5),
            ("Jardin des Plantes", "jussieu", "à pied", "7 min à pied", 7),
            ("Muséum d'Histoire Naturelle", "jussieu", "à pied", "Jardin des Plantes (7 min)", 7),
            ("Les Gobelins (Manufacture)", "les-gobelins", "M7", "M7 directe (1 station)", 2),
            ("Place d'Italie", "place-d-italie", "M7", "M7 directe (2 stations)", 4),
            ("Châtelet", "chatelet", "M7", "M7 directe (~10 min)", 10)
        ]
    },
    "les-gobelins": {
        "addr": "Avenue des Gobelins, 75013 Paris", "arr": "13e arrondissement (Paris)",
        "seo": "Station Les Gobelins (M7) avenue des Gobelins dans le 13e. Manufacture des Gobelins (tapisseries royales depuis 1662). Galerie des Gobelins.",
        "tagline": "M7 — Manufacture des Gobelins (1662)",
        "hero_desc": "Station <strong>Les Gobelins</strong> sur l'<strong>avenue des Gobelins</strong> dans le <strong>13e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>15 février 1931</strong>. À proximité : la <strong>Manufacture des Gobelins</strong>, célèbre <strong>manufacture de tapisseries royales</strong> depuis <strong>1662</strong>.",
        "intros": [
            "La station <strong>Les Gobelins</strong> est implantée sur l'<strong>avenue des Gobelins</strong> dans le <strong>13e arrondissement</strong>. Elle est desservie par la <strong>M7</strong>, entre <strong>Censier - Daubenton</strong> (1 station) et <strong>Place d'Italie</strong> (1 station). Bus 27, 47, 83, 91.",
            "Ouverte le <strong>15 février 1931</strong> avec le <strong>prolongement de la M7</strong> de Place Monge à Porte d'Italie.",
            "À proximité : la <strong>Manufacture des Gobelins</strong>, célèbre <strong>manufacture de tapisseries royales</strong> fondée en <strong>1662</strong> par <strong>Colbert</strong> sous <strong>Louis XIV</strong>. La <strong>Galerie des Gobelins</strong>, ouverte au public, expose les <strong>tapisseries</strong>, <strong>tapis</strong> et <strong>mobilier</strong> produits."
        ],
        "hist_title": "1931 : Manufacture des Gobelins (1662, Colbert)",
        "hist": [
            "La station Les Gobelins est <strong>inaugurée le 15 février 1931</strong> avec le <strong>prolongement de la M7</strong>.",
            "La <strong>Manufacture des Gobelins</strong>, à proximité, est fondée en <strong>1662</strong> par <strong>Jean-Baptiste Colbert</strong>, ministre de <strong>Louis XIV</strong>. Installée dans une <strong>ancienne teinturerie</strong> de la <strong>famille Gobelin</strong> (XVe siècle). <strong>Manufacture royale</strong> chargée de produire les <strong>tapisseries</strong> destinées au <strong>roi et à la cour</strong>.",
            "Sous <strong>Charles Le Brun</strong>, <strong>directeur de 1663 à 1690</strong>, la manufacture atteint son <strong>apogée artistique</strong>. <strong>Tapisseries des séries de Louis XIV</strong>, <strong>Tentures des Saisons</strong>, <strong>Histoire d'Alexandre</strong>. <strong>Mobilier National</strong> aujourd'hui. <strong>Galerie des Gobelins</strong> ouverte au public depuis 2007. <strong>Inscrite aux monuments historiques</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Les Gobelins ?", "Uniquement la <strong>M7</strong>. Bus 27, 47, 83, 91."),
            ("Qu'est-ce que la Manufacture des Gobelins ?", "<strong>Manufacture royale de tapisseries</strong> fondée en <strong>1662</strong> par <strong>Colbert</strong> sous Louis XIV. Aujourd'hui rattachée au <strong>Mobilier National</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>15 février 1931</strong>."),
            ("Peut-on visiter la Manufacture ?", "<strong>Oui</strong>. <strong>Galerie des Gobelins</strong> ouverte au public depuis 2007. <strong>Visites des ateliers</strong> sur réservation."),
            ("Pour Place d'Italie ?", "<strong>M7 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Manufacture des Gobelins</strong> à 3 min : tapisseries royales depuis 1662.",
            "<strong>Galerie des Gobelins</strong> ouverte au public : tapisseries et mobilier.",
            "<strong>Quartier Butte-aux-Cailles</strong> à 10 min à pied.",
            "Pour <strong>Place d'Italie</strong> : <strong>M7 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎨", "Manufacture des Gobelins (1662)", "La <strong>Manufacture des Gobelins</strong>, à 3 min à pied, est fondée en <strong>1662</strong> par <strong>Jean-Baptiste Colbert</strong>, ministre de <strong>Louis XIV</strong>. <strong>Manufacture royale</strong> chargée de produire les <strong>tapisseries</strong> destinées au <strong>roi et à la cour</strong>. Sous <strong>Charles Le Brun</strong> (directeur 1663-1690), elle atteint son <strong>apogée artistique</strong>. <strong>Tapisseries célèbres</strong> : <strong>Histoire d'Alexandre</strong>, <strong>Histoire du Roi</strong>, <strong>Tentures des Saisons</strong>. <strong>Mobilier National</strong> aujourd'hui. <strong>Galerie ouverte au public</strong>."),
            ("🏛️", "Galerie des Gobelins (2007)", "La <strong>Galerie des Gobelins</strong>, à proximité de la station, est <strong>ouverte au public</strong> depuis le <strong>14 novembre 2007</strong>. Conçue par l'architecte <strong>Jean-Loup Roubert</strong>. <strong>Expositions de tapisseries, tapis et mobilier</strong> produits par la manufacture et le <strong>Mobilier National</strong>. <strong>Visites des ateliers</strong> sur réservation : on peut y observer les <strong>tisserands au travail</strong> selon les <strong>techniques de haute lisse et basse lisse</strong>.")
        ],
        "itin": [
            ("Manufacture des Gobelins", "les-gobelins", "à pied", "Sortie directe (3 min)", 3),
            ("Place d'Italie", "place-d-italie", "M7", "M7 directe (1 station)", 2),
            ("Butte-aux-Cailles", "corvisart", "M6 + à pied", "À pied (10 min)", 10),
            ("Jardin des Plantes", "jussieu", "M7", "M7 directe (3 stations)", 6),
            ("Châtelet", "chatelet", "M7", "M7 directe (~12 min)", 12),
            ("Opéra Garnier", "opera", "M7", "M7 directe (~14 min)", 14)
        ]
    },
    "tolbiac": {
        "addr": "Avenue d'Italie, 75013 Paris", "arr": "13e arrondissement (Paris)",
        "seo": "Station Tolbiac (M7) avenue d'Italie dans le 13e. Hommage à la bataille de Tolbiac (496) victoire de Clovis sur les Alamans.",
        "tagline": "M7 — Tolbiac, bataille de Clovis (496)",
        "hero_desc": "Station <strong>Tolbiac</strong> sur l'<strong>avenue d'Italie</strong> dans le <strong>13e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>7 mars 1930</strong>. Hommage à la <strong>bataille de Tolbiac</strong> (<strong>496</strong>), <strong>victoire de Clovis</strong> sur les Alamans.",
        "intros": [
            "La station <strong>Tolbiac</strong> est implantée sur l'<strong>avenue d'Italie</strong> dans le <strong>13e arrondissement</strong>. Elle est desservie par la <strong>M7</strong>, entre <strong>Place d'Italie</strong> (1 station) et <strong>Maison Blanche</strong> (1 station). Bus 47, 62, 67, 83.",
            "Ouverte le <strong>7 mars 1930</strong> avec le <strong>prolongement de la M7</strong> de <strong>Place d'Italie à Porte d'Ivry</strong>.",
            "Le nom <strong>Tolbiac</strong> rend hommage à la <strong>bataille de Tolbiac</strong> (<strong>496 ou 506 selon les sources</strong>), <strong>victoire de Clovis Ier</strong>, <strong>roi des Francs</strong>, sur les <strong>Alamans</strong>. Cette victoire conduisit à la <strong>conversion de Clovis</strong> au <strong>christianisme</strong>."
        ],
        "hist_title": "1930 : Tolbiac, victoire de Clovis (496)",
        "hist": [
            "La station Tolbiac est <strong>inaugurée le 7 mars 1930</strong> avec le <strong>prolongement de la M7</strong>.",
            "Le nom <strong>Tolbiac</strong> rend hommage à la <strong>bataille de Tolbiac</strong> (<strong>496 ou 506 selon les sources</strong>), <strong>victoire de Clovis Ier</strong> (<strong>466-511</strong>), <strong>roi des Francs</strong>, sur les <strong>Alamans</strong>. <strong>Tolbiac</strong> est aujourd'hui identifiée à <strong>Zülpich</strong> en Allemagne (Rhénanie-du-Nord-Westphalie).",
            "Selon la <strong>tradition</strong>, lors de la bataille, en <strong>difficulté</strong>, Clovis aurait <strong>promis</strong> de se convertir au <strong>christianisme</strong> s'il remportait la victoire. Sa <strong>victoire</strong> conduisit à son <strong>baptême par saint Remi à Reims</strong> en <strong>496 ou 498</strong>. Cet événement marque le <strong>début de l'alliance</strong> entre la <strong>monarchie franque</strong> et l'<strong>Église catholique</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Tolbiac ?", "Uniquement la <strong>M7</strong>. Bus 47, 62, 67, 83."),
            ("Qu'est-ce que la bataille de Tolbiac ?", "<strong>Victoire de Clovis Ier</strong>, roi des Francs, sur les <strong>Alamans</strong> en <strong>496</strong>. Conduit à sa <strong>conversion au christianisme</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>7 mars 1930</strong>."),
            ("Où se trouvait Tolbiac ?", "Aujourd'hui identifiée à <strong>Zülpich</strong> en Allemagne (Rhénanie-du-Nord-Westphalie)."),
            ("Pour Place d'Italie ?", "<strong>M7 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Place d'Italie</strong> et son centre commercial à <strong>M7 directe</strong> (1 station).",
            "<strong>Avenue d'Italie</strong> : axe commercial du 13e.",
            "<strong>Chinatown</strong> (13e) à proximité.",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⚔️", "Bataille de Tolbiac (496)", "La <strong>bataille de Tolbiac</strong>, en <strong>496 ou 506</strong>, est une <strong>victoire décisive de Clovis Ier</strong> (<strong>466-511</strong>), <strong>roi des Francs</strong>, sur les <strong>Alamans</strong>. <strong>Tolbiac</strong> est aujourd'hui identifiée à <strong>Zülpich</strong> en Allemagne. Selon la <strong>tradition</strong>, en <strong>difficulté</strong> au cours de la bataille, Clovis aurait <strong>promis</strong> de se convertir au <strong>christianisme</strong> s'il remportait la victoire. Sa victoire conduisit à son <strong>baptême par saint Remi à Reims</strong> en <strong>496 ou 498</strong>. <strong>Événement fondateur</strong> de l'alliance entre <strong>monarchie franque</strong> et <strong>Église catholique</strong>."),
            ("👑", "Clovis Ier, premier roi des Francs chrétien", "<strong>Clovis Ier</strong> (<strong>466-511</strong>), <strong>roi des Francs</strong> de la <strong>dynastie mérovingienne</strong>. <strong>Unifie les tribus franques</strong>. <strong>Conquiert la Gaule</strong> sur les <strong>Romains</strong> (victoire de Soissons en 486) et sur les <strong>Wisigoths</strong> (victoire de Vouillé en 507). <strong>Premier roi des Francs chrétien</strong>. <strong>Baptisé à Reims</strong> par <strong>saint Remi</strong>. <strong>Considéré comme le fondateur</strong> de la <strong>monarchie française</strong>.")
        ],
        "itin": [
            ("Place d'Italie", "place-d-italie", "M7", "M7 directe (1 station)", 2),
            ("Chinatown (13e)", "place-d-italie", "M7 + à pied", "M7 → Porte de Choisy", 5),
            ("Maison Blanche", "maison-blanche", "M7", "M7 directe (1 station)", 2),
            ("Châtelet", "chatelet", "M7", "M7 directe (~14 min)", 14),
            ("Opéra", "opera", "M7", "M7 directe (~16 min)", 16),
            ("Gare de l'Est", "gare-de-l-est", "M7", "M7 directe (~22 min)", 22)
        ]
    },
    "porte-d-italie": {
        "addr": "Avenue d'Italie, 75013 Paris", "arr": "13e arrondissement (Paris)",
        "seo": "Station Porte d'Italie (M7) avenue d'Italie dans le 13e. Limite sud Paris, tramway T3a. Quartier Chinatown.",
        "tagline": "M7 — porte sud, tramway T3a, Chinatown",
        "hero_desc": "Station <strong>Porte d'Italie</strong> sur l'<strong>avenue d'Italie</strong> dans le <strong>13e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>15 février 1931</strong>. Correspondance <strong>tramway T3a</strong>. À proximité du <strong>Chinatown</strong> du 13e.",
        "intros": [
            "La station <strong>Porte d'Italie</strong> est implantée sur l'<strong>avenue d'Italie</strong>, à la <strong>limite sud du 13e arrondissement</strong>. Elle est desservie par la <strong>M7</strong> et le <strong>tramway T3a</strong>, entre <strong>Maison Blanche</strong> (1 station) et <strong>Le Kremlin-Bicêtre</strong> (1 station, banlieue). Bus 47, 67, 184, 185.",
            "Ouverte le <strong>15 février 1931</strong> comme <strong>terminus sud temporaire</strong> de la M7 (jusqu'au prolongement vers Mairie d'Ivry en 1946).",
            "À proximité : le <strong>Chinatown du 13e arrondissement</strong>, principal quartier asiatique de Paris (avenues de Choisy, d'Ivry, Porte d'Ivry). <strong>Tramway T3a</strong> en correspondance directe."
        ],
        "hist_title": "1931 : porte sud et Chinatown 13e",
        "hist": [
            "La station Porte d'Italie est <strong>inaugurée le 15 février 1931</strong> comme <strong>terminus sud temporaire</strong> de la M7 (extension vers Mairie d'Ivry en 1946).",
            "À proximité : le <strong>Chinatown du 13e arrondissement</strong>, <strong>principal quartier asiatique de Paris</strong>. Formé à partir de <strong>1975</strong> avec l'<strong>arrivée des réfugiés d'Asie du Sud-Est</strong> (<strong>Vietnam, Cambodge, Laos</strong>). Plus de <strong>200 commerces asiatiques</strong>, restaurants, supermarchés. <strong>Défilé du Nouvel An chinois</strong> chaque année.",
            "Le <strong>tramway T3a</strong>, en correspondance directe, est <strong>inauguré en 2006</strong>. Circule sur les <strong>boulevards des Maréchaux</strong> au sud de Paris. <strong>~12 km</strong>, <strong>~150 000 voyageurs/jour</strong>. Remplace l'ancienne <strong>PC1</strong> (Petite Ceinture)."
        ],
        "faq": [
            ("Quelles lignes desservent Porte d'Italie ?", "<strong>M7</strong> et <strong>tramway T3a</strong>. Bus 47, 67, 184, 185."),
            ("Quand a-t-elle ouvert ?", "Le <strong>15 février 1931</strong>."),
            ("Pour le Chinatown ?", "<strong>~5 min à pied</strong> via les avenues de Choisy et d'Ivry."),
            ("Pour Le Kremlin-Bicêtre ?", "<strong>M7 directe</strong> (1 station, banlieue 94)."),
            ("Pour Place d'Italie ?", "<strong>M7 directe</strong> (3 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Chinatown</strong> à 5 min à pied : restaurants et commerces asiatiques.",
            "<strong>Nouvel An chinois</strong> dans le 13e chaque année.",
            "<strong>Tramway T3a</strong> en correspondance directe.",
            "Pour <strong>Le Kremlin-Bicêtre</strong> et l'<strong>hôpital Bicêtre</strong> : <strong>M7 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🇨🇳", "Chinatown du 13e", "Le <strong>Chinatown du 13e arrondissement</strong>, à 5 min à pied, est le <strong>principal quartier asiatique de Paris</strong>. Formé à partir de <strong>1975</strong> avec l'<strong>arrivée des réfugiés d'Asie du Sud-Est</strong> (<strong>Vietnam, Cambodge, Laos</strong>). S'étend autour des <strong>avenues de Choisy, d'Ivry et de la Porte d'Ivry</strong>. Plus de <strong>200 commerces asiatiques</strong>, <strong>restaurants vietnamiens, chinois, thaïlandais</strong>, <strong>supermarchés</strong> (Tang Frères, Paris Store). <strong>Défilé du Nouvel An chinois</strong> chaque année, l'un des plus importants d'Europe."),
            ("🚊", "Tramway T3a (2006)", "Le <strong>tramway T3a</strong>, en correspondance directe, est <strong>inauguré le 16 décembre 2006</strong>. Circule sur les <strong>boulevards des Maréchaux</strong> au sud de Paris entre <strong>Pont du Garigliano</strong> et <strong>Porte d'Ivry</strong> (prolongé jusqu'à <strong>Porte de Vincennes</strong> en 2012). <strong>~12 km</strong>, <strong>~150 000 voyageurs/jour</strong>. <strong>Premier tramway de Paris intra-muros</strong> moderne.")
        ],
        "itin": [
            ("Chinatown 13e", "porte-de-choisy", "M7", "M7 directe (1 station)", 2),
            ("Tramway T3a", "porte-d-italie", "T3a", "Correspondance directe", 1),
            ("Place d'Italie", "place-d-italie", "M7", "M7 directe (3 stations)", 6),
            ("Le Kremlin-Bicêtre", "le-kremlin-bicetre", "M7", "M7 directe (1 station)", 2),
            ("Châtelet", "chatelet", "M7", "M7 directe (~18 min)", 18),
            ("Opéra", "opera", "M7", "M7 directe (~20 min)", 20)
        ]
    },
    "porte-de-choisy": {
        "addr": "Avenue de Choisy, 75013 Paris", "arr": "13e arrondissement (Paris)",
        "seo": "Station Porte de Choisy (M7) avenue de Choisy dans le 13e. Cœur du Chinatown parisien. Tramway T3a en correspondance.",
        "tagline": "M7 — Porte de Choisy, cœur du Chinatown",
        "hero_desc": "Station <strong>Porte de Choisy</strong> sur l'<strong>avenue de Choisy</strong> dans le <strong>13e arrondissement</strong>. Desservie par la <strong>M7</strong>, ouverte le <strong>15 février 1931</strong>. Correspondance <strong>tramway T3a</strong>. <strong>Cœur du Chinatown</strong> parisien.",
        "intros": [
            "La station <strong>Porte de Choisy</strong> est implantée sur l'<strong>avenue de Choisy</strong>, à la <strong>limite sud du 13e arrondissement</strong>. Elle est desservie par la <strong>M7</strong> (branche Mairie d'Ivry) et le <strong>tramway T3a</strong>. Bus 27, 47, 83, 183.",
            "Ouverte le <strong>15 février 1931</strong>.",
            "À la sortie : le <strong>cœur du Chinatown</strong> du 13e. <strong>Avenues de Choisy et d'Ivry</strong> : <strong>commerces asiatiques</strong>, <strong>supermarchés</strong> (Tang Frères, Paris Store), <strong>restaurants vietnamiens, chinois, thaïlandais</strong>. <strong>Tramway T3a</strong> en correspondance directe."
        ],
        "hist_title": "1931 : Porte de Choisy et Chinatown",
        "hist": [
            "La station Porte de Choisy est <strong>inaugurée le 15 février 1931</strong> avec le <strong>prolongement de la M7</strong>.",
            "Le quartier autour de la station est le <strong>cœur du Chinatown du 13e</strong>, principal quartier asiatique de Paris. <strong>Avenues de Choisy et d'Ivry</strong> : artères commerçantes principales. Les <strong>supermarchés Tang Frères et Paris Store</strong>, fondés dans les années 1970-1980 par les frères <strong>Tang</strong>, sont les <strong>plus grands d'Europe</strong> dans la spécialité asiatique.",
            "Le <strong>tramway T3a</strong>, en correspondance directe, est <strong>inauguré en 2006</strong>. Permet la <strong>desserte des boulevards des Maréchaux</strong> au sud de Paris."
        ],
        "faq": [
            ("Quelles lignes desservent Porte de Choisy ?", "<strong>M7</strong> (branche Mairie d'Ivry) et <strong>tramway T3a</strong>. Bus 27, 47, 83, 183."),
            ("Quand a-t-elle ouvert ?", "Le <strong>15 février 1931</strong>."),
            ("Pour le Chinatown ?", "<strong>Sortie directe</strong>. Cœur du quartier asiatique du 13e."),
            ("Pour Tang Frères ?", "<strong>~3 min à pied</strong> avenue d'Ivry."),
            ("Pour le Nouvel An chinois ?", "<strong>Défilé annuel</strong> dans le 13e (fin janvier / février selon les années)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Cœur du Chinatown</strong> à la sortie : commerces et restaurants asiatiques.",
            "<strong>Tang Frères</strong> à 3 min : plus grand supermarché asiatique d'Europe.",
            "<strong>Défilé du Nouvel An chinois</strong> chaque année (fin janvier / février).",
            "<strong>Tramway T3a</strong> en correspondance directe.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🛍️", "Tang Frères, supermarché asiatique iconique", "<strong>Tang Frères</strong>, à 3 min à pied avenue d'Ivry, est l'un des <strong>plus grands supermarchés asiatiques d'Europe</strong>. Fondé en <strong>1976</strong> par les frères <strong>Bun, Hong, Mong, Lee Tang</strong>, réfugiés du <strong>Cambodge</strong>. <strong>Plusieurs magasins</strong> dans le 13e. <strong>Produits asiatiques</strong> : sauces, épices, légumes, poissons, viandes, bonbons, jouets, ustensiles. <strong>Atmosphère caractéristique</strong> du Chinatown parisien."),
            ("🎉", "Défilé du Nouvel An chinois", "Le <strong>défilé du Nouvel An chinois</strong> dans le <strong>13e arrondissement</strong> est l'un des <strong>plus importants d'Europe</strong>. Organisé chaque année <strong>fin janvier ou février</strong> selon le calendrier lunaire. <strong>Dragons</strong>, <strong>lions</strong>, <strong>danseurs</strong>, <strong>fanfares</strong> défilent sur les <strong>avenues de Choisy et d'Ivry</strong>. <strong>~200 000 spectateurs</strong>.")
        ],
        "itin": [
            ("Tang Frères", "porte-de-choisy", "à pied", "Avenue d'Ivry (3 min)", 3),
            ("Place d'Italie", "place-d-italie", "M7", "M7 directe (3 stations)", 6),
            ("Tramway T3a", "porte-de-choisy", "T3a", "Correspondance directe", 1),
            ("Porte d'Ivry", "porte-d-ivry", "M7", "M7 directe (1 station)", 2),
            ("Châtelet", "chatelet", "M7", "M7 directe (~18 min)", 18),
            ("Mairie d'Ivry (terminus)", "mairie-d-ivry", "M7", "M7 directe (3 stations)", 6)
        ]
    },
    "le-kremlin-bicetre": {
        "addr": "Avenue de Fontainebleau, 94270 Le Kremlin-Bicêtre", "arr": "Le Kremlin-Bicêtre (94)",
        "seo": "Station Le Kremlin-Bicêtre (M7) au Kremlin-Bicêtre (94). Hôpital Bicêtre (XVIIe) à proximité. Étymologie russe « kremlin ».",
        "tagline": "M7 — Le Kremlin-Bicêtre, hôpital historique",
        "hero_desc": "Station <strong>Le Kremlin-Bicêtre</strong> à <strong>Le Kremlin-Bicêtre</strong> (Val-de-Marne, 94). Desservie par la <strong>M7</strong>, ouverte le <strong>10 février 1982</strong>. À proximité de l'<strong>hôpital Bicêtre</strong>, ancien <strong>hôpital général</strong> fondé au <strong>XVIIe siècle</strong>.",
        "intros": [
            "La station <strong>Le Kremlin-Bicêtre</strong> est implantée à <strong>Le Kremlin-Bicêtre</strong> (Val-de-Marne, 94), à la <strong>limite sud de Paris</strong>. Elle est desservie par la <strong>M7</strong> (branche Villejuif), entre <strong>Porte d'Italie</strong> (1 station, Paris) et <strong>Villejuif - Léo Lagrange</strong> (1 station). Bus 47, 131, 185.",
            "Ouverte le <strong>10 février 1982</strong> avec le <strong>prolongement de la M7</strong> de <strong>Porte d'Italie à Villejuif - Louis Aragon</strong>.",
            "Le nom <strong>Le Kremlin-Bicêtre</strong> combine deux références. <strong>Bicêtre</strong> rappelle l'<strong>hôpital Bicêtre</strong> historique. <strong>Kremlin</strong> vient d'une <strong>auberge russe</strong> dénommée <strong>« Au sergent du Kremlin »</strong>, ouverte au début du XIXe siècle après la <strong>campagne de Russie</strong> de Napoléon."
        ],
        "hist_title": "1982 : hôpital Bicêtre et auberge du Kremlin",
        "hist": [
            "La station Le Kremlin-Bicêtre est <strong>inaugurée le 10 février 1982</strong> avec le <strong>prolongement de la M7</strong> de Porte d'Italie à Villejuif - Louis Aragon.",
            "Le nom <strong>Bicêtre</strong> rappelle l'<strong>hôpital Bicêtre</strong>, ancien <strong>hôpital général</strong> fondé au <strong>XVIIe siècle</strong>. Construit sur un terrain ayant appartenu à <strong>Jean, évêque de Winchester</strong> (XIIIe siècle), d'où l'étymologie <strong>« Bicêtre »</strong> (déformation de Winchester). Aujourd'hui établissement de l'<strong>Assistance publique - Hôpitaux de Paris (AP-HP)</strong>.",
            "Le nom <strong>Kremlin</strong> vient d'une <strong>auberge russe</strong> dénommée <strong>« Au sergent du Kremlin »</strong>, ouverte au début du XIXe siècle dans la commune après la <strong>campagne de Russie</strong> de Napoléon (1812). Le nom de l'auberge fit fortune et la <strong>commune adopta « Le Kremlin »</strong> en <strong>1896</strong>, lors de sa séparation de Gentilly."
        ],
        "faq": [
            ("Quelle ligne dessert Le Kremlin-Bicêtre ?", "Uniquement la <strong>M7</strong> (branche Villejuif). Bus 47, 131, 185."),
            ("Quand a-t-elle ouvert ?", "Le <strong>10 février 1982</strong>."),
            ("D'où vient le nom Kremlin ?", "D'une <strong>auberge russe « Au sergent du Kremlin »</strong> du XIXe siècle. La commune adopta ce nom en <strong>1896</strong>."),
            ("Pour l'hôpital Bicêtre ?", "<strong>~5 min à pied</strong>. Hôpital de l'AP-HP."),
            ("Pour Paris centre ?", "<strong>M7 directe</strong> vers Châtelet (~20 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Hôpital Bicêtre</strong> à 5 min à pied : établissement AP-HP.",
            "<strong>Étymologie originale</strong> : auberge russe + Winchester.",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong>.",
            "Pour <strong>Villejuif - Louis Aragon</strong> (terminus) : <strong>M7 directe</strong> (3 stations).",
            "Zone tarifaire <strong>2</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("🏥", "Hôpital Bicêtre (XVIIe siècle)", "L'<strong>hôpital Bicêtre</strong>, à 5 min à pied, est un <strong>ancien hôpital général</strong> fondé au <strong>XVIIe siècle</strong>. Construit sur un terrain ayant appartenu à <strong>Jean, évêque de Winchester</strong> (XIIIe siècle), d'où l'étymologie <strong>« Bicêtre »</strong> (déformation de « Winchester »). Sous l'<strong>Ancien Régime</strong>, c'était un <strong>hôpital pour les pauvres, vieillards et aliénés</strong>. <strong>Philippe Pinel</strong> y exerça à la fin du XVIIIe (réforme du traitement des aliénés). Aujourd'hui <strong>établissement de l'AP-HP</strong>."),
            ("🇷🇺", "Auberge russe « Au sergent du Kremlin »", "Le <strong>Kremlin</strong> de la station n'a aucun rapport direct avec le Kremlin de Moscou. Il vient d'une <strong>auberge russe</strong> dénommée <strong>« Au sergent du Kremlin »</strong>, ouverte au début du <strong>XIXe siècle</strong> dans la commune. Cette auberge évoquait la <strong>campagne de Russie de Napoléon</strong> (1812) et les <strong>soldats français</strong> qui avaient combattu autour du <strong>Kremlin de Moscou</strong>. Le nom de l'auberge fit fortune. <strong>La commune adopta « Le Kremlin »</strong> en <strong>1896</strong>, lors de sa séparation de Gentilly.")
        ],
        "itin": [
            ("Hôpital Bicêtre", "le-kremlin-bicetre", "à pied", "Sortie + 5 min", 5),
            ("Villejuif - Louis Aragon (terminus)", "villejuif-louis-aragon", "M7", "M7 directe (3 stations)", 6),
            ("Porte d'Italie", "porte-d-italie", "M7", "M7 directe (1 station)", 2),
            ("Place d'Italie", "place-d-italie", "M7", "M7 directe (4 stations)", 8),
            ("Châtelet", "chatelet", "M7", "M7 directe (~20 min)", 20),
            ("Opéra", "opera", "M7", "M7 directe (~22 min)", 22)
        ]
    },
    "villejuif-leo-lagrange": {
        "addr": "Avenue de Stalingrad, 94800 Villejuif", "arr": "Villejuif (94)",
        "seo": "Station Villejuif - Léo Lagrange (M7) à Villejuif (94). Hommage à Léo Lagrange, homme politique du Front populaire.",
        "tagline": "M7 — Léo Lagrange, homme politique",
        "hero_desc": "Station <strong>Villejuif - Léo Lagrange</strong> à <strong>Villejuif</strong> (Val-de-Marne, 94). Desservie par la <strong>M7</strong>, ouverte le <strong>10 février 1982</strong>. Hommage à <strong>Léo Lagrange</strong> (<strong>1900-1940</strong>), <strong>homme politique français</strong>.",
        "intros": [
            "La station <strong>Villejuif - Léo Lagrange</strong> est implantée à <strong>Villejuif</strong> (Val-de-Marne, 94). Elle est desservie par la <strong>M7</strong>, entre <strong>Le Kremlin-Bicêtre</strong> (1 station) et <strong>Villejuif - Paul Vaillant-Couturier</strong> (1 station). Bus 131, 162, 185.",
            "Ouverte le <strong>10 février 1982</strong> avec le <strong>prolongement de la M7</strong>.",
            "Le nom <strong>Léo Lagrange</strong> rend hommage à <strong>Léo Lagrange</strong> (<strong>1900-1940</strong>), <strong>homme politique français</strong>. <strong>Député socialiste du Nord</strong>. <strong>Sous-secrétaire d'État aux Sports et à l'organisation des Loisirs</strong> dans le gouvernement <strong>Léon Blum</strong> (Front populaire, 1936-1937)."
        ],
        "hist_title": "1982 : prolongement et Léo Lagrange",
        "hist": [
            "La station est <strong>inaugurée le 10 février 1982</strong> avec le <strong>prolongement de la M7</strong>.",
            "Le nom <strong>Léo Lagrange</strong> rend hommage à <strong>Léo Lagrange</strong> (<strong>28 novembre 1900 - 9 juin 1940</strong>), <strong>homme politique français</strong>. <strong>Avocat</strong>, <strong>député socialiste du Nord</strong> à partir de 1932.",
            "<strong>Sous-secrétaire d'État aux Sports et à l'organisation des Loisirs</strong> dans le gouvernement de <strong>Léon Blum</strong> pendant le <strong>Front populaire</strong> (juin 1936 - juin 1937). <strong>Promoteur du tourisme social</strong>, des <strong>auberges de jeunesse</strong>, des <strong>loisirs populaires</strong>. <strong>Père du tourisme social français</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Villejuif - Léo Lagrange ?", "Uniquement la <strong>M7</strong>. Bus 131, 162, 185."),
            ("Qui est Léo Lagrange ?", "<strong>Léo Lagrange</strong> (1900-1940), <strong>homme politique français</strong>. <strong>Sous-secrétaire d'État aux Sports et aux Loisirs</strong> dans le gouvernement Léon Blum (Front populaire)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>10 février 1982</strong>."),
            ("Pour Villejuif - Louis Aragon (terminus) ?", "<strong>M7 directe</strong> (2 stations)."),
            ("Pour Châtelet ?", "<strong>M7 directe</strong> (~22 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "Quartier résidentiel de <strong>Villejuif</strong> (94).",
            "Pour <strong>Villejuif - Louis Aragon</strong> (terminus) : <strong>M7 directe</strong>.",
            "Pour <strong>hôpital Paul-Brousse</strong> : <strong>M7 directe</strong> (1 station vers Paul Vaillant-Couturier).",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("⛺", "Léo Lagrange et le tourisme social", "<strong>Léo Lagrange</strong> (1900-1940), <strong>avocat et député socialiste du Nord</strong>. <strong>Sous-secrétaire d'État aux Sports et à l'organisation des Loisirs</strong> sous <strong>Léon Blum</strong> (Front populaire, 1936-1937). <strong>Promoteur du tourisme social</strong>, des <strong>auberges de jeunesse</strong>, des <strong>congés payés actifs</strong>. <strong>Création des billets populaires SNCF</strong> à <strong>40 % de réduction</strong> pour les <strong>premiers congés payés</strong> en <strong>1936</strong>. <strong>Considéré comme le « père du tourisme social français »</strong>."),
            ("🏛️", "Villejuif, ville hospitalière", "<strong>Villejuif</strong> (~57 000 habitants), commune du <strong>Val-de-Marne</strong>, est connue pour son <strong>pôle hospitalier majeur</strong> : <strong>hôpital Paul-Brousse</strong>, <strong>Institut Gustave-Roussy</strong> (cancérologie de référence européenne), <strong>hôpital Le Roy-des-Belges</strong>. <strong>Ancienne commune rurale</strong>, en transformation urbaine.")
        ],
        "itin": [
            ("Villejuif - Louis Aragon (terminus)", "villejuif-louis-aragon", "M7", "M7 directe (2 stations)", 4),
            ("Hôpital Paul-Brousse", "villejuif-paul-vaillant-couturier", "M7", "M7 directe (1 station)", 2),
            ("Le Kremlin-Bicêtre", "le-kremlin-bicetre", "M7", "M7 directe (1 station)", 2),
            ("Porte d'Italie", "porte-d-italie", "M7", "M7 directe (2 stations)", 4),
            ("Place d'Italie", "place-d-italie", "M7", "M7 directe (5 stations)", 10),
            ("Châtelet", "chatelet", "M7", "M7 directe (~22 min)", 22)
        ]
    },
    "villejuif-paul-vaillant-couturier": {
        "addr": "Avenue de Stalingrad, 94800 Villejuif", "arr": "Villejuif (94)",
        "seo": "Station Villejuif - Paul Vaillant-Couturier (M7) à Villejuif (94). Hommage à Paul Vaillant-Couturier, écrivain et journaliste. Hôpital Paul-Brousse.",
        "tagline": "M7 — Paul Vaillant-Couturier, écrivain et hôpital",
        "hero_desc": "Station <strong>Villejuif - Paul Vaillant-Couturier</strong> à <strong>Villejuif</strong> (Val-de-Marne, 94). Desservie par la <strong>M7</strong>, ouverte le <strong>10 février 1982</strong>. Hommage à <strong>Paul Vaillant-Couturier</strong> (<strong>1892-1937</strong>), <strong>écrivain et journaliste français</strong>. À proximité de l'<strong>hôpital Paul-Brousse</strong>.",
        "intros": [
            "La station <strong>Villejuif - Paul Vaillant-Couturier</strong> est implantée à <strong>Villejuif</strong> (Val-de-Marne, 94). Elle est desservie par la <strong>M7</strong>, entre <strong>Villejuif - Léo Lagrange</strong> (1 station) et <strong>Villejuif - Louis Aragon</strong> (1 station, terminus). Bus 131, 162, 185.",
            "Ouverte le <strong>10 février 1982</strong> avec le <strong>prolongement de la M7</strong>.",
            "Le nom <strong>Paul Vaillant-Couturier</strong> rend hommage à <strong>Paul Vaillant-Couturier</strong> (<strong>1892-1937</strong>), <strong>écrivain et journaliste français</strong>. <strong>Maire de Villejuif</strong> de <strong>1929 à 1937</strong>. À proximité : l'<strong>hôpital Paul-Brousse</strong> (AP-HP) et l'<strong>Institut Gustave-Roussy</strong>."
        ],
        "hist_title": "1982 : prolongement et Vaillant-Couturier",
        "hist": [
            "La station est <strong>inaugurée le 10 février 1982</strong> avec le <strong>prolongement de la M7</strong>.",
            "Le nom <strong>Paul Vaillant-Couturier</strong> rend hommage à <strong>Paul Vaillant-Couturier</strong> (<strong>8 janvier 1892 - 10 octobre 1937</strong>), <strong>écrivain, poète et journaliste français</strong>. <strong>Maire de Villejuif</strong> de <strong>1929 à 1937</strong>. <strong>Député de la Seine</strong>.",
            "À proximité : l'<strong>hôpital Paul-Brousse</strong>, établissement de l'<strong>Assistance publique - Hôpitaux de Paris (AP-HP)</strong> fondé en <strong>1905</strong>. Spécialisé en <strong>greffes hépatiques</strong> et <strong>maladies du foie</strong>. L'<strong>Institut Gustave-Roussy</strong> à proximité est le <strong>plus grand centre de cancérologie</strong> européen."
        ],
        "faq": [
            ("Quelle ligne dessert Villejuif - Paul Vaillant-Couturier ?", "Uniquement la <strong>M7</strong>. Bus 131, 162, 185."),
            ("Qui est Paul Vaillant-Couturier ?", "<strong>Paul Vaillant-Couturier</strong> (1892-1937), <strong>écrivain, poète et journaliste</strong>. <strong>Maire de Villejuif</strong> (1929-1937)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>10 février 1982</strong>."),
            ("Pour l'hôpital Paul-Brousse ?", "<strong>~5 min à pied</strong>. AP-HP, fondé en 1905."),
            ("Pour l'Institut Gustave-Roussy ?", "<strong>~10 min à pied</strong>. Plus grand centre de cancérologie d'Europe."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Hôpital Paul-Brousse</strong> (AP-HP) à 5 min à pied.",
            "<strong>Institut Gustave-Roussy</strong> à 10 min : cancérologie de référence européenne.",
            "Pour <strong>Villejuif - Louis Aragon</strong> (terminus) : <strong>M7 directe</strong> (1 station).",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("📚", "Paul Vaillant-Couturier, journaliste et maire", "<strong>Paul Vaillant-Couturier</strong> (1892-1937), <strong>écrivain, poète et journaliste français</strong>. Études à <strong>Saint-Louis</strong>, puis à la <strong>Sorbonne</strong>. <strong>Maire de Villejuif</strong> de <strong>1929 à 1937</strong>. <strong>Député de la Seine</strong>. <strong>Journaliste à L'Humanité</strong>. Auteur de <em>La Guerre des soldats</em> (1919) et de plusieurs <strong>recueils de poésie</strong>. Mort à 45 ans en 1937."),
            ("🏥", "Institut Gustave-Roussy", "L'<strong>Institut Gustave-Roussy</strong>, à 10 min à pied, est le <strong>plus grand centre de cancérologie en Europe</strong>. Fondé en <strong>1926</strong> par <strong>Gustave Roussy</strong>. <strong>~500 lits</strong>, <strong>~3 500 employés</strong>, <strong>~700 chercheurs</strong>. <strong>~50 000 patients/an</strong>. <strong>Centre de référence international</strong> pour les <strong>traitements innovants</strong> et la <strong>recherche en oncologie</strong>.")
        ],
        "itin": [
            ("Hôpital Paul-Brousse", "villejuif-paul-vaillant-couturier", "à pied", "5 min à pied", 5),
            ("Institut Gustave-Roussy", "villejuif-louis-aragon", "M7 + à pied", "M7 → Louis Aragon + à pied", 10),
            ("Villejuif - Louis Aragon (terminus)", "villejuif-louis-aragon", "M7", "M7 directe (1 station)", 2),
            ("Villejuif - Léo Lagrange", "villejuif-leo-lagrange", "M7", "M7 directe (1 station)", 2),
            ("Place d'Italie", "place-d-italie", "M7", "M7 directe (6 stations)", 12),
            ("Châtelet", "chatelet", "M7", "M7 directe (~24 min)", 24)
        ]
    },
    "villejuif-louis-aragon": {
        "addr": "Avenue de Stalingrad, 94800 Villejuif", "arr": "Villejuif (94)",
        "seo": "Station Villejuif - Louis Aragon, terminus sud-ouest M7 à Villejuif (94). Hommage à Louis Aragon, poète et romancier. Tramway T7.",
        "tagline": "M7 — terminus, Louis Aragon poète et romancier",
        "hero_desc": "Station <strong>Villejuif - Louis Aragon</strong>, <strong>terminus sud-ouest de la M7</strong> (branche Villejuif), à <strong>Villejuif</strong> (Val-de-Marne, 94). Ouverte le <strong>28 février 1985</strong>. Hommage à <strong>Louis Aragon</strong> (<strong>1897-1982</strong>), <strong>poète, romancier et journaliste français</strong>. Correspondance <strong>tramway T7</strong>.",
        "intros": [
            "La station <strong>Villejuif - Louis Aragon</strong> est <strong>terminus sud-ouest de la M7</strong> (branche Villejuif), à <strong>Villejuif</strong> (Val-de-Marne, 94). Bus 131, 162, 185, 285, 480, tramway T7.",
            "Ouverte le <strong>28 février 1985</strong> avec le <strong>prolongement de la M7</strong> de Villejuif - Paul Vaillant-Couturier.",
            "Le nom <strong>Louis Aragon</strong> rend hommage à <strong>Louis Aragon</strong> (<strong>1897-1982</strong>), <strong>poète, romancier et journaliste français</strong>. <strong>Cofondateur du surréalisme</strong> avec André Breton (1924). Auteur de <em>Les Cloches de Bâle</em> (1934), <em>Aurélien</em> (1944), <em>Les Yeux d'Elsa</em> (1942). Correspondance <strong>tramway T7</strong> vers Athis-Mons et Juvisy-sur-Orge."
        ],
        "hist_title": "1985 : terminus et Louis Aragon poète",
        "hist": [
            "La station Villejuif - Louis Aragon est <strong>inaugurée le 28 février 1985</strong> comme <strong>terminus sud-ouest de la M7</strong>.",
            "Le nom <strong>Louis Aragon</strong> rend hommage à <strong>Louis Aragon</strong> (<strong>3 octobre 1897 - 24 décembre 1982</strong>), <strong>poète, romancier et journaliste français</strong>. <strong>Cofondateur du surréalisme</strong> avec <strong>André Breton</strong> et <strong>Philippe Soupault</strong> en <strong>1924</strong>.",
            "Œuvres majeures : <em><strong>Les Cloches de Bâle</strong></em> (1934), <em><strong>Aurélien</strong></em> (1944), <em><strong>Les Yeux d'Elsa</strong></em> (1942), <em><strong>La Diane française</strong></em> (1945), <em><strong>Le Roman inachevé</strong></em> (1956). <strong>Compagnon d'Elsa Triolet</strong> de 1928 à 1970. <strong>Prix lénine de la paix</strong> en 1957. Le <strong>tramway T7</strong> en correspondance directe (inauguré en 2013) relie <strong>Villejuif - Louis Aragon</strong> à <strong>Athis-Mons - Porte de l'Essonne</strong> et à <strong>Juvisy</strong>."
        ],
        "faq": [
            ("Quelles lignes desservent Villejuif - Louis Aragon ?", "<strong>M7</strong> (terminus branche Villejuif) + <strong>tramway T7</strong>. Bus 131, 162, 185, 285, 480."),
            ("Qui est Louis Aragon ?", "<strong>Louis Aragon</strong> (1897-1982), <strong>poète et romancier français</strong>. <strong>Cofondateur du surréalisme</strong>. Auteur des <em>Yeux d'Elsa</em> et d'<em>Aurélien</em>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>28 février 1985</strong>."),
            ("Pour Châtelet ?", "<strong>M7 directe</strong> (~25 min)."),
            ("Pour le tramway T7 ?", "<strong>Correspondance directe</strong>. Vers Athis-Mons et Juvisy."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Tramway T7</strong> en correspondance vers Athis-Mons et Juvisy.",
            "<strong>Institut Gustave-Roussy</strong> à 7 min à pied : cancérologie européenne.",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong> (~25 min).",
            "Pour <strong>Opéra</strong> : <strong>M7 directe</strong> (~27 min).",
            "Zone tarifaire <strong>3</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("📚", "Louis Aragon, cofondateur du surréalisme", "<strong>Louis Aragon</strong> (1897-1982), <strong>poète, romancier et journaliste français</strong>. <strong>Cofondateur du surréalisme</strong> avec <strong>André Breton</strong> et <strong>Philippe Soupault</strong> en <strong>1924</strong>. Œuvres majeures : <em><strong>Les Cloches de Bâle</strong></em> (1934, premier roman du « Monde réel »), <em><strong>Aurélien</strong></em> (1944), <em><strong>Les Yeux d'Elsa</strong></em> (1942), <em><strong>La Diane française</strong></em> (1945). <strong>Compagnon d'Elsa Triolet</strong> de <strong>1928 à 1970</strong>, qui inspira de nombreux poèmes. <strong>Prix lénine de la paix</strong> en 1957."),
            ("🚊", "Tramway T7 (2013)", "Le <strong>tramway T7</strong>, en correspondance directe, est <strong>inauguré le 16 novembre 2013</strong>. Relie <strong>Villejuif - Louis Aragon</strong> à <strong>Athis-Mons - Porte de l'Essonne</strong> et au <strong>RER C de Juvisy-sur-Orge</strong>. <strong>11,2 km</strong>, <strong>~50 000 voyageurs/jour</strong>. Dessert <strong>Chevilly-Larue, Rungis, Orly</strong>.")
        ],
        "itin": [
            ("Tramway T7", "villejuif-louis-aragon", "T7", "Correspondance directe", 1),
            ("Institut Gustave-Roussy", "villejuif-louis-aragon", "à pied", "7 min à pied", 7),
            ("Villejuif - Paul Vaillant-Couturier", "villejuif-paul-vaillant-couturier", "M7", "M7 directe (1 station)", 2),
            ("Place d'Italie", "place-d-italie", "M7", "M7 directe (7 stations)", 14),
            ("Châtelet", "chatelet", "M7", "M7 directe (~25 min)", 25),
            ("Opéra", "opera", "M7", "M7 directe (~27 min)", 27)
        ]
    },
    "pierre-et-marie-curie": {
        "addr": "Avenue Maurice-Thorez, 94200 Ivry-sur-Seine", "arr": "Ivry-sur-Seine (94)",
        "seo": "Station Pierre et Marie Curie (M7) à Ivry-sur-Seine (94). Hommage à Pierre Curie (1859-1906) et Marie Curie (1867-1934), découvreurs de la radioactivité.",
        "tagline": "M7 — Pierre et Marie Curie, radioactivité",
        "hero_desc": "Station <strong>Pierre et Marie Curie</strong> à <strong>Ivry-sur-Seine</strong> (Val-de-Marne, 94). Desservie par la <strong>M7</strong> (branche Mairie d'Ivry), ouverte le <strong>1er mai 1946</strong>. Hommage à <strong>Pierre Curie</strong> (<strong>1859-1906</strong>) et <strong>Marie Curie</strong> (<strong>1867-1934</strong>), <strong>découvreurs de la radioactivité</strong>.",
        "intros": [
            "La station <strong>Pierre et Marie Curie</strong> est implantée à <strong>Ivry-sur-Seine</strong> (Val-de-Marne, 94). Elle est desservie par la <strong>M7</strong> (branche Mairie d'Ivry), entre <strong>Porte d'Ivry</strong> (1 station) et <strong>Mairie d'Ivry</strong> (1 station, terminus). Bus 125, 132, 323.",
            "Ouverte le <strong>1er mai 1946</strong> avec le <strong>prolongement de la M7</strong> de Porte d'Ivry à Mairie d'Ivry. Initialement nommée <strong>« Maurice Thorez »</strong>. <strong>Renommée Pierre et Marie Curie</strong> en <strong>1981</strong>.",
            "Le nom <strong>Pierre et Marie Curie</strong> rend hommage à <strong>Pierre Curie</strong> (<strong>1859-1906</strong>) et <strong>Marie Curie</strong> (<strong>1867-1934</strong>), <strong>découvreurs de la radioactivité</strong>. <strong>Prix Nobel de physique 1903</strong> (avec Henri Becquerel). Marie obtient un <strong>second Nobel</strong> en <strong>chimie en 1911</strong>."
        ],
        "hist_title": "1946-1981 : Maurice Thorez renommée Pierre et Marie Curie",
        "hist": [
            "La station est <strong>inaugurée le 1er mai 1946</strong> sous le nom <strong>« Maurice Thorez »</strong> avec le <strong>prolongement de la M7</strong> de Porte d'Ivry à Mairie d'Ivry. <strong>Renommée Pierre et Marie Curie</strong> en <strong>1981</strong>.",
            "Le nom <strong>Pierre et Marie Curie</strong> rend hommage au couple de scientifiques. <strong>Pierre Curie</strong> (<strong>15 mai 1859 - 19 avril 1906</strong>), <strong>physicien français</strong>. <strong>Marie Curie</strong> (<strong>7 novembre 1867 - 4 juillet 1934</strong>), née <strong>Maria Skłodowska</strong>, <strong>physicienne et chimiste polonaise</strong> naturalisée française.",
            "Le couple <strong>découvre la radioactivité</strong> et identifie le <strong>polonium</strong> (1898) puis le <strong>radium</strong> (1898). <strong>Prix Nobel de physique 1903</strong> partagé avec <strong>Henri Becquerel</strong>. <strong>Marie obtient un second Nobel en chimie en 1911</strong>, ce qui en fait la <strong>première personne à recevoir deux Nobel</strong> dans deux disciplines scientifiques différentes. <strong>Pierre meurt en 1906</strong> dans un accident. <strong>Marie inhumée au Panthéon en 1995</strong> avec Pierre."
        ],
        "faq": [
            ("Quelle ligne dessert Pierre et Marie Curie ?", "Uniquement la <strong>M7</strong> (branche Mairie d'Ivry). Bus 125, 132, 323."),
            ("Qui sont Pierre et Marie Curie ?", "<strong>Pierre Curie</strong> (1859-1906) et <strong>Marie Curie</strong> (1867-1934), <strong>découvreurs de la radioactivité</strong>. <strong>Prix Nobel physique 1903</strong>. <strong>Marie : Prix Nobel chimie 1911</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>1er mai 1946</strong>, renommée en <strong>1981</strong>."),
            ("Quel était l'ancien nom ?", "<strong>« Maurice Thorez »</strong> (1946-1981)."),
            ("Combien de Prix Nobel pour Marie Curie ?", "<strong>Deux</strong> : <strong>physique 1903</strong> (avec Pierre et Becquerel) et <strong>chimie 1911</strong> (seule). <strong>Première personne à recevoir 2 Nobel</strong> dans 2 disciplines différentes."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "Hommage à <strong>Pierre et Marie Curie</strong> : <strong>radioactivité, polonium, radium</strong>.",
            "<strong>Marie Curie</strong> est la <strong>première personne</strong> à recevoir <strong>deux Nobel</strong> dans deux disciplines différentes.",
            "Pour <strong>Mairie d'Ivry</strong> (terminus) : <strong>M7 directe</strong> (1 station).",
            "Pour <strong>Châtelet</strong> : <strong>M7 directe</strong>.",
            "Zone tarifaire <strong>2</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("⚛️", "Découverte de la radioactivité (1898)", "<strong>Pierre</strong> et <strong>Marie Curie</strong> découvrent la <strong>radioactivité</strong> en collaboration avec <strong>Henri Becquerel</strong>. Marie identifie le <strong>polonium</strong> (juillet 1898, nommé d'après sa <strong>Pologne natale</strong>) puis le <strong>radium</strong> (décembre 1898). Ces travaux révolutionnent la <strong>physique nucléaire</strong> et la <strong>médecine</strong> (radiothérapie). <strong>Prix Nobel de physique 1903</strong> partagé entre Pierre, Marie et Henri Becquerel."),
            ("🏛️", "Marie Curie au Panthéon (1995)", "<strong>Marie Curie</strong> (1867-1934), née <strong>Maria Skłodowska</strong>, est la <strong>première personne</strong> à recevoir <strong>deux Prix Nobel</strong> dans <strong>deux disciplines scientifiques différentes</strong> : <strong>physique 1903</strong> et <strong>chimie 1911</strong>. <strong>Pierre meurt en 1906</strong> renversé par un chariot rue Dauphine. <strong>Marie inhumée au Panthéon</strong> le <strong>20 avril 1995</strong> avec Pierre, sous la <strong>présidence de François Mitterrand</strong>. <strong>Première femme inhumée au Panthéon</strong> pour ses propres mérites.")
        ],
        "itin": [
            ("Mairie d'Ivry (terminus)", "mairie-d-ivry", "M7", "M7 directe (1 station)", 2),
            ("Porte d'Ivry", "porte-d-ivry", "M7", "M7 directe (1 station)", 2),
            ("Ivry-sur-Seine centre", "mairie-d-ivry", "M7", "M7 directe (1 station)", 5),
            ("Châtelet", "chatelet", "M7", "M7 directe (~18 min)", 18),
            ("Place d'Italie", "place-d-italie", "M7", "M7 directe (5 stations)", 10),
            ("Opéra", "opera", "M7", "M7 directe (~20 min)", 20)
        ]
    },
    "mairie-d-ivry": {
        "addr": "Boulevard Paul-Vaillant-Couturier, 94200 Ivry-sur-Seine", "arr": "Ivry-sur-Seine (94)",
        "seo": "Station Mairie d'Ivry, terminus sud-est M7 à Ivry-sur-Seine (94). Hôtel de ville d'Ivry-sur-Seine. Quartier historique.",
        "tagline": "M7 — terminus sud-est, Ivry-sur-Seine",
        "hero_desc": "Station <strong>Mairie d'Ivry</strong>, <strong>terminus sud-est de la M7</strong> (branche Mairie d'Ivry), à <strong>Ivry-sur-Seine</strong> (Val-de-Marne, 94). Ouverte le <strong>1er mai 1946</strong>. À la sortie : l'<strong>hôtel de ville d'Ivry-sur-Seine</strong>.",
        "intros": [
            "La station <strong>Mairie d'Ivry</strong> est le <strong>terminus sud-est de la M7</strong> (branche Mairie d'Ivry), à <strong>Ivry-sur-Seine</strong> (Val-de-Marne, 94). Bus 125, 132, 180, 323, T9 tramway.",
            "Ouverte le <strong>1er mai 1946</strong> avec le <strong>prolongement de la M7</strong> de Porte d'Ivry à Mairie d'Ivry.",
            "À la sortie : l'<strong>hôtel de ville d'Ivry-sur-Seine</strong>, en plein centre de la commune. <strong>Ivry-sur-Seine</strong> (~62 000 habitants), commune dynamique du <strong>Val-de-Marne</strong>. <strong>Correspondance tramway T9</strong>."
        ],
        "hist_title": "1946 : terminus sud-est Ivry-sur-Seine",
        "hist": [
            "La station Mairie d'Ivry est <strong>inaugurée le 1er mai 1946</strong> comme <strong>terminus sud-est de la M7</strong> (branche Mairie d'Ivry), avec le <strong>prolongement de la M7</strong> de Porte d'Ivry à Mairie d'Ivry.",
            "<strong>Ivry-sur-Seine</strong> (~62 000 habitants), commune dynamique du <strong>Val-de-Marne</strong>. <strong>Ancienne commune industrielle</strong> aux XIXe-XXe siècles (Citroën, manufactures), elle s'est transformée depuis les années 1990 en <strong>commune résidentielle et de bureaux</strong>.",
            "Le <strong>tramway T9</strong>, en correspondance, est <strong>inauguré le 10 avril 2021</strong>. Relie <strong>Porte de Choisy</strong> (Paris) à <strong>Orly</strong>. <strong>10 km</strong>, <strong>~70 000 voyageurs/jour</strong>. Dessert <strong>Ivry-sur-Seine, Vitry-sur-Seine, Choisy-le-Roi, Orly</strong>."
        ],
        "faq": [
            ("Quelles lignes desservent Mairie d'Ivry ?", "<strong>M7</strong> (terminus branche Mairie d'Ivry) + <strong>tramway T9</strong>. Bus 125, 132, 180, 323."),
            ("Quand a-t-elle ouvert ?", "Le <strong>1er mai 1946</strong>."),
            ("Pour Ivry-sur-Seine centre ?", "<strong>Sortie directe</strong>."),
            ("Pour Paris centre ?", "<strong>M7 directe</strong> vers Châtelet (~16 min)."),
            ("Pour Orly ?", "<strong>Tramway T9</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Hôtel de ville d'Ivry-sur-Seine</strong> à la sortie.",
            "<strong>Tramway T9</strong> en correspondance : vers Orly.",
            "Pour <strong>Paris centre</strong> : <strong>M7 directe</strong>.",
            "Pour <strong>Place d'Italie</strong> : <strong>M7 directe</strong> (5 stations).",
            "Zone tarifaire <strong>2</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("🏛️", "Ivry-sur-Seine, ancienne ville industrielle", "<strong>Ivry-sur-Seine</strong>, ~62 000 habitants, commune dynamique du <strong>Val-de-Marne</strong>. <strong>Ancienne commune industrielle</strong> aux XIXe-XXe siècles. Accueillait des <strong>usines Citroën</strong>, des <strong>manufactures</strong>. Se transforme depuis les années 1990 en <strong>commune résidentielle et de bureaux</strong>. <strong>Quartier Ivry Confluences</strong> en pleine transformation."),
            ("🚊", "Tramway T9 (2021)", "Le <strong>tramway T9</strong>, en correspondance, est <strong>inauguré le 10 avril 2021</strong>. Relie <strong>Porte de Choisy</strong> (Paris) à <strong>Orly</strong>. <strong>10 km</strong>, <strong>19 stations</strong>, <strong>~70 000 voyageurs/jour</strong>. Dessert <strong>Ivry-sur-Seine, Vitry-sur-Seine, Choisy-le-Roi, Orly</strong>. <strong>Premier tramway de la Métropole du Grand Paris</strong> au sud-est.")
        ],
        "itin": [
            ("Hôtel de ville Ivry-sur-Seine", "mairie-d-ivry", "à pied", "Sortie directe", 1),
            ("Tramway T9 (vers Orly)", "mairie-d-ivry", "T9", "Correspondance directe", 1),
            ("Pierre et Marie Curie", "pierre-et-marie-curie", "M7", "M7 directe (1 station)", 2),
            ("Place d'Italie", "place-d-italie", "M7", "M7 directe (5 stations)", 10),
            ("Châtelet", "chatelet", "M7", "M7 directe (~16 min)", 16),
            ("Opéra", "opera", "M7", "M7 directe (~18 min)", 18)
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
    elif "(94)" in c["arr"]:
        zone = 3 if "Villejuif" in c["arr"] else 2
        d["tariff_zone"] = zone
        d["tariff_zone_context"] = f"Val-de-Marne (94), zone tarifaire {zone}"
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
