#!/usr/bin/env python3
"""Enrichit M2 16 stations avec contenu T0 Wikipedia FR."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    "porte-dauphine": {
        "addr": "Avenue Foch, 75116 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Porte Dauphine, terminus ouest de la M2. Édicule Guimard Art Nouveau original de 1900 classé. Accès Bois de Boulogne, avenue Foch.",
        "tagline": "M2 — terminus ouest, édicule Guimard original 1900",
        "hero_desc": "Station <strong>Porte Dauphine</strong>, <strong>terminus ouest de la M2</strong>, à l'extrémité de l'<strong>avenue Foch</strong> dans le <strong>16e arrondissement</strong>. Ouverte le <strong>13 décembre 1900</strong>. Célèbre pour son <strong>édicule Hector Guimard</strong> en <strong>fonte et fer forgé</strong> Art Nouveau, l'un des <strong>derniers édicules originaux</strong> de 1900 préservés à Paris (<strong>classé monument historique</strong>). Accès au <strong>Bois de Boulogne</strong>.",
        "intros": [
            "La station <strong>Porte Dauphine</strong>, <strong>terminus ouest de la ligne 2</strong>, est implantée à l'extrémité de l'<strong>avenue Foch</strong>, à l'orée du <strong>Bois de Boulogne</strong>, dans le <strong>16e arrondissement</strong>. Elle est desservie par la <strong>M2</strong> et par le <strong>RER C</strong> (station Avenue Foch toute proche). Bus PC1, 82.",
            "Inaugurée le <strong>13 décembre 1900</strong> avec le tronçon Étoile ↔ Porte Dauphine, premier prolongement de la ligne 2. La station a conservé son <strong>édicule original signé Hector Guimard</strong>, en <strong>fonte et fer forgé</strong>, qui constitue aujourd'hui un des <strong>derniers édicules originaux</strong> du métropolitain. <strong>Classé monument historique</strong> en 1978.",
            "L'<strong>avenue Foch</strong>, la <strong>plus large de Paris</strong> (<strong>120 m de large</strong>, longue de 1,3 km), relie la <strong>place Charles-de-Gaulle (Étoile)</strong> à la <strong>porte Dauphine</strong>. Anciennement <strong>avenue du Bois</strong>, renommée en 1929 en hommage au <strong>maréchal Ferdinand Foch</strong>. Accès au <strong>Bois de Boulogne</strong> (845 ha)."
        ],
        "hist_title": "1900 : édicule Guimard et terminus ouest",
        "hist": [
            "La station Porte Dauphine est <strong>inaugurée le 13 décembre 1900</strong> avec le prolongement de la <strong>ligne 2 Nord</strong> (devenue ligne 2 en 1907) de la <strong>place de l'Étoile</strong> jusqu'à <strong>Porte Dauphine</strong>. Initialement <strong>boucle terminus</strong> (les rames repartaient sans demi-tour), elle est aujourd'hui un terminus classique.",
            "L'<strong>édicule Guimard</strong> de Porte Dauphine est l'un des <strong>derniers édicules originaux</strong> de l'<strong>architecte Hector Guimard</strong> (<strong>1867-1942</strong>), figure majeure de l'<strong>Art Nouveau</strong>. Construit en <strong>fonte et fer forgé</strong>, il présente des <strong>balustrades</strong> et <strong>lampadaires</strong> ouvragés. <strong>Classé monument historique</strong> le <strong>12 juillet 1978</strong>. Sur les 167 entrées Guimard d'origine, <strong>moins de 90 subsistent</strong>.",
            "L'<strong>avenue Foch</strong> (anciennement <strong>avenue du Bois</strong>), large de <strong>120 m</strong>, est la <strong>plus large avenue de Paris</strong>. Tracée par <strong>Haussmann en 1854</strong>, renommée en <strong>1929</strong> en hommage à <strong>Ferdinand Foch</strong> (1851-1929), <strong>maréchal de France</strong>, <strong>commandant en chef des armées alliées</strong> à la fin de la Première Guerre mondiale (signataire de l'armistice du <strong>11 novembre 1918</strong> à Rethondes)."
        ],
        "faq": [
            ("Quelle ligne dessert Porte Dauphine ?", "<strong>Ligne 2 du métro</strong> (terminus ouest) et <strong>RER C</strong> (Avenue Foch toute proche). Bus PC1, 82."),
            ("Qu'a-t-elle de spécial ?", "Elle conserve un <strong>édicule original Hector Guimard</strong> de <strong>1900</strong> en fonte et fer forgé, <strong>classé monument historique</strong>. L'un des derniers à Paris."),
            ("Qui est Hector Guimard ?", "<strong>Hector Guimard</strong> (1867-1942), <strong>architecte français</strong>, figure majeure de l'<strong>Art Nouveau</strong>. Auteur des édicules d'entrée du métro parisien et de l'<strong>Castel Béranger</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>13 décembre 1900</strong>."),
            ("Pour le Bois de Boulogne ?", "<strong>Sortie directe</strong>. Entrée par la <strong>porte Dauphine</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Édicule Guimard original 1900</strong> classé monument historique — à photographier.",
            "Accès direct au <strong>Bois de Boulogne</strong> (lac inférieur, hippodrome de Longchamp accessible).",
            "Pour <strong>Charles de Gaulle - Étoile</strong> : <strong>M2 directe</strong> (1 station).",
            "<strong>Avenue Foch</strong> : la <strong>plus large de Paris</strong> (120 m).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎨", "Hector Guimard et les entrées Art Nouveau du métro", "<strong>Hector Guimard</strong> (1867-1942), <strong>architecte français</strong>, est l'un des <strong>maîtres de l'Art Nouveau</strong>. Commandé en <strong>1899</strong> par la <strong>Compagnie du Métropolitain Parisien</strong> (CMP), il conçoit <strong>167 édicules</strong> d'entrée en <strong>fonte verte</strong> et <strong>verre opaline jaune</strong>. Reconnaissables à leurs <strong>arches en forme de tige végétale</strong> et lampadaires <em>brins de muguet</em>. Aujourd'hui <strong>moins de 90 édicules subsistent</strong>, certains classés monuments historiques. Porte Dauphine est l'un des <strong>derniers édicules originaux</strong>."),
            ("🌳", "Bois de Boulogne, le poumon ouest de Paris", "Le <strong>Bois de Boulogne</strong>, à la sortie directe de la station, est l'un des <strong>plus grands espaces verts de Paris</strong> avec <strong>846 hectares</strong>. Ancien <strong>domaine de chasse royal</strong>, cédé à la Ville de Paris en <strong>1852</strong> par Napoléon III, aménagé par <strong>Adolphe Alphand</strong>. Il abrite <strong>deux lacs</strong>, l'<strong>hippodrome de Longchamp</strong>, le <strong>jardin d'acclimatation</strong>, la <strong>Fondation Louis Vuitton</strong> (depuis 2014).")
        ],
        "itin": [
            ("Bois de Boulogne", "porte-dauphine", "à pied", "Sortie directe", 2),
            ("Charles de Gaulle - Étoile", "charles-de-gaulle-etoile", "M2", "M2 directe (1 station)", 3),
            ("Champs-Élysées", "george-v", "M2 + M1", "M2 → Étoile + M1", 7),
            ("La Défense", "la-defense", "M2 + M1", "M2 → Étoile + M1", 11),
            ("Fondation Louis Vuitton", "porte-dauphine", "Bus", "Bus 244 ou navette Fondation", 15),
            ("Concorde", "concorde", "M2 + M1", "M2 → Étoile + M1", 14)
        ]
    },
    "victor-hugo": {
        "addr": "Place Victor-Hugo, 75116 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Victor Hugo (M2) place Victor-Hugo dans le 16e arrondissement. Nommée d'après l'écrivain Victor Hugo (1802-1885), figure majeure du romantisme français.",
        "tagline": "M2 — Victor Hugo (1802-1885), écrivain romantique",
        "hero_desc": "Station <strong>Victor Hugo</strong> sur la <strong>place Victor-Hugo</strong> dans le <strong>16e arrondissement</strong>. Desservie par la <strong>ligne 2 du métro</strong>, ouverte le <strong>13 décembre 1900</strong>. Nommée d'après <strong>Victor Hugo</strong> (<strong>1802-1885</strong>), <strong>écrivain, poète et homme politique français</strong>, figure majeure du <strong>romantisme</strong>. Quartier résidentiel chic du <strong>16e</strong>.",
        "intros": [
            "La station <strong>Victor Hugo</strong> est implantée sur la <strong>place Victor-Hugo</strong> dans le <strong>16e arrondissement</strong>. Elle est desservie par la <strong>ligne 2 du métro parisien</strong>, entre <strong>Porte Dauphine</strong> (1 station) et <strong>Charles de Gaulle - Étoile</strong> (1 station). Bus 52 et 82 en correspondance.",
            "Ouverte le <strong>13 décembre 1900</strong> avec le tronçon <strong>Étoile ↔ Porte Dauphine</strong>. Particularité : ses <strong>quais sont décalés</strong> en raison de la <strong>courbure étroite</strong> de la ligne sous la place Victor-Hugo (quai direction Nation rapproché, quai direction Porte Dauphine décalé).",
            "Le nom <strong>Victor Hugo</strong> rend hommage à <strong>Victor Marie Hugo</strong> (<strong>1802-1885</strong>), <strong>écrivain, poète, dramaturge et homme politique français</strong>. Chef de file du <strong>romantisme français</strong>. Auteur des <em>Misérables</em> (1862), <em>Notre-Dame de Paris</em> (1831), <em>Les Contemplations</em> (1856). Quartier résidentiel chic du <strong>16e</strong>."
        ],
        "hist_title": "1900 : place Victor-Hugo et l'écrivain romantique",
        "hist": [
            "La station Victor Hugo est <strong>inaugurée le 13 décembre 1900</strong> avec le tronçon <strong>Étoile ↔ Porte Dauphine</strong>, prolongement de la <strong>ligne 2 Nord</strong> (devenue ligne 2 en 1907). Elle dessert la <strong>place Victor-Hugo</strong>, dans le quartier chic du <strong>Bois</strong>.",
            "Le nom <strong>Victor Hugo</strong> commémore <strong>Victor Marie Hugo</strong> (<strong>26 février 1802 - 22 mai 1885</strong>), <strong>écrivain, poète, dramaturge et homme politique français</strong>. Né à <strong>Besançon</strong>, il devient à 23 ans <strong>chef de file du romantisme</strong>. Œuvres majeures : <em>Notre-Dame de Paris</em> (1831), <em>Les Misérables</em> (1862, écrit en grande partie en exil), <em>Les Contemplations</em> (1856), <em>La Légende des siècles</em> (1859-1883).",
            "<strong>Pair de France</strong> en 1845, <strong>député républicain</strong> en 1848, il <strong>s'oppose au coup d'État du 2 décembre 1851</strong> et s'<strong>exile à Jersey puis Guernesey</strong> jusqu'en 1870. Retour triomphal après la chute du Second Empire. <strong>Funérailles nationales</strong> le <strong>1er juin 1885</strong>, deux millions de Parisiens accompagnent son cortège. <strong>Inhumé au Panthéon</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Victor Hugo ?", "Uniquement la <strong>ligne 2 du métro</strong>. Bus 52 et 82."),
            ("Qui est Victor Hugo ?", "<strong>Victor Hugo</strong> (1802-1885), <strong>écrivain, poète et homme politique français</strong>, figure majeure du <strong>romantisme</strong>. Auteur des <em>Misérables</em> et <em>Notre-Dame de Paris</em>."),
            ("Quand la station a-t-elle ouvert ?", "Le <strong>13 décembre 1900</strong>."),
            ("Pourquoi les quais sont-ils décalés ?", "À cause de la <strong>courbure étroite</strong> de la ligne 2 sous la place Victor-Hugo. Les deux quais ne sont pas alignés."),
            ("Pour les Champs-Élysées ?", "<strong>M2 vers Étoile + M1</strong> (~7 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Quais décalés</strong> en raison de la courbure de la ligne — particularité architecturale du métro.",
            "Quartier résidentiel chic du <strong>16e arrondissement</strong>.",
            "Pour l'<strong>Arc de Triomphe</strong> : <strong>M2 directe</strong> vers Étoile (1 station).",
            "Pour <strong>Trocadéro</strong> et <strong>Tour Eiffel</strong> : <strong>M2 → Étoile + M6</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("📚", "Victor Hugo, géant des lettres françaises", "<strong>Victor Marie Hugo</strong> (1802-1885), né à <strong>Besançon</strong>, devient à <strong>23 ans</strong> chef de file du <strong>romantisme français</strong>. Œuvres majeures : <em>Notre-Dame de Paris</em> (<strong>1831</strong>), <em>Les Misérables</em> (<strong>1862</strong>, écrit en grande partie en exil à Guernesey), <em>Les Contemplations</em> (1856). <strong>Député</strong> en 1848, il <strong>s'oppose à Napoléon III</strong> et s'exile à Jersey puis Guernesey (1851-1870). Funérailles nationales le 1er juin 1885, deux millions de Parisiens. <strong>Inhumé au Panthéon</strong>."),
            ("🏛️", "Place Victor-Hugo, étoile de douze avenues", "La <strong>place Victor-Hugo</strong>, sur laquelle ouvre la station, est une <strong>place en étoile</strong> d'où rayonnent <strong>douze avenues</strong>. Tracée sous Haussmann (<strong>1857</strong>), elle s'appelait initialement <strong>place du Roi-de-Rome</strong> puis place d'Eylau (1868), avant d'être <strong>renommée en hommage à Victor Hugo</strong> en <strong>1881</strong>, du vivant de l'écrivain — qui habitait alors à proximité, avenue d'Eylau (aujourd'hui avenue Victor-Hugo).")
        ],
        "itin": [
            ("Charles de Gaulle - Étoile", "charles-de-gaulle-etoile", "M2", "M2 directe (1 station)", 3),
            ("Champs-Élysées", "george-v", "M2 + M1", "M2 → Étoile + M1", 7),
            ("Tour Eiffel", "trocadero", "M2 + M6", "M2 → Étoile + M6", 14),
            ("Bois de Boulogne", "porte-dauphine", "M2", "M2 directe (1 station)", 3),
            ("Opéra Garnier", "opera", "M2 + M3", "M2 → Villiers + M3 ou via Étoile", 18),
            ("La Défense", "la-defense", "M2 + M1", "M2 → Étoile + M1", 11)
        ]
    },
    "ternes": {
        "addr": "Place des Ternes, 75017 Paris", "arr": "17e arrondissement (Paris)",
        "seo": "Station Ternes (M2) place des Ternes dans le 17e arrondissement. Quartier résidentiel chic du 17e, proche de la Salle Pleyel et du parc Monceau.",
        "tagline": "M2 — place des Ternes, quartier 17e chic",
        "hero_desc": "Station <strong>Ternes</strong> sur la <strong>place des Ternes</strong> dans le <strong>17e arrondissement</strong>. Desservie par la <strong>ligne 2 du métro</strong>, ouverte le <strong>7 octobre 1902</strong>. Située au croisement de l'<strong>avenue de Wagram</strong> et du <strong>boulevard de Courcelles</strong>. Quartier résidentiel chic du <strong>17e</strong>, proche de la <strong>salle Pleyel</strong>.",
        "intros": [
            "La station <strong>Ternes</strong> est implantée sur la <strong>place des Ternes</strong> dans le <strong>17e arrondissement</strong>. Elle est desservie par la <strong>ligne 2 du métro parisien</strong>, entre <strong>Charles de Gaulle - Étoile</strong> (1 station) et <strong>Courcelles</strong> (1 station). Bus 30, 31, 43, 93 en correspondance.",
            "Ouverte le <strong>7 octobre 1902</strong> avec le tronçon <strong>Étoile ↔ Anvers</strong> de la ligne 2 Nord (devenue ligne 2). Particularité historique : un <strong>train R</strong> y a déraillé en <strong>1903</strong> (catastrophe ferroviaire de Couronnes).",
            "Le nom <strong>Ternes</strong> vient de l'ancien <strong>village des Ternes</strong>, rattaché à Paris en <strong>1860</strong>. Quartier résidentiel chic du <strong>17e arrondissement</strong>, proche de la <strong>salle Pleyel</strong> (salle de concerts), du <strong>parc Monceau</strong> et de l'<strong>Arc de Triomphe</strong>."
        ],
        "hist_title": "1902 : Ternes et le village rattaché à Paris",
        "hist": [
            "La station Ternes est <strong>inaugurée le 7 octobre 1902</strong> avec le tronçon <strong>Étoile ↔ Anvers</strong> de la <strong>ligne 2 Nord</strong> (devenue ligne 2 en 1907). Le tronçon faisait partie du second souffle d'expansion du métropolitain après le succès de l'<strong>Exposition universelle de 1900</strong>.",
            "Le nom <strong>Ternes</strong> vient de l'ancien <strong>village des Ternes</strong>, rattaché à Paris en <strong>1860</strong> avec d'autres communes périphériques (annexion par Haussmann). L'<strong>étymologie</strong> est incertaine : du latin <em>villa externa</em> (« domaine extérieur ») selon une hypothèse, ou plus vraisemblablement du toponyme franco-celtique <em>Ternae</em>.",
            "Le quartier est aujourd'hui résidentiel chic du <strong>17e arrondissement</strong>. La <strong>place des Ternes</strong> accueille un marché aux fleurs et héberge l'entrée du <strong>marché des Ternes</strong>. À proximité : la <strong>salle Pleyel</strong> (salle de concerts inaugurée en 1927, rénovée en 2006), le <strong>parc Monceau</strong> et l'<strong>Arc de Triomphe</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Ternes ?", "Uniquement la <strong>ligne 2 du métro</strong>. Bus 30, 31, 43, 93."),
            ("Quand la station a-t-elle ouvert ?", "Le <strong>7 octobre 1902</strong>."),
            ("D'où vient le nom Ternes ?", "De l'ancien <strong>village des Ternes</strong>, rattaché à Paris en <strong>1860</strong>."),
            ("Pour la salle Pleyel ?", "<strong>~5 min à pied</strong> via la rue du Faubourg-Saint-Honoré."),
            ("Pour les Champs-Élysées ?", "<strong>M2 + M1</strong> via Charles de Gaulle - Étoile (~10 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Salle Pleyel</strong> à 5 min à pied (concerts).",
            "<strong>Marché des Ternes</strong> sur la place : marché couvert ouvert tous les jours sauf lundi.",
            "Pour <strong>Charles de Gaulle - Étoile</strong> : <strong>M2 directe</strong> (1 station).",
            "Pour <strong>Parc Monceau</strong> : <strong>M2 vers Monceau</strong> (2 stations) ou à pied (12 min).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎵", "Salle Pleyel, temple de la musique classique", "La <strong>salle Pleyel</strong>, à 5 min à pied de Ternes, est l'une des <strong>plus prestigieuses salles de concerts</strong> de Paris. Inaugurée en <strong>1927</strong> au 252 rue du Faubourg-Saint-Honoré, conçue par les architectes <strong>Aubertin, Granet et Mathon</strong>. <strong>1900 places</strong>. Acoustique exceptionnelle. Rénovée en <strong>2006</strong> après cinq ans de travaux. Accueille concerts classiques, jazz, variétés."),
            ("🏘️", "Ancien village des Ternes", "Le <strong>village des Ternes</strong>, ancien territoire rural à l'ouest de Paris, est <strong>rattaché à la capitale en 1860</strong> avec d'autres communes (Auteuil, Passy, Batignolles, Montmartre, Belleville). Cette <strong>annexion par Haussmann</strong> fait passer Paris de 12 à 20 arrondissements. Les Ternes deviennent une partie du nouveau <strong>17e arrondissement</strong>. Le quartier conserve une identité villageoise autour de la <strong>place des Ternes</strong>.")
        ],
        "itin": [
            ("Charles de Gaulle - Étoile", "charles-de-gaulle-etoile", "M2", "M2 directe (1 station)", 3),
            ("Champs-Élysées", "george-v", "M2 + M1", "M2 → Étoile + M1", 8),
            ("Salle Pleyel", "ternes", "à pied", "Faubourg Saint-Honoré (5 min)", 5),
            ("Parc Monceau", "monceau", "M2", "M2 directe (2 stations)", 5),
            ("Saint-Lazare", "saint-lazare", "M2 + M3", "M2 → Villiers + M3", 13),
            ("Opéra", "opera", "M2 + M3", "M2 → Villiers + M3", 18)
        ]
    },
    "courcelles": {
        "addr": "Boulevard de Courcelles, 75017 Paris", "arr": "17e arrondissement (Paris)",
        "seo": "Station Courcelles (M2) boulevard de Courcelles dans le 17e arrondissement. À proximité du parc Monceau et du musée Jacquemart-André.",
        "tagline": "M2 — boulevard de Courcelles, proche parc Monceau",
        "hero_desc": "Station <strong>Courcelles</strong> sur le <strong>boulevard de Courcelles</strong> dans le <strong>17e arrondissement</strong>. Desservie par la <strong>ligne 2 du métro</strong>, ouverte le <strong>7 octobre 1902</strong>. À proximité du <strong>parc Monceau</strong> et du <strong>musée Jacquemart-André</strong>. Quartier chic du <strong>17e</strong>.",
        "intros": [
            "La station <strong>Courcelles</strong> est implantée sur le <strong>boulevard de Courcelles</strong> dans le <strong>17e arrondissement</strong>. Elle est desservie par la <strong>ligne 2 du métro parisien</strong>, entre <strong>Ternes</strong> (1 station) et <strong>Monceau</strong> (1 station). Bus 30, 31, 84, 94 en correspondance.",
            "Ouverte le <strong>7 octobre 1902</strong> avec le tronçon <strong>Étoile ↔ Anvers</strong> de la ligne 2 Nord (devenue ligne 2).",
            "Le nom <strong>Courcelles</strong> vient du <strong>boulevard de Courcelles</strong>, qui rappelle l'ancien <strong>village de Courcelles</strong>, rattaché à Paris en <strong>1860</strong>. Quartier résidentiel chic du <strong>17e</strong>, à proximité du <strong>parc Monceau</strong> et du <strong>musée Jacquemart-André</strong>."
        ],
        "hist_title": "1902 : boulevard de Courcelles et ancien village",
        "hist": [
            "La station Courcelles est <strong>inaugurée le 7 octobre 1902</strong> avec le tronçon <strong>Étoile ↔ Anvers</strong> de la <strong>ligne 2 Nord</strong> (devenue ligne 2 en 1907).",
            "Le nom <strong>Courcelles</strong> vient du <strong>boulevard de Courcelles</strong>, qui rappelle l'ancien <strong>village de Courcelles</strong>. <strong>Étymologie</strong> : du latin <em>curtis</em> (« domaine ») + <em>cella</em> (« petite cellule »), suggérant un domaine agricole. Le village est <strong>rattaché à Paris en 1860</strong> avec les autres communes périphériques.",
            "Le quartier est aujourd'hui résidentiel chic du <strong>17e arrondissement</strong>, à proximité du <strong>parc Monceau</strong> (jardin à l'anglaise) et du <strong>musée Jacquemart-André</strong> (158 boulevard Haussmann) — collection d'art italien Renaissance et de peintures françaises XVIIIe."
        ],
        "faq": [
            ("Quelle ligne dessert Courcelles ?", "Uniquement la <strong>ligne 2 du métro</strong>. Bus 30, 31, 84, 94."),
            ("Quand la station a-t-elle ouvert ?", "Le <strong>7 octobre 1902</strong>."),
            ("D'où vient le nom Courcelles ?", "Du <strong>boulevard de Courcelles</strong>, rappel de l'ancien <strong>village de Courcelles</strong> rattaché à Paris en <strong>1860</strong>."),
            ("Pour le parc Monceau ?", "<strong>~5 min à pied</strong> via le boulevard, ou <strong>M2 vers Monceau</strong> (1 station)."),
            ("Pour le musée Jacquemart-André ?", "<strong>~10 min à pied</strong> via le boulevard Haussmann."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Parc Monceau</strong> à 5 min à pied : jardin à l'anglaise, rotonde de Ledoux.",
            "<strong>Musée Jacquemart-André</strong> à 10 min à pied : collection d'art italien Renaissance.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M2 + M3</strong> via Villiers.",
            "Quartier résidentiel chic du <strong>17e</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🌳", "Parc Monceau, jardin à l'anglaise du 8e", "Le <strong>parc Monceau</strong>, à 5 min à pied de Courcelles, est un <strong>jardin à l'anglaise</strong> de <strong>8,2 hectares</strong> situé dans le <strong>8e arrondissement</strong>. Créé en <strong>1769</strong> par le <strong>duc de Chartres</strong> (futur Philippe Égalité), aménagé par <strong>Carmontelle</strong> dans un style fantaisiste avec <strong>fabriques exotiques</strong> (pagode chinoise, pyramide égyptienne, temple antique). Restauré par <strong>Adolphe Alphand</strong> sous le Second Empire."),
            ("🏛️", "Musée Jacquemart-André, hôtel particulier", "Le <strong>musée Jacquemart-André</strong>, à 10 min à pied de Courcelles, est installé dans un <strong>hôtel particulier du Second Empire</strong> au 158 boulevard Haussmann. Construit pour <strong>Édouard André</strong> (1833-1894) et sa femme <strong>Nélie Jacquemart</strong>, il abrite leur <strong>collection privée d'art italien Renaissance</strong> et de peintures françaises du XVIIIe.")
        ],
        "itin": [
            ("Parc Monceau", "monceau", "M2", "M2 directe (1 station)", 3),
            ("Musée Jacquemart-André", "miromesnil", "M2 + M3", "À pied (10 min) ou M2 + M3", 10),
            ("Saint-Lazare", "saint-lazare", "M2 + M3", "M2 → Villiers + M3", 12),
            ("Charles de Gaulle - Étoile", "charles-de-gaulle-etoile", "M2", "M2 directe (2 stations)", 5),
            ("Champs-Élysées", "george-v", "M2 + M1", "M2 → Étoile + M1", 10),
            ("Opéra", "opera", "M2 + M3", "M2 → Villiers + M3", 16)
        ]
    },
    "monceau": {
        "addr": "Boulevard de Courcelles, 75008 Paris", "arr": "8e arrondissement (Paris)",
        "seo": "Station Monceau (M2) à l'entrée du parc Monceau dans le 8e arrondissement. Proche musée Nissim de Camondo et musée Cernuschi.",
        "tagline": "M2 — entrée du parc Monceau, musées de la plaine",
        "hero_desc": "Station <strong>Monceau</strong> à l'<strong>entrée nord du parc Monceau</strong> dans le <strong>8e arrondissement</strong>. Desservie par la <strong>ligne 2 du métro</strong>, ouverte le <strong>7 octobre 1902</strong>. <strong>Parc Monceau</strong> (8,2 ha) à la sortie. Proche du <strong>musée Nissim de Camondo</strong> et du <strong>musée Cernuschi</strong>. Quartier chic du <strong>8e</strong>.",
        "intros": [
            "La station <strong>Monceau</strong> est implantée sur le <strong>boulevard de Courcelles</strong>, juste à l'<strong>entrée nord du parc Monceau</strong>, dans le <strong>8e arrondissement</strong>. Elle est desservie par la <strong>ligne 2 du métro parisien</strong>, entre <strong>Courcelles</strong> (1 station) et <strong>Villiers</strong> (1 station). Bus 30, 84, 94 en correspondance.",
            "Ouverte le <strong>7 octobre 1902</strong> avec le tronçon <strong>Étoile ↔ Anvers</strong> de la ligne 2 Nord (devenue ligne 2).",
            "Le <strong>parc Monceau</strong> est un <strong>jardin à l'anglaise</strong> de <strong>8,2 hectares</strong> créé en <strong>1769</strong> par le <strong>duc de Chartres</strong>, aménagé par <strong>Carmontelle</strong>. Il accueille des <strong>fabriques exotiques</strong> (pagode chinoise, pyramide, temple antique). À proximité : le <strong>musée Nissim de Camondo</strong> (arts décoratifs XVIIIe), le <strong>musée Cernuschi</strong> (arts asiatiques)."
        ],
        "hist_title": "1902 : entrée du parc Monceau et jardin à l'anglaise",
        "hist": [
            "La station Monceau est <strong>inaugurée le 7 octobre 1902</strong> avec le tronçon <strong>Étoile ↔ Anvers</strong> de la <strong>ligne 2 Nord</strong> (devenue ligne 2 en 1907).",
            "Le <strong>parc Monceau</strong>, créé en <strong>1769</strong> par <strong>Louis-Philippe d'Orléans, duc de Chartres</strong> (futur <strong>Philippe Égalité</strong>), est un <strong>jardin à l'anglaise</strong> aménagé par le peintre <strong>Carmontelle</strong>. Il proposait un parcours initiatique avec des <strong>fabriques exotiques</strong> : <strong>pyramide égyptienne</strong>, <strong>pagode chinoise</strong>, <strong>moulin à vent hollandais</strong>, <strong>temple antique</strong>, <strong>colonnade corinthienne</strong>. <strong>Restauré sous le Second Empire</strong> par <strong>Adolphe Alphand</strong>.",
            "Le quartier autour de la station est marqué par les <strong>hôtels particuliers</strong> du <strong>Second Empire</strong>. À proximité : le <strong>musée Nissim de Camondo</strong> (63 rue de Monceau, arts décoratifs français XVIIIe), le <strong>musée Cernuschi</strong> (7 avenue Vélasquez, arts asiatiques)."
        ],
        "faq": [
            ("Quelle ligne dessert Monceau ?", "Uniquement la <strong>ligne 2 du métro</strong>. Bus 30, 84, 94."),
            ("Quand la station a-t-elle ouvert ?", "Le <strong>7 octobre 1902</strong>."),
            ("Pour le parc Monceau ?", "<strong>Sortie directe</strong>. Entrée nord du parc."),
            ("Pour le musée Nissim de Camondo ?", "<strong>~5 min à pied</strong> via la rue de Monceau."),
            ("Pour le musée Cernuschi ?", "<strong>~5 min à pied</strong> via l'avenue Vélasquez."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Parc Monceau</strong> à la sortie : jardin à l'anglaise, rotonde de Ledoux, colonnade.",
            "<strong>Musée Nissim de Camondo</strong> à 5 min : arts décoratifs français XVIIIe.",
            "<strong>Musée Cernuschi</strong> à 5 min : arts asiatiques.",
            "Quartier des <strong>hôtels particuliers</strong> du Second Empire.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Carmontelle et les fabriques exotiques", "Le <strong>parc Monceau</strong> a été conçu en <strong>1769</strong> par le peintre et écrivain <strong>Louis Carrogis dit Carmontelle</strong> (1717-1806) pour le <strong>duc de Chartres</strong>. Il intégrait un <strong>parcours initiatique</strong> avec des <strong>fabriques exotiques</strong> : <strong>pyramide égyptienne</strong>, <strong>pagode chinoise</strong>, <strong>moulin à vent hollandais</strong>, <strong>temple antique</strong>, <strong>colonnade corinthienne</strong> (Naumachie). Certaines de ces fabriques subsistent."),
            ("🏛️", "Musée Nissim de Camondo, hôtel particulier", "Le <strong>musée Nissim de Camondo</strong> est installé dans un <strong>hôtel particulier</strong> du 63 rue de Monceau, construit en <strong>1911-1914</strong> pour le <strong>comte Moïse de Camondo</strong>. Il abrite sa <strong>collection d'arts décoratifs français du XVIIIe siècle</strong>. Le musée porte le nom de son fils <strong>Nissim</strong>, tué pendant la Première Guerre mondiale. Toute la famille Camondo a été <strong>déportée et exterminée à Auschwitz</strong>.")
        ],
        "itin": [
            ("Parc Monceau", "monceau", "à pied", "Sortie directe", 1),
            ("Musée Nissim de Camondo", "monceau", "à pied", "Rue de Monceau (5 min)", 5),
            ("Musée Cernuschi", "monceau", "à pied", "Avenue Vélasquez (5 min)", 5),
            ("Saint-Lazare", "saint-lazare", "M2 + M3", "M2 → Villiers + M3", 10),
            ("Charles de Gaulle - Étoile", "charles-de-gaulle-etoile", "M2", "M2 directe (3 stations)", 7),
            ("Opéra", "opera", "M2 + M3", "M2 → Villiers + M3", 14)
        ]
    },
    "villiers": {
        "addr": "Boulevard de Courcelles, 75008 Paris", "arr": "17e arrondissement (Paris)",
        "seo": "Station Villiers (M2+M3) place de Villiers. Hub des 17e/8e arrondissements. Proche du parc Monceau et du musée Cernuschi.",
        "tagline": "M2 + M3 — place de Villiers, hub 17e/8e",
        "hero_desc": "Station <strong>Villiers</strong>, hub <strong>M2 + M3</strong>, <strong>place de Villiers</strong>, à la limite des <strong>17e et 8e arrondissements</strong>. Quais <strong>M2</strong> ouverts le <strong>7 octobre 1902</strong>, quais <strong>M3</strong> le <strong>19 octobre 1904</strong>. Proche du <strong>parc Monceau</strong> et du <strong>musée Cernuschi</strong>.",
        "intros": [
            "La station <strong>Villiers</strong> est implantée <strong>place de Villiers</strong>, à la jonction des <strong>17e et 8e arrondissements</strong>. Elle est desservie par les <strong>lignes 2 et 3</strong> du métro parisien, formant un <strong>hub de correspondance</strong>. Bus 30, 53, 94 en correspondance.",
            "Quais <strong>ligne 2</strong> ouverts le <strong>7 octobre 1902</strong> (tronçon Étoile ↔ Anvers), quais <strong>ligne 3</strong> ouverts le <strong>19 octobre 1904</strong> (tronçon Père Lachaise ↔ Villiers, devenu plus tard Champerret).",
            "Le nom <strong>Villiers</strong> vient de la <strong>place de Villiers</strong>, qui rappelle l'ancien <strong>village de Villiers</strong>, intégré aux <strong>Batignolles</strong>, commune rattachée à Paris en <strong>1860</strong>. À proximité : <strong>parc Monceau</strong>, <strong>musée Cernuschi</strong>, <strong>musée Nissim de Camondo</strong>."
        ],
        "hist_title": "1902-1904 : hub M2/M3 et ancien village",
        "hist": [
            "Les quais <strong>ligne 2</strong> sont <strong>inaugurés le 7 octobre 1902</strong> avec le tronçon <strong>Étoile ↔ Anvers</strong>. Les quais <strong>ligne 3</strong> ouvrent le <strong>19 octobre 1904</strong> avec le tronçon <strong>Père Lachaise ↔ Villiers</strong> (initial terminus ouest, prolongé ensuite vers Pereire et Pont de Levallois).",
            "Le nom <strong>Villiers</strong> vient de la <strong>place de Villiers</strong>, qui rappelle l'ancien <strong>hameau de Villiers</strong>, intégré aux <strong>Batignolles</strong>, commune rattachée à Paris en <strong>1860</strong>. <strong>Étymologie</strong> : <em>villare</em> (latin), « petit domaine ».",
            "La station est un <strong>hub de correspondance</strong> stratégique entre les <strong>16e/17e (M2)</strong> et le <strong>réseau M3</strong> qui rejoint Saint-Lazare, Opéra, République et Père Lachaise. À proximité : <strong>parc Monceau</strong>, <strong>musée Cernuschi</strong> (arts asiatiques), <strong>musée Nissim de Camondo</strong>."
        ],
        "faq": [
            ("Quelles lignes desservent Villiers ?", "<strong>M2</strong> (1902) et <strong>M3</strong> (1904). Bus 30, 53, 94. Hub à la limite 17e/8e."),
            ("Quand a-t-elle ouvert ?", "Quais M2 : <strong>7 octobre 1902</strong>. Quais M3 : <strong>19 octobre 1904</strong>."),
            ("Pour le parc Monceau ?", "<strong>~5 min à pied</strong> via le boulevard de Courcelles."),
            ("Pour Saint-Lazare ?", "<strong>M3 directe</strong> (3 stations, ~7 min)."),
            ("Pour Opéra ?", "<strong>M3 directe</strong> (4 stations, ~9 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "Hub <strong>M2 + M3</strong> stratégique 17e/8e.",
            "<strong>Parc Monceau</strong> à 5 min à pied.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M3 directe</strong> (~7 min).",
            "Pour <strong>Opéra</strong> : <strong>M3 directe</strong> (~9 min).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏘️", "Ancien hameau de Villiers", "<strong>Villiers</strong> tire son nom d'un <strong>ancien hameau</strong> de la commune des <strong>Batignolles</strong>, rattachée à Paris en <strong>1860</strong>. L'<strong>étymologie</strong> vient du latin <em>villare</em> (« petit domaine »), désignant une petite exploitation agricole. La <strong>place de Villiers</strong> conserve la mémoire de ce hameau."),
            ("🏛️", "Musée Cernuschi, arts asiatiques", "Le <strong>musée Cernuschi</strong>, à 5 min à pied de Villiers (7 avenue Vélasquez), abrite la <strong>collection d'arts asiatiques</strong> de <strong>Henri Cernuschi</strong> (1821-1896), banquier italien réfugié à Paris. Installé dans son <strong>hôtel particulier</strong> construit pour abriter ses collections rapportées d'un voyage en Asie (1871-1873). <strong>15 000 œuvres</strong> de Chine, Japon, Corée, Vietnam.")
        ],
        "itin": [
            ("Parc Monceau", "monceau", "M2", "M2 directe (1 station)", 3),
            ("Saint-Lazare", "saint-lazare", "M3", "M3 directe (3 stations)", 7),
            ("Opéra Garnier", "opera", "M3", "M3 directe (4 stations)", 9),
            ("République", "republique", "M3", "M3 directe (7 stations)", 14),
            ("Père Lachaise", "pere-lachaise", "M2 ou M3", "M2 ou M3 directes", 18),
            ("Charles de Gaulle - Étoile", "charles-de-gaulle-etoile", "M2", "M2 directe (4 stations)", 9)
        ]
    },
    "rome": {
        "addr": "Place de Dublin, 75008 Paris", "arr": "8e arrondissement (Paris)",
        "seo": "Station Rome (M2) rue de Rome dans le 8e arrondissement. Quartier de l'Europe (rues nommées d'après les capitales). Proche du parc Monceau et de Saint-Lazare.",
        "tagline": "M2 — rue de Rome, quartier de l'Europe",
        "hero_desc": "Station <strong>Rome</strong> sur la <strong>rue de Rome</strong> dans le <strong>8e arrondissement</strong>. Desservie par la <strong>ligne 2 du métro</strong>, ouverte le <strong>7 octobre 1902</strong>. Située dans le <strong>quartier de l'Europe</strong>, où les rues portent les noms des <strong>capitales européennes</strong>. Proche de la <strong>gare Saint-Lazare</strong> et du <strong>parc Monceau</strong>.",
        "intros": [
            "La station <strong>Rome</strong> est implantée sur la <strong>rue de Rome</strong>, dans le <strong>quartier de l'Europe</strong> (8e arrondissement). Elle est desservie par la <strong>ligne 2 du métro parisien</strong>, entre <strong>Villiers</strong> (1 station) et <strong>Place de Clichy</strong> (1 station). Bus 53, 81, 94 en correspondance.",
            "Ouverte le <strong>7 octobre 1902</strong> avec le tronçon <strong>Étoile ↔ Anvers</strong> de la ligne 2 Nord (devenue ligne 2).",
            "Le <strong>quartier de l'Europe</strong> est un secteur du <strong>8e arrondissement</strong> où toutes les rues portent les noms de <strong>capitales européennes</strong> (Rome, Madrid, Naples, Vienne, Berlin, Saint-Pétersbourg, Londres). Aménagé sous le <strong>Second Empire</strong>, il convergeait vers la <strong>gare Saint-Lazare</strong>, point névralgique du réseau ferré français."
        ],
        "hist_title": "1902 : rue de Rome et quartier de l'Europe",
        "hist": [
            "La station Rome est <strong>inaugurée le 7 octobre 1902</strong> avec le tronçon <strong>Étoile ↔ Anvers</strong> de la <strong>ligne 2 Nord</strong> (devenue ligne 2 en 1907).",
            "Le <strong>quartier de l'Europe</strong>, dans le <strong>8e arrondissement</strong>, doit son nom à la disposition de ses rues nommées d'après les <strong>capitales européennes</strong> : <strong>rue de Rome</strong>, <strong>rue de Madrid</strong>, <strong>rue de Naples</strong>, <strong>rue de Vienne</strong>, <strong>rue de Berlin</strong> (renommée rue de Liège en 1914 après la Première Guerre mondiale), <strong>rue de Saint-Pétersbourg</strong>, <strong>rue de Londres</strong>. Le quartier a été aménagé sous le <strong>Second Empire</strong>.",
            "La <strong>rue de Rome</strong>, longue de <strong>1,1 km</strong>, longe les <strong>voies ferrées de la gare Saint-Lazare</strong>. Elle est connue pour ses <strong>nombreux magasins de musique</strong> (instruments, partitions), regroupés depuis la fin du XIXe siècle (proximité du <strong>conservatoire</strong>). Stéphane Mallarmé y vécut au <strong>89 rue de Rome</strong> (1875-1898) et y tint son célèbre <strong>« mardi de Mallarmé »</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Rome ?", "Uniquement la <strong>ligne 2 du métro</strong>. Bus 53, 81, 94."),
            ("Quand la station a-t-elle ouvert ?", "Le <strong>7 octobre 1902</strong>."),
            ("Qu'est-ce que le quartier de l'Europe ?", "Un quartier du <strong>8e arrondissement</strong> où les rues portent les noms des <strong>capitales européennes</strong> (Rome, Madrid, Naples, Vienne, etc.)."),
            ("Pourquoi la rue de Rome est-elle dédiée à la musique ?", "Concentration historique de <strong>magasins d'instruments</strong> et de <strong>partitions</strong> depuis la fin du XIXe siècle, en raison de la proximité du <strong>conservatoire</strong>."),
            ("Pour Saint-Lazare ?", "<strong>~7 min à pied</strong> via la rue de Rome."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Rue de Rome</strong> connue pour ses <strong>magasins de musique</strong> (instruments, partitions).",
            "<strong>Gare Saint-Lazare</strong> à 7 min à pied.",
            "<strong>Quartier de l'Europe</strong> : rues nommées d'après les capitales.",
            "Pour <strong>Place de Clichy</strong> (M2+M13) : <strong>M2 directe</strong> (1 station).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎵", "Rue de Rome, temple parisien de la musique", "La <strong>rue de Rome</strong> est connue depuis la fin du XIXe siècle pour sa <strong>concentration de magasins d'instruments de musique</strong> et de <strong>partitions</strong>. Cette tradition s'explique par la <strong>proximité du Conservatoire</strong> (ancien siège place du Père-Teilhard-de-Chardin, dans le 8e) et de la <strong>gare Saint-Lazare</strong>, point de passage des musiciens de province. Plusieurs <strong>luthiers historiques</strong> y subsistent encore."),
            ("✍️", "Stéphane Mallarmé, 89 rue de Rome", "<strong>Stéphane Mallarmé</strong> (1842-1898), <strong>poète symboliste français</strong>, a vécu au <strong>89 rue de Rome</strong> de <strong>1875 à 1898</strong>. Tous les <strong>mardis soir</strong>, il y tenait le célèbre <strong>« mardi de Mallarmé »</strong>, salon littéraire qui réunissait l'élite des lettres et des arts symbolistes : <strong>Verlaine, Valéry, Gide, Rodin, Whistler, Manet, Debussy</strong>. Œuvres : <em>L'Après-midi d'un faune</em> (1876), <em>Un coup de dés jamais n'abolira le hasard</em> (1897).")
        ],
        "itin": [
            ("Saint-Lazare", "saint-lazare", "à pied", "Rue de Rome (7 min)", 7),
            ("Place de Clichy", "place-de-clichy", "M2", "M2 directe (1 station)", 3),
            ("Parc Monceau", "monceau", "M2", "M2 directe (2 stations)", 5),
            ("Opéra", "opera", "M2 + M3", "M2 → Villiers + M3", 12),
            ("Charles de Gaulle - Étoile", "charles-de-gaulle-etoile", "M2", "M2 directe (5 stations)", 11),
            ("Pigalle", "pigalle", "M2", "M2 directe (3 stations)", 7)
        ]
    },
    "place-de-clichy": {
        "addr": "Place de Clichy, 75009 Paris", "arr": "9e arrondissement (Paris)",
        "seo": "Station Place de Clichy (M2+M13) place de Clichy. Hub à la limite des 8e, 9e, 17e et 18e. Cinéma Pathé Wepler, statue Maréchal Moncey.",
        "tagline": "M2 + M13 — statue maréchal Moncey, cinéma Pathé Wepler",
        "hero_desc": "Station <strong>Place de Clichy</strong>, hub <strong>M2 + M13</strong>, place de Clichy, à la limite des <strong>8e, 9e, 17e et 18e arrondissements</strong>. Quais <strong>M2</strong> ouverts le <strong>7 octobre 1902</strong>, quais <strong>M13</strong> le <strong>26 février 1911</strong>. Au centre de la place : <strong>statue du Maréchal Moncey</strong> (1869). Cinéma <strong>Pathé Wepler</strong>.",
        "intros": [
            "La station <strong>Place de Clichy</strong> est implantée <strong>place de Clichy</strong>, au croisement de <strong>quatre arrondissements</strong> (8e, 9e, 17e, 18e). Elle est desservie par les <strong>lignes 2 et 13</strong> du métro parisien, formant un <strong>hub majeur</strong>. Bus 30, 54, 68, 74, 80, 81, 95 en correspondance.",
            "Quais <strong>ligne 2</strong> ouverts le <strong>7 octobre 1902</strong> (tronçon Étoile ↔ Anvers), quais <strong>ligne 13</strong> (anciennement ligne B du Nord-Sud) ouverts le <strong>26 février 1911</strong>.",
            "Au centre de la place se dresse la <strong>statue du Maréchal Moncey</strong>, érigée en <strong>1869</strong> en hommage au <strong>maréchal Bon-Adrien Jeannot de Moncey</strong> (<strong>1754-1842</strong>), qui défendit Paris lors de la <strong>bataille de Paris</strong> (30 mars 1814) à la <strong>barrière de Clichy</strong>. Le cinéma <strong>Pathé Wepler</strong> domine la place."
        ],
        "hist_title": "1902-1911 : hub M2/M13 et maréchal Moncey",
        "hist": [
            "Les quais <strong>ligne 2</strong> sont <strong>inaugurés le 7 octobre 1902</strong> avec le tronçon <strong>Étoile ↔ Anvers</strong>. Les quais <strong>ligne 13</strong> ouvrent le <strong>26 février 1911</strong> avec la <strong>ligne B du Nord-Sud</strong> (compagnie privée fusionnée avec la CMP en 1930, ligne devenue M13 en 1942).",
            "La <strong>place de Clichy</strong> tire son nom de l'ancienne <strong>barrière de Clichy</strong>, l'une des <strong>portes d'octroi</strong> du <strong>mur des Fermiers généraux</strong> (1784-1860). C'est ici que le <strong>30 mars 1814</strong>, lors de la <strong>bataille de Paris</strong>, le <strong>maréchal Bon-Adrien Jeannot de Moncey</strong> (<strong>1754-1842</strong>) <strong>défendit héroïquement la barrière</strong> contre les Russes et les Prussiens.",
            "La <strong>statue du Maréchal Moncey</strong>, érigée en <strong>1869</strong>, lui rend hommage au centre de la place. Œuvre du sculpteur <strong>Amédée Doublemard</strong>. Le cinéma <strong>Pathé Wepler</strong> (anciennement <strong>cinéma Wepler</strong>, ouvert en 1909) domine la place. La place est aussi un haut lieu de la <strong>fête de la Saint-Jean</strong> et des manifestations parisiennes."
        ],
        "faq": [
            ("Quelles lignes desservent Place de Clichy ?", "<strong>M2</strong> (1902) et <strong>M13</strong> (1911). Bus 30, 54, 68, 74, 80, 81, 95. Hub des 4 arrondissements (8e, 9e, 17e, 18e)."),
            ("Quand a-t-elle ouvert ?", "Quais M2 : <strong>7 octobre 1902</strong>. Quais M13 : <strong>26 février 1911</strong>."),
            ("Qui est le maréchal Moncey ?", "<strong>Bon-Adrien Jeannot de Moncey</strong> (1754-1842), <strong>maréchal d'Empire</strong>. Défendit héroïquement la <strong>barrière de Clichy</strong> contre les Russes et Prussiens le <strong>30 mars 1814</strong>."),
            ("Pour Saint-Lazare ?", "<strong>M13 directe</strong> (2 stations, ~5 min)."),
            ("Pour Pigalle ?", "<strong>M2 directe</strong> (2 stations, ~4 min)."),
            ("Pour Montmartre ?", "<strong>M2 → Anvers</strong> (3 stations) ou M2/M13 puis funiculaire.")
        ],
        "tips": [
            "<strong>Statue du Maréchal Moncey</strong> (1869) au centre de la place.",
            "<strong>Cinéma Pathé Wepler</strong> sur la place (multiplexe).",
            "Hub <strong>M2 + M13</strong> à la jonction de 4 arrondissements.",
            "Pour <strong>Montmartre</strong> : <strong>M2 vers Anvers</strong> ou <strong>M13 vers Saint-Lazare</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⚔️", "Maréchal Moncey défend la barrière de Clichy (1814)", "<strong>Bon-Adrien Jeannot de Moncey</strong> (1754-1842), <strong>maréchal d'Empire</strong>. À la fin de l'Empire, alors que les <strong>Russes et Prussiens</strong> approchent de Paris, il <strong>défend héroïquement la barrière de Clichy</strong> le <strong>30 mars 1814</strong>. Bien que finalement contraint à la capitulation, sa résistance fait de lui un héros parisien. La <strong>statue</strong> au centre de la place (œuvre d'<strong>Amédée Doublemard</strong>) lui rend hommage depuis <strong>1869</strong>."),
            ("🎬", "Cinéma Pathé Wepler depuis 1909", "Le <strong>cinéma Wepler</strong>, sur la place de Clichy, est l'un des <strong>plus anciens cinémas parisiens encore en activité</strong>. Ouvert en <strong>1909</strong>, il abrite aujourd'hui un <strong>multiplexe Pathé</strong> de <strong>14 salles</strong>. Il fait face à la <strong>brasserie Wepler</strong> (1810), célèbre <strong>brasserie historique parisienne</strong> qui inspira <strong>Henry Miller</strong> dans <em>Jours tranquilles à Clichy</em>.")
        ],
        "itin": [
            ("Saint-Lazare", "saint-lazare", "M13", "M13 directe (2 stations)", 5),
            ("Pigalle", "pigalle", "M2", "M2 directe (2 stations)", 4),
            ("Montmartre via Anvers", "anvers", "M2", "M2 directe (3 stations)", 6),
            ("Montmartre via Lamarck", "lamarck-caulaincourt", "M13 + M12", "M13 → Saint-Lazare + M12", 14),
            ("Opéra", "opera", "M13 + M3", "M13 → Liège + M3 ou via Saint-Lazare", 10),
            ("Châtelet", "chatelet", "M13 + M4 ou M14", "M13 → Saint-Lazare + M14", 14)
        ]
    },
    "blanche": {
        "addr": "Boulevard de Clichy, 75009 Paris", "arr": "9e arrondissement (Paris)",
        "seo": "Station Blanche (M2) place Blanche dans le 9e arrondissement. À deux pas du Moulin Rouge, cabaret emblématique de Pigalle.",
        "tagline": "M2 — place Blanche, sortie Moulin Rouge",
        "hero_desc": "Station <strong>Blanche</strong>, <strong>place Blanche</strong>, sur le <strong>boulevard de Clichy</strong> dans le <strong>9e arrondissement</strong>. Desservie par la <strong>ligne 2 du métro</strong>, ouverte le <strong>21 octobre 1902</strong>. À deux pas du <strong>Moulin Rouge</strong> (face à la sortie), cabaret emblématique de <strong>Pigalle</strong> fondé en <strong>1889</strong>.",
        "intros": [
            "La station <strong>Blanche</strong> est implantée sur le <strong>boulevard de Clichy</strong>, <strong>place Blanche</strong>, dans le <strong>9e arrondissement</strong>. Elle est desservie par la <strong>ligne 2 du métro parisien</strong>, entre <strong>Place de Clichy</strong> (1 station) et <strong>Pigalle</strong> (1 station). Bus 30 et 54 en correspondance.",
            "Ouverte le <strong>21 octobre 1902</strong>, simultanément au prolongement <strong>Anvers → Bagnolet</strong> (devenu Alexandre Dumas). En face de la sortie : le <strong>Moulin Rouge</strong>, cabaret mythique ouvert en <strong>1889</strong>, célèbre dans le monde entier pour son <strong>French Cancan</strong>.",
            "Le nom <strong>Blanche</strong> vient de la <strong>place Blanche</strong>, qui doit son nom à la <strong>blancheur</strong> du <strong>plâtre</strong> transporté par les charrois descendant des <strong>carrières de plâtre de Montmartre</strong> au XVIIIe siècle. Cœur du <strong>quartier Pigalle</strong>, secteur historique du <strong>cabaret parisien</strong>."
        ],
        "hist_title": "1902 : place Blanche et le Moulin Rouge",
        "hist": [
            "La station Blanche est <strong>inaugurée le 21 octobre 1902</strong> avec le prolongement <strong>Anvers ↔ Bagnolet</strong> de la <strong>ligne 2 Nord</strong> (devenue ligne 2 en 1907).",
            "Le nom <strong>place Blanche</strong> rappelle la <strong>blancheur</strong> du <strong>plâtre</strong> transporté par les charrettes descendant des <strong>carrières de plâtre de Montmartre</strong> au <strong>XVIIIe siècle</strong>. Cœur du <strong>quartier Pigalle</strong>.",
            "Le <strong>Moulin Rouge</strong>, face à la sortie, est ouvert le <strong>6 octobre 1889</strong> par <strong>Joseph Oller</strong> et <strong>Charles Zidler</strong>. Cabaret-music hall emblématique, célèbre pour son <strong>French Cancan</strong> et ses <strong>spectacles de revue</strong>. Immortalisé par les affiches d'<strong>Henri de Toulouse-Lautrec</strong> et la chanson d'<strong>Edith Piaf</strong>. Reconnaissable à son <strong>moulin rouge</strong> emblématique sur la façade. Détruit par un incendie en 1915, reconstruit, il continue de programmer des revues."
        ],
        "faq": [
            ("Quelle ligne dessert Blanche ?", "Uniquement la <strong>ligne 2 du métro</strong>. Bus 30 et 54."),
            ("Pour le Moulin Rouge ?", "<strong>Sortie directe</strong>. Cabaret face à la sortie de la station."),
            ("Quand a-t-elle ouvert ?", "Le <strong>21 octobre 1902</strong>."),
            ("Pourquoi place Blanche ?", "À cause de la <strong>blancheur du plâtre</strong> qui descendait des <strong>carrières de Montmartre</strong> au XVIIIe siècle."),
            ("Pour Montmartre ?", "<strong>~10 min à pied</strong> via la rue Lepic, ou <strong>M2 → Anvers</strong> + funiculaire."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Moulin Rouge</strong> face à la sortie : cabaret historique (1889), revues quotidiennes.",
            "<strong>Rue Lepic</strong> (à 2 min) : rue commerçante pittoresque montant vers Montmartre.",
            "Cœur du <strong>quartier Pigalle</strong> : cabarets, théâtres, vie nocturne.",
            "Pour <strong>Montmartre Sacré-Cœur</strong> : <strong>M2 → Anvers</strong> + funiculaire.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🌹", "Moulin Rouge depuis 1889", "Le <strong>Moulin Rouge</strong>, ouvert le <strong>6 octobre 1889</strong> par <strong>Joseph Oller</strong> et <strong>Charles Zidler</strong>, est le <strong>cabaret le plus célèbre au monde</strong>. Berceau du <strong>French Cancan</strong>, immortalisé par les <strong>affiches d'Henri de Toulouse-Lautrec</strong> et la chanson <em>Le Moulin Rouge</em> d'<strong>Edith Piaf</strong>. Reconnaissable à son <strong>moulin rouge</strong> emblématique. <strong>Incendié en 1915</strong>, reconstruit. Continue de programmer des <strong>revues spectaculaires</strong> (<em>Féerie</em> depuis 1999)."),
            ("🎨", "Toulouse-Lautrec et les affiches Pigalle", "<strong>Henri de Toulouse-Lautrec</strong> (1864-1901), peintre <strong>post-impressionniste</strong>, a immortalisé le <strong>cabaret du Moulin Rouge</strong> dès son ouverture en 1889. Ses <strong>affiches lithographiques</strong> révolutionnaires (1891-1900), aux <strong>aplats de couleurs vives</strong> et au <strong>cadrage cinématographique</strong>, sont considérées comme <strong>fondatrices de l'art de l'affiche moderne</strong>. <em>La Goulue au Moulin Rouge</em> (1891), <em>Jane Avril</em> (1893), <em>Aristide Bruant</em> (1893).")
        ],
        "itin": [
            ("Moulin Rouge", "blanche", "à pied", "Sortie directe", 1),
            ("Pigalle", "pigalle", "M2", "M2 directe (1 station)", 2),
            ("Montmartre Sacré-Cœur", "anvers", "M2 + funiculaire", "M2 → Anvers + funiculaire", 12),
            ("Place de Clichy", "place-de-clichy", "M2", "M2 directe (1 station)", 3),
            ("Opéra Garnier", "opera", "M2 + M3 + M14", "M2 → Pigalle + M12", 12),
            ("Saint-Lazare", "saint-lazare", "M2 + M13", "M2 → Place de Clichy + M13", 8)
        ]
    },
    "la-chapelle": {
        "addr": "Boulevard de la Chapelle, 75010 Paris", "arr": "10e arrondissement (Paris)",
        "seo": "Station La Chapelle (M2) aérienne boulevard de la Chapelle, à proximité de la gare du Nord. Quartier multi-ethnique du 10e/18e arrondissement.",
        "tagline": "M2 — aérienne, gare du Nord et 10e/18e",
        "hero_desc": "Station <strong>La Chapelle</strong>, <strong>aérienne</strong>, sur le <strong>boulevard de la Chapelle</strong>, à la limite des <strong>10e et 18e arrondissements</strong>. Desservie par la <strong>ligne 2 du métro</strong>, ouverte le <strong>31 janvier 1903</strong>. À <strong>5 min à pied de la gare du Nord</strong>. Quartier <strong>multi-ethnique</strong> animé.",
        "intros": [
            "La station <strong>La Chapelle</strong> est implantée sur le <strong>boulevard de la Chapelle</strong>, à la limite des <strong>10e et 18e arrondissements</strong>. Elle est desservie par la <strong>ligne 2 du métro parisien</strong>, entre <strong>Barbès - Rochechouart</strong> (1 station) et <strong>Stalingrad</strong> (1 station). Bus 35, 65, 302 en correspondance.",
            "Station <strong>aérienne</strong> sur le viaduc de la ligne 2, ouverte le <strong>31 janvier 1903</strong> avec le prolongement Anvers ↔ Bagnolet. À <strong>5 min à pied de la gare du Nord</strong> (RER B, D, E ; Eurostar, Thalys).",
            "Le nom <strong>La Chapelle</strong> rappelle l'ancien <strong>village de La Chapelle-Saint-Denis</strong>, rattaché à Paris en <strong>1860</strong>. Quartier <strong>multi-ethnique</strong> animé : <strong>Tamouls, Sri Lankais, Pakistanais, Bangladais, Africains</strong>. Marché de la rue Marx-Dormoy. À proximité : <strong>rue du Faubourg-Saint-Denis</strong> et son <strong>Petit Inde</strong>."
        ],
        "hist_title": "1903 : aérienne et village de La Chapelle",
        "hist": [
            "La station La Chapelle est <strong>inaugurée le 31 janvier 1903</strong> avec le prolongement <strong>Anvers ↔ Bagnolet</strong> de la <strong>ligne 2 Nord</strong> (devenue ligne 2 en 1907). Station <strong>aérienne</strong> sur le viaduc.",
            "Le nom <strong>La Chapelle</strong> rappelle l'ancien <strong>village de La Chapelle-Saint-Denis</strong>, l'un des plus anciens des environs de Paris (mentionné dès le <strong>VIIe siècle</strong>). Étymologie : du latin <em>capella</em> (« petite chapelle »), désignant un <strong>oratoire dédié à saint Denis</strong>, premier évêque de Paris martyr (IIIe siècle). Rattaché à Paris en <strong>1860</strong> avec d'autres communes périphériques.",
            "Le quartier est aujourd'hui <strong>multi-ethnique animé</strong> : <strong>Tamouls, Sri Lankais</strong> (rue du Faubourg-Saint-Denis, « Petit Inde »), <strong>Pakistanais et Bangladais</strong> (passage Brady), <strong>Africains</strong>. Marché alimentaire <strong>rue Marx-Dormoy</strong>. À <strong>5 min à pied de la gare du Nord</strong>, point de départ vers le nord de l'Europe (Eurostar Londres, Thalys Bruxelles/Amsterdam)."
        ],
        "faq": [
            ("Quelle ligne dessert La Chapelle ?", "Uniquement la <strong>ligne 2 du métro</strong>. Bus 35, 65, 302."),
            ("La Chapelle est-elle aérienne ?", "<strong>Oui</strong>. Station aérienne sur le viaduc de la ligne 2, boulevard de la Chapelle."),
            ("Quand a-t-elle ouvert ?", "Le <strong>31 janvier 1903</strong>."),
            ("Pour la gare du Nord ?", "<strong>~5 min à pied</strong> via la rue Marx-Dormoy."),
            ("Pour l'Eurostar Londres ?", "<strong>Gare du Nord à 5 min à pied</strong>, terminal Eurostar."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station aérienne ancienne (1903), pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Gare du Nord</strong> à 5 min à pied : RER B, D, E + Eurostar + Thalys.",
            "<strong>Quartier multi-ethnique</strong> : « <strong>Petit Inde</strong> » rue du Faubourg-Saint-Denis.",
            "<strong>Marché Marx-Dormoy</strong> à proximité.",
            "Pour <strong>Stalingrad</strong> et <strong>canal de l'Ourcq</strong> : <strong>M2 directe</strong> (1 station).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "La Chapelle-Saint-Denis, village millénaire", "Le <strong>village de La Chapelle-Saint-Denis</strong> est l'un des <strong>plus anciens des environs de Paris</strong>, mentionné dès le <strong>VIIe siècle</strong>. Son nom vient du latin <em>capella</em> (« petite chapelle »), désignant un <strong>oratoire dédié à saint Denis</strong>, premier évêque de Paris martyr (IIIe siècle). Le village a été <strong>rattaché à Paris en 1860</strong> avec l'annexion des communes périphériques par Haussmann. Il faisait partie de la route de pèlerinage vers la <strong>basilique Saint-Denis</strong>."),
            ("🇮🇳", "Petit Inde rue du Faubourg-Saint-Denis", "Le <strong>passage Brady</strong> et la <strong>rue du Faubourg-Saint-Denis</strong>, à proximité, forment ce que les Parisiens appellent le <strong>« Petit Inde »</strong> ou <strong>Little Sri Lanka</strong>. Concentration de <strong>commerces, restaurants et épiceries indiennes, sri-lankaises, pakistanaises, bangladaises</strong>. Communauté installée depuis les <strong>années 1970</strong>. Le <strong>passage Brady</strong> (1828) est l'un des <strong>derniers passages couverts</strong> de Paris.")
        ],
        "itin": [
            ("Gare du Nord", "gare-du-nord", "à pied", "Rue Marx-Dormoy (5 min)", 5),
            ("Stalingrad", "stalingrad", "M2", "M2 directe (1 station)", 2),
            ("Barbès - Rochechouart", "barbes-rochechouart", "M2", "M2 directe (1 station)", 2),
            ("Pigalle", "pigalle", "M2", "M2 directe (3 stations)", 6),
            ("Bassin de la Villette", "stalingrad", "M2", "M2 directe (1 station)", 3),
            ("Châtelet", "chatelet", "M2 + M4", "M2 → Barbès + M4", 12)
        ]
    },
    "colonel-fabien": {
        "addr": "Place du Colonel-Fabien, 75019 Paris", "arr": "19e arrondissement (Paris)",
        "seo": "Station Colonel Fabien (M2) place du Colonel-Fabien dans le 19e. Nommée d'après Pierre Georges, résistant communiste. Siège du PCF.",
        "tagline": "M2 — Pierre Georges « Colonel Fabien » (résistance)",
        "hero_desc": "Station <strong>Colonel Fabien</strong> sur la <strong>place du Colonel-Fabien</strong> dans le <strong>19e arrondissement</strong>. Desservie par la <strong>ligne 2 du métro</strong>, ouverte le <strong>31 janvier 1903</strong>. Nommée d'après <strong>Pierre Georges</strong> dit <strong>« Colonel Fabien »</strong> (<strong>1919-1944</strong>), <strong>résistant communiste</strong>. Place du <strong>siège du PCF</strong> (Parti communiste français).",
        "intros": [
            "La station <strong>Colonel Fabien</strong> est implantée sur la <strong>place du Colonel-Fabien</strong> dans le <strong>19e arrondissement</strong>. Elle est desservie par la <strong>ligne 2 du métro parisien</strong>, entre <strong>Jaurès</strong> (1 station) et <strong>Belleville</strong> (1 station). Bus 26, 75 en correspondance.",
            "Ouverte le <strong>31 janvier 1903</strong>, initialement nommée <strong>« Combat »</strong> (rappel d'un <strong>combat de coqs</strong> qui se tenait à cet endroit autrefois). Renommée <strong>« Colonel Fabien »</strong> le <strong>13 février 1946</strong>, en hommage au <strong>résistant communiste Pierre Georges</strong>.",
            "Le nom <strong>Colonel Fabien</strong> rend hommage à <strong>Pierre Georges</strong> dit <strong>« Colonel Fabien »</strong> (<strong>1919-1944</strong>), <strong>résistant communiste</strong>, <strong>auteur du premier attentat contre un officier allemand à Paris</strong> (<strong>21 août 1941</strong>, station de métro Barbès-Rochechouart). <strong>Tué au combat le 27 décembre 1944</strong> en Alsace. La place accueille le <strong>siège du PCF</strong>."
        ],
        "hist_title": "1903-1946 : Combat puis Colonel Fabien",
        "hist": [
            "La station est <strong>inaugurée le 31 janvier 1903</strong> sous le nom de <strong>« Combat »</strong>, en référence à un <strong>combat de coqs</strong> traditionnel qui se tenait à cet endroit du quartier. Le tronçon Anvers ↔ Bagnolet de la ligne 2 Nord ouvre alors.",
            "Le <strong>13 février 1946</strong>, la station est <strong>renommée Colonel Fabien</strong> en hommage à <strong>Pierre Georges</strong> dit <strong>« Colonel Fabien »</strong> (<strong>9 janvier 1919 - 27 décembre 1944</strong>), <strong>résistant communiste</strong>. Né à Paris, ouvrier, militant communiste, il s'engage dans les <strong>Brigades internationales</strong> en Espagne (1937).",
            "À 22 ans, il devient l'<strong>auteur du premier attentat contre un officier allemand à Paris</strong> : le <strong>21 août 1941</strong>, à la station de métro <strong>Barbès-Rochechouart</strong>, il abat l'aspirant Alfons Moser. Cet acte marque le <strong>début de la lutte armée</strong> de la Résistance française. Devient <strong>commandant des FTP de Paris</strong> puis <strong>colonel</strong>. <strong>Tué au combat le 27 décembre 1944</strong> en Alsace (mine antichar). Le <strong>siège du Parti communiste français</strong> est installé sur la place depuis <strong>1971</strong> (architecte <strong>Oscar Niemeyer</strong>)."
        ],
        "faq": [
            ("Quelle ligne dessert Colonel Fabien ?", "Uniquement la <strong>ligne 2 du métro</strong>. Bus 26 et 75."),
            ("Qui est le Colonel Fabien ?", "<strong>Pierre Georges</strong> dit <strong>« Colonel Fabien »</strong> (1919-1944), <strong>résistant communiste</strong>, auteur du <strong>premier attentat contre un officier allemand à Paris</strong> (21 août 1941). Tué au combat en 1944."),
            ("Quel était l'ancien nom ?", "<strong>« Combat »</strong> (1903-1946), en référence à un combat de coqs traditionnel."),
            ("Quand a-t-elle ouvert ?", "Le <strong>31 janvier 1903</strong> (nom « Combat »), renommée le <strong>13 février 1946</strong>."),
            ("Qu'est-ce que le siège du PCF ?", "Bâtiment moderniste conçu par <strong>Oscar Niemeyer</strong> (architecte brésilien), inauguré en <strong>1971</strong>, siège national du <strong>Parti communiste français</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Siège du PCF</strong> par <strong>Oscar Niemeyer</strong> (1971) : bâtiment moderniste remarquable.",
            "Pour <strong>Buttes-Chaumont</strong> : <strong>M2 → Belleville</strong> ou bus 26.",
            "Pour <strong>République</strong> : <strong>M2 + M11</strong> ou bus.",
            "Pour <strong>Stalingrad</strong> et <strong>canal de l'Ourcq</strong> : <strong>M2 directe</strong> (3 stations).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎖️", "Colonel Fabien et l'entrée en lutte armée", "<strong>Pierre Georges</strong> dit <strong>« Colonel Fabien »</strong> (1919-1944), <strong>résistant communiste</strong>, est l'<strong>auteur du premier attentat contre un officier allemand à Paris</strong>. Le <strong>21 août 1941</strong>, à la station de métro <strong>Barbès-Rochechouart</strong>, il abat à 22 ans l'aspirant <strong>Alfons Moser</strong>. Cet acte marque le <strong>début de la lutte armée</strong> de la Résistance française. Devient <strong>commandant des FTP de Paris</strong> puis <strong>colonel</strong>. <strong>Tué au combat le 27 décembre 1944</strong> en Alsace par une mine antichar."),
            ("🏛️", "Siège du PCF par Oscar Niemeyer", "Le <strong>siège du Parti communiste français</strong>, sur la place du Colonel-Fabien, a été inauguré en <strong>1971</strong>. Conçu par l'<strong>architecte brésilien Oscar Niemeyer</strong> (1907-2012), figure du <strong>modernisme</strong> et concepteur de Brasilia. Le bâtiment se compose d'une <strong>tour-tablette en façade ondulée vitrée</strong> et d'une <strong>coupole semi-enterrée</strong> (salle de réunion). <strong>Inscrit aux monuments historiques en 2007</strong>.")
        ],
        "itin": [
            ("Stalingrad et canal de l'Ourcq", "stalingrad", "M2", "M2 directe (3 stations)", 7),
            ("Buttes-Chaumont", "buttes-chaumont", "M2 + bus", "M2 → Belleville puis bus 26", 10),
            ("Belleville", "belleville", "M2", "M2 directe (1 station)", 2),
            ("République", "republique", "M2 + M11", "M2 → Belleville + M11", 9),
            ("Gare du Nord", "gare-du-nord", "M2", "M2 directe (4 stations)", 8),
            ("Père Lachaise", "pere-lachaise", "M2", "M2 directe (3 stations)", 6)
        ]
    },
    "couronnes": {
        "addr": "Boulevard de Belleville, 75020 Paris", "arr": "20e arrondissement (Paris)",
        "seo": "Station Couronnes (M2) boulevard de Belleville dans le 20e arrondissement. Lieu de la catastrophe ferroviaire de 1903 (84 morts) qui transforma la sécurité du métro.",
        "tagline": "M2 — boulevard de Belleville, mémoire 1903",
        "hero_desc": "Station <strong>Couronnes</strong> sur le <strong>boulevard de Belleville</strong> dans le <strong>20e arrondissement</strong>. Desservie par la <strong>ligne 2 du métro</strong>, ouverte le <strong>31 janvier 1903</strong>. Tristement célèbre pour la <strong>catastrophe ferroviaire du 10 août 1903</strong> (<strong>84 morts</strong>), qui transforma profondément les <strong>règles de sécurité</strong> du métro parisien.",
        "intros": [
            "La station <strong>Couronnes</strong> est implantée sur le <strong>boulevard de Belleville</strong> dans le <strong>20e arrondissement</strong>. Elle est desservie par la <strong>ligne 2 du métro parisien</strong>, entre <strong>Belleville</strong> (1 station) et <strong>Ménilmontant</strong> (1 station). Bus 96 en correspondance.",
            "Ouverte le <strong>31 janvier 1903</strong> avec le prolongement Anvers ↔ Bagnolet. La station est tristement célèbre pour la <strong>catastrophe ferroviaire du 10 août 1903</strong>, l'<strong>accident le plus meurtrier de l'histoire du métro parisien</strong> avec <strong>84 morts</strong>.",
            "Le nom <strong>Couronnes</strong> vient de la <strong>rue des Couronnes</strong>, ancienne <strong>rue des Couronnes-Saint-Sauveur</strong>, allusion aux <strong>couronnes d'épines</strong> portées par les pèlerins de l'église Saint-Sauveur. Quartier populaire et historique de <strong>Belleville</strong>, intégré à Paris en <strong>1860</strong>."
        ],
        "hist_title": "1903 : catastrophe ferroviaire et révolution sécurité",
        "hist": [
            "La station Couronnes est <strong>inaugurée le 31 janvier 1903</strong> avec le prolongement <strong>Anvers ↔ Bagnolet</strong> de la <strong>ligne 2 Nord</strong>.",
            "Le <strong>10 août 1903</strong>, à 19h30, une <strong>catastrophe ferroviaire</strong> se produit en station. Un train de <strong>matériel roulant en bois</strong> prend feu suite à un <strong>court-circuit</strong>. La fumée envahit la station, les passagers tentent de s'échapper dans le tunnel mais succombent à l'<strong>asphyxie</strong>. <strong>84 personnes périssent</strong> — l'<strong>accident le plus meurtrier de l'histoire du métro parisien</strong>. La catastrophe avait été précédée de plusieurs incendies et alertes ignorées.",
            "Les <strong>conséquences de la catastrophe</strong> furent considérables : <strong>remplacement progressif du matériel en bois par du métal</strong>, <strong>renforcement de l'éclairage de secours</strong>, <strong>amélioration de la ventilation</strong>, <strong>multiplication des issues de secours</strong>, <strong>création d'un service de sécurité spécialisé</strong>. Cette catastrophe est considérée comme un <strong>tournant fondamental dans l'histoire de la sécurité du métro</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Couronnes ?", "Uniquement la <strong>ligne 2 du métro</strong>. Bus 96."),
            ("Quand a-t-elle ouvert ?", "Le <strong>31 janvier 1903</strong>."),
            ("Qu'est-ce que la catastrophe de Couronnes ?", "Le <strong>10 août 1903</strong>, un incendie dans un train en bois provoqua la mort de <strong>84 personnes</strong> par asphyxie. <strong>Accident le plus meurtrier</strong> de l'histoire du métro parisien."),
            ("Quelles ont été les conséquences ?", "Refonte complète des <strong>règles de sécurité</strong> : matériel métallique, éclairage de secours, ventilation, issues de secours, service de sécurité."),
            ("Pour Belleville ?", "<strong>M2 directe</strong> (1 station, ~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "Pour <strong>Belleville</strong> : <strong>M2 directe</strong> (1 station).",
            "Pour le <strong>parc de Belleville</strong> et <strong>vue sur Paris</strong> : à 5 min à pied (rue des Couronnes).",
            "Quartier <strong>multi-ethnique animé</strong> du 20e arrondissement.",
            "<strong>Boulevard de Belleville</strong> : marché les mardi et vendredi matin.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⚠️", "Catastrophe de Couronnes (10 août 1903)", "Le <strong>10 août 1903</strong>, à 19h30, une <strong>catastrophe ferroviaire</strong> se produit à la station Couronnes. Un train en <strong>bois</strong> prend feu suite à un <strong>court-circuit</strong>. La fumée envahit la station ; les passagers, tentant de s'échapper dans le tunnel, succombent à l'<strong>asphyxie</strong>. <strong>84 morts</strong> — l'accident le plus <strong>meurtrier de l'histoire du métro parisien</strong>. Causes : <strong>matériel en bois</strong>, <strong>éclairage défaillant</strong>, <strong>signalisation insuffisante</strong>, <strong>ignorance des alertes préalables</strong>. La catastrophe entraîna une <strong>refonte complète</strong> des règles de sécurité."),
            ("🏘️", "Belleville, ancien village de la périphérie", "<strong>Belleville</strong>, ancien <strong>village rattaché à Paris en 1860</strong> avec d'autres communes, est aujourd'hui un quartier <strong>populaire et multi-ethnique</strong> du <strong>20e arrondissement</strong>. Quartier de <strong>communistes</strong> et d'<strong>artistes</strong> au XXe siècle (Édith Piaf y est née en <strong>1915</strong>). <strong>Chinatown bis</strong> de Paris (boulevard de Belleville). <strong>Parc de Belleville</strong> (1988) : <strong>vue panoramique sur Paris</strong>.")
        ],
        "itin": [
            ("Belleville", "belleville", "M2", "M2 directe (1 station)", 2),
            ("Ménilmontant", "menilmontant", "M2", "M2 directe (1 station)", 2),
            ("Parc de Belleville", "couronnes", "à pied", "Rue des Couronnes (5 min)", 5),
            ("Père Lachaise", "pere-lachaise", "M2", "M2 directe (2 stations)", 5),
            ("République", "republique", "M2 + M11", "M2 → Belleville + M11", 9),
            ("Châtelet", "chatelet", "M2 + M11", "M2 → Belleville + M11", 14)
        ]
    },
    "menilmontant": {
        "addr": "Boulevard de Ménilmontant, 75020 Paris", "arr": "20e arrondissement (Paris)",
        "seo": "Station Ménilmontant (M2) boulevard de Ménilmontant dans le 20e arrondissement. Ancien village populaire chanté par Charles Trenet (« Ménilmontant »).",
        "tagline": "M2 — boulevard de Ménilmontant, village populaire",
        "hero_desc": "Station <strong>Ménilmontant</strong> sur le <strong>boulevard de Ménilmontant</strong> dans le <strong>20e arrondissement</strong>. Desservie par la <strong>ligne 2 du métro</strong>, ouverte le <strong>31 janvier 1903</strong>. <strong>Ancien village rattaché à Paris en 1860</strong>, chanté par <strong>Charles Trenet</strong> (<em>« Ménilmontant »</em>, 1938) et <strong>Maurice Chevalier</strong>. Quartier populaire du <strong>20e</strong>.",
        "intros": [
            "La station <strong>Ménilmontant</strong> est implantée sur le <strong>boulevard de Ménilmontant</strong> dans le <strong>20e arrondissement</strong>. Elle est desservie par la <strong>ligne 2 du métro parisien</strong>, entre <strong>Couronnes</strong> (1 station) et <strong>Père Lachaise</strong> (1 station). Bus 96 en correspondance.",
            "Ouverte le <strong>31 janvier 1903</strong> avec le prolongement Anvers ↔ Bagnolet.",
            "Le nom <strong>Ménilmontant</strong> vient de l'<strong>ancien village de Ménilmontant</strong>, rattaché à Paris en <strong>1860</strong>. <strong>Étymologie</strong> incertaine : du latin <em>mesnil maletantum</em> (« mauvais hameau »), ou plus probablement <em>mesnil montant</em> (« hameau de la côte »), évoquant le relief du quartier. Quartier <strong>populaire et artistique</strong> chanté par <strong>Charles Trenet</strong>."
        ],
        "hist_title": "1903 : Ménilmontant, village artistique",
        "hist": [
            "La station Ménilmontant est <strong>inaugurée le 31 janvier 1903</strong> avec le prolongement <strong>Anvers ↔ Bagnolet</strong> de la <strong>ligne 2 Nord</strong>.",
            "Le nom <strong>Ménilmontant</strong> vient de l'<strong>ancien village de Ménilmontant</strong>, rattaché à Paris en <strong>1860</strong>. <strong>Étymologie</strong> contestée : <em>mesnil maletantum</em> (« mauvais hameau ») ou <em>mesnil montant</em> (« hameau de la côte »). Le village s'est développé au flanc de la <strong>colline de Belleville</strong> (~120 m d'altitude). <strong>Quartier populaire et ouvrier</strong> au XIXe siècle.",
            "Au <strong>XXe siècle</strong>, le quartier devient <strong>haut lieu de la chanson populaire française</strong>. <strong>Charles Trenet</strong> compose <em>« Ménilmontant »</em> en <strong>1938</strong> (chanson restée culte). <strong>Maurice Chevalier</strong>, né dans le quartier (12 rue du Retrait), évoque souvent Ménilmontant dans ses chansons. Aujourd'hui, le quartier reste <strong>populaire, multi-ethnique et artistique</strong>, avec le <strong>parc de Belleville</strong> et de nombreux <strong>ateliers d'artistes</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Ménilmontant ?", "Uniquement la <strong>ligne 2 du métro</strong>. Bus 96."),
            ("Quand a-t-elle ouvert ?", "Le <strong>31 janvier 1903</strong>."),
            ("Qu'est-ce que Ménilmontant ?", "Un <strong>ancien village</strong> rattaché à Paris en <strong>1860</strong>, situé au flanc de la <strong>colline de Belleville</strong>. Quartier <strong>populaire et artistique</strong>."),
            ("Pourquoi cette chanson de Charles Trenet ?", "<strong>Charles Trenet</strong> compose <em>« Ménilmontant »</em> en <strong>1938</strong>, chanson devenue <strong>culte</strong> qui célèbre le quartier populaire. <strong>Maurice Chevalier</strong> est né dans le quartier."),
            ("Pour le Père Lachaise ?", "<strong>M2 directe</strong> (1 station, ~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Parc de Belleville</strong> à 10 min à pied : vue panoramique sur Paris.",
            "Quartier <strong>populaire et artistique</strong> : ateliers, restaurants, bars.",
            "Pour le <strong>Père Lachaise</strong> : <strong>M2 directe</strong> (1 station).",
            "Pour <strong>Nation</strong> : <strong>M2 directe</strong> (5 stations).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎤", "Charles Trenet — Ménilmontant (1938)", "<strong>Charles Trenet</strong> (1913-2001), <strong>« Fou chantant »</strong>, compose en <strong>1938</strong> la chanson <em>« Ménilmontant »</em>. <em>« Ménilmontant, mais oui Madame, c'est là que j'ai laissé mon cœur, c'est là que je viens retrouver mon âme »</em>. Cette chanson, restée <strong>culte</strong>, célèbre le quartier populaire parisien. Trenet a aussi composé <em>La Mer</em> (1946), <em>Y'a d'la joie</em> (1937), <em>Douce France</em> (1947)."),
            ("🎩", "Maurice Chevalier, enfant de Ménilmontant", "<strong>Maurice Chevalier</strong> (<strong>1888-1972</strong>), <strong>chanteur et acteur français</strong>, est <strong>né le 12 septembre 1888</strong> au <strong>12 rue du Retrait</strong>, à Ménilmontant. Enfant pauvre du quartier, il devient une <strong>star internationale du music-hall</strong> et du cinéma. Évoque souvent Ménilmontant dans ses chansons. Reconnaissable à son <strong>canotier</strong> et son <strong>nœud papillon</strong>. <em>Valentine</em> (1924), <em>Prosper</em> (1935).")
        ],
        "itin": [
            ("Père Lachaise", "pere-lachaise", "M2", "M2 directe (1 station)", 2),
            ("Belleville", "belleville", "M2", "M2 directe (2 stations)", 4),
            ("Parc de Belleville", "couronnes", "à pied", "Rue des Pyrénées (10 min)", 10),
            ("Nation", "nation", "M2", "M2 directe (5 stations)", 10),
            ("République", "republique", "M2 + M11", "M2 → Belleville + M11", 11),
            ("Châtelet", "chatelet", "M2 + M11", "M2 → Belleville + M11", 15)
        ]
    },
    "philippe-auguste": {
        "addr": "Boulevard de Charonne, 75011 Paris", "arr": "11e arrondissement (Paris)",
        "seo": "Station Philippe Auguste (M2) boulevard de Charonne dans le 11e arrondissement. Nommée d'après le roi Philippe Auguste (1165-1223), bâtisseur du mur de Paris.",
        "tagline": "M2 — roi Philippe Auguste (1165-1223), mur de Paris",
        "hero_desc": "Station <strong>Philippe Auguste</strong> sur le <strong>boulevard de Charonne</strong> dans le <strong>11e arrondissement</strong>. Desservie par la <strong>ligne 2 du métro</strong>, ouverte le <strong>2 avril 1903</strong>. Nommée d'après <strong>Philippe II Auguste</strong> (<strong>1165-1223</strong>), <strong>roi de France</strong> qui fit <strong>construire le mur d'enceinte de Paris</strong> (<strong>1190-1213</strong>).",
        "intros": [
            "La station <strong>Philippe Auguste</strong> est implantée sur le <strong>boulevard de Charonne</strong> dans le <strong>11e arrondissement</strong>. Elle est desservie par la <strong>ligne 2 du métro parisien</strong>, entre <strong>Père Lachaise</strong> (1 station) et <strong>Alexandre Dumas</strong> (1 station). Bus 56, 76 en correspondance.",
            "Ouverte le <strong>2 avril 1903</strong> avec le prolongement Anvers ↔ Bagnolet (Alexandre Dumas).",
            "Le nom <strong>Philippe Auguste</strong> rend hommage à <strong>Philippe II Auguste</strong> (<strong>21 août 1165 - 14 juillet 1223</strong>), <strong>roi de France</strong> (1180-1223). Il fit <strong>construire le mur d'enceinte de Paris</strong> (<strong>1190-1213</strong>) — la <strong>première grande muraille parisienne</strong>. À l'extérieur de ce mur s'étendait alors la rue qui porte aujourd'hui le nom du roi."
        ],
        "hist_title": "1903 : boulevard de Charonne et le roi Philippe Auguste",
        "hist": [
            "La station Philippe Auguste est <strong>inaugurée le 2 avril 1903</strong> avec le prolongement <strong>Anvers ↔ Bagnolet</strong> de la <strong>ligne 2 Nord</strong>.",
            "Le nom <strong>Philippe Auguste</strong> commémore <strong>Philippe II</strong>, dit <strong>Philippe Auguste</strong> (<strong>21 août 1165 - 14 juillet 1223</strong>), <strong>roi de France</strong> (<strong>1180-1223</strong>). Premier à porter le titre de <strong>« roi de France »</strong> (et non plus « roi des Francs »). Il <strong>triple le domaine royal</strong> en reprenant aux Plantagenêts la Normandie, l'Anjou, le Maine, la Touraine, le Poitou (<strong>1202-1214</strong>). Vainqueur à <strong>Bouvines</strong> (<strong>27 juillet 1214</strong>).",
            "Il fit <strong>construire le mur d'enceinte de Paris</strong> de <strong>1190 à 1213</strong>. Cette <strong>première grande muraille parisienne</strong>, longue de <strong>5,3 km</strong>, comprenait <strong>67 tours</strong> et 10 portes. Elle entourait Paris pendant son départ pour la <strong>Troisième croisade</strong> (1190). Quelques vestiges subsistent (rue Clovis, rue des Jardins-Saint-Paul). La <strong>rue Philippe Auguste</strong> et son boulevard suivent à peu près le tracé extérieur du mur."
        ],
        "faq": [
            ("Quelle ligne dessert Philippe Auguste ?", "Uniquement la <strong>ligne 2 du métro</strong>. Bus 56 et 76."),
            ("Qui est Philippe Auguste ?", "<strong>Philippe II Auguste</strong> (1165-1223), <strong>roi de France</strong> (1180-1223). Triple le domaine royal, vainqueur à <strong>Bouvines</strong> (1214), fait construire le <strong>mur d'enceinte de Paris</strong> (1190-1213)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>2 avril 1903</strong>."),
            ("Le mur de Philippe Auguste existe-t-il encore ?", "<strong>Quelques vestiges</strong> subsistent : rue Clovis, rue des Jardins-Saint-Paul (4e arr.). Visibles librement."),
            ("Pour le Père Lachaise ?", "<strong>M2 directe</strong> (1 station, ~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "Pour le <strong>cimetière du Père Lachaise</strong> : <strong>M2 directe</strong> (1 station).",
            "Pour <strong>Nation</strong> et son hub : <strong>M2 directe</strong> (3 stations).",
            "Quartier résidentiel du <strong>11e arrondissement</strong>.",
            "Vestiges du <strong>mur de Philippe Auguste</strong> visibles rue Clovis et rue des Jardins-Saint-Paul (4e).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("👑", "Philippe Auguste, premier roi de France", "<strong>Philippe II</strong>, dit <strong>Philippe Auguste</strong> (1165-1223), <strong>roi de France</strong> (1180-1223). <strong>Premier à porter le titre de « roi de France »</strong> (et non plus « roi des Francs »). <strong>Triple le domaine royal</strong> en reprenant aux <strong>Plantagenêts</strong> la Normandie, l'Anjou, le Maine, la Touraine, le Poitou (1202-1214). <strong>Vainqueur à Bouvines</strong> (27 juillet 1214) — <strong>victoire fondatrice de la nation française</strong>. <strong>Fonde l'université de Paris</strong> (1200). Fait <strong>paver les principales rues de Paris</strong>."),
            ("🧱", "Mur d'enceinte de Philippe Auguste", "Le <strong>mur de Philippe Auguste</strong>, construit de <strong>1190 à 1213</strong>, est la <strong>première grande muraille de Paris</strong>. Longue de <strong>5,3 km</strong>, elle comprend <strong>67 tours</strong>, <strong>10 portes</strong> et entoure le <strong>domaine royal urbain</strong>. Construite pendant la <strong>Troisième croisade</strong> de Philippe Auguste pour protéger Paris en son absence. <strong>Quelques vestiges subsistent</strong> : <strong>rue Clovis</strong> (5e), <strong>rue des Jardins-Saint-Paul</strong> (4e), <strong>parking du Louvre</strong> (fondations).")
        ],
        "itin": [
            ("Père Lachaise", "pere-lachaise", "M2", "M2 directe (1 station)", 2),
            ("Nation", "nation", "M2", "M2 directe (3 stations)", 6),
            ("Alexandre Dumas", "alexandre-dumas", "M2", "M2 directe (1 station)", 2),
            ("République", "republique", "M2 + M11", "M2 → Belleville + M11", 14),
            ("Bastille", "bastille", "M2 + M5", "M2 → Nation + M1", 12),
            ("Gare du Nord", "gare-du-nord", "M2", "M2 directe (9 stations)", 18)
        ]
    },
    "alexandre-dumas": {
        "addr": "Boulevard de Charonne, 75020 Paris", "arr": "20e arrondissement (Paris)",
        "seo": "Station Alexandre Dumas (M2) boulevard de Charonne dans le 20e arrondissement. Nommée d'après Alexandre Dumas (1802-1870), auteur des Trois Mousquetaires.",
        "tagline": "M2 — Alexandre Dumas (1802-1870), Les Trois Mousquetaires",
        "hero_desc": "Station <strong>Alexandre Dumas</strong> sur le <strong>boulevard de Charonne</strong> dans le <strong>20e arrondissement</strong>. Desservie par la <strong>ligne 2 du métro</strong>, ouverte le <strong>2 avril 1903</strong>. Nommée d'après <strong>Alexandre Dumas</strong> (<strong>1802-1870</strong>), <strong>écrivain français</strong> auteur des <em>Trois Mousquetaires</em> (1844) et du <em>Comte de Monte-Cristo</em> (1844-1846).",
        "intros": [
            "La station <strong>Alexandre Dumas</strong> est implantée sur le <strong>boulevard de Charonne</strong> dans le <strong>20e arrondissement</strong> (initialement <strong>« Bagnolet »</strong>, terminus est de la ligne 2). Elle est desservie par la <strong>ligne 2 du métro parisien</strong>, entre <strong>Philippe Auguste</strong> (1 station) et <strong>Avron</strong> (1 station). Bus 56, 76 en correspondance.",
            "Ouverte le <strong>2 avril 1903</strong> comme <strong>terminus est de la ligne 2</strong> (sous le nom de <strong>« Bagnolet »</strong>). Renommée <strong>« Alexandre Dumas »</strong> le <strong>2 août 1970</strong>, à l'occasion du <strong>centenaire de la mort de l'écrivain</strong>.",
            "Le nom <strong>Alexandre Dumas</strong> commémore <strong>Alexandre Dumas père</strong> (<strong>1802-1870</strong>), <strong>écrivain français</strong>, auteur de romans historiques très populaires. <em>Les Trois Mousquetaires</em> (1844), <em>Le Comte de Monte-Cristo</em> (1844-1846), <em>La Reine Margot</em> (1845), <em>Vingt Ans après</em> (1845), <em>Le Vicomte de Bragelonne</em> (1847-1850). Inhumé au <strong>Panthéon</strong> en <strong>2002</strong>."
        ],
        "hist_title": "1903-1970 : Bagnolet puis Alexandre Dumas",
        "hist": [
            "La station est <strong>inaugurée le 2 avril 1903</strong> sous le nom de <strong>« Bagnolet »</strong>, comme <strong>terminus est de la ligne 2</strong> (jusqu'à son prolongement vers Nation le 31 janvier 1903 — mais la station Bagnolet/Alexandre Dumas restait alors un terminus important).",
            "Le <strong>2 août 1970</strong>, à l'occasion du <strong>centenaire de la mort d'Alexandre Dumas</strong>, la station est <strong>renommée Alexandre Dumas</strong>. Le nom <strong>« Bagnolet »</strong> est alors attribué à une <strong>nouvelle station de la ligne 3</strong> (Galliéni - Porte de Bagnolet).",
            "Le nom <strong>Alexandre Dumas</strong> commémore <strong>Alexandre Dumas père</strong> (<strong>24 juillet 1802 - 5 décembre 1870</strong>), <strong>écrivain français</strong>. Petit-fils d'esclave noir et d'un marquis français. Auteur de <strong>plus de 250 ouvrages</strong>, dont les <strong>romans historiques</strong> très populaires : <em>Les Trois Mousquetaires</em> (<strong>1844</strong>), <em>Le Comte de Monte-Cristo</em> (<strong>1844-1846</strong>), <em>La Reine Margot</em> (1845), <em>Vingt Ans après</em> (1845). Ses œuvres traduites en <strong>plus de 100 langues</strong>. <strong>Inhumé au Panthéon</strong> le <strong>30 novembre 2002</strong>, sous la présidence de Jacques Chirac."
        ],
        "faq": [
            ("Quelle ligne dessert Alexandre Dumas ?", "Uniquement la <strong>ligne 2 du métro</strong>. Bus 56 et 76."),
            ("Quel était l'ancien nom ?", "<strong>« Bagnolet »</strong> (1903-1970)."),
            ("Quand a-t-elle été renommée ?", "Le <strong>2 août 1970</strong>, pour le <strong>centenaire de la mort d'Alexandre Dumas</strong>."),
            ("Qui est Alexandre Dumas ?", "<strong>Alexandre Dumas père</strong> (1802-1870), <strong>écrivain français</strong>, auteur des <em>Trois Mousquetaires</em> (1844) et du <em>Comte de Monte-Cristo</em> (1844-1846). <strong>Inhumé au Panthéon en 2002</strong>."),
            ("Pour Nation ?", "<strong>M2 directe</strong> (2 stations, ~5 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "Pour <strong>Nation</strong> et son hub : <strong>M2 directe</strong> (2 stations).",
            "Pour le <strong>Père Lachaise</strong> : <strong>M2 directe</strong> (2 stations).",
            "Quartier résidentiel des <strong>11e/20e arrondissements</strong>.",
            "<strong>Inhumation au Panthéon</strong> d'Alexandre Dumas en <strong>2002</strong> (centenaire de sa naissance).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⚔️", "Alexandre Dumas, génie du roman-feuilleton", "<strong>Alexandre Dumas père</strong> (1802-1870), <strong>écrivain français</strong>, <strong>petit-fils d'esclave noir</strong> et d'un marquis. Auteur de <strong>plus de 250 ouvrages</strong> : <em>Les Trois Mousquetaires</em> (<strong>1844</strong>), <em>Le Comte de Monte-Cristo</em> (<strong>1844-1846</strong>), <em>La Reine Margot</em> (1845), <em>Vingt Ans après</em> (1845), <em>Le Vicomte de Bragelonne</em> (1847-1850). Travaillait avec son nègre littéraire <strong>Auguste Maquet</strong>. Œuvres traduites en <strong>plus de 100 langues</strong>. <strong>Inhumé au Panthéon</strong> le <strong>30 novembre 2002</strong>, sous Jacques Chirac."),
            ("🏛️", "Au Panthéon en 2002", "L'<strong>inhumation d'Alexandre Dumas au Panthéon</strong> a lieu le <strong>30 novembre 2002</strong>, pour le <strong>bicentenaire de sa naissance</strong>. Décision du président <strong>Jacques Chirac</strong>. Cérémonie marquée par le discours présidentiel : <em>« Avec vous, c'est l'enfance, ce sont les heures d'émerveillement, les lectures faites en cachette à la lumière d'une lampe, sous un drap. »</em> Son cercueil a été <strong>porté par quatre cavaliers en costume de mousquetaire</strong>.")
        ],
        "itin": [
            ("Nation", "nation", "M2", "M2 directe (2 stations)", 5),
            ("Père Lachaise", "pere-lachaise", "M2", "M2 directe (2 stations)", 5),
            ("Philippe Auguste", "philippe-auguste", "M2", "M2 directe (1 station)", 2),
            ("Bastille", "bastille", "M2 + M1", "M2 → Nation + M1", 11),
            ("République", "republique", "M2 + M11", "M2 → Belleville + M11", 15),
            ("Châtelet", "chatelet", "M2 + M1", "M2 → Nation + M1", 18)
        ]
    },
    "avron": {
        "addr": "Boulevard de Charonne, 75020 Paris", "arr": "20e arrondissement (Paris)",
        "seo": "Station Avron (M2) dans le 20e arrondissement, sur la rue d'Avron. Quartier résidentiel proche du Cours de Vincennes et du Bois de Vincennes.",
        "tagline": "M2 — rue d'Avron, 20e résidentiel",
        "hero_desc": "Station <strong>Avron</strong> sur la <strong>rue d'Avron</strong> dans le <strong>20e arrondissement</strong>. Desservie par la <strong>ligne 2 du métro</strong>, ouverte le <strong>2 avril 1903</strong>. Quartier résidentiel du <strong>20e</strong>, à proximité du <strong>Cours de Vincennes</strong> et du <strong>Bois de Vincennes</strong>.",
        "intros": [
            "La station <strong>Avron</strong> est implantée à proximité de la <strong>rue d'Avron</strong> dans le <strong>20e arrondissement</strong>. Elle est desservie par la <strong>ligne 2 du métro parisien</strong>, entre <strong>Alexandre Dumas</strong> (1 station) et <strong>Nation</strong> (1 station, terminus est de la M2). Bus 26 et 71 en correspondance.",
            "Ouverte le <strong>2 avril 1903</strong> avec le prolongement de la <strong>ligne 2 Nord</strong> vers <strong>Bagnolet</strong> (devenu Alexandre Dumas).",
            "Le nom <strong>Avron</strong> vient de la <strong>rue d'Avron</strong>, voie historique du <strong>20e arrondissement</strong>. Quartier résidentiel paisible, à proximité du <strong>Cours de Vincennes</strong> (large avenue) et du <strong>Bois de Vincennes</strong> à courte distance."
        ],
        "hist_title": "1903 : prolongement M2 et rue d'Avron",
        "hist": [
            "La station Avron est <strong>inaugurée le 2 avril 1903</strong> avec le prolongement <strong>Anvers ↔ Bagnolet</strong> de la <strong>ligne 2 Nord</strong> (devenue ligne 2 en 1907).",
            "La <strong>rue d'Avron</strong>, qui donne son nom à la station, est une <strong>voie historique du 20e arrondissement</strong>. Le nom vient probablement d'un ancien lieu-dit. Le quartier s'est urbanisé au <strong>XIXe siècle</strong> après le rattachement à Paris en <strong>1860</strong>.",
            "Le quartier est aujourd'hui résidentiel paisible du <strong>20e</strong>, à proximité du <strong>Cours de Vincennes</strong> (large avenue rectiligne entre Nation et la Porte de Vincennes) et à courte distance du <strong>Bois de Vincennes</strong> (995 ha) — accessible par la <strong>M2 → Nation</strong> puis bus 56."
        ],
        "faq": [
            ("Quelle ligne dessert Avron ?", "Uniquement la <strong>ligne 2 du métro</strong>. Bus 26 et 71."),
            ("Quand a-t-elle ouvert ?", "Le <strong>2 avril 1903</strong>."),
            ("Pour Nation ?", "<strong>M2 directe</strong> (1 station, terminus est, ~2 min)."),
            ("Pour le Bois de Vincennes ?", "<strong>M2 → Nation</strong> + bus 56 ou 86 (~10 min)."),
            ("Quartier résidentiel ?", "<strong>Oui</strong>. Atmosphère paisible du 20e arrondissement."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "Pour <strong>Nation</strong> : <strong>M2 directe</strong> (1 station, terminus est).",
            "Pour le <strong>Bois de Vincennes</strong> : <strong>M2 → Nation</strong> + bus 56/86.",
            "<strong>Cours de Vincennes</strong> : large avenue à proximité.",
            "Quartier résidentiel paisible du <strong>20e</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🌳", "Cours de Vincennes, axe historique", "Le <strong>Cours de Vincennes</strong>, à proximité d'Avron, est une <strong>large avenue rectiligne</strong> reliant la <strong>place de la Nation</strong> à la <strong>porte de Vincennes</strong>. Tracée sous le <strong>Second Empire</strong>, elle constitue l'<strong>axe historique royal</strong> menant au <strong>château de Vincennes</strong>. Bordée de <strong>platanes centenaires</strong>, elle accueille des marchés (mercredi, samedi) et plusieurs <strong>statues</strong> à la place de la Nation (Triomphe de la République de Dalou, 1899)."),
            ("🏰", "Château de Vincennes, forteresse royale", "Le <strong>château de Vincennes</strong>, à 10 min en bus 56 depuis Nation, est l'une des <strong>plus importantes forteresses royales</strong> de France. Construit du <strong>XIIe au XVIIe siècle</strong>, il abrite le <strong>donjon le plus haut d'Europe</strong> (52 m, XIVe siècle). Résidence des rois de France pendant des siècles, il devient <strong>prison d'État</strong> (Diderot, Mirabeau, marquis de Sade y furent enfermés). <strong>Classé monument historique</strong>, ouvert au public.")
        ],
        "itin": [
            ("Nation", "nation", "M2", "M2 directe (1 station, terminus)", 2),
            ("Alexandre Dumas", "alexandre-dumas", "M2", "M2 directe (1 station)", 2),
            ("Bois de Vincennes", "porte-doree", "M2 + bus", "M2 → Nation + bus 56", 10),
            ("Père Lachaise", "pere-lachaise", "M2", "M2 directe (3 stations)", 7),
            ("Bastille", "bastille", "M2 + M1", "M2 → Nation + M1", 11),
            ("République", "republique", "M2 + M11", "M2 → Belleville + M11", 17)
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
    d["tariff_zone"] = 1
    d["tariff_zone_context"] = "Paris intra-muros"
    d["commune"] = "Paris"
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
