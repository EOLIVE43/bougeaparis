#!/usr/bin/env python3
"""Enrichit M11 12 stations avec contenu T0 Wikipedia FR (condensé)."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    "goncourt": {
        "addr": "Bd Jules-Ferry / rue de Lancry, 75011 Paris", "arr": "11e (Paris)",
        "seo": "Station Goncourt : M11 dans le 11e arr., quartier République, rue de Lancry. Petite station historique 1935 de la ligne 11.",
        "tagline": "M11 — quartier République et canal Saint-Martin",
        "hero_desc": "Station <strong>Goncourt</strong> ouverte le <strong>28 avril 1935</strong> avec la M11 originelle. Située dans le <strong>11e arrondissement</strong>, à proximité du <strong>canal Saint-Martin</strong> et de la <strong>rue de Lancry</strong>. Nom des <strong>frères Goncourt</strong>, écrivains français du XIXe siècle, fondateurs de l'<strong>Académie Goncourt</strong> (prix littéraire prestigieux).",
        "intros": [
            "La station <strong>Goncourt</strong> est située dans le <strong>11e arrondissement de Paris</strong>, sur le <strong>boulevard Jules-Ferry</strong> à proximité de la <strong>rue de Lancry</strong>. Elle est desservie uniquement par la <strong>M11</strong> (Châtelet ↔ Rosny - Bois-Perrier), entre <strong>République</strong> (1 station vers le sud-ouest) et <strong>Belleville</strong> (1 station vers le nord-est). Bus 46, 75.",
            "Ouverte le <strong>28 avril 1935</strong> avec la M11 originelle (Châtelet ↔ Porte des Lilas).",
            "Le nom <strong>Goncourt</strong> commémore les <strong>frères Edmond (1822-1896) et Jules (1830-1870) Goncourt</strong>, écrivains et critiques d'art français du XIXe siècle. Fondateurs de l'<strong>Académie Goncourt</strong> et créateurs du <strong>prix Goncourt</strong> (1903), prix littéraire le plus prestigieux de France."
        ],
        "hist_title": "1935 : M11, et les frères Goncourt",
        "hist": [
            "La station <strong>Goncourt</strong> est inaugurée le <strong>28 avril 1935</strong> avec la <strong>M11 originelle</strong> (Châtelet ↔ Porte des Lilas, 9 stations).",
            "Le nom commémore les <strong>frères Goncourt</strong> : <strong>Edmond (1822-1896)</strong> et <strong>Jules (1830-1870)</strong>, écrivains naturalistes et critiques d'art français. <strong>Co-écrivains</strong> jusqu'à la mort de Jules. Pionniers du <strong>naturalisme français</strong> avec Zola.",
            "L'<strong>Académie Goncourt</strong> est fondée en <strong>1900</strong> par le legs d'Edmond. <strong>Prix Goncourt</strong> décerné depuis <strong>1903</strong> — prix littéraire <strong>le plus prestigieux de France</strong>. Lauréats célèbres : Marcel Proust (1919), André Malraux (1933), Simone de Beauvoir (1954), Marguerite Duras (1984), Michel Houellebecq (2010, refusé), Patrick Modiano, etc.",
            "Le quartier autour est résidentiel, à proximité du <strong>canal Saint-Martin</strong> (5 min) — lieu emblématique du Paris bohème depuis les années 2000 (cafés, péniches, restaurants)."
        ],
        "faq": [
            ("Quelle ligne dessert Goncourt ?", "Uniquement la <strong>M11</strong>. Bus 46, 75."),
            ("Qui sont les frères Goncourt ?", "<strong>Edmond (1822-1896) et Jules (1830-1870) Goncourt</strong>, écrivains français pionniers du naturalisme. Fondateurs de l'<strong>Académie Goncourt</strong> et créateurs du <strong>prix Goncourt</strong> (1903), prix littéraire le plus prestigieux de France."),
            ("Qu'est-ce que le prix Goncourt ?", "<strong>Prix littéraire français le plus prestigieux</strong>, décerné chaque année depuis <strong>1903</strong> par l'Académie Goncourt. Récompense le meilleur roman de l'année."),
            ("Comment aller au canal Saint-Martin ?", "<strong>5 min à pied</strong> direction sud-ouest."),
            ("Comment aller à Châtelet ?", "<strong>M11 directe</strong> : ~10 min (5 stations vers le sud-ouest)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station historique 1935.")
        ],
        "tips": [
            "<strong>Canal Saint-Martin</strong> à 5 min — péniches, cafés, atmosphère bohème.",
            "Pour <strong>République</strong> : M11 directe (1 station).",
            "Pour <strong>Châtelet</strong> : M11 directe (~10 min).",
            "Pour <strong>Belleville</strong> : M11 directe (1 station).",
            "Quartier résidentiel populaire du 11e."
        ],
        "trivia": [
            ("📚", "Frères Goncourt — pionniers du naturalisme français", "Les <strong>frères Edmond (1822-1896) et Jules (1830-1870) Goncourt</strong> étaient <strong>écrivains français du XIXe siècle</strong>, pionniers du <strong>naturalisme français</strong> avec Zola. <strong>Co-écrivains</strong> jusqu'à la mort de Jules en 1870 — Edmond continue seul. Tinrent un célèbre <strong>Journal</strong> de la vie littéraire et artistique parisienne (1851-1896). Œuvres : <em>Germinie Lacerteux</em> (1865), <em>Renée Mauperin</em> (1864). Promoteurs du <strong>réalisme social</strong>."),
            ("🏆", "Prix Goncourt — le plus prestigieux de France (1903)", "Le <strong>Prix Goncourt</strong> est décerné chaque année <strong>depuis 1903</strong> par l'<strong>Académie Goncourt</strong> (fondée 1900 par legs d'Edmond). <strong>Prix littéraire le plus prestigieux de France</strong>. Récompense le meilleur roman de l'année. <strong>Lauréats célèbres</strong> : Marcel Proust (1919), André Malraux (1933), Simone de Beauvoir (1954), Marguerite Duras (1984), Michel Houellebecq (2010, refusé), Patrick Modiano, Patrick Rambaud, Annie Ernaux, etc.")
        ],
        "itin": [
            ("République via M11", "republique", "M11", "M11 direction Châtelet (1 station)", 2),
            ("Belleville via M11", "belleville", "M11", "M11 direction Rosny (1 station)", 2),
            ("Châtelet via M11", "chatelet", "M11", "M11 direction Châtelet (5 stations)", 10),
            ("Canal Saint-Martin", "canal-saint-martin", "à pied", "5 min sud-ouest", 5),
            ("Place de la République", "republique", "à pied", "5 min", 5),
            ("Place des Fêtes via M11", "place-des-fetes", "M11", "M11 direction Rosny (3 stations)", 7)
        ]
    },
    "belleville": {
        "addr": "Bd de Belleville / rue de Belleville, 75011/75019/75020 Paris", "arr": "11e/19e/20e (Paris)",
        "seo": "Station Belleville : M2 + M11 à la jonction 11e/19e/20e arr. Quartier multi-ethnique emblématique, Chinatown nord, Parc de Belleville (vue panoramique sur Paris).",
        "tagline": "M2 + M11 — quartier multi-ethnique de Belleville",
        "hero_desc": "Station <strong>Belleville</strong> à la <strong>jonction des 11e, 19e et 20e arrondissements</strong>. Desservie par <strong>M2</strong> (ouverte 31 janvier 1903) et <strong>M11</strong> (ouverte 28 avril 1935). Cœur du <strong>quartier multi-ethnique de Belleville</strong>, l'un des plus diversifiés de Paris. Présence du <strong>Chinatown nord</strong> et du <strong>Parc de Belleville</strong> (vue panoramique sur Paris depuis 108 m).",
        "intros": [
            "La station <strong>Belleville</strong> est située à la <strong>jonction des 11e, 19e et 20e arrondissements</strong>, sur le <strong>boulevard de Belleville</strong>. Elle est desservie par <strong>2 lignes</strong> : <strong>M2</strong> (Porte Dauphine ↔ Nation) et <strong>M11</strong> (Châtelet ↔ Rosny - Bois-Perrier). Bus 26, 75.",
            "La station <strong>M2</strong> ouvre le <strong>31 janvier 1903</strong> avec le tronçon Villiers ↔ Bagnolet. La station <strong>M11</strong> est ajoutée le <strong>28 avril 1935</strong>.",
            "Belleville est l'un des <strong>quartiers les plus multi-ethniques de Paris</strong>. <strong>Ancien village vigneron</strong> annexé en 1860. À partir du XXe siècle : vagues d'immigration <strong>juive ashkénaze</strong>, <strong>arménienne</strong>, <strong>maghrébine</strong>, puis <strong>asiatique</strong> (Chinatown nord depuis 1980s — chinois, vietnamiens, cambodgiens, laotiens). À <strong>5 min</strong> : le <strong>Parc de Belleville</strong> (4,5 ha, 108 m d'altitude), <strong>vue panoramique sur Paris</strong>."
        ],
        "hist_title": "1903 : M2, 1935 : M11, et Belleville multi-ethnique",
        "hist": [
            "La station <strong>M2</strong> ouvre le <strong>31 janvier 1903</strong>. La station <strong>M11</strong> est ajoutée le <strong>28 avril 1935</strong>.",
            "<strong>Belleville</strong> était un <strong>village indépendant vigneron</strong> jusqu'au XIXe siècle, <strong>annexé à Paris en 1860</strong> par Napoléon III. Au XIXe : quartier <strong>ouvrier populaire</strong>, refuge des Communards en 1871 (le mur des Fédérés est dans le Père-Lachaise voisin).",
            "Au XXe siècle, Belleville accueille successivement plusieurs vagues d'immigration :\n- <strong>Juifs ashkénazes</strong> (avant 1939, Pologne, Russie)\n- <strong>Arméniens</strong> (rescapés du génocide 1915)\n- <strong>Maghrébins</strong> (1950s-60s, Algérie, Tunisie, Maroc)\n- <strong>Asiatiques</strong> (1980s+, réfugiés du Sud-Est asiatique : Chine du Sud, Vietnam, Cambodge, Laos)",
            "Aujourd'hui, le <strong>Chinatown nord de Paris</strong> (avenue de Belleville) abrite la deuxième concentration asiatique de Paris (après le 13e arr.). Restaurants asiatiques, supermarchés, salons de coiffure.",
            "À 5 min à pied : le <strong>Parc de Belleville</strong> (4,5 ha, créé en 1988 par Paul Brichet), <strong>108 m d'altitude</strong>, <strong>vue panoramique exceptionnelle sur Paris</strong> (Tour Eiffel, Sacré-Cœur visibles). <strong>Pavillon du Bouddha</strong> au sommet."
        ],
        "faq": [
            ("Quelles lignes desservent Belleville ?", "<strong>M2</strong> (1903) et <strong>M11</strong> (1935). Bus 26, 75."),
            ("Qu'est-ce que Belleville ?", "Quartier multi-ethnique de Paris à la jonction des 11e, 19e et 20e arrondissements. Ancien village vigneron, annexé en 1860. Vagues d'immigration juive, arménienne, maghrébine, asiatique. <strong>Chinatown nord</strong> de Paris."),
            ("Où est le Parc de Belleville ?", "<strong>5 min à pied</strong> direction nord. <strong>4,5 ha</strong>, <strong>108 m d'altitude</strong> — <strong>vue panoramique exceptionnelle sur Paris</strong>."),
            ("Comment aller à Châtelet ?", "<strong>M11 directe</strong> : ~14 min (7 stations) OU <strong>M2 vers République + M11</strong>."),
            ("Comment aller au Père-Lachaise ?", "<strong>M2 directe</strong> : ~6 min (2 stations vers Nation)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Stations historiques 1903/1935.")
        ],
        "tips": [
            "<strong>Parc de Belleville</strong> à 5 min — vue panoramique sur Paris.",
            "<strong>Chinatown nord</strong> avenue de Belleville — restaurants asiatiques.",
            "<strong>Marché de Belleville</strong> (mardi/vendredi) — l'un des plus authentiques de Paris.",
            "Pour <strong>Père-Lachaise</strong> : M2 directe (~6 min).",
            "Pour <strong>République</strong> : M11 directe (~5 min)."
        ],
        "trivia": [
            ("🍷", "Ancien village vigneron annexé en 1860", "<strong>Belleville</strong> était un <strong>village indépendant vigneron</strong> jusqu'au XIXe siècle, situé sur une colline au nord-est de Paris. <strong>Vignes</strong> et <strong>guinguettes</strong> attiraient les Parisiens. <strong>Annexé à Paris en 1860</strong> par Napoléon III (avec Charonne, Grenelle, etc.). Au XIXe : devient quartier <strong>ouvrier populaire</strong>, refuge des Communards en 1871. Aujourd'hui : l'un des quartiers les plus multi-ethniques de Paris (juif, arménien, maghrébin, asiatique)."),
            ("🌏", "Chinatown nord — 2e concentration asiatique de Paris", "Le <strong>Chinatown nord de Paris</strong> (avenue de Belleville) est la <strong>2e concentration asiatique de Paris</strong> après le 13e arr. (Olympiades). Présence depuis les <strong>années 1980</strong> avec les réfugiés du Sud-Est asiatique : <strong>Chinois du Sud</strong>, <strong>Vietnamiens</strong>, <strong>Cambodgiens</strong>, <strong>Laotiens</strong>. <strong>Restaurants asiatiques</strong>, <strong>supermarchés</strong>, <strong>salons de coiffure</strong>, <strong>boulangeries asiatiques</strong>. Plus authentique et populaire que le Chinatown sud (qui est plus touristique).")
        ],
        "itin": [
            ("Parc de Belleville", "parc-belleville", "à pied", "5 min direct", 5),
            ("Père-Lachaise via M2", "pere-lachaise", "M2", "M2 direction Nation (2 stations)", 6),
            ("République via M11", "republique", "M11", "M11 direction Châtelet (2 stations)", 5),
            ("Châtelet via M11", "chatelet", "M11", "M11 direction Châtelet (7 stations)", 14),
            ("Chinatown nord (av. Belleville)", "chinatown-nord", "à pied", "Sortie directe", 2),
            ("Place des Fêtes via M11", "place-des-fetes", "M11", "M11 direction Rosny (2 stations)", 5)
        ]
    },
    "pyrenees": {
        "addr": "Rue des Pyrénées / rue de Belleville, 75019/75020 Paris", "arr": "19e/20e (Paris)",
        "seo": "Station Pyrénées : M11 à la jonction 19e/20e arr., rue des Pyrénées et rue de Belleville. Hôpital Tenon à proximité.",
        "tagline": "M11 — rue des Pyrénées",
        "hero_desc": "Station <strong>Pyrénées</strong> ouverte le <strong>28 avril 1935</strong> avec la M11 originelle. Située à la <strong>jonction des 19e et 20e arrondissements</strong>, à l'intersection de la <strong>rue des Pyrénées</strong> et de la <strong>rue de Belleville</strong>. Nom du massif <strong>des Pyrénées</strong> (frontière France-Espagne). Quartier résidentiel populaire.",
        "intros": [
            "La station <strong>Pyrénées</strong> est située à la <strong>jonction des 19e et 20e arrondissements de Paris</strong>, à l'intersection de la <strong>rue des Pyrénées</strong> et de la <strong>rue de Belleville</strong>. Elle est desservie uniquement par la <strong>M11</strong>, entre <strong>Belleville</strong> (1 station vers le sud-ouest) et <strong>Jourdain</strong> (1 station vers le nord-est). Bus 26.",
            "Ouverte le <strong>28 avril 1935</strong> avec la M11 originelle.",
            "Le nom <strong>Pyrénées</strong> vient de la <strong>rue des Pyrénées</strong>, l'une des plus longues du 20e arrondissement, baptisée d'après le <strong>massif des Pyrénées</strong> (chaîne montagneuse frontière France-Espagne, point culminant Aneto 3 404 m). À 10 min : l'<strong>hôpital Tenon</strong> (AP-HP)."
        ],
        "hist_title": "1935 : M11, et la rue des Pyrénées",
        "hist": [
            "La station <strong>Pyrénées</strong> ouvre le <strong>28 avril 1935</strong> avec la M11 originelle (Châtelet ↔ Porte des Lilas).",
            "Le nom vient de la <strong>rue des Pyrénées</strong>, l'une des plus longues du 20e arrondissement (~2 km), baptisée d'après le <strong>massif des Pyrénées</strong>. Tradition haussmannienne : nommer les rues d'après des éléments géographiques (massifs, fleuves, mers).",
            "Le <strong>massif des Pyrénées</strong> : chaîne montagneuse de ~500 km séparant la <strong>France de l'Espagne</strong>, avec l'<strong>Andorre</strong> au centre. <strong>Point culminant : pic d'Aneto</strong> (3 404 m, côté espagnol). <strong>Plus de 200 sommets de 3 000 m</strong>. Lieux célèbres : <strong>Pic du Midi</strong>, <strong>Pic d'Ossau</strong>, <strong>Cirque de Gavarnie</strong> (Patrimoine mondial UNESCO).",
            "Le quartier autour est <strong>résidentiel populaire</strong> du 20e. À 10 min : <strong>hôpital Tenon</strong> (Assistance Publique - Hôpitaux de Paris)."
        ],
        "faq": [
            ("Quelle ligne dessert Pyrénées ?", "Uniquement la <strong>M11</strong>. Bus 26."),
            ("Pourquoi le nom Pyrénées ?", "De la <strong>rue des Pyrénées</strong>, l'une des plus longues du 20e arr. (~2 km), baptisée d'après le <strong>massif des Pyrénées</strong> (chaîne montagneuse frontière France-Espagne, point culminant Aneto 3 404 m)."),
            ("Comment aller à Châtelet ?", "<strong>M11 directe</strong> : ~16 min (8 stations vers le sud-ouest)."),
            ("Comment aller à Belleville ?", "<strong>M11 directe</strong> : 1 station vers le sud-ouest (~2 min)."),
            ("Où est l'hôpital Tenon ?", "<strong>10 min à pied</strong> direction est."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station historique 1935.")
        ],
        "tips": [
            "Pour <strong>Belleville</strong> : M11 directe (1 station).",
            "Pour <strong>Châtelet</strong> : M11 directe (~16 min).",
            "Pour <strong>Jourdain</strong> : M11 directe (1 station).",
            "Pour <strong>Père-Lachaise</strong> via Belleville + M2.",
            "Quartier résidentiel populaire — commerces locaux."
        ],
        "trivia": [
            ("⛰️", "Massif des Pyrénées — frontière France/Espagne", "Le <strong>massif des Pyrénées</strong> est une chaîne montagneuse de <strong>~500 km</strong> séparant la <strong>France de l'Espagne</strong>, avec l'<strong>Andorre</strong> au centre. <strong>Point culminant : pic d'Aneto</strong> (3 404 m, côté espagnol). Plus de <strong>200 sommets de 3 000 m</strong>. Lieux célèbres : <strong>Pic du Midi de Bigorre</strong> (2 877 m, observatoire), <strong>Pic d'Ossau</strong> (2 884 m, emblématique pyramide), <strong>Cirque de Gavarnie</strong> (Patrimoine mondial UNESCO 1997). Tradition haussmannienne de nommer les rues parisiennes d'après les massifs : Pyrénées, Mont-Cenis (M12), Simplon (M4), etc.")
        ],
        "itin": [
            ("Belleville via M11", "belleville", "M11", "M11 direction Châtelet (1 station)", 2),
            ("Jourdain via M11", "jourdain", "M11", "M11 direction Rosny (1 station)", 2),
            ("Châtelet via M11", "chatelet", "M11", "M11 direction Châtelet (8 stations)", 16),
            ("Place des Fêtes via M11", "place-des-fetes", "M11", "M11 direction Rosny (2 stations)", 4),
            ("Hôpital Tenon", "hopital-tenon", "à pied", "10 min direct", 10),
            ("Père-Lachaise via M11 + M2", "pere-lachaise", "M11 + M2", "M11 jusqu'à Belleville + M2", 10)
        ]
    },
    "jourdain": {
        "addr": "Rue de Belleville haute, 75019 Paris", "arr": "19e (Paris)",
        "seo": "Station Jourdain : M11 dans le 19e arr., haut de la rue de Belleville. Église Saint-Jean-Baptiste de Belleville et quartier résidentiel.",
        "tagline": "M11 — rue de Belleville haute",
        "hero_desc": "Station <strong>Jourdain</strong> ouverte le <strong>28 avril 1935</strong> avec la M11 originelle. Située dans le <strong>19e arrondissement</strong>, sur la partie haute de la <strong>rue de Belleville</strong>. Nom du <strong>Maréchal Jean-Baptiste Jourdan</strong> (1762-1833), général de la Révolution et Empire. À côté : l'<strong>église Saint-Jean-Baptiste de Belleville</strong>.",
        "intros": [
            "La station <strong>Jourdain</strong> est située dans le <strong>19e arrondissement de Paris</strong>, sur la partie haute de la <strong>rue de Belleville</strong>. Elle est desservie uniquement par la <strong>M11</strong>, entre <strong>Pyrénées</strong> (1 station vers le sud-ouest) et <strong>Place des Fêtes</strong> (1 station vers le nord-est, M7bis correspondance). Bus 26, 60.",
            "Ouverte le <strong>28 avril 1935</strong> avec la M11 originelle.",
            "Le nom <strong>Jourdain</strong> commémore le <strong>maréchal Jean-Baptiste Jourdan</strong> (1762-1833), <strong>général de la Révolution française et de l'Empire</strong>. Vainqueur de la <strong>bataille de Fleurus</strong> (1794). <strong>Maréchal d'Empire</strong> sous Napoléon. À proximité : l'<strong>église Saint-Jean-Baptiste de Belleville</strong> (XIXe)."
        ],
        "hist_title": "1935 : M11, et le maréchal Jourdan",
        "hist": [
            "La station <strong>Jourdain</strong> ouvre le <strong>28 avril 1935</strong> avec la M11 originelle (Châtelet ↔ Porte des Lilas).",
            "Le nom commémore le <strong>maréchal Jean-Baptiste Jourdan</strong> (1762-1833), <strong>général de la Révolution française et de l'Empire</strong>.",
            "<strong>Carrière militaire</strong> : volontaire en 1791, général en 1793. <strong>Vainqueur de la bataille de Fleurus</strong> le 26 juin 1794 (Belgique) — victoire décisive de la Première République française. <strong>Maréchal d'Empire</strong> sous Napoléon en 1804 (l'un des 26 maréchaux nommés). Vainqueur en Espagne. <strong>Comte d'Empire</strong>, puis <strong>pair de France</strong> sous la Restauration.",
            "Le quartier autour est <strong>résidentiel populaire</strong> du 19e. À côté : l'<strong>église Saint-Jean-Baptiste de Belleville</strong> (XIXe), néo-gothique. Marché Jourdain animé."
        ],
        "faq": [
            ("Quelle ligne dessert Jourdain ?", "Uniquement la <strong>M11</strong>. Bus 26, 60."),
            ("Qui est Jourdan ?", "<strong>Jean-Baptiste Jourdan</strong> (1762-1833), <strong>général de la Révolution française et de l'Empire</strong>. Vainqueur de la <strong>bataille de Fleurus</strong> (1794). <strong>Maréchal d'Empire</strong> sous Napoléon (1804)."),
            ("Comment aller à Châtelet ?", "<strong>M11 directe</strong> : ~18 min (9 stations vers le sud-ouest)."),
            ("Comment aller à Place des Fêtes ?", "<strong>M11 directe</strong> : 1 station vers le nord-est (~2 min)."),
            ("Où est l'église Saint-Jean-Baptiste de Belleville ?", "À côté de la station, rue Lassus."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station historique 1935.")
        ],
        "tips": [
            "<strong>Église Saint-Jean-Baptiste de Belleville</strong> (XIXe néo-gothique) — à côté.",
            "<strong>Marché Jourdain</strong> — quartier animé.",
            "Pour <strong>Châtelet</strong> : M11 directe (~18 min).",
            "Pour <strong>Place des Fêtes</strong> (correspondance M7bis) : M11 directe (1 station).",
            "Quartier résidentiel populaire du 19e."
        ],
        "trivia": [
            ("⚔️", "Maréchal Jourdan — vainqueur de Fleurus (1794)", "Le nom <strong>Jourdain</strong> commémore le <strong>maréchal Jean-Baptiste Jourdan</strong> (1762-1833), <strong>général de la Révolution française et de l'Empire</strong>. <strong>Volontaire en 1791</strong>, <strong>général en 1793</strong>. <strong>Vainqueur de la bataille de Fleurus</strong> le 26 juin 1794 (Belgique) — <strong>victoire décisive de la Première République française</strong> contre les Autrichiens. Première fois où un ballon d'observation fut utilisé en bataille. <strong>Maréchal d'Empire</strong> sous Napoléon (l'un des 26 maréchaux nommés en 1804). Sa victoire sécurise les frontières nord de la France révolutionnaire.")
        ],
        "itin": [
            ("Place des Fêtes via M11", "place-des-fetes", "M11", "M11 direction Rosny (1 station)", 2),
            ("Pyrénées via M11", "pyrenees", "M11", "M11 direction Châtelet (1 station)", 2),
            ("Châtelet via M11", "chatelet", "M11", "M11 direction Châtelet (9 stations)", 18),
            ("Belleville via M11", "belleville", "M11", "M11 direction Châtelet (2 stations)", 4),
            ("Église Saint-Jean-Baptiste", "eglise-saint-jean-baptiste-belleville", "à pied", "Sortie directe", 1),
            ("Marché Jourdain", "marche-jourdain", "à pied", "Sortie directe", 1)
        ]
    },
    "telegraphe": {
        "addr": "Rue du Télégraphe, 75020 Paris", "arr": "20e (Paris)",
        "seo": "Station Télégraphe : M11 dans le 20e arr., rue du Télégraphe. Cimetière de Belleville et point le plus haut de Paris (128,21 m).",
        "tagline": "M11 — point le plus haut de Paris (128 m)",
        "hero_desc": "Station <strong>Télégraphe</strong> ouverte le <strong>28 avril 1935</strong> avec la M11 originelle. Située dans le <strong>20e arrondissement</strong>, sur la <strong>rue du Télégraphe</strong>. Nom du <strong>télégraphe Chappe</strong> installé sur la colline en 1793. À côté : le <strong>point le plus haut de Paris intra-muros</strong> (<strong>128,21 m</strong>) et le <strong>Cimetière de Belleville</strong>.",
        "intros": [
            "La station <strong>Télégraphe</strong> est située dans le <strong>20e arrondissement de Paris</strong>, sur la <strong>rue du Télégraphe</strong>. Elle est desservie uniquement par la <strong>M11</strong>, entre <strong>Place des Fêtes</strong> (1 station vers le sud-ouest) et <strong>Porte des Lilas</strong> (1 station vers le nord-est). Bus 64.",
            "Ouverte le <strong>28 avril 1935</strong> avec la M11 originelle.",
            "Le nom <strong>Télégraphe</strong> vient du <strong>télégraphe Chappe</strong> installé sur la <strong>colline de Belleville</strong> en <strong>1793</strong>. La <strong>rue du Télégraphe</strong> commémore ce premier dispositif. À côté : le <strong>point le plus haut de Paris intra-muros</strong> à <strong>128,21 m d'altitude</strong> (à côté du Cimetière de Belleville)."
        ],
        "hist_title": "1793 : télégraphe Chappe, 1935 : M11",
        "hist": [
            "La station <strong>Télégraphe</strong> ouvre le <strong>28 avril 1935</strong> avec la M11 originelle (Châtelet ↔ Porte des Lilas).",
            "Le nom vient du <strong>télégraphe Chappe</strong>, l'un des <strong>premiers systèmes de télécommunication à longue distance</strong>. <strong>Inventé par Claude Chappe</strong> (1763-1805) en 1793 — <strong>communication optique</strong> par signaux mécaniques visibles à grande distance grâce à des bras articulés sur des tours.",
            "<strong>Un poste du télégraphe Chappe a été installé sur la colline de Belleville en 1793</strong>, point culminant de l'est parisien. Il faisait partie de la <strong>ligne Paris-Lille</strong> (la première du réseau Chappe). <strong>Activité jusqu'au milieu du XIXe siècle</strong>, supplanté par le télégraphe électrique (1840s).",
            "À côté de la station : le <strong>point le plus haut de Paris intra-muros</strong>, à <strong>128,21 m d'altitude</strong> — exactement à l'angle de la rue du Télégraphe et de la rue Pixérécourt, dans le 20e arrondissement. Légèrement plus haut que la <strong>butte Montmartre</strong> (130 m mesurés à la sortie M12 Lamarck-Caulaincourt mais l'altitude varie selon le point).",
            "Adjacent : le <strong>Cimetière de Belleville</strong> (1808, ~3 ha)."
        ],
        "faq": [
            ("Quelle ligne dessert Télégraphe ?", "Uniquement la <strong>M11</strong>. Bus 64."),
            ("Qu'est-ce que le télégraphe Chappe ?", "<strong>Premier système de télécommunication à longue distance</strong>, inventé par <strong>Claude Chappe</strong> (1763-1805) en 1793. <strong>Communication optique</strong> par signaux mécaniques (bras articulés sur tours). <strong>Un poste installé sur la colline de Belleville en 1793</strong>, premier réseau Paris-Lille."),
            ("C'est le point le plus haut de Paris ?", "<strong>Oui, point culminant de Paris intra-muros à 128,21 m</strong>, à l'angle de la rue du Télégraphe et de la rue Pixérécourt. Légèrement plus haut que la butte Montmartre."),
            ("Comment aller à Châtelet ?", "<strong>M11 directe</strong> : ~20 min (10 stations)."),
            ("Comment aller à Place des Fêtes ?", "<strong>M11 directe</strong> : 1 station (~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station historique 1935.")
        ],
        "tips": [
            "<strong>Point le plus haut de Paris</strong> à 1 min — 128,21 m.",
            "<strong>Cimetière de Belleville</strong> adjacent — 1808.",
            "Pour <strong>Place des Fêtes</strong> : M11 directe (1 station).",
            "Pour <strong>Porte des Lilas</strong> : M11 directe (1 station).",
            "Pour <strong>Châtelet</strong> : M11 directe (~20 min)."
        ],
        "trivia": [
            ("📡", "Télégraphe Chappe — première télécommunication longue distance (1793)", "Le nom <strong>Télégraphe</strong> vient du <strong>télégraphe Chappe</strong>, <strong>premier système de télécommunication à longue distance</strong> de l'histoire. <strong>Inventé par Claude Chappe</strong> (1763-1805) en <strong>1793</strong> — communication optique par <strong>signaux mécaniques</strong> (bras articulés sur tours). <strong>Un poste installé sur la colline de Belleville en 1793</strong>, premier réseau <strong>Paris-Lille</strong>. <strong>196 postes</strong> à son apogée. Permettait transmettre un message Paris ↔ Lille en <strong>2 minutes</strong> (vs plusieurs jours par messager). Activité jusqu'au milieu du XIXe, supplanté par le télégraphe électrique."),
            ("⛰️", "Point le plus haut de Paris intra-muros — 128,21 m", "À <strong>1 min</strong> de la station, à l'angle de la rue du Télégraphe et de la rue Pixérécourt, se trouve le <strong>point le plus haut de Paris intra-muros</strong>, mesuré à <strong>128,21 m d'altitude</strong>. <strong>Légèrement plus haut que la butte Montmartre</strong> (130 m à la sortie M12 Lamarck-Caulaincourt mais varie selon point exact). Témoigne du caractère élevé du nord-est parisien (anciennes carrières). Plaque commémorative au sol.")
        ],
        "itin": [
            ("Point le plus haut de Paris", "point-plus-haut-paris", "à pied", "1 min direct", 1),
            ("Cimetière de Belleville", "cimetiere-belleville", "à pied", "Sortie directe", 2),
            ("Place des Fêtes via M11", "place-des-fetes", "M11", "M11 direction Châtelet (1 station)", 2),
            ("Porte des Lilas via M11", "porte-des-lilas", "M11", "M11 direction Rosny (1 station)", 2),
            ("Châtelet via M11", "chatelet", "M11", "M11 direction Châtelet (10 stations)", 20),
            ("Buttes-Chaumont via M7bis (à Place des Fêtes)", "buttes-chaumont", "M11 + M7bis", "M11 → Place des Fêtes + M7bis", 8)
        ]
    },
    "mairie-des-lilas": {
        "addr": "Mairie des Lilas, 93260 Les Lilas", "arr": "Les Lilas (93)",
        "seo": "Station Mairie des Lilas : M11 aux Lilas (Seine-Saint-Denis 93). Hôtel de Ville des Lilas. Ancien terminus est M11 jusqu'à l'extension du 13 juin 2024.",
        "tagline": "M11 — Mairie des Lilas (ex-terminus est)",
        "hero_desc": "Station <strong>Mairie des Lilas</strong> aux <strong>Lilas</strong> (Seine-Saint-Denis, 93). Desservie par la <strong>M11</strong> (ouverte 17 février 1937). <strong>Ancien terminus est de la M11</strong> jusqu'à l'<strong>extension à Rosny-Bois-Perrier le 13 juin 2024</strong>. À la sortie : l'<strong>Hôtel de Ville des Lilas</strong>.",
        "intros": [
            "La station <strong>Mairie des Lilas</strong> est située aux <strong>Lilas</strong> (Seine-Saint-Denis, 93), commune limitrophe de Paris (20e). Elle est desservie par la <strong>M11</strong> (Châtelet ↔ Rosny - Bois-Perrier), entre <strong>Porte des Lilas</strong> (1 station vers le sud-ouest) et <strong>Serge Gainsbourg</strong> (1 station vers le nord-est, ouverte 13 juin 2024). Bus 96, 105, 115, 129, 170.",
            "Ouverte le <strong>17 février 1937</strong> avec le prolongement de la M11 de Porte des Lilas à Mairie des Lilas. <strong>Terminus est de la M11 pendant 87 ans</strong>, jusqu'au <strong>13 juin 2024</strong> et l'<strong>extension à Rosny-Bois-Perrier</strong> (5 nouvelles stations ajoutées).",
            "À la sortie : l'<strong>Hôtel de Ville des Lilas</strong>, mairie de la commune des Lilas (~22 000 habitants). Centre civique de la commune."
        ],
        "hist_title": "1937 : terminus, 2024 : extension à Rosny",
        "hist": [
            "La station <strong>Mairie des Lilas</strong> est inaugurée le <strong>17 février 1937</strong> avec le <strong>prolongement de la M11 de Porte des Lilas à Mairie des Lilas</strong> (2 stations ajoutées : Place des Fêtes existe déjà sur M7bis, donc + Mairie des Lilas).",
            "<strong>Terminus est de la M11 pendant 87 ans</strong> (1937-2024), l'une des stations terminus les plus longues sans modification du réseau parisien.",
            "Le <strong>13 juin 2024</strong> : <strong>extension à Rosny-Bois-Perrier</strong>, avec 5 nouvelles stations ajoutées : <strong>Serge Gainsbourg</strong>, <strong>Romainville - Carnot</strong>, <strong>Montreuil - Hôpital</strong>, <strong>La Dhuys</strong>, <strong>Coteaux Beauclair</strong>, <strong>Rosny - Bois-Perrier</strong> (terminus, correspondance RER E).",
            "La <strong>commune des Lilas</strong> (~22 000 habitants) doit son nom aux <strong>lilas qui parfumaient l'ancien village rural</strong> au XIXe siècle. Annexée partiellement à Paris en 1860, reste commune indépendante. <strong>Hôtel de Ville des Lilas</strong> conçu en 1932 (style Art déco)."
        ],
        "faq": [
            ("Quelle ligne dessert Mairie des Lilas ?", "Uniquement la <strong>M11</strong> (Châtelet ↔ Rosny - Bois-Perrier depuis 2024). Bus 96, 105, 115, 129, 170."),
            ("C'était le terminus M11 ?", "<strong>Oui pendant 87 ans</strong>, de 1937 à 2024. <strong>L'extension du 13 juin 2024</strong> à Rosny-Bois-Perrier a ajouté 5 stations supplémentaires."),
            ("Quelles sont les nouvelles stations 2024 ?", "<strong>Serge Gainsbourg, Romainville - Carnot, Montreuil - Hôpital, La Dhuys, Coteaux Beauclair, Rosny - Bois-Perrier</strong> (terminus, correspondance RER E)."),
            ("Où est l'Hôtel de Ville des Lilas ?", "À la sortie de la station — bâtiment Art déco de 1932."),
            ("Comment aller à Châtelet ?", "<strong>M11 directe</strong> : ~24 min (13 stations vers le sud-ouest)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station historique 1937.")
        ],
        "tips": [
            "<strong>Hôtel de Ville des Lilas</strong> à la sortie — Art déco 1932.",
            "Pour <strong>Châtelet</strong> : M11 directe (~24 min).",
            "Pour <strong>Rosny-Bois-Perrier</strong> (RER E) : M11 directe (terminus est, ~12 min, depuis 2024).",
            "Pour <strong>Serge Gainsbourg</strong> : M11 directe (1 station).",
            "Zone tarifaire 2 — vérifier votre titre transport."
        ],
        "trivia": [
            ("🏛️", "Terminus est M11 pendant 87 ans (1937-2024)", "<strong>Mairie des Lilas</strong> a été <strong>terminus est de la M11 pendant 87 ans</strong> (1937-2024), l'une des stations terminus les plus longues sans modification du réseau parisien. L'<strong>extension à Rosny-Bois-Perrier le 13 juin 2024</strong> a ajouté <strong>5 nouvelles stations</strong> au-delà de Mairie des Lilas : Serge Gainsbourg, Romainville - Carnot, Montreuil - Hôpital, La Dhuys, Coteaux Beauclair, et Rosny - Bois-Perrier (terminus avec correspondance RER E)."),
            ("🌸", "Les Lilas — village rural au parfum de lilas", "La <strong>commune des Lilas</strong> (~22 000 habitants) doit son nom aux <strong>lilas qui parfumaient l'ancien village rural</strong> au XIXe siècle. Avant l'annexion partielle à Paris en 1860 et la construction des fortifications de Thiers (1841-1844), le territoire était occupé par des <strong>vergers et plantations de lilas</strong>, fournissant le marché parisien en fleurs. Aujourd'hui : commune résidentielle limitrophe de Paris.")
        ],
        "itin": [
            ("Châtelet via M11", "chatelet", "M11", "M11 direction Châtelet (13 stations)", 24),
            ("Rosny-Bois-Perrier via M11", "rosny-bois-perrier", "M11", "M11 terminus est (5 stations, depuis 2024)", 12),
            ("Hôtel de Ville Les Lilas", "hotel-ville-lilas", "à pied", "Sortie directe", 1),
            ("Porte des Lilas via M11", "porte-des-lilas", "M11", "M11 direction Châtelet (1 station)", 2),
            ("Serge Gainsbourg via M11", "serge-gainsbourg", "M11", "M11 direction Rosny (1 station)", 2),
            ("République via M11", "republique", "M11", "M11 direction Châtelet (8 stations)", 17)
        ]
    },
    "serge-gainsbourg": {
        "addr": "Av. Saint-Maur, 93260 Les Lilas", "arr": "Les Lilas (93)",
        "seo": "Station Serge Gainsbourg : M11 aux Lilas (93), ouverte 13 juin 2024 avec l'extension M11. Nommée d'après Serge Gainsbourg, chanteur français iconique (1928-1991).",
        "tagline": "M11 — Serge Gainsbourg chanteur iconique (extension 2024)",
        "hero_desc": "Station <strong>Serge Gainsbourg</strong> aux <strong>Lilas</strong> (Seine-Saint-Denis, 93), ouverte le <strong>13 juin 2024</strong> avec l'<strong>extension de la M11 à Rosny-Bois-Perrier</strong>. Nommée d'après <strong>Serge Gainsbourg</strong> (1928-1991), <strong>chanteur et compositeur français iconique</strong>. <strong>Première station M11 de l'extension est 2024</strong>.",
        "intros": [
            "La station <strong>Serge Gainsbourg</strong> est située aux <strong>Lilas</strong> (Seine-Saint-Denis, 93), sur l'avenue Saint-Maur. Elle est desservie par la <strong>M11</strong>, entre <strong>Mairie des Lilas</strong> (1 station vers le sud-ouest) et <strong>Romainville - Carnot</strong> (1 station vers le nord-est). Bus locaux Seine-Saint-Denis.",
            "Ouverte le <strong>13 juin 2024</strong> avec l'<strong>extension de la M11 de Mairie des Lilas à Rosny-Bois-Perrier</strong> (5 nouvelles stations ajoutées). <strong>Première station de l'extension</strong>.",
            "Le nom <strong>Serge Gainsbourg</strong> commémore <strong>Serge Gainsbourg</strong> (1928-1991), <strong>chanteur, compositeur, pianiste et réalisateur français</strong>. <strong>Né Lucien Ginsburg à Paris</strong>. L'un des artistes français les plus iconiques du XXe siècle. Œuvres : <em>Histoire de Melody Nelson</em> (1971), <em>L'Homme à tête de chou</em> (1976), <em>Je t'aime... moi non plus</em> (1969). Provocateur, libertaire."
        ],
        "hist_title": "13 juin 2024 : extension M11 et Gainsbourg iconique",
        "hist": [
            "La station <strong>Serge Gainsbourg</strong> est inaugurée le <strong>13 juin 2024</strong> avec l'<strong>extension de la M11 de Mairie des Lilas à Rosny-Bois-Perrier</strong> (5 stations ajoutées : Serge Gainsbourg, Romainville - Carnot, Montreuil - Hôpital, La Dhuys, Coteaux Beauclair, Rosny - Bois-Perrier).",
            "Le nom <strong>Serge Gainsbourg</strong> commémore <strong>Serge Gainsbourg</strong> (1928-1991), <strong>chanteur, compositeur, pianiste, réalisateur et acteur français</strong>. <strong>Né Lucien Ginsburg à Paris</strong> de parents juifs d'origine ukrainienne.",
            "<strong>L'un des artistes français les plus iconiques du XXe siècle</strong>. Carrière diversifiée : jazz (années 1950), pop (années 1960), funk (années 1970), rock (années 1980). Œuvres emblématiques : <strong><em>Histoire de Melody Nelson</em></strong> (1971, concept album), <strong><em>L'Homme à tête de chou</em></strong> (1976), <strong><em>Aux armes et cætera</em></strong> (1979, reggae), <strong><em>You're Under Arrest</em></strong> (1987).",
            "Chansons célèbres : <em>Je t'aime... moi non plus</em> (1969, avec Jane Birkin), <em>Bonnie and Clyde</em> (1968), <em>La Javanaise</em> (1963), <em>Comic Strip</em> (1968), <em>Initials BB</em> (1968), <em>Lemon Incest</em> (1984), <em>Bonnie and Clyde</em>, <em>69 année érotique</em>.",
            "<strong>Provocateur, libertaire, scandaleux</strong>. Brûle un billet de 500 francs en direct à la TV en 1984. Chanson <em>Aux armes et cætera</em> (1979) chantée en reggae. <strong>Décédé en 1991</strong>. Inhumé au cimetière du Montparnasse. <strong>Statue à Strasbourg-Saint-Denis</strong> Paris."
        ],
        "faq": [
            ("Quelle ligne dessert Serge Gainsbourg ?", "Uniquement la <strong>M11</strong>. Bus locaux Seine-Saint-Denis."),
            ("Quand a-t-elle ouvert ?", "Le <strong>13 juin 2024</strong>, avec l'extension de la M11 de Mairie des Lilas à Rosny-Bois-Perrier."),
            ("Qui est Serge Gainsbourg ?", "<strong>Serge Gainsbourg</strong> (1928-1991), <strong>chanteur, compositeur, pianiste et réalisateur français</strong>. L'un des artistes français les plus iconiques du XXe siècle. Œuvres : <em>Histoire de Melody Nelson</em>, <em>L'Homme à tête de chou</em>, <em>Je t'aime... moi non plus</em>, etc."),
            ("Quelle est la commune ?", "<strong>Les Lilas</strong>, commune de Seine-Saint-Denis (93). ~22 000 habitants."),
            ("Comment aller à Châtelet ?", "<strong>M11 directe</strong> : ~26 min (14 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Oui, entièrement</strong>. Station moderne 2024 conforme aux normes PMR.")
        ],
        "tips": [
            "<strong>Première station extension 2024</strong> — accessibilité totale.",
            "Pour <strong>Châtelet</strong> : M11 directe (~26 min).",
            "Pour <strong>Rosny-Bois-Perrier</strong> (RER E) : M11 directe (~10 min).",
            "Pour <strong>Mairie des Lilas</strong> : M11 directe (1 station).",
            "Zone tarifaire 2."
        ],
        "trivia": [
            ("🎵", "Serge Gainsbourg (1928-1991) — artiste français iconique", "<strong>Serge Gainsbourg</strong> (1928-1991), né <strong>Lucien Ginsburg à Paris</strong>, est l'un des <strong>artistes français les plus iconiques du XXe siècle</strong>. Carrière diversifiée : <strong>jazz, pop, funk, rock, reggae</strong>. Œuvres emblématiques : <em>Histoire de Melody Nelson</em> (1971, concept album culte), <em>L'Homme à tête de chou</em> (1976), <em>Aux armes et cætera</em> (1979, reggae avec La Marseillaise). Chansons célèbres : <em>Je t'aime... moi non plus</em> (1969, avec Jane Birkin), <em>Bonnie and Clyde</em>, <em>La Javanaise</em>. <strong>Provocateur</strong> : brûle un billet de 500 francs en direct TV (1984). Décédé en 1991, inhumé au cimetière du Montparnasse."),
            ("🚇", "Extension M11 (13 juin 2024) — 6 km, 5 nouvelles stations", "L'<strong>extension de la M11 de Mairie des Lilas à Rosny-Bois-Perrier</strong>, inaugurée le <strong>13 juin 2024</strong>, ajoute <strong>5 nouvelles stations</strong> (~6 km) : Serge Gainsbourg, Romainville - Carnot, Montreuil - Hôpital, La Dhuys, Coteaux Beauclair, et Rosny - Bois-Perrier (terminus avec correspondance RER E). Première extension de la M11 depuis <strong>1937</strong> (87 ans). Permet de désengorger le RER E et améliorer l'accès à l'est parisien.")
        ],
        "itin": [
            ("Châtelet via M11", "chatelet", "M11", "M11 direction Châtelet (14 stations)", 26),
            ("Rosny-Bois-Perrier via M11", "rosny-bois-perrier", "M11", "M11 terminus est (4 stations, depuis 2024)", 10),
            ("Mairie des Lilas via M11", "mairie-des-lilas", "M11", "M11 direction Châtelet (1 station)", 2),
            ("Romainville - Carnot via M11", "romainville-carnot", "M11", "M11 direction Rosny (1 station)", 2),
            ("République via M11", "republique", "M11", "M11 direction Châtelet (9 stations)", 19),
            ("Cimetière Montparnasse (tombe Gainsbourg)", "cimetiere-montparnasse", "M11 + M4", "M11 → Châtelet + M4 direction Bagneux", 35)
        ]
    },
    "romainville-carnot": {
        "addr": "Romainville (93)", "arr": "Romainville (93)",
        "seo": "Station Romainville - Carnot : M11 à Romainville (93), ouverte 13 juin 2024 avec extension M11. Commune de Romainville Seine-Saint-Denis.",
        "tagline": "M11 — Romainville (extension 2024)",
        "hero_desc": "Station <strong>Romainville - Carnot</strong> à <strong>Romainville</strong> (Seine-Saint-Denis, 93), ouverte le <strong>13 juin 2024</strong> avec l'extension de la M11. Première desserte métro de la commune de Romainville. Nom du <strong>Maréchal Carnot</strong> (« l'Organisateur de la Victoire »).",
        "intros": [
            "La station <strong>Romainville - Carnot</strong> est située à <strong>Romainville</strong> (Seine-Saint-Denis, 93). Elle est desservie par la <strong>M11</strong> (Châtelet ↔ Rosny - Bois-Perrier), entre <strong>Serge Gainsbourg</strong> (1 station vers le sud-ouest) et <strong>Montreuil - Hôpital</strong> (1 station vers le nord-est). Bus locaux 93.",
            "Ouverte le <strong>13 juin 2024</strong> avec l'extension M11 (5 nouvelles stations).",
            "Le nom commémore <strong>Lazare Carnot</strong> (1753-1823), <strong>« l'Organisateur de la Victoire »</strong>, général et homme politique français, membre du <strong>Comité de salut public</strong> et père de la <strong>conscription militaire moderne</strong>. <strong>Romainville</strong> (~28 000 habitants) est une commune de Seine-Saint-Denis."
        ],
        "hist_title": "13 juin 2024 : extension M11 à Romainville",
        "hist": [
            "La station est inaugurée le <strong>13 juin 2024</strong> avec l'extension M11 de Mairie des Lilas à Rosny-Bois-Perrier.",
            "Le nom <strong>Carnot</strong> commémore <strong>Lazare Carnot</strong> (1753-1823), <strong>général, mathématicien et homme politique français</strong>. Membre du <strong>Comité de salut public</strong> sous la Révolution. Surnommé <strong>« l'Organisateur de la Victoire »</strong> pour avoir réorganisé l'armée révolutionnaire et permis les <strong>14 victoires</strong> de la Première République. <strong>Père de la conscription militaire moderne</strong> (loi du 23 août 1793).",
            "<strong>Sadi Carnot</strong> (1796-1832), son fils, est l'un des fondateurs de la <strong>thermodynamique</strong> (Cycle de Carnot, second principe).",
            "<strong>Romainville</strong> est une commune de <strong>Seine-Saint-Denis (93)</strong>, ~28 000 habitants. Origine villageoise rurale, devenue résidentielle au XXe siècle. <strong>Première desserte métro</strong> de la commune avec cette extension. Quartier en mutation."
        ],
        "faq": [
            ("Quelle ligne dessert Romainville - Carnot ?", "Uniquement la <strong>M11</strong>. Bus locaux 93."),
            ("Quand a-t-elle ouvert ?", "Le <strong>13 juin 2024</strong>, avec l'extension M11."),
            ("Qui est Carnot ?", "<strong>Lazare Carnot</strong> (1753-1823), <strong>« l'Organisateur de la Victoire »</strong>, général de la Révolution française. Membre du Comité de salut public. <strong>Père de la conscription militaire moderne</strong>."),
            ("Quelle est la commune ?", "<strong>Romainville</strong>, commune de Seine-Saint-Denis (93), ~28 000 habitants. Première desserte métro avec cette extension."),
            ("Comment aller à Châtelet ?", "<strong>M11 directe</strong> : ~28 min (15 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Oui, entièrement</strong>. Station moderne 2024.")
        ],
        "tips": [
            "<strong>Première desserte métro de Romainville</strong> (depuis 2024).",
            "Pour <strong>Châtelet</strong> : M11 directe (~28 min).",
            "Pour <strong>Rosny-Bois-Perrier</strong> (RER E) : M11 directe (~8 min).",
            "Pour <strong>Serge Gainsbourg</strong> : M11 directe (1 station).",
            "Zone tarifaire 3."
        ],
        "trivia": [
            ("⚔️", "Lazare Carnot — « l'Organisateur de la Victoire »", "<strong>Lazare Carnot</strong> (1753-1823), <strong>général, mathématicien et homme politique français</strong>, est l'une des figures majeures de la Révolution française. <strong>Membre du Comité de salut public</strong>. Surnommé <strong>« l'Organisateur de la Victoire »</strong> pour avoir <strong>réorganisé l'armée révolutionnaire</strong> et permis les <strong>14 victoires</strong> de la Première République (dont Fleurus en 1794 avec Jourdan). <strong>Père de la conscription militaire moderne</strong> (loi du 23 août 1793, « levée en masse »). <strong>Comte d'Empire</strong> sous Napoléon. Père de Sadi Carnot (fondateur thermodynamique).")
        ],
        "itin": [
            ("Châtelet via M11", "chatelet", "M11", "M11 direction Châtelet (15 stations)", 28),
            ("Rosny-Bois-Perrier via M11", "rosny-bois-perrier", "M11", "M11 terminus est (3 stations)", 8),
            ("Serge Gainsbourg via M11", "serge-gainsbourg", "M11", "M11 direction Châtelet (1 station)", 2),
            ("Montreuil - Hôpital via M11", "montreuil-hopital", "M11", "M11 direction Rosny (1 station)", 2),
            ("Mairie des Lilas via M11", "mairie-des-lilas", "M11", "M11 direction Châtelet (2 stations)", 4),
            ("Romainville centre-ville", "romainville-centre", "à pied", "10 min", 10)
        ]
    },
    "montreuil-hopital": {
        "addr": "Montreuil / Noisy-le-Sec (93)", "arr": "Montreuil (93)",
        "seo": "Station Montreuil - Hôpital : M11 à Montreuil/Noisy-le-Sec (93), ouverte 13 juin 2024 avec extension M11. Dessert l'hôpital intercommunal et le quartier Boissière.",
        "tagline": "M11 — Montreuil/Noisy-le-Sec (extension 2024)",
        "hero_desc": "Station <strong>Montreuil - Hôpital</strong> à <strong>Montreuil</strong> et <strong>Noisy-le-Sec</strong> (Seine-Saint-Denis, 93), ouverte le <strong>13 juin 2024</strong> avec l'extension de la M11. Dessert l'<strong>hôpital intercommunal Montreuil/Noisy-le-Sec</strong>. Quartier Boissière en mutation.",
        "intros": [
            "La station <strong>Montreuil - Hôpital</strong> est située à la limite de <strong>Montreuil</strong> et <strong>Noisy-le-Sec</strong> (Seine-Saint-Denis, 93). Elle est desservie par la <strong>M11</strong>, entre <strong>Romainville - Carnot</strong> (1 station vers le sud-ouest) et <strong>La Dhuys</strong> (1 station vers le nord-est). Bus locaux 93.",
            "Ouverte le <strong>13 juin 2024</strong> avec l'extension M11.",
            "À proximité : l'<strong>hôpital intercommunal Montreuil/Noisy-le-Sec</strong>, établissement de santé desservant les deux communes. Le <strong>quartier Boissière</strong> autour est en mutation urbanistique."
        ],
        "hist_title": "13 juin 2024 : extension M11 et hôpital intercommunal",
        "hist": [
            "La station est inaugurée le <strong>13 juin 2024</strong> avec l'extension M11 de Mairie des Lilas à Rosny-Bois-Perrier.",
            "Le nom <strong>Hôpital</strong> commémore l'<strong>hôpital intercommunal Montreuil/Noisy-le-Sec</strong>, établissement de santé public desservant les deux communes voisines.",
            "<strong>Montreuil</strong> (~110 000 habitants) est la <strong>3e plus peuplée commune de Seine-Saint-Denis</strong> et la 4e plus peuplée d'Île-de-France hors Paris. Commune populaire et multiculturelle, en gentrification progressive depuis les années 2000. Surnommée « Le 21e arrondissement » par certains commentateurs.",
            "<strong>Noisy-le-Sec</strong> (~45 000 habitants), commune limitrophe avec un riche patrimoine industriel (anciennes usines). Gare RER E historique.",
            "Le <strong>quartier Boissière</strong> autour de la station fait l'objet d'un <strong>projet de rénovation urbaine</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Montreuil - Hôpital ?", "Uniquement la <strong>M11</strong>. Bus locaux 93."),
            ("Quand a-t-elle ouvert ?", "Le <strong>13 juin 2024</strong>, avec l'extension M11."),
            ("Quel hôpital dessert la station ?", "L'<strong>hôpital intercommunal Montreuil/Noisy-le-Sec</strong>, établissement de santé public desservant les deux communes."),
            ("Quelle est la commune ?", "À la limite de <strong>Montreuil</strong> (~110 000 hab.) et <strong>Noisy-le-Sec</strong> (~45 000 hab.), Seine-Saint-Denis (93)."),
            ("Comment aller à Châtelet ?", "<strong>M11 directe</strong> : ~30 min (16 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Oui, entièrement</strong>. Station moderne 2024.")
        ],
        "tips": [
            "<strong>Hôpital intercommunal</strong> à proximité.",
            "Pour <strong>Châtelet</strong> : M11 directe (~30 min).",
            "Pour <strong>Rosny-Bois-Perrier</strong> (RER E) : M11 directe (~6 min).",
            "Pour <strong>Romainville - Carnot</strong> : M11 directe (1 station).",
            "Zone tarifaire 3."
        ],
        "trivia": [
            ("🏥", "Hôpital intercommunal Montreuil/Noisy-le-Sec", "L'<strong>hôpital intercommunal Montreuil/Noisy-le-Sec</strong> à proximité de la station est un <strong>établissement de santé public</strong> desservant les deux communes voisines. Création remontant aux années 1970. Spécialités : médecine générale, urgences, maternité, gériatrie. L'extension M11 améliore considérablement l'accès depuis Paris pour les patients et soignants. Avant 2024 : accessible uniquement par bus depuis Mairie des Lilas (~20 min)."),
            ("🏙️", "Montreuil — « 21e arrondissement » de Paris", "<strong>Montreuil</strong> (~110 000 habitants) est la <strong>3e plus peuplée commune de Seine-Saint-Denis</strong> et la 4e plus peuplée d'Île-de-France hors Paris. Surnommée <strong>« le 21e arrondissement »</strong> par certains commentateurs en raison de sa proximité géographique avec Paris (limitrophe du 20e) et de sa <strong>gentrification progressive</strong> depuis les années 2000 (familles parisiennes cherchant des logements plus grands). Commune populaire et multiculturelle.")
        ],
        "itin": [
            ("Châtelet via M11", "chatelet", "M11", "M11 direction Châtelet (16 stations)", 30),
            ("Rosny-Bois-Perrier via M11", "rosny-bois-perrier", "M11", "M11 terminus est (2 stations)", 6),
            ("Romainville - Carnot via M11", "romainville-carnot", "M11", "M11 direction Châtelet (1 station)", 2),
            ("La Dhuys via M11", "la-dhuys", "M11", "M11 direction Rosny (1 station)", 2),
            ("Hôpital intercommunal", "hopital-montreuil-noisy", "à pied", "5 min direct", 5),
            ("Centre-ville Montreuil", "centre-montreuil", "à pied + bus", "15 min", 15)
        ]
    },
    "la-dhuys": {
        "addr": "Montreuil / Rosny-sous-Bois (93)", "arr": "Montreuil (93)",
        "seo": "Station La Dhuys : M11 à Montreuil/Rosny-sous-Bois (93), ouverte 13 juin 2024 avec extension M11. Aqueduc de la Dhuys (1862-1865, Haussmann, alimentation Paris en eau).",
        "tagline": "M11 — Aqueduc de la Dhuys (Haussmann 1865)",
        "hero_desc": "Station <strong>La Dhuys</strong> à la limite <strong>Montreuil/Rosny-sous-Bois</strong> (Seine-Saint-Denis, 93), ouverte le <strong>13 juin 2024</strong> avec l'extension de la M11. Nommée d'après l'<strong>aqueduc de la Dhuys</strong>, ouvrage hydraulique exceptionnel construit entre <strong>1862 et 1865</strong> sous Haussmann pour alimenter Paris en eau potable.",
        "intros": [
            "La station <strong>La Dhuys</strong> est située à la limite de <strong>Montreuil</strong> et <strong>Rosny-sous-Bois</strong> (Seine-Saint-Denis, 93). Elle est desservie par la <strong>M11</strong>, entre <strong>Montreuil - Hôpital</strong> (1 station vers le sud-ouest) et <strong>Coteaux Beauclair</strong> (1 station vers le nord-est). Bus locaux 93.",
            "Ouverte le <strong>13 juin 2024</strong> avec l'extension M11.",
            "Le nom <strong>La Dhuys</strong> commémore l'<strong>aqueduc de la Dhuys</strong>, <strong>ouvrage hydraulique exceptionnel</strong> construit entre <strong>1862 et 1865</strong> sous <strong>Haussmann</strong> par l'ingénieur <strong>Eugène Belgrand</strong>. <strong>131 km de long</strong>, capte la <strong>source de la Dhuys</strong> en Brie pour alimenter Paris en eau potable. Vestige encore visible."
        ],
        "hist_title": "1862-1865 : aqueduc de la Dhuys par Haussmann",
        "hist": [
            "La station est inaugurée le <strong>13 juin 2024</strong> avec l'extension M11.",
            "Le nom commémore l'<strong>aqueduc de la Dhuys</strong>, l'un des <strong>plus grands ouvrages hydrauliques du Second Empire</strong>. Construit entre <strong>1862 et 1865</strong> sous l'impulsion de <strong>Georges-Eugène Haussmann</strong> et conçu par l'ingénieur <strong>Eugène Belgrand</strong> (1810-1878, ingénieur hydraulique en chef de Paris).",
            "<strong>Caractéristiques techniques</strong> : <strong>131 km de long</strong>, capte les eaux de la <strong>source de la Dhuys</strong> dans la <strong>Brie champenoise</strong> (Marne, 100 m d'altitude). Trajet par <strong>gravité</strong> : Belleville (Reservoir des Lilas), 17 ponts-aqueducs, 21 siphons.",
            "<strong>Capacité historique : ~25 000 m³/jour</strong>. Alimentait Paris en eau potable. <strong>Encore partiellement en service aujourd'hui</strong> pour Eau de Paris (eau brute non potable).",
            "Le tracé de l'aqueduc traverse l'est parisien et la Seine-Saint-Denis, dont la commune de Montreuil. La <strong>promenade de la Dhuys</strong> suit son tracé sur plusieurs kilomètres."
        ],
        "faq": [
            ("Quelle ligne dessert La Dhuys ?", "Uniquement la <strong>M11</strong>. Bus locaux 93."),
            ("Quand a-t-elle ouvert ?", "Le <strong>13 juin 2024</strong>, avec l'extension M11."),
            ("Qu'est-ce que l'aqueduc de la Dhuys ?", "<strong>Aqueduc construit 1862-1865</strong> sous Haussmann par <strong>Eugène Belgrand</strong>. <strong>131 km de long</strong>, capte la source de la Dhuys en Brie pour alimenter Paris en eau potable. <strong>Encore partiellement en service</strong> aujourd'hui (Eau de Paris)."),
            ("Qui est Belgrand ?", "<strong>Eugène Belgrand</strong> (1810-1878), <strong>ingénieur hydraulique en chef de Paris</strong> sous Haussmann. Auteur des grands aqueducs alimentant Paris (Dhuys, Vanne, plus tard Avre). <strong>Père du réseau d'eau parisien moderne</strong>."),
            ("Comment aller à Châtelet ?", "<strong>M11 directe</strong> : ~32 min (17 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Oui, entièrement</strong>. Station moderne 2024.")
        ],
        "tips": [
            "<strong>Promenade de la Dhuys</strong> à proximité — suit le tracé de l'aqueduc.",
            "Pour <strong>Châtelet</strong> : M11 directe (~32 min).",
            "Pour <strong>Rosny-Bois-Perrier</strong> (RER E) : M11 directe (~4 min).",
            "Pour <strong>Montreuil - Hôpital</strong> : M11 directe (1 station).",
            "Zone tarifaire 3."
        ],
        "trivia": [
            ("💧", "Aqueduc de la Dhuys (1862-1865) — 131 km hydraulique Haussmann", "L'<strong>aqueduc de la Dhuys</strong>, à l'origine du nom de la station, est l'un des <strong>plus grands ouvrages hydrauliques du Second Empire</strong>. Construit entre <strong>1862 et 1865</strong> sous <strong>Haussmann</strong>, conçu par l'ingénieur <strong>Eugène Belgrand</strong> (1810-1878). <strong>131 km de long</strong>, capte les eaux de la <strong>source de la Dhuys</strong> dans la <strong>Brie champenoise</strong> (Marne, 100 m d'altitude). Trajet par <strong>gravité</strong> jusqu'au <strong>Réservoir des Lilas</strong> : <strong>17 ponts-aqueducs</strong>, <strong>21 siphons</strong>. <strong>Capacité historique : ~25 000 m³/jour</strong>. <strong>Encore partiellement en service</strong> aujourd'hui pour Eau de Paris (eau brute non potable)."),
            ("👨‍🔧", "Eugène Belgrand — père du réseau d'eau parisien moderne", "<strong>Eugène Belgrand</strong> (1810-1878), <strong>ingénieur hydraulique en chef de Paris</strong> sous Haussmann. <strong>Père du réseau d'eau parisien moderne</strong>. Auteur des <strong>grands aqueducs alimentant Paris</strong> : Dhuys (1862-1865), Vanne (1866-1874), plus tard Avre (1893). <strong>Géologue</strong> et <strong>hydrologue</strong> de formation. Sa <strong>Société d'études</strong> sera la matrice du futur Eau de Paris. Statue à proximité de la place de l'Hôtel-de-Ville. <strong>Égout principal de Paris</strong> (rue Belgrand dans le 20e arr.) porte son nom.")
        ],
        "itin": [
            ("Châtelet via M11", "chatelet", "M11", "M11 direction Châtelet (17 stations)", 32),
            ("Rosny-Bois-Perrier via M11", "rosny-bois-perrier", "M11", "M11 terminus est (1 station)", 4),
            ("Montreuil - Hôpital via M11", "montreuil-hopital", "M11", "M11 direction Châtelet (1 station)", 2),
            ("Coteaux Beauclair via M11", "coteaux-beauclair", "M11", "M11 direction Rosny (1 station)", 2),
            ("Promenade de la Dhuys", "promenade-dhuys", "à pied", "5 min direct", 5),
            ("Réservoir des Lilas via M11 + bus", "reservoir-lilas", "M11 + bus", "M11 → Mairie des Lilas + bus", 25)
        ]
    },
    "coteaux-beauclair": {
        "addr": "Noisy-le-Sec / Rosny-sous-Bois (93)", "arr": "Noisy-le-Sec (93)",
        "seo": "Station Coteaux Beauclair : M11 à Noisy-le-Sec/Rosny-sous-Bois (93), ouverte 13 juin 2024 avec extension M11. Quartier Coteaux Beauclair.",
        "tagline": "M11 — quartier Coteaux Beauclair (extension 2024)",
        "hero_desc": "Station <strong>Coteaux Beauclair</strong> à la limite <strong>Noisy-le-Sec/Rosny-sous-Bois</strong> (Seine-Saint-Denis, 93), ouverte le <strong>13 juin 2024</strong> avec l'extension de la M11. Dessert le <strong>quartier Coteaux Beauclair</strong>, zone résidentielle en mutation.",
        "intros": [
            "La station <strong>Coteaux Beauclair</strong> est située à la limite de <strong>Noisy-le-Sec</strong> et <strong>Rosny-sous-Bois</strong> (Seine-Saint-Denis, 93). Elle est desservie par la <strong>M11</strong>, entre <strong>La Dhuys</strong> (1 station vers le sud-ouest) et <strong>Rosny - Bois-Perrier</strong> (1 station vers le nord-est, terminus + RER E). Bus locaux 93.",
            "Ouverte le <strong>13 juin 2024</strong> avec l'extension M11.",
            "Dessert le <strong>quartier Coteaux Beauclair</strong>, zone résidentielle en mutation à la limite de Noisy-le-Sec et Rosny-sous-Bois. Le nom évoque les <strong>coteaux</strong> (terrain en pente) du secteur."
        ],
        "hist_title": "13 juin 2024 : extension M11 et quartier Coteaux Beauclair",
        "hist": [
            "La station est inaugurée le <strong>13 juin 2024</strong> avec l'extension M11 (5 nouvelles stations).",
            "Le nom <strong>Coteaux Beauclair</strong> désigne le <strong>quartier résidentiel</strong> à la limite de <strong>Noisy-le-Sec</strong> et <strong>Rosny-sous-Bois</strong>. Étymologie : <strong>« Coteaux »</strong> = terrain en pente (le secteur est sur les hauteurs du nord-est parisien). <strong>« Beauclair »</strong> = nom historique de la zone (probablement d'une ancienne propriété).",
            "<strong>Noisy-le-Sec</strong> (~45 000 habitants) est une commune de Seine-Saint-Denis avec un riche <strong>patrimoine industriel</strong> (anciennes usines XIXe-XXe). <strong>Gare RER E historique</strong>. Profondément bombardée en 1944 lors des combats de la libération de Paris.",
            "<strong>Rosny-sous-Bois</strong> (~46 000 habitants) est une autre commune de Seine-Saint-Denis. <strong>Centre commercial Rosny 2</strong> à proximité.",
            "Le quartier Coteaux Beauclair fait l'objet d'un <strong>projet de rénovation urbaine</strong> autour de l'arrivée du métro."
        ],
        "faq": [
            ("Quelle ligne dessert Coteaux Beauclair ?", "Uniquement la <strong>M11</strong>. Bus locaux 93."),
            ("Quand a-t-elle ouvert ?", "Le <strong>13 juin 2024</strong>, avec l'extension M11."),
            ("Quelle est la commune ?", "À la limite de <strong>Noisy-le-Sec</strong> et <strong>Rosny-sous-Bois</strong> (Seine-Saint-Denis 93)."),
            ("Comment aller à Châtelet ?", "<strong>M11 directe</strong> : ~34 min (18 stations)."),
            ("Comment aller à Rosny-Bois-Perrier (RER E) ?", "<strong>M11 directe</strong> : 1 station vers le nord-est (~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Oui, entièrement</strong>. Station moderne 2024.")
        ],
        "tips": [
            "Pour <strong>Rosny-Bois-Perrier</strong> (RER E) : M11 directe (1 station).",
            "Pour <strong>Châtelet</strong> : M11 directe (~34 min).",
            "Pour <strong>Centre commercial Rosny 2</strong> : M11 → Rosny + à pied.",
            "Pour <strong>La Dhuys</strong> : M11 directe (1 station).",
            "Zone tarifaire 3 — vérifier votre titre transport."
        ],
        "trivia": [
            ("🏘️", "Coteaux Beauclair — quartier résidentiel rénové", "Le <strong>quartier Coteaux Beauclair</strong> à la limite de <strong>Noisy-le-Sec</strong> et <strong>Rosny-sous-Bois</strong> fait l'objet d'un <strong>projet de rénovation urbaine</strong> autour de l'arrivée du métro. Étymologie : <strong>« Coteaux »</strong> = terrain en pente (hauteurs du nord-est parisien). <strong>« Beauclair »</strong> = nom historique (ancienne propriété). L'arrivée de la M11 le <strong>13 juin 2024</strong> ouvre le quartier sur Paris en ~34 min — révolution d'accessibilité.")
        ],
        "itin": [
            ("Châtelet via M11", "chatelet", "M11", "M11 direction Châtelet (18 stations)", 34),
            ("Rosny-Bois-Perrier via M11", "rosny-bois-perrier", "M11", "M11 terminus est (1 station)", 2),
            ("La Dhuys via M11", "la-dhuys", "M11", "M11 direction Châtelet (1 station)", 2),
            ("Centre commercial Rosny 2", "rosny-2", "M11 + à pied", "M11 → Rosny + 5 min", 7),
            ("RER E direction Paris-Saint-Lazare", "rer-e-saint-lazare", "M11 + RER E", "M11 → Rosny + RER E", 15),
            ("République via M11", "republique", "M11", "M11 direction Châtelet (13 stations)", 27)
        ]
    },
    "rosny-bois-perrier": {
        "addr": "Rosny-sous-Bois (93)", "arr": "Rosny-sous-Bois (93)",
        "seo": "Station Rosny-Bois-Perrier : M11 terminus est à Rosny-sous-Bois (93), ouverte 13 juin 2024. Correspondance RER E (vers Paris-Saint-Lazare et Chelles). Centre commercial Rosny 2.",
        "tagline": "M11 + RER E — terminus est, Rosny 2",
        "hero_desc": "Station <strong>Rosny - Bois-Perrier</strong>, <strong>terminus est de la M11</strong> ouvert le <strong>13 juin 2024</strong>. Située à <strong>Rosny-sous-Bois</strong> (Seine-Saint-Denis, 93). Correspondance directe avec la <strong>gare RER E Rosny-Bois-Perrier</strong> (Paris-Saint-Lazare ↔ Chelles - Gournay). À côté : le <strong>Centre commercial Rosny 2</strong>, l'un des plus grands d'Île-de-France.",
        "intros": [
            "La station <strong>Rosny - Bois-Perrier</strong> est <strong>terminus est de la M11</strong>, ouverte le <strong>13 juin 2024</strong> avec l'extension M11. Située à <strong>Rosny-sous-Bois</strong> (Seine-Saint-Denis, 93). Correspondance directe avec la <strong>gare RER E Rosny-Bois-Perrier</strong> (Paris-Saint-Lazare ↔ Chelles - Gournay), entre <strong>Coteaux Beauclair</strong> (1 station vers le sud-ouest) et le terminus. Bus locaux 93.",
            "Ouverte le <strong>13 juin 2024</strong> comme <strong>terminus est du prolongement de la M11</strong>. Première liaison directe métro Châtelet ↔ Rosny-Bois-Perrier, désengorgeant le RER E.",
            "À <strong>5 min</strong> : le <strong>Centre commercial Rosny 2</strong>, l'un des <strong>plus grands d'Île-de-France</strong>. ~140 boutiques, ~50 000 m². Ouvert en 1973, rénové. Restaurants, cinémas, hypermarchés."
        ],
        "hist_title": "13 juin 2024 : terminus est M11 et hub multimodal",
        "hist": [
            "La station est inaugurée le <strong>13 juin 2024</strong> comme <strong>terminus est du prolongement de la M11</strong> de Mairie des Lilas à Rosny-Bois-Perrier (5 stations ajoutées). <strong>Première liaison directe métro Châtelet ↔ Rosny-Bois-Perrier</strong>.",
            "<strong>Pôle multimodal majeur</strong> : <strong>M11</strong> (terminus est) + <strong>RER E</strong> (Paris-Saint-Lazare ↔ Chelles - Gournay) + bus. Permet de <strong>désengorger le RER E</strong> qui était saturé sur ses dernières stations parisiennes.",
            "<strong>Rosny-sous-Bois</strong> (~46 000 habitants) est une commune de Seine-Saint-Denis. <strong>Centre commercial Rosny 2</strong> à proximité (5 min à pied), l'un des <strong>plus grands centres commerciaux d'Île-de-France</strong>. <strong>~140 boutiques</strong>, <strong>~50 000 m²</strong>. Ouvert en 1973, rénové plusieurs fois. Restaurants, cinéma multiplex, hypermarchés.",
            "L'extension M11 est conçue pour <strong>améliorer significativement les temps de trajet</strong> entre l'est parisien et le centre. Châtelet en ~38 min depuis Rosny (vs ~25 min en RER E mais avec correspondance bus depuis nombreuses zones non desservies)."
        ],
        "faq": [
            ("Quelles lignes desservent Rosny-Bois-Perrier ?", "<strong>M11</strong> (terminus est, depuis 2024) + <strong>RER E</strong> (Paris-Saint-Lazare ↔ Chelles - Gournay). Bus locaux 93."),
            ("Quand a-t-elle ouvert ?", "Le <strong>13 juin 2024</strong> comme terminus est du prolongement M11."),
            ("Où est Rosny 2 ?", "<strong>5 min à pied</strong> de la station. <strong>Centre commercial Rosny 2</strong>, l'un des plus grands d'Île-de-France. <strong>~140 boutiques</strong>, <strong>~50 000 m²</strong>. Ouvert 1973."),
            ("Comment aller à Châtelet ?", "<strong>M11 directe</strong> : ~38 min (19 stations) OU <strong>RER E vers Paris-Saint-Lazare + correspondance</strong> (~25 min plus rapide)."),
            ("Pour Paris-Saint-Lazare : M11 ou RER E ?", "<strong>RER E plus rapide</strong> : ~18 min direct. M11 nécessite correspondance."),
            ("La station est-elle accessible PMR ?", "<strong>Oui, entièrement</strong>. Station moderne 2024.")
        ],
        "tips": [
            "<strong>Centre commercial Rosny 2</strong> à 5 min — l'un des plus grands d'Île-de-France.",
            "Pour <strong>Paris-Saint-Lazare</strong> : RER E directe (~18 min, plus rapide que M11).",
            "Pour <strong>Châtelet</strong> : M11 directe (~38 min).",
            "Pour <strong>Chelles - Gournay</strong> : RER E directe est.",
            "Zone tarifaire 3 — vérifier votre titre transport."
        ],
        "trivia": [
            ("🚇", "Première liaison directe métro Châtelet ↔ Rosny (2024)", "L'extension de la M11 à <strong>Rosny - Bois-Perrier le 13 juin 2024</strong> crée la <strong>première liaison directe métro</strong> entre <strong>Châtelet et Rosny-sous-Bois</strong>. <strong>~38 min en M11 directe</strong>. Désengorge le <strong>RER E</strong> qui était saturé sur ses dernières stations parisiennes. <strong>5 stations ajoutées</strong> (~6 km nouvelle infrastructure) : Serge Gainsbourg, Romainville - Carnot, Montreuil - Hôpital, La Dhuys, Coteaux Beauclair, et Rosny - Bois-Perrier (terminus avec correspondance RER E)."),
            ("🛍️", "Centre commercial Rosny 2 (1973) — l'un des plus grands d'IDF", "À <strong>5 min</strong>, le <strong>Centre commercial Rosny 2</strong> est l'un des <strong>plus grands centres commerciaux d'Île-de-France</strong>. <strong>Ouvert en 1973</strong>, rénové plusieurs fois. <strong>~140 boutiques</strong> sur <strong>~50 000 m²</strong>. <strong>Restaurants</strong>, <strong>cinéma multiplex</strong>, <strong>hypermarchés</strong>. Hôtels, parking 5 000 places. Concept de centre commercial régional typique des années 1970 (style nord-américain importé). Affluence ~12 millions de visiteurs/an.")
        ],
        "itin": [
            ("Paris-Saint-Lazare via RER E", "saint-lazare", "RER E", "RER E direction Paris-Saint-Lazare", 18),
            ("Châtelet via M11", "chatelet", "M11", "M11 direction Châtelet (19 stations)", 38),
            ("Centre commercial Rosny 2", "rosny-2", "à pied", "5 min direct", 5),
            ("Coteaux Beauclair via M11", "coteaux-beauclair", "M11", "M11 direction Châtelet (1 station)", 2),
            ("Chelles - Gournay via RER E", "chelles-gournay", "RER E", "RER E direction Chelles", 15),
            ("République via M11", "republique", "M11", "M11 direction Châtelet (14 stations)", 30)
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
    elif "Les Lilas" in c["arr"]:
        d["tariff_zone"] = 2
        d["tariff_zone_context"] = "Seine-Saint-Denis (93), zone tarifaire 2"
        d["commune"] = "Les Lilas"
    else:
        d["tariff_zone"] = 3
        d["tariff_zone_context"] = "Seine-Saint-Denis (93), zone tarifaire 3"
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
        except Exception as e: print(f"✗ {slug}: {e}", file=sys.stderr)
