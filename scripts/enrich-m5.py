#!/usr/bin/env python3
"""Enrichit M5 15 stations avec contenu T0 Wikipedia FR."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    "bobigny-pablo-picasso": {
        "addr": "Av. Henri Barbusse, 93000 Bobigny", "arr": "Bobigny (93)",
        "seo": "Station Bobigny - Pablo Picasso : terminus nord M5 à Bobigny (93). Préfecture de Seine-Saint-Denis et Conseil départemental 93.",
        "tagline": "M5 — terminus nord, Préfecture du 93",
        "hero_desc": "Station <strong>Bobigny - Pablo Picasso</strong>, <strong>terminus nord de la M5</strong> ouvert le <strong>25 avril 1985</strong>. Située à <strong>Bobigny</strong> (Seine-Saint-Denis, 93). Dessert la <strong>Préfecture de Seine-Saint-Denis</strong> et le <strong>Conseil départemental du 93</strong>. Nom du peintre <strong>Pablo Picasso</strong> (1881-1973).",
        "intros": [
            "La station <strong>Bobigny - Pablo Picasso</strong> est <strong>terminus nord de la M5</strong>, située à <strong>Bobigny</strong> (Seine-Saint-Denis, 93). Bus 145, 146, 234, 247, 251, 322, 323, T1 Tramway (Saint-Denis ↔ Noisy-le-Sec).",
            "Ouverte le <strong>25 avril 1985</strong> avec le prolongement de la M5 de Église de Pantin à Bobigny - Pablo Picasso. <strong>Terminus nord de la M5</strong>.",
            "Dessert la <strong>Préfecture de Seine-Saint-Denis</strong> et le <strong>Conseil départemental du 93</strong>. <strong>Bobigny</strong> (~50 000 habitants) est la <strong>préfecture de la Seine-Saint-Denis</strong>. Pôle multimodal avec Tramway T1."
        ],
        "hist_title": "1985 : terminus M5, et Pablo Picasso",
        "hist": [
            "La station est inaugurée le <strong>25 avril 1985</strong> avec le <strong>prolongement de la M5</strong> de Église de Pantin à Bobigny - Pablo Picasso (3 stations ajoutées).",
            "Le nom <strong>Pablo Picasso</strong> commémore <strong>Pablo Ruiz Picasso</strong> (1881-1973), <strong>peintre, sculpteur et graveur espagnol</strong>. <strong>Cofondateur du cubisme</strong> avec Georges Braque (1907). Plus de <strong>50 000 œuvres</strong>. Œuvres majeures : <em>Les Demoiselles d'Avignon</em> (1907), <em>Guernica</em> (1937).",
            "<strong>Bobigny</strong>, ~50 000 habitants, <strong>préfecture de la Seine-Saint-Denis (93)</strong>. Pôle administratif avec Préfecture, Conseil départemental, tribunal."
        ],
        "faq": [
            ("Quelle ligne dessert Bobigny - Pablo Picasso ?", "Uniquement la <strong>M5</strong> (terminus nord). Bus 145, 146, 234, 247, 251, 322, 323. <strong>Tramway T1</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>25 avril 1985</strong>."),
            ("Qui est Pablo Picasso ?", "<strong>Pablo Ruiz Picasso</strong> (1881-1973), peintre espagnol cofondateur du cubisme. <em>Les Demoiselles d'Avignon</em> (1907), <em>Guernica</em> (1937)."),
            ("Quelle est la commune ?", "<strong>Bobigny</strong> (~50 000 hab.), <strong>préfecture de Seine-Saint-Denis (93)</strong>."),
            ("Comment aller à Place d'Italie ?", "<strong>M5 directe</strong> : ~40 min (terminus sud)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>. Station moderne 1985.")
        ],
        "tips": [
            "<strong>Préfecture du 93</strong> à la sortie.",
            "<strong>Tramway T1</strong> (Saint-Denis ↔ Noisy-le-Sec).",
            "Pour <strong>République</strong> : M5 directe (~20 min).",
            "Pour <strong>Place d'Italie</strong> : M5 directe (~40 min).",
            "Zone tarifaire 3."
        ],
        "trivia": [
            ("🎨", "Pablo Picasso (1881-1973) — cofondateur du cubisme", "<strong>Pablo Ruiz Picasso</strong> (1881-1973), <strong>peintre, sculpteur, graveur et céramiste espagnol</strong>. <strong>Cofondateur du cubisme</strong> avec Georges Braque en 1907. Plus de <strong>50 000 œuvres</strong> au cours de sa carrière. Œuvres emblématiques : <em>Les Demoiselles d'Avignon</em> (1907), <em>Guernica</em> (1937, dénonciation du bombardement de Guernica), <em>La Femme qui pleure</em>. <strong>Musée Picasso</strong> à Paris (3e arr.).")
        ],
        "itin": [
            ("Préfecture du 93", "prefecture-93", "à pied", "Sortie directe", 2),
            ("République via M5", "republique", "M5", "M5 direction Place d'Italie (10 stations)", 20),
            ("Place d'Italie via M5", "place-d-italie", "M5", "M5 terminus sud", 40),
            ("Bastille via M5", "bastille", "M5", "M5 direction Place d'Italie", 26),
            ("Tramway T1", "tramway-t1", "T1", "T1 Saint-Denis ou Noisy-le-Sec", 5),
            ("Stalingrad via M5", "stalingrad", "M5", "M5 direction Place d'Italie (7 stations)", 14)
        ]
    },
    "bobigny-pantin-raymond-queneau": {
        "addr": "Limite Bobigny / Pantin (93)", "arr": "Bobigny (93)",
        "seo": "Station Bobigny - Pantin - Raymond Queneau : M5 à la limite Bobigny/Pantin (93). Nommée d'après Raymond Queneau (1903-1976), écrivain (Zazie dans le métro).",
        "tagline": "M5 — Raymond Queneau écrivain (Zazie dans le métro)",
        "hero_desc": "Station <strong>Bobigny - Pantin - Raymond Queneau</strong> à la limite de <strong>Bobigny</strong> et <strong>Pantin</strong> (Seine-Saint-Denis, 93). Desservie par la <strong>M5</strong>, ouverte le <strong>25 avril 1985</strong>. Nommée d'après <strong>Raymond Queneau</strong> (1903-1976), écrivain français, cofondateur de l'<strong>Oulipo</strong>, auteur de <em>Zazie dans le métro</em> (1959).",
        "intros": [
            "La station <strong>Bobigny - Pantin - Raymond Queneau</strong> est située à la limite des communes de <strong>Bobigny</strong> et <strong>Pantin</strong> (Seine-Saint-Denis, 93). Elle est desservie par la <strong>M5</strong>, entre <strong>Bobigny - Pablo Picasso</strong> (terminus nord, 1 station) et <strong>Église de Pantin</strong> (1 station vers le sud).",
            "Ouverte le <strong>25 avril 1985</strong> avec le prolongement M5.",
            "Le nom <strong>Raymond Queneau</strong> commémore <strong>Raymond Queneau</strong> (1903-1976), <strong>écrivain, poète, mathématicien et éditeur français</strong>. <strong>Cofondateur de l'Oulipo</strong> (Ouvroir de littérature potentielle) en 1960. Œuvres : <strong><em>Zazie dans le métro</em> (1959, adapté au cinéma par Louis Malle 1960)</strong>, <em>Exercices de style</em> (1947), <em>Les Fleurs bleues</em> (1965)."
        ],
        "hist_title": "1985 : M5, et Raymond Queneau l'Oulipo",
        "hist": [
            "La station est inaugurée le <strong>25 avril 1985</strong> avec le prolongement M5 vers Bobigny.",
            "Le nom commémore <strong>Raymond Queneau</strong> (1903-1976), <strong>écrivain, poète, mathématicien et éditeur français</strong>. Cofondateur en <strong>1960</strong> de l'<strong>Oulipo</strong> (Ouvroir de Littérature Potentielle), groupe littéraire alliant écriture et mathématiques (contraintes formelles).",
            "Œuvre majeure : <strong><em>Zazie dans le métro</em></strong> (1959), roman culte sur une jeune provinciale à Paris, adapté au cinéma par <strong>Louis Malle en 1960</strong>. Autres œuvres : <em>Exercices de style</em> (1947), <em>Les Fleurs bleues</em> (1965), <em>Cent mille milliards de poèmes</em> (1961, livre combinatoire avec 10^14 poèmes possibles).",
            "Co-fondateurs de l'Oulipo : Queneau, François Le Lionnais, Italo Calvino, Georges Perec (<em>La Disparition</em> 1969 — roman sans la lettre e)."
        ],
        "faq": [
            ("Quelle ligne dessert Bobigny - Pantin - Raymond Queneau ?", "Uniquement la <strong>M5</strong>."),
            ("Qui est Raymond Queneau ?", "<strong>Raymond Queneau</strong> (1903-1976), écrivain, poète, mathématicien et éditeur français. <strong>Cofondateur de l'Oulipo</strong> (1960). Auteur de <em>Zazie dans le métro</em> (1959)."),
            ("Qu'est-ce que l'Oulipo ?", "<strong>Ouvroir de Littérature Potentielle</strong>, groupe littéraire fondé en 1960 par Queneau et François Le Lionnais. Alliance entre <strong>écriture et mathématiques</strong> (contraintes formelles). Membres : Calvino, Perec, etc."),
            ("Comment aller à Place d'Italie ?", "<strong>M5 directe</strong> : ~38 min."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>. Station moderne 1985.")
        ],
        "tips": [
            "Pour <strong>Bobigny - Pablo Picasso</strong> (terminus + T1) : M5 directe (1 station).",
            "Pour <strong>République</strong> : M5 directe (~18 min).",
            "Pour <strong>Pantin centre</strong> : à pied.",
            "Pour <strong>Bastille</strong> : M5 directe.",
            "Zone tarifaire 3."
        ],
        "trivia": [
            ("📚", "Raymond Queneau (1903-1976) — Zazie dans le métro et l'Oulipo", "<strong>Raymond Queneau</strong> (1903-1976), <strong>écrivain, poète, mathématicien et éditeur français</strong>. <strong>Cofondateur de l'Oulipo</strong> (Ouvroir de Littérature Potentielle) en 1960 avec François Le Lionnais. Œuvre culte : <strong><em>Zazie dans le métro</em></strong> (1959), roman sur une jeune provinciale à Paris cherchant à monter dans le métro (en grève !), adapté au cinéma par <strong>Louis Malle en 1960</strong>. Autres : <em>Exercices de style</em> (1947, 99 variations du même récit), <em>Cent mille milliards de poèmes</em> (1961, livre combinatoire). <strong>Pléiade</strong> de son vivant.")
        ],
        "itin": [
            ("Bobigny - Pablo Picasso via M5", "bobigny-pablo-picasso", "M5", "M5 terminus nord (1 station)", 2),
            ("Église de Pantin via M5", "eglise-de-pantin", "M5", "M5 direction Place d'Italie (1 station)", 2),
            ("République via M5", "republique", "M5", "M5 direction Place d'Italie", 18),
            ("Place d'Italie via M5", "place-d-italie", "M5", "M5 direction Place d'Italie", 38),
            ("Bastille via M5", "bastille", "M5", "M5 direction Place d'Italie", 24),
            ("Stalingrad via M5", "stalingrad", "M5", "M5 direction Place d'Italie", 12)
        ]
    },
    "eglise-de-pantin": {
        "addr": "Av. Jean Lolive, 93500 Pantin", "arr": "Pantin (93)",
        "seo": "Station Église de Pantin : M5 à Pantin (93), proche de l'église Saint-Germain l'Auxerrois (1670). Mairie de Pantin.",
        "tagline": "M5 — Église de Pantin (1670)",
        "hero_desc": "Station <strong>Église de Pantin</strong> à <strong>Pantin</strong> (Seine-Saint-Denis, 93), ouverte le <strong>12 octobre 1942</strong> avec le prolongement M5. Dessert l'<strong>église Saint-Germain l'Auxerrois de Pantin</strong> (1670). À côté : la <strong>Mairie de Pantin</strong>.",
        "intros": [
            "La station <strong>Église de Pantin</strong> est située à <strong>Pantin</strong> (Seine-Saint-Denis, 93), sur l'avenue Jean Lolive. Elle est desservie par la <strong>M5</strong>, entre <strong>Bobigny - Pantin - Raymond Queneau</strong> (1 station nord) et <strong>Hoche</strong> (1 station sud).",
            "Ouverte le <strong>12 octobre 1942</strong> avec le prolongement de la M5 d'Église de Pantin (alors terminus est).",
            "À la sortie : l'<strong>église Saint-Germain l'Auxerrois de Pantin</strong>, construite au <strong>XVIIe siècle</strong> (1670). Style classique. À côté : la <strong>Mairie de Pantin</strong>. <strong>Pantin</strong> (~58 000 habitants) est l'une des plus peuplées communes du 93."
        ],
        "hist_title": "1942 : M5, et l'église Saint-Germain l'Auxerrois (1670)",
        "hist": [
            "La station est inaugurée le <strong>12 octobre 1942</strong> avec le prolongement de la M5 vers Église de Pantin (alors terminus est).",
            "L'<strong>église Saint-Germain l'Auxerrois de Pantin</strong> à la sortie est construite en <strong>1670</strong>, style classique français. Dédiée à <strong>saint Germain l'Auxerrois</strong> (évêque d'Auxerre Ve siècle, patron de Paris).",
            "<strong>Pantin</strong> (~58 000 habitants), commune limitrophe de Paris (19e arr.). <strong>Forte gentrification depuis 2000s</strong> : nouveaux quartiers (BNP Paribas, Hermès), berges du canal de l'Ourcq aménagées. Surnommée <strong>« Brooklyn parisien »</strong> par certains observateurs."
        ],
        "faq": [
            ("Quelle ligne dessert Église de Pantin ?", "Uniquement la <strong>M5</strong>."),
            ("Quelle est l'église à la sortie ?", "L'<strong>église Saint-Germain l'Auxerrois de Pantin</strong>, construite en <strong>1670</strong>, style classique. Dédiée à saint Germain l'Auxerrois (Ve siècle, patron de Paris)."),
            ("Quelle est la commune ?", "<strong>Pantin</strong> (~58 000 habitants), Seine-Saint-Denis (93). Surnommée <strong>« Brooklyn parisien »</strong>."),
            ("Comment aller à Place d'Italie ?", "<strong>M5 directe</strong> : ~36 min."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station 1942.")
        ],
        "tips": [
            "<strong>Église Saint-Germain l'Auxerrois</strong> à la sortie (1670).",
            "<strong>Mairie de Pantin</strong> à proximité.",
            "Pour <strong>Pantin centre</strong> et quartier nouveau : à pied.",
            "Pour <strong>République</strong> : M5 directe (~16 min).",
            "Zone tarifaire 2."
        ],
        "trivia": [
            ("⛪", "Église Saint-Germain l'Auxerrois de Pantin (1670)", "L'<strong>église Saint-Germain l'Auxerrois de Pantin</strong> à la sortie de la station est construite en <strong>1670</strong>, style classique français. Dédiée à <strong>saint Germain l'Auxerrois</strong> (Ve siècle, évêque d'Auxerre, <strong>patron de Paris</strong>). Édifice modeste mais cœur historique de la commune de Pantin. Restaurée plusieurs fois. Classée Monument Historique."),
            ("🌆", "Pantin — « Brooklyn parisien »", "<strong>Pantin</strong> (~58 000 habitants), commune limitrophe de Paris (19e arr.). <strong>Forte gentrification depuis les années 2000</strong> : nouveaux quartiers d'affaires (sièges BNP Paribas et Hermès), berges du canal de l'Ourcq aménagées. Surnommée <strong>« Brooklyn parisien »</strong> par certains observateurs en raison de la migration de jeunes familles parisiennes cherchant des logements plus grands. Quartier dynamique en mutation.")
        ],
        "itin": [
            ("Église Saint-Germain l'Auxerrois", "eglise-saint-germain-pantin", "à pied", "Sortie directe", 1),
            ("Mairie de Pantin", "mairie-pantin", "à pied", "5 min", 5),
            ("République via M5", "republique", "M5", "M5 direction Place d'Italie", 16),
            ("Bobigny - Pablo Picasso via M5", "bobigny-pablo-picasso", "M5", "M5 terminus nord (2 stations)", 4),
            ("Place d'Italie via M5", "place-d-italie", "M5", "M5 direction Place d'Italie", 36),
            ("Bastille via M5", "bastille", "M5", "M5 direction Place d'Italie", 22)
        ]
    },
    "hoche": {
        "addr": "Av. Édouard-Vaillant, 93500 Pantin", "arr": "Pantin (93)",
        "seo": "Station Hoche : M5 à Pantin (93). Nommée d'après le général Lazare Hoche (1768-1797), général de la Révolution française.",
        "tagline": "M5 — Général Hoche (1768-1797)",
        "hero_desc": "Station <strong>Hoche</strong> à <strong>Pantin</strong> (Seine-Saint-Denis, 93), ouverte le <strong>12 octobre 1942</strong> avec le prolongement M5. Nommée d'après <strong>Lazare Hoche</strong> (1768-1797), <strong>général de la Révolution française</strong>, l'un des plus brillants commandants militaires de son époque.",
        "intros": [
            "La station <strong>Hoche</strong> est située à <strong>Pantin</strong> (Seine-Saint-Denis, 93), sur l'avenue Édouard-Vaillant. Elle est desservie par la <strong>M5</strong>, entre <strong>Église de Pantin</strong> (1 station nord) et <strong>Porte de Pantin</strong> (1 station sud).",
            "Ouverte le <strong>12 octobre 1942</strong> avec le prolongement de la M5 vers Église de Pantin.",
            "Le nom <strong>Hoche</strong> commémore <strong>Lazare Hoche</strong> (1768-1797), <strong>général de la Révolution française</strong>. <strong>Né dans une famille modeste</strong>, monté du rang grâce à la Révolution. <strong>Mort prématurément à 29 ans</strong> en 1797. Considéré comme l'un des <strong>plus brillants commandants militaires</strong> de son époque."
        ],
        "hist_title": "1942 : M5, et le général Hoche",
        "hist": [
            "La station est inaugurée le <strong>12 octobre 1942</strong> avec le prolongement de la M5 vers Église de Pantin.",
            "Le nom commémore <strong>Louis Lazare Hoche</strong> (1768-1797), <strong>général de la Révolution française</strong>. <strong>Né dans une famille modeste</strong> à Versailles. <strong>Soldat puis sergent</strong> avant la Révolution, monté au grade de <strong>général de division à 24 ans</strong> en 1793.",
            "<strong>Succès militaires</strong> : <strong>pacification de la Vendée</strong> (1795-1796, fin de la guerre civile), <strong>campagne du Rhin</strong>, opérations en Irlande (échec lié à la tempête). <strong>Mort à 29 ans en 1797</strong>, probablement d'une <strong>tuberculose ou d'un empoisonnement</strong> (incertitude historique).",
            "Considéré comme l'un des <strong>plus brillants commandants militaires</strong> de son époque, avant l'ascension de Bonaparte. <strong>Statue à Quiberon</strong> (Bretagne). Son nom est gravé sous l'<strong>Arc de Triomphe à Paris</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Hoche ?", "Uniquement la <strong>M5</strong>."),
            ("Qui est Hoche ?", "<strong>Louis Lazare Hoche</strong> (1768-1797), <strong>général de la Révolution française</strong>. Né dans une famille modeste, général à 24 ans. <strong>Pacificateur de la Vendée</strong>. Mort à 29 ans en 1797."),
            ("Pourquoi mort si jeune ?", "À <strong>29 ans en 1797</strong>, probablement de <strong>tuberculose ou empoisonnement</strong> (incertitude historique). Considéré comme l'un des plus brillants généraux de son époque."),
            ("Comment aller à République ?", "<strong>M5 directe</strong> : ~14 min."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station 1942.")
        ],
        "tips": [
            "Pour <strong>République</strong> : M5 directe (~14 min).",
            "Pour <strong>Porte de Pantin</strong> (Parc de la Villette) : M5 directe (1 station).",
            "Pour <strong>Bobigny - Pablo Picasso</strong> (terminus + T1) : M5 directe (3 stations).",
            "Pour <strong>Bastille</strong> : M5 directe.",
            "Zone tarifaire 2."
        ],
        "trivia": [
            ("⚔️", "Général Hoche — pacificateur de la Vendée à 29 ans", "<strong>Louis Lazare Hoche</strong> (1768-1797), <strong>général de la Révolution française</strong>. <strong>Né dans une famille modeste</strong> à Versailles. <strong>Soldat puis sergent</strong> avant la Révolution, monté au grade de <strong>général de division à 24 ans</strong> en 1793. <strong>Succès militaires</strong> : <strong>pacification de la Vendée</strong> (1795-1796, fin de la guerre civile), <strong>campagne du Rhin</strong>, opérations en Irlande. <strong>Mort à 29 ans en 1797</strong>, probablement de <strong>tuberculose ou d'un empoisonnement</strong>. Son nom est gravé sous l'<strong>Arc de Triomphe à Paris</strong>.")
        ],
        "itin": [
            ("Porte de Pantin via M5", "porte-de-pantin", "M5", "M5 direction Place d'Italie (1 station)", 2),
            ("Église de Pantin via M5", "eglise-de-pantin", "M5", "M5 direction Bobigny (1 station)", 2),
            ("République via M5", "republique", "M5", "M5 direction Place d'Italie", 14),
            ("Bobigny - Pablo Picasso via M5", "bobigny-pablo-picasso", "M5", "M5 terminus nord", 6),
            ("Place d'Italie via M5", "place-d-italie", "M5", "M5 direction Place d'Italie", 34),
            ("Stalingrad via M5", "stalingrad", "M5", "M5 direction Place d'Italie", 8)
        ]
    },
    "porte-de-pantin": {
        "addr": "Av. Jean Jaurès, 75019 Paris", "arr": "19e (Paris)",
        "seo": "Station Porte de Pantin : M5 dans le 19e arr. Parc de la Villette, Cité de la Musique - Philharmonie de Paris, Grande Halle de la Villette, Géode.",
        "tagline": "M5 — Parc de la Villette, Philharmonie de Paris",
        "hero_desc": "Station <strong>Porte de Pantin</strong> ouverte le <strong>12 octobre 1942</strong> avec le prolongement M5. Située à la <strong>limite du 19e arrondissement</strong> et de Pantin. Dessert le <strong>Parc de la Villette</strong> (55 ha, le plus grand parc culturel de Paris), la <strong>Cité de la Musique - Philharmonie de Paris</strong>, la <strong>Grande Halle de la Villette</strong> et la <strong>Géode</strong> (cinéma IMAX).",
        "intros": [
            "La station <strong>Porte de Pantin</strong> est située à la <strong>limite du 19e arrondissement de Paris</strong> et de la commune de Pantin. Elle est desservie par la <strong>M5</strong>, entre <strong>Hoche</strong> (1 station nord) et <strong>Ourcq</strong> (1 station sud). Bus 75, 151, 170, Tramway T3b.",
            "Ouverte le <strong>12 octobre 1942</strong> avec le prolongement M5 vers Église de Pantin.",
            "À la sortie : le <strong>Parc de la Villette</strong>, <strong>55 hectares</strong>, conçu par l'architecte <strong>Bernard Tschumi</strong> (1982-1991). <strong>Plus grand parc culturel de Paris</strong>. Composantes : <strong>Cité des Sciences et de l'Industrie</strong>, <strong>Cité de la Musique - Philharmonie de Paris</strong> (Jean Nouvel 2015), <strong>Grande Halle de la Villette</strong> (Halle de Baltard 1867 réhabilitée), <strong>Géode</strong> (cinéma IMAX sphérique 1985), <strong>Zénith de Paris</strong>."
        ],
        "hist_title": "Anciens abattoirs (1867) → Parc de la Villette (1991)",
        "hist": [
            "La station <strong>Porte de Pantin</strong> est inaugurée le <strong>12 octobre 1942</strong> avec le prolongement de la M5 vers Église de Pantin.",
            "Le site du <strong>Parc de la Villette</strong> était occupé par les <strong>anciens abattoirs et marché aux bestiaux de la Villette</strong>, créés en <strong>1867</strong> par Napoléon III pour <strong>centraliser l'abattage à Paris</strong>. <strong>Plus grand marché aux bestiaux du monde</strong> à l'époque. <strong>Fermeture en 1974</strong>, abattoirs transférés à Rungis et autres villes.",
            "<strong>Réaménagement 1979-1991</strong> en parc paysager. Concours international remporté en <strong>1982</strong> par l'architecte suisse <strong>Bernard Tschumi</strong> (déconstructivisme). Inauguration progressive : <strong>Cité des Sciences 1986</strong>, <strong>Géode 1985</strong>, <strong>Cité de la Musique 1995</strong>, <strong>Philharmonie de Paris 2015</strong> (Jean Nouvel, après 8 ans de retard et controverses budgétaires).",
            "<strong>55 hectares</strong>, le <strong>plus grand parc culturel de Paris</strong>. <strong>Folies</strong> rouges (35 pavillons-sculptures de Tschumi), <strong>jardins thématiques</strong>, <strong>canal de l'Ourcq</strong> traversant le parc. <strong>~10 millions de visiteurs/an</strong>."
        ],
        "faq": [
            ("Quelles lignes desservent Porte de Pantin ?", "<strong>M5</strong> + <strong>Tramway T3b</strong> (boulevards des Maréchaux). Bus 75, 151, 170."),
            ("Qu'est-ce que le Parc de la Villette ?", "<strong>55 hectares</strong>, <strong>plus grand parc culturel de Paris</strong>. Conçu par <strong>Bernard Tschumi</strong> (1982-1991). Inclut : Cité des Sciences, Philharmonie de Paris, Grande Halle, Géode, Zénith. <strong>~10 millions de visiteurs/an</strong>."),
            ("Qu'est-ce que la Philharmonie de Paris ?", "<strong>Salle de concert</strong> conçue par <strong>Jean Nouvel</strong>, inaugurée en <strong>2015</strong>. <strong>2 400 places</strong>. Résidence de l'Orchestre de Paris. Architecture iconique (façade en mosaïque d'oiseaux)."),
            ("Qu'est-ce que la Géode ?", "<strong>Cinéma IMAX sphérique</strong> en miroir poli, ouverte en <strong>1985</strong>. <strong>36 m de diamètre</strong>. Conçue par Adrien Fainsilber. Icône architecturale."),
            ("Comment aller à Châtelet ?", "<strong>M5 directe vers République + M11/M14</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station 1942.")
        ],
        "tips": [
            "<strong>Parc de la Villette</strong> à la sortie — 55 ha.",
            "<strong>Philharmonie de Paris</strong> (Jean Nouvel 2015) — concerts.",
            "<strong>Cité des Sciences</strong> à 10 min — musée scientifique.",
            "<strong>Géode</strong> à 10 min — cinéma IMAX sphérique.",
            "<strong>Grande Halle</strong> (Baltard 1867) — expositions, festivals.",
            "Pour <strong>République</strong> : M5 directe (~12 min)."
        ],
        "trivia": [
            ("🎭", "Parc de la Villette (1991) — plus grand parc culturel de Paris", "Le <strong>Parc de la Villette</strong> à la sortie de la station est le <strong>plus grand parc culturel de Paris</strong>. <strong>55 hectares</strong>, conçu par l'architecte suisse <strong>Bernard Tschumi</strong> (déconstructivisme), inauguré progressivement entre <strong>1982 et 1991</strong>. <strong>35 folies rouges</strong> (pavillons-sculptures) ponctuent le parc. Inclut : <strong>Cité des Sciences et de l'Industrie</strong> (1986), <strong>Géode</strong> (1985, cinéma IMAX sphérique), <strong>Cité de la Musique</strong> (1995), <strong>Philharmonie de Paris</strong> (2015, Jean Nouvel, 2 400 places), <strong>Grande Halle de la Villette</strong> (Baltard 1867, réhabilitée), <strong>Zénith de Paris</strong> (1984, 6 000 places concerts). <strong>~10 millions de visiteurs/an</strong>."),
            ("🐄", "Anciens abattoirs (1867-1974) — plus grand marché aux bestiaux du monde", "Le site du Parc de la Villette était occupé par les <strong>anciens abattoirs et marché aux bestiaux de la Villette</strong>, créés en <strong>1867</strong> par <strong>Napoléon III</strong> pour <strong>centraliser l'abattage à Paris</strong>. <strong>Plus grand marché aux bestiaux du monde</strong> à l'époque. <strong>~30 000 animaux abattus/jour</strong> au pic. <strong>Fermeture en 1974</strong>, abattoirs transférés à Rungis et autres villes. Reconversion exemplaire en <strong>parc culturel</strong> à partir de 1979.")
        ],
        "itin": [
            ("Parc de la Villette", "parc-villette", "à pied", "Sortie directe", 2),
            ("Philharmonie de Paris", "philharmonie-paris", "à pied", "5 min", 5),
            ("Cité des Sciences", "cite-sciences", "à pied", "10 min", 10),
            ("Géode", "geode", "à pied", "10 min", 10),
            ("République via M5", "republique", "M5", "M5 direction Place d'Italie", 12),
            ("Place d'Italie via M5", "place-d-italie", "M5", "M5 direction Place d'Italie", 32)
        ]
    },
    "ourcq": {
        "addr": "Av. Jean Jaurès / canal de l'Ourcq, 75019 Paris", "arr": "19e (Paris)",
        "seo": "Station Ourcq : M5 dans le 19e arr., canal de l'Ourcq. Bassin de la Villette, port de plaisance.",
        "tagline": "M5 — canal de l'Ourcq",
        "hero_desc": "Station <strong>Ourcq</strong> ouverte le <strong>12 octobre 1942</strong> avec le prolongement M5. Située dans le <strong>19e arrondissement</strong>, sur l'avenue Jean Jaurès à proximité du <strong>canal de l'Ourcq</strong>. Quartier emblématique du nord-est parisien revitalisé années 2010 (péniches, cafés, restaurants).",
        "intros": [
            "La station <strong>Ourcq</strong> est située dans le <strong>19e arrondissement de Paris</strong>, sur l'avenue Jean Jaurès à proximité du <strong>canal de l'Ourcq</strong>. Elle est desservie par la <strong>M5</strong>, entre <strong>Porte de Pantin</strong> (1 station nord) et <strong>Laumière</strong> (1 station sud). Bus 60, 75.",
            "Ouverte le <strong>12 octobre 1942</strong> avec le prolongement de la M5.",
            "À la sortie : le <strong>canal de l'Ourcq</strong>, <strong>97 km de long</strong>, construit entre <strong>1802 et 1825</strong> pour alimenter Paris en eau potable et faciliter le transport fluvial. Lieu emblématique du <strong>nord-est parisien</strong>, revitalisé dans les années 2010 (péniches restaurants, cafés, MK2 cinéma)."
        ],
        "hist_title": "Canal de l'Ourcq (1802-1825, Napoléon)",
        "hist": [
            "La station <strong>Ourcq</strong> est inaugurée le <strong>12 octobre 1942</strong> avec le prolongement M5 vers Église de Pantin.",
            "Le <strong>canal de l'Ourcq</strong> est une voie navigable de <strong>97 km</strong>, construite entre <strong>1802 et 1825</strong> sous <strong>Napoléon Ier</strong> par l'ingénieur <strong>Pierre-Simon Girard</strong>. Capte les eaux de la <strong>rivière Ourcq</strong> (Aisne) pour alimenter <strong>Paris en eau potable</strong> (à l'époque où le réseau d'eau parisien était insuffisant).",
            "Le canal alimentait également les <strong>fontaines monumentales</strong> du nord-est parisien (place du Châtelet, fontaine Trévise) et facilitait le <strong>transport fluvial</strong> de marchandises (charbon, bois, pierre).",
            "À l'arrivée à Paris : le <strong>bassin de la Villette</strong> (15 ha) joue le rôle de <strong>port de plaisance</strong>. Aujourd'hui : lieu emblématique du nord-est parisien revitalisé années 2010 (péniches restaurants, cafés Pavillon Puebla, cinéma plein air, jeux nautiques)."
        ],
        "faq": [
            ("Quelle ligne dessert Ourcq ?", "Uniquement la <strong>M5</strong>."),
            ("Qu'est-ce que le canal de l'Ourcq ?", "<strong>Voie navigable de 97 km</strong> construite entre <strong>1802 et 1825</strong> sous <strong>Napoléon Ier</strong>. Capte les eaux de la rivière Ourcq pour alimenter Paris en eau potable et faciliter le transport fluvial."),
            ("Qu'est-ce que le bassin de la Villette ?", "<strong>Port de plaisance</strong> de Paris (15 ha), partie du canal de l'Ourcq à l'arrivée parisienne. Revitalisé années 2010."),
            ("Comment aller à Châtelet ?", "<strong>M5 directe vers République + M11</strong>."),
            ("Comment aller au Parc de la Villette ?", "<strong>M5 directe</strong> : 1 station vers Porte de Pantin."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station 1942.")
        ],
        "tips": [
            "<strong>Canal de l'Ourcq</strong> à proximité — péniches restaurants.",
            "<strong>Bassin de la Villette</strong> à 5 min — port de plaisance.",
            "Pour <strong>Parc de la Villette</strong> : M5 directe (1 station).",
            "Pour <strong>République</strong> : M5 directe (~10 min).",
            "Pour <strong>Stalingrad</strong> : M5 directe (3 stations)."
        ],
        "trivia": [
            ("🚢", "Canal de l'Ourcq (1802-1825) — Napoléon hydraulique", "Le <strong>canal de l'Ourcq</strong> est une voie navigable de <strong>97 km</strong>, construite entre <strong>1802 et 1825</strong> sous <strong>Napoléon Ier</strong> par l'ingénieur <strong>Pierre-Simon Girard</strong>. Capte les eaux de la <strong>rivière Ourcq</strong> (Aisne, 87 km) pour alimenter <strong>Paris en eau potable</strong> (besoin urgent au début du XIXe siècle, le réseau d'eau parisien étant alors insuffisant) et faciliter le <strong>transport fluvial</strong> de marchandises (charbon, bois, pierre, blé). Alimentait aussi les <strong>fontaines monumentales</strong> du nord-est parisien.")
        ],
        "itin": [
            ("Canal de l'Ourcq", "canal-ourcq", "à pied", "Sortie directe", 2),
            ("Parc de la Villette via M5", "porte-de-pantin", "M5", "M5 direction Bobigny (1 station)", 2),
            ("Bassin de la Villette", "bassin-villette", "à pied", "5 min sud-ouest", 5),
            ("République via M5", "republique", "M5", "M5 direction Place d'Italie", 10),
            ("Stalingrad via M5", "stalingrad", "M5", "M5 direction Place d'Italie (3 stations)", 6),
            ("Place d'Italie via M5", "place-d-italie", "M5", "M5 direction Place d'Italie", 30)
        ]
    },
    "laumiere": {
        "addr": "Av. de Laumière, 75019 Paris", "arr": "19e (Paris)",
        "seo": "Station Laumière : M5 dans le 19e arr., avenue de Laumière. Général Boudet de Laumière (1814-1863). Quartier résidentiel.",
        "tagline": "M5 — Général Boudet de Laumière",
        "hero_desc": "Station <strong>Laumière</strong> ouverte le <strong>12 octobre 1942</strong> avec le prolongement M5. Située dans le <strong>19e arrondissement</strong>, sur l'<strong>avenue de Laumière</strong>. Nommée d'après le <strong>général Boudet de Laumière</strong> (1814-1863), mort à la guerre du Mexique.",
        "intros": [
            "La station <strong>Laumière</strong> est située dans le <strong>19e arrondissement de Paris</strong>, sur l'<strong>avenue de Laumière</strong>. Elle est desservie par la <strong>M5</strong>, entre <strong>Ourcq</strong> (1 station nord) et <strong>Jaurès</strong> (1 station sud, M2+M5+M7bis). Bus 60.",
            "Ouverte le <strong>12 octobre 1942</strong> avec le prolongement de la M5.",
            "Le nom <strong>Laumière</strong> commémore le <strong>général François Pierre Boudet de Laumière</strong> (1814-1863), général français mort à la <strong>guerre du Mexique</strong> (1862-1867, intervention de Napoléon III). Quartier résidentiel calme du 19e."
        ],
        "hist_title": "1942 : M5, et le général de Laumière (Mexique 1863)",
        "hist": [
            "La station est inaugurée le <strong>12 octobre 1942</strong> avec le prolongement M5.",
            "Le nom commémore le <strong>général François Pierre Boudet de Laumière</strong> (1814-1863). <strong>Général français</strong>, <strong>mort à la guerre du Mexique</strong> le 5 mai 1863 lors de la <strong>bataille de Camerone</strong>.",
            "La <strong>guerre du Mexique</strong> (1862-1867) était une <strong>intervention militaire française</strong> sous <strong>Napoléon III</strong> pour soutenir l'<strong>empire mexicain de Maximilien Ier</strong> (frère de François-Joseph d'Autriche) contre les républicains de Benito Juárez. Échec total : Maximilien fusillé en 1867. La <strong>bataille de Camerone</strong> (30 avril 1863) est devenue une <strong>fête tradition de la Légion étrangère</strong>.",
            "Quartier résidentiel calme du 19e. Tour Pyramides à proximité."
        ],
        "faq": [
            ("Quelle ligne dessert Laumière ?", "Uniquement la <strong>M5</strong>."),
            ("Qui est Laumière ?", "<strong>Général François Pierre Boudet de Laumière</strong> (1814-1863), <strong>général français mort à la guerre du Mexique</strong> le 5 mai 1863. Intervention française sous Napoléon III."),
            ("Comment aller à République ?", "<strong>M5 directe</strong> : ~8 min."),
            ("Comment aller à Jaurès (canal Ourcq) ?", "<strong>M5 directe</strong> : 1 station vers le sud."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station 1942.")
        ],
        "tips": [
            "Pour <strong>Jaurès</strong> (canal Ourcq + M2+M7bis) : M5 directe (1 station).",
            "Pour <strong>République</strong> : M5 directe (~8 min).",
            "Pour <strong>Parc de la Villette</strong> : M5 directe (2 stations).",
            "Quartier résidentiel calme — commerces locaux."
        ],
        "trivia": [
            ("⚔️", "Général Boudet de Laumière — mort à Camerone (1863)", "<strong>Général François Pierre Boudet de Laumière</strong> (1814-1863), <strong>général français mort à la guerre du Mexique</strong> le 5 mai 1863, en lien avec la célèbre <strong>bataille de Camerone</strong> (30 avril 1863). La <strong>guerre du Mexique</strong> (1862-1867) était une <strong>intervention militaire française</strong> sous <strong>Napoléon III</strong> pour soutenir l'<strong>empire mexicain de Maximilien Ier</strong>. Échec total : Maximilien fusillé en 1867. La <strong>bataille de Camerone</strong> est devenue une <strong>fête tradition de la Légion étrangère</strong> (62 légionnaires contre 2 000 Mexicains).")
        ],
        "itin": [
            ("Jaurès via M5", "jaures", "M5", "M5 direction Place d'Italie (1 station)", 2),
            ("Ourcq via M5", "ourcq", "M5", "M5 direction Bobigny (1 station)", 2),
            ("République via M5", "republique", "M5", "M5 direction Place d'Italie", 8),
            ("Parc de la Villette via M5", "porte-de-pantin", "M5", "M5 direction Bobigny (2 stations)", 4),
            ("Stalingrad via M5", "stalingrad", "M5", "M5 direction Place d'Italie (2 stations)", 4),
            ("Bastille via M5", "bastille", "M5", "M5 direction Place d'Italie", 16)
        ]
    },
    "jacques-bonsergent": {
        "addr": "Bd de Magenta / rue de Lancry, 75010 Paris", "arr": "10e (Paris)",
        "seo": "Station Jacques Bonsergent : M5 dans le 10e arr. Nommée d'après Jacques Bonsergent (1912-1940), premier civil parisien fusillé par les Allemands.",
        "tagline": "M5 — Jacques Bonsergent (1er fusillé parisien 1940)",
        "hero_desc": "Station <strong>Jacques Bonsergent</strong> dans le <strong>10e arrondissement</strong>, sur le boulevard de Magenta. Desservie par la <strong>M5</strong>, ouverte le <strong>17 décembre 1907</strong>. Nommée d'après <strong>Jacques Bonsergent</strong> (1912-1940), <strong>premier civil parisien fusillé</strong> par les Allemands en décembre 1940. Mémoire du Paris occupé.",
        "intros": [
            "La station <strong>Jacques Bonsergent</strong> est située dans le <strong>10e arrondissement de Paris</strong>, sur le <strong>boulevard de Magenta</strong>. Elle est desservie par la <strong>M5</strong>, entre <strong>Gare de l'Est</strong> (1 station nord) et <strong>République</strong> (1 station sud, hub M3+M5+M8+M9+M11). Bus 38, 39, 47, 91.",
            "Ouverte le <strong>17 décembre 1907</strong> avec le tronçon Gare du Nord ↔ Place Mazas (futur Quai de la Rapée) de la M5 originelle. Initialement nommée <strong>« Lancry »</strong>, renommée <strong>« Jacques Bonsergent »</strong> en <strong>1946</strong> en hommage au premier civil parisien fusillé.",
            "<strong>Jacques Bonsergent</strong> (1912-1940), <strong>ingénieur français</strong>. <strong>Premier civil parisien fusillé par les Allemands</strong> le <strong>23 décembre 1940</strong> à <strong>Vincennes</strong>, pour avoir bousculé un soldat allemand. Devenu <strong>symbole de la Résistance et de l'Occupation</strong>."
        ],
        "hist_title": "1907 : M5, 1940 : Jacques Bonsergent fusillé",
        "hist": [
            "La station ouvre le <strong>17 décembre 1907</strong> avec la M5 originelle (Gare du Nord ↔ Place Mazas). Initialement nommée <strong>« Lancry »</strong>.",
            "<strong>Jacques Bonsergent</strong> (1912-1940), <strong>ingénieur français</strong>, est le <strong>premier civil parisien fusillé par les Allemands</strong> sous l'Occupation.",
            "<strong>Le 10 novembre 1940</strong>, le soir de son mariage, Jacques Bonsergent bouscule involontairement un <strong>sous-officier allemand</strong> dans la rue. Une dispute éclate, un autre invité frappe le soldat. Bonsergent <strong>refuse de dénoncer l'auteur réel</strong>. Condamné par tribunal allemand le 5 décembre 1940. <strong>Fusillé le 23 décembre 1940</strong> à <strong>Vincennes</strong>.",
            "Le <strong>1er civil parisien fusillé</strong> sous l'Occupation. Sa mort déclenche un sentiment d'horreur dans Paris. <strong>Symbole de la Résistance et de l'Occupation</strong>. Affichettes apposées par les Allemands annonçant son exécution déclenchent les premières manifestations parisiennes contre l'Occupation.",
            "La station est <strong>renommée « Jacques Bonsergent » en 1946</strong> en son hommage, l'une des premières stations de métro renommées d'un résistant après la Libération."
        ],
        "faq": [
            ("Quelle ligne dessert Jacques Bonsergent ?", "Uniquement la <strong>M5</strong>."),
            ("Qui est Jacques Bonsergent ?", "<strong>Ingénieur français</strong> (1912-1940), <strong>premier civil parisien fusillé par les Allemands</strong> le <strong>23 décembre 1940</strong> à Vincennes, pour avoir bousculé un soldat allemand le soir de son mariage et refusé de dénoncer un autre invité. <strong>Symbole de la Résistance</strong>."),
            ("Pourquoi le changement de nom ?", "Station nommée <strong>« Lancry » depuis 1907</strong>. Renommée <strong>« Jacques Bonsergent » en 1946</strong> en hommage au premier civil parisien fusillé par les Allemands."),
            ("Comment aller à Châtelet ?", "<strong>M5 directe vers République + M11</strong> : ~10 min."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station 1907.")
        ],
        "tips": [
            "Pour <strong>République</strong> (hub) : M5 directe (1 station).",
            "Pour <strong>Gare de l'Est</strong> : M5 directe (1 station).",
            "Pour <strong>Canal Saint-Martin</strong> : 5 min à pied.",
            "Pour <strong>Bastille</strong> : M5 directe.",
            "Quartier 10e mixte populaire."
        ],
        "trivia": [
            ("🕯️", "Jacques Bonsergent (1912-1940) — 1er civil parisien fusillé", "<strong>Jacques Bonsergent</strong> (1912-1940), <strong>ingénieur français</strong>, est le <strong>premier civil parisien fusillé par les Allemands</strong> sous l'Occupation. <strong>Le 10 novembre 1940</strong>, le <strong>soir de son mariage</strong>, il bouscule involontairement un sous-officier allemand. Une dispute éclate, un autre invité frappe le soldat. Bonsergent <strong>refuse de dénoncer l'auteur réel</strong>. <strong>Condamné le 5 décembre 1940</strong> par tribunal allemand. <strong>Fusillé le 23 décembre 1940</strong> à Vincennes. <strong>1er civil parisien fusillé</strong> sous l'Occupation. Sa mort déclenche horreur et premières manifestations contre l'Occupation. Station renommée en son honneur en 1946.")
        ],
        "itin": [
            ("République via M5", "republique", "M5", "M5 direction Place d'Italie (1 station)", 2),
            ("Gare de l'Est via M5", "gare-de-l-est", "M5", "M5 direction Bobigny (1 station)", 2),
            ("Canal Saint-Martin", "canal-saint-martin", "à pied", "5 min sud", 5),
            ("Châtelet via M5 + M11", "chatelet", "M5 + M11", "M5 → République + M11", 10),
            ("Bastille via M5", "bastille", "M5", "M5 direction Place d'Italie", 10),
            ("Gare du Nord via M5", "gare-du-nord", "M5", "M5 direction Bobigny", 6)
        ]
    },
    "oberkampf": {
        "addr": "Bd Voltaire / rue Oberkampf, 75011 Paris", "arr": "11e (Paris)",
        "seo": "Station Oberkampf : M5 + M9 dans le 11e arr. Christophe-Philippe Oberkampf (1738-1815), industriel allemand, fondateur Toile de Jouy. Quartier festif.",
        "tagline": "M5 + M9 — Oberkampf, quartier festif du 11e",
        "hero_desc": "Station <strong>Oberkampf</strong> dans le <strong>11e arrondissement</strong>, à l'intersection du boulevard Voltaire et de la rue Oberkampf. Desservie par <strong>M5</strong> (ouverte 17 décembre 1907) et <strong>M9</strong> (ouverte 10 décembre 1933). Nommée d'après <strong>Christophe-Philippe Oberkampf</strong> (1738-1815), industriel allemand fondateur de la <strong>Toile de Jouy</strong>. <strong>Quartier festif</strong> emblématique de Paris.",
        "intros": [
            "La station <strong>Oberkampf</strong> est située dans le <strong>11e arrondissement de Paris</strong>, à l'intersection du <strong>boulevard Voltaire</strong> et de la <strong>rue Oberkampf</strong>. Elle est desservie par <strong>2 lignes</strong> : <strong>M5</strong> (Bobigny ↔ Place d'Italie) et <strong>M9</strong> (Pont de Sèvres ↔ Mairie de Montreuil). Bus 56, 96.",
            "La station <strong>M5</strong> ouvre le <strong>17 décembre 1907</strong>. La station <strong>M9</strong> est ajoutée le <strong>10 décembre 1933</strong>.",
            "Le nom <strong>Oberkampf</strong> commémore <strong>Christophe-Philippe Oberkampf</strong> (1738-1815), <strong>industriel français d'origine allemande (Bavière)</strong>. <strong>Fondateur de la manufacture de Jouy-en-Josas</strong> (1760), célèbre pour sa <strong>Toile de Jouy</strong>. La <strong>rue Oberkampf</strong> est un des hauts lieux de la <strong>vie nocturne parisienne</strong>."
        ],
        "hist_title": "Oberkampf et la Toile de Jouy (1760)",
        "hist": [
            "La station <strong>M5</strong> ouvre le <strong>17 décembre 1907</strong>. La station <strong>M9</strong> est ajoutée le <strong>10 décembre 1933</strong>.",
            "Le nom commémore <strong>Christophe-Philippe Oberkampf</strong> (1738-1815), <strong>industriel français d'origine allemande (Bavière)</strong>. <strong>Fondateur de la manufacture de Jouy-en-Josas</strong> en <strong>1760</strong>.",
            "<strong>Toile de Jouy</strong> : tissu imprimé orné de <strong>scènes pastorales en monochrome</strong> (rouge, bleu, vert). Innovation technique : <strong>impression sur cuivre</strong> permettant des motifs très fins. La manufacture employait jusqu'à <strong>1 300 ouvriers</strong>. <strong>Anobli par Louis XVI</strong> en 1787 et par Napoléon en 1810.",
            "La <strong>rue Oberkampf</strong> (et environs : rue Saint-Maur, rue Jean-Pierre Timbaud) est l'un des <strong>hauts lieux de la vie nocturne parisienne</strong> depuis les années 1990. Bars, restaurants, salles de concert. Quartier festif et alternatif emblématique du 11e."
        ],
        "faq": [
            ("Quelles lignes desservent Oberkampf ?", "<strong>M5</strong> (1907) et <strong>M9</strong> (1933). Bus 56, 96."),
            ("Qui est Oberkampf ?", "<strong>Christophe-Philippe Oberkampf</strong> (1738-1815), <strong>industriel français d'origine allemande</strong>. <strong>Fondateur de la manufacture de Jouy-en-Josas</strong> (1760), célèbre pour sa <strong>Toile de Jouy</strong>."),
            ("Qu'est-ce que la Toile de Jouy ?", "<strong>Tissu imprimé orné de scènes pastorales en monochrome</strong> (rouge, bleu, vert). Innovation : <strong>impression sur cuivre</strong> pour motifs très fins. Manufacture de Jouy-en-Josas (1760)."),
            ("Pourquoi le quartier est-il festif ?", "La <strong>rue Oberkampf</strong> est l'un des hauts lieux de la <strong>vie nocturne parisienne</strong> depuis les années 1990. Bars, restaurants, salles de concert."),
            ("Comment aller à Châtelet ?", "<strong>M5 vers République + M11</strong> : ~8 min."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Stations historiques 1907/1933.")
        ],
        "tips": [
            "<strong>Rue Oberkampf</strong> — vie nocturne du 11e.",
            "Pour <strong>République</strong> : M5 directe (2 stations).",
            "Pour <strong>Bastille</strong> : M5 directe (2 stations).",
            "Pour <strong>Père-Lachaise</strong> : M9 directe.",
            "Quartier festif jeune."
        ],
        "trivia": [
            ("👔", "Oberkampf et la Toile de Jouy (1760)", "<strong>Christophe-Philippe Oberkampf</strong> (1738-1815), <strong>industriel français d'origine allemande (Bavière)</strong>. <strong>Fondateur de la manufacture de Jouy-en-Josas</strong> en <strong>1760</strong>, célèbre pour sa <strong>Toile de Jouy</strong>. Tissu imprimé orné de <strong>scènes pastorales en monochrome</strong> (rouge, bleu, vert). Innovation technique : <strong>impression sur cuivre</strong> permettant des motifs très fins. La manufacture employait jusqu'à <strong>1 300 ouvriers</strong>. <strong>Anobli par Louis XVI en 1787</strong> et par Napoléon en 1810. La Toile de Jouy reste un classique du textile d'ameublement français."),
            ("🌃", "Rue Oberkampf — vie nocturne emblématique du 11e", "La <strong>rue Oberkampf</strong> (et les rues voisines : Saint-Maur, Jean-Pierre Timbaud, Saint-Sébastien) est l'un des <strong>hauts lieux de la vie nocturne parisienne</strong> depuis les années 1990. <strong>Bars</strong>, <strong>restaurants</strong>, <strong>salles de concert</strong>. <strong>Café Charbon</strong>, <strong>Le Nouveau Casino</strong>, <strong>Les Trois Mailletz</strong>. Devient le <strong>cœur de la scène alternative</strong> et indé parisienne. Aujourd'hui : quartier festif jeune, gentrification progressive.")
        ],
        "itin": [
            ("République via M5", "republique", "M5", "M5 direction Bobigny (2 stations)", 4),
            ("Bastille via M5", "bastille", "M5", "M5 direction Place d'Italie (2 stations)", 4),
            ("Père-Lachaise via M9", "pere-lachaise", "M9", "M9 direction Mairie de Montreuil", 8),
            ("Châtelet via M5 + M11", "chatelet", "M5 + M11", "M5 → République + M11", 8),
            ("Stalingrad via M5", "stalingrad", "M5", "M5 direction Bobigny (3 stations)", 6),
            ("Rue Oberkampf (vie nocturne)", "rue-oberkampf", "à pied", "Sortie directe", 1)
        ]
    },
    "richard-lenoir": {
        "addr": "Bd Richard Lenoir, 75011 Paris", "arr": "11e (Paris)",
        "seo": "Station Richard-Lenoir : M5 dans le 11e arr., boulevard Richard-Lenoir. François Richard-Lenoir industriel cotonnier. Marché Bastille à proximité.",
        "tagline": "M5 — boulevard Richard-Lenoir, Marché Bastille",
        "hero_desc": "Station <strong>Richard-Lenoir</strong> dans le <strong>11e arrondissement</strong>, sur le <strong>boulevard Richard-Lenoir</strong>. Desservie par la <strong>M5</strong>, ouverte le <strong>17 décembre 1907</strong>. Nommée d'après <strong>François Richard-Lenoir</strong> (1765-1839), <strong>industriel cotonnier français</strong>. À proximité : le célèbre <strong>Marché Bastille</strong> (jeudis et dimanches).",
        "intros": [
            "La station <strong>Richard-Lenoir</strong> est située dans le <strong>11e arrondissement de Paris</strong>, sur le <strong>boulevard Richard-Lenoir</strong>. Elle est desservie par la <strong>M5</strong>, entre <strong>Oberkampf</strong> (1 station nord, M5+M9) et <strong>Bréguet-Sabin</strong> (1 station sud). Bus 56, 91.",
            "Ouverte le <strong>17 décembre 1907</strong> avec la M5 originelle.",
            "Le nom <strong>Richard-Lenoir</strong> commémore <strong>François Richard-Lenoir</strong> (1765-1839), <strong>industriel cotonnier français</strong>, propriétaire de plusieurs manufactures de coton. À proximité : le célèbre <strong>Marché Bastille</strong> (jeudis et dimanches), l'un des plus animés de Paris."
        ],
        "hist_title": "1907 : M5, Richard-Lenoir industriel cotonnier",
        "hist": [
            "La station <strong>Richard-Lenoir</strong> ouvre le <strong>17 décembre 1907</strong> avec la M5 originelle (Gare du Nord ↔ Place Mazas).",
            "Le nom commémore <strong>François Richard-Lenoir</strong> (1765-1839), <strong>industriel cotonnier français</strong>. Né dans une famille modeste, monta une <strong>importante entreprise de manufactures cotonnières</strong> au début du XIXe siècle. <strong>Ennobli</strong> par Napoléon.",
            "Le <strong>boulevard Richard-Lenoir</strong> a été <strong>aménagé en 1859-1861</strong> sur l'emplacement de l'ancien <strong>canal Saint-Martin couvert</strong> entre la rotonde de la Villette et le port de l'Arsenal. Boulevard caractéristique du <strong>plan Haussmann</strong>, large et ombragé.",
            "À proximité : le <strong>Marché Bastille</strong>, ouvert les <strong>jeudis et dimanches matin</strong> sur le boulevard. <strong>L'un des marchés alimentaires les plus animés de Paris</strong>. Produits frais, fromages, vins, fleurs."
        ],
        "faq": [
            ("Quelle ligne dessert Richard-Lenoir ?", "Uniquement la <strong>M5</strong>."),
            ("Qui est Richard-Lenoir ?", "<strong>François Richard-Lenoir</strong> (1765-1839), <strong>industriel cotonnier français</strong>. Propriétaire de manufactures de coton au début du XIXe. <strong>Ennobli par Napoléon</strong>."),
            ("Le boulevard a-t-il toujours été là ?", "Non, le <strong>boulevard Richard-Lenoir</strong> a été <strong>aménagé en 1859-1861</strong> sur l'emplacement de l'<strong>ancien canal Saint-Martin couvert</strong> (entre rotonde de la Villette et port de l'Arsenal). Plan Haussmann."),
            ("Qu'est-ce que le Marché Bastille ?", "<strong>L'un des marchés alimentaires les plus animés de Paris</strong>, ouvert les <strong>jeudis et dimanches matin</strong> sur le boulevard. Produits frais, fromages, vins."),
            ("Comment aller à Bastille ?", "<strong>M5 directe</strong> : ~3 min (2 stations vers le sud)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station 1907.")
        ],
        "tips": [
            "<strong>Marché Bastille</strong> jeudis/dimanches matin — l'un des plus animés.",
            "Pour <strong>Bastille</strong> : M5 directe (2 stations).",
            "Pour <strong>République</strong> : M5 directe (3 stations).",
            "Pour <strong>Oberkampf</strong> (vie nocturne) : M5 directe (1 station).",
            "Boulevard ombragé — promenade agréable."
        ],
        "trivia": [
            ("🌳", "Boulevard Richard-Lenoir — sur l'ancien canal Saint-Martin (1859)", "Le <strong>boulevard Richard-Lenoir</strong> a été <strong>aménagé en 1859-1861</strong> sur l'emplacement de l'<strong>ancien canal Saint-Martin couvert</strong> entre la rotonde de la Villette et le port de l'Arsenal. <strong>Plan Haussmann</strong>. Caractéristique des grands boulevards haussmanniens : <strong>large (~70 m)</strong>, <strong>ombragé</strong> par 4 rangées de platanes. Le canal Saint-Martin reste visible aux extrémités (Villette nord, Bastille sud) et a été <strong>renouvelé en lieu emblématique du Paris bohème</strong> depuis les années 2000. Tronçon central couvert toujours en service navigation souterraine."),
            ("🥖", "Marché Bastille — l'un des plus animés de Paris", "Le <strong>Marché Bastille</strong> à proximité de la station est <strong>l'un des marchés alimentaires les plus animés de Paris</strong>. Ouvert les <strong>jeudis et dimanches matin</strong> sur le boulevard Richard-Lenoir, entre la Bastille et la rue Saint-Ambroise. <strong>~100 commerçants</strong>. Produits frais : <strong>fromages, charcuteries, vins, poissons, fruits/légumes, fleurs</strong>. Quartier populaire et bourgeois mixte. Affluence record le dimanche matin.")
        ],
        "itin": [
            ("Marché Bastille (jeudis/dimanches)", "marche-bastille", "à pied", "Sortie directe", 1),
            ("Bastille via M5", "bastille", "M5", "M5 direction Place d'Italie (2 stations)", 4),
            ("Oberkampf via M5", "oberkampf", "M5", "M5 direction Bobigny (1 station)", 2),
            ("République via M5", "republique", "M5", "M5 direction Bobigny (3 stations)", 6),
            ("Canal Saint-Martin", "canal-saint-martin", "à pied", "10 min nord", 10),
            ("Père-Lachaise via M5 + M2 ou M9", "pere-lachaise", "M5 + M2/M9", "M5 → Oberkampf + M9", 10)
        ]
    },
    "breguet-sabin": {
        "addr": "Bd Richard Lenoir / rue Bréguet, 75011 Paris", "arr": "11e (Paris)",
        "seo": "Station Bréguet - Sabin : M5 dans le 11e arr. Abraham Louis Breguet horloger genevois et Joseph Sabin avocat. Quartier Bastille.",
        "tagline": "M5 — Bréguet horloger et Sabin avocat",
        "hero_desc": "Station <strong>Bréguet - Sabin</strong> dans le <strong>11e arrondissement</strong>, sur le boulevard Richard-Lenoir. Desservie par la <strong>M5</strong>, ouverte le <strong>17 décembre 1907</strong>. Nommée d'après <strong>Abraham Louis Breguet</strong> (1747-1823), <strong>horloger genevois</strong> mondialement célèbre, et <strong>Joseph Sabin</strong>, avocat parisien.",
        "intros": [
            "La station <strong>Bréguet - Sabin</strong> est située dans le <strong>11e arrondissement de Paris</strong>, sur le <strong>boulevard Richard-Lenoir</strong> à l'intersection avec la rue Bréguet. Elle est desservie par la <strong>M5</strong>, entre <strong>Richard-Lenoir</strong> (1 station nord) et <strong>Bastille</strong> (1 station sud). Bus 56, 91.",
            "Ouverte le <strong>17 décembre 1907</strong> avec la M5 originelle.",
            "Le nom <strong>Bréguet</strong> commémore <strong>Abraham Louis Breguet</strong> (1747-1823), <strong>horloger genevois</strong> mondialement célèbre, installé à Paris. <strong>Inventeur de plusieurs mécanismes horlogers majeurs</strong>. <strong>Sabin</strong> commémore <strong>Joseph Sabin</strong>, avocat parisien."
        ],
        "hist_title": "1907 : M5, Bréguet horloger mythique",
        "hist": [
            "La station <strong>Bréguet - Sabin</strong> ouvre le <strong>17 décembre 1907</strong> avec la M5 originelle (Gare du Nord ↔ Place Mazas).",
            "<strong>Abraham Louis Breguet</strong> (1747-1823), <strong>horloger genevois</strong>, est l'un des <strong>plus grands horlogers de l'histoire</strong>. <strong>Né à Neuchâtel (Suisse)</strong>, installé à Paris dès 1762.",
            "<strong>Inventions majeures</strong> : <strong>tourbillon</strong> (1801, brevet) — mécanisme compensant la gravité ; <strong>spiral plat</strong> ; <strong>échappement à chronomètre</strong> ; <strong>répétitions minutes</strong> à gong ; <strong>aiguilles Breguet</strong> (style spécifique). <strong>Horloger officiel</strong> de la <strong>famille royale de France</strong> sous Louis XVI, puis de <strong>Napoléon</strong>, puis des Bourbons.",
            "<strong>Maison Breguet</strong> fondée en 1775, encore active aujourd'hui (propriété du <strong>groupe Swatch</strong> depuis 1999). <strong>Marque de référence</strong> de la haute horlogerie suisse mondiale.",
            "<strong>Joseph Sabin</strong> (1830-1881), <strong>avocat parisien</strong>. Spécialisé dans la défense des prévenus politiques sous le Second Empire."
        ],
        "faq": [
            ("Quelle ligne dessert Bréguet - Sabin ?", "Uniquement la <strong>M5</strong>."),
            ("Qui est Bréguet ?", "<strong>Abraham Louis Breguet</strong> (1747-1823), <strong>horloger genevois mondialement célèbre</strong>. Installé à Paris dès 1762. <strong>Inventions</strong> : tourbillon (1801), spiral plat, échappement chronomètre. <strong>Horloger officiel de la famille royale de France</strong>, puis de <strong>Napoléon</strong>."),
            ("Qui est Sabin ?", "<strong>Joseph Sabin</strong> (1830-1881), <strong>avocat parisien</strong>. Spécialisé dans la défense des prévenus politiques sous le Second Empire."),
            ("La Maison Breguet existe-t-elle encore ?", "<strong>Oui</strong>. <strong>Fondée en 1775</strong>, encore active aujourd'hui. Propriété du <strong>groupe Swatch</strong> depuis 1999. Marque de référence de la haute horlogerie suisse."),
            ("Comment aller à Bastille ?", "<strong>M5 directe</strong> : 1 station (~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station 1907.")
        ],
        "tips": [
            "Pour <strong>Bastille</strong> : M5 directe (1 station).",
            "Pour <strong>République</strong> : M5 directe (4 stations).",
            "Pour <strong>Marché Bastille</strong> (Richard-Lenoir) : M5 directe (1 station).",
            "Pour <strong>Oberkampf</strong> (vie nocturne) : M5 directe (2 stations).",
            "Quartier 11e proche Bastille."
        ],
        "trivia": [
            ("⌚", "Abraham Louis Breguet — inventeur du tourbillon (1801)", "<strong>Abraham Louis Breguet</strong> (1747-1823), <strong>horloger genevois mondialement célèbre</strong>, est l'un des <strong>plus grands horlogers de l'histoire</strong>. <strong>Né à Neuchâtel (Suisse)</strong>, installé à Paris dès 1762. <strong>Inventions majeures</strong> : <strong>tourbillon</strong> (1801, brevet) — mécanisme compensant la gravité dans les montres ; <strong>spiral plat</strong> ; <strong>échappement à chronomètre</strong> ; <strong>répétitions minutes</strong> à gong ; <strong>aiguilles Breguet</strong> (style caractéristique). <strong>Horloger officiel</strong> de la <strong>famille royale de France</strong> sous Louis XVI, puis de <strong>Napoléon</strong>, puis des Bourbons. <strong>Maison Breguet</strong> fondée en 1775, encore active aujourd'hui (Swatch Group depuis 1999).")
        ],
        "itin": [
            ("Bastille via M5", "bastille", "M5", "M5 direction Place d'Italie (1 station)", 2),
            ("Richard-Lenoir via M5", "richard-lenoir", "M5", "M5 direction Bobigny (1 station)", 2),
            ("République via M5", "republique", "M5", "M5 direction Bobigny (4 stations)", 8),
            ("Oberkampf via M5", "oberkampf", "M5", "M5 direction Bobigny (2 stations)", 4),
            ("Quai de la Rapée via M5", "quai-de-la-rapee", "M5", "M5 direction Place d'Italie (2 stations)", 4),
            ("Marché Bastille (jeudis/dimanches)", "marche-bastille", "à pied", "5 min", 5)
        ]
    },
    "quai-de-la-rapee": {
        "addr": "Quai de la Rapée, 75012 Paris", "arr": "12e (Paris)",
        "seo": "Station Quai de la Rapée : M5 dans le 12e arr., AÉRIENNE au-dessus de la Seine (pont d'Austerlitz). Vue spectaculaire. Institut Médico-Légal à proximité.",
        "tagline": "M5 — station aérienne sur la Seine (pont d'Austerlitz)",
        "hero_desc": "Station <strong>Quai de la Rapée</strong> dans le <strong>12e arrondissement</strong>, sur le <strong>quai de la Rapée</strong>. Desservie par la <strong>M5</strong>, ouverte le <strong>17 décembre 1907</strong>. <strong>Station aérienne</strong> au-dessus de la Seine, sur le <strong>pont d'Austerlitz</strong>. <strong>Vue spectaculaire</strong> sur la Seine et les bords. À proximité : l'<strong>Institut Médico-Légal</strong> (morgue de Paris).",
        "intros": [
            "La station <strong>Quai de la Rapée</strong> est située dans le <strong>12e arrondissement de Paris</strong>, sur le <strong>quai de la Rapée</strong>. Elle est desservie par la <strong>M5</strong>, entre <strong>Bastille</strong> (1 station nord) et <strong>Gare d'Austerlitz</strong> (1 station sud, M5+M10+RER C+gare). Bus 24, 87.",
            "Ouverte le <strong>17 décembre 1907</strong> avec la M5 originelle.",
            "<strong>Station aérienne</strong> au-dessus de la <strong>Seine</strong> sur le <strong>pont d'Austerlitz</strong>. <strong>Vue spectaculaire</strong> sur la Seine, les <strong>Voies sur berges</strong>, le <strong>port de l'Arsenal</strong>, l'<strong>île Louviers</strong> (disparue mais souvenir). À <strong>2 min</strong> : l'<strong>Institut Médico-Légal</strong> (morgue de Paris)."
        ],
        "hist_title": "1907 : M5 aérienne sur la Seine",
        "hist": [
            "La station <strong>Quai de la Rapée</strong> ouvre le <strong>17 décembre 1907</strong> avec la M5 originelle (Gare du Nord ↔ Place Mazas).",
            "<strong>Configuration unique</strong> : <strong>station aérienne</strong> au-dessus de la <strong>Seine</strong>, sur le <strong>pont d'Austerlitz</strong>. Construite sur le pont métallique de la Seine. <strong>Vue spectaculaire</strong> sur la Seine et les bords.",
            "Le <strong>pont d'Austerlitz</strong> a été construit entre <strong>1801 et 1807</strong> en commémoration de la <strong>bataille d'Austerlitz</strong> (2 décembre 1805) — victoire majeure de Napoléon contre les Autrichiens et Russes.",
            "À proximité : l'<strong>Institut Médico-Légal</strong> (IML), <strong>morgue de Paris</strong>, où sont effectuées les autopsies médico-légales. Bâtiment de 1923. À côté : la <strong>place Mazas</strong> (anciennement terminus de la M5 jusqu'en 1942).",
            "Le quai de la Rapée tire son nom du <strong>Sieur de la Rapée</strong>, propriétaire des terrains au XVIIe siècle. <strong>Anciens entrepôts</strong> de bois pour le chauffage parisien."
        ],
        "faq": [
            ("Quelle ligne dessert Quai de la Rapée ?", "Uniquement la <strong>M5</strong>."),
            ("La station est-elle aérienne ?", "<strong>Oui</strong>. <strong>Station aérienne au-dessus de la Seine</strong>, sur le <strong>pont d'Austerlitz</strong>. <strong>Vue spectaculaire</strong> sur la Seine."),
            ("Qu'est-ce que l'Institut Médico-Légal ?", "L'<strong>IML</strong> est la <strong>morgue de Paris</strong>, où sont effectuées les autopsies médico-légales. Bâtiment de 1923. À 2 min de la station."),
            ("Pourquoi le nom Quai de la Rapée ?", "Du <strong>Sieur de la Rapée</strong>, propriétaire des terrains au XVIIe siècle. <strong>Anciens entrepôts</strong> de bois pour le chauffage parisien."),
            ("Comment aller à Bastille ?", "<strong>M5 directe</strong> : 1 station (~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station 1907.")
        ],
        "tips": [
            "<strong>Vue aérienne sur la Seine</strong> depuis les quais — unique.",
            "Pour <strong>Bastille</strong> : M5 directe (1 station).",
            "Pour <strong>Gare d'Austerlitz</strong> (gare + M10 + RER C) : M5 directe (1 station).",
            "<strong>Voies sur berges</strong> à côté.",
            "<strong>Port de l'Arsenal</strong> à 5 min."
        ],
        "trivia": [
            ("🌉", "Station aérienne sur la Seine (pont d'Austerlitz 1807)", "La station <strong>Quai de la Rapée</strong> est l'une des <strong>rares stations aériennes au-dessus de la Seine</strong> du métro parisien (avec Quai de la Gare M6, Bercy M6, Cité M4 partiellement). Construite sur le <strong>pont d'Austerlitz</strong> (1801-1807, en commémoration de la <strong>bataille d'Austerlitz</strong> du 2 décembre 1805 — victoire majeure de Napoléon contre les Autrichiens et Russes). <strong>Vue spectaculaire</strong> depuis les quais : Seine, Voies sur berges, port de l'Arsenal."),
            ("⚖️", "Institut Médico-Légal — morgue de Paris (1923)", "À <strong>2 min</strong> de la station, l'<strong>Institut Médico-Légal</strong> (IML) est la <strong>morgue de Paris</strong>, où sont effectuées les <strong>autopsies médico-légales</strong> en cas de mort suspecte ou non identifiée. Bâtiment de <strong>1923</strong>, conçu par Albert Tournaire. <strong>Successeur de l'ancienne morgue de l'Île de la Cité</strong> (XIXe siècle), célèbre pour ses expositions publiques des corps non identifiés (pratique abandonnée 1907).")
        ],
        "itin": [
            ("Bastille via M5", "bastille", "M5", "M5 direction Bobigny (1 station)", 2),
            ("Gare d'Austerlitz via M5", "gare-d-austerlitz", "M5", "M5 direction Place d'Italie (1 station)", 2),
            ("Voies sur berges (rive droite)", "voies-sur-berges", "à pied", "Sortie directe", 1),
            ("Port de l'Arsenal", "port-arsenal", "à pied", "5 min nord", 5),
            ("Institut Médico-Légal", "institut-medico-legal", "à pied", "2 min", 2),
            ("Place d'Italie via M5", "place-d-italie", "M5", "M5 direction Place d'Italie (3 stations)", 6)
        ]
    },
    "gare-d-austerlitz": {
        "addr": "Bd de l'Hôpital, 75013 Paris", "arr": "13e (Paris)",
        "seo": "Station Gare d'Austerlitz : M5 + M10 + RER C + gare SNCF dans le 13e arr. Trains vers le sud-ouest de la France (Toulouse, Bordeaux). Jardin des Plantes proche.",
        "tagline": "M5 + M10 + RER C — gare SNCF Austerlitz, Jardin des Plantes",
        "hero_desc": "Station <strong>Gare d'Austerlitz</strong> dans le <strong>13e arrondissement</strong>, sur le boulevard de l'Hôpital. Desservie par <strong>M5</strong>, <strong>M10</strong>, <strong>RER C</strong> et la <strong>gare SNCF Austerlitz</strong>. Trains vers le <strong>sud-ouest de la France</strong> (Toulouse, Bordeaux, Cahors, Limoges). À proximité : le <strong>Jardin des Plantes</strong> (Muséum national d'Histoire naturelle).",
        "intros": [
            "La station <strong>Gare d'Austerlitz</strong> est située dans le <strong>13e arrondissement de Paris</strong>, sur le boulevard de l'Hôpital. Elle est desservie par <strong>3 modes</strong> : <strong>M5</strong> (Bobigny ↔ Place d'Italie), <strong>M10</strong> (Boulogne ↔ Gare d'Austerlitz, terminus est) et <strong>RER C</strong>. Correspondance directe avec la <strong>gare SNCF Paris-Austerlitz</strong>. Bus 24, 57, 61, 63, 89, 91.",
            "La <strong>gare SNCF Austerlitz</strong> est l'une des <strong>6 grandes gares parisiennes</strong>. Trains vers le <strong>sud-ouest de la France</strong> : <strong>Toulouse</strong>, <strong>Bordeaux</strong> (avant 2017, transféré vers Montparnasse pour LGV), <strong>Cahors</strong>, <strong>Limoges</strong>, <strong>Châteauroux</strong>. Trains de nuit Intercités (Latour-de-Carol, Rodez, Cerbère).",
            "À <strong>10 min</strong> : le <strong>Jardin des Plantes</strong> (Muséum national d'Histoire naturelle, <strong>23 ha</strong>, créé en 1635 sous Louis XIII). <strong>Grande Galerie de l'Évolution</strong>, <strong>ménagerie</strong>, <strong>serres tropicales</strong>."
        ],
        "hist_title": "1840 : gare, 1907 : M5, 1924 : M10",
        "hist": [
            "La <strong>gare SNCF Paris-Austerlitz</strong> est inaugurée en <strong>1840</strong> comme terminus de la <strong>Compagnie du Paris-Orléans</strong>. <strong>L'une des plus anciennes gares de Paris</strong>. Façade actuelle de 1865 (architecte Pierre-Louis Renaud).",
            "La station <strong>M5</strong> ouvre le <strong>17 décembre 1907</strong>. La station <strong>M10</strong> arrive le <strong>26 avril 1939</strong> (Gare d'Austerlitz est terminus est M10). La <strong>gare RER C</strong> ouvre en <strong>1981</strong> avec l'extension du RER C.",
            "La gare SNCF a longtemps été le <strong>terminus pour le sud-ouest de la France</strong> : trains vers Bordeaux, Toulouse, Limoges. Avec l'ouverture de la <strong>LGV Sud Europe Atlantique en 2017</strong>, les trains vers Bordeaux ont été <strong>transférés à Montparnasse</strong>. Austerlitz conserve les trains <strong>Intercités</strong> et <strong>Trains de nuit</strong> (Latour-de-Carol, Rodez, Cerbère, Briançon).",
            "À <strong>10 min</strong> : le <strong>Jardin des Plantes</strong>, créé en <strong>1635 sous Louis XIII</strong> par Guy de La Brosse comme <strong>Jardin du Roi</strong>. Devenu <strong>Muséum national d'Histoire naturelle</strong> en 1793. <strong>23 hectares</strong>. Lieu emblématique : <strong>Grande Galerie de l'Évolution</strong>, <strong>ménagerie</strong> (1793, plus ancienne ménagerie en activité au monde), <strong>serres tropicales</strong>, <strong>jardin alpin</strong>."
        ],
        "faq": [
            ("Quelles lignes desservent Gare d'Austerlitz ?", "<strong>M5</strong>, <strong>M10</strong> (terminus est), <strong>RER C</strong>, et la <strong>gare SNCF</strong>. Bus 24, 57, 61, 63, 89, 91."),
            ("Quels trains partent d'Austerlitz ?", "Trains vers le <strong>sud-ouest de la France</strong> : <strong>Toulouse</strong>, <strong>Cahors</strong>, <strong>Limoges</strong>, <strong>Châteauroux</strong>. <strong>Trains de nuit Intercités</strong> (Latour-de-Carol, Rodez, Cerbère, Briançon). Bordeaux transféré à Montparnasse depuis 2017 (LGV)."),
            ("Où est le Jardin des Plantes ?", "<strong>10 min à pied</strong>. <strong>Muséum national d'Histoire naturelle</strong>, créé en <strong>1635 sous Louis XIII</strong>. 23 hectares. Grande Galerie de l'Évolution, ménagerie, serres tropicales."),
            ("Comment aller à Châtelet ?", "<strong>M10 directe</strong> ne va pas à Châtelet. <strong>M5 vers Bastille + M1 vers Châtelet</strong> : ~10 min. Ou <strong>RER C jusqu'à Saint-Michel</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>. Gare SNCF PMR, quais M5/M10 historiques partiels.")
        ],
        "tips": [
            "<strong>Jardin des Plantes</strong> à 10 min — Muséum d'Histoire naturelle.",
            "<strong>Grande Galerie de l'Évolution</strong> à voir.",
            "Trains nuit Intercités : <strong>Latour-de-Carol</strong>, <strong>Rodez</strong>, <strong>Cerbère</strong>.",
            "Pour <strong>Place d'Italie</strong> : M5 directe (2 stations).",
            "Pour <strong>Saint-Michel</strong> : RER C directe (1 station)."
        ],
        "trivia": [
            ("🚆", "Gare Paris-Austerlitz (1840) — l'une des plus anciennes", "La <strong>gare SNCF Paris-Austerlitz</strong> est inaugurée en <strong>1840</strong> comme terminus de la <strong>Compagnie du Paris-Orléans</strong>. <strong>L'une des plus anciennes gares de Paris</strong>. Façade actuelle de <strong>1865</strong>. Historiquement terminus pour le <strong>sud-ouest de la France</strong> (Bordeaux, Toulouse, Limoges). Avec l'ouverture de la <strong>LGV Sud Europe Atlantique en 2017</strong>, les trains vers Bordeaux ont été transférés à Montparnasse. Austerlitz conserve les <strong>Intercités</strong> et <strong>trains de nuit</strong> (Latour-de-Carol, Rodez, Cerbère, Briançon)."),
            ("🌿", "Jardin des Plantes (1635) — Muséum Histoire naturelle", "Le <strong>Jardin des Plantes</strong> à 10 min de la station est l'un des plus emblématiques jardins parisiens. Créé en <strong>1635 sous Louis XIII</strong> par <strong>Guy de La Brosse</strong> comme <strong>Jardin du Roi</strong>. Devenu <strong>Muséum national d'Histoire naturelle</strong> en <strong>1793</strong> (Révolution). <strong>23 hectares</strong>. <strong>Grande Galerie de l'Évolution</strong> (1994, rénovation spectaculaire). <strong>Ménagerie</strong> (1793, plus ancienne ménagerie en activité au monde). <strong>Serres tropicales</strong> (1830s, classés MH). <strong>Jardin alpin</strong>. Sont également au sein : galeries de Minéralogie, de Paléontologie, etc.")
        ],
        "itin": [
            ("Gare SNCF Austerlitz", "gare-austerlitz-sncf", "à pied", "Sortie directe", 2),
            ("Jardin des Plantes", "jardin-plantes", "à pied", "10 min", 10),
            ("Place d'Italie via M5", "place-d-italie", "M5", "M5 direction Place d'Italie (2 stations)", 4),
            ("Châtelet via M5 + M1", "chatelet", "M5 + M1", "M5 jusqu'à Bastille + M1", 10),
            ("Saint-Michel via RER C", "saint-michel-notre-dame", "RER C", "RER C direction Saint-Michel (1 station)", 3),
            ("Bastille via M5", "bastille", "M5", "M5 direction Bobigny (2 stations)", 4)
        ]
    },
    "saint-marcel": {
        "addr": "Bd Saint-Marcel, 75013 Paris", "arr": "13e (Paris)",
        "seo": "Station Saint-Marcel : M5 dans le 13e arr., boulevard Saint-Marcel. Hôpital de la Pitié-Salpêtrière à 10 min. Quartier résidentiel 13e.",
        "tagline": "M5 — Pitié-Salpêtrière proche",
        "hero_desc": "Station <strong>Saint-Marcel</strong> dans le <strong>13e arrondissement</strong>, sur le <strong>boulevard Saint-Marcel</strong>. Desservie par la <strong>M5</strong>, ouverte le <strong>17 décembre 1907</strong>. À <strong>10 min</strong> : l'<strong>hôpital de la Pitié-Salpêtrière</strong> (l'un des plus grands hôpitaux d'Europe).",
        "intros": [
            "La station <strong>Saint-Marcel</strong> est située dans le <strong>13e arrondissement de Paris</strong>, sur le <strong>boulevard Saint-Marcel</strong>. Elle est desservie par la <strong>M5</strong>, entre <strong>Gare d'Austerlitz</strong> (1 station nord, M5+M10+RER C) et <strong>Campo-Formio</strong> (1 station sud). Bus 27, 47.",
            "Ouverte le <strong>17 décembre 1907</strong> avec la M5 originelle.",
            "Le nom <strong>Saint-Marcel</strong> commémore <strong>saint Marcel de Paris</strong> (IVe siècle), <strong>9e évêque de Paris</strong>. À <strong>10 min</strong> : l'<strong>hôpital de la Pitié-Salpêtrière</strong>, l'un des plus grands hôpitaux d'Europe (1656)."
        ],
        "hist_title": "1907 : M5, et la Pitié-Salpêtrière",
        "hist": [
            "La station <strong>Saint-Marcel</strong> ouvre le <strong>17 décembre 1907</strong> avec la M5 originelle (Gare du Nord ↔ Place Mazas).",
            "Le nom commémore <strong>saint Marcel de Paris</strong> (IVe siècle), <strong>9e évêque de Paris</strong>. <strong>Mort en 436</strong>. Patron secondaire de Paris (après sainte Geneviève).",
            "À <strong>10 min à pied</strong> : l'<strong>hôpital de la Pitié-Salpêtrière</strong>, l'un des <strong>plus grands hôpitaux d'Europe</strong>. <strong>~85 000 m²</strong>, ~3 500 lits, ~12 000 personnels. <strong>Fondé en 1656</strong> par Louis XIV comme <strong>asile de la Pitié et de la Salpêtrière</strong> (réunissant 2 institutions distinctes en 1964).",
            "<strong>Spécialités</strong> : neurologie (Charcot, Pinel), psychiatrie, gérontologie, transplantations. Hôpital universitaire (faculté de médecine Sorbonne Université). <strong>Pinel y libérera les aliénés de leurs chaînes en 1795</strong>. <strong>Charcot</strong> y enseigne la neurologie (1880s).",
            "Le quartier autour est <strong>résidentiel populaire</strong> du 13e."
        ],
        "faq": [
            ("Quelle ligne dessert Saint-Marcel ?", "Uniquement la <strong>M5</strong>."),
            ("Qu'est-ce que la Pitié-Salpêtrière ?", "L'<strong>un des plus grands hôpitaux d'Europe</strong>, à 10 min. <strong>Fondé en 1656</strong> par Louis XIV. <strong>~85 000 m², 3 500 lits, 12 000 personnels</strong>. Spécialités : neurologie, psychiatrie, transplantations."),
            ("Qui est saint Marcel ?", "<strong>Saint Marcel de Paris</strong> (IVe siècle), <strong>9e évêque de Paris</strong>. Mort en 436. Patron secondaire de Paris."),
            ("Comment aller à Place d'Italie ?", "<strong>M5 directe</strong> : 2 stations vers le sud (~4 min)."),
            ("Comment aller à Gare d'Austerlitz ?", "<strong>M5 directe</strong> : 1 station (~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station 1907.")
        ],
        "tips": [
            "<strong>Hôpital de la Pitié-Salpêtrière</strong> à 10 min.",
            "Pour <strong>Gare d'Austerlitz</strong> (gare SNCF) : M5 directe (1 station).",
            "Pour <strong>Place d'Italie</strong> : M5 directe (2 stations).",
            "Pour <strong>Jardin des Plantes</strong> : M5 jusqu'à Gare d'Austerlitz + à pied.",
            "Quartier résidentiel populaire du 13e."
        ],
        "trivia": [
            ("🏥", "Hôpital Pitié-Salpêtrière (1656) — plus grand hôpital d'Europe", "À <strong>10 min</strong> de la station, l'<strong>hôpital de la Pitié-Salpêtrière</strong> est l'un des <strong>plus grands hôpitaux d'Europe</strong>. <strong>Fondé en 1656</strong> par <strong>Louis XIV</strong> comme <strong>asile de la Pitié</strong> et <strong>Salpêtrière</strong> (2 institutions réunies en 1964). <strong>~85 000 m²</strong>, <strong>~3 500 lits</strong>, <strong>~12 000 personnels</strong>. <strong>Spécialités</strong> : neurologie, psychiatrie, gérontologie, transplantations. Hôpital universitaire (Sorbonne Université). <strong>Pinel y libère les aliénés de leurs chaînes en 1795</strong> — événement fondateur de la psychiatrie. <strong>Charcot</strong> y enseigne la neurologie (1880s, hystérie, sclérose en plaques). <strong>Princesse Diana</strong> y meurt en 1997.")
        ],
        "itin": [
            ("Pitié-Salpêtrière", "pitie-salpetriere", "à pied", "10 min", 10),
            ("Gare d'Austerlitz via M5", "gare-d-austerlitz", "M5", "M5 direction Bobigny (1 station)", 2),
            ("Place d'Italie via M5", "place-d-italie", "M5", "M5 direction Place d'Italie (2 stations)", 4),
            ("Jardin des Plantes via M5 + à pied", "jardin-plantes", "M5 + à pied", "M5 → Austerlitz + 10 min", 14),
            ("Bastille via M5", "bastille", "M5", "M5 direction Bobigny (3 stations)", 6),
            ("Campo-Formio via M5", "campo-formio", "M5", "M5 direction Place d'Italie (1 station)", 2)
        ]
    },
    "campo-formio": {
        "addr": "Av. des Gobelins / Bd Saint-Marcel, 75013 Paris", "arr": "13e (Paris)",
        "seo": "Station Campo-Formio : M5 dans le 13e arr. Traité de Campo-Formio (1797), accord de paix Bonaparte/Autriche. Quartier 13e.",
        "tagline": "M5 — Traité de Campo-Formio (Bonaparte 1797)",
        "hero_desc": "Station <strong>Campo-Formio</strong> dans le <strong>13e arrondissement</strong>, à proximité de l'avenue des Gobelins. Desservie par la <strong>M5</strong>, ouverte le <strong>17 décembre 1907</strong>. Nommée d'après le <strong>traité de Campo-Formio</strong> (17 octobre 1797), <strong>accord de paix</strong> signé par <strong>Bonaparte</strong> entre la France et l'Autriche.",
        "intros": [
            "La station <strong>Campo-Formio</strong> est située dans le <strong>13e arrondissement de Paris</strong>, à proximité de l'<strong>avenue des Gobelins</strong>. Elle est desservie par la <strong>M5</strong>, entre <strong>Saint-Marcel</strong> (1 station nord) et <strong>Place d'Italie</strong> (1 station sud, terminus M5+M6+M7). Bus 27, 47.",
            "Ouverte le <strong>17 décembre 1907</strong> avec la M5 originelle.",
            "Le nom <strong>Campo-Formio</strong> commémore le <strong>traité de Campo-Formio</strong>, signé le <strong>17 octobre 1797</strong> entre la <strong>France républicaine et l'Autriche</strong>. Négocié par <strong>Napoléon Bonaparte</strong> alors général en Italie. Met fin à la <strong>première guerre de coalition</strong>."
        ],
        "hist_title": "Traité de Campo-Formio (1797) — Bonaparte et l'Italie",
        "hist": [
            "La station <strong>Campo-Formio</strong> ouvre le <strong>17 décembre 1907</strong> avec la M5 originelle.",
            "Le nom commémore le <strong>traité de Campo-Formio</strong>, signé le <strong>17 octobre 1797</strong> entre la <strong>France républicaine et l'Autriche</strong> (Saint Empire). <strong>Négocié par Napoléon Bonaparte</strong>, alors <strong>général en chef de l'Armée d'Italie</strong> (28 ans).",
            "<strong>Contexte</strong> : la <strong>campagne d'Italie</strong> de Bonaparte (1796-1797) a écrasé les armées autrichiennes en Italie du Nord. Bonaparte avance jusqu'à <strong>100 km de Vienne</strong>, forçant l'Autriche à négocier.",
            "<strong>Termes</strong> : la France obtient la <strong>Belgique (Pays-Bas autrichiens)</strong>, la <strong>rive gauche du Rhin</strong>, et l'<strong>Italie du Nord</strong> (République cisalpine). L'Autriche reçoit <strong>Venise</strong> et la <strong>Vénétie</strong> (fin de la République de Venise, 1 100 ans d'indépendance).",
            "<strong>Première grande victoire diplomatique de Bonaparte</strong>, qui lance sa carrière politique. Met fin à la <strong>première guerre de coalition</strong> (1792-1797). Préfigure les <strong>traités impériaux ultérieurs</strong> (Lunéville 1801, Presbourg 1805).",
            "Le quartier autour est résidentiel du 13e. À proximité : <strong>Manufacture des Gobelins</strong> (tapisseries royales depuis 1662)."
        ],
        "faq": [
            ("Quelle ligne dessert Campo-Formio ?", "Uniquement la <strong>M5</strong>."),
            ("Qu'est-ce que le traité de Campo-Formio ?", "<strong>Traité de paix signé le 17 octobre 1797</strong> entre la <strong>France républicaine et l'Autriche</strong>. <strong>Négocié par Napoléon Bonaparte</strong> alors général en Italie. Met fin à la <strong>première guerre de coalition</strong>."),
            ("Qu'a obtenu la France ?", "<strong>Belgique, rive gauche du Rhin, Italie du Nord</strong> (République cisalpine). L'Autriche reçoit <strong>Venise</strong> et la Vénétie (fin de la République de Venise)."),
            ("Comment aller à Place d'Italie ?", "<strong>M5 directe</strong> : 1 station (terminus sud)."),
            ("Comment aller à Châtelet ?", "<strong>M5 vers Bastille + M1</strong> : ~14 min."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Station 1907.")
        ],
        "tips": [
            "<strong>Manufacture des Gobelins</strong> à 10 min — tapisseries royales 1662.",
            "Pour <strong>Place d'Italie</strong> (hub M5+M6+M7) : M5 directe (1 station).",
            "Pour <strong>Saint-Marcel</strong> : M5 directe (1 station).",
            "Pour <strong>Pitié-Salpêtrière</strong> : M5 vers Saint-Marcel + à pied.",
            "Pour <strong>Bastille</strong> : M5 directe."
        ],
        "trivia": [
            ("📜", "Traité de Campo-Formio (1797) — Bonaparte 28 ans diplomate", "Le <strong>traité de Campo-Formio</strong>, signé le <strong>17 octobre 1797</strong>, est un <strong>accord de paix entre la France républicaine et l'Autriche</strong> (Saint Empire). <strong>Négocié par Napoléon Bonaparte</strong> alors <strong>général en chef de l'Armée d'Italie</strong>, à <strong>28 ans</strong>. Met fin à la <strong>première guerre de coalition</strong> (1792-1797). <strong>Première grande victoire diplomatique de Bonaparte</strong>, qui lance sa carrière politique. <strong>Termes</strong> : France obtient Belgique, rive gauche du Rhin, Italie du Nord. Autriche reçoit <strong>Venise</strong> (fin de la République de Venise après 1 100 ans d'indépendance).")
        ],
        "itin": [
            ("Place d'Italie via M5", "place-d-italie", "M5", "M5 terminus sud (1 station)", 2),
            ("Saint-Marcel via M5", "saint-marcel", "M5", "M5 direction Bobigny (1 station)", 2),
            ("Manufacture des Gobelins", "manufacture-gobelins", "à pied", "10 min", 10),
            ("Bastille via M5", "bastille", "M5", "M5 direction Bobigny (4 stations)", 8),
            ("Gare d'Austerlitz via M5", "gare-d-austerlitz", "M5", "M5 direction Bobigny (2 stations)", 4),
            ("Tour Eiffel via M5 + M6", "tour-eiffel", "M5 + M6", "M5 → Place d'Italie + M6", 25)
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
    elif "Pantin" in c["arr"]:
        d["tariff_zone"] = 2
        d["tariff_zone_context"] = "Seine-Saint-Denis (93), zone tarifaire 2"
        d["commune"] = "Pantin"
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
