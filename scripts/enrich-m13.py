#!/usr/bin/env python3
"""Enrichit M13 — 22 stations T0 (biographies sensibles neutralisées)."""
import json
from pathlib import Path
ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    "saint-denis-universite": {
        "addr": "Avenue du Président-Wilson, 93200 Saint-Denis", "arr": "Saint-Denis (93)",
        "seo": "Station Saint-Denis - Université, terminus nord branche Saint-Denis M13 à Saint-Denis (93). Université Paris 8 à proximité.",
        "tagline": "M13 — terminus branche Saint-Denis, université",
        "hero_desc": "Station <strong>Saint-Denis - Université</strong>, <strong>terminus nord de la branche Saint-Denis</strong> de la <strong>ligne 13</strong>, à <strong>Saint-Denis</strong> (Seine-Saint-Denis, 93). Ouverte le <strong>25 mai 1998</strong>. À proximité de l'<strong>université Paris 8 Vincennes-Saint-Denis</strong>.",
        "intros": [
            "La station <strong>Saint-Denis - Université</strong> est <strong>terminus nord de la branche Saint-Denis</strong> de la <strong>M13</strong>, située à <strong>Saint-Denis</strong> (Seine-Saint-Denis, 93). Bus 154, 254, 255, 268, 356, T8 tramway.",
            "Ouverte le <strong>25 mai 1998</strong> avec le <strong>prolongement de la M13</strong> de <strong>Basilique de Saint-Denis à Saint-Denis - Université</strong>.",
            "À proximité : l'<strong>université Paris 8 Vincennes-Saint-Denis</strong> (~25 000 étudiants). <strong>Saint-Denis</strong> (~115 000 habitants), <strong>préfecture de la Seine-Saint-Denis</strong>."
        ],
        "hist_title": "1998 : terminus nord et université",
        "hist": [
            "La station Saint-Denis - Université est <strong>inaugurée le 25 mai 1998</strong> avec le <strong>prolongement de la M13</strong>.",
            "L'<strong>université Paris 8 Vincennes-Saint-Denis</strong>, à proximité, est fondée à <strong>Vincennes en 1968</strong> dans le cadre des réformes universitaires post-Mai 68. <strong>Transférée à Saint-Denis en 1980</strong>. <strong>~25 000 étudiants</strong>, spécialisée en <strong>sciences humaines et sociales</strong>.",
            "<strong>Saint-Denis</strong>, ~115 000 habitants, est la <strong>préfecture de la Seine-Saint-Denis</strong>. <strong>Berceau historique</strong> de la <strong>monarchie française</strong> avec la <strong>basilique Saint-Denis</strong>, nécropole royale."
        ],
        "faq": [
            ("Quelles lignes desservent Saint-Denis - Université ?", "<strong>M13</strong> (terminus nord branche Saint-Denis) + <strong>tramway T8</strong>. Bus 154, 254, 255, 268, 356."),
            ("Quand a-t-elle ouvert ?", "Le <strong>25 mai 1998</strong>."),
            ("Pour l'université Paris 8 ?", "<strong>~5 min à pied</strong>."),
            ("Pour la basilique Saint-Denis ?", "<strong>M13 directe</strong> (2 stations)."),
            ("Pour Châtelet ?", "<strong>M13 directe</strong> (~30 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Oui</strong>. Station moderne (1998).")
        ],
        "tips": [
            "<strong>Université Paris 8</strong> à 5 min à pied (~25 000 étudiants).",
            "<strong>Tramway T8</strong> en correspondance.",
            "Pour <strong>basilique Saint-Denis</strong> : <strong>M13 directe</strong> (2 stations).",
            "Pour <strong>Châtelet</strong> : <strong>M13 directe</strong> (~30 min).",
            "Zone tarifaire <strong>3</strong>, Seine-Saint-Denis."
        ],
        "trivia": [
            ("🎓", "Université Paris 8, héritière de Vincennes", "L'<strong>université Paris 8 Vincennes-Saint-Denis</strong>, à 5 min à pied, est fondée à <strong>Vincennes en 1968</strong> dans le cadre des réformes universitaires post-Mai 68. <strong>Université expérimentale et pluridisciplinaire</strong> à ses débuts (Foucault, Deleuze, Châtelet y enseignèrent). <strong>Transférée à Saint-Denis en 1980</strong>. <strong>~25 000 étudiants</strong>, spécialisée en sciences humaines et sociales."),
            ("🏛️", "Saint-Denis, préfecture du 93", "<strong>Saint-Denis</strong>, ~115 000 habitants, est la <strong>préfecture de la Seine-Saint-Denis</strong>. Ville historique liée à la <strong>monarchie française</strong> avec la <strong>basilique Saint-Denis</strong> (nécropole royale). <strong>Stade de France</strong> (1998). <strong>Quartier Pleyel</strong> en pleine transformation pour les <strong>JO 2024</strong>.")
        ],
        "itin": [
            ("Université Paris 8", "saint-denis-universite", "à pied", "Sortie directe (5 min)", 5),
            ("Basilique de Saint-Denis", "basilique-de-saint-denis", "M13", "M13 directe (2 stations)", 5),
            ("Stade de France", "stade-de-france-saint-denis", "M13 + RER B", "M13 + bus 154", 12),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~22 min)", 22),
            ("Châtelet", "chatelet", "M13 + M4", "M13 → Saint-Lazare + M14", 28),
            ("La Défense", "la-defense", "M13 + RER A", "M13 → Champs-Élysées + M1", 25)
        ]
    },
    "basilique-de-saint-denis": {
        "addr": "Place Victor-Hugo, 93200 Saint-Denis", "arr": "Saint-Denis (93)",
        "seo": "Station Basilique de Saint-Denis (M13) à Saint-Denis (93). Basilique royale Saint-Denis, nécropole des rois de France, première grande cathédrale gothique du XIIe siècle.",
        "tagline": "M13 — basilique royale, nécropole des rois de France",
        "hero_desc": "Station <strong>Basilique de Saint-Denis</strong> à <strong>Saint-Denis</strong> (Seine-Saint-Denis, 93), au cœur de la <strong>ville royale</strong>. Desservie par la <strong>M13</strong>, ouverte le <strong>20 juin 1976</strong>. À la sortie : la <strong>basilique royale de Saint-Denis</strong>, <strong>nécropole des rois de France</strong> et <strong>première grande cathédrale gothique</strong> (XIIe siècle).",
        "intros": [
            "La station <strong>Basilique de Saint-Denis</strong> est implantée à <strong>Saint-Denis</strong> (Seine-Saint-Denis, 93), au cœur de l'ancienne ville royale. Elle est desservie par la <strong>ligne 13 du métro</strong>, entre <strong>Saint-Denis - Université</strong> (1 station) et <strong>Carrefour Pleyel</strong> (1 station). Bus 154, 253, 254, 255, T1 tramway, T5 tramway.",
            "Ouverte le <strong>20 juin 1976</strong> avec le <strong>prolongement de la M13</strong> de <strong>Carrefour Pleyel à Basilique de Saint-Denis</strong>.",
            "À la sortie : la <strong>basilique royale de Saint-Denis</strong>, <strong>première grande cathédrale gothique</strong> (XIIe siècle, abbé Suger) et <strong>nécropole des rois de France</strong>. <strong>43 rois, 32 reines, 63 princes et princesses</strong>, soit la quasi-totalité des souverains français depuis Dagobert Ier (639) jusqu'à Louis XVIII (1824)."
        ],
        "hist_title": "1976 : basilique gothique et nécropole royale",
        "hist": [
            "La station Basilique de Saint-Denis est <strong>inaugurée le 20 juin 1976</strong> avec le <strong>prolongement de la M13</strong> de Carrefour Pleyel.",
            "La <strong>basilique royale de Saint-Denis</strong>, à la sortie, est l'un des <strong>monuments majeurs du gothique européen</strong>. Construite à partir de <strong>1135</strong> sous l'impulsion de l'<strong>abbé Suger</strong>, conseiller des rois Louis VI et Louis VII. <strong>Premier édifice gothique</strong> au monde : utilisation de la <strong>croisée d'ogives</strong>, des <strong>arcs-boutants</strong>, de la <strong>verrière</strong> permettant de monter à des hauteurs jusque-là impossibles.",
            "La basilique devient <strong>nécropole royale</strong> dès le <strong>VIe siècle</strong> avec l'inhumation du roi <strong>Dagobert Ier</strong> en <strong>639</strong>. Au fil des siècles, elle accueille la quasi-totalité des <strong>rois et reines de France</strong> : <strong>43 rois</strong>, <strong>32 reines</strong>, <strong>63 princes et princesses</strong>. Les <strong>tombeaux</strong> et <strong>gisants</strong> sont des chefs-d'œuvre de la sculpture médiévale. <strong>Classée monument historique en 1862</strong>, <strong>basilique cathédrale</strong> depuis 1966."
        ],
        "faq": [
            ("Quelles lignes desservent Basilique de Saint-Denis ?", "<strong>M13</strong>, <strong>tramway T1</strong>, <strong>tramway T5</strong>. Bus 154, 253, 254, 255."),
            ("Quand a-t-elle ouvert ?", "Le <strong>20 juin 1976</strong>."),
            ("Qu'est-ce que la basilique de Saint-Denis ?", "<strong>Première grande cathédrale gothique</strong> (XIIe siècle, abbé Suger) et <strong>nécropole des rois de France</strong>. 43 rois, 32 reines, 63 princes inhumés."),
            ("Combien de rois inhumés ?", "<strong>43 rois</strong>, <strong>32 reines</strong>, <strong>63 princes et princesses</strong> — soit la quasi-totalité des souverains français de Dagobert Ier (639) à Louis XVIII (1824)."),
            ("Pour la basilique ?", "<strong>Sortie directe</strong>. Visite ~1h30."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Basilique royale</strong> à la sortie : nécropole de 43 rois de France, première cathédrale gothique.",
            "<strong>Tombeaux et gisants</strong> chefs-d'œuvre de la sculpture médiévale.",
            "<strong>Tramways T1 et T5</strong> en correspondance.",
            "Pour <strong>Stade de France</strong> : bus 154 ou T1.",
            "Zone tarifaire <strong>3</strong>, Seine-Saint-Denis."
        ],
        "trivia": [
            ("⛪", "Basilique de Saint-Denis, naissance du gothique", "La <strong>basilique royale de Saint-Denis</strong>, à la sortie de la station, est l'un des <strong>monuments fondateurs de l'art gothique</strong>. Construite à partir de <strong>1135</strong> sous l'impulsion de l'<strong>abbé Suger</strong>, conseiller des rois Louis VI et Louis VII. <strong>Première utilisation de la croisée d'ogives</strong>, des <strong>arcs-boutants</strong>, de la <strong>verrière haute</strong>. Le <strong>chœur</strong> de Suger (1144) est considéré comme le <strong>premier exemple d'architecture gothique</strong>. Modèle pour Notre-Dame de Paris, Chartres, Reims."),
            ("👑", "Nécropole royale, 43 rois inhumés", "La basilique est la <strong>nécropole des rois de France</strong> depuis l'inhumation du roi <strong>Dagobert Ier</strong> en <strong>639</strong>. <strong>43 rois</strong>, <strong>32 reines</strong>, <strong>63 princes et princesses</strong> y sont inhumés — soit la quasi-totalité des <strong>souverains français de Dagobert Ier à Louis XVIII</strong>. Les <strong>tombeaux et gisants</strong> sont des chefs-d'œuvre de la sculpture médiévale : <strong>Philippe le Bel</strong>, <strong>Catherine de Médicis</strong>, <strong>Henri II</strong>, <strong>François Ier</strong>, <strong>Louis XII et Anne de Bretagne</strong>.")
        ],
        "itin": [
            ("Basilique royale", "basilique-de-saint-denis", "à pied", "Sortie directe", 2),
            ("Saint-Denis - Université", "saint-denis-universite", "M13", "M13 directe (1 station)", 2),
            ("Stade de France", "stade-de-france-saint-denis", "T1 + RER B", "T1 ou bus 154", 10),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~20 min)", 20),
            ("Châtelet", "chatelet", "M13 + M4", "M13 → Saint-Lazare + M14", 24),
            ("La Défense", "la-defense", "M13 + RER A", "Via Champs-Élysées + M1", 24)
        ]
    },
    "carrefour-pleyel": {
        "addr": "Avenue du Général-de-Gaulle, 93200 Saint-Denis", "arr": "Saint-Denis (93)",
        "seo": "Station Carrefour Pleyel (M13) à Saint-Denis (93). Quartier Pleyel en transformation pour les JO 2024. Hommage à Ignace Pleyel, facteur de pianos.",
        "tagline": "M13 — quartier Pleyel, transformation JO 2024",
        "hero_desc": "Station <strong>Carrefour Pleyel</strong> à <strong>Saint-Denis</strong> (Seine-Saint-Denis, 93). Desservie par la <strong>M13</strong>, ouverte le <strong>20 juin 1976</strong>. Hommage à <strong>Ignace Pleyel</strong> (<strong>1757-1831</strong>), <strong>compositeur et facteur de pianos</strong>. Quartier en <strong>pleine transformation</strong> pour les <strong>JO 2024</strong>.",
        "intros": [
            "La station <strong>Carrefour Pleyel</strong> est implantée à <strong>Saint-Denis</strong> (Seine-Saint-Denis, 93). Elle est desservie par la <strong>M13</strong>, entre <strong>Basilique de Saint-Denis</strong> (1 station) et <strong>Mairie de Saint-Ouen</strong> (1 station). Bus 138, 255, 274, 356.",
            "Ouverte le <strong>20 juin 1976</strong> avec le <strong>prolongement de la M13</strong> de <strong>Carrefour Pleyel à Basilique de Saint-Denis</strong>.",
            "Le nom <strong>Pleyel</strong> rend hommage à <strong>Ignace Pleyel</strong> (<strong>1757-1831</strong>), <strong>compositeur</strong> et <strong>facteur de pianos</strong>. Fondateur en <strong>1807</strong> de la <strong>manufacture de pianos Pleyel</strong>, devenue célèbre dans le monde entier. Le quartier autour de la station est en <strong>profonde transformation urbaine</strong> avec la <strong>Tour Pleyel</strong> (1973, 129 m) et les nouveaux quartiers édifiés pour les <strong>JO 2024</strong>."
        ],
        "hist_title": "1976 : Pleyel et JO 2024",
        "hist": [
            "La station Carrefour Pleyel est <strong>inaugurée le 20 juin 1976</strong> avec le <strong>prolongement de la M13</strong> de <strong>La Fourche à Carrefour Pleyel</strong>.",
            "Le nom <strong>Pleyel</strong> rend hommage à <strong>Ignace Joseph Pleyel</strong> (<strong>18 juin 1757 - 14 novembre 1831</strong>), <strong>compositeur autrichien</strong> naturalisé français. Élève de <strong>Joseph Haydn</strong>. <strong>Fondateur en 1807 de la manufacture de pianos Pleyel</strong>, devenue l'une des plus prestigieuses au monde. <strong>Frédéric Chopin</strong> jouait sur les pianos Pleyel.",
            "Le quartier autour de la station est en <strong>profonde transformation urbaine</strong>. La <strong>Tour Pleyel</strong> (1973), <strong>129 m de haut</strong>, est le <strong>plus haut bâtiment de la Seine-Saint-Denis</strong>. Les <strong>JO 2024</strong> ont catalysé la <strong>rénovation du quartier</strong> : nouveaux quartiers, <strong>Village Olympique</strong> à proximité, gare du <strong>Grand Paris Express</strong> en construction."
        ],
        "faq": [
            ("Quelle ligne dessert Carrefour Pleyel ?", "Uniquement la <strong>M13</strong>. Bus 138, 255, 274, 356."),
            ("Qui est Ignace Pleyel ?", "<strong>Ignace Pleyel</strong> (1757-1831), <strong>compositeur autrichien naturalisé français</strong>. Élève de Haydn. Fondateur en <strong>1807</strong> de la <strong>manufacture de pianos Pleyel</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>20 juin 1976</strong>."),
            ("Pour la Tour Pleyel ?", "<strong>~5 min à pied</strong>. 129 m de haut, plus haut bâtiment du 93."),
            ("Pour les JO 2024 ?", "Quartier en transformation pour les JO. <strong>Village Olympique</strong> à proximité."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Tour Pleyel</strong> (1973, 129 m) à 5 min à pied.",
            "<strong>Quartier Pleyel</strong> en pleine transformation post-JO 2024.",
            "Pour <strong>Stade de France</strong> : ~10 min à pied ou bus.",
            "Pour <strong>basilique Saint-Denis</strong> : <strong>M13 directe</strong> (1 station).",
            "Zone tarifaire <strong>3</strong>, Seine-Saint-Denis."
        ],
        "trivia": [
            ("🎹", "Ignace Pleyel, pianos et Chopin", "<strong>Ignace Joseph Pleyel</strong> (1757-1831), <strong>compositeur autrichien</strong> naturalisé français. Élève de <strong>Joseph Haydn</strong>. <strong>Fondateur en 1807 de la manufacture de pianos Pleyel</strong>, l'une des plus prestigieuses au monde. <strong>Frédéric Chopin</strong> jouait exclusivement sur des pianos Pleyel et donna son <strong>premier concert parisien</strong> dans les salons Pleyel le <strong>26 février 1832</strong>. Les <strong>pianos Pleyel</strong> équipèrent les <strong>plus grands musiciens du XIXe siècle</strong> : Liszt, Saint-Saëns, Debussy, Ravel."),
            ("🏗️", "Tour Pleyel et JO 2024", "La <strong>Tour Pleyel</strong>, à 5 min à pied, est le <strong>plus haut bâtiment de la Seine-Saint-Denis</strong>. <strong>Construite en 1973</strong>, <strong>129 m de haut</strong>, <strong>39 étages</strong>. Initialement bureaux, elle est <strong>reconvertie en hôtel</strong> pour les <strong>JO 2024</strong>. Le quartier Pleyel est l'un des <strong>grands chantiers du Grand Paris Express</strong> avec la <strong>gare de Saint-Denis Pleyel</strong> en construction (ligne 14, 15, 16, 17).")
        ],
        "itin": [
            ("Tour Pleyel", "carrefour-pleyel", "à pied", "Avenue Général de Gaulle (5 min)", 5),
            ("Basilique de Saint-Denis", "basilique-de-saint-denis", "M13", "M13 directe (1 station)", 2),
            ("Stade de France", "stade-de-france-saint-denis", "à pied + RER", "10 min à pied + RER", 10),
            ("Mairie de Saint-Ouen", "mairie-de-saint-ouen", "M13", "M13 directe (1 station)", 2),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~18 min)", 18),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 22)
        ]
    },
    "garibaldi": {
        "addr": "Avenue Gabriel-Péri, 93400 Saint-Ouen-sur-Seine", "arr": "Saint-Ouen-sur-Seine (93)",
        "seo": "Station Garibaldi (M13) à Saint-Ouen-sur-Seine (93). Hommage à Giuseppe Garibaldi, héros italien du Risorgimento.",
        "tagline": "M13 — Garibaldi, unificateur de l'Italie",
        "hero_desc": "Station <strong>Garibaldi</strong> à <strong>Saint-Ouen-sur-Seine</strong> (Seine-Saint-Denis, 93). Desservie par la <strong>M13</strong>, ouverte le <strong>20 juin 1976</strong>. Hommage à <strong>Giuseppe Garibaldi</strong> (<strong>1807-1882</strong>), <strong>général italien</strong>, figure majeure du <strong>Risorgimento</strong> et de l'<strong>unification de l'Italie</strong>.",
        "intros": [
            "La station <strong>Garibaldi</strong> est implantée à <strong>Saint-Ouen-sur-Seine</strong> (Seine-Saint-Denis, 93). Elle est desservie par la <strong>M13</strong>, entre <strong>Mairie de Saint-Ouen</strong> (1 station) et <strong>Porte de Saint-Ouen</strong> (1 station). Bus 137, 173, 274.",
            "Ouverte le <strong>20 juin 1976</strong> avec le <strong>prolongement de la M13</strong> de <strong>Porte de Saint-Ouen à Carrefour Pleyel</strong>.",
            "Le nom <strong>Garibaldi</strong> rend hommage à <strong>Giuseppe Garibaldi</strong> (<strong>1807-1882</strong>), <strong>général italien</strong>, figure majeure du <strong>Risorgimento</strong> et de l'<strong>unification de l'Italie</strong> au XIXe siècle."
        ],
        "hist_title": "1976 : Garibaldi et Risorgimento",
        "hist": [
            "La station Garibaldi est <strong>inaugurée le 20 juin 1976</strong> avec le <strong>prolongement de la M13</strong> de <strong>Porte de Saint-Ouen à Carrefour Pleyel</strong>.",
            "Le nom <strong>Garibaldi</strong> rend hommage à <strong>Giuseppe Garibaldi</strong> (<strong>4 juillet 1807 - 2 juin 1882</strong>), <strong>général italien</strong>, figure majeure du <strong>Risorgimento</strong>. <strong>Acteur majeur de l'unification de l'Italie</strong> (1860 : célèbre <strong>expédition des Mille</strong> en Sicile).",
            "Garibaldi combattit également pour la France lors de la <strong>guerre franco-prussienne de 1870-1871</strong>, à la tête de l'<strong>armée des Vosges</strong>. <strong>Élu député</strong> à l'Assemblée nationale française en 1871. Surnommé le <strong>« héros des deux mondes »</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Garibaldi ?", "Uniquement la <strong>M13</strong>. Bus 137, 173, 274."),
            ("Qui est Garibaldi ?", "<strong>Giuseppe Garibaldi</strong> (1807-1882), <strong>général italien</strong>, artisan de l'<strong>unification de l'Italie</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>20 juin 1976</strong>."),
            ("Pour le centre Saint-Ouen ?", "<strong>M13 directe</strong> vers <strong>Mairie de Saint-Ouen</strong> (1 station)."),
            ("Pour le centre de Paris ?", "<strong>M13 directe</strong> vers <strong>Saint-Lazare</strong> (~14 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier <strong>Saint-Ouen</strong> résidentiel et commerçant.",
            "Pour <strong>Marché aux Puces de Saint-Ouen</strong> : <strong>M13 → Porte de Clignancourt M4</strong>.",
            "Pour <strong>Mairie de Saint-Ouen</strong> (hub M13+M14) : <strong>M13 directe</strong>.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M13 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Seine-Saint-Denis."
        ],
        "trivia": [
            ("🇮🇹", "Garibaldi et l'unification de l'Italie", "<strong>Giuseppe Garibaldi</strong> (1807-1882), <strong>général italien</strong>, figure majeure du <strong>Risorgimento</strong> (mouvement d'unification italienne). <strong>Expédition des Mille</strong> en Sicile (1860) : conquête du <strong>royaume des Deux-Siciles</strong> avec seulement <strong>1 000 volontaires</strong>. Acteur clé de l'<strong>unification italienne</strong> proclamée en 1861. Combattit aussi pour la France lors de la <strong>guerre franco-prussienne</strong> (1870-1871). Surnommé le <strong>« héros des deux mondes »</strong>."),
            ("🏛️", "Saint-Ouen, ancienne ville industrielle", "<strong>Saint-Ouen-sur-Seine</strong>, ~50 000 habitants, est l'une des communes de la <strong>Seine-Saint-Denis</strong>. Ancienne <strong>ville industrielle</strong> aux XIXe-XXe siècles. Elle abrite le célèbre <strong>marché aux Puces de Saint-Ouen</strong>, l'un des <strong>plus grands marchés d'antiquités au monde</strong> (~7 hectares, ~2 500 marchands). Quartier en transformation depuis les années 2010.")
        ],
        "itin": [
            ("Mairie de Saint-Ouen", "mairie-de-saint-ouen", "M13", "M13 directe (1 station)", 2),
            ("Porte de Saint-Ouen", "porte-de-saint-ouen", "M13", "M13 directe (1 station)", 2),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~14 min)", 14),
            ("Marché aux Puces", "porte-de-clignancourt", "M13 + M4", "M13 → Porte de Saint-Ouen + bus", 12),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 18),
            ("Champs-Élysées", "champs-elysees-clemenceau", "M13", "M13 directe (~16 min)", 16)
        ]
    },
    "porte-de-saint-ouen": {
        "addr": "Avenue de Saint-Ouen, 75017 Paris", "arr": "17e arrondissement (Paris)",
        "seo": "Station Porte de Saint-Ouen (M13) avenue de Saint-Ouen dans le 17e. Ancien terminus M13 (1912-1952). Bordure de Saint-Ouen.",
        "tagline": "M13 — porte vers Saint-Ouen",
        "hero_desc": "Station <strong>Porte de Saint-Ouen</strong> sur l'<strong>avenue de Saint-Ouen</strong> dans le <strong>17e arrondissement</strong>. Desservie par la <strong>M13</strong>, ouverte le <strong>20 janvier 1912</strong>. <strong>Ancien terminus nord</strong> de la ligne 13 (1912-1952).",
        "intros": [
            "La station <strong>Porte de Saint-Ouen</strong> est implantée sur l'<strong>avenue de Saint-Ouen</strong>, à la <strong>limite nord du 17e arrondissement</strong>. Elle est desservie par la <strong>M13</strong>, entre <strong>Garibaldi</strong> (1 station) et <strong>Guy Môquet</strong> (1 station). Bus 30, 60, 137, 173.",
            "Ouverte le <strong>20 janvier 1912</strong> comme <strong>terminus nord de la ligne B du Nord-Sud</strong> (devenue M13 en 1942).",
            "Elle conserve ce statut de <strong>terminus pendant 40 ans</strong>, jusqu'au <strong>prolongement vers Carrefour Pleyel</strong> en <strong>1952</strong>. À courte distance : le <strong>quartier de Saint-Ouen</strong> (Seine-Saint-Denis) et le <strong>marché aux Puces</strong>."
        ],
        "hist_title": "1912 : Porte de Saint-Ouen et ancien terminus",
        "hist": [
            "La station Porte de Saint-Ouen est <strong>inaugurée le 20 janvier 1912</strong> comme <strong>terminus nord de la ligne B du Nord-Sud</strong> (compagnie privée fusionnée avec la CMP en 1930, ligne devenue M13 en 1942).",
            "Elle conserve ce statut de <strong>terminus nord pendant 40 ans</strong>, jusqu'au <strong>prolongement vers Carrefour Pleyel</strong> en <strong>1952</strong>.",
            "L'<strong>avenue de Saint-Ouen</strong> traverse l'<strong>ancien village de Saint-Ouen</strong>, rattaché à Paris en partie en 1860. Le quartier autour de la station est résidentiel et populaire."
        ],
        "faq": [
            ("Quelle ligne dessert Porte de Saint-Ouen ?", "Uniquement la <strong>M13</strong>. Bus 30, 60, 137, 173."),
            ("Quand a-t-elle ouvert ?", "Le <strong>20 janvier 1912</strong> (comme terminus nord jusqu'en 1952)."),
            ("Pour Saint-Ouen ?", "<strong>M13 directe</strong> vers Saint-Ouen (banlieue 93)."),
            ("Pour le marché aux Puces ?", "<strong>~15 min à pied</strong> ou <strong>M13 → Garibaldi</strong>."),
            ("Pour Saint-Lazare ?", "<strong>M13 directe</strong> (~12 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier <strong>résidentiel populaire</strong> du 17e nord.",
            "<strong>Avenue de Saint-Ouen</strong> : axe commerçant.",
            "Pour <strong>marché aux Puces</strong> : ~15 min à pied.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M13 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🚇", "Ancien terminus 1912-1952", "Pendant <strong>40 ans</strong>, la station Porte de Saint-Ouen fut le <strong>terminus nord de la ligne 13</strong>. <strong>Inaugurée le 20 janvier 1912</strong> sur la <strong>ligne B du Nord-Sud</strong>, elle conserva ce statut jusqu'au <strong>prolongement de 1952</strong> vers Carrefour Pleyel. La ligne 13 actuelle est issue de la fusion de l'ancienne <strong>ligne 14 (1937)</strong> et de l'ancienne <strong>ligne 13</strong> en <strong>1976</strong>."),
            ("🛍️", "Marché aux Puces de Saint-Ouen", "Le <strong>marché aux Puces de Saint-Ouen</strong>, à 15 min à pied, est l'un des <strong>plus grands marchés d'antiquités au monde</strong>. ~<strong>7 hectares</strong>, <strong>~2 500 marchands</strong>, plusieurs millions de visiteurs par an. Fondé à la fin du <strong>XIXe siècle</strong> par des chiffonniers, il s'est progressivement spécialisé en <strong>antiquités, brocante, mobilier</strong>. <strong>Ouvert week-end et lundi</strong>.")
        ],
        "itin": [
            ("Marché aux Puces", "porte-de-clignancourt", "M13 + à pied", "À pied (15 min) ou via M4", 15),
            ("Garibaldi (Saint-Ouen)", "garibaldi", "M13", "M13 directe (1 station)", 2),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~12 min)", 12),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 16),
            ("Champs-Élysées", "champs-elysees-clemenceau", "M13", "M13 directe (~14 min)", 14),
            ("Mairie de Saint-Ouen", "mairie-de-saint-ouen", "M13", "M13 directe (2 stations)", 5)
        ]
    },
    "guy-moquet": {
        "addr": "Avenue de Saint-Ouen, 75017 Paris", "arr": "17e arrondissement (Paris)",
        "seo": "Station Guy Môquet (M13) avenue de Saint-Ouen dans le 17e. Hommage à Guy Môquet (1924-1941). Quartier résidentiel 17e.",
        "tagline": "M13 — Guy Môquet, 17e résidentiel",
        "hero_desc": "Station <strong>Guy Môquet</strong> sur l'<strong>avenue de Saint-Ouen</strong> dans le <strong>17e arrondissement</strong>. Desservie par la <strong>M13</strong>, ouverte le <strong>26 février 1911</strong>. Initialement nommée <strong>« Marcadet »</strong>. Renommée en <strong>1946</strong> en hommage à <strong>Guy Môquet</strong> (<strong>1924-1941</strong>).",
        "intros": [
            "La station <strong>Guy Môquet</strong> est implantée sur l'<strong>avenue de Saint-Ouen</strong> dans le <strong>17e arrondissement</strong>. Elle est desservie par la <strong>M13</strong>, entre <strong>Porte de Saint-Ouen</strong> (1 station) et <strong>La Fourche</strong> (1 station). Bus 31, 60, 95.",
            "Ouverte le <strong>26 février 1911</strong> sous le nom <strong>« Marcadet »</strong>. <strong>Renommée Guy Môquet</strong> le <strong>16 mai 1946</strong>.",
            "Le nom <strong>Guy Môquet</strong> rend hommage à <strong>Guy Môquet</strong> (<strong>26 avril 1924 - 22 octobre 1941</strong>), <strong>militant français</strong>. Fils du député communiste Prosper Môquet. Quartier <strong>résidentiel</strong> du <strong>17e arrondissement</strong>."
        ],
        "hist_title": "1911-1946 : Marcadet renommée Guy Môquet",
        "hist": [
            "La station est <strong>inaugurée le 26 février 1911</strong> sous le nom <strong>« Marcadet »</strong> sur la <strong>ligne B du Nord-Sud</strong> (compagnie privée fusionnée avec la CMP en 1930, ligne devenue M13 en 1942).",
            "<strong>Renommée Guy Môquet</strong> le <strong>16 mai 1946</strong>. Le nom commémore <strong>Guy Môquet</strong> (<strong>26 avril 1924 - 22 octobre 1941</strong>), <strong>militant français</strong>, fils du <strong>député communiste Prosper Môquet</strong> (élu du 17e arrondissement).",
            "Le quartier autour de la station est résidentiel et commerçant. À proximité : le <strong>square des Épinettes</strong> et le <strong>quartier des Batignolles</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Guy Môquet ?", "Uniquement la <strong>M13</strong>. Bus 31, 60, 95."),
            ("Quel était l'ancien nom ?", "<strong>« Marcadet »</strong> (1911-1946)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>26 février 1911</strong>, renommée en <strong>1946</strong>."),
            ("Qui est Guy Môquet ?", "<strong>Guy Môquet</strong> (1924-1941), <strong>militant français</strong>. Fils du député Prosper Môquet."),
            ("Pour le square des Épinettes ?", "<strong>~5 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Square des Épinettes</strong> à 5 min à pied.",
            "Quartier <strong>résidentiel</strong> du 17e.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M13 directe</strong>.",
            "Pour <strong>Place de Clichy</strong> : <strong>M13 directe</strong> (4 stations).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏘️", "Quartier des Épinettes (17e)", "Le <strong>quartier des Épinettes</strong>, autour de la station, est un quartier <strong>résidentiel et populaire</strong> du <strong>17e arrondissement</strong>. <strong>Square des Épinettes</strong> (1893, 5 280 m²), espace vert apprécié des familles. Quartier traditionnellement <strong>ouvrier</strong>, en pleine <strong>gentrification</strong> depuis les années 2000."),
            ("🏛️", "17e arrondissement, contrastes nord-sud", "Le <strong>17e arrondissement</strong> présente de <strong>forts contrastes</strong> entre le sud (Ternes, Wagram, Monceau — quartiers chic) et le nord (Épinettes, Batignolles — quartiers plus populaires). <strong>~170 000 habitants</strong>. Le <strong>nouveau quartier Clichy-Batignolles</strong> (parc Martin-Luther-King, Cité judiciaire de Renzo Piano) renouvelle le 17e nord depuis les années 2010.")
        ],
        "itin": [
            ("Square des Épinettes", "guy-moquet", "à pied", "Rue des Épinettes (5 min)", 5),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~10 min)", 10),
            ("Place de Clichy", "place-de-clichy", "M13", "M13 directe (4 stations)", 8),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 14),
            ("Champs-Élysées", "champs-elysees-clemenceau", "M13", "M13 directe (~12 min)", 12),
            ("Porte de Saint-Ouen", "porte-de-saint-ouen", "M13", "M13 directe (1 station)", 2)
        ]
    },
    "asnieres-gennevilliers-les-courtilles": {
        "addr": "Avenue Henri-Barbusse, 92230 Gennevilliers", "arr": "Gennevilliers (92)",
        "seo": "Station Asnières - Gennevilliers - Les Courtilles, terminus nord-ouest M13 branche Asnières. Hauts-de-Seine (92). Extension 2008.",
        "tagline": "M13 — terminus nord-ouest branche Asnières",
        "hero_desc": "Station <strong>Asnières - Gennevilliers - Les Courtilles</strong>, <strong>terminus nord-ouest de la branche Asnières</strong> de la <strong>M13</strong>, à la limite d'<strong>Asnières-sur-Seine</strong> et de <strong>Gennevilliers</strong> (Hauts-de-Seine, 92). Ouverte le <strong>14 juin 2008</strong>.",
        "intros": [
            "La station <strong>Asnières - Gennevilliers - Les Courtilles</strong> est <strong>terminus nord-ouest de la branche Asnières</strong> de la <strong>M13</strong>, à la limite d'<strong>Asnières-sur-Seine</strong> et de <strong>Gennevilliers</strong> (Hauts-de-Seine, 92). Bus 138, 175, 235, 304, 366, 378, tramway T1.",
            "Ouverte le <strong>14 juin 2008</strong> avec le <strong>prolongement de la branche Asnières</strong> de <strong>Gabriel Péri à Asnières - Gennevilliers - Les Courtilles</strong>.",
            "À proximité : la <strong>cité des Courtilles</strong> (Asnières/Gennevilliers), le <strong>tramway T1</strong> en correspondance directe. Quartier en <strong>mutation urbaine</strong> depuis les années 2000."
        ],
        "hist_title": "2008 : extension nord-ouest et tramway T1",
        "hist": [
            "La station est <strong>inaugurée le 14 juin 2008</strong> avec le <strong>prolongement de la branche Asnières</strong> de la M13, de <strong>Gabriel Péri à Asnières - Gennevilliers - Les Courtilles</strong> (2 stations ajoutées : <strong>Les Agnettes</strong> et <strong>Asnières - Gennevilliers - Les Courtilles</strong>).",
            "Le prolongement constitue l'un des <strong>premiers chantiers du Grand Paris</strong>. Permet le <strong>désenclavement</strong> des quartiers nord d'Asnières et de Gennevilliers.",
            "<strong>Asnières-sur-Seine</strong> (~85 000 habitants) et <strong>Gennevilliers</strong> (~50 000 habitants) sont deux communes des <strong>Hauts-de-Seine</strong>. Quartier <strong>Les Courtilles</strong> en transformation avec de nouveaux logements et bureaux."
        ],
        "faq": [
            ("Quelles lignes desservent Asnières - Gennevilliers - Les Courtilles ?", "<strong>M13</strong> (terminus branche Asnières) + <strong>tramway T1</strong>. Bus 138, 175, 235, 304, 366, 378."),
            ("Quand a-t-elle ouvert ?", "Le <strong>14 juin 2008</strong>."),
            ("Pour Saint-Lazare ?", "<strong>M13 directe</strong> (~18 min)."),
            ("Pour Châtelet ?", "<strong>M13 → Saint-Lazare + M14</strong> (~22 min)."),
            ("Pour Asnières centre ?", "Bus ou tramway T1."),
            ("La station est-elle accessible PMR ?", "<strong>Oui</strong>. Station moderne (2008).")
        ],
        "tips": [
            "<strong>Tramway T1</strong> en correspondance directe.",
            "Quartier <strong>Les Courtilles</strong> en transformation.",
            "Pour <strong>Asnières centre</strong> : tramway T1 ou bus 175.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M13 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("🚇", "Extension 2008 et Grand Paris", "L'<strong>extension de 2008</strong>, qui ouvre cette station, est l'un des <strong>premiers chantiers de modernisation du Grand Paris</strong>. <strong>2 nouvelles stations</strong> ajoutées : <strong>Les Agnettes</strong> et <strong>Asnières - Gennevilliers - Les Courtilles</strong>. <strong>1,9 km de prolongement</strong>. Permet le <strong>désenclavement</strong> des quartiers nord d'<strong>Asnières-sur-Seine</strong> (~85 000 habitants) et de <strong>Gennevilliers</strong> (~50 000 habitants)."),
            ("🚊", "Tramway T1, ligne historique 1992", "Le <strong>tramway T1</strong>, en correspondance directe, est le <strong>premier tramway moderne d'Île-de-France</strong>. <strong>Inauguré le 6 juillet 1992</strong> entre <strong>Bobigny - Pablo Picasso</strong> et <strong>Saint-Denis</strong>. <strong>Prolongé progressivement</strong> à l'ouest jusqu'à Asnières - Gennevilliers - Les Courtilles (2012). <strong>~115 000 voyageurs/jour</strong> à son ouverture, <strong>~270 000 aujourd'hui</strong>.")
        ],
        "itin": [
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~18 min)", 18),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 22),
            ("Champs-Élysées", "champs-elysees-clemenceau", "M13", "M13 directe (~20 min)", 20),
            ("Les Agnettes", "les-agnettes", "M13", "M13 directe (1 station)", 2),
            ("Gabriel Péri", "gabriel-peri", "M13", "M13 directe (2 stations)", 4),
            ("La Défense", "la-defense", "M13 + M1", "M13 → Champs-Élysées + M1", 25)
        ]
    },
    "les-agnettes": {
        "addr": "Avenue des Grésillons, 92230 Gennevilliers", "arr": "Gennevilliers (92)",
        "seo": "Station Les Agnettes (M13) à Gennevilliers (92). Quartier en transformation. Extension 2008 de la branche Asnières.",
        "tagline": "M13 — Gennevilliers, extension 2008",
        "hero_desc": "Station <strong>Les Agnettes</strong> à <strong>Gennevilliers</strong> (Hauts-de-Seine, 92). Desservie par la <strong>M13</strong>, ouverte le <strong>14 juin 2008</strong> avec l'<strong>extension de la branche Asnières</strong>.",
        "intros": [
            "La station <strong>Les Agnettes</strong> est implantée à <strong>Gennevilliers</strong> (Hauts-de-Seine, 92). Elle est desservie par la <strong>M13</strong>, entre <strong>Asnières - Gennevilliers - Les Courtilles</strong> (1 station, terminus) et <strong>Gabriel Péri</strong> (1 station). Bus 138, 175, 304, 540.",
            "Ouverte le <strong>14 juin 2008</strong> avec le <strong>prolongement de la branche Asnières</strong> de la M13.",
            "Quartier en <strong>transformation urbaine</strong>. <strong>Gennevilliers</strong> (~50 000 habitants) est l'une des communes des <strong>Hauts-de-Seine</strong>."
        ],
        "hist_title": "2008 : extension Asnières et Gennevilliers",
        "hist": [
            "La station Les Agnettes est <strong>inaugurée le 14 juin 2008</strong> avec le <strong>prolongement de la branche Asnières</strong> de la M13.",
            "Le nom <strong>Les Agnettes</strong> rappelle le <strong>quartier des Agnettes</strong> à Gennevilliers. Quartier en <strong>transformation urbaine</strong> depuis les années 2000.",
            "<strong>Gennevilliers</strong> (~50 000 habitants), ancienne commune <strong>industrielle</strong> des <strong>Hauts-de-Seine</strong>. Connue pour son <strong>port industriel sur la Seine</strong>, l'un des principaux ports fluviaux d'Île-de-France."
        ],
        "faq": [
            ("Quelle ligne dessert Les Agnettes ?", "Uniquement la <strong>M13</strong>. Bus 138, 175, 304, 540."),
            ("Quand a-t-elle ouvert ?", "Le <strong>14 juin 2008</strong>."),
            ("Pour le terminus Asnières - Gennevilliers ?", "<strong>M13 directe</strong> (1 station, terminus)."),
            ("Pour Saint-Lazare ?", "<strong>M13 directe</strong> (~16 min)."),
            ("Pour Gennevilliers centre ?", "Bus ou <strong>M13 → Gabriel Péri</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Oui</strong>. Station moderne (2008).")
        ],
        "tips": [
            "Station moderne <strong>2008</strong>, accessibilité PMR.",
            "Quartier en <strong>transformation urbaine</strong>.",
            "Pour <strong>terminus Asnières - Gennevilliers</strong> : <strong>M13 directe</strong>.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M13 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("🚇", "Extension Asnières 2008", "L'<strong>extension de 2008</strong> est l'un des premiers grands chantiers de <strong>modernisation du métro</strong> autour de Paris. <strong>1,9 km</strong>, <strong>2 nouvelles stations</strong> (Les Agnettes + Asnières - Gennevilliers - Les Courtilles). <strong>~180 millions d'euros</strong>. Permet le <strong>désenclavement</strong> du nord des Hauts-de-Seine."),
            ("⚓", "Port de Gennevilliers", "Le <strong>port de Gennevilliers</strong>, à proximité, est l'un des <strong>plus importants ports fluviaux d'Île-de-France</strong> et le <strong>premier port fluvial intérieur de France</strong>. <strong>400 hectares</strong>, <strong>~3 millions de tonnes</strong> de marchandises par an. Construit dans les années 1930.")
        ],
        "itin": [
            ("Asnières - Gennevilliers - Les Courtilles", "asnieres-gennevilliers-les-courtilles", "M13", "M13 directe (1 station, terminus)", 2),
            ("Gabriel Péri", "gabriel-peri", "M13", "M13 directe (1 station)", 2),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~16 min)", 16),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 20),
            ("Champs-Élysées", "champs-elysees-clemenceau", "M13", "M13 directe (~18 min)", 18),
            ("La Défense", "la-defense", "M13 + M1", "Via Champs-Élysées + M1", 22)
        ]
    },
    "gabriel-peri": {
        "addr": "Avenue Gabriel-Péri, 92600 Asnières-sur-Seine", "arr": "Asnières-sur-Seine (92)",
        "seo": "Station Gabriel Péri (M13) à Asnières-sur-Seine (92). Hommage à Gabriel Péri (1902-1941), journaliste et homme politique français.",
        "tagline": "M13 — Gabriel Péri, journaliste et homme politique",
        "hero_desc": "Station <strong>Gabriel Péri</strong> à <strong>Asnières-sur-Seine</strong> (Hauts-de-Seine, 92). Desservie par la <strong>M13</strong>, ouverte le <strong>9 mai 1980</strong>. Hommage à <strong>Gabriel Péri</strong> (<strong>1902-1941</strong>), <strong>journaliste et homme politique français</strong>.",
        "intros": [
            "La station <strong>Gabriel Péri</strong> est implantée à <strong>Asnières-sur-Seine</strong> (Hauts-de-Seine, 92). Elle est desservie par la <strong>M13</strong>, entre <strong>Les Agnettes</strong> (1 station) et <strong>Mairie de Clichy</strong> (1 station). Bus 138, 175, 235.",
            "Ouverte le <strong>9 mai 1980</strong> avec le <strong>prolongement de la M13</strong> de <strong>Carrefour Pleyel à Gabriel Péri</strong> (anciennement nommée <strong>« Gabriel Péri - Asnières - Gennevilliers »</strong>).",
            "Le nom <strong>Gabriel Péri</strong> rend hommage à <strong>Gabriel Péri</strong> (<strong>1902-1941</strong>), <strong>journaliste et homme politique français</strong>. <strong>Député communiste</strong> de l'Allier, journaliste à <em>L'Humanité</em>."
        ],
        "hist_title": "1980 : extension M13 et hommage",
        "hist": [
            "La station Gabriel Péri est <strong>inaugurée le 9 mai 1980</strong> avec le <strong>prolongement de la M13</strong> de <strong>Carrefour Pleyel à Gabriel Péri</strong> (côté branche Asnières).",
            "Le nom <strong>Gabriel Péri</strong> rend hommage à <strong>Gabriel Péri</strong> (<strong>9 février 1902 - 15 décembre 1941</strong>), <strong>journaliste et homme politique français</strong>. <strong>Député communiste</strong> de l'Allier, <strong>journaliste à L'Humanité</strong>.",
            "Le quartier autour de la station est résidentiel et commerçant. <strong>Asnières-sur-Seine</strong> (~85 000 habitants) est l'une des communes les plus dynamiques des <strong>Hauts-de-Seine</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Gabriel Péri ?", "Uniquement la <strong>M13</strong>. Bus 138, 175, 235."),
            ("Qui est Gabriel Péri ?", "<strong>Gabriel Péri</strong> (1902-1941), <strong>journaliste à L'Humanité</strong> et <strong>député communiste</strong> de l'Allier."),
            ("Quand a-t-elle ouvert ?", "Le <strong>9 mai 1980</strong>."),
            ("Pour Asnières centre ?", "<strong>~10 min à pied</strong>."),
            ("Pour Saint-Lazare ?", "<strong>M13 directe</strong> (~14 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Asnières-sur-Seine</strong> centre à 10 min à pied.",
            "Quartier résidentiel et commerçant.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M13 directe</strong>.",
            "Pour <strong>terminus Asnières</strong> : <strong>M13 directe</strong> (2 stations).",
            "Zone tarifaire <strong>3</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("📰", "Gabriel Péri, journaliste à L'Humanité", "<strong>Gabriel Péri</strong> (1902-1941), <strong>journaliste et homme politique français</strong>. <strong>Député communiste</strong> de l'Allier élu en 1932. <strong>Journaliste à L'Humanité</strong>, spécialiste de <strong>politique étrangère</strong>. Couvre la <strong>guerre d'Espagne</strong> et les <strong>relations internationales</strong> dans les années 1930. Auteur d'une <strong>lettre célèbre</strong> avant sa fin : <em>« Je ne regrette rien… je crois en effet à ces lendemains qui chantent »</em> — formule devenue iconique."),
            ("🏘️", "Asnières-sur-Seine, ville du 92", "<strong>Asnières-sur-Seine</strong>, ~85 000 habitants, est l'une des communes les plus dynamiques des <strong>Hauts-de-Seine</strong>. Bordée par la <strong>Seine</strong>. Ancienne commune <strong>résidentielle bourgeoise</strong>, elle conserve de nombreuses <strong>villas du XIXe siècle</strong>. <strong>Cimetière des chiens d'Asnières</strong> (1899), l'un des premiers cimetières animaliers au monde.")
        ],
        "itin": [
            ("Asnières centre", "gabriel-peri", "à pied", "10 min à pied", 10),
            ("Les Agnettes", "les-agnettes", "M13", "M13 directe (1 station)", 2),
            ("Mairie de Clichy", "mairie-de-clichy", "M13", "M13 directe (1 station)", 2),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~14 min)", 14),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 18),
            ("Champs-Élysées", "champs-elysees-clemenceau", "M13", "M13 directe (~16 min)", 16)
        ]
    },
    "mairie-de-clichy": {
        "addr": "Place du 4-Septembre, 92110 Clichy", "arr": "Clichy (92)",
        "seo": "Station Mairie de Clichy (M13) à Clichy (92). Mairie de Clichy-la-Garenne. Quartier dynamique des Hauts-de-Seine.",
        "tagline": "M13 — Mairie de Clichy-la-Garenne",
        "hero_desc": "Station <strong>Mairie de Clichy</strong> à <strong>Clichy</strong> (Hauts-de-Seine, 92). Desservie par la <strong>M13</strong>, ouverte le <strong>3 juin 1980</strong>. À la sortie : la <strong>mairie de Clichy-la-Garenne</strong>.",
        "intros": [
            "La station <strong>Mairie de Clichy</strong> est implantée à <strong>Clichy</strong> (Hauts-de-Seine, 92), en face de la <strong>mairie</strong>. Elle est desservie par la <strong>M13</strong>, entre <strong>Gabriel Péri</strong> (1 station) et <strong>La Fourche</strong> (1 station, côté Asnières) / <strong>Brochant</strong> (1 station, côté Pleyel). Bus 54, 74, 138, 174, 274.",
            "Ouverte le <strong>3 juin 1980</strong> avec le <strong>prolongement de la M13</strong> de <strong>Porte de Clichy à Mairie de Clichy</strong>.",
            "À la sortie : la <strong>mairie de Clichy-la-Garenne</strong>, hôtel de ville construit en <strong>1869</strong>. <strong>Clichy</strong> (~62 000 habitants), commune des <strong>Hauts-de-Seine</strong>."
        ],
        "hist_title": "1980 : prolongement et mairie 1869",
        "hist": [
            "La station Mairie de Clichy est <strong>inaugurée le 3 juin 1980</strong> avec le <strong>prolongement de la M13</strong> de <strong>Porte de Clichy à Mairie de Clichy</strong>.",
            "La <strong>mairie de Clichy-la-Garenne</strong>, en face de la station, est un <strong>édifice du Second Empire</strong> construit en <strong>1869</strong> par l'architecte <strong>Henri Salvador</strong>. <strong>Style néo-Renaissance</strong>. <strong>Inscrite aux monuments historiques en 1996</strong>.",
            "<strong>Clichy</strong> (~62 000 habitants), commune des <strong>Hauts-de-Seine</strong> à la limite nord-ouest de Paris. Ancienne commune <strong>industrielle</strong> (Wonder, Citroën, Renault), elle se transforme depuis les années 1990 en <strong>commune résidentielle et de bureaux</strong>. Connue pour ses <strong>« nuits chaudes de Clichy »</strong> chantées par Maurice Chevalier."
        ],
        "faq": [
            ("Quelle ligne dessert Mairie de Clichy ?", "Uniquement la <strong>M13</strong>. Bus 54, 74, 138, 174, 274."),
            ("Quand a-t-elle ouvert ?", "Le <strong>3 juin 1980</strong>."),
            ("Pour la mairie de Clichy ?", "<strong>Sortie directe</strong>. Édifice néo-Renaissance de 1869."),
            ("Pour Saint-Lazare ?", "<strong>M13 directe</strong> (~12 min)."),
            ("Pour Châtelet ?", "<strong>M13 + M14</strong> via Saint-Lazare (~16 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Mairie de Clichy</strong> à la sortie : édifice néo-Renaissance 1869, monument historique.",
            "<strong>Clichy centre commerçant</strong> à proximité.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M13 directe</strong>.",
            "Pour <strong>Place de Clichy</strong> (hub M2+M13) : <strong>M13 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("🏛️", "Mairie de Clichy-la-Garenne (1869)", "La <strong>mairie de Clichy-la-Garenne</strong>, en face de la station, est un <strong>édifice du Second Empire</strong> construit en <strong>1869</strong> par l'architecte <strong>Henri Salvador</strong>. <strong>Style néo-Renaissance</strong> avec <strong>tour-horloge</strong>. <strong>Inscrite aux monuments historiques en 1996</strong>. Témoignage de l'<strong>essor des communes périphériques</strong> de Paris au XIXe siècle."),
            ("🏘️", "Clichy, ancienne ville industrielle", "<strong>Clichy</strong>, ~62 000 habitants, est l'une des communes les plus dynamiques des <strong>Hauts-de-Seine</strong>. Ancienne commune <strong>industrielle</strong> (<strong>usines Wonder, Citroën, Renault</strong>), elle a connu une <strong>transformation profonde</strong> depuis les années 1990. Aujourd'hui mix de <strong>quartiers résidentiels, bureaux et commerces</strong>. Célèbre pour les <strong>« nuits chaudes de Clichy »</strong> chantées par Maurice Chevalier.")
        ],
        "itin": [
            ("Mairie de Clichy", "mairie-de-clichy", "à pied", "Sortie directe", 1),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~12 min)", 12),
            ("Place de Clichy", "place-de-clichy", "M13", "M13 directe (~6 min)", 6),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 16),
            ("Champs-Élysées", "champs-elysees-clemenceau", "M13", "M13 directe (~14 min)", 14),
            ("Gabriel Péri", "gabriel-peri", "M13", "M13 directe (1 station)", 2)
        ]
    },
    "brochant": {
        "addr": "Avenue de Clichy, 75017 Paris", "arr": "17e arrondissement (Paris)",
        "seo": "Station Brochant (M13) avenue de Clichy dans le 17e. Hommage au géologue André Brochant de Villiers. Quartier Batignolles.",
        "tagline": "M13 — Brochant, géologue du XIXe siècle",
        "hero_desc": "Station <strong>Brochant</strong> sur l'<strong>avenue de Clichy</strong> dans le <strong>17e arrondissement</strong>. Desservie par la <strong>M13</strong>, ouverte le <strong>20 janvier 1912</strong>. Hommage à <strong>André Brochant de Villiers</strong> (<strong>1772-1840</strong>), <strong>géologue et minéralogiste français</strong>.",
        "intros": [
            "La station <strong>Brochant</strong> est implantée sur l'<strong>avenue de Clichy</strong> dans le <strong>17e arrondissement</strong>. Elle est desservie par la <strong>M13</strong>, entre <strong>Porte de Clichy</strong> (1 station, côté Pleyel) et <strong>La Fourche</strong> (1 station). Bus 31, 54, 74.",
            "Ouverte le <strong>20 janvier 1912</strong> sur la <strong>ligne B du Nord-Sud</strong>.",
            "Le nom <strong>Brochant</strong> rend hommage à <strong>André Jean François Marie Brochant de Villiers</strong> (<strong>1772-1840</strong>), <strong>géologue et minéralogiste français</strong>. <strong>Membre de l'Académie des sciences</strong>. Quartier <strong>Batignolles</strong> du <strong>17e</strong>."
        ],
        "hist_title": "1912 : Nord-Sud et géologue",
        "hist": [
            "La station Brochant est <strong>inaugurée le 20 janvier 1912</strong> sur la <strong>ligne B du Nord-Sud</strong> (compagnie privée fusionnée avec la CMP en 1930, ligne devenue M13 en 1942).",
            "Le nom <strong>Brochant</strong> rend hommage à <strong>André Jean François Marie Brochant de Villiers</strong> (<strong>10 août 1772 - 16 mai 1840</strong>), <strong>géologue et minéralogiste français</strong>. <strong>Membre de l'Académie des sciences</strong> en 1816. <strong>Professeur à l'École des mines</strong>.",
            "Le quartier autour de la station fait partie des <strong>Batignolles</strong>, ancien village rattaché à Paris en <strong>1860</strong>. Quartier en pleine <strong>transformation urbaine</strong> avec le projet <strong>Clichy-Batignolles</strong> (parc Martin-Luther-King, Cité judiciaire de Renzo Piano)."
        ],
        "faq": [
            ("Quelle ligne dessert Brochant ?", "Uniquement la <strong>M13</strong>. Bus 31, 54, 74."),
            ("Qui est Brochant de Villiers ?", "<strong>André Brochant de Villiers</strong> (1772-1840), <strong>géologue et minéralogiste</strong>. Membre de l'Académie des sciences."),
            ("Quand a-t-elle ouvert ?", "Le <strong>20 janvier 1912</strong>."),
            ("Pour le parc Martin-Luther-King ?", "<strong>~10 min à pied</strong>."),
            ("Pour Saint-Lazare ?", "<strong>M13 directe</strong> (~8 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Parc Martin-Luther-King</strong> (Clichy-Batignolles) à 10 min à pied.",
            "<strong>Cité judiciaire de Paris</strong> (Renzo Piano, 2018) à 10 min.",
            "Quartier <strong>Batignolles</strong> en transformation.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M13 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🔬", "Brochant de Villiers, géologue académicien", "<strong>André Brochant de Villiers</strong> (1772-1840), <strong>géologue et minéralogiste français</strong>. <strong>Membre de l'Académie des sciences</strong> en 1816. <strong>Professeur à l'École des mines</strong>. Auteur de la <strong>première carte géologique de France</strong> (avec Élie de Beaumont et Dufrénoy, 1841). Pionnier de la <strong>géologie française</strong>."),
            ("🌳", "Quartier Clichy-Batignolles en transformation", "Le <strong>quartier Clichy-Batignolles</strong>, à 10 min à pied, est l'un des <strong>plus grands projets d'urbanisme parisien</strong> depuis les années 2010. <strong>Parc Martin-Luther-King</strong> (10 ha, 2014), <strong>Cité judiciaire de Renzo Piano</strong> (tour de 160 m, 2018), <strong>logements et bureaux</strong>. Le projet a permis de <strong>désenclaver le nord du 17e</strong>.")
        ],
        "itin": [
            ("Parc Martin-Luther-King", "porte-de-clichy", "M13 + à pied", "À pied (10 min)", 10),
            ("Cité judiciaire", "porte-de-clichy", "M13", "M13 + à pied", 10),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~8 min)", 8),
            ("Place de Clichy", "place-de-clichy", "M13", "M13 directe (3 stations)", 6),
            ("La Fourche", "la-fourche", "M13", "M13 directe (1 station)", 2),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 12)
        ]
    },
    "la-fourche": {
        "addr": "Avenue de Saint-Ouen, 75017 Paris", "arr": "17e arrondissement (Paris)",
        "seo": "Station La Fourche (M13) avenue de Saint-Ouen dans le 17e. Point de fourche unique de la M13 (branches Asnières et Saint-Denis).",
        "tagline": "M13 — point de fourche, séparation des 2 branches",
        "hero_desc": "Station <strong>La Fourche</strong> sur l'<strong>avenue de Saint-Ouen</strong> dans le <strong>17e arrondissement</strong>. Desservie par la <strong>M13</strong>, ouverte le <strong>26 février 1911</strong>. <strong>Point unique de la fourche M13</strong> où la ligne se sépare en <strong>2 branches</strong> : <strong>Asnières-Gennevilliers</strong> (ouest) et <strong>Saint-Denis</strong> (nord).",
        "intros": [
            "La station <strong>La Fourche</strong> est implantée sur l'<strong>avenue de Saint-Ouen</strong> dans le <strong>17e arrondissement</strong>. Elle est desservie par la <strong>M13</strong>, entre <strong>Guy Môquet</strong> (1 station, côté sud) et <strong>Brochant / Porte de Saint-Ouen</strong> (1 station selon branche). Bus 31, 54, 66, 74.",
            "Ouverte le <strong>26 février 1911</strong> sur la <strong>ligne B du Nord-Sud</strong>. <strong>Point unique de fourche</strong> de la M13.",
            "À cette station, la M13 se <strong>scinde en 2 branches</strong> : la <strong>branche Asnières-Gennevilliers</strong> (vers l'ouest, terminus Asnières - Gennevilliers - Les Courtilles) et la <strong>branche Saint-Denis</strong> (vers le nord-est, terminus Saint-Denis - Université). Les rames alternent automatiquement entre les 2 branches."
        ],
        "hist_title": "1911 : Nord-Sud et point de fourche unique",
        "hist": [
            "La station La Fourche est <strong>inaugurée le 26 février 1911</strong> sur la <strong>ligne B du Nord-Sud</strong> (compagnie privée fusionnée avec la CMP en 1930, ligne devenue M13 en 1942).",
            "Le nom <strong>La Fourche</strong> fait référence à la <strong>configuration unique</strong> de la station : elle est le <strong>point de fourche de la M13</strong>, où la ligne se sépare en <strong>2 branches distinctes</strong>. <strong>Particularité architecturale</strong> : la station a une <strong>plateforme inférieure</strong> pour les trains de la branche Saint-Denis et une <strong>plateforme supérieure</strong> pour la branche Asnières-Gennevilliers.",
            "<strong>Système d'alternance automatique</strong> : les rames alternent entre les 2 branches selon la fréquentation. Cette configuration de <strong>fourche M13</strong> est <strong>unique sur le réseau métro parisien</strong> (seule autre fourche : ligne 7 entre Maison Blanche et ses 2 terminus sud, et brièvement ligne 7bis)."
        ],
        "faq": [
            ("Quelle ligne dessert La Fourche ?", "Uniquement la <strong>M13</strong>. Bus 31, 54, 66, 74."),
            ("Qu'est-ce que la fourche M13 ?", "Le <strong>point unique de séparation</strong> où la M13 se scinde en <strong>2 branches</strong> : <strong>Asnières-Gennevilliers</strong> (ouest) et <strong>Saint-Denis</strong> (nord-est)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>26 février 1911</strong>."),
            ("Comment fonctionne l'alternance ?", "Les rames <strong>alternent automatiquement</strong> entre les 2 branches. Vérifiez la destination du train sur les panneaux d'affichage."),
            ("Pour Saint-Lazare ?", "<strong>M13 directe</strong> (~8 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Point de fourche M13</strong> : <strong>vérifiez la destination</strong> du train.",
            "Vers <strong>Saint-Denis</strong> : trains marqués « Saint-Denis - Université ».",
            "Vers <strong>Asnières</strong> : trains marqués « Asnières - Gennevilliers - Les Courtilles ».",
            "Pour <strong>Saint-Lazare</strong> : <strong>M13 directe</strong> (les deux branches).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🚇", "Fourche M13, configuration unique", "La <strong>fourche M13</strong> à La Fourche est <strong>unique dans le métro parisien</strong> par son ampleur. La ligne se <strong>scinde en 2 branches</strong> : <strong>Asnières-Gennevilliers</strong> (ouest) et <strong>Saint-Denis</strong> (nord-est). Les <strong>rames alternent automatiquement</strong> entre les 2 branches selon le service. Cela permet de <strong>desservir 2 axes simultanément</strong> mais réduit la <strong>fréquence sur chaque branche</strong>."),
            ("🏛️", "Architecture à 2 niveaux", "La station <strong>La Fourche</strong> présente une <strong>architecture particulière à 2 niveaux</strong> : une <strong>plateforme supérieure</strong> pour la branche Asnières-Gennevilliers et une <strong>plateforme inférieure</strong> pour la branche Saint-Denis. Cette configuration permet de gérer le <strong>croisement complexe des voies</strong> sans interruption.")
        ],
        "itin": [
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~8 min)", 8),
            ("Place de Clichy", "place-de-clichy", "M13", "M13 directe (2 stations)", 4),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 12),
            ("Champs-Élysées", "champs-elysees-clemenceau", "M13", "M13 directe (~10 min)", 10),
            ("Mairie de Saint-Ouen", "mairie-de-saint-ouen", "M13", "M13 branche Saint-Denis (3 stations)", 6),
            ("La Défense", "la-defense", "M13 + M1", "Via Champs-Élysées + M1", 18)
        ]
    },
    "liege": {
        "addr": "Rue d'Amsterdam, 75009 Paris", "arr": "9e arrondissement (Paris)",
        "seo": "Station Liège (M13) rue d'Amsterdam dans le 9e. Anciennement nommée Berlin jusqu'en 1914. Particularité historique : fermée la nuit jusqu'en 2006.",
        "tagline": "M13 — Liège, ancienne « Berlin » (1914)",
        "hero_desc": "Station <strong>Liège</strong> sur la <strong>rue d'Amsterdam</strong> dans le <strong>9e arrondissement</strong>. Desservie par la <strong>M13</strong>, ouverte le <strong>26 février 1911</strong>. Initialement nommée <strong>« Berlin »</strong> (1911-1914), renommée <strong>« Liège »</strong> en <strong>1914</strong> après la <strong>Première Guerre mondiale</strong>.",
        "intros": [
            "La station <strong>Liège</strong> est implantée sur la <strong>rue d'Amsterdam</strong> dans le <strong>9e arrondissement</strong>. Elle est desservie par la <strong>M13</strong>, entre <strong>Place de Clichy</strong> (1 station) et <strong>Saint-Lazare</strong> (1 station). Bus 21, 26, 68.",
            "Ouverte le <strong>26 février 1911</strong> sous le nom <strong>« Berlin »</strong>, sur la <strong>ligne B du Nord-Sud</strong>. <strong>Renommée « Liège »</strong> en <strong>octobre 1914</strong>, peu après le <strong>début de la Première Guerre mondiale</strong>.",
            "<strong>Particularité historique</strong> : la station est <strong>restée fermée la nuit et les dimanches</strong> de <strong>1939 à 2006</strong>, en raison de sa <strong>proximité avec Saint-Lazare</strong>. Désormais ouverte normalement."
        ],
        "hist_title": "1911-1914 : Berlin renommée Liège",
        "hist": [
            "La station est <strong>inaugurée le 26 février 1911</strong> sous le nom <strong>« Berlin »</strong> sur la <strong>ligne B du Nord-Sud</strong> (compagnie privée fusionnée avec la CMP en 1930, ligne devenue M13 en 1942). Le nom rappelait alors la <strong>rue de Berlin</strong> à proximité, située dans le <strong>quartier de l'Europe</strong> (rues nommées d'après les capitales européennes).",
            "<strong>Renommée « Liège »</strong> en <strong>octobre 1914</strong>, peu après le <strong>début de la Première Guerre mondiale</strong>. Le nom rend hommage à la <strong>ville belge de Liège</strong>, qui résista héroïquement à l'<strong>invasion allemande</strong> au début du conflit (août 1914). La <strong>rue de Berlin</strong> fut également renommée <strong>rue de Liège</strong>.",
            "<strong>Particularité</strong> : la station est <strong>fermée la nuit et les dimanches</strong> à partir de <strong>1939</strong>, en raison de sa <strong>très grande proximité avec la station Saint-Lazare</strong> (300 m seulement). Elle <strong>rouvre normalement le 6 décembre 2006</strong> après modernisation."
        ],
        "faq": [
            ("Quelle ligne dessert Liège ?", "Uniquement la <strong>M13</strong>. Bus 21, 26, 68."),
            ("Quel était l'ancien nom ?", "<strong>« Berlin »</strong> (1911-1914), renommée après le début de la Première Guerre mondiale."),
            ("Pourquoi renommée en 1914 ?", "Hommage à la <strong>ville belge de Liège</strong> qui résista à l'<strong>invasion allemande</strong> en <strong>août 1914</strong>."),
            ("Particularité historique ?", "<strong>Fermée la nuit et dimanches de 1939 à 2006</strong> (proximité avec Saint-Lazare). <strong>Rouverte le 6 décembre 2006</strong>."),
            ("Pour Saint-Lazare ?", "<strong>M13 directe</strong> (1 station) ou ~3 min à pied."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Quartier de l'Europe</strong> (9e/8e) : rues nommées d'après les capitales.",
            "<strong>Gare Saint-Lazare</strong> à 5 min à pied.",
            "Pour <strong>Galeries Lafayette</strong> : <strong>M13 → Saint-Lazare + M9</strong>.",
            "Pour <strong>Châtelet</strong> : <strong>M13 + M14</strong> via Saint-Lazare.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🇧🇪", "Liège, ville belge héroïque (août 1914)", "La <strong>ville de Liège</strong>, à laquelle la station rend hommage, fut le <strong>premier obstacle majeur</strong> à l'<strong>invasion allemande</strong> de la Belgique en <strong>août 1914</strong>. Les <strong>forts de Liège</strong> résistèrent <strong>12 jours</strong> (4-16 août 1914) au siège allemand, retardant l'<strong>offensive du plan Schlieffen</strong> et permettant aux Alliés français et britanniques de se préparer. La <strong>défense de Liège</strong> devint un <strong>symbole de la résistance</strong>. Le <strong>roi Albert Ier de Belgique</strong> y fut décoré."),
            ("🚇", "Station fermée 67 ans la nuit (1939-2006)", "<strong>Particularité historique</strong> : la station Liège a été <strong>fermée la nuit et le dimanche</strong> pendant <strong>67 ans</strong>, de <strong>1939 à 2006</strong>. Cette mesure exceptionnelle s'explique par sa <strong>très grande proximité avec Saint-Lazare</strong> (300 m). <strong>Réouverture normale le 6 décembre 2006</strong> après modernisation. Aujourd'hui, la station fonctionne aux horaires standards.")
        ],
        "itin": [
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (1 station)", 2),
            ("Galeries Lafayette", "havre-caumartin", "M13 + M9", "M13 → Saint-Lazare + M9", 6),
            ("Place de Clichy", "place-de-clichy", "M13", "M13 directe (1 station)", 2),
            ("Opéra Garnier", "opera", "M13 + M3", "M13 → Saint-Lazare + M3", 8),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 8),
            ("Champs-Élysées", "champs-elysees-clemenceau", "M13", "M13 directe (~6 min)", 6)
        ]
    },
    "miromesnil": {
        "addr": "Rue de Miromesnil, 75008 Paris", "arr": "8e arrondissement (Paris)",
        "seo": "Station Miromesnil (M9+M13) rue de Miromesnil dans le 8e. Hub M9 et M13. Musée Jacquemart-André à proximité.",
        "tagline": "M9 + M13 — hub 8e, Jacquemart-André",
        "hero_desc": "Station <strong>Miromesnil</strong>, hub <strong>M9 + M13</strong>, sur la <strong>rue de Miromesnil</strong> dans le <strong>8e arrondissement</strong>. Quais <strong>M9</strong> ouverts le <strong>27 mai 1923</strong>, quais <strong>M13</strong> le <strong>18 février 1973</strong>. À proximité du <strong>musée Jacquemart-André</strong>.",
        "intros": [
            "La station <strong>Miromesnil</strong> est implantée sur la <strong>rue de Miromesnil</strong> dans le <strong>8e arrondissement</strong>. Elle est desservie par les <strong>lignes 9 et 13</strong> du métro parisien, formant un <strong>hub de correspondance</strong>. Bus 22, 28, 32, 43, 80, 84, 93, 94.",
            "Quais <strong>ligne 9</strong> ouverts le <strong>27 mai 1923</strong> avec le tronçon Trocadéro ↔ Saint-Augustin. Quais <strong>ligne 13</strong> ouverts le <strong>18 février 1973</strong> avec le prolongement de la M13 vers le sud.",
            "Le nom <strong>Miromesnil</strong> vient de la <strong>rue de Miromesnil</strong>, qui rend hommage à <strong>Armand Thomas Hue, marquis de Miromesnil</strong> (<strong>1723-1796</strong>), <strong>magistrat et ministre français</strong>. <strong>Garde des Sceaux</strong> sous Louis XVI (1774-1787). À proximité : le <strong>musée Jacquemart-André</strong>."
        ],
        "hist_title": "1923-1973 : hub M9/M13 et marquis de Miromesnil",
        "hist": [
            "Les quais <strong>ligne 9</strong> sont <strong>inaugurés le 27 mai 1923</strong> avec le tronçon <strong>Trocadéro ↔ Saint-Augustin</strong>. Les quais <strong>ligne 13</strong> ouvrent le <strong>18 février 1973</strong> avec le prolongement de la M13.",
            "Le nom <strong>Miromesnil</strong> rend hommage à <strong>Armand Thomas Hue, marquis de Miromesnil</strong> (<strong>27 août 1723 - 6 juillet 1796</strong>), <strong>magistrat et homme d'État français</strong>. <strong>Premier président du Parlement de Normandie</strong>, puis <strong>Garde des Sceaux</strong> sous <strong>Louis XVI</strong> (<strong>1774-1787</strong>). Tenta des <strong>réformes judiciaires</strong>.",
            "À proximité : le <strong>musée Jacquemart-André</strong> (boulevard Haussmann), installé dans un <strong>hôtel particulier du Second Empire</strong>. Collection privée d'<strong>art italien Renaissance</strong> et de <strong>peintures françaises du XVIIIe</strong> léguée par <strong>Édouard André</strong> et sa femme <strong>Nélie Jacquemart</strong> à l'<strong>Institut de France</strong>."
        ],
        "faq": [
            ("Quelles lignes desservent Miromesnil ?", "<strong>M9</strong> et <strong>M13</strong>. Hub du 8e. Bus 22, 28, 32, 43, 80, 84, 93, 94."),
            ("Qui est Miromesnil ?", "<strong>Armand Thomas Hue, marquis de Miromesnil</strong> (1723-1796), <strong>Garde des Sceaux</strong> sous Louis XVI (1774-1787)."),
            ("Quand a-t-elle ouvert ?", "Quais M9 : <strong>27 mai 1923</strong>. Quais M13 : <strong>18 février 1973</strong>."),
            ("Pour le musée Jacquemart-André ?", "<strong>~5 min à pied</strong> via la rue de Miromesnil."),
            ("Pour Saint-Lazare ?", "<strong>M13 directe</strong> (1 station, ~3 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Musée Jacquemart-André</strong> à 5 min : collection d'art italien Renaissance.",
            "Hub <strong>M9 + M13</strong> du 8e.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M13 directe</strong> (1 station).",
            "Pour <strong>Trocadéro</strong> et <strong>Tour Eiffel</strong> : <strong>M9 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Musée Jacquemart-André", "Le <strong>musée Jacquemart-André</strong>, à 5 min à pied (158 boulevard Haussmann), est l'un des <strong>plus beaux musées d'hôtel particulier de Paris</strong>. Installé dans la <strong>demeure du Second Empire</strong> d'<strong>Édouard André</strong> (1833-1894) et sa femme <strong>Nélie Jacquemart</strong>. Collection privée d'<strong>art italien Renaissance</strong> (Botticelli, Mantegna, Uccello), <strong>peintures françaises du XVIIIe</strong> (Boucher, Watteau, Fragonard), <strong>peintures flamandes</strong> (Rembrandt, Van Dyck). Léguée à l'<strong>Institut de France</strong>."),
            ("⚖️", "Miromesnil, Garde des Sceaux de Louis XVI", "<strong>Armand Thomas Hue, marquis de Miromesnil</strong> (1723-1796), <strong>magistrat et homme d'État français</strong>. <strong>Premier président du Parlement de Normandie</strong> puis <strong>Garde des Sceaux</strong> de <strong>Louis XVI</strong> de <strong>1774 à 1787</strong>. Tenta des <strong>réformes judiciaires</strong> dont la <strong>suppression de la torture</strong> (édit d'août 1780). Disgrace en 1787 dans le contexte de la <strong>crise pré-révolutionnaire</strong>.")
        ],
        "itin": [
            ("Musée Jacquemart-André", "miromesnil", "à pied", "Rue de Miromesnil (5 min)", 5),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (1 station)", 3),
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (~10 min)", 10),
            ("Champs-Élysées Clemenceau", "champs-elysees-clemenceau", "M13", "M13 directe (1 station)", 2),
            ("Galeries Lafayette", "chaussee-d-antin-la-fayette", "M9", "M9 directe (3 stations)", 6),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 8)
        ]
    },
    "saint-francois-xavier": {
        "addr": "Boulevard des Invalides, 75007 Paris", "arr": "7e arrondissement (Paris)",
        "seo": "Station Saint-François-Xavier (M13) boulevard des Invalides dans le 7e. Église Saint-François-Xavier (1874). Quartier 7e proche Invalides.",
        "tagline": "M13 — église Saint-François-Xavier (1874)",
        "hero_desc": "Station <strong>Saint-François-Xavier</strong> sur le <strong>boulevard des Invalides</strong> dans le <strong>7e arrondissement</strong>. Desservie par la <strong>M13</strong>, ouverte le <strong>18 février 1973</strong>. À proximité de l'<strong>église Saint-François-Xavier</strong> (1874).",
        "intros": [
            "La station <strong>Saint-François-Xavier</strong> est implantée sur le <strong>boulevard des Invalides</strong> dans le <strong>7e arrondissement</strong>. Elle est desservie par la <strong>M13</strong>, entre <strong>Varenne</strong> (1 station) et <strong>Duroc</strong> (1 station). Bus 28, 87, 92.",
            "Ouverte le <strong>18 février 1973</strong> avec le <strong>prolongement de la M13</strong> de <strong>Miromesnil à Saint-Augustin</strong>, puis vers le sud.",
            "À proximité : l'<strong>église Saint-François-Xavier</strong> (12 place du Président-Mithouard), édifice <strong>néo-Renaissance</strong> construit de <strong>1861 à 1874</strong>. Dédiée à <strong>saint François Xavier</strong> (1506-1552), <strong>missionnaire jésuite espagnol</strong>."
        ],
        "hist_title": "1973 : prolongement M13 et église néo-Renaissance",
        "hist": [
            "La station Saint-François-Xavier est <strong>inaugurée le 18 février 1973</strong> avec le <strong>prolongement de la M13</strong> de <strong>Miromesnil à Champs-Élysées - Clemenceau</strong>, puis vers le sud (Invalides, Duroc).",
            "L'<strong>église Saint-François-Xavier</strong>, à proximité (12 place du Président-Mithouard), est un <strong>édifice religieux néo-Renaissance</strong> construit de <strong>1861 à 1874</strong> par les architectes <strong>Joseph Uchard</strong> et <strong>Adrien Lusson</strong>. <strong>Façade néo-Renaissance</strong> avec dôme central.",
            "Dédiée à <strong>saint François Xavier</strong> (<strong>1506-1552</strong>), <strong>missionnaire jésuite espagnol</strong> et <strong>cofondateur de la Compagnie de Jésus</strong> avec Ignace de Loyola (1540). Surnommé <strong>« apôtre des Indes et du Japon »</strong> pour ses missions évangélisatrices."
        ],
        "faq": [
            ("Quelle ligne dessert Saint-François-Xavier ?", "Uniquement la <strong>M13</strong>. Bus 28, 87, 92."),
            ("Qu'est-ce que l'église Saint-François-Xavier ?", "<strong>Édifice religieux néo-Renaissance</strong> construit de <strong>1861 à 1874</strong> par Joseph Uchard et Adrien Lusson."),
            ("Quand a-t-elle ouvert ?", "Le <strong>18 février 1973</strong>."),
            ("Qui est saint François Xavier ?", "<strong>Missionnaire jésuite espagnol</strong> (1506-1552), cofondateur de la Compagnie de Jésus."),
            ("Pour les Invalides ?", "<strong>M13 directe</strong> vers Invalides (~5 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Église Saint-François-Xavier</strong> à proximité : édifice néo-Renaissance 1874.",
            "<strong>Hôtel des Invalides</strong> et <strong>tombeau de Napoléon</strong> à 10 min à pied.",
            "Pour <strong>Le Bon Marché</strong> : <strong>M13 → Duroc + M10</strong>.",
            "Pour <strong>Trocadéro</strong> et <strong>Tour Eiffel</strong> : <strong>M13 → Invalides + RER C</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⛪", "Église Saint-François-Xavier (1874)", "L'<strong>église Saint-François-Xavier</strong>, à proximité de la station (12 place du Président-Mithouard), est un <strong>édifice religieux néo-Renaissance</strong> construit de <strong>1861 à 1874</strong>. Architectes : <strong>Joseph Uchard</strong> et <strong>Adrien Lusson</strong>. <strong>Façade à colonnade corinthienne</strong> et <strong>dôme central</strong>. Style inspiré de la <strong>Renaissance italienne</strong>."),
            ("🌍", "Saint François Xavier, « apôtre des Indes »", "<strong>Saint François Xavier</strong> (1506-1552), <strong>missionnaire jésuite espagnol</strong>. <strong>Cofondateur de la Compagnie de Jésus</strong> avec Ignace de Loyola (1540). <strong>Mission en Inde</strong> (Goa, 1542), puis <strong>Asie du Sud-Est</strong>, <strong>Japon</strong> (1549). Mort en Chine en <strong>1552</strong>. <strong>Canonisé en 1622</strong>. Surnommé <strong>« apôtre des Indes et du Japon »</strong>.")
        ],
        "itin": [
            ("Église Saint-François-Xavier", "saint-francois-xavier", "à pied", "Place Président-Mithouard (2 min)", 2),
            ("Invalides et tombeau Napoléon", "invalides", "M13", "M13 directe (1 station)", 3),
            ("Duroc (hub M10+M13)", "duroc", "M13", "M13 directe (1 station)", 2),
            ("Le Bon Marché", "sevres-babylone", "M13 + M10", "M13 → Duroc + M10", 6),
            ("Montparnasse", "montparnasse-bienvenue", "M13", "M13 directe (~7 min)", 7),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 14)
        ]
    },
    "gaite": {
        "addr": "Rue de la Gaîté, 75014 Paris", "arr": "14e arrondissement (Paris)",
        "seo": "Station Gaîté (M13) rue de la Gaîté dans le 14e. Quartier des théâtres de Montparnasse. Théâtre Montparnasse, Bobino.",
        "tagline": "M13 — rue de la Gaîté, théâtres Montparnasse",
        "hero_desc": "Station <strong>Gaîté</strong> sur la <strong>rue de la Gaîté</strong> dans le <strong>14e arrondissement</strong>. Desservie par la <strong>M13</strong>, ouverte le <strong>21 janvier 1937</strong>. Cœur du <strong>quartier des théâtres de Montparnasse</strong> : <strong>Théâtre Montparnasse</strong>, <strong>Bobino</strong>, <strong>Théâtre de la Gaîté-Montparnasse</strong>.",
        "intros": [
            "La station <strong>Gaîté</strong> est implantée sur la <strong>rue de la Gaîté</strong> dans le <strong>14e arrondissement</strong>. Elle est desservie par la <strong>M13</strong>, entre <strong>Montparnasse - Bienvenüe</strong> (1 station) et <strong>Pernety</strong> (1 station). Bus 28, 58, 91.",
            "Ouverte le <strong>21 janvier 1937</strong> avec la <strong>ligne 14</strong> (<strong>ancienne</strong>, intégrée à la M13 en 1976).",
            "La <strong>rue de la Gaîté</strong>, qui donne son nom à la station, est l'un des <strong>hauts lieux du théâtre parisien</strong>. <strong>Théâtre Montparnasse</strong>, <strong>Bobino</strong>, <strong>Théâtre de la Gaîté-Montparnasse</strong>, <strong>Théâtre du Petit Montparnasse</strong>. Tradition de <strong>théâtre populaire</strong> depuis le XIXe siècle."
        ],
        "hist_title": "1937 : rue de la Gaîté et théâtres Montparnasse",
        "hist": [
            "La station Gaîté est <strong>inaugurée le 21 janvier 1937</strong> avec l'ancienne <strong>ligne 14</strong> (<strong>Bienvenüe ↔ Porte de Vanves</strong>), <strong>intégrée à la M13 en 1976</strong>.",
            "La <strong>rue de la Gaîté</strong>, longue de <strong>400 m</strong>, est l'un des <strong>hauts lieux du théâtre parisien</strong> depuis le <strong>XIXe siècle</strong>. Concentre plusieurs <strong>théâtres populaires</strong> : <strong>Théâtre Montparnasse</strong> (1851), <strong>Bobino</strong> (1873, mythique cabaret-théâtre), <strong>Théâtre de la Gaîté-Montparnasse</strong> (1868), <strong>Théâtre du Petit Montparnasse</strong>.",
            "<strong>Bobino</strong>, célèbre cabaret-théâtre où se produisirent <strong>Édith Piaf, Maurice Chevalier, Charles Trenet, Yves Montand, Brigitte Bardot, Georges Brassens, Jacques Brel, Serge Gainsbourg</strong>. La <strong>tradition théâtrale</strong> de la rue de la Gaîté perdure aujourd'hui."
        ],
        "faq": [
            ("Quelle ligne dessert Gaîté ?", "Uniquement la <strong>M13</strong>. Bus 28, 58, 91."),
            ("Quand a-t-elle ouvert ?", "Le <strong>21 janvier 1937</strong>."),
            ("Qu'est-ce que Bobino ?", "<strong>Célèbre cabaret-théâtre</strong> de la rue de la Gaîté. Édith Piaf, Brassens, Brel, Gainsbourg s'y produisirent."),
            ("Pour le Théâtre Montparnasse ?", "<strong>~2 min à pied</strong>."),
            ("Pour la Tour Montparnasse ?", "<strong>M13 → Montparnasse</strong> (1 station) ou à pied (5 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Rue de la Gaîté</strong> : théâtres populaires depuis le XIXe.",
            "<strong>Bobino</strong>, <strong>Théâtre Montparnasse</strong>, <strong>Théâtre de la Gaîté-Montparnasse</strong> à proximité.",
            "<strong>Tour Montparnasse</strong> à 5 min à pied.",
            "<strong>Cimetière du Montparnasse</strong> à 10 min à pied.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎭", "Rue de la Gaîté, théâtres populaires", "La <strong>rue de la Gaîté</strong>, longue de <strong>400 m</strong>, est l'un des <strong>hauts lieux du théâtre populaire parisien</strong> depuis le <strong>XIXe siècle</strong>. <strong>Théâtre Montparnasse</strong> (1851), <strong>Théâtre de la Gaîté-Montparnasse</strong> (1868), <strong>Bobino</strong> (1873), <strong>Théâtre du Petit Montparnasse</strong>. <strong>Tradition de comédies populaires</strong> et <strong>cabarets</strong>. La rue conserve son <strong>atmosphère théâtrale</strong>."),
            ("🎤", "Bobino, cabaret mythique", "<strong>Bobino</strong>, ouvert en <strong>1873</strong>, est l'un des <strong>cabarets-théâtres les plus mythiques</strong> de Paris. <strong>Édith Piaf</strong>, <strong>Maurice Chevalier</strong>, <strong>Charles Trenet</strong>, <strong>Yves Montand</strong>, <strong>Brigitte Bardot</strong>, <strong>Georges Brassens</strong>, <strong>Jacques Brel</strong>, <strong>Serge Gainsbourg</strong> y firent leurs récitals légendaires. Fermé en <strong>1985</strong>, <strong>rouvert en 1991</strong> après reconstruction. Continue d'accueillir des spectacles.")
        ],
        "itin": [
            ("Théâtre Montparnasse", "gaite", "à pied", "Rue de la Gaîté (2 min)", 2),
            ("Bobino", "gaite", "à pied", "Rue de la Gaîté (2 min)", 2),
            ("Tour Montparnasse", "montparnasse-bienvenue", "M13", "M13 directe (1 station)", 3),
            ("Cimetière du Montparnasse", "edgar-quinet", "M13 + M6", "À pied (10 min) ou M13 + M6", 10),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 18),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~14 min)", 14)
        ]
    },
    "pernety": {
        "addr": "Rue Raymond-Losserand, 75014 Paris", "arr": "14e arrondissement (Paris)",
        "seo": "Station Pernety (M13) rue Raymond-Losserand dans le 14e. Hommage à Joseph-Marie Pernety, général de la Révolution.",
        "tagline": "M13 — Pernety, 14e résidentiel",
        "hero_desc": "Station <strong>Pernety</strong> sur la <strong>rue Raymond-Losserand</strong> dans le <strong>14e arrondissement</strong>. Desservie par la <strong>M13</strong>, ouverte le <strong>21 janvier 1937</strong>. Hommage à <strong>Joseph-Marie Pernety</strong> (<strong>1766-1856</strong>), <strong>général français</strong>.",
        "intros": [
            "La station <strong>Pernety</strong> est implantée sur la <strong>rue Raymond-Losserand</strong> dans le <strong>14e arrondissement</strong>. Elle est desservie par la <strong>M13</strong>, entre <strong>Gaîté</strong> (1 station) et <strong>Plaisance</strong> (1 station). Bus 58, 62.",
            "Ouverte le <strong>21 janvier 1937</strong> avec l'<strong>ancienne ligne 14</strong> (intégrée à la M13 en 1976).",
            "Le nom <strong>Pernety</strong> rend hommage à <strong>Joseph-Marie de Pernety</strong> (<strong>1766-1856</strong>), <strong>général français</strong> de la <strong>Révolution</strong> et de l'<strong>Empire</strong>. Quartier <strong>14e résidentiel</strong>."
        ],
        "hist_title": "1937 : ancienne ligne 14 et général",
        "hist": [
            "La station Pernety est <strong>inaugurée le 21 janvier 1937</strong> avec l'<strong>ancienne ligne 14</strong> (<strong>Bienvenüe ↔ Porte de Vanves</strong>), <strong>intégrée à la M13 en 1976</strong>.",
            "Le nom <strong>Pernety</strong> rend hommage à <strong>Joseph-Marie de Pernety</strong> (<strong>1766-1856</strong>), <strong>général français</strong> de la <strong>Révolution</strong> et de l'<strong>Empire</strong>. <strong>Général d'artillerie</strong>.",
            "Le quartier autour de la station fait partie du <strong>14e arrondissement</strong>, secteur résidentiel populaire et commerçant. À proximité : le <strong>quartier Plaisance</strong> et l'ancien <strong>quartier des Maraîchers</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Pernety ?", "Uniquement la <strong>M13</strong>. Bus 58, 62."),
            ("Qui est Pernety ?", "<strong>Joseph-Marie de Pernety</strong> (1766-1856), <strong>général français</strong> de la Révolution et de l'Empire."),
            ("Quand a-t-elle ouvert ?", "Le <strong>21 janvier 1937</strong>."),
            ("Pour la Tour Montparnasse ?", "<strong>M13 directe</strong> (2 stations, ~5 min)."),
            ("Pour le quartier Plaisance ?", "<strong>~5 min à pied</strong> ou <strong>M13 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier <strong>14e résidentiel</strong> et commerçant.",
            "Pour <strong>Tour Montparnasse</strong> : <strong>M13 directe</strong> (2 stations).",
            "Pour <strong>Châtelet</strong> : <strong>M13 + M14</strong> via Saint-Lazare.",
            "Pour <strong>Plaisance</strong> : <strong>M13 directe</strong> (1 station).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⚔️", "Pernety, général d'artillerie", "<strong>Joseph-Marie de Pernety</strong> (1766-1856), <strong>général français</strong> de la <strong>Révolution</strong> et de l'<strong>Empire</strong>. <strong>Général d'artillerie</strong>. Sert dans les campagnes de l'Armée d'Italie sous Bonaparte, puis dans la Grande Armée. <strong>Pair de France</strong> sous la Restauration. <strong>Grand-officier de la Légion d'honneur</strong>."),
            ("🏘️", "14e arrondissement, contrastes", "Le <strong>14e arrondissement</strong> de Paris (~140 000 habitants) présente un mix de <strong>quartiers résidentiels</strong>, de <strong>secteurs Montparnasse</strong> (théâtres, cafés), et de <strong>quartiers populaires</strong> (Plaisance, Pernety). Il comprend également le <strong>cimetière du Montparnasse</strong>, les <strong>Catacombes</strong>, le <strong>parc Montsouris</strong>, la <strong>Cité internationale universitaire</strong>.")
        ],
        "itin": [
            ("Plaisance", "plaisance", "M13", "M13 directe (1 station)", 2),
            ("Tour Montparnasse", "montparnasse-bienvenue", "M13", "M13 directe (2 stations)", 5),
            ("Gaîté (théâtres)", "gaite", "M13", "M13 directe (1 station)", 2),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 20),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~16 min)", 16),
            ("Porte de Vanves", "porte-de-vanves", "M13", "M13 directe (2 stations)", 4)
        ]
    },
    "plaisance": {
        "addr": "Avenue du Maine, 75014 Paris", "arr": "14e arrondissement (Paris)",
        "seo": "Station Plaisance (M13) avenue du Maine dans le 14e. Ancien quartier de Plaisance, rattaché à Paris en 1860.",
        "tagline": "M13 — quartier de Plaisance, ancien village",
        "hero_desc": "Station <strong>Plaisance</strong> sur l'<strong>avenue du Maine</strong> dans le <strong>14e arrondissement</strong>. Desservie par la <strong>M13</strong>, ouverte le <strong>21 janvier 1937</strong>. Ancien <strong>village de Plaisance</strong>, rattaché à Paris en <strong>1860</strong>.",
        "intros": [
            "La station <strong>Plaisance</strong> est implantée sur l'<strong>avenue du Maine</strong> dans le <strong>14e arrondissement</strong>. Elle est desservie par la <strong>M13</strong>, entre <strong>Pernety</strong> (1 station) et <strong>Porte de Vanves</strong> (1 station). Bus 58, 62.",
            "Ouverte le <strong>21 janvier 1937</strong> avec l'<strong>ancienne ligne 14</strong> (intégrée à la M13 en 1976).",
            "Le nom <strong>Plaisance</strong> rappelle l'<strong>ancien quartier de Plaisance</strong>, rattaché à Paris en <strong>1860</strong>. Étymologie : nom commercial donné à un lotissement créé en <strong>1830</strong> par <strong>Alphonse-Frédéric Lacroix</strong>, évoquant une vie « plaisante » à la périphérie. Quartier populaire et résidentiel."
        ],
        "hist_title": "1937 : ancien village de Plaisance",
        "hist": [
            "La station Plaisance est <strong>inaugurée le 21 janvier 1937</strong> avec l'<strong>ancienne ligne 14</strong> (Bienvenüe ↔ Porte de Vanves), intégrée à la M13 en 1976.",
            "Le nom <strong>Plaisance</strong> rappelle l'<strong>ancien quartier de Plaisance</strong>. Le quartier est créé en <strong>1830</strong> par <strong>Alphonse-Frédéric Lacroix</strong>, qui lotit ses terres à la périphérie sud de Paris. Le nom <strong>« Plaisance »</strong> évoque la <strong>vie agréable</strong> et <strong>plaisante</strong> que prometaient ces nouveaux lotissements aux Parisiens.",
            "<strong>Rattaché à Paris en 1860</strong> avec d'autres communes périphériques (annexion par Haussmann). Le quartier conserve son <strong>caractère populaire</strong>, avec ses <strong>petites maisons</strong>, ses <strong>ruelles pavées</strong>, ses <strong>petits commerces</strong>. <strong>Marché Brune</strong> (alimentaire) à proximité."
        ],
        "faq": [
            ("Quelle ligne dessert Plaisance ?", "Uniquement la <strong>M13</strong>. Bus 58, 62."),
            ("D'où vient le nom Plaisance ?", "Du <strong>quartier de Plaisance</strong> créé en <strong>1830</strong>, nom commercial évoquant la <strong>vie agréable</strong> de la périphérie."),
            ("Quand a-t-elle ouvert ?", "Le <strong>21 janvier 1937</strong>."),
            ("Pour le marché Brune ?", "<strong>~5 min à pied</strong>."),
            ("Pour la Tour Montparnasse ?", "<strong>M13 directe</strong> (3 stations, ~7 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier <strong>14e populaire</strong> avec petites maisons et ruelles.",
            "<strong>Marché Brune</strong> à 5 min à pied.",
            "Pour <strong>Tour Montparnasse</strong> : <strong>M13 directe</strong> (3 stations).",
            "Pour <strong>Porte de Vanves</strong> et <strong>marché aux puces</strong> : <strong>M13 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏘️", "Quartier de Plaisance, lotissement 1830", "Le <strong>quartier de Plaisance</strong>, autour de la station, est créé en <strong>1830</strong> par <strong>Alphonse-Frédéric Lacroix</strong>, propriétaire qui lotit ses terres à la périphérie sud de Paris. Le nom <strong>« Plaisance »</strong> est un <strong>argument commercial</strong> évoquant la <strong>vie agréable et plaisante</strong> que promettent ces nouveaux lotissements. <strong>Rattaché à Paris en 1860</strong> avec d'autres communes."),
            ("🏠", "Architecture populaire préservée", "Le <strong>quartier de Plaisance</strong> conserve une <strong>architecture populaire</strong> caractéristique. <strong>Petites maisons</strong> (rez-de-chaussée et un étage), <strong>ruelles pavées</strong>, <strong>cours intérieures</strong>. Témoignage du <strong>Paris d'avant Haussmann</strong>. À pied, on découvre des <strong>passages anciens</strong> (passage de Plaisance, passage Léon).")
        ],
        "itin": [
            ("Marché Brune", "porte-de-vanves", "à pied", "5 min à pied", 5),
            ("Tour Montparnasse", "montparnasse-bienvenue", "M13", "M13 directe (3 stations)", 7),
            ("Porte de Vanves", "porte-de-vanves", "M13", "M13 directe (1 station)", 2),
            ("Pernety", "pernety", "M13", "M13 directe (1 station)", 2),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 22),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~18 min)", 18)
        ]
    },
    "porte-de-vanves": {
        "addr": "Avenue Marc-Sangnier, 75014 Paris", "arr": "14e arrondissement (Paris)",
        "seo": "Station Porte de Vanves (M13) avenue Marc-Sangnier dans le 14e. Marché aux puces de la Porte de Vanves (samedi et dimanche).",
        "tagline": "M13 — porte de Vanves, marché aux puces",
        "hero_desc": "Station <strong>Porte de Vanves</strong> sur l'<strong>avenue Marc-Sangnier</strong> dans le <strong>14e arrondissement</strong>. Desservie par la <strong>M13</strong>, ouverte le <strong>21 janvier 1937</strong>. À proximité : le <strong>marché aux puces de la Porte de Vanves</strong>.",
        "intros": [
            "La station <strong>Porte de Vanves</strong> est implantée sur l'<strong>avenue Marc-Sangnier</strong>, à la <strong>limite sud du 14e arrondissement</strong>. Elle est desservie par la <strong>M13</strong>, entre <strong>Plaisance</strong> (1 station) et <strong>Malakoff - Plateau de Vanves</strong> (1 station). Bus 58, 62, 95, 195, T3a tramway.",
            "Ouverte le <strong>21 janvier 1937</strong> avec l'<strong>ancienne ligne 14</strong> (intégrée à la M13 en 1976).",
            "À la sortie : le <strong>marché aux puces de la Porte de Vanves</strong>, l'un des <strong>trois grands marchés aux puces parisiens</strong>. Ouvert <strong>samedi et dimanche</strong> matin. Spécialisé en <strong>antiquités</strong>, <strong>brocante</strong>, <strong>vinyles</strong>, <strong>jouets anciens</strong>."
        ],
        "hist_title": "1937 : porte sud et marché aux puces",
        "hist": [
            "La station Porte de Vanves est <strong>inaugurée le 21 janvier 1937</strong> comme <strong>terminus sud temporaire</strong> de l'<strong>ancienne ligne 14</strong> (intégrée à la M13 en 1976, prolongée vers Châtillon-Montrouge).",
            "Le <strong>marché aux puces de la Porte de Vanves</strong>, à la sortie, est l'un des <strong>trois grands marchés aux puces parisiens</strong> avec <strong>Saint-Ouen</strong> et <strong>Montreuil</strong>. Ouvert depuis les <strong>années 1920</strong>. <strong>~400 exposants</strong> sur <strong>2 km d'étals</strong> le long de l'avenue Georges-Lafenestre.",
            "<strong>Spécialisé en antiquités</strong>, <strong>brocante</strong>, <strong>vinyles</strong>, <strong>jouets anciens</strong>, <strong>vintage</strong>. Marché ouvert <strong>samedi et dimanche</strong> matin (7h-13h). Atmosphère <strong>plus intimiste</strong> que Saint-Ouen, fréquenté par les <strong>chineurs</strong>."
        ],
        "faq": [
            ("Quelles lignes desservent Porte de Vanves ?", "<strong>M13</strong> et <strong>tramway T3a</strong>. Bus 58, 62, 95, 195."),
            ("Quand a-t-elle ouvert ?", "Le <strong>21 janvier 1937</strong>."),
            ("Quand est ouvert le marché aux puces ?", "<strong>Samedi et dimanche matin</strong> (7h-13h)."),
            ("Pour le marché aux puces ?", "<strong>Sortie directe</strong> vers l'avenue Georges-Lafenestre."),
            ("Pour Châtillon-Montrouge (terminus) ?", "<strong>M13 directe</strong> (3 stations)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Marché aux puces de la Porte de Vanves</strong> à la sortie : <strong>samedi et dimanche</strong> matin.",
            "<strong>Tramway T3a</strong> en correspondance.",
            "Spécialités : <strong>antiquités, brocante, vinyles, jouets anciens, vintage</strong>.",
            "Pour <strong>Châtillon-Montrouge</strong> : <strong>M13 directe</strong> (3 stations).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🛍️", "Marché aux puces de la Porte de Vanves", "Le <strong>marché aux puces de la Porte de Vanves</strong>, à la sortie de la station, est l'un des <strong>trois grands marchés aux puces parisiens</strong> avec <strong>Saint-Ouen</strong> et <strong>Montreuil</strong>. Ouvert depuis les <strong>années 1920</strong>. <strong>~400 exposants</strong> sur <strong>2 km d'étals</strong> le long de l'avenue Georges-Lafenestre. <strong>Spécialités</strong> : antiquités, brocante, vinyles, jouets anciens, vintage. Marché <strong>samedi et dimanche matin</strong>. <strong>Atmosphère plus intimiste</strong> que Saint-Ouen."),
            ("🚊", "Tramway T3a, boulevards des Maréchaux", "Le <strong>tramway T3a</strong>, en correspondance directe, circule sur les <strong>boulevards des Maréchaux</strong> au sud de Paris. <strong>Inauguré en 2006</strong> entre <strong>Pont du Garigliano</strong> et <strong>Porte d'Ivry</strong>. <strong>Prolongé en 2012</strong> jusqu'à <strong>Porte de Vincennes</strong>. <strong>~12 km</strong>, <strong>~150 000 voyageurs/jour</strong>. Remplace l'ancienne <strong>PC1</strong> (Petite Ceinture).")
        ],
        "itin": [
            ("Marché aux puces", "porte-de-vanves", "à pied", "Sortie directe (samedi/dimanche matin)", 2),
            ("Tramway T3a", "porte-de-vanves", "tramway", "Correspondance directe", 1),
            ("Châtillon-Montrouge (terminus)", "chatillon-montrouge", "M13", "M13 directe (3 stations)", 6),
            ("Tour Montparnasse", "montparnasse-bienvenue", "M13", "M13 directe (4 stations)", 10),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~20 min)", 20),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 24)
        ]
    },
    "malakoff-plateau-de-vanves": {
        "addr": "Avenue Pierre-Brossolette, 92240 Malakoff", "arr": "Malakoff (92)",
        "seo": "Station Malakoff - Plateau de Vanves (M13) à Malakoff (92). Hommage à la bataille de Malakoff (1855) lors de la guerre de Crimée.",
        "tagline": "M13 — Malakoff, bataille de Crimée (1855)",
        "hero_desc": "Station <strong>Malakoff - Plateau de Vanves</strong> à <strong>Malakoff</strong> (Hauts-de-Seine, 92). Desservie par la <strong>M13</strong>, ouverte le <strong>9 novembre 1976</strong>. Hommage à la <strong>bataille de Malakoff</strong> (8 septembre 1855), bataille majeure de la <strong>guerre de Crimée</strong>.",
        "intros": [
            "La station <strong>Malakoff - Plateau de Vanves</strong> est implantée à <strong>Malakoff</strong> (Hauts-de-Seine, 92). Elle est desservie par la <strong>M13</strong>, entre <strong>Porte de Vanves</strong> (1 station) et <strong>Malakoff - Rue Étienne Dolet</strong> (1 station). Bus 58, 191, 194.",
            "Ouverte le <strong>9 novembre 1976</strong> avec le <strong>prolongement de la M13</strong> de <strong>Porte de Vanves à Châtillon-Montrouge</strong>.",
            "Le nom <strong>Malakoff</strong> rend hommage à la <strong>bataille de Malakoff</strong> (<strong>8 septembre 1855</strong>), <strong>victoire française décisive</strong> lors de la <strong>guerre de Crimée</strong>. La commune de <strong>Malakoff</strong> (~30 000 habitants) prend ce nom en <strong>1883</strong>."
        ],
        "hist_title": "1976 : prolongement et bataille de Crimée 1855",
        "hist": [
            "La station est <strong>inaugurée le 9 novembre 1976</strong> avec le <strong>prolongement de la M13</strong> de <strong>Porte de Vanves à Châtillon-Montrouge</strong>.",
            "Le nom <strong>Malakoff</strong> rend hommage à la <strong>bataille de Malakoff</strong> (<strong>8 septembre 1855</strong>), <strong>victoire française décisive</strong> lors de la <strong>guerre de Crimée</strong> (1853-1856). Les <strong>Français</strong> commandés par le <strong>général Pélissier</strong> s'emparent du <strong>fort de Malakoff</strong> à <strong>Sébastopol</strong>, ouvrant la voie à la <strong>chute de Sébastopol</strong>.",
            "La <strong>commune de Malakoff</strong> (~30 000 habitants), à laquelle appartient la station, prend ce nom en <strong>1883</strong> en l'honneur de la bataille. Elle se sépare de la commune de Vanves. Ancien terrain de <strong>tour Malakoff</strong> (1855) qui célébrait la victoire (démontée en 1870)."
        ],
        "faq": [
            ("Quelle ligne dessert Malakoff - Plateau de Vanves ?", "Uniquement la <strong>M13</strong>. Bus 58, 191, 194."),
            ("Qu'est-ce que la bataille de Malakoff ?", "<strong>Victoire française décisive</strong> du <strong>8 septembre 1855</strong> lors de la <strong>guerre de Crimée</strong>. Prise du fort de Malakoff à Sébastopol."),
            ("Quand a-t-elle ouvert ?", "Le <strong>9 novembre 1976</strong>."),
            ("Pourquoi la commune se nomme Malakoff ?", "Renommée en <strong>1883</strong> en hommage à la <strong>bataille de Malakoff</strong>."),
            ("Pour Châtillon-Montrouge ?", "<strong>M13 directe</strong> (2 stations, terminus)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "Quartier résidentiel de <strong>Malakoff</strong> (92).",
            "Pour <strong>Châtillon-Montrouge</strong> (terminus + T6) : <strong>M13 directe</strong>.",
            "Pour <strong>Porte de Vanves</strong> et son marché : <strong>M13 directe</strong> (1 station).",
            "Pour <strong>Tour Montparnasse</strong> : <strong>M13 directe</strong> (5 stations).",
            "Zone tarifaire <strong>2</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("⚔️", "Bataille de Malakoff (8 septembre 1855)", "La <strong>bataille de Malakoff</strong>, le <strong>8 septembre 1855</strong>, est une <strong>victoire française décisive</strong> de la <strong>guerre de Crimée</strong> (1853-1856). Les <strong>Français</strong>, commandés par le <strong>général Pélissier</strong>, s'emparent du <strong>fort de Malakoff</strong> à <strong>Sébastopol</strong> après <strong>349 jours de siège</strong>. Ouvre la voie à la <strong>chute de Sébastopol</strong> (10 septembre 1855) et à la <strong>fin de la guerre</strong>. <strong>Traité de Paris</strong> (30 mars 1856)."),
            ("🏛️", "Commune de Malakoff (1883)", "La <strong>commune de Malakoff</strong> (~30 000 habitants) prend ce nom en <strong>1883</strong> en l'honneur de la <strong>bataille</strong>. Auparavant, le territoire faisait partie de la commune de <strong>Vanves</strong>. La <strong>tour Malakoff</strong> (1855), monument célébrant la victoire, fut démontée en <strong>1870</strong> mais donna son nom au quartier. Aujourd'hui, commune des Hauts-de-Seine.")
        ],
        "itin": [
            ("Châtillon-Montrouge (terminus + T6)", "chatillon-montrouge", "M13", "M13 directe (2 stations, terminus)", 5),
            ("Malakoff - Rue Étienne Dolet", "malakoff-rue-etienne-dolet", "M13", "M13 directe (1 station)", 2),
            ("Porte de Vanves (marché)", "porte-de-vanves", "M13", "M13 directe (1 station)", 2),
            ("Tour Montparnasse", "montparnasse-bienvenue", "M13", "M13 directe (5 stations)", 12),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 25),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~22 min)", 22)
        ]
    },
    "malakoff-rue-etienne-dolet": {
        "addr": "Rue Étienne-Dolet, 92240 Malakoff", "arr": "Malakoff (92)",
        "seo": "Station Malakoff - Rue Étienne Dolet (M13) à Malakoff (92). Hommage à Étienne Dolet, humaniste et imprimeur de la Renaissance.",
        "tagline": "M13 — Étienne Dolet, humaniste de la Renaissance",
        "hero_desc": "Station <strong>Malakoff - Rue Étienne Dolet</strong> à <strong>Malakoff</strong> (Hauts-de-Seine, 92). Desservie par la <strong>M13</strong>, ouverte le <strong>9 novembre 1976</strong>. Hommage à <strong>Étienne Dolet</strong> (<strong>1509-1546</strong>), <strong>humaniste, imprimeur et écrivain français</strong> de la <strong>Renaissance</strong>.",
        "intros": [
            "La station <strong>Malakoff - Rue Étienne Dolet</strong> est implantée à <strong>Malakoff</strong> (Hauts-de-Seine, 92). Elle est desservie par la <strong>M13</strong>, entre <strong>Malakoff - Plateau de Vanves</strong> (1 station) et <strong>Châtillon-Montrouge</strong> (1 station, terminus). Bus 191, 194.",
            "Ouverte le <strong>9 novembre 1976</strong> avec le <strong>prolongement de la M13</strong>.",
            "Le nom <strong>Étienne Dolet</strong> rend hommage à <strong>Étienne Dolet</strong> (<strong>1509-1546</strong>), <strong>humaniste, imprimeur et écrivain français</strong> de la <strong>Renaissance</strong>. Auteur d'<strong>ouvrages de philosophie</strong> et de <strong>traductions</strong>."
        ],
        "hist_title": "1976 : prolongement et humaniste Renaissance",
        "hist": [
            "La station est <strong>inaugurée le 9 novembre 1976</strong> avec le <strong>prolongement de la M13</strong> de <strong>Porte de Vanves à Châtillon-Montrouge</strong>.",
            "Le nom <strong>Étienne Dolet</strong> rend hommage à <strong>Étienne Dolet</strong> (<strong>3 août 1509 - 3 août 1546</strong>), <strong>humaniste, imprimeur et écrivain français</strong> de la <strong>Renaissance</strong>. Né à Orléans.",
            "<strong>Imprimeur</strong> et <strong>traducteur</strong>, il publie des <strong>œuvres de philosophie</strong> antique et des <strong>traductions</strong>. Auteur des <em><strong>Commentaires de la langue latine</strong></em>. <strong>Figure majeure de l'humanisme français</strong> du XVIe siècle. <strong>Pair de Rabelais</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Malakoff - Rue Étienne Dolet ?", "Uniquement la <strong>M13</strong>. Bus 191, 194."),
            ("Qui est Étienne Dolet ?", "<strong>Étienne Dolet</strong> (1509-1546), <strong>humaniste, imprimeur et écrivain français</strong> de la <strong>Renaissance</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>9 novembre 1976</strong>."),
            ("Pour Châtillon-Montrouge ?", "<strong>M13 directe</strong> (1 station, terminus)."),
            ("Pour Tour Montparnasse ?", "<strong>M13 directe</strong> (6 stations, ~14 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "Quartier résidentiel de <strong>Malakoff</strong>.",
            "Pour <strong>Châtillon-Montrouge</strong> (terminus + T6) : <strong>M13 directe</strong> (1 station).",
            "Pour <strong>Porte de Vanves</strong> et son marché : <strong>M13 directe</strong>.",
            "Pour <strong>Tour Montparnasse</strong> : <strong>M13 directe</strong>.",
            "Zone tarifaire <strong>2</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("📚", "Étienne Dolet, humaniste de la Renaissance", "<strong>Étienne Dolet</strong> (<strong>1509-1546</strong>), <strong>humaniste, imprimeur et écrivain français</strong> de la <strong>Renaissance</strong>. Né à <strong>Orléans</strong>. <strong>Imprimeur</strong> et <strong>traducteur</strong>, il publie des <strong>œuvres de philosophie antique</strong> et des <strong>traductions</strong> (notamment de <strong>Platon</strong>). Auteur des <em><strong>Commentaires de la langue latine</strong></em> (1536-1538). <strong>Figure majeure de l'humanisme français</strong> du XVIe siècle."),
            ("🏛️", "Renaissance française et imprimerie", "L'<strong>imprimerie</strong>, inventée par <strong>Gutenberg</strong> au milieu du <strong>XVe siècle</strong>, joue un rôle clé dans la <strong>Renaissance française</strong>. Permet la <strong>diffusion massive</strong> des <strong>œuvres antiques</strong> redécouvertes et des <strong>idées humanistes</strong>. Des imprimeurs comme <strong>Étienne Dolet</strong>, <strong>Robert Estienne</strong>, <strong>Geoffroy Tory</strong> contribuent à la <strong>standardisation du français</strong> et à la <strong>diffusion de l'humanisme</strong>.")
        ],
        "itin": [
            ("Châtillon-Montrouge (terminus + T6)", "chatillon-montrouge", "M13", "M13 directe (1 station)", 2),
            ("Malakoff - Plateau de Vanves", "malakoff-plateau-de-vanves", "M13", "M13 directe (1 station)", 2),
            ("Porte de Vanves (marché)", "porte-de-vanves", "M13", "M13 directe (2 stations)", 4),
            ("Tour Montparnasse", "montparnasse-bienvenue", "M13", "M13 directe (6 stations)", 14),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~24 min)", 24),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 28)
        ]
    },
    "chatillon-montrouge": {
        "addr": "Avenue de la République, 92320 Châtillon", "arr": "Châtillon (92)",
        "seo": "Station Châtillon - Montrouge, terminus sud M13 à Châtillon (92). Correspondance tramway T6 vers Vélizy.",
        "tagline": "M13 — terminus sud, tramway T6 vers Vélizy",
        "hero_desc": "Station <strong>Châtillon - Montrouge</strong>, <strong>terminus sud de la M13</strong>, à <strong>Châtillon</strong> (Hauts-de-Seine, 92), à la limite de <strong>Montrouge</strong>. Ouverte le <strong>9 novembre 1976</strong>. Correspondance <strong>tramway T6</strong> vers <strong>Vélizy-Villacoublay</strong>.",
        "intros": [
            "La station <strong>Châtillon - Montrouge</strong> est le <strong>terminus sud de la M13</strong>, située à <strong>Châtillon</strong> (Hauts-de-Seine, 92), à la limite de <strong>Montrouge</strong>. Bus 68, 195, 294, 388, 391, tramway T6.",
            "Ouverte le <strong>9 novembre 1976</strong> avec le <strong>prolongement de la M13</strong> de <strong>Porte de Vanves à Châtillon-Montrouge</strong>.",
            "<strong>Correspondance tramway T6</strong> qui dessert <strong>Vélizy-Villacoublay</strong> et <strong>Viroflay</strong>, mis en service en <strong>2014</strong>. À la limite de deux communes : <strong>Châtillon</strong> (~37 000 habitants) et <strong>Montrouge</strong> (~50 000 habitants)."
        ],
        "hist_title": "1976 : terminus sud et T6 (2014)",
        "hist": [
            "La station Châtillon - Montrouge est <strong>inaugurée le 9 novembre 1976</strong> comme <strong>terminus sud de la M13</strong>, avec le <strong>prolongement de la ligne</strong> de <strong>Porte de Vanves à Châtillon</strong>. Ce <strong>prolongement</strong> dessert les communes du <strong>plateau de Vanves</strong> et de la <strong>vallée de la Bièvre</strong>.",
            "Le <strong>tramway T6</strong>, en correspondance, est <strong>inauguré le 13 décembre 2014</strong>. Ligne entre <strong>Châtillon - Montrouge</strong> et <strong>Vélizy-Villacoublay</strong>, prolongée à <strong>Viroflay - Rive Droite</strong> en <strong>2016</strong>. <strong>14 km</strong>, <strong>~70 000 voyageurs/jour</strong>.",
            "<strong>Châtillon</strong> (~37 000 habitants) et <strong>Montrouge</strong> (~50 000 habitants) sont deux communes dynamiques des <strong>Hauts-de-Seine</strong>. Quartier d'affaires en développement avec plusieurs sièges sociaux."
        ],
        "faq": [
            ("Quelles lignes desservent Châtillon - Montrouge ?", "<strong>M13</strong> (terminus sud) et <strong>tramway T6</strong>. Bus 68, 195, 294, 388, 391."),
            ("Quand a-t-elle ouvert ?", "Le <strong>9 novembre 1976</strong>."),
            ("Pour Vélizy ?", "<strong>Tramway T6</strong>."),
            ("Pour Châtillon centre ?", "À <strong>5-10 min à pied</strong>."),
            ("Pour Tour Montparnasse ?", "<strong>M13 directe</strong> (7 stations, ~16 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Tramway T6</strong> vers Vélizy et Viroflay.",
            "<strong>Châtillon</strong> et <strong>Montrouge</strong> : communes dynamiques 92.",
            "Pour <strong>Tour Montparnasse</strong> : <strong>M13 directe</strong> (7 stations).",
            "Pour <strong>Saint-Lazare</strong> : <strong>M13 directe</strong> (~26 min).",
            "Zone tarifaire <strong>2</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("🚊", "Tramway T6, ligne pneumatique 2014", "Le <strong>tramway T6</strong>, en correspondance, est <strong>inauguré le 13 décembre 2014</strong>. <strong>Ligne pneumatique</strong> (sur pneus, sur rail central guidé) entre <strong>Châtillon - Montrouge</strong> et <strong>Vélizy-Villacoublay</strong>, prolongée à <strong>Viroflay - Rive Droite</strong> en <strong>2016</strong>. <strong>14 km</strong>, <strong>21 stations</strong>, <strong>~70 000 voyageurs/jour</strong>. <strong>Technologie Translohr</strong> (Lohr Industrie)."),
            ("🏛️", "Châtillon, ancien village", "<strong>Châtillon</strong>, ~37 000 habitants, commune des <strong>Hauts-de-Seine</strong>. <strong>Ancien village</strong> au <strong>nom évoquant un château</strong> (Castellio en latin). Aujourd'hui commune <strong>résidentielle et tertiaire</strong>. Quartier d'affaires en développement avec plusieurs <strong>sièges sociaux</strong> (Bouygues Telecom, OVH).")
        ],
        "itin": [
            ("Vélizy-Villacoublay", "chatillon-montrouge", "T6", "Tramway T6 (~25 min)", 25),
            ("Tour Montparnasse", "montparnasse-bienvenue", "M13", "M13 directe (7 stations)", 16),
            ("Porte de Vanves (marché)", "porte-de-vanves", "M13", "M13 directe (3 stations)", 6),
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (~26 min)", 26),
            ("Châtelet", "chatelet", "M13 + M14", "M13 → Saint-Lazare + M14", 30),
            ("Champs-Élysées", "champs-elysees-clemenceau", "M13", "M13 directe (~28 min)", 28)
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
