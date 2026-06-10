#!/usr/bin/env python3
"""Enrichit M12 — 19 stations avec contenu T0 Wikipedia FR (biographies sensibles neutralisées)."""
import json
from pathlib import Path
ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    "mairie-d-aubervilliers": {
        "addr": "Avenue Victor-Hugo, 93300 Aubervilliers", "arr": "Aubervilliers (93)",
        "seo": "Station Mairie d'Aubervilliers, terminus nord M12 à Aubervilliers (93). Ouverte en mai 2022 avec l'extension nord de la ligne 12.",
        "tagline": "M12 — terminus nord, Aubervilliers (extension 2022)",
        "hero_desc": "Station <strong>Mairie d'Aubervilliers</strong>, <strong>terminus nord de la M12</strong>, à <strong>Aubervilliers</strong> (Seine-Saint-Denis, 93). Ouverte le <strong>31 mai 2022</strong> avec l'<strong>extension nord</strong> de la ligne 12 (Front Populaire → Mairie d'Aubervilliers).",
        "intros": [
            "La station <strong>Mairie d'Aubervilliers</strong> est <strong>terminus nord de la M12</strong>, située à <strong>Aubervilliers</strong> (Seine-Saint-Denis, 93). Bus 35, 134, 139, 150, 152, 234, 249, 250, 330.",
            "Ouverte le <strong>31 mai 2022</strong> avec l'<strong>extension de la M12</strong> de <strong>Front Populaire à Mairie d'Aubervilliers</strong> (2 stations ajoutées).",
            "À proximité : la <strong>mairie d'Aubervilliers</strong> et le quartier central de la commune. <strong>Aubervilliers</strong> (~85 000 habitants), commune dynamique de la <strong>Seine-Saint-Denis</strong>, en pleine transformation urbaine."
        ],
        "hist_title": "2022 : extension nord M12",
        "hist": [
            "La station Mairie d'Aubervilliers est <strong>inaugurée le 31 mai 2022</strong> avec l'<strong>extension nord de la M12</strong>. Le prolongement ajoute deux stations : <strong>Aimé Césaire</strong> et <strong>Mairie d'Aubervilliers</strong> (terminus).",
            "Ce <strong>prolongement</strong> est l'un des <strong>premiers grands chantiers</strong> du <strong>Grand Paris Express</strong>. Conçu pour <strong>désenclaver Aubervilliers</strong> et renforcer le maillage métro vers la Seine-Saint-Denis.",
            "<strong>Aubervilliers</strong> (~85 000 habitants) est l'une des communes les plus dynamiques de Seine-Saint-Denis. La <strong>mairie d'Aubervilliers</strong> est implantée sur l'avenue Victor-Hugo, axe principal de la commune."
        ],
        "faq": [
            ("Quelle ligne dessert Mairie d'Aubervilliers ?", "Uniquement la <strong>M12</strong> (terminus nord). Bus 35, 134, 139, 150, 152, 234, 249, 250, 330."),
            ("Quand a-t-elle ouvert ?", "Le <strong>31 mai 2022</strong>."),
            ("Combien d'habitants à Aubervilliers ?", "<strong>~85 000 habitants</strong>, l'une des communes les plus peuplées de Seine-Saint-Denis."),
            ("Pour le centre de Paris ?", "<strong>M12 directe</strong> vers <strong>Concorde</strong> (~22 min) ou <strong>Saint-Lazare</strong>."),
            ("Pour Front Populaire ?", "<strong>M12 directe</strong> (1 station, ~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Oui</strong>. Station moderne (2022).")
        ],
        "tips": [
            "<strong>Mairie d'Aubervilliers</strong> à la sortie : centre administratif.",
            "<strong>Marché d'Aubervilliers</strong> à proximité (mardi et vendredi).",
            "Pour <strong>Saint-Lazare</strong> : <strong>M12 directe</strong> (~18 min).",
            "Pour <strong>Concorde</strong> : <strong>M12 directe</strong> (~22 min).",
            "Zone tarifaire <strong>3</strong>, Seine-Saint-Denis."
        ],
        "trivia": [
            ("🚇", "Extension nord M12 (mai 2022)", "L'<strong>extension nord de la M12</strong>, inaugurée le <strong>31 mai 2022</strong>, prolonge la ligne 12 de <strong>Front Populaire</strong> (terminus depuis 2012) jusqu'à <strong>Mairie d'Aubervilliers</strong>. Deux stations ajoutées : <strong>Aimé Césaire</strong> et <strong>Mairie d'Aubervilliers</strong>. <strong>3,8 km</strong> de prolongement, premier grand chantier du <strong>Grand Paris Express</strong> mis en service. <strong>~37 000 voyageurs/jour</strong> attendus."),
            ("🏛️", "Aubervilliers, commune dynamique 93", "<strong>Aubervilliers</strong> (~85 000 habitants) est l'une des <strong>communes les plus peuplées</strong> de Seine-Saint-Denis. Ancienne commune <strong>industrielle</strong> aux XIXe et XXe siècles (production chimique, métallurgie), elle est en <strong>pleine transformation urbaine</strong>. Accueille la <strong>Cité internationale du cinéma</strong> (Studios d'Aubervilliers).")
        ],
        "itin": [
            ("Aimé Césaire", "aime-cesaire", "M12", "M12 directe (1 station)", 2),
            ("Front Populaire", "front-populaire", "M12", "M12 directe (2 stations)", 4),
            ("Saint-Lazare", "saint-lazare", "M12", "M12 directe (~18 min)", 18),
            ("Concorde", "concorde", "M12", "M12 directe (~22 min)", 22),
            ("Madeleine", "madeleine", "M12", "M12 directe (~20 min)", 20),
            ("Montparnasse", "montparnasse-bienvenue", "M12", "M12 directe (~28 min)", 28)
        ]
    },
    "aime-cesaire": {
        "addr": "Avenue Jean-Jaurès, 93300 Aubervilliers", "arr": "Aubervilliers (93)",
        "seo": "Station Aimé Césaire (M12) à Aubervilliers (93). Hommage à Aimé Césaire (1913-2008), poète et écrivain martiniquais. Ouverte en mai 2022.",
        "tagline": "M12 — Aimé Césaire, poète et écrivain martiniquais",
        "hero_desc": "Station <strong>Aimé Césaire</strong> à <strong>Aubervilliers</strong> (Seine-Saint-Denis, 93). Desservie par la <strong>M12</strong>, ouverte le <strong>31 mai 2022</strong>. Hommage à <strong>Aimé Césaire</strong> (<strong>1913-2008</strong>), <strong>poète, écrivain et homme politique français</strong> originaire de Martinique.",
        "intros": [
            "La station <strong>Aimé Césaire</strong> est implantée à <strong>Aubervilliers</strong> (Seine-Saint-Denis, 93). Elle est desservie par la <strong>ligne 12 du métro</strong>, entre <strong>Mairie d'Aubervilliers</strong> (1 station, terminus nord) et <strong>Front Populaire</strong> (1 station). Bus 35, 134, 150, 152, 250.",
            "Ouverte le <strong>31 mai 2022</strong> avec l'<strong>extension nord</strong> de la M12.",
            "Le nom <strong>Aimé Césaire</strong> rend hommage à <strong>Aimé Fernand David Césaire</strong> (<strong>26 juin 1913 - 17 avril 2008</strong>), <strong>poète, écrivain, dramaturge et homme politique français</strong> originaire de <strong>Martinique</strong>. <strong>Cofondateur du mouvement de la négritude</strong> avec Léopold Sédar Senghor et Léon-Gontran Damas. Auteur du <em>Cahier d'un retour au pays natal</em> (1939)."
        ],
        "hist_title": "2022 : extension nord et hommage à Césaire",
        "hist": [
            "La station Aimé Césaire est <strong>inaugurée le 31 mai 2022</strong> avec l'<strong>extension nord de la M12</strong>.",
            "Le nom <strong>Aimé Césaire</strong> commémore <strong>Aimé Fernand David Césaire</strong> (<strong>26 juin 1913 - 17 avril 2008</strong>), <strong>poète, écrivain, dramaturge et homme politique français</strong> originaire de <strong>Martinique</strong>. Études au <strong>lycée Louis-le-Grand</strong> et à l'<strong>École normale supérieure</strong>.",
            "<strong>Cofondateur du mouvement de la négritude</strong> avec <strong>Léopold Sédar Senghor</strong> (Sénégal) et <strong>Léon-Gontran Damas</strong> (Guyane) dans les années 1930. Auteur du célèbre <em><strong>Cahier d'un retour au pays natal</strong></em> (1939). Œuvres : <em>Discours sur le colonialisme</em> (1950), <em>Une Saison au Congo</em> (1966), <em>La Tragédie du roi Christophe</em> (1963). <strong>Maire de Fort-de-France</strong> de 1945 à 2001, <strong>député de la Martinique</strong> à l'Assemblée nationale (1945-1993)."
        ],
        "faq": [
            ("Quelle ligne dessert Aimé Césaire ?", "Uniquement la <strong>M12</strong>. Bus 35, 134, 150, 152, 250."),
            ("Qui est Aimé Césaire ?", "<strong>Aimé Césaire</strong> (1913-2008), <strong>poète et homme politique français</strong> originaire de Martinique. <strong>Cofondateur du mouvement de la négritude</strong>. Auteur du <em>Cahier d'un retour au pays natal</em> (1939)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>31 mai 2022</strong>."),
            ("Qu'est-ce que la négritude ?", "<strong>Mouvement littéraire et culturel</strong> fondé dans les années 1930 par <strong>Aimé Césaire</strong>, <strong>Léopold Sédar Senghor</strong> et <strong>Léon-Gontran Damas</strong>. <strong>Affirmation et valorisation</strong> de l'identité culturelle noire."),
            ("Pour Mairie d'Aubervilliers ?", "<strong>M12 directe</strong> (1 station, terminus nord)."),
            ("La station est-elle accessible PMR ?", "<strong>Oui</strong>. Station moderne (2022).")
        ],
        "tips": [
            "Station moderne <strong>2022</strong>, accessibilité PMR complète.",
            "Pour <strong>Mairie d'Aubervilliers</strong> : <strong>M12 directe</strong> (1 station, terminus nord).",
            "Pour <strong>Front Populaire</strong> : <strong>M12 directe</strong> (1 station).",
            "Pour <strong>Saint-Lazare</strong> : <strong>M12 directe</strong> (~16 min).",
            "Zone tarifaire <strong>3</strong>, Seine-Saint-Denis."
        ],
        "trivia": [
            ("📚", "Aimé Césaire et la négritude", "<strong>Aimé Césaire</strong> (1913-2008), <strong>poète et homme politique français</strong> né à Basse-Pointe (Martinique). Études brillantes au <strong>lycée Louis-le-Grand</strong> à Paris, puis à l'<strong>École normale supérieure</strong>. <strong>Cofondateur du mouvement de la négritude</strong> avec <strong>Léopold Sédar Senghor</strong> et <strong>Léon-Gontran Damas</strong> dans les années 1930 — mouvement littéraire affirmant l'identité culturelle noire. Œuvre majeure : <em><strong>Cahier d'un retour au pays natal</strong></em> (1939, préfacé par <strong>André Breton</strong>). <strong>Maire de Fort-de-France pendant 56 ans</strong> (1945-2001)."),
            ("🏛️", "Hommage parisien à l'engagement martiniquais", "L'<strong>attribution du nom Aimé Césaire</strong> à cette station du <strong>Grand Paris</strong> rend hommage à l'un des plus <strong>grands poètes francophones du XXe siècle</strong>. Au-delà de son œuvre littéraire, Césaire incarne l'<strong>engagement intellectuel et politique</strong>. <strong>Député de la Martinique</strong> à l'Assemblée nationale pendant <strong>48 ans</strong> (1945-1993). <strong>Funérailles nationales</strong> en 2008.")
        ],
        "itin": [
            ("Mairie d'Aubervilliers", "mairie-d-aubervilliers", "M12", "M12 directe (1 station, terminus)", 2),
            ("Front Populaire", "front-populaire", "M12", "M12 directe (1 station)", 2),
            ("Saint-Lazare", "saint-lazare", "M12", "M12 directe (~16 min)", 16),
            ("Concorde", "concorde", "M12", "M12 directe (~20 min)", 20),
            ("Madeleine", "madeleine", "M12", "M12 directe (~18 min)", 18),
            ("Montparnasse", "montparnasse-bienvenue", "M12", "M12 directe (~26 min)", 26)
        ]
    },
    "front-populaire": {
        "addr": "Avenue du Président-Wilson, 93210 Saint-Denis", "arr": "Saint-Denis (93)",
        "seo": "Station Front Populaire (M12) à La Plaine Saint-Denis (93). Hommage au Front Populaire (juin 1936). Ouverte en décembre 2012.",
        "tagline": "M12 — Front Populaire (juin 1936)",
        "hero_desc": "Station <strong>Front Populaire</strong> à <strong>Saint-Denis</strong> (Seine-Saint-Denis, 93), quartier <strong>La Plaine Saint-Denis</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>18 décembre 2012</strong>. Hommage au <strong>Front Populaire</strong>, coalition de gauche qui remporta les élections législatives de <strong>juin 1936</strong>.",
        "intros": [
            "La station <strong>Front Populaire</strong> est implantée à <strong>Saint-Denis</strong> (Seine-Saint-Denis, 93), dans le quartier de <strong>La Plaine Saint-Denis</strong>, à la limite d'Aubervilliers. Elle est desservie par la <strong>M12</strong>, entre <strong>Aimé Césaire</strong> (1 station) et <strong>Porte de la Chapelle</strong> (1 station). Bus 139, 150, 153, 239.",
            "Ouverte le <strong>18 décembre 2012</strong> avec le <strong>prolongement de la M12</strong> de <strong>Porte de la Chapelle à Front Populaire</strong>. Devient terminus nord de la ligne jusqu'en 2022.",
            "Le nom <strong>Front Populaire</strong> rend hommage à la <strong>coalition de partis de gauche</strong> qui remporte les <strong>élections législatives françaises de juin 1936</strong>. Gouvernement dirigé par <strong>Léon Blum</strong> (mai 1936 - juin 1937). Le <strong>quartier de La Plaine Saint-Denis</strong>, ancien <strong>quartier industriel</strong>, est en pleine transformation urbaine."
        ],
        "hist_title": "2012 : prolongement M12 et coalition de 1936",
        "hist": [
            "La station Front Populaire est <strong>inaugurée le 18 décembre 2012</strong> avec le <strong>prolongement de la M12</strong> de <strong>Porte de la Chapelle à Front Populaire</strong>. Devient <strong>terminus nord</strong> de la ligne 12 jusqu'au <strong>31 mai 2022</strong>.",
            "Le nom <strong>Front Populaire</strong> commémore le <strong>Front populaire</strong>, <strong>coalition de partis de gauche</strong> (SFIO, Parti radical, Parti communiste, etc.) qui remporte les <strong>élections législatives françaises de juin 1936</strong>. Gouvernement dirigé par <strong>Léon Blum</strong> (mai 1936 - juin 1937).",
            "Le <strong>quartier de La Plaine Saint-Denis</strong>, autour de la station, est un <strong>ancien quartier industriel</strong> en pleine transformation urbaine depuis les années 1990. <strong>Stade de France</strong> à proximité (construit pour la Coupe du monde de football 1998). <strong>Universités</strong>, <strong>sièges sociaux</strong> (Generali, SNCF, SFR), <strong>quartier d'affaires</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Front Populaire ?", "Uniquement la <strong>M12</strong>. Bus 139, 150, 153, 239."),
            ("Quand a-t-elle ouvert ?", "Le <strong>18 décembre 2012</strong>."),
            ("Qu'est-ce que le Front populaire ?", "<strong>Coalition de partis de gauche</strong> (SFIO, Parti radical, PCF) qui remporte les <strong>élections législatives françaises de juin 1936</strong>. Gouvernement dirigé par <strong>Léon Blum</strong>."),
            ("Pour le Stade de France ?", "<strong>~15 min à pied</strong> ou bus 150."),
            ("Pour Saint-Lazare ?", "<strong>M12 directe</strong> (~14 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Oui</strong>. Station moderne (2012).")
        ],
        "tips": [
            "<strong>Stade de France</strong> à 15 min à pied ou bus 150.",
            "Quartier <strong>La Plaine Saint-Denis</strong> en pleine transformation urbaine.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M12 directe</strong> (~14 min).",
            "Pour <strong>Concorde</strong> : <strong>M12 directe</strong> (~18 min).",
            "Zone tarifaire <strong>3</strong>, Seine-Saint-Denis."
        ],
        "trivia": [
            ("🗳️", "Front populaire de 1936", "Le <strong>Front populaire</strong> est une <strong>coalition de partis de gauche</strong> formée en France en <strong>1935</strong> (SFIO, Parti radical, PCF). Remporte les <strong>élections législatives de juin 1936</strong>. <strong>Gouvernement Léon Blum</strong> (mai 1936 - juin 1937). <strong>Réformes sociales majeures</strong> : <strong>semaine de 40 heures</strong>, <strong>2 semaines de congés payés</strong>, <strong>conventions collectives</strong>, <strong>scolarité obligatoire jusqu'à 14 ans</strong>. <strong>Accords de Matignon</strong> (7 juin 1936) entre patronat et syndicats."),
            ("🏟️", "Stade de France à proximité", "Le <strong>Stade de France</strong>, à 15 min à pied de la station, est le <strong>plus grand stade français</strong> avec <strong>81 338 places</strong>. Inauguré le <strong>28 janvier 1998</strong> pour la <strong>Coupe du monde de football 1998</strong> remportée par la France. Accueille les <strong>matchs internationaux</strong> de football et rugby, les <strong>finales de Coupe de France</strong>, des <strong>concerts</strong>.")
        ],
        "itin": [
            ("Stade de France", "stade-de-france", "M12 + à pied", "À pied (15 min) ou bus 150", 15),
            ("Aimé Césaire", "aime-cesaire", "M12", "M12 directe (1 station)", 2),
            ("Mairie d'Aubervilliers", "mairie-d-aubervilliers", "M12", "M12 directe (2 stations, terminus)", 4),
            ("Saint-Lazare", "saint-lazare", "M12", "M12 directe (~14 min)", 14),
            ("Concorde", "concorde", "M12", "M12 directe (~18 min)", 18),
            ("Madeleine", "madeleine", "M12", "M12 directe (~16 min)", 16)
        ]
    },
    "porte-de-la-chapelle": {
        "addr": "Boulevard Ney, 75018 Paris", "arr": "18e arrondissement (Paris)",
        "seo": "Station Porte de la Chapelle (M12) boulevard Ney dans le 18e. Correspondance tramway T3b. Adidas Arena (2024) à proximité.",
        "tagline": "M12 + T3b — porte nord, Adidas Arena",
        "hero_desc": "Station <strong>Porte de la Chapelle</strong> sur le <strong>boulevard Ney</strong> dans le <strong>18e arrondissement</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>23 août 1916</strong>. Correspondance <strong>tramway T3b</strong>. À proximité de l'<strong>Adidas Arena</strong> (2024, salle multifonctions des JO de Paris).",
        "intros": [
            "La station <strong>Porte de la Chapelle</strong> est implantée sur le <strong>boulevard Ney</strong> dans le <strong>18e arrondissement</strong>, à la <strong>limite du boulevard périphérique</strong>. Elle est desservie par la <strong>M12</strong> et le <strong>tramway T3b</strong>, entre <strong>Front Populaire</strong> (1 station, terminus nord) et <strong>Marx Dormoy</strong> (1 station). Bus 35, 60, 65, 153, 239, 302, 519.",
            "Ouverte le <strong>23 août 1916</strong> comme <strong>terminus nord</strong> de la ligne A du <strong>Nord-Sud</strong> (compagnie privée, devenue ligne 12 en 1930 puis 1942). Conserve ce statut jusqu'au <strong>prolongement de 2012</strong>.",
            "À proximité immédiate : l'<strong>Adidas Arena</strong> (inaugurée en <strong>février 2024</strong>, capacité 8 000 places), construite pour les <strong>Jeux Olympiques de Paris 2024</strong>. <strong>Quartier de la Chapelle</strong>, en transformation urbaine."
        ],
        "hist_title": "1916 : ancien terminus nord et Adidas Arena (2024)",
        "hist": [
            "La station Porte de la Chapelle est <strong>inaugurée le 23 août 1916</strong> comme <strong>terminus nord</strong> de la <strong>ligne A du Nord-Sud</strong> (compagnie privée fusionnée avec la CMP en 1930, ligne devenue M12 en 1942).",
            "Elle conserve ce statut de <strong>terminus nord pendant 96 ans</strong>, jusqu'au <strong>18 décembre 2012</strong>, date du <strong>prolongement vers Front Populaire</strong>.",
            "L'<strong>Adidas Arena</strong>, à proximité, est inaugurée en <strong>février 2024</strong> pour les <strong>Jeux Olympiques de Paris 2024</strong>. <strong>Capacité de 8 000 places</strong>. Conçue par les architectes <strong>NP2F</strong> et <strong>SCAU</strong>. <strong>Salle multifonctions</strong> accueillant événements sportifs, concerts, salons. Le quartier de la Chapelle connaît une <strong>profonde transformation urbaine</strong>."
        ],
        "faq": [
            ("Quelles lignes desservent Porte de la Chapelle ?", "<strong>M12</strong> et <strong>tramway T3b</strong>. Bus 35, 60, 65, 153, 239, 302, 519."),
            ("Quand a-t-elle ouvert ?", "Le <strong>23 août 1916</strong>, comme terminus nord de la ligne 12 (jusqu'en 2012)."),
            ("Pour l'Adidas Arena ?", "<strong>~5 min à pied</strong>. Salle multifonctions des JO 2024."),
            ("Pour la Gare du Nord ?", "<strong>M12 → Marx Dormoy + à pied</strong>, ou bus 65."),
            ("Pour Marx Dormoy ?", "<strong>M12 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>. Accès tramway T3b accessible.")
        ],
        "tips": [
            "<strong>Adidas Arena</strong> à 5 min à pied : salle multifonctions des JO 2024 (8 000 places).",
            "<strong>Tramway T3b</strong> en correspondance : axe des Maréchaux.",
            "Pour <strong>Porte d'Aubervilliers</strong> : T3b directe.",
            "Quartier en <strong>transformation urbaine</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏟️", "Adidas Arena, héritage JO 2024", "L'<strong>Adidas Arena</strong>, à 5 min à pied de la station, est inaugurée en <strong>février 2024</strong> pour les <strong>Jeux Olympiques et Paralympiques de Paris 2024</strong>. <strong>Capacité de 8 000 places</strong>. Conçue par les architectes <strong>NP2F</strong> et <strong>SCAU</strong>. Pendant les JO 2024 : <strong>épreuves de badminton et gymnastique rythmique</strong>. En héritage : <strong>salle multifonctions</strong> accueillant événements sportifs (basket Paris Basketball), concerts, salons. Investissement de <strong>140 millions d'euros</strong>."),
            ("🚇", "Ancien terminus nord 1916-2012", "Pendant <strong>96 ans</strong>, la station Porte de la Chapelle a été le <strong>terminus nord de la M12</strong>. Inaugurée le <strong>23 août 1916</strong> comme terminus de la <strong>ligne A du Nord-Sud</strong> (compagnie privée), elle conserve ce statut jusqu'au <strong>prolongement de 2012</strong> qui ajoute Front Populaire. La station a connu plusieurs <strong>rénovations</strong> pour s'adapter à son rôle de hub avec le <strong>tramway T3b</strong> (inauguré en 2012).")
        ],
        "itin": [
            ("Adidas Arena", "porte-de-la-chapelle", "à pied", "Boulevard Ney (5 min)", 5),
            ("Marx Dormoy", "marx-dormoy", "M12", "M12 directe (1 station)", 2),
            ("Gare du Nord", "gare-du-nord", "M12 + à pied", "M12 → Marx Dormoy + à pied (10 min)", 12),
            ("Saint-Lazare", "saint-lazare", "M12", "M12 directe (~12 min)", 12),
            ("Concorde", "concorde", "M12", "M12 directe (~16 min)", 16),
            ("Madeleine", "madeleine", "M12", "M12 directe (~14 min)", 14)
        ]
    },
    "marx-dormoy": {
        "addr": "Rue de la Chapelle, 75018 Paris", "arr": "18e arrondissement (Paris)",
        "seo": "Station Marx Dormoy (M12) rue de la Chapelle dans le 18e. Hommage à Marx Dormoy (1888-1941), homme politique français. Quartier Goutte d'Or.",
        "tagline": "M12 — Marx Dormoy, 18e arrondissement",
        "hero_desc": "Station <strong>Marx Dormoy</strong> sur la <strong>rue de la Chapelle</strong> dans le <strong>18e arrondissement</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>5 novembre 1910</strong>. Hommage à <strong>Marx Dormoy</strong> (<strong>1888-1941</strong>), <strong>homme politique français</strong>. Quartier <strong>Goutte d'Or</strong>.",
        "intros": [
            "La station <strong>Marx Dormoy</strong> est implantée sur la <strong>rue de la Chapelle</strong> dans le <strong>18e arrondissement</strong>. Elle est desservie par la <strong>ligne 12 du métro</strong>, entre <strong>Porte de la Chapelle</strong> (1 station) et <strong>Marcadet - Poissonniers</strong> (1 station). Bus 35, 60, 65.",
            "Ouverte le <strong>5 novembre 1910</strong> avec le tronçon initial <strong>Porte de Versailles ↔ Notre-Dame-de-Lorette</strong> de la ligne A du <strong>Nord-Sud</strong> (compagnie privée). Le nom actuel a été attribué après 1945.",
            "Le nom <strong>Marx Dormoy</strong> rend hommage à <strong>Marx Dormoy</strong> (<strong>1888-1941</strong>), <strong>homme politique socialiste français</strong>. <strong>Député de l'Allier</strong>, <strong>ministre de l'Intérieur</strong> sous le gouvernement <strong>Léon Blum</strong> (1936-1937). Quartier de la <strong>Goutte d'Or</strong>, secteur populaire et multi-ethnique du <strong>18e arrondissement</strong>."
        ],
        "hist_title": "1910 : Nord-Sud et hommage politique",
        "hist": [
            "La station est <strong>inaugurée le 5 novembre 1910</strong> avec le tronçon initial <strong>Porte de Versailles ↔ Notre-Dame-de-Lorette</strong> de la <strong>ligne A du Nord-Sud</strong> (compagnie privée). Initialement nommée <strong>« Torcy »</strong> ou <strong>« La Chapelle »</strong> selon les sources.",
            "Le nom actuel <strong>Marx Dormoy</strong> est attribué après <strong>1945</strong>, en hommage à <strong>Marx Dormoy</strong> (<strong>1888-1941</strong>), <strong>homme politique socialiste français</strong>. <strong>Député SFIO de l'Allier</strong>, <strong>ministre de l'Intérieur</strong> dans le gouvernement de <strong>Léon Blum</strong> (juin 1936 - juin 1937).",
            "Le quartier de la <strong>Goutte d'Or</strong>, autour de la station, est l'un des quartiers les plus <strong>populaires et multi-ethniques</strong> de Paris. Important quartier d'<strong>immigration africaine</strong> et <strong>maghrébine</strong>. <strong>Marché Dejean</strong> (alimentaire) à proximité, l'un des principaux marchés africains de Paris."
        ],
        "faq": [
            ("Quelle ligne dessert Marx Dormoy ?", "Uniquement la <strong>M12</strong>. Bus 35, 60, 65."),
            ("Qui est Marx Dormoy ?", "<strong>Marx Dormoy</strong> (1888-1941), <strong>homme politique socialiste français</strong>. <strong>Député SFIO de l'Allier</strong>, <strong>ministre de l'Intérieur</strong> sous le gouvernement Léon Blum (1936-1937)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>."),
            ("Pour la Goutte d'Or ?", "<strong>~5 min à pied</strong>. Quartier multi-ethnique populaire."),
            ("Pour la Gare du Nord ?", "<strong>~10 min à pied</strong> via la rue de la Chapelle."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Marché Dejean</strong> à proximité : principal marché africain de Paris.",
            "<strong>Quartier Goutte d'Or</strong> : populaire et multi-ethnique.",
            "<strong>Gare du Nord</strong> à 10 min à pied.",
            "Pour <strong>Concorde</strong> : <strong>M12 directe</strong> (~14 min).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Marx Dormoy, ministre du Front populaire", "<strong>Marx Dormoy</strong> (1888-1941), <strong>homme politique socialiste français</strong>. <strong>Député SFIO de l'Allier</strong> (Montluçon). <strong>Ministre de l'Intérieur</strong> dans le gouvernement de <strong>Léon Blum</strong> pendant le <strong>Front populaire</strong> (juin 1936 - juin 1937). Membre influent du <strong>Parti SFIO</strong>. <strong>Maire de Montluçon</strong>. Son nom a été donné à la station après 1945."),
            ("🛍️", "Marché Dejean, marché africain", "Le <strong>marché Dejean</strong>, à proximité de la station, est l'un des <strong>principaux marchés africains de Paris</strong>. Situé rue Dejean, au cœur du <strong>quartier de la Goutte d'Or</strong>. Spécialités : <strong>produits africains et antillais</strong>, <strong>fruits exotiques</strong>, <strong>épices</strong>, <strong>poissons frais</strong>. <strong>Atmosphère cosmopolite</strong>, fréquenté par les communautés africaines installées dans le quartier depuis les années 1960.")
        ],
        "itin": [
            ("Gare du Nord", "gare-du-nord", "à pied", "Rue de la Chapelle (10 min)", 10),
            ("Marché Dejean (Goutte d'Or)", "barbes-rochechouart", "M12 + M4", "À pied (5 min) ou M12 → Marcadet + M4", 5),
            ("Marcadet - Poissonniers", "marcadet-poissonniers", "M12", "M12 directe (1 station)", 2),
            ("Saint-Lazare", "saint-lazare", "M12", "M12 directe (~10 min)", 10),
            ("Concorde", "concorde", "M12", "M12 directe (~14 min)", 14),
            ("Montmartre Abbesses", "abbesses", "M12", "M12 directe (3 stations)", 6)
        ]
    },
    "jules-joffrin": {
        "addr": "Place Jules-Joffrin, 75018 Paris", "arr": "18e arrondissement (Paris)",
        "seo": "Station Jules Joffrin (M12) place Jules-Joffrin dans le 18e. Mairie du 18e arrondissement. Quartier Montmartre nord (Clignancourt).",
        "tagline": "M12 — mairie du 18e, Montmartre nord",
        "hero_desc": "Station <strong>Jules Joffrin</strong> sur la <strong>place Jules-Joffrin</strong> dans le <strong>18e arrondissement</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>31 octobre 1912</strong>. À la sortie : la <strong>mairie du 18e arrondissement</strong>. Quartier <strong>Montmartre nord</strong> (Clignancourt).",
        "intros": [
            "La station <strong>Jules Joffrin</strong> est implantée sur la <strong>place Jules-Joffrin</strong> dans le <strong>18e arrondissement</strong>, en face de la <strong>mairie du 18e</strong>. Elle est desservie par la <strong>ligne 12 du métro</strong>, entre <strong>Marcadet - Poissonniers</strong> (1 station) et <strong>Lamarck - Caulaincourt</strong> (1 station). Bus 31, 60, 80, 85.",
            "Ouverte le <strong>31 octobre 1912</strong> avec le prolongement de la <strong>ligne A du Nord-Sud</strong> de Pigalle à Jules Joffrin.",
            "Le nom <strong>Jules Joffrin</strong> rend hommage à <strong>Jules Joffrin</strong> (<strong>1846-1890</strong>), <strong>élu socialiste</strong>, <strong>conseiller municipal et député du 18e arrondissement</strong>. La <strong>mairie du 18e arrondissement</strong> est à la sortie de la station."
        ],
        "hist_title": "1912 : Nord-Sud et mairie du 18e",
        "hist": [
            "La station Jules Joffrin est <strong>inaugurée le 31 octobre 1912</strong> avec le prolongement de la <strong>ligne A du Nord-Sud</strong> (compagnie privée) de <strong>Pigalle à Jules Joffrin</strong>. Intégrée au réseau métropolitain en 1930.",
            "Le nom <strong>Jules Joffrin</strong> rend hommage à <strong>Jules François Alexandre Joffrin</strong> (<strong>1846-1890</strong>), <strong>élu socialiste français</strong>. Ouvrier mécanicien, militant <strong>boulangiste</strong> puis socialiste indépendant. <strong>Conseiller municipal de Paris</strong> et <strong>député du 18e arrondissement</strong>.",
            "La <strong>mairie du 18e arrondissement</strong>, à la sortie de la station, est un édifice de <strong>style néo-Renaissance</strong> construit de <strong>1888 à 1892</strong>. Ses architectes sont <strong>Auguste Joseph Magne</strong> et <strong>Charles Auburtin</strong>. La <strong>basilique du Sacré-Cœur</strong> est à 15 min à pied."
        ],
        "faq": [
            ("Quelle ligne dessert Jules Joffrin ?", "Uniquement la <strong>M12</strong>. Bus 31, 60, 80, 85."),
            ("Qui est Jules Joffrin ?", "<strong>Jules Joffrin</strong> (1846-1890), <strong>élu socialiste français</strong>. <strong>Conseiller municipal de Paris</strong> et <strong>député du 18e arrondissement</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>31 octobre 1912</strong>."),
            ("Pour la mairie du 18e ?", "<strong>Sortie directe</strong>. Édifice néo-Renaissance (1888-1892)."),
            ("Pour le Sacré-Cœur ?", "<strong>~15 min à pied</strong> via la rue Custine."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Mairie du 18e arrondissement</strong> à la sortie : édifice néo-Renaissance.",
            "<strong>Sacré-Cœur de Montmartre</strong> à 15 min à pied.",
            "Pour <strong>Marché Saint-Pierre</strong> (tissus, à Anvers M2) : <strong>~12 min à pied</strong>.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M12 directe</strong> (~8 min).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Mairie du 18e arrondissement", "La <strong>mairie du 18e arrondissement</strong>, à la sortie de la station, est un <strong>édifice de style néo-Renaissance</strong> construit de <strong>1888 à 1892</strong>. Architectes : <strong>Auguste Joseph Magne</strong> et <strong>Charles Auburtin</strong>. La mairie administre le <strong>plus grand arrondissement de Paris</strong> en termes de population (~200 000 habitants). Le <strong>18e</strong> comprend <strong>Montmartre</strong>, la <strong>Goutte d'Or</strong>, <strong>Clignancourt</strong>, <strong>Lariboisière</strong>."),
            ("⛪", "Sacré-Cœur de Montmartre", "La <strong>basilique du Sacré-Cœur de Montmartre</strong>, à 15 min à pied de la station, est l'une des <strong>plus visitées de Paris</strong>. Construite de <strong>1875 à 1914</strong>, consacrée en <strong>1919</strong>. Style <strong>romano-byzantin</strong>, œuvre de <strong>Paul Abadie</strong>. <strong>83 m de haut</strong>. Située au sommet de la <strong>butte Montmartre</strong> (130 m), elle offre un <strong>panorama exceptionnel</strong> sur Paris.")
        ],
        "itin": [
            ("Mairie du 18e", "jules-joffrin", "à pied", "Sortie directe", 1),
            ("Sacré-Cœur", "abbesses", "M12 + à pied", "M12 → Abbesses + funiculaire ou à pied", 15),
            ("Marcadet - Poissonniers", "marcadet-poissonniers", "M12", "M12 directe (1 station)", 2),
            ("Lamarck - Caulaincourt", "lamarck-caulaincourt", "M12", "M12 directe (1 station)", 2),
            ("Saint-Lazare", "saint-lazare", "M12", "M12 directe (~8 min)", 8),
            ("Concorde", "concorde", "M12", "M12 directe (~12 min)", 12)
        ]
    },
    "lamarck-caulaincourt": {
        "addr": "Rue Caulaincourt, 75018 Paris", "arr": "18e arrondissement (Paris)",
        "seo": "Station Lamarck - Caulaincourt (M12) rue Caulaincourt dans le 18e. Naturaliste Lamarck. Cimetière de Montmartre à proximité. Quartier Montmartre nord-ouest.",
        "tagline": "M12 — Lamarck, naturaliste et quartier Montmartre",
        "hero_desc": "Station <strong>Lamarck - Caulaincourt</strong> sur la <strong>rue Caulaincourt</strong> dans le <strong>18e arrondissement</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>31 octobre 1912</strong>. Hommage à <strong>Jean-Baptiste de Lamarck</strong> (<strong>1744-1829</strong>), <strong>naturaliste français</strong>. Quartier <strong>Montmartre nord-ouest</strong>, <strong>cimetière de Montmartre</strong> à proximité.",
        "intros": [
            "La station <strong>Lamarck - Caulaincourt</strong> est implantée sur la <strong>rue Caulaincourt</strong> dans le <strong>18e arrondissement</strong>, sur le flanc nord-ouest de la <strong>butte Montmartre</strong>. Elle est desservie par la <strong>ligne 12 du métro</strong>, entre <strong>Jules Joffrin</strong> (1 station) et <strong>Abbesses</strong> (1 station). Bus 31, 80, 85.",
            "Ouverte le <strong>31 octobre 1912</strong> avec le prolongement de la <strong>ligne A du Nord-Sud</strong> de Pigalle à Jules Joffrin.",
            "Le nom <strong>Lamarck - Caulaincourt</strong> combine deux références : la <strong>rue Lamarck</strong>, hommage à <strong>Jean-Baptiste de Lamarck</strong> (<strong>1744-1829</strong>), <strong>naturaliste français</strong> précurseur de la théorie de l'évolution, et la <strong>rue Caulaincourt</strong>, hommage à <strong>Armand de Caulaincourt</strong> (1773-1827), <strong>général d'Empire et diplomate</strong>."
        ],
        "hist_title": "1912 : Montmartre nord et Lamarck naturaliste",
        "hist": [
            "La station Lamarck - Caulaincourt est <strong>inaugurée le 31 octobre 1912</strong> avec le prolongement de la <strong>ligne A du Nord-Sud</strong> de <strong>Pigalle à Jules Joffrin</strong>.",
            "Le nom <strong>Lamarck</strong> rend hommage à <strong>Jean-Baptiste Pierre Antoine de Monet, chevalier de Lamarck</strong> (<strong>1744-1829</strong>), <strong>naturaliste français</strong>. <strong>Membre de l'Académie des sciences</strong> (1779). <strong>Professeur au Muséum national d'histoire naturelle</strong> (1793).",
            "Lamarck développe la <strong>première théorie de l'évolution</strong> (le <strong>« transformisme »</strong> ou <strong>« lamarckisme »</strong>), exposée dans sa <strong>Philosophie zoologique</strong> (<strong>1809</strong>). Théorie reprise et dépassée plus tard par <strong>Charles Darwin</strong> (<em>De l'origine des espèces</em>, 1859). Le <strong>cimetière de Montmartre</strong>, à 5 min à pied, accueille de nombreuses personnalités : <strong>Émile Zola</strong>, <strong>Hector Berlioz</strong>, <strong>Stendhal</strong>, <strong>Edgar Degas</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Lamarck - Caulaincourt ?", "Uniquement la <strong>M12</strong>. Bus 31, 80, 85."),
            ("Qui est Lamarck ?", "<strong>Jean-Baptiste de Lamarck</strong> (1744-1829), <strong>naturaliste français</strong>. <strong>Premier théoricien de l'évolution</strong> (transformisme). <strong>Professeur au Muséum national d'histoire naturelle</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>31 octobre 1912</strong>."),
            ("Pour le cimetière de Montmartre ?", "<strong>~5 min à pied</strong> via la rue Caulaincourt. Tombes de Zola, Berlioz, Stendhal, Degas."),
            ("Pour le Sacré-Cœur ?", "<strong>~10 min à pied</strong> en montant la butte."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur, dénivelé important.")
        ],
        "tips": [
            "<strong>Cimetière de Montmartre</strong> à 5 min : tombes de Zola, Berlioz, Stendhal, Degas, Truffaut.",
            "<strong>Sacré-Cœur</strong> à 10 min à pied (côté nord, montée).",
            "<strong>Rue Caulaincourt</strong> : axe traversant la butte Montmartre.",
            "Pour <strong>Abbesses</strong> et la <strong>place du Tertre</strong> : <strong>M12 directe</strong> (1 station).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🧬", "Lamarck, premier théoricien de l'évolution", "<strong>Jean-Baptiste de Lamarck</strong> (1744-1829), <strong>naturaliste français</strong>. <strong>Membre de l'Académie des sciences</strong> (1779). <strong>Professeur au Muséum national d'histoire naturelle</strong> (1793). Développe la <strong>première théorie cohérente de l'évolution</strong> dans sa <strong><em>Philosophie zoologique</em></strong> (<strong>1809</strong>). <strong>Théorie du transformisme</strong> ou <strong>« lamarckisme »</strong> : transmission des caractères acquis aux descendants. Théorie reprise et dépassée par <strong>Charles Darwin</strong> dans <em>De l'origine des espèces</em> (1859). Considéré comme le <strong>fondateur de la biologie moderne</strong>."),
            ("🪦", "Cimetière de Montmartre, panthéon artistique", "Le <strong>cimetière de Montmartre</strong>, à 5 min à pied de la station, est l'un des <strong>plus importants cimetières parisiens</strong>. <strong>Ouvert en 1825</strong>. Tombes de nombreuses <strong>personnalités</strong> : <strong>Émile Zola</strong> (avant transfert au Panthéon), <strong>Hector Berlioz</strong>, <strong>Stendhal</strong> (Henri Beyle), <strong>Edgar Degas</strong>, <strong>Vaslav Nijinsky</strong>, <strong>François Truffaut</strong>, <strong>Dalida</strong>, <strong>Vincent Vega</strong>.")
        ],
        "itin": [
            ("Cimetière de Montmartre", "lamarck-caulaincourt", "à pied", "Rue Caulaincourt (5 min)", 5),
            ("Sacré-Cœur", "abbesses", "M12 + funiculaire", "M12 directe ou à pied (10 min)", 10),
            ("Abbesses (Montmartre)", "abbesses", "M12", "M12 directe (1 station)", 2),
            ("Jules Joffrin", "jules-joffrin", "M12", "M12 directe (1 station)", 2),
            ("Saint-Lazare", "saint-lazare", "M12", "M12 directe (~6 min)", 6),
            ("Concorde", "concorde", "M12", "M12 directe (~10 min)", 10)
        ]
    },
    "saint-georges": {
        "addr": "Place Saint-Georges, 75009 Paris", "arr": "9e arrondissement (Paris)",
        "seo": "Station Saint-Georges (M12) place Saint-Georges dans le 9e. Quartier romantique de la Nouvelle Athènes. Hôtels particuliers du XIXe siècle.",
        "tagline": "M12 — quartier romantique de la Nouvelle Athènes",
        "hero_desc": "Station <strong>Saint-Georges</strong> sur la <strong>place Saint-Georges</strong> dans le <strong>9e arrondissement</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>5 novembre 1910</strong>. Au cœur du <strong>quartier de la Nouvelle Athènes</strong>, secteur résidentiel chic du <strong>9e</strong>.",
        "intros": [
            "La station <strong>Saint-Georges</strong> est implantée sur la <strong>place Saint-Georges</strong> dans le <strong>9e arrondissement</strong>. Elle est desservie par la <strong>ligne 12 du métro</strong>, entre <strong>Pigalle</strong> (1 station) et <strong>Notre-Dame-de-Lorette</strong> (1 station). Bus 67, 74.",
            "Ouverte le <strong>5 novembre 1910</strong> avec le tronçon initial de la <strong>ligne A du Nord-Sud</strong>.",
            "La station est implantée au cœur du <strong>quartier de la Nouvelle Athènes</strong>, secteur résidentiel chic du <strong>9e arrondissement</strong> aménagé sous la <strong>Restauration</strong> et la <strong>Monarchie de Juillet</strong>. Nombreux <strong>hôtels particuliers du XIXe siècle</strong>, demeures d'artistes du <strong>romantisme</strong> (<strong>Eugène Delacroix</strong>, <strong>George Sand</strong>, <strong>Frédéric Chopin</strong>, <strong>Georges Bizet</strong>)."
        ],
        "hist_title": "1910 : Nord-Sud et Nouvelle Athènes",
        "hist": [
            "La station Saint-Georges est <strong>inaugurée le 5 novembre 1910</strong> avec le tronçon initial <strong>Porte de Versailles ↔ Notre-Dame-de-Lorette</strong> de la <strong>ligne A du Nord-Sud</strong> (compagnie privée).",
            "Le quartier de la <strong>Nouvelle Athènes</strong>, autour de la station, est un <strong>secteur résidentiel chic du 9e arrondissement</strong> aménagé sous la <strong>Restauration</strong> (1815-1830) et la <strong>Monarchie de Juillet</strong> (1830-1848). Il doit son nom à la <strong>fascination de l'époque pour la Grèce antique</strong> et la <strong>guerre d'indépendance grecque</strong> (1821-1832).",
            "Le quartier accueille de nombreux <strong>artistes et écrivains romantiques</strong> au XIXe siècle : <strong>Eugène Delacroix</strong> (atelier place de Furstenberg, mais aussi rue Notre-Dame-de-Lorette), <strong>George Sand</strong> et <strong>Frédéric Chopin</strong> (au 16 rue Pigalle), <strong>Georges Bizet</strong> (compositeur de <em>Carmen</em>), <strong>Hector Berlioz</strong>, <strong>Théodore Géricault</strong>. <strong>Musée de la Vie romantique</strong> à proximité (16 rue Chaptal)."
        ],
        "faq": [
            ("Quelle ligne dessert Saint-Georges ?", "Uniquement la <strong>M12</strong>. Bus 67, 74."),
            ("Qu'est-ce que la Nouvelle Athènes ?", "<strong>Secteur résidentiel chic du 9e</strong> aménagé sous la Restauration. Nom évoquant la fascination romantique pour la <strong>Grèce antique</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>."),
            ("Pour le musée de la Vie romantique ?", "<strong>~5 min à pied</strong> via la rue Chaptal."),
            ("Pour Pigalle ?", "<strong>M12 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Musée de la Vie romantique</strong> à 5 min : ancienne demeure d'Ary Scheffer, souvenirs de George Sand.",
            "Quartier <strong>Nouvelle Athènes</strong> : architecture XIXe.",
            "Pour <strong>Pigalle</strong> et <strong>Moulin Rouge</strong> : <strong>M12 directe</strong>.",
            "Pour <strong>Opéra Garnier</strong> : <strong>M12 directe</strong> + à pied (~7 min).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎨", "Nouvelle Athènes, quartier romantique", "Le <strong>quartier de la Nouvelle Athènes</strong>, autour de la station, est un <strong>secteur résidentiel chic du 9e</strong> aménagé sous la <strong>Restauration</strong> (1815-1830) et la <strong>Monarchie de Juillet</strong>. Doit son nom à la <strong>fascination de l'époque pour la Grèce antique</strong>. Accueillit de nombreux <strong>artistes romantiques</strong> : <strong>Eugène Delacroix</strong>, <strong>George Sand</strong>, <strong>Frédéric Chopin</strong>, <strong>Georges Bizet</strong>, <strong>Hector Berlioz</strong>, <strong>Théodore Géricault</strong>. <strong>Hôtels particuliers</strong> élégants, atmosphère intime."),
            ("🎵", "Musée de la Vie romantique", "Le <strong>musée de la Vie romantique</strong>, à 5 min à pied (16 rue Chaptal), est installé dans l'<strong>ancienne demeure du peintre Ary Scheffer</strong> (1795-1858). Ouvert en <strong>1987</strong>. Collections de <strong>souvenirs de George Sand</strong> (manuscrits, bijoux, portraits, meubles), tableaux de l'<strong>époque romantique</strong>. Atmosphère <strong>intime XIXe siècle</strong> avec <strong>jardin et salon de thé</strong>.")
        ],
        "itin": [
            ("Musée de la Vie romantique", "saint-georges", "à pied", "Rue Chaptal (5 min)", 5),
            ("Pigalle", "pigalle", "M12", "M12 directe (1 station)", 2),
            ("Notre-Dame-de-Lorette", "notre-dame-de-lorette", "M12", "M12 directe (1 station)", 2),
            ("Opéra Garnier", "opera", "M12 + M3 ou à pied", "À pied (10 min) ou M12 + M3", 7),
            ("Galeries Lafayette", "chaussee-d-antin-la-fayette", "M12", "M12 directe (3 stations)", 6),
            ("Saint-Lazare", "saint-lazare", "M12", "M12 directe (~4 min)", 4)
        ]
    },
    "notre-dame-de-lorette": {
        "addr": "Rue Saint-Lazare, 75009 Paris", "arr": "9e arrondissement (Paris)",
        "seo": "Station Notre-Dame-de-Lorette (M12) rue Saint-Lazare dans le 9e. Église Notre-Dame-de-Lorette (1836, néo-classique). Quartier de la Nouvelle Athènes.",
        "tagline": "M12 — église néo-classique de 1836",
        "hero_desc": "Station <strong>Notre-Dame-de-Lorette</strong> sur la <strong>rue Saint-Lazare</strong> dans le <strong>9e arrondissement</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>5 novembre 1910</strong>. À la sortie : l'<strong>église Notre-Dame-de-Lorette</strong> (<strong>1836</strong>), édifice <strong>néo-classique</strong>.",
        "intros": [
            "La station <strong>Notre-Dame-de-Lorette</strong> est implantée sur la <strong>rue Saint-Lazare</strong> dans le <strong>9e arrondissement</strong>. Elle est desservie par la <strong>ligne 12 du métro</strong>, entre <strong>Saint-Georges</strong> (1 station) et <strong>Trinité - d'Estienne d'Orves</strong> (1 station). Bus 26, 32, 43, 49, 67, 74.",
            "Ouverte le <strong>5 novembre 1910</strong> comme <strong>terminus sud temporaire</strong> du tronçon initial de la <strong>ligne A du Nord-Sud</strong>, jusqu'au prolongement vers Pigalle puis Jules Joffrin (1912).",
            "À la sortie : l'<strong>église Notre-Dame-de-Lorette</strong>, édifice <strong>néo-classique</strong> construit de <strong>1823 à 1836</strong> par <strong>Hippolyte Le Bas</strong>. Quartier <strong>Nouvelle Athènes</strong>, résidentiel chic du <strong>9e</strong>. À courte distance : <strong>cathédrale orthodoxe russe Saint-Alexandre-Nevsky</strong>."
        ],
        "hist_title": "1910 : église néo-classique de 1836",
        "hist": [
            "La station Notre-Dame-de-Lorette est <strong>inaugurée le 5 novembre 1910</strong> comme <strong>terminus sud temporaire</strong> du tronçon initial <strong>Porte de Versailles ↔ Notre-Dame-de-Lorette</strong> de la <strong>ligne A du Nord-Sud</strong>.",
            "L'<strong>église Notre-Dame-de-Lorette</strong>, à la sortie, est un <strong>édifice religieux néo-classique</strong> construit de <strong>1823 à 1836</strong> par l'architecte <strong>Hippolyte Le Bas</strong>. <strong>Façade à colonnade corinthienne</strong> inspirée des temples antiques romains. Dédiée à <strong>Notre-Dame-de-Lorette</strong> (<strong>Madone de Lorette</strong> en Italie).",
            "Le quartier autour de la station fait partie de la <strong>Nouvelle Athènes</strong>, secteur résidentiel chic du <strong>9e arrondissement</strong>. À courte distance : la <strong>cathédrale orthodoxe russe Saint-Alexandre-Nevsky</strong> (1861, rue Daru), le <strong>musée Gustave Moreau</strong>, le <strong>musée de la Vie romantique</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Notre-Dame-de-Lorette ?", "Uniquement la <strong>M12</strong>. Bus 26, 32, 43, 49, 67, 74."),
            ("Qu'est-ce que l'église Notre-Dame-de-Lorette ?", "<strong>Édifice néo-classique</strong> construit de <strong>1823 à 1836</strong> par <strong>Hippolyte Le Bas</strong>. Façade à colonnade corinthienne inspirée des temples antiques."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>."),
            ("Pour le musée Gustave Moreau ?", "<strong>~7 min à pied</strong> via la rue de La Rochefoucauld."),
            ("Pour la cathédrale orthodoxe russe ?", "<strong>~15 min à pied</strong> via le 8e arrondissement (rue Daru)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Église Notre-Dame-de-Lorette</strong> à la sortie : édifice néo-classique 1836.",
            "<strong>Musée Gustave Moreau</strong> à 7 min : ancienne demeure du peintre symboliste.",
            "<strong>Musée de la Vie romantique</strong> à 10 min.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M12 directe</strong> (~4 min).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⛪", "Église Notre-Dame-de-Lorette (1836)", "L'<strong>église Notre-Dame-de-Lorette</strong>, à la sortie de la station, est un <strong>édifice religieux néo-classique</strong> construit de <strong>1823 à 1836</strong> par l'architecte <strong>Hippolyte Le Bas</strong>. <strong>Façade à colonnade corinthienne</strong> inspirée des <strong>temples antiques romains</strong>. Dédiée à <strong>Notre-Dame-de-Lorette</strong> (<strong>Madone de Lorette</strong> en Italie). <strong>Inscrite aux monuments historiques en 1984</strong>."),
            ("🎨", "Musée Gustave Moreau", "Le <strong>musée Gustave Moreau</strong>, à 7 min à pied (14 rue de La Rochefoucauld), est installé dans l'<strong>ancienne demeure du peintre symboliste Gustave Moreau</strong> (1826-1898). Ouvert en <strong>1903</strong>. <strong>~1 300 peintures et aquarelles</strong>, <strong>5 000 dessins</strong>. Atmosphère <strong>fin XIXe siècle</strong> préservée. L'un des <strong>plus importants musées d'un seul artiste</strong> en France.")
        ],
        "itin": [
            ("Église Notre-Dame-de-Lorette", "notre-dame-de-lorette", "à pied", "Sortie directe", 1),
            ("Musée Gustave Moreau", "notre-dame-de-lorette", "à pied", "Rue de La Rochefoucauld (7 min)", 7),
            ("Musée de la Vie romantique", "saint-georges", "M12", "M12 → Saint-Georges + à pied", 10),
            ("Saint-Lazare", "saint-lazare", "M12", "M12 directe (~4 min)", 4),
            ("Galeries Lafayette", "chaussee-d-antin-la-fayette", "M12 + M9", "M12 → Saint-Lazare + M9", 8),
            ("Opéra Garnier", "opera", "M12 + M3 ou à pied", "À pied (10 min)", 10)
        ]
    },
    "trinite-d-estienne-d-orves": {
        "addr": "Rue Saint-Lazare, 75009 Paris", "arr": "9e arrondissement (Paris)",
        "seo": "Station Trinité - d'Estienne d'Orves (M12) rue Saint-Lazare dans le 9e. Église de la Sainte-Trinité (1867). Quartier 9e résidentiel.",
        "tagline": "M12 — église de la Sainte-Trinité (1867)",
        "hero_desc": "Station <strong>Trinité - d'Estienne d'Orves</strong> sur la <strong>rue Saint-Lazare</strong> dans le <strong>9e arrondissement</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>13 juillet 1911</strong>. À la sortie : l'<strong>église de la Sainte-Trinité</strong> (<strong>1867</strong>), édifice néo-Renaissance.",
        "intros": [
            "La station <strong>Trinité - d'Estienne d'Orves</strong> est implantée sur la <strong>rue Saint-Lazare</strong> dans le <strong>9e arrondissement</strong>. Elle est desservie par la <strong>ligne 12 du métro</strong>, entre <strong>Notre-Dame-de-Lorette</strong> (1 station) et <strong>Saint-Lazare</strong> (1 station). Bus 26, 32, 43, 49, 67, 68, 74, 81.",
            "Ouverte le <strong>13 juillet 1911</strong> avec le prolongement de la <strong>ligne A du Nord-Sud</strong>. Renommée le <strong>16 mai 1946</strong> en l'honneur de l'<strong>officier de marine Honoré d'Estienne d'Orves</strong> (1901-1941).",
            "À la sortie : l'<strong>église de la Sainte-Trinité</strong>, édifice <strong>néo-Renaissance</strong> construit de <strong>1861 à 1867</strong> par <strong>Théodore Ballu</strong>. <strong>Façade à clocher-porche</strong> de <strong>63 m de haut</strong>. À l'intérieur, <strong>orgue Cavaillé-Coll</strong> sur lequel jouèrent <strong>Olivier Messiaen</strong> et <strong>Charles-Marie Widor</strong>."
        ],
        "hist_title": "1911 : église néo-Renaissance et hommage 1946",
        "hist": [
            "La station Trinité est <strong>inaugurée le 13 juillet 1911</strong> sous le nom <strong>« Trinité »</strong>, avec le prolongement de la <strong>ligne A du Nord-Sud</strong>.",
            "Le <strong>16 mai 1946</strong>, la station est <strong>renommée Trinité - d'Estienne d'Orves</strong>. Le nom rend hommage à <strong>Honoré d'Estienne d'Orves</strong> (<strong>1901-1941</strong>), <strong>officier de marine français</strong>.",
            "L'<strong>église de la Sainte-Trinité</strong>, à la sortie, est un <strong>édifice religieux néo-Renaissance</strong> construit de <strong>1861 à 1867</strong> par l'architecte <strong>Théodore Ballu</strong>. <strong>Façade à clocher-porche</strong> de <strong>63 m de haut</strong>. <strong>Orgue Cavaillé-Coll</strong> (1869) sur lequel jouèrent <strong>Olivier Messiaen</strong> (titulaire de 1931 à 1992), <strong>Charles-Marie Widor</strong>, et plusieurs grands organistes français."
        ],
        "faq": [
            ("Quelle ligne dessert Trinité - d'Estienne d'Orves ?", "Uniquement la <strong>M12</strong>. Bus 26, 32, 43, 49, 67, 68, 74, 81."),
            ("Qu'est-ce que l'église de la Sainte-Trinité ?", "<strong>Édifice religieux néo-Renaissance</strong> construit de <strong>1861 à 1867</strong> par <strong>Théodore Ballu</strong>. Clocher-porche de 63 m. <strong>Orgue Cavaillé-Coll</strong> de 1869."),
            ("Quand a-t-elle ouvert ?", "Le <strong>13 juillet 1911</strong>, renommée le <strong>16 mai 1946</strong>."),
            ("Pour Saint-Lazare ?", "<strong>M12 directe</strong> (1 station, ~2 min)."),
            ("Pour l'opéra Garnier ?", "<strong>~10 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Église de la Sainte-Trinité</strong> à la sortie : édifice néo-Renaissance 1867, orgue Cavaillé-Coll.",
            "<strong>Olivier Messiaen</strong> y fut <strong>titulaire de l'orgue de 1931 à 1992</strong> (61 ans).",
            "Pour <strong>Saint-Lazare</strong> : <strong>M12 directe</strong>.",
            "Pour <strong>Galeries Lafayette</strong> : <strong>M12 + M9</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⛪", "Église de la Sainte-Trinité (1867)", "L'<strong>église de la Sainte-Trinité</strong>, à la sortie de la station, est un <strong>édifice religieux néo-Renaissance</strong> construit de <strong>1861 à 1867</strong> par l'architecte <strong>Théodore Ballu</strong>. <strong>Façade à clocher-porche</strong> de <strong>63 m de haut</strong>. <strong>Inscrite aux monuments historiques en 1984</strong>. Style éclectique mêlant influences <strong>Renaissance française et italienne</strong>. À l'intérieur, <strong>orgue Cavaillé-Coll</strong> de <strong>1869</strong> sur lequel se sont succédé de grands organistes."),
            ("🎹", "Olivier Messiaen et l'orgue de la Trinité", "<strong>Olivier Messiaen</strong> (1908-1992), <strong>compositeur français majeur</strong> du XXe siècle, fut <strong>titulaire de l'orgue de la Sainte-Trinité pendant 61 ans</strong> (<strong>1931 à 1992</strong>). Il y créa de nombreuses de ses <strong>œuvres pour orgue</strong> : <em>La Nativité du Seigneur</em> (1935), <em>Les Corps glorieux</em> (1939), <em>Méditations sur le mystère de la Sainte Trinité</em> (1969), <em>Livre du Saint Sacrement</em> (1984).")
        ],
        "itin": [
            ("Église de la Sainte-Trinité", "trinite-d-estienne-d-orves", "à pied", "Sortie directe", 1),
            ("Saint-Lazare", "saint-lazare", "M12", "M12 directe (1 station)", 2),
            ("Galeries Lafayette", "chaussee-d-antin-la-fayette", "M12 + M9", "M12 → Saint-Lazare + M9", 6),
            ("Opéra Garnier", "opera", "M12 + M3 ou à pied", "À pied (10 min)", 10),
            ("Pigalle", "pigalle", "M12", "M12 directe (3 stations)", 6),
            ("Madeleine", "madeleine", "M12", "M12 directe (~6 min)", 6)
        ]
    },
    "assemblee-nationale": {
        "addr": "Quai d'Orsay, 75007 Paris", "arr": "7e arrondissement (Paris)",
        "seo": "Station Assemblée Nationale (M12) quai d'Orsay dans le 7e. Palais Bourbon, siège de l'Assemblée nationale française depuis 1798.",
        "tagline": "M12 — Palais Bourbon, Assemblée nationale",
        "hero_desc": "Station <strong>Assemblée Nationale</strong> sur le <strong>quai d'Orsay</strong> dans le <strong>7e arrondissement</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>5 novembre 1910</strong>. À la sortie : le <strong>Palais Bourbon</strong>, siège de l'<strong>Assemblée nationale française</strong> depuis 1798.",
        "intros": [
            "La station <strong>Assemblée Nationale</strong> est implantée sur le <strong>quai d'Orsay</strong> dans le <strong>7e arrondissement</strong>. Elle est desservie par la <strong>ligne 12 du métro</strong>, entre <strong>Concorde</strong> (1 station) et <strong>Solférino</strong> (1 station). Bus 63, 73, 83, 84, 94.",
            "Ouverte le <strong>5 novembre 1910</strong> sous le nom <strong>« Chambre des députés »</strong>. Renommée <strong>« Assemblée Nationale »</strong> en <strong>1989</strong>, à l'occasion du <strong>bicentenaire de la Révolution française</strong>.",
            "À la sortie : le <strong>Palais Bourbon</strong>, <strong>siège de l'Assemblée nationale française</strong>. Construit de <strong>1722 à 1728</strong> pour <strong>Louise-Françoise de Bourbon</strong>, fille légitimée de <strong>Louis XIV</strong>. <strong>Façade néo-classique à colonnade corinthienne</strong> ajoutée en <strong>1806-1810</strong> par <strong>Bernard Poyet</strong> pour faire face au <strong>temple de la Madeleine</strong> de l'autre côté de la Seine."
        ],
        "hist_title": "1910 : Palais Bourbon depuis 1722",
        "hist": [
            "La station est <strong>inaugurée le 5 novembre 1910</strong> sous le nom <strong>« Chambre des députés »</strong>, avec le tronçon initial de la <strong>ligne A du Nord-Sud</strong>. <strong>Renommée « Assemblée Nationale »</strong> en <strong>1989</strong>, à l'occasion du <strong>bicentenaire de la Révolution française</strong>.",
            "Le <strong>Palais Bourbon</strong>, à la sortie, est construit de <strong>1722 à 1728</strong> pour <strong>Louise-Françoise de Bourbon</strong>, fille légitimée de <strong>Louis XIV</strong>. Architectes : <strong>Lorenzo Giardini</strong> et <strong>Pierre Cailleteau</strong>.",
            "Le palais devient <strong>siège du Conseil des Cinq-Cents</strong> en <strong>1798</strong> sous le <strong>Directoire</strong>, puis <strong>siège de la Chambre des députés</strong> sous la Restauration et la Monarchie de Juillet, puis du <strong>Corps législatif</strong> sous le Second Empire, et enfin de l'<strong>Assemblée nationale</strong> sous la Troisième République et depuis. La <strong>façade néo-classique à colonnade corinthienne</strong> donnant sur la Seine est ajoutée en <strong>1806-1810</strong> par <strong>Bernard Poyet</strong> pour faire face au <strong>temple de la Madeleine</strong> de l'autre côté du fleuve."
        ],
        "faq": [
            ("Quelle ligne dessert Assemblée Nationale ?", "Uniquement la <strong>M12</strong>. Bus 63, 73, 83, 84, 94."),
            ("Quel était l'ancien nom ?", "<strong>« Chambre des députés »</strong> (1910-1989)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>, renommée en <strong>1989</strong>."),
            ("Qu'est-ce que le Palais Bourbon ?", "<strong>Siège de l'Assemblée nationale française</strong>. Construit de <strong>1722 à 1728</strong> pour Louise-Françoise de Bourbon. Façade néo-classique de 1806-1810."),
            ("Peut-on visiter le Palais Bourbon ?", "<strong>Oui</strong>, sur réservation et les <strong>Journées européennes du patrimoine</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Palais Bourbon</strong> à la sortie : siège de l'Assemblée nationale (visites guidées sur réservation).",
            "<strong>Esplanade des Invalides</strong> à proximité.",
            "<strong>Pont de la Concorde</strong> à 5 min à pied.",
            "Pour <strong>Concorde</strong> : <strong>M12 directe</strong> (1 station).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Palais Bourbon, siège de l'Assemblée nationale", "Le <strong>Palais Bourbon</strong>, à la sortie de la station, est le <strong>siège de l'Assemblée nationale française</strong>. Construit de <strong>1722 à 1728</strong> pour <strong>Louise-Françoise de Bourbon</strong>, fille légitimée de <strong>Louis XIV</strong>. <strong>Façade néo-classique à colonnade corinthienne</strong> ajoutée en <strong>1806-1810</strong> par <strong>Bernard Poyet</strong> sous l'<strong>Empire</strong>, pour répondre à la <strong>colonnade de la Madeleine</strong> de l'autre côté de la Seine. Devient <strong>siège du Conseil des Cinq-Cents</strong> en <strong>1798</strong>, puis successivement de la Chambre des députés et de l'Assemblée nationale."),
            ("📜", "Bicentenaire de la Révolution (1989)", "C'est à l'occasion du <strong>bicentenaire de la Révolution française</strong> en <strong>1989</strong> que la station change de nom, passant de <strong>« Chambre des députés »</strong> (nom datant de 1910) à <strong>« Assemblée Nationale »</strong>. Les <strong>célébrations du bicentenaire</strong> furent marquées notamment par le <strong>défilé du 14 juillet 1989</strong> sur les Champs-Élysées, orchestré par <strong>Jean-Paul Goude</strong>, et l'<strong>inauguration de la Grande Arche de la Défense</strong>.")
        ],
        "itin": [
            ("Palais Bourbon", "assemblee-nationale", "à pied", "Sortie directe", 1),
            ("Concorde", "concorde", "M12", "M12 directe (1 station)", 2),
            ("Invalides", "invalides", "M12 + M13", "M12 → Concorde + M13", 6),
            ("Musée d'Orsay", "musee-d-orsay", "M12 + à pied", "M12 → Solférino + à pied", 5),
            ("Madeleine", "madeleine", "M12", "M12 directe (~5 min)", 5),
            ("Champs-Élysées", "champs-elysees-clemenceau", "M12 + M1", "M12 → Concorde + M1", 7)
        ]
    },
    "rue-du-bac": {
        "addr": "Boulevard Raspail, 75007 Paris", "arr": "7e arrondissement (Paris)",
        "seo": "Station Rue du Bac (M12) boulevard Raspail dans le 7e. Rue du Bac axe historique. Chapelle Notre-Dame de la Médaille Miraculeuse à proximité.",
        "tagline": "M12 — rue du Bac, Saint-Germain rive gauche",
        "hero_desc": "Station <strong>Rue du Bac</strong> sur le <strong>boulevard Raspail</strong> dans le <strong>7e arrondissement</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>5 novembre 1910</strong>. La <strong>rue du Bac</strong>, axe historique du <strong>7e</strong>, accueille <strong>antiquaires</strong>, <strong>librairies</strong>, <strong>galeries d'art</strong>. <strong>Chapelle Notre-Dame-de-la-Médaille-Miraculeuse</strong> à proximité.",
        "intros": [
            "La station <strong>Rue du Bac</strong> est implantée sur le <strong>boulevard Raspail</strong> dans le <strong>7e arrondissement</strong>. Elle est desservie par la <strong>ligne 12 du métro</strong>, entre <strong>Solférino</strong> (1 station) et <strong>Sèvres - Babylone</strong> (1 station). Bus 39, 63, 68, 69, 70, 83, 84, 94.",
            "Ouverte le <strong>5 novembre 1910</strong> avec le tronçon initial de la <strong>ligne A du Nord-Sud</strong>.",
            "La <strong>rue du Bac</strong>, longue de <strong>1,2 km</strong>, est l'un des <strong>axes historiques du 7e arrondissement</strong>. Tracée à partir du <strong>XVIIe siècle</strong>, elle doit son nom au <strong>bac</strong> qui permettait de traverser la Seine. Aujourd'hui, elle concentre <strong>antiquaires</strong>, <strong>librairies anciennes</strong>, <strong>galeries d'art</strong>, <strong>fromageries</strong> et <strong>chocolateries de luxe</strong>. À proximité : la <strong>chapelle Notre-Dame-de-la-Médaille-Miraculeuse</strong>, l'<strong>Hôtel Lutetia</strong> et le <strong>Bon Marché</strong>."
        ],
        "hist_title": "1910 : rue du Bac et chapelle de la Médaille",
        "hist": [
            "La station Rue du Bac est <strong>inaugurée le 5 novembre 1910</strong> avec le tronçon initial <strong>Porte de Versailles ↔ Notre-Dame-de-Lorette</strong> de la <strong>ligne A du Nord-Sud</strong>.",
            "La <strong>rue du Bac</strong>, qui donne son nom à la station, est tracée à partir du <strong>XVIIe siècle</strong>. Son nom vient du <strong>bac</strong> qui permettait alors de traverser la Seine pour transporter les pierres du chantier des Tuileries. Avenue commerçante prestigieuse du <strong>7e arrondissement</strong>, atypique avec ses <strong>antiquaires</strong>, <strong>libraires</strong>, <strong>galeries d'art</strong>.",
            "À proximité : la <strong>chapelle Notre-Dame-de-la-Médaille-Miraculeuse</strong> (140 rue du Bac), <strong>lieu de pèlerinage majeur</strong> de la chrétienté. Sœur <strong>Catherine Labouré</strong> y reçut en <strong>1830</strong> des apparitions de la <strong>Vierge Marie</strong>, à l'origine de la frappe de la <strong>Médaille miraculeuse</strong>. <strong>~2 millions de pèlerins par an</strong>. À courte distance également : <strong>Le Bon Marché</strong> (1838), l'<strong>Hôtel Lutetia</strong> (1910), <strong>musée Maillol</strong> (1995)."
        ],
        "faq": [
            ("Quelle ligne dessert Rue du Bac ?", "Uniquement la <strong>M12</strong>. Bus 39, 63, 68, 69, 70, 83, 84, 94."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>."),
            ("Qu'est-ce que la chapelle Notre-Dame-de-la-Médaille-Miraculeuse ?", "<strong>Lieu de pèlerinage majeur</strong> de la chrétienté (140 rue du Bac). Sœur <strong>Catherine Labouré</strong> y reçut en <strong>1830</strong> des apparitions de la Vierge."),
            ("Pour le musée Maillol ?", "<strong>~5 min à pied</strong> via la rue de Grenelle."),
            ("Pour Le Bon Marché ?", "<strong>~7 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Rue du Bac</strong> : antiquaires, librairies, galeries d'art, fromageries et chocolateries de luxe.",
            "<strong>Chapelle Notre-Dame-de-la-Médaille-Miraculeuse</strong> (140 rue du Bac) : 2 millions de pèlerins/an.",
            "<strong>Le Bon Marché</strong> à 7 min à pied : premier grand magasin (1838).",
            "<strong>Musée Maillol</strong> à 5 min à pied.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⛪", "Chapelle Notre-Dame-de-la-Médaille-Miraculeuse", "La <strong>chapelle Notre-Dame-de-la-Médaille-Miraculeuse</strong>, à proximité de la station (<strong>140 rue du Bac</strong>), est l'un des <strong>lieux de pèlerinage majeurs</strong> de la chrétienté. Sœur <strong>Catherine Labouré</strong> y reçut en <strong>1830</strong> des <strong>apparitions de la Vierge Marie</strong>, à l'origine de la frappe de la <strong>Médaille miraculeuse</strong>. Plus de <strong>1 milliard de médailles</strong> auraient été frappées depuis. <strong>~2 millions de pèlerins par an</strong> visitent la chapelle."),
            ("🎨", "Musée Maillol", "Le <strong>musée Maillol</strong>, à 5 min à pied (61 rue de Grenelle), est consacré au sculpteur <strong>Aristide Maillol</strong> (1861-1944). <strong>Fondé en 1995</strong> par <strong>Dina Vierny</strong> (modèle et muse de Maillol). <strong>Sculptures, dessins et peintures de Maillol</strong>, ainsi que des œuvres de <strong>Matisse, Picasso, Bonnard, Degas, Cézanne, Gauguin</strong>. <strong>Expositions temporaires</strong> reconnues.")
        ],
        "itin": [
            ("Chapelle Notre-Dame-de-la-Médaille-Miraculeuse", "rue-du-bac", "à pied", "Rue du Bac (3 min)", 3),
            ("Le Bon Marché", "sevres-babylone", "M12", "M12 directe (1 station) ou à pied (7 min)", 5),
            ("Musée Maillol", "rue-du-bac", "à pied", "Rue de Grenelle (5 min)", 5),
            ("Musée d'Orsay", "solferino", "M12 + à pied", "M12 → Solférino + à pied (5 min)", 5),
            ("Saint-Germain-des-Prés", "saint-germain-des-pres", "M12 + M4", "M12 → Sèvres-Babylone + M12", 6),
            ("Concorde", "concorde", "M12", "M12 directe (~6 min)", 6)
        ]
    },
    "rennes": {
        "addr": "Rue de Rennes, 75006 Paris", "arr": "6e arrondissement (Paris)",
        "seo": "Station Rennes (M12) rue de Rennes dans le 6e. Quartier Saint-Germain-des-Prés. Place Saint-Sulpice à proximité.",
        "tagline": "M12 — rue de Rennes, Saint-Germain rive gauche",
        "hero_desc": "Station <strong>Rennes</strong> sur la <strong>rue de Rennes</strong> dans le <strong>6e arrondissement</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>5 novembre 1910</strong>. <strong>Quartier Saint-Germain-des-Prés</strong>. À proximité de la <strong>place Saint-Sulpice</strong>.",
        "intros": [
            "La station <strong>Rennes</strong> est implantée sur la <strong>rue de Rennes</strong> dans le <strong>6e arrondissement</strong>. Elle est desservie par la <strong>ligne 12 du métro</strong>, entre <strong>Sèvres - Babylone</strong> (1 station) et <strong>Notre-Dame-des-Champs</strong> (1 station). Bus 39, 95.",
            "Ouverte le <strong>5 novembre 1910</strong> avec le tronçon initial de la <strong>ligne A du Nord-Sud</strong>. <strong>Fermée pendant 35 ans</strong> (1939-1968) en raison de sa proximité avec la station Saint-Placide.",
            "La <strong>rue de Rennes</strong>, qui donne son nom à la station, est tracée sous le <strong>Second Empire</strong> (1853-1864). Elle relie la <strong>gare Montparnasse</strong> à <strong>Saint-Germain-des-Prés</strong>. Le quartier autour de la station appartient à <strong>Saint-Germain-des-Prés</strong>, secteur historique du <strong>6e arrondissement</strong>. À proximité : la <strong>place Saint-Sulpice</strong> et son <strong>église Saint-Sulpice</strong>."
        ],
        "hist_title": "1910 : rue de Rennes et fermeture 1939-1968",
        "hist": [
            "La station Rennes est <strong>inaugurée le 5 novembre 1910</strong> avec le tronçon initial <strong>Porte de Versailles ↔ Notre-Dame-de-Lorette</strong> de la <strong>ligne A du Nord-Sud</strong>.",
            "Particularité : la station est <strong>fermée pendant 35 ans</strong>, de <strong>1939 à 1968</strong>, en raison de sa <strong>proximité avec la station Saint-Placide</strong>. <strong>Rouverte le 20 mai 1968</strong> en pleine effervescence des <strong>événements de Mai 68</strong>.",
            "La <strong>rue de Rennes</strong>, tracée sous le <strong>Second Empire</strong> (1853-1864), relie la <strong>gare Montparnasse</strong> à <strong>Saint-Germain-des-Prés</strong>. Elle constitue l'un des <strong>axes commerciaux majeurs</strong> du <strong>6e arrondissement</strong>. À proximité : la <strong>place Saint-Sulpice</strong> (XVIIe-XVIIIe siècles) et son <strong>église Saint-Sulpice</strong>, deuxième plus grande église de Paris après Notre-Dame."
        ],
        "faq": [
            ("Quelle ligne dessert Rennes ?", "Uniquement la <strong>M12</strong>. Bus 39, 95."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>, puis <strong>fermée de 1939 à 1968</strong>, rouverte le <strong>20 mai 1968</strong>."),
            ("Pourquoi cette longue fermeture ?", "<strong>Proximité avec la station Saint-Placide</strong> qui rendait Rennes redondante."),
            ("Pour la place Saint-Sulpice ?", "<strong>~5 min à pied</strong> via la rue du Vieux-Colombier."),
            ("Pour Saint-Germain-des-Prés ?", "<strong>~10 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Église Saint-Sulpice</strong> à 5 min à pied : 2e plus grande église parisienne.",
            "<strong>Place Saint-Sulpice</strong> : fontaine, marché aux poètes.",
            "<strong>Saint-Germain-des-Prés</strong> à 10 min à pied : Café de Flore, Les Deux Magots.",
            "Pour <strong>Montparnasse</strong> : <strong>M12 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⛪", "Église Saint-Sulpice, 2e plus grande de Paris", "L'<strong>église Saint-Sulpice</strong>, à 5 min à pied de la station, est la <strong>deuxième plus grande église de Paris</strong> après Notre-Dame (113 m de long contre 127 m). Construite de <strong>1646 à 1745</strong> sur l'emplacement d'une ancienne église romane. <strong>Façade néo-classique</strong> achevée en <strong>1745</strong> par l'architecte <strong>Giovanni Servandoni</strong>. <strong>Orgue Cavaillé-Coll</strong> (1862) parmi les plus célèbres du monde. <strong>Méridien</strong> (gnomon) au sol, popularisé par le roman <em>Da Vinci Code</em>."),
            ("🚇", "Fermeture historique 1939-1968", "La station Rennes connaît une <strong>fermeture record</strong> de <strong>35 ans</strong>, de <strong>1939 à 1968</strong>. Fermée en raison de sa <strong>proximité avec la station Saint-Placide</strong> (300 m seulement), jugée redondante. <strong>Rouverte le 20 mai 1968</strong>, en plein <strong>Mai 68</strong>, alors que des grèves paralysaient la France. Aujourd'hui, la station fonctionne normalement avec une fréquentation modérée.")
        ],
        "itin": [
            ("Place Saint-Sulpice", "saint-sulpice", "M12 + M4", "À pied (5 min) ou M12 → Sèvres-Babylone + M4", 5),
            ("Saint-Germain-des-Prés", "saint-germain-des-pres", "M12 + M4", "M12 → Sèvres-Babylone + M4", 8),
            ("Le Bon Marché", "sevres-babylone", "M12", "M12 directe (1 station)", 3),
            ("Notre-Dame-des-Champs", "notre-dame-des-champs", "M12", "M12 directe (1 station)", 2),
            ("Montparnasse", "montparnasse-bienvenue", "M12", "M12 directe (2 stations)", 5),
            ("Jardin du Luxembourg", "luxembourg", "M12 + RER B", "À pied (10 min) ou M12 + RER B", 10)
        ]
    },
    "falguiere": {
        "addr": "Rue Falguière, 75015 Paris", "arr": "15e arrondissement (Paris)",
        "seo": "Station Falguière (M12) rue Falguière dans le 15e. Hommage au sculpteur Alexandre Falguière. Proche gare Montparnasse et Institut Pasteur.",
        "tagline": "M12 — Falguière, sculpteur 19e siècle",
        "hero_desc": "Station <strong>Falguière</strong> sur la <strong>rue Falguière</strong> dans le <strong>15e arrondissement</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>5 novembre 1910</strong>. Hommage à <strong>Jean-Alexandre-Joseph Falguière</strong> (<strong>1831-1900</strong>), <strong>sculpteur français</strong>. Proche de la <strong>gare Montparnasse</strong> et de l'<strong>Institut Pasteur</strong>.",
        "intros": [
            "La station <strong>Falguière</strong> est implantée sur la <strong>rue Falguière</strong> dans le <strong>15e arrondissement</strong>. Elle est desservie par la <strong>ligne 12 du métro</strong>, entre <strong>Pasteur</strong> (1 station) et <strong>Montparnasse - Bienvenüe</strong> (1 station). Bus 89.",
            "Ouverte le <strong>5 novembre 1910</strong> avec le tronçon initial de la <strong>ligne A du Nord-Sud</strong>.",
            "Le nom <strong>Falguière</strong> rend hommage à <strong>Jean-Alexandre-Joseph Falguière</strong> (<strong>1831-1900</strong>), <strong>sculpteur et peintre français</strong>. <strong>Grand prix de Rome</strong> en sculpture (1859). <strong>Membre de l'Académie des beaux-arts</strong> (1882). Œuvres : <em>Le Vainqueur du combat de coqs</em> (1864), <em>Tarcisius martyr chrétien</em> (1868), statue de <strong>La Résistance</strong> au sommet de l'Arc de Triomphe (1882)."
        ],
        "hist_title": "1910 : Nord-Sud et sculpteur académicien",
        "hist": [
            "La station Falguière est <strong>inaugurée le 5 novembre 1910</strong> avec le tronçon initial de la <strong>ligne A du Nord-Sud</strong>.",
            "Le nom <strong>Falguière</strong> rend hommage à <strong>Jean-Alexandre-Joseph Falguière</strong> (<strong>7 septembre 1831 - 19 avril 1900</strong>), <strong>sculpteur et peintre français</strong>. Né à Toulouse.",
            "<strong>Grand prix de Rome</strong> en sculpture en <strong>1859</strong>. <strong>Membre de l'Académie des beaux-arts</strong> en <strong>1882</strong>. <strong>Professeur à l'École des beaux-arts</strong>. Œuvres célèbres : <em>Le Vainqueur du combat de coqs</em> (1864, musée d'Orsay), <em>Tarcisius martyr chrétien</em> (1868), <em>La Résistance</em> au sommet de l'<strong>Arc de Triomphe</strong> (1882, en remplacement de l'œuvre de Rude détruite). <strong>Atelier rue d'Assas</strong>, proche du quartier Montparnasse, devenu un haut lieu artistique au XIXe siècle."
        ],
        "faq": [
            ("Quelle ligne dessert Falguière ?", "Uniquement la <strong>M12</strong>. Bus 89."),
            ("Qui est Falguière ?", "<strong>Jean-Alexandre-Joseph Falguière</strong> (1831-1900), <strong>sculpteur et peintre français</strong>. <strong>Grand prix de Rome</strong> (1859), <strong>membre de l'Académie des beaux-arts</strong> (1882)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>."),
            ("Pour la gare Montparnasse ?", "<strong>M12 directe</strong> (1 station, ~2 min) ou <strong>~10 min à pied</strong>."),
            ("Pour l'Institut Pasteur ?", "<strong>~10 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "Pour <strong>gare Montparnasse</strong> : <strong>M12 directe</strong> (1 station).",
            "Pour <strong>Institut Pasteur</strong> : 10 min à pied via rue Falguière.",
            "Quartier <strong>15e résidentiel</strong>.",
            "Pour <strong>Concorde</strong> : <strong>M12 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🗿", "Falguière, sculpteur académique", "<strong>Jean-Alexandre-Joseph Falguière</strong> (1831-1900), <strong>sculpteur et peintre français</strong> né à <strong>Toulouse</strong>. <strong>Grand prix de Rome</strong> en sculpture en <strong>1859</strong>. Pensionnaire de la <strong>Villa Médicis</strong> à Rome (1859-1864). <strong>Membre de l'Académie des beaux-arts</strong> en <strong>1882</strong>. <strong>Professeur à l'École des beaux-arts</strong>. Œuvres : <em>Le Vainqueur du combat de coqs</em> (1864, musée d'Orsay), <em>Tarcisius martyr chrétien</em> (1868). Sculpture de <em>La Résistance</em> au sommet de l'<strong>Arc de Triomphe</strong> (1882). Atelier rue d'Assas, quartier Montparnasse."),
            ("🎨", "Montparnasse, quartier d'artistes", "Le <strong>quartier Montparnasse</strong>, à proximité de la station Falguière, est l'un des <strong>plus importants quartiers d'artistes</strong> de Paris à la fin du XIXe et au début du XXe siècle. <strong>Académies privées</strong>, <strong>ateliers</strong>, <strong>cafés mythiques</strong> (Le Dôme, La Coupole, La Rotonde, Le Select). Artistes ayant vécu ou travaillé à Montparnasse : <strong>Modigliani, Picasso, Soutine, Chagall, Brancusi, Foujita, Man Ray</strong>.")
        ],
        "itin": [
            ("Montparnasse", "montparnasse-bienvenue", "M12", "M12 directe (1 station)", 2),
            ("Institut Pasteur", "pasteur", "M12", "M12 directe (1 station) + à pied", 5),
            ("Pasteur", "pasteur", "M12", "M12 directe (1 station)", 2),
            ("Tour Montparnasse", "montparnasse-bienvenue", "M12", "M12 directe (1 station)", 3),
            ("Concorde", "concorde", "M12", "M12 directe (~10 min)", 10),
            ("Madeleine", "madeleine", "M12", "M12 directe (~8 min)", 8)
        ]
    },
    "volontaires": {
        "addr": "Rue des Volontaires, 75015 Paris", "arr": "15e arrondissement (Paris)",
        "seo": "Station Volontaires (M12) rue des Volontaires dans le 15e. Quartier Vaugirard résidentiel. Proche Institut Pasteur.",
        "tagline": "M12 — rue des Volontaires, 15e résidentiel",
        "hero_desc": "Station <strong>Volontaires</strong> sur la <strong>rue des Volontaires</strong> dans le <strong>15e arrondissement</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>5 novembre 1910</strong>. Quartier <strong>Vaugirard</strong> résidentiel.",
        "intros": [
            "La station <strong>Volontaires</strong> est implantée sur la <strong>rue des Volontaires</strong> dans le <strong>15e arrondissement</strong>. Elle est desservie par la <strong>ligne 12 du métro</strong>, entre <strong>Pasteur</strong> (1 station) et <strong>Vaugirard</strong> (1 station). Bus 39 et 89.",
            "Ouverte le <strong>5 novembre 1910</strong> avec le tronçon initial de la <strong>ligne A du Nord-Sud</strong>.",
            "La <strong>rue des Volontaires</strong> rend hommage aux <strong>volontaires de la Révolution française</strong> qui s'engagèrent en 1791-1792 pour défendre la jeune République. Quartier <strong>Vaugirard</strong> résidentiel du <strong>15e arrondissement</strong>, à proximité de l'<strong>Institut Pasteur</strong>."
        ],
        "hist_title": "1910 : Nord-Sud et volontaires de 1792",
        "hist": [
            "La station Volontaires est <strong>inaugurée le 5 novembre 1910</strong> avec le tronçon initial de la <strong>ligne A du Nord-Sud</strong>.",
            "La <strong>rue des Volontaires</strong> rend hommage aux <strong>volontaires de la Révolution française</strong> qui s'engagèrent en <strong>1791-1792</strong> pour défendre la jeune <strong>République face aux armées européennes</strong>. La <strong>levée des volontaires</strong> de 1791 (200 000 volontaires) et le <strong>décret du 11 juillet 1792</strong> (« La patrie est en danger ») contribuèrent à la <strong>victoire de Valmy</strong> (20 septembre 1792).",
            "Le quartier <strong>Vaugirard</strong>, autour de la station, est l'un des <strong>plus peuplés de Paris</strong> (<strong>15e arrondissement</strong>, ~240 000 habitants — premier arrondissement parisien par la population). Quartier <strong>résidentiel et commerçant</strong>. À courte distance : l'<strong>Institut Pasteur</strong>, la <strong>gare Montparnasse</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Volontaires ?", "Uniquement la <strong>M12</strong>. Bus 39 et 89."),
            ("D'où vient le nom Volontaires ?", "Des <strong>volontaires de la Révolution française</strong> engagés en <strong>1791-1792</strong> pour défendre la République."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>."),
            ("Pour l'Institut Pasteur ?", "<strong>~7 min à pied</strong>."),
            ("Pour Montparnasse ?", "<strong>M12 directe</strong> (~5 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Institut Pasteur</strong> à 7 min à pied.",
            "Quartier <strong>Vaugirard</strong> résidentiel.",
            "Pour <strong>Montparnasse</strong> : <strong>M12 directe</strong>.",
            "Pour <strong>Convention</strong> : <strong>M12 directe</strong> (1 station).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🇫🇷", "Volontaires de 1791-1792", "Les <strong>volontaires nationaux</strong> sont des soldats <strong>volontaires</strong> qui s'engagèrent en <strong>1791-1792</strong> pour défendre la <strong>République française</strong> face aux <strong>armées européennes coalisées</strong>. La <strong>levée des volontaires</strong> de juin 1791 (<strong>200 000 hommes</strong>) et le <strong>décret du 11 juillet 1792</strong> (« <em>La patrie est en danger</em> ») permirent de constituer une armée populaire. Cette mobilisation contribua à la <strong>victoire de Valmy</strong> (20 septembre 1792) sur les <strong>Prussiens</strong>, considérée comme la <strong>naissance de la République française</strong>."),
            ("🏘️", "15e arrondissement, le plus peuplé de Paris", "Le <strong>15e arrondissement</strong>, autour de Volontaires, est le <strong>plus peuplé de Paris</strong> avec <strong>~240 000 habitants</strong>. Quartier <strong>résidentiel et commerçant</strong>. Il comprend les anciens <strong>villages de Grenelle et de Vaugirard</strong>, rattachés à Paris en <strong>1860</strong>. Plusieurs <strong>institutions importantes</strong> y sont implantées : <strong>Institut Pasteur</strong>, <strong>UNESCO</strong>, <strong>Beaugrenelle</strong>, <strong>Tour Eiffel</strong> (à la limite avec le 7e).")
        ],
        "itin": [
            ("Institut Pasteur", "pasteur", "M12", "M12 directe (1 station) + à pied", 7),
            ("Pasteur", "pasteur", "M12", "M12 directe (1 station)", 2),
            ("Montparnasse", "montparnasse-bienvenue", "M12", "M12 directe (~5 min)", 5),
            ("Vaugirard", "vaugirard", "M12", "M12 directe (1 station)", 2),
            ("Concorde", "concorde", "M12", "M12 directe (~12 min)", 12),
            ("Madeleine", "madeleine", "M12", "M12 directe (~10 min)", 10)
        ]
    },
    "vaugirard": {
        "addr": "Rue de Vaugirard, 75015 Paris", "arr": "15e arrondissement (Paris)",
        "seo": "Station Vaugirard (M12) rue de Vaugirard dans le 15e. Plus longue rue de Paris (4,3 km). Quartier Vaugirard du 15e arrondissement.",
        "tagline": "M12 — rue de Vaugirard, plus longue de Paris",
        "hero_desc": "Station <strong>Vaugirard</strong> sur la <strong>rue de Vaugirard</strong> dans le <strong>15e arrondissement</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>5 novembre 1910</strong>. La <strong>rue de Vaugirard</strong> est la <strong>plus longue rue de Paris</strong> (<strong>4,3 km</strong>).",
        "intros": [
            "La station <strong>Vaugirard</strong> est implantée sur la <strong>rue de Vaugirard</strong> dans le <strong>15e arrondissement</strong>. Elle est desservie par la <strong>ligne 12 du métro</strong>, entre <strong>Volontaires</strong> (1 station) et <strong>Convention</strong> (1 station). Bus 39, 70, 80, 89.",
            "Ouverte le <strong>5 novembre 1910</strong> avec le tronçon initial de la <strong>ligne A du Nord-Sud</strong>.",
            "La <strong>rue de Vaugirard</strong>, qui donne son nom à la station, est la <strong>plus longue rue de Paris</strong> (<strong>4,3 km</strong>). Elle traverse les <strong>6e et 15e arrondissements</strong>, du <strong>Jardin du Luxembourg</strong> à la <strong>Porte de Versailles</strong>. Le quartier <strong>Vaugirard</strong>, autour de la station, est un ancien village rattaché à Paris en <strong>1860</strong>."
        ],
        "hist_title": "1910 : la plus longue rue de Paris",
        "hist": [
            "La station Vaugirard est <strong>inaugurée le 5 novembre 1910</strong> avec le tronçon initial de la <strong>ligne A du Nord-Sud</strong>.",
            "La <strong>rue de Vaugirard</strong>, qui donne son nom à la station, est la <strong>plus longue rue de Paris</strong> avec <strong>4,3 km</strong>. Elle traverse les <strong>6e et 15e arrondissements</strong>, reliant le <strong>Jardin du Luxembourg</strong> à la <strong>Porte de Versailles</strong>. Son tracé suit en grande partie l'ancien <strong>chemin de Vaugirard</strong>, qui menait Paris au village du même nom.",
            "Le quartier <strong>Vaugirard</strong>, autour de la station, est un <strong>ancien village</strong> rattaché à Paris en <strong>1860</strong> avec d'autres communes périphériques. <strong>Étymologie</strong> : de <em>Val Girard</em>, hommage probable à un certain <strong>Girard</strong>, abbé de Saint-Germain-des-Prés au XIIIe siècle. Le quartier conserve une <strong>atmosphère de village</strong>, à proximité du <strong>parc Georges-Brassens</strong> (anciennes <strong>abattoirs de Vaugirard</strong>)."
        ],
        "faq": [
            ("Quelle ligne dessert Vaugirard ?", "Uniquement la <strong>M12</strong>. Bus 39, 70, 80, 89."),
            ("Quelle est la longueur de la rue de Vaugirard ?", "<strong>4,3 km</strong> — <strong>plus longue rue de Paris</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>."),
            ("Pour le parc Georges-Brassens ?", "<strong>~10 min à pied</strong>. Anciens abattoirs de Vaugirard."),
            ("Pour Convention ?", "<strong>M12 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Rue de Vaugirard</strong> : plus longue rue de Paris (4,3 km).",
            "<strong>Parc Georges-Brassens</strong> à 10 min : anciens abattoirs.",
            "<strong>Marché du livre ancien</strong> au parc Georges-Brassens (samedi et dimanche).",
            "Pour <strong>Montparnasse</strong> : <strong>M12 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("📏", "Rue de Vaugirard, plus longue de Paris", "La <strong>rue de Vaugirard</strong>, qui donne son nom à la station, est la <strong>plus longue rue de Paris</strong> avec <strong>4,3 km</strong>. Elle traverse les <strong>6e et 15e arrondissements</strong>, reliant le <strong>Jardin du Luxembourg</strong> à l'est à la <strong>Porte de Versailles</strong> à l'ouest. Son tracé suit en grande partie l'<strong>ancien chemin de Vaugirard</strong>, qui menait Paris au village du même nom rattaché à la capitale en <strong>1860</strong>."),
            ("🐎", "Parc Georges-Brassens, anciens abattoirs", "Le <strong>parc Georges-Brassens</strong>, à 10 min à pied de Vaugirard, est aménagé sur les <strong>anciens abattoirs de Vaugirard</strong> (1898-1976). <strong>Inauguré en 1984</strong>, baptisé en hommage à <strong>Georges Brassens</strong> (1921-1981) qui habita à proximité. <strong>7,8 hectares</strong>. Le <strong>marché du livre ancien et d'occasion</strong> s'y tient chaque <strong>samedi et dimanche</strong> matin dans les anciens pavillons.")
        ],
        "itin": [
            ("Parc Georges-Brassens", "convention", "M12 + à pied", "À pied (10 min)", 10),
            ("Convention", "convention", "M12", "M12 directe (1 station)", 2),
            ("Volontaires", "volontaires", "M12", "M12 directe (1 station)", 2),
            ("Montparnasse", "montparnasse-bienvenue", "M12", "M12 directe (~7 min)", 7),
            ("Institut Pasteur", "pasteur", "M12", "M12 directe (2 stations) + à pied", 8),
            ("Porte de Versailles", "porte-de-versailles", "M12", "M12 directe (~5 min)", 5)
        ]
    },
    "convention": {
        "addr": "Rue de la Convention, 75015 Paris", "arr": "15e arrondissement (Paris)",
        "seo": "Station Convention (M12) rue de la Convention dans le 15e. Convention nationale (1792-1795). Quartier Vaugirard du 15e arrondissement.",
        "tagline": "M12 — Convention nationale (1792-1795)",
        "hero_desc": "Station <strong>Convention</strong> sur la <strong>rue de la Convention</strong> dans le <strong>15e arrondissement</strong>. Desservie par la <strong>M12</strong>, ouverte le <strong>5 novembre 1910</strong>. Hommage à la <strong>Convention nationale</strong> (<strong>1792-1795</strong>), assemblée révolutionnaire qui proclama la Première République.",
        "intros": [
            "La station <strong>Convention</strong> est implantée sur la <strong>rue de la Convention</strong> dans le <strong>15e arrondissement</strong>. Elle est desservie par la <strong>ligne 12 du métro</strong>, entre <strong>Vaugirard</strong> (1 station) et <strong>Porte de Versailles</strong> (1 station). Bus 39, 49, 62, 70, 80, 89.",
            "Ouverte le <strong>5 novembre 1910</strong> avec le tronçon initial de la <strong>ligne A du Nord-Sud</strong>.",
            "Le nom <strong>Convention</strong> rend hommage à la <strong>Convention nationale</strong> (<strong>20 septembre 1792 - 26 octobre 1795</strong>), <strong>assemblée révolutionnaire française</strong> qui <strong>proclama la Première République française</strong> le <strong>22 septembre 1792</strong>. Quartier <strong>Vaugirard</strong> résidentiel du <strong>15e arrondissement</strong>."
        ],
        "hist_title": "1910 : Convention nationale (1792-1795)",
        "hist": [
            "La station Convention est <strong>inaugurée le 5 novembre 1910</strong> avec le tronçon initial de la <strong>ligne A du Nord-Sud</strong>.",
            "Le nom <strong>Convention</strong> rend hommage à la <strong>Convention nationale</strong> (<strong>20 septembre 1792 - 26 octobre 1795</strong>), <strong>assemblée révolutionnaire française</strong>. Élue au <strong>suffrage universel masculin</strong> (premier vote au suffrage universel en Europe). <strong>749 députés</strong>.",
            "La Convention <strong>proclama la Première République française</strong> le <strong>22 septembre 1792</strong>. Elle <strong>vota la nouvelle Constitution de l'An I</strong> (24 juin 1793, jamais appliquée), puis la <strong>Constitution de l'An III</strong> (22 août 1795). Elle créa le <strong>Comité de salut public</strong>, le <strong>système métrique décimal</strong>, le <strong>calendrier républicain</strong>, l'<strong>École polytechnique</strong> (1794), le <strong>Conservatoire national des arts et métiers</strong> (1794). Elle abolit l'<strong>esclavage</strong> dans les colonies (<strong>4 février 1794</strong>)."
        ],
        "faq": [
            ("Quelle ligne dessert Convention ?", "Uniquement la <strong>M12</strong>. Bus 39, 49, 62, 70, 80, 89."),
            ("Qu'est-ce que la Convention nationale ?", "<strong>Assemblée révolutionnaire française</strong> (20 septembre 1792 - 26 octobre 1795). <strong>Proclama la Première République</strong>. Élue au <strong>suffrage universel masculin</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 novembre 1910</strong>."),
            ("Quelles réalisations majeures de la Convention ?", "<strong>Proclamation de la Première République</strong> (22 septembre 1792), <strong>système métrique décimal</strong>, <strong>calendrier républicain</strong>, <strong>abolition de l'esclavage</strong> (1794), <strong>École polytechnique</strong> (1794)."),
            ("Pour Porte de Versailles ?", "<strong>M12 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Parc Georges-Brassens</strong> à 10 min à pied : anciens abattoirs.",
            "Pour <strong>Porte de Versailles</strong> et <strong>Parc des Expositions</strong> : <strong>M12 directe</strong>.",
            "Quartier <strong>Vaugirard</strong> résidentiel.",
            "Pour <strong>Montparnasse</strong> : <strong>M12 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Convention nationale et Première République", "La <strong>Convention nationale</strong> est l'<strong>assemblée constituante française</strong> qui <strong>gouverna la France du 20 septembre 1792 au 26 octobre 1795</strong>. Élue au <strong>suffrage universel masculin</strong> (premier vote au suffrage universel en Europe). <strong>Proclama la Première République française</strong> le <strong>22 septembre 1792</strong>. <strong>Vota la nouvelle Constitution de l'An I</strong> (24 juin 1793, jamais appliquée), puis la <strong>Constitution de l'An III</strong>. <strong>Abolit l'esclavage</strong> dans les colonies (<strong>4 février 1794</strong>, première abolition mondiale)."),
            ("📐", "Système métrique décimal, héritage durable", "Parmi les <strong>réalisations majeures et durables</strong> de la <strong>Convention</strong> figure l'<strong>adoption du système métrique décimal</strong> (<strong>1er août 1793</strong>). Inspiré des travaux de la <strong>Commission des poids et mesures</strong> de l'<strong>Académie des sciences</strong>. <strong>Définition du mètre</strong> comme le dix-millionième du quart du méridien terrestre. <strong>Système adopté progressivement en Europe et dans le monde</strong>, sauf États-Unis, Royaume-Uni, Birmanie.")
        ],
        "itin": [
            ("Porte de Versailles (Parc Expositions)", "porte-de-versailles", "M12", "M12 directe (1 station)", 2),
            ("Parc Georges-Brassens", "convention", "à pied", "Rue de Vaugirard (10 min)", 10),
            ("Vaugirard", "vaugirard", "M12", "M12 directe (1 station)", 2),
            ("Montparnasse", "montparnasse-bienvenue", "M12", "M12 directe (~10 min)", 10),
            ("Pasteur", "pasteur", "M12", "M12 directe (3 stations)", 6),
            ("Madeleine", "madeleine", "M12", "M12 directe (~14 min)", 14)
        ]
    },
    "corentin-celton": {
        "addr": "Place Corentin-Celton, 92130 Issy-les-Moulineaux", "arr": "Issy-les-Moulineaux (92)",
        "seo": "Station Corentin-Celton (M12) à Issy-les-Moulineaux (92). Hôpital Corentin-Celton à la sortie. Quartier en mutation urbaine.",
        "tagline": "M12 — Issy-les-Moulineaux, hôpital",
        "hero_desc": "Station <strong>Corentin-Celton</strong> sur la <strong>place Corentin-Celton</strong> à <strong>Issy-les-Moulineaux</strong> (Hauts-de-Seine, 92). Desservie par la <strong>M12</strong>, ouverte le <strong>5 février 1934</strong>. À la sortie : l'<strong>hôpital Corentin-Celton</strong> (AP-HP).",
        "intros": [
            "La station <strong>Corentin-Celton</strong> est implantée à <strong>Issy-les-Moulineaux</strong> (Hauts-de-Seine, 92). Elle est desservie par la <strong>M12</strong>, entre <strong>Porte de Versailles</strong> (1 station) et <strong>Mairie d'Issy</strong> (1 station, terminus sud). Bus 39, 89, 123, 169, 190.",
            "Ouverte le <strong>5 février 1934</strong> avec le <strong>prolongement de la M12</strong> de <strong>Porte de Versailles à Mairie d'Issy</strong>. Initialement nommée <strong>« Petits-Ménages »</strong> (en référence à l'hospice des Petits-Ménages).",
            "À la sortie : l'<strong>hôpital Corentin-Celton</strong>, établissement de santé de l'<strong>Assistance publique - Hôpitaux de Paris (AP-HP)</strong>. <strong>~400 lits</strong>, spécialisé en <strong>gériatrie, soins palliatifs, rééducation</strong>. Le quartier est en pleine <strong>mutation urbaine</strong>."
        ],
        "hist_title": "1934 : Issy-les-Moulineaux et hôpital",
        "hist": [
            "La station est <strong>inaugurée le 5 février 1934</strong> sous le nom de <strong>« Petits-Ménages »</strong>, avec le <strong>prolongement de la M12</strong> de <strong>Porte de Versailles à Mairie d'Issy</strong>.",
            "<strong>Renommée Corentin-Celton</strong> le <strong>15 mai 1945</strong>, en hommage à <strong>Corentin Celton</strong> (<strong>1901-1943</strong>), <strong>infirmier français</strong> de l'<strong>hospice des Petits-Ménages</strong> (devenu hôpital Corentin-Celton).",
            "L'<strong>hôpital Corentin-Celton</strong>, à la sortie de la station, est un établissement de santé de l'<strong>Assistance publique - Hôpitaux de Paris (AP-HP)</strong>. <strong>Construit en 1862</strong> comme <strong>hospice des Petits-Ménages</strong> pour personnes âgées. <strong>~400 lits</strong>, spécialisé en <strong>gériatrie, soins palliatifs, rééducation</strong>. Le quartier autour est en <strong>mutation urbaine</strong> avec de nombreux <strong>nouveaux immeubles de bureaux et logements</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Corentin-Celton ?", "Uniquement la <strong>M12</strong>. Bus 39, 89, 123, 169, 190."),
            ("Quel était l'ancien nom ?", "<strong>« Petits-Ménages »</strong> (1934-1945)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 février 1934</strong>, renommée le <strong>15 mai 1945</strong>."),
            ("Pour l'hôpital Corentin-Celton ?", "<strong>Sortie directe</strong>. AP-HP, ~400 lits."),
            ("Pour Issy-les-Moulineaux centre ?", "<strong>M12 directe</strong> vers <strong>Mairie d'Issy</strong> (1 station, terminus sud)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Hôpital Corentin-Celton</strong> à la sortie : AP-HP, ~400 lits, gériatrie et rééducation.",
            "Quartier en <strong>mutation urbaine</strong>.",
            "Pour <strong>Porte de Versailles</strong> (Parc Expositions) : <strong>M12 directe</strong> (1 station).",
            "Pour <strong>Mairie d'Issy</strong> : <strong>M12 directe</strong> (terminus sud).",
            "Zone tarifaire <strong>2</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("🏥", "Hôpital Corentin-Celton, AP-HP", "L'<strong>hôpital Corentin-Celton</strong>, à la sortie de la station, est un <strong>établissement de santé de l'AP-HP</strong> (Assistance publique - Hôpitaux de Paris). <strong>Construit en 1862</strong> comme <strong>hospice des Petits-Ménages</strong> pour personnes âgées sans ressources, à l'initiative du <strong>baron Haussmann</strong>. <strong>~400 lits</strong>, spécialisé en <strong>gériatrie, soins palliatifs, rééducation</strong>. <strong>Renommé Corentin-Celton</strong> en 1945."),
            ("🏘️", "Issy-les-Moulineaux, mutation urbaine", "<strong>Issy-les-Moulineaux</strong> (~70 000 habitants) est l'une des communes les plus dynamiques des <strong>Hauts-de-Seine</strong>. <strong>Ancienne commune industrielle</strong> (Renault Industrie Équipements), elle s'est transformée en <strong>quartier de bureaux et de logements</strong> depuis les années 1980. <strong>Sièges sociaux</strong> (Microsoft France, Bouygues Telecom, Cisco France, Hewlett-Packard France). <strong>Quartier Île-de-France numérique</strong>.")
        ],
        "itin": [
            ("Hôpital Corentin-Celton", "corentin-celton", "à pied", "Sortie directe", 1),
            ("Mairie d'Issy (terminus)", "mairie-d-issy", "M12", "M12 directe (1 station)", 2),
            ("Porte de Versailles", "porte-de-versailles", "M12", "M12 directe (1 station)", 2),
            ("Convention", "convention", "M12", "M12 directe (2 stations)", 4),
            ("Montparnasse", "montparnasse-bienvenue", "M12", "M12 directe (~12 min)", 12),
            ("Concorde", "concorde", "M12", "M12 directe (~18 min)", 18)
        ]
    },
    "mairie-d-issy": {
        "addr": "Avenue Bonaparte, 92130 Issy-les-Moulineaux", "arr": "Issy-les-Moulineaux (92)",
        "seo": "Station Mairie d'Issy, terminus sud M12 à Issy-les-Moulineaux (92). Hôtel de ville d'Issy-les-Moulineaux. Île Saint-Germain à proximité.",
        "tagline": "M12 — terminus sud, Issy-les-Moulineaux",
        "hero_desc": "Station <strong>Mairie d'Issy</strong>, <strong>terminus sud de la M12</strong>, à <strong>Issy-les-Moulineaux</strong> (Hauts-de-Seine, 92). Ouverte le <strong>24 mars 1934</strong>. À la sortie : l'<strong>hôtel de ville d'Issy-les-Moulineaux</strong>. À proximité de l'<strong>Île Saint-Germain</strong>.",
        "intros": [
            "La station <strong>Mairie d'Issy</strong> est le <strong>terminus sud de la M12</strong>, située à <strong>Issy-les-Moulineaux</strong> (Hauts-de-Seine, 92). Bus 39, 123, 126, 169, 189, 190, 290.",
            "Ouverte le <strong>24 mars 1934</strong> avec le <strong>prolongement de la M12</strong> de <strong>Porte de Versailles à Mairie d'Issy</strong> (2 stations ajoutées).",
            "À la sortie : l'<strong>hôtel de ville d'Issy-les-Moulineaux</strong>, en plein centre de la commune. <strong>Issy-les-Moulineaux</strong> (~70 000 habitants), commune dynamique des <strong>Hauts-de-Seine</strong>. À proximité : l'<strong>Île Saint-Germain</strong> (parc départemental), le <strong>quartier Issy 2015</strong> (urbanisme contemporain)."
        ],
        "hist_title": "1934 : terminus sud Issy-les-Moulineaux",
        "hist": [
            "La station Mairie d'Issy est <strong>inaugurée le 24 mars 1934</strong> avec le <strong>prolongement de la M12</strong> de <strong>Porte de Versailles à Mairie d'Issy</strong>. Devient <strong>terminus sud</strong> de la ligne 12.",
            "<strong>Issy-les-Moulineaux</strong> (~70 000 habitants) est une commune dynamique des <strong>Hauts-de-Seine</strong>. <strong>Étymologie</strong> : de <em>Issiacum</em> (latin, IXe siècle), domaine d'un certain Itius. <strong>Les-Moulineaux</strong> ajouté en 1893 en référence aux <strong>moulins</strong> qui se trouvaient sur les hauteurs.",
            "<strong>Ancienne commune industrielle</strong> (Renault Industrie Équipements, anciens hangars d'aviation), elle s'est <strong>transformée en quartier de bureaux et de logements</strong> depuis les années 1980. <strong>Sièges sociaux</strong> de nombreuses entreprises tech (Microsoft France, Bouygues Telecom, Cisco France, Hewlett-Packard France). <strong>Quartier Île-de-France numérique</strong>. L'<strong>Île Saint-Germain</strong>, à proximité, est un <strong>parc départemental</strong> de 12 hectares sur une île de la Seine."
        ],
        "faq": [
            ("Quelle ligne dessert Mairie d'Issy ?", "Uniquement la <strong>M12</strong> (terminus sud). Bus 39, 123, 126, 169, 189, 190, 290."),
            ("Quand a-t-elle ouvert ?", "Le <strong>24 mars 1934</strong>."),
            ("Combien d'habitants à Issy-les-Moulineaux ?", "<strong>~70 000 habitants</strong>."),
            ("Pour l'Île Saint-Germain ?", "<strong>~10 min à pied</strong>. Parc départemental de 12 ha."),
            ("Pour Paris centre ?", "<strong>M12 directe</strong> vers <strong>Concorde</strong> (~20 min) ou <strong>Madeleine</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Hôtel de ville d'Issy-les-Moulineaux</strong> à la sortie.",
            "<strong>Île Saint-Germain</strong> à 10 min : parc départemental sur île de la Seine.",
            "<strong>Quartier Issy 2015</strong> : urbanisme contemporain, sièges tech.",
            "Pour <strong>Concorde</strong> : <strong>M12 directe</strong> (~20 min).",
            "Zone tarifaire <strong>2</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("🏛️", "Issy-les-Moulineaux, ancien Issiacum", "<strong>Issy-les-Moulineaux</strong>, commune des <strong>Hauts-de-Seine</strong> (~70 000 habitants). <strong>Étymologie</strong> : de <em>Issiacum</em> (latin, IXe siècle), domaine d'un certain Itius. La mention <strong>« les-Moulineaux »</strong> est ajoutée en <strong>1893</strong> en référence aux <strong>moulins</strong> qui se trouvaient sur les hauteurs. <strong>Ancienne commune industrielle</strong> (Renault, anciens hangars d'aviation au début du XXe siècle), elle s'est <strong>transformée en quartier de bureaux et de logements</strong> depuis les années 1980. Capitale de la <strong>French Tech</strong>."),
            ("🌳", "Île Saint-Germain, parc sur la Seine", "L'<strong>Île Saint-Germain</strong>, à 10 min à pied de la station, est un <strong>parc départemental</strong> de <strong>12 hectares</strong> sur une <strong>île de la Seine</strong>. Aménagée comme <strong>parc public</strong> à partir des années 1970. Anciennement <strong>île industrielle</strong> (usines Renault), elle est devenue un <strong>espace vert apprécié</strong> par les habitants de la commune. <strong>Tour-aux-Figures</strong> (1988), sculpture de <strong>Jean Dubuffet</strong>.")
        ],
        "itin": [
            ("Hôtel de ville Issy-les-Moulineaux", "mairie-d-issy", "à pied", "Sortie directe", 1),
            ("Île Saint-Germain", "mairie-d-issy", "à pied", "À pied (10 min)", 10),
            ("Corentin-Celton", "corentin-celton", "M12", "M12 directe (1 station)", 2),
            ("Porte de Versailles", "porte-de-versailles", "M12", "M12 directe (2 stations)", 5),
            ("Montparnasse", "montparnasse-bienvenue", "M12", "M12 directe (~14 min)", 14),
            ("Concorde", "concorde", "M12", "M12 directe (~20 min)", 20)
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
    elif "(92)" in c["arr"]:
        d["tariff_zone"] = 2
        d["tariff_zone_context"] = "Hauts-de-Seine (92), zone tarifaire 2"
        d["commune"] = c["arr"].split(" (")[0]
    elif "(93)" in c["arr"]:
        d["tariff_zone"] = 3
        d["tariff_zone_context"] = "Seine-Saint-Denis (93), zone tarifaire 3"
        d["commune"] = c["arr"].split(" (")[0]
    else:
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
    d["hero_image"]["keep_hero"] = True
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
