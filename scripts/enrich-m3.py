#!/usr/bin/env python3
"""Enrichit M3 17 stations avec contenu T0 Wikipedia FR."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    "pont-de-levallois-becon": {
        "addr": "Place du Pont-de-Levallois, 92300 Levallois-Perret", "arr": "Levallois-Perret (92)",
        "seo": "Station Pont de Levallois - Bécon, terminus ouest M3 à Levallois-Perret (92). Pont sur la Seine, accès Pont de Levallois (île de la Jatte).",
        "tagline": "M3 — terminus ouest, Levallois-Perret (92)",
        "hero_desc": "Station <strong>Pont de Levallois - Bécon</strong>, <strong>terminus ouest de la M3</strong>, à <strong>Levallois-Perret</strong> (Hauts-de-Seine, 92). Ouverte le <strong>24 septembre 1937</strong> avec le prolongement Porte de Champerret ↔ Pont de Levallois. Située à proximité du <strong>pont de Levallois</strong> sur la Seine et du quartier <strong>Bécon-les-Bruyères</strong>.",
        "intros": [
            "La station <strong>Pont de Levallois - Bécon</strong> est <strong>terminus ouest de la M3</strong>, située à <strong>Levallois-Perret</strong> (Hauts-de-Seine, 92). Bus 53, 165, 174, 175, 274, 275, 467. À courte distance de la <strong>gare Bécon-les-Bruyères</strong> (Transilien L).",
            "Ouverte le <strong>24 septembre 1937</strong> avec le <strong>prolongement de la ligne 3</strong> de Porte de Champerret à Pont de Levallois. Dernier prolongement à l'ouest de la ligne.",
            "Le nom <strong>Pont de Levallois - Bécon</strong> combine deux références : le <strong>pont de Levallois</strong>, qui enjambe la Seine vers l'<strong>île de la Jatte</strong>, et le quartier <strong>Bécon</strong> (Bécon-les-Bruyères), village ancien de Levallois-Perret. <strong>Levallois-Perret</strong> (~65 000 habitants) est l'une des communes les plus densément peuplées d'Europe."
        ],
        "hist_title": "1937 : terminus ouest et pont sur la Seine",
        "hist": [
            "La station est <strong>inaugurée le 24 septembre 1937</strong> avec le <strong>prolongement de la ligne 3</strong> de Porte de Champerret à Pont de Levallois - Bécon. Ce <strong>dernier prolongement ouest</strong> de la ligne 3 dessert l'expansion résidentielle de <strong>Levallois-Perret</strong>.",
            "Le <strong>pont de Levallois</strong>, qui donne son nom à la station, enjambe la <strong>Seine</strong> entre Levallois-Perret et Neuilly-sur-Seine, donnant accès à l'<strong>île de la Jatte</strong>. Première version construite en <strong>1789</strong> (passerelle en bois), pont métallique en 1850, reconstruit plusieurs fois.",
            "<strong>Levallois-Perret</strong> (~65 000 habitants) est née de la fusion en <strong>1867</strong> du <strong>village de Bécon-les-Bruyères</strong> et du domaine de Champerret. Devient indépendante en <strong>1867</strong> avec le nom de son fondateur, <strong>Nicolas Eugène Levallois</strong> (1816-1879), industriel et urbaniste. C'est l'une des <strong>communes les plus densément peuplées d'Europe</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Pont de Levallois - Bécon ?", "Uniquement la <strong>M3</strong> (terminus ouest). Bus 53, 165, 174, 175, 274, 275, 467."),
            ("Quand a-t-elle ouvert ?", "Le <strong>24 septembre 1937</strong>."),
            ("Qu'est-ce que le pont de Levallois ?", "Pont sur la <strong>Seine</strong> entre Levallois-Perret et Neuilly-sur-Seine, donnant accès à l'<strong>île de la Jatte</strong>."),
            ("Pour Bécon-les-Bruyères Transilien L ?", "<strong>~10 min à pied</strong> via la rue Anatole-France."),
            ("Pour l'île de la Jatte ?", "<strong>~7 min à pied</strong> via le pont de Levallois."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Île de la Jatte</strong> à 7 min à pied — île de la Seine pittoresque (Maupassant, Seurat).",
            "<strong>Gare Bécon-les-Bruyères</strong> Transilien L à 10 min à pied.",
            "Pour <strong>Opéra</strong> et le centre de Paris : <strong>M3 directe</strong> (~22 min).",
            "Quartier résidentiel dense de <strong>Levallois-Perret</strong>.",
            "Zone tarifaire <strong>2</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("🏘️", "Levallois-Perret, ville fondée en 1867", "<strong>Levallois-Perret</strong> est née de la fusion en <strong>1867</strong> du <strong>village de Bécon-les-Bruyères</strong> et du domaine de Champerret. Devient une commune indépendante en <strong>1867</strong> avec le nom de son fondateur, <strong>Nicolas Eugène Levallois</strong> (1816-1879), industriel et urbaniste qui lotit le quartier. Population de <strong>~65 000 habitants</strong> sur seulement <strong>2,4 km²</strong>, l'une des <strong>communes les plus densément peuplées d'Europe</strong>."),
            ("🎨", "Île de la Jatte, refuge des artistes", "L'<strong>île de la Jatte</strong>, accessible via le pont de Levallois (~7 min à pied), est une <strong>île de la Seine</strong> située entre Levallois-Perret et Neuilly. Inspiratrice des <strong>impressionnistes</strong> et <strong>néo-impressionnistes</strong>. <strong>Georges Seurat</strong> y peignit son chef-d'œuvre <em>« Un dimanche après-midi à l'Île de la Grande Jatte »</em> (<strong>1884-1886</strong>). <strong>Maupassant</strong> y faisait du canotage. Aujourd'hui, parc urbain et chemin de promenade.")
        ],
        "itin": [
            ("Île de la Jatte", "pont-de-levallois-becon", "à pied", "Pont de Levallois (7 min)", 7),
            ("Bécon-les-Bruyères Transilien L", "pont-de-levallois-becon", "à pied", "Rue Anatole-France (10 min)", 10),
            ("Anatole France", "anatole-france", "M3", "M3 directe (1 station)", 2),
            ("Opéra", "opera", "M3", "M3 directe (10 stations)", 22),
            ("Saint-Lazare", "saint-lazare", "M3", "M3 directe (8 stations)", 18),
            ("République", "republique", "M3", "M3 directe (15 stations)", 30)
        ]
    },
    "anatole-france": {
        "addr": "Rue Anatole-France, 92300 Levallois-Perret", "arr": "Levallois-Perret (92)",
        "seo": "Station Anatole France (M3) à Levallois-Perret. Nommée d'après Anatole France (1844-1924), écrivain et Prix Nobel de littérature 1921.",
        "tagline": "M3 — Anatole France (Prix Nobel 1921)",
        "hero_desc": "Station <strong>Anatole France</strong> sur la <strong>rue Anatole-France</strong> à <strong>Levallois-Perret</strong> (Hauts-de-Seine, 92). Desservie par la <strong>M3</strong>, ouverte le <strong>24 septembre 1937</strong>. Nommée d'après <strong>Anatole France</strong> (<strong>1844-1924</strong>), <strong>écrivain français</strong> et <strong>Prix Nobel de littérature 1921</strong>.",
        "intros": [
            "La station <strong>Anatole France</strong> est implantée sur la <strong>rue Anatole-France</strong>, axe principal de <strong>Levallois-Perret</strong> (Hauts-de-Seine, 92). Desservie par la <strong>ligne 3 du métro</strong>, entre <strong>Pont de Levallois - Bécon</strong> (1 station) et <strong>Louise Michel</strong> (1 station). Bus 53, 165, 174, 175.",
            "Ouverte le <strong>24 septembre 1937</strong> avec le prolongement Porte de Champerret ↔ Pont de Levallois.",
            "Le nom <strong>Anatole France</strong> rend hommage à <strong>Jacques Anatole François Thibault dit Anatole France</strong> (<strong>1844-1924</strong>), <strong>écrivain, romancier et critique français</strong>, <strong>Prix Nobel de littérature 1921</strong>. Auteur de <em>Le Crime de Sylvestre Bonnard</em> (1881), <em>Thaïs</em> (1890), <em>L'Île des Pingouins</em> (1908), <em>Les dieux ont soif</em> (1912)."
        ],
        "hist_title": "1937 : Levallois-Perret et l'écrivain académicien",
        "hist": [
            "La station Anatole France est <strong>inaugurée le 24 septembre 1937</strong> avec le <strong>prolongement de la ligne 3</strong> à Pont de Levallois.",
            "Le nom <strong>Anatole France</strong> commémore <strong>Jacques Anatole François Thibault dit Anatole France</strong> (<strong>16 avril 1844 - 12 octobre 1924</strong>), <strong>écrivain, romancier, poète, critique et essayiste français</strong>. Né à Paris, fils d'un libraire des quais. Devient le <strong>plus grand écrivain français de la Belle Époque</strong>.",
            "<strong>Prix Nobel de littérature 1921</strong> <em>« en reconnaissance de la brillante qualité de ses œuvres littéraires, caractérisées par leur noblesse de style, leur profonde sympathie humaine, leur grâce et leur véritable tempérament gaulois »</em>. <strong>Membre de l'Académie française</strong> (élu en 1896). Œuvres : <em>Le Crime de Sylvestre Bonnard</em> (1881), <em>Thaïs</em> (1890), <em>L'Île des Pingouins</em> (1908), <em>Les dieux ont soif</em> (1912), <em>La Révolte des anges</em> (1914). Dreyfusard engagé."
        ],
        "faq": [
            ("Quelle ligne dessert Anatole France ?", "Uniquement la <strong>M3</strong>. Bus 53, 165, 174, 175."),
            ("Qui est Anatole France ?", "<strong>Anatole France</strong> (1844-1924), <strong>écrivain français</strong>, <strong>Prix Nobel de littérature 1921</strong>. Membre de l'Académie française. Auteur de <em>L'Île des Pingouins</em>, <em>Les dieux ont soif</em>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>24 septembre 1937</strong>."),
            ("Pour Pont de Levallois - Bécon ?", "<strong>M3 directe</strong> (1 station, terminus ouest)."),
            ("Pour Opéra ?", "<strong>M3 directe</strong> (~20 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "Quartier résidentiel dense de <strong>Levallois-Perret</strong>.",
            "Pour <strong>Pont de Levallois - Bécon</strong> et <strong>île de la Jatte</strong> : <strong>M3 directe</strong> (1 station).",
            "Pour <strong>Opéra</strong> et centre de Paris : <strong>M3 directe</strong> (~20 min).",
            "<strong>Mairie de Levallois-Perret</strong> à proximité.",
            "Zone tarifaire <strong>2</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("📚", "Anatole France, Prix Nobel 1921", "<strong>Anatole France</strong> (1844-1924), né <strong>Jacques Anatole François Thibault</strong>, devient à 37 ans avec <em>Le Crime de Sylvestre Bonnard</em> (1881) un <strong>écrivain célèbre</strong>. <strong>Membre de l'Académie française</strong> en <strong>1896</strong>. <strong>Prix Nobel de littérature 1921</strong> pour l'<em>« ensemble de son œuvre »</em>. <strong>Dreyfusard engagé</strong>, ami de <strong>Zola</strong>. Œuvres : <em>Thaïs</em> (1890), <em>L'Île des Pingouins</em> (1908, satire), <em>Les dieux ont soif</em> (1912, sur la Terreur). <strong>Funérailles nationales</strong> en 1924."),
            ("🏛️", "Académie française et l'engagement", "Élu à l'<strong>Académie française</strong> le <strong>23 janvier 1896</strong>, Anatole France a successivement été <strong>journaliste, bibliothécaire au Sénat, écrivain à plein temps</strong>. <strong>Dreyfusard engagé</strong>, il signe la pétition pour la révision du procès Dreyfus. Engagement <strong>socialiste</strong> à partir de 1904. Soutient la <strong>Révolution russe</strong> en 1917 (mais critique le tournant bolchevique).")
        ],
        "itin": [
            ("Pont de Levallois - Bécon (terminus)", "pont-de-levallois-becon", "M3", "M3 directe (1 station)", 2),
            ("Louise Michel", "louise-michel", "M3", "M3 directe (1 station)", 2),
            ("Opéra", "opera", "M3", "M3 directe (9 stations)", 20),
            ("Saint-Lazare", "saint-lazare", "M3", "M3 directe (7 stations)", 16),
            ("Champs-Élysées via Étoile", "george-v", "M3 + M1", "M3 → Étoile + M1", 16),
            ("Arc de Triomphe", "charles-de-gaulle-etoile", "M3 + M1", "M3 → Wagram + M1 via Étoile", 14)
        ]
    },
    "louise-michel": {
        "addr": "Place de la Liberté, 92300 Levallois-Perret", "arr": "Levallois-Perret (92)",
        "seo": "Station Louise Michel (M3) à Levallois-Perret. Nommée d'après Louise Michel (1830-1905), militante anarchiste et figure de la Commune de Paris.",
        "tagline": "M3 — Louise Michel (1830-1905), Commune et anarchie",
        "hero_desc": "Station <strong>Louise Michel</strong> sur la <strong>place de la Liberté</strong> à <strong>Levallois-Perret</strong> (Hauts-de-Seine, 92). Desservie par la <strong>M3</strong>, ouverte le <strong>24 septembre 1937</strong>. Nommée d'après <strong>Louise Michel</strong> (<strong>1830-1905</strong>), <strong>institutrice, militante anarchiste et féministe</strong>, figure majeure de la <strong>Commune de Paris</strong> (1871).",
        "intros": [
            "La station <strong>Louise Michel</strong> est implantée à <strong>Levallois-Perret</strong>, place de la Liberté (Hauts-de-Seine, 92). Elle est desservie par la <strong>ligne 3 du métro</strong>, entre <strong>Anatole France</strong> (1 station) et <strong>Porte de Champerret</strong> (1 station). Bus 53 et 165 en correspondance.",
            "Ouverte le <strong>24 septembre 1937</strong> avec le prolongement Porte de Champerret ↔ Pont de Levallois.",
            "Le nom <strong>Louise Michel</strong> rend hommage à <strong>Louise Michel</strong> (<strong>1830-1905</strong>), <strong>institutrice, militante anarchiste, féministe</strong>. Figure de la <strong>Commune de Paris</strong> (mars-mai 1871), elle fut <strong>déportée en Nouvelle-Calédonie</strong> de 1873 à 1880. Surnommée la <strong>« Vierge rouge »</strong>."
        ],
        "hist_title": "1937 : Levallois et la Vierge rouge",
        "hist": [
            "La station Louise Michel est <strong>inaugurée le 24 septembre 1937</strong> avec le <strong>prolongement de la ligne 3</strong> à Pont de Levallois.",
            "Le nom <strong>Louise Michel</strong> commémore <strong>Louise Michel</strong> (<strong>29 mai 1830 - 9 janvier 1905</strong>), <strong>institutrice, militante anarchiste, féministe et écrivaine française</strong>. Fille naturelle d'une servante et du fils d'un châtelain. Devient <strong>institutrice</strong>, puis militante <strong>blanquiste</strong> puis <strong>anarchiste</strong>.",
            "Figure majeure de la <strong>Commune de Paris</strong> (<strong>mars-mai 1871</strong>), elle combat sur les barricades en uniforme de la Garde nationale. <strong>Arrêtée</strong>, jugée par un conseil de guerre en décembre 1871, elle revendique sa participation et demande la mort : <em>« Puisqu'il semble que tout cœur qui bat pour la liberté n'a droit qu'à un peu de plomb, j'en réclame ma part. »</em> <strong>Déportée en Nouvelle-Calédonie</strong> de <strong>1873 à 1880</strong>. <strong>Amnistiée en 1880</strong>, elle reprend son activité militante. Surnommée la <strong>« Vierge rouge »</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Louise Michel ?", "Uniquement la <strong>M3</strong>. Bus 53 et 165."),
            ("Qui est Louise Michel ?", "<strong>Louise Michel</strong> (1830-1905), <strong>institutrice, militante anarchiste et féministe</strong>. Figure majeure de la <strong>Commune de Paris</strong> (1871). <strong>Déportée en Nouvelle-Calédonie</strong> (1873-1880). Surnommée la <strong>« Vierge rouge »</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>24 septembre 1937</strong>."),
            ("Pour Levallois-Perret centre ?", "<strong>~5 min à pied</strong> via la rue Anatole-France."),
            ("Pour Porte de Champerret ?", "<strong>M3 directe</strong> (1 station, retour Paris)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "Pour <strong>Porte de Champerret</strong> et retour Paris : <strong>M3 directe</strong> (1 station).",
            "<strong>Mairie de Levallois-Perret</strong> à proximité.",
            "Quartier résidentiel dense de <strong>Levallois-Perret</strong>.",
            "Pour <strong>Opéra</strong> : <strong>M3 directe</strong> (~19 min).",
            "Zone tarifaire <strong>2</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("⚔️", "Louise Michel, la « Vierge rouge » de la Commune", "<strong>Louise Michel</strong> (1830-1905), <strong>institutrice anarchiste</strong>, devient une <strong>figure mythique</strong> de la <strong>Commune de Paris</strong> (mars-mai 1871). Elle combat <strong>en uniforme de Garde nationale</strong> sur les barricades. Lors de son procès en décembre 1871, elle revendique tout : <em>« Si vous n'êtes pas des lâches, tuez-moi ! »</em>. <strong>Déportée à Nouméa</strong> (Nouvelle-Calédonie) de <strong>1873 à 1880</strong>, où elle <strong>défend les Kanaks</strong> révoltés contre la France. <strong>Amnistiée</strong>, elle poursuit son combat anarchiste jusqu'à sa mort."),
            ("📚", "Une figure du panthéon républicain", "<strong>Louise Michel</strong> est aujourd'hui une <strong>figure du panthéon républicain et féministe</strong>. De nombreuses <strong>écoles, rues et stations</strong> portent son nom (dont cette station, le métro Louise Michel à Paris). Son combat pour les <strong>droits des femmes</strong>, la <strong>justice sociale</strong> et contre le <strong>colonialisme</strong> en fait une <strong>icône</strong> du mouvement libertaire. <strong>Funérailles populaires</strong> en 1905, plus de <strong>100 000 personnes</strong> suivent son cortège.")
        ],
        "itin": [
            ("Porte de Champerret", "porte-de-champerret", "M3", "M3 directe (1 station)", 2),
            ("Anatole France", "anatole-france", "M3", "M3 directe (1 station)", 2),
            ("Pont de Levallois - Bécon", "pont-de-levallois-becon", "M3", "M3 directe (2 stations)", 4),
            ("Opéra", "opera", "M3", "M3 directe (8 stations)", 19),
            ("Saint-Lazare", "saint-lazare", "M3", "M3 directe (6 stations)", 14),
            ("Champs-Élysées", "george-v", "M3 + M1", "M3 → Étoile + M1", 15)
        ]
    },
    "porte-de-champerret": {
        "addr": "Place Stuart Merrill, 75017 Paris", "arr": "17e arrondissement (Paris)",
        "seo": "Station Porte de Champerret (M3) place Stuart Merrill dans le 17e. Ancien terminus M3, accès Palais des Congrès, parc Martin-Luther-King.",
        "tagline": "M3 — ancien terminus, Palais des Congrès proche",
        "hero_desc": "Station <strong>Porte de Champerret</strong>, <strong>place Stuart Merrill</strong> dans le <strong>17e arrondissement</strong>. Desservie par la <strong>M3</strong>, ouverte le <strong>23 mai 1911</strong>. <strong>Terminus ouest de la ligne 3</strong> jusqu'au <strong>24 septembre 1937</strong> (prolongement vers Pont de Levallois). Accès au <strong>parc Martin-Luther-King</strong> et au <strong>Palais des Congrès</strong>.",
        "intros": [
            "La station <strong>Porte de Champerret</strong> est implantée <strong>place Stuart Merrill</strong> dans le <strong>17e arrondissement</strong>, à la limite du périphérique. Elle est desservie par la <strong>ligne 3 du métro parisien</strong>, entre <strong>Louise Michel</strong> (1 station) et <strong>Pereire</strong> (1 station). Bus 84, 92, 93, 165, PC1 en correspondance.",
            "Ouverte le <strong>23 mai 1911</strong> comme <strong>terminus ouest de la ligne 3</strong>. Elle conserve ce statut pendant <strong>26 ans</strong>, jusqu'au <strong>prolongement vers Pont de Levallois</strong> le <strong>24 septembre 1937</strong>.",
            "À proximité : le <strong>Palais des Congrès de Paris</strong> (porte Maillot, 1974), le <strong>parc Clichy-Batignolles - Martin-Luther-King</strong> (10 ha, 2007-2014), la <strong>nouvelle Cité judiciaire de Paris</strong> (2018, Renzo Piano). Quartier en pleine transformation depuis 2010."
        ],
        "hist_title": "1911-1937 : terminus ouest, puis prolongement Levallois",
        "hist": [
            "La station Porte de Champerret est <strong>inaugurée le 23 mai 1911</strong> avec le prolongement <strong>Villiers ↔ Porte de Champerret</strong> de la ligne 3, alors <strong>terminus ouest</strong>.",
            "Elle conserve ce statut de <strong>terminus pendant 26 ans</strong>, jusqu'au <strong>24 septembre 1937</strong>, date à laquelle la ligne 3 est <strong>prolongée vers Pont de Levallois</strong> (3 nouvelles stations : Louise Michel, Anatole France, Pont de Levallois - Bécon).",
            "Le nom <strong>Champerret</strong> rappelle l'ancien <strong>château de Champerret</strong>, propriété disparue à la fin du XIXe siècle. La <strong>place Stuart Merrill</strong> rend hommage à <strong>Stuart Merrill</strong> (1863-1915), <strong>poète symboliste américano-français</strong>. Le quartier est <strong>aujourd'hui en pleine transformation</strong> avec le projet <strong>Clichy-Batignolles</strong> (parc Martin-Luther-King, Cité judiciaire de Renzo Piano)."
        ],
        "faq": [
            ("Quelle ligne dessert Porte de Champerret ?", "Uniquement la <strong>M3</strong>. Bus 84, 92, 93, 165, PC1."),
            ("Quand a-t-elle ouvert ?", "Le <strong>23 mai 1911</strong> (comme terminus ouest jusqu'en 1937)."),
            ("Pour le Palais des Congrès ?", "<strong>~10 min à pied</strong> via le boulevard Pereire."),
            ("Pour le parc Martin-Luther-King ?", "<strong>~12 min à pied</strong> via la rue Cardinet, ou bus 31."),
            ("Pour la Cité judiciaire ?", "<strong>~10 min à pied</strong> ou tramway T3b."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Parc Martin-Luther-King</strong> (10 ha) à 12 min à pied : grand parc paysager du nouveau Clichy-Batignolles.",
            "<strong>Cité judiciaire de Paris</strong> (Renzo Piano, 2018) à 10 min.",
            "<strong>Palais des Congrès</strong> (porte Maillot) à 10 min à pied.",
            "Quartier en <strong>pleine transformation</strong> (Clichy-Batignolles).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🌳", "Parc Martin-Luther-King, Clichy-Batignolles", "Le <strong>parc Clichy-Batignolles - Martin-Luther-King</strong>, à 12 min à pied de Porte de Champerret, est un <strong>parc paysager de 10 hectares</strong> créé entre <strong>2007 et 2014</strong> sur d'anciens terrains ferroviaires. Œuvre du paysagiste <strong>Jacqueline Osty</strong>. <strong>Inauguré en 2014</strong> par Anne Hidalgo, il rend hommage à <strong>Martin Luther King</strong> (1929-1968), <strong>pasteur baptiste américain</strong> et figure majeure du <strong>mouvement des droits civiques</strong>. <strong>Prix Nobel de la paix 1964</strong>."),
            ("⚖️", "Cité judiciaire par Renzo Piano (2018)", "La <strong>nouvelle Cité judiciaire de Paris</strong>, dans le quartier Clichy-Batignolles, est inaugurée le <strong>16 avril 2018</strong>. Œuvre de l'<strong>architecte italien Renzo Piano</strong> (Pritzker 1998). <strong>Tour de 160 mètres</strong> et <strong>40 étages</strong> — l'un des plus hauts gratte-ciel parisiens. Regroupe le <strong>Tribunal de grande instance</strong>, le <strong>Tribunal d'instance</strong> et la <strong>police judiciaire</strong>. Quitte définitivement le <strong>Palais de Justice de l'île de la Cité</strong>.")
        ],
        "itin": [
            ("Palais des Congrès", "porte-maillot", "M3 ou à pied", "À pied (10 min) ou M3 + M1", 10),
            ("Parc Martin-Luther-King", "porte-de-champerret", "à pied", "Rue Cardinet (12 min)", 12),
            ("Cité judiciaire", "porte-de-clichy", "T3b ou à pied", "Tramway T3b ou à pied", 10),
            ("Saint-Lazare", "saint-lazare", "M3", "M3 directe (5 stations)", 12),
            ("Opéra", "opera", "M3", "M3 directe (7 stations)", 17),
            ("La Défense", "la-defense", "M3 + M1 ou M3 + RER A", "Via Étoile + M1", 16)
        ]
    },
    "pereire": {
        "addr": "Boulevard Pereire, 75017 Paris", "arr": "17e arrondissement (Paris)",
        "seo": "Station Pereire (M3) boulevard Pereire dans le 17e. Hommage aux frères Pereire, banquiers et pionniers du chemin de fer Paris-Saint-Germain (1837).",
        "tagline": "M3 — frères Pereire (banque, chemin de fer 1837)",
        "hero_desc": "Station <strong>Pereire</strong> (officiellement <strong>Péreire Levallois</strong> sur RER C tout proche) sur le <strong>boulevard Pereire</strong> dans le <strong>17e arrondissement</strong>. Desservie par la <strong>M3</strong>, ouverte le <strong>23 mai 1911</strong>. Nommée d'après les <strong>frères Pereire</strong>, banquiers et <strong>pionniers du chemin de fer en France</strong> (<strong>ligne Paris ↔ Saint-Germain, 1837</strong>).",
        "intros": [
            "La station <strong>Pereire</strong> est implantée sur le <strong>boulevard Pereire</strong> dans le <strong>17e arrondissement</strong>. Elle est desservie par la <strong>ligne 3 du métro parisien</strong>, entre <strong>Porte de Champerret</strong> (1 station) et <strong>Wagram</strong> (1 station). À courte distance de la <strong>gare Pereire-Levallois</strong> (RER C). Bus 53, 92, 93, PC1 en correspondance.",
            "Ouverte le <strong>23 mai 1911</strong> avec le prolongement <strong>Villiers ↔ Porte de Champerret</strong> de la ligne 3.",
            "Le nom <strong>Pereire</strong> rend hommage aux <strong>frères Pereire</strong> : <strong>Jacob Émile Pereire</strong> (1800-1875) et <strong>Isaac Pereire</strong> (1806-1880), <strong>banquiers et industriels saint-simoniens</strong>. Pionniers du <strong>chemin de fer en France</strong> (<strong>ligne Paris ↔ Saint-Germain</strong>, première ligne française de voyageurs, <strong>1837</strong>). Fondateurs du <strong>Crédit Mobilier</strong> (1852)."
        ],
        "hist_title": "1911 : prolongement et hommage aux frères Pereire",
        "hist": [
            "La station Pereire est <strong>inaugurée le 23 mai 1911</strong> avec le prolongement <strong>Villiers ↔ Porte de Champerret</strong> de la ligne 3.",
            "Le nom <strong>Pereire</strong> rend hommage aux <strong>frères Pereire</strong> : <strong>Jacob Émile Pereire</strong> (<strong>1800-1875</strong>) et <strong>Isaac Pereire</strong> (<strong>1806-1880</strong>), <strong>banquiers et industriels français</strong> d'origine portugaise. <strong>Saint-simoniens</strong>, ils investirent dans les nouvelles industries du Second Empire.",
            "Ils créent et financent la <strong>première ligne de chemin de fer de voyageurs en France</strong> : la <strong>ligne Paris ↔ Saint-Germain</strong> (aujourd'hui RER A), inaugurée le <strong>26 août 1837</strong>. Fondateurs du <strong>Crédit Mobilier</strong> (<strong>1852</strong>), première grande banque d'affaires française. Ruinés par la faillite du Crédit Mobilier en <strong>1867</strong>. Le <strong>boulevard Pereire</strong>, axe rectiligne de 4 km, fut tracé sur leur ancien projet d'<strong>« avenue de Saint-Germain »</strong> qui devait relier Paris au chemin de fer."
        ],
        "faq": [
            ("Quelle ligne dessert Pereire ?", "<strong>M3</strong> métro. À courte distance de la <strong>gare Pereire-Levallois</strong> (RER C). Bus 53, 92, 93, PC1."),
            ("Qui sont les frères Pereire ?", "<strong>Jacob Émile Pereire</strong> (1800-1875) et <strong>Isaac Pereire</strong> (1806-1880), <strong>banquiers et industriels saint-simoniens</strong>. Créateurs du chemin de fer <strong>Paris ↔ Saint-Germain</strong> (1837) — première ligne de voyageurs française."),
            ("Quand a-t-elle ouvert ?", "Le <strong>23 mai 1911</strong>."),
            ("Pour Wagram (salle de concerts) ?", "<strong>M3 directe</strong> (1 station)."),
            ("Pour Pereire-Levallois RER C ?", "<strong>~5 min à pied</strong> via boulevard Pereire."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Boulevard Pereire</strong> (4 km) : axe rectiligne du 17e, ancien projet d'avenue ferroviaire.",
            "<strong>RER C Pereire-Levallois</strong> à 5 min à pied.",
            "Pour <strong>Wagram</strong> et la <strong>salle Wagram</strong> : <strong>M3 directe</strong> (1 station).",
            "Pour <strong>Charles de Gaulle - Étoile</strong> : <strong>M3 + M1</strong> via Wagram.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🚂", "Frères Pereire, pionniers du chemin de fer", "<strong>Jacob Émile</strong> (1800-1875) et <strong>Isaac Pereire</strong> (1806-1880), <strong>banquiers saint-simoniens</strong> d'origine portugaise. <strong>Pionniers du chemin de fer français</strong>. Ils créent la <strong>première ligne de chemin de fer pour voyageurs en France</strong> (Paris ↔ Saint-Germain, <strong>26 août 1837</strong>, aujourd'hui RER A) puis la ligne Paris ↔ Versailles. Fondateurs du <strong>Crédit Mobilier</strong> (1852), <strong>première grande banque d'affaires</strong>. <strong>Ruinés par la faillite</strong> du Crédit Mobilier en 1867."),
            ("🏛️", "Saint-simonisme et capitalisme", "Les frères Pereire étaient des <strong>disciples de Saint-Simon</strong> (1760-1825), philosophe utopiste qui prônait <strong>l'industrialisation</strong> comme moteur du progrès social. Cette idéologie influença fortement les <strong>élites du Second Empire</strong> et conduisit à des <strong>investissements massifs</strong> dans le chemin de fer, l'industrie, les banques. Le <strong>boulevard Pereire</strong> (4 km) fut tracé sur leur projet d'<strong>« avenue de Saint-Germain »</strong>.")
        ],
        "itin": [
            ("Wagram (salle Wagram)", "wagram", "M3", "M3 directe (1 station)", 2),
            ("Charles de Gaulle - Étoile", "charles-de-gaulle-etoile", "M3 + M1", "M3 → Wagram + M1", 7),
            ("Champs-Élysées", "george-v", "M3 + M1", "M3 → Wagram + M1", 9),
            ("Saint-Lazare", "saint-lazare", "M3", "M3 directe (6 stations)", 14),
            ("Opéra", "opera", "M3", "M3 directe (8 stations)", 19),
            ("Porte de Champerret", "porte-de-champerret", "M3", "M3 directe (1 station)", 2)
        ]
    },
    "wagram": {
        "addr": "Avenue de Wagram, 75017 Paris", "arr": "17e arrondissement (Paris)",
        "seo": "Station Wagram (M3) avenue de Wagram dans le 17e. Bataille de Wagram (1809) victoire de Napoléon en Autriche. Salle Wagram (concerts).",
        "tagline": "M3 — bataille de Wagram (Napoléon, 1809), salle Wagram",
        "hero_desc": "Station <strong>Wagram</strong> sur l'<strong>avenue de Wagram</strong> dans le <strong>17e arrondissement</strong>. Desservie par la <strong>M3</strong>, ouverte le <strong>23 mai 1911</strong>. Nommée en hommage à la <strong>bataille de Wagram</strong> (<strong>5-6 juillet 1809</strong>), <strong>victoire décisive de Napoléon</strong> sur l'Autriche. À proximité de la <strong>salle Wagram</strong>, salle de concerts historique.",
        "intros": [
            "La station <strong>Wagram</strong> est implantée sur l'<strong>avenue de Wagram</strong> dans le <strong>17e arrondissement</strong>. Elle est desservie par la <strong>ligne 3 du métro parisien</strong>, entre <strong>Pereire</strong> (1 station) et <strong>Malesherbes</strong> (1 station). Bus 30, 31, 92 en correspondance.",
            "Ouverte le <strong>23 mai 1911</strong> avec le prolongement <strong>Villiers ↔ Porte de Champerret</strong> de la ligne 3.",
            "Le nom <strong>Wagram</strong> rend hommage à la <strong>bataille de Wagram</strong> (<strong>5-6 juillet 1809</strong>), <strong>victoire décisive de Napoléon Ier</strong> sur les Autrichiens lors de la <strong>guerre de la Cinquième Coalition</strong>. Plus de <strong>300 000 hommes</strong> mobilisés des deux côtés. À proximité : la <strong>salle Wagram</strong> (salle de concerts mythique fondée en 1812)."
        ],
        "hist_title": "1911 : avenue de Wagram et victoire napoléonienne",
        "hist": [
            "La station Wagram est <strong>inaugurée le 23 mai 1911</strong> avec le prolongement <strong>Villiers ↔ Porte de Champerret</strong> de la ligne 3.",
            "Le nom <strong>Wagram</strong> commémore la <strong>bataille de Wagram</strong> (<strong>5-6 juillet 1809</strong>), <strong>victoire décisive de Napoléon Ier</strong> sur l'<strong>archiduc Charles d'Autriche</strong>. Bataille de la <strong>guerre de la Cinquième Coalition</strong> (Cinquième anti-française), opposant la France à l'Autriche. Plus de <strong>300 000 hommes</strong> mobilisés, <strong>50 000 morts</strong> environ. La victoire conduit à la <strong>paix de Schönbrunn</strong> (14 octobre 1809).",
            "La <strong>salle Wagram</strong>, à proximité de la station (39 avenue de Wagram), est une <strong>salle de concerts historique</strong>. Fondée en <strong>1812</strong>, elle accueille initialement des <strong>bals</strong> et <strong>banquets</strong>. Devient au <strong>XXe siècle</strong> une grande salle de <strong>concerts</strong>, de <strong>conférences politiques</strong>, de <strong>tournages de cinéma</strong> (Jean Renoir, Jean Cocteau). Encore active aujourd'hui."
        ],
        "faq": [
            ("Quelle ligne dessert Wagram ?", "Uniquement la <strong>M3</strong>. Bus 30, 31, 92."),
            ("Qu'est-ce que la bataille de Wagram ?", "<strong>Victoire de Napoléon</strong> sur l'Autriche les <strong>5-6 juillet 1809</strong>. <strong>300 000 hommes</strong> mobilisés. Conduit à la <strong>paix de Schönbrunn</strong> (14 octobre 1809)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>23 mai 1911</strong>."),
            ("Pour la salle Wagram ?", "<strong>~5 min à pied</strong> via l'avenue de Wagram (39 avenue de Wagram)."),
            ("Pour Charles de Gaulle - Étoile ?", "<strong>M3 + M1</strong> via Étoile (~5 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Salle Wagram</strong> à 5 min à pied : salle de concerts historique (1812).",
            "Pour <strong>Charles de Gaulle - Étoile</strong> et l'<strong>Arc de Triomphe</strong> : <strong>M3 + M1</strong> via Étoile.",
            "Pour <strong>Saint-Lazare</strong> : <strong>M3 directe</strong> (5 stations).",
            "<strong>Avenue de Wagram</strong> : axe haussmannien rayonnant depuis l'Étoile.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⚔️", "Bataille de Wagram (5-6 juillet 1809)", "La <strong>bataille de Wagram</strong>, <strong>5-6 juillet 1809</strong>, est une <strong>victoire décisive de Napoléon Ier</strong> sur l'<strong>archiduc Charles d'Autriche</strong>. Opposant la France à l'<strong>Autriche</strong> dans le cadre de la <strong>Cinquième Coalition anti-française</strong>. Plus de <strong>300 000 hommes</strong> mobilisés, <strong>50 000 morts et blessés</strong> environ. Bataille décisive pour Napoléon qui impose la <strong>paix de Schönbrunn</strong> (14 octobre 1809), confisquant des territoires autrichiens et imposant l'<strong>alliance matrimoniale</strong> avec Marie-Louise d'Autriche."),
            ("🎵", "Salle Wagram, lieu mythique parisien", "La <strong>salle Wagram</strong> (39 avenue de Wagram), à 5 min à pied de la station, est une <strong>salle de concerts historique</strong>. Fondée en <strong>1812</strong>, elle accueille des <strong>bals</strong> puis devient au XXe siècle une grande salle de <strong>concerts</strong>, <strong>conférences politiques</strong>, <strong>tournages de cinéma</strong>. <strong>Jean Renoir, Jean Cocteau, Jean-Luc Godard</strong> y tournèrent. Encore active aujourd'hui pour des concerts, événements, congrès.")
        ],
        "itin": [
            ("Salle Wagram", "wagram", "à pied", "Avenue de Wagram (5 min)", 5),
            ("Charles de Gaulle - Étoile", "charles-de-gaulle-etoile", "M3 + M1", "M3 → Villiers + M1 ou à pied", 7),
            ("Arc de Triomphe", "charles-de-gaulle-etoile", "à pied", "Avenue de Wagram (10 min)", 10),
            ("Champs-Élysées", "george-v", "M3 + M1", "Via Étoile + M1", 10),
            ("Saint-Lazare", "saint-lazare", "M3", "M3 directe (5 stations)", 12),
            ("Opéra", "opera", "M3", "M3 directe (7 stations)", 16)
        ]
    },
    "malesherbes": {
        "addr": "Boulevard Malesherbes, 75017 Paris", "arr": "17e arrondissement (Paris)",
        "seo": "Station Malesherbes (M3) boulevard Malesherbes dans le 17e. Nommée d'après Chrétien-Guillaume de Lamoignon de Malesherbes (1721-1794), avocat de Louis XVI.",
        "tagline": "M3 — Malesherbes, avocat de Louis XVI",
        "hero_desc": "Station <strong>Malesherbes</strong> sur le <strong>boulevard Malesherbes</strong> dans le <strong>17e arrondissement</strong>. Desservie par la <strong>M3</strong>, ouverte le <strong>23 mai 1911</strong>. Nommée d'après <strong>Chrétien-Guillaume de Lamoignon de Malesherbes</strong> (<strong>1721-1794</strong>), <strong>avocat de Louis XVI</strong> lors de son procès. Quartier résidentiel chic du <strong>17e</strong>.",
        "intros": [
            "La station <strong>Malesherbes</strong> est implantée sur le <strong>boulevard Malesherbes</strong> dans le <strong>17e arrondissement</strong>. Elle est desservie par la <strong>ligne 3 du métro parisien</strong>, entre <strong>Wagram</strong> (1 station) et <strong>Villiers</strong> (1 station). Bus 30, 84 et 94 en correspondance.",
            "Ouverte le <strong>23 mai 1911</strong> avec le prolongement <strong>Villiers ↔ Porte de Champerret</strong> de la ligne 3.",
            "Le nom <strong>Malesherbes</strong> rend hommage à <strong>Chrétien-Guillaume de Lamoignon de Malesherbes</strong> (<strong>1721-1794</strong>), <strong>magistrat, homme d'État et avocat français</strong>. <strong>Avocat de Louis XVI</strong> lors de son procès devant la Convention (décembre 1792). Lui-même <strong>guillotiné</strong> sous la Terreur (<strong>22 avril 1794</strong>)."
        ],
        "hist_title": "1911 : boulevard et avocat de Louis XVI",
        "hist": [
            "La station Malesherbes est <strong>inaugurée le 23 mai 1911</strong> avec le prolongement <strong>Villiers ↔ Porte de Champerret</strong> de la ligne 3.",
            "Le nom <strong>Malesherbes</strong> commémore <strong>Chrétien-Guillaume de Lamoignon de Malesherbes</strong> (<strong>6 décembre 1721 - 22 avril 1794</strong>), <strong>magistrat, ministre et avocat français</strong>. <strong>Premier président de la Cour des aides</strong> (1750-1775), <strong>ministre de la Maison du Roi</strong> sous Louis XVI (1775-1776, 1787-1788).",
            "<strong>Protecteur des philosophes</strong> et des <strong>Lumières</strong> en tant que <strong>directeur de la Librairie</strong> (censure royale) — il <strong>favorisa la publication de l'Encyclopédie</strong>. En <strong>décembre 1792</strong>, il se porte <strong>volontaire pour défendre Louis XVI</strong> devant la <strong>Convention</strong>. Trop tard pour sauver le roi. <strong>Arrêté en 1793</strong>, il est <strong>guillotiné le 22 avril 1794</strong> avec sa fille, son gendre et son petit-fils."
        ],
        "faq": [
            ("Quelle ligne dessert Malesherbes ?", "Uniquement la <strong>M3</strong>. Bus 30, 84 et 94."),
            ("Qui est Malesherbes ?", "<strong>Chrétien-Guillaume de Lamoignon de Malesherbes</strong> (1721-1794), <strong>magistrat et ministre</strong>. <strong>Avocat volontaire de Louis XVI</strong> à son procès. <strong>Guillotiné</strong> le 22 avril 1794."),
            ("Quand a-t-elle ouvert ?", "Le <strong>23 mai 1911</strong>."),
            ("Pour Villiers (M2+M3 hub) ?", "<strong>M3 directe</strong> (1 station)."),
            ("Pour Saint-Lazare ?", "<strong>M3 directe</strong> (4 stations, ~10 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "Quartier résidentiel chic du <strong>17e arrondissement</strong>.",
            "Pour <strong>Villiers</strong> (hub M2+M3) : <strong>M3 directe</strong> (1 station).",
            "Pour <strong>Saint-Lazare</strong> : <strong>M3 directe</strong> (4 stations).",
            "<strong>Parc Monceau</strong> à 10 min à pied via le boulevard Malesherbes.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⚖️", "Malesherbes, avocat volontaire de Louis XVI", "<strong>Chrétien-Guillaume de Lamoignon de Malesherbes</strong> (1721-1794), <strong>magistrat éclairé et ministre</strong>. Comme <strong>directeur de la Librairie</strong> (censure royale), il <strong>protégea l'Encyclopédie</strong> de Diderot et d'Alembert et <strong>favorisa la diffusion des Lumières</strong>. En <strong>décembre 1792</strong>, à 71 ans, il se porte <strong>volontaire pour défendre Louis XVI</strong> devant la <strong>Convention nationale</strong>. Sa <strong>défense courageuse</strong> ne peut sauver le roi, exécuté le 21 janvier 1793. <strong>Malesherbes lui-même arrêté</strong>, il est <strong>guillotiné le 22 avril 1794</strong> avec sa fille, son gendre et son petit-fils."),
            ("📚", "Protecteur des Lumières et de l'Encyclopédie", "Comme <strong>directeur de la Librairie</strong> (censure royale, 1750-1763), <strong>Malesherbes</strong> a joué un <strong>rôle essentiel dans la diffusion des Lumières</strong> en France. Il a <strong>protégé l'Encyclopédie</strong> de Diderot et d'Alembert contre les interdictions répétées (1751-1772), <strong>caché les manuscrits</strong> chez lui en cas de saisie. Ami de <strong>Jean-Jacques Rousseau</strong>, de <strong>Voltaire</strong>, des <strong>physiocrates</strong>. Considéré comme un des <strong>artisans intellectuels de la Révolution</strong>.")
        ],
        "itin": [
            ("Villiers (hub M2+M3)", "villiers", "M3", "M3 directe (1 station)", 2),
            ("Parc Monceau", "monceau", "M2", "M3 → Villiers + M2", 5),
            ("Saint-Lazare", "saint-lazare", "M3", "M3 directe (4 stations)", 10),
            ("Opéra", "opera", "M3", "M3 directe (6 stations)", 14),
            ("Charles de Gaulle - Étoile", "charles-de-gaulle-etoile", "M3 + M2", "M3 → Villiers + M2", 9),
            ("République", "republique", "M3", "M3 directe (10 stations)", 22)
        ]
    },
    "europe": {
        "addr": "Place de l'Europe, 75008 Paris", "arr": "8e arrondissement (Paris)",
        "seo": "Station Europe (M3) place de l'Europe dans le 8e. Quartier de l'Europe (rues nommées capitales européennes), passerelle au-dessus voies Saint-Lazare.",
        "tagline": "M3 — place de l'Europe, passerelle Saint-Lazare",
        "hero_desc": "Station <strong>Europe</strong> sur la <strong>place de l'Europe</strong> dans le <strong>8e arrondissement</strong>. Desservie par la <strong>M3</strong>, ouverte le <strong>19 octobre 1904</strong>. Située sur la <strong>passerelle</strong> de la place de l'Europe, qui enjambe les <strong>voies ferrées de la gare Saint-Lazare</strong>. Cœur du <strong>quartier de l'Europe</strong>, rues nommées d'après les capitales européennes.",
        "intros": [
            "La station <strong>Europe</strong> est implantée sur la <strong>place de l'Europe</strong> dans le <strong>8e arrondissement</strong>. Elle est desservie par la <strong>ligne 3 du métro parisien</strong>, entre <strong>Villiers</strong> (1 station) et <strong>Saint-Lazare</strong> (1 station). Bus 20, 24, 27, 80, 95 en correspondance.",
            "Ouverte le <strong>19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong> de la ligne 3.",
            "La <strong>place de l'Europe</strong>, où la station est implantée, est célèbre pour sa <strong>passerelle</strong> qui <strong>enjambe les voies ferrées</strong> de la <strong>gare Saint-Lazare</strong>. Au cœur du <strong>quartier de l'Europe</strong>, où toutes les rues portent les noms de <strong>capitales européennes</strong> (Rome, Madrid, Berlin/Liège, Vienne, Saint-Pétersbourg, Londres, Constantinople)."
        ],
        "hist_title": "1904 : passerelle et quartier de l'Europe",
        "hist": [
            "La station Europe est <strong>inaugurée le 19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong> de la <strong>ligne 3</strong>.",
            "La <strong>place de l'Europe</strong> est aménagée à partir de <strong>1855</strong> sous le <strong>Second Empire</strong>. Sa célèbre <strong>passerelle métallique</strong> enjambe les <strong>voies ferrées de la gare Saint-Lazare</strong> sur <strong>180 mètres</strong>, formant une étoile à 6 branches. Symbole de la <strong>modernité industrielle</strong> du XIXe siècle, elle a inspiré de nombreux peintres impressionnistes.",
            "Le <strong>quartier de l'Europe</strong>, qui s'étend autour de la place, est un <strong>secteur typique du Second Empire</strong>, où toutes les rues portent les noms de <strong>capitales européennes</strong> : <strong>rue de Rome</strong>, <strong>rue de Madrid</strong>, <strong>rue de Berlin</strong> (renommée <strong>rue de Liège</strong> en <strong>1914</strong> après la Première Guerre mondiale), <strong>rue de Vienne</strong>, <strong>rue de Saint-Pétersbourg</strong>, <strong>rue de Londres</strong>, <strong>rue de Constantinople</strong>. Tracé par Haussmann."
        ],
        "faq": [
            ("Quelle ligne dessert Europe ?", "Uniquement la <strong>M3</strong>. Bus 20, 24, 27, 80, 95."),
            ("Quand a-t-elle ouvert ?", "Le <strong>19 octobre 1904</strong>."),
            ("Qu'est-ce que la place de l'Europe ?", "Une <strong>place du 8e arrondissement</strong> dont la célèbre <strong>passerelle métallique</strong> enjambe les voies ferrées de la <strong>gare Saint-Lazare</strong>. Aménagée à partir de 1855."),
            ("Pourquoi quartier de l'Europe ?", "Toutes les rues portent les <strong>noms de capitales européennes</strong> : Rome, Madrid, Berlin/Liège, Vienne, Saint-Pétersbourg, Londres, Constantinople."),
            ("Pour Saint-Lazare ?", "<strong>M3 directe</strong> (1 station, ~2 min) ou ~5 min à pied."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Passerelle de l'Europe</strong> sur les voies ferrées Saint-Lazare : vue iconique.",
            "<strong>Gare Saint-Lazare</strong> à 5 min à pied.",
            "<strong>Quartier de l'Europe</strong> : rues nommées d'après les capitales.",
            "Pour <strong>Galeries Lafayette / Printemps</strong> (Haussmann) : <strong>M3 directe</strong> vers Havre-Caumartin.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🌉", "Passerelle de l'Europe et impressionnistes", "La <strong>passerelle métallique de la place de l'Europe</strong>, qui enjambe les voies de la gare Saint-Lazare sur <strong>180 mètres</strong>, fut un <strong>symbole de la modernité industrielle</strong> du XIXe siècle. Elle inspira de nombreux <strong>peintres impressionnistes</strong> : <strong>Édouard Manet</strong> (<em>Le Chemin de fer</em>, 1872-1873), <strong>Claude Monet</strong> (série <em>La Gare Saint-Lazare</em>, 1877), <strong>Gustave Caillebotte</strong> (<em>Le Pont de l'Europe</em>, 1876). La modernité métallique fascinait les peintres."),
            ("🇪🇺", "Quartier de l'Europe, urbanisme du Second Empire", "Le <strong>quartier de l'Europe</strong>, aménagé par <strong>Haussmann</strong> sous le <strong>Second Empire</strong>, est un quartier typique de l'<strong>urbanisme parisien du XIXe siècle</strong>. Toutes les rues portent les noms de <strong>capitales européennes</strong> : Rome, Madrid, Berlin (renommée Liège en 1914), Vienne, Saint-Pétersbourg, Londres, Constantinople. Cet <strong>hommage à l'Europe</strong> traduisait l'optimisme cosmopolite du Second Empire et la centralité de la <strong>gare Saint-Lazare</strong> dans le réseau international (Calais, Londres, Bruxelles, Berlin).")
        ],
        "itin": [
            ("Saint-Lazare (hub majeur)", "saint-lazare", "M3", "M3 directe (1 station)", 2),
            ("Galeries Lafayette / Printemps", "havre-caumartin", "M3", "M3 directe (2 stations)", 4),
            ("Opéra Garnier", "opera", "M3", "M3 directe (3 stations)", 7),
            ("Villiers (parc Monceau)", "villiers", "M3", "M3 directe (1 station)", 2),
            ("Charles de Gaulle - Étoile", "charles-de-gaulle-etoile", "M3 + M2", "M3 → Villiers + M2", 8),
            ("République", "republique", "M3", "M3 directe (9 stations)", 18)
        ]
    },
    "havre-caumartin": {
        "addr": "Boulevard Haussmann, 75009 Paris", "arr": "9e arrondissement (Paris)",
        "seo": "Station Havre - Caumartin (M3+M9) à l'intersection des rues du Havre et de Caumartin. Hub Saint-Lazare. Galeries Lafayette et Printemps à proximité.",
        "tagline": "M3 + M9 — Galeries Lafayette, Printemps, Saint-Lazare",
        "hero_desc": "Station <strong>Havre - Caumartin</strong>, hub <strong>M3 + M9</strong>, à l'intersection des <strong>rues du Havre et de Caumartin</strong> dans le <strong>9e arrondissement</strong>. À courte distance de la <strong>gare Saint-Lazare</strong>, des <strong>Galeries Lafayette</strong> et du <strong>Printemps Haussmann</strong>. Quais <strong>M3</strong> ouverts en <strong>1904</strong>, quais <strong>M9</strong> en <strong>1923</strong>.",
        "intros": [
            "La station <strong>Havre - Caumartin</strong> est implantée à l'intersection des <strong>rues du Havre et de Caumartin</strong>, sur le <strong>boulevard Haussmann</strong>, dans le <strong>9e arrondissement</strong>. Elle est desservie par les <strong>lignes 3 et 9</strong> du métro parisien, formant un <strong>hub majeur</strong>. À <strong>5 min à pied de la gare Saint-Lazare</strong>, des <strong>Galeries Lafayette</strong> et du <strong>Printemps Haussmann</strong>. Bus 20, 21, 22, 26, 27, 29, 32, 43, 52, 53, 66, 68, 80, 81, 84, 94, 95.",
            "Quais <strong>ligne 3</strong> ouverts le <strong>19 octobre 1904</strong> (tronçon Père Lachaise ↔ Villiers), quais <strong>ligne 9</strong> ouverts le <strong>27 mai 1923</strong> (prolongement Trocadéro ↔ Saint-Augustin).",
            "Le nom <strong>Havre - Caumartin</strong> combine les noms de deux rues. La <strong>rue du Havre</strong> rappelle la ville du <strong>Havre</strong> (Seine-Maritime), reliée à Paris par train depuis Saint-Lazare en <strong>1847</strong>. La <strong>rue de Caumartin</strong> rend hommage à <strong>Antoine Le Fèvre de Caumartin</strong> (1725-1803), <strong>prévôt des marchands de Paris</strong> sous Louis XV."
        ],
        "hist_title": "1904-1923 : hub M3/M9, Haussmann et grands magasins",
        "hist": [
            "Les quais <strong>ligne 3</strong> sont <strong>inaugurés le 19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong>. Les quais <strong>ligne 9</strong> ouvrent le <strong>27 mai 1923</strong> avec le prolongement <strong>Trocadéro ↔ Saint-Augustin</strong> de la ligne 9.",
            "Le quartier est marqué par les <strong>grands magasins du boulevard Haussmann</strong> : le <strong>Printemps Haussmann</strong> (fondé en <strong>1865</strong> par Jules Jaluzot, façade Art Nouveau d'<strong>Henri Sauvage</strong>) et les <strong>Galeries Lafayette Haussmann</strong> (fondées en <strong>1893</strong> par Théophile Bader, célèbre <strong>coupole néo-byzantine</strong> de 33 m, 1912).",
            "La <strong>rue du Havre</strong> mène directement à la <strong>gare Saint-Lazare</strong> (5 min à pied), <strong>3e gare la plus fréquentée d'Europe</strong> (~100 millions de voyageurs/an). La gare a été reliée au <strong>Havre</strong> dès <strong>1847</strong>, point de départ historique des paquebots transatlantiques."
        ],
        "faq": [
            ("Quelles lignes desservent Havre - Caumartin ?", "<strong>M3</strong> (1904) et <strong>M9</strong> (1923). Hub majeur du 9e."),
            ("Pour les Galeries Lafayette ?", "<strong>~3 min à pied</strong> via le boulevard Haussmann."),
            ("Pour le Printemps Haussmann ?", "<strong>~3 min à pied</strong> via le boulevard Haussmann."),
            ("Pour la gare Saint-Lazare ?", "<strong>~5 min à pied</strong> via la rue du Havre."),
            ("Quand a-t-elle ouvert ?", "Quais M3 : <strong>19 octobre 1904</strong>. Quais M9 : <strong>27 mai 1923</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Galeries Lafayette Haussmann</strong> à 3 min : célèbre <strong>coupole néo-byzantine de 1912</strong>.",
            "<strong>Printemps Haussmann</strong> à 3 min : grand magasin fondé en 1865.",
            "<strong>Gare Saint-Lazare</strong> à 5 min à pied (Transilien J/L, RER, métro).",
            "<strong>Opéra Garnier</strong> à 5 min à pied.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🛍️", "Galeries Lafayette Haussmann, coupole 1912", "Les <strong>Galeries Lafayette Haussmann</strong>, à 3 min à pied, sont l'un des <strong>plus célèbres grands magasins parisiens</strong>. Fondées en <strong>1893</strong> par <strong>Théophile Bader</strong>. Leur <strong>célèbre coupole néo-byzantine</strong>, dessinée par <strong>Ferdinand Chanut</strong>, est inaugurée en <strong>1912</strong>. <strong>33 mètres de haut</strong>, vitraux de <strong>Jacques Gruber</strong>. Classée <strong>monument historique en 1975</strong>. Le grand magasin attire chaque année des <strong>millions de visiteurs</strong>."),
            ("🛍️", "Printemps Haussmann, fondé en 1865", "Le <strong>Printemps Haussmann</strong>, à 3 min à pied, est l'autre grand magasin emblématique du boulevard Haussmann. Fondé en <strong>1865</strong> par <strong>Jules Jaluzot</strong>. Sa <strong>façade Art Nouveau</strong> est l'œuvre de l'architecte <strong>Henri Sauvage</strong> (1907). Reconnaissable à ses <strong>coupoles vitrées</strong> et son <strong>style Belle Époque</strong>. <strong>Inscrit aux monuments historiques en 1975</strong>.")
        ],
        "itin": [
            ("Galeries Lafayette", "havre-caumartin", "à pied", "Boulevard Haussmann (3 min)", 3),
            ("Printemps Haussmann", "havre-caumartin", "à pied", "Boulevard Haussmann (3 min)", 3),
            ("Gare Saint-Lazare", "saint-lazare", "à pied", "Rue du Havre (5 min)", 5),
            ("Opéra Garnier", "opera", "M3", "M3 directe (1 station) ou 5 min à pied", 4),
            ("Concorde", "concorde", "M9", "M9 directe (3 stations)", 7),
            ("République", "republique", "M3", "M3 directe (7 stations)", 14)
        ]
    },
    "quatre-septembre": {
        "addr": "Rue du Quatre-Septembre, 75002 Paris", "arr": "2e arrondissement (Paris)",
        "seo": "Station Quatre-Septembre (M3) rue du Quatre-Septembre dans le 2e. Date de la proclamation de la IIIe République (4 septembre 1870). Proche siège Le Figaro.",
        "tagline": "M3 — 4 septembre 1870, proclamation IIIe République",
        "hero_desc": "Station <strong>Quatre-Septembre</strong> sur la <strong>rue du Quatre-Septembre</strong> dans le <strong>2e arrondissement</strong>. Desservie par la <strong>M3</strong>, ouverte le <strong>19 octobre 1904</strong>. Nommée d'après la <strong>date du 4 septembre 1870</strong>, jour de la <strong>proclamation de la IIIe République</strong> à l'Hôtel de Ville, après la <strong>défaite de Sedan</strong> face à la Prusse.",
        "intros": [
            "La station <strong>Quatre-Septembre</strong> est implantée sur la <strong>rue du Quatre-Septembre</strong> dans le <strong>2e arrondissement</strong>. Elle est desservie par la <strong>ligne 3 du métro parisien</strong>, entre <strong>Opéra</strong> (1 station) et <strong>Bourse</strong> (1 station). Bus 20, 39 en correspondance.",
            "Ouverte le <strong>19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong> de la ligne 3.",
            "Le nom <strong>Quatre-Septembre</strong> commémore la <strong>date du 4 septembre 1870</strong>, jour de la <strong>proclamation de la Troisième République française</strong> à l'<strong>Hôtel de Ville de Paris</strong>, après la <strong>défaite de Sedan</strong> (1er septembre 1870) face à la Prusse et la <strong>capture de Napoléon III</strong>. À proximité : siège de plusieurs <strong>quotidiens</strong> historiques (<strong>Le Figaro</strong>)."
        ],
        "hist_title": "1904 : rue et proclamation de la République",
        "hist": [
            "La station Quatre-Septembre est <strong>inaugurée le 19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong> de la <strong>ligne 3</strong>.",
            "Le nom <strong>Quatre-Septembre</strong> commémore le <strong>4 septembre 1870</strong>. Ce jour-là, après la <strong>défaite de Sedan</strong> (1er septembre 1870) face à la <strong>Prusse de Bismarck</strong> et la <strong>capture de Napoléon III</strong>, <strong>Léon Gambetta</strong> et les députés républicains proclament la <strong>déchéance de l'Empire</strong> au Corps législatif, puis la <strong>République française</strong> à l'<strong>Hôtel de Ville de Paris</strong>.",
            "C'est la <strong>naissance de la Troisième République</strong>, qui durera <strong>70 ans</strong> (jusqu'à 1940). La <strong>rue du Quatre-Septembre</strong> fut ainsi renommée en <strong>1881</strong> pour célébrer cette date fondatrice. Le quartier accueille historiquement de nombreux <strong>journaux et imprimeries</strong>. Le siège de <strong>Le Figaro</strong> se trouve à proximité."
        ],
        "faq": [
            ("Quelle ligne dessert Quatre-Septembre ?", "Uniquement la <strong>M3</strong>. Bus 20, 39."),
            ("Que commémore le nom ?", "La <strong>proclamation de la IIIe République</strong> le <strong>4 septembre 1870</strong> à l'Hôtel de Ville, après la défaite de Sedan."),
            ("Quand a-t-elle ouvert ?", "Le <strong>19 octobre 1904</strong>."),
            ("Pour Opéra Garnier ?", "<strong>M3 directe</strong> (1 station, ~2 min)."),
            ("Pour la Bourse ?", "<strong>M3 directe</strong> (1 station, ~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Quartier des journaux</strong> historiques (Le Figaro à proximité).",
            "Pour <strong>Opéra Garnier</strong> : <strong>M3 directe</strong> (1 station).",
            "Pour <strong>Palais Brongniart</strong> (Bourse) : <strong>M3 directe</strong> (1 station).",
            "<strong>Avenue de l'Opéra</strong> à 5 min à pied.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🇫🇷", "4 septembre 1870, naissance de la IIIe République", "Le <strong>4 septembre 1870</strong>, après la <strong>défaite de Sedan</strong> (1er septembre 1870) face à la <strong>Prusse de Bismarck</strong> et la <strong>capture de Napoléon III</strong>, les députés républicains proclament la <strong>déchéance de l'Empire</strong>. <strong>Léon Gambetta</strong> et <strong>Jules Favre</strong> proclament la <strong>République française</strong> à l'<strong>Hôtel de Ville de Paris</strong>. C'est la <strong>naissance de la Troisième République</strong>, qui durera <strong>70 ans</strong>, jusqu'à 1940."),
            ("📰", "Quartier historique de la presse parisienne", "Le quartier de Quatre-Septembre, Bourse et Sentier accueille historiquement de nombreuses <strong>imprimeries</strong> et <strong>journaux</strong>. Le siège de <strong>Le Figaro</strong> est à proximité. Au XIXe et XXe siècle, le quartier concentrait <strong>la presse française</strong> (Le Temps, Le Petit Parisien, Le Petit Journal). Aujourd'hui, beaucoup de rédactions ont déménagé mais le quartier conserve ses <strong>imprimeries</strong> et <strong>kiosques historiques</strong>.")
        ],
        "itin": [
            ("Opéra Garnier", "opera", "M3", "M3 directe (1 station)", 2),
            ("Bourse (Palais Brongniart)", "bourse", "M3", "M3 directe (1 station)", 2),
            ("Galeries Lafayette", "havre-caumartin", "M3", "M3 directe (3 stations)", 6),
            ("Sentier", "sentier", "M3", "M3 directe (2 stations)", 4),
            ("Châtelet", "chatelet", "M3 + M14", "M3 → Réaumur + M11 ou via Opéra", 10),
            ("République", "republique", "M3", "M3 directe (6 stations)", 12)
        ]
    },
    "bourse": {
        "addr": "Place de la Bourse, 75002 Paris", "arr": "2e arrondissement (Paris)",
        "seo": "Station Bourse (M3) place de la Bourse dans le 2e. Palais Brongniart, ancienne Bourse de Paris (1826-1987). Bibliothèque nationale Richelieu.",
        "tagline": "M3 — Palais Brongniart (Bourse 1826-1987)",
        "hero_desc": "Station <strong>Bourse</strong> sur la <strong>place de la Bourse</strong> dans le <strong>2e arrondissement</strong>. Desservie par la <strong>M3</strong>, ouverte le <strong>19 octobre 1904</strong>. <strong>Palais Brongniart</strong> face à la sortie : ancien <strong>Palais de la Bourse de Paris</strong> (<strong>1826-1987</strong>), aujourd'hui centre de congrès. <strong>Bibliothèque nationale de France site Richelieu</strong> à proximité.",
        "intros": [
            "La station <strong>Bourse</strong> est implantée sur la <strong>place de la Bourse</strong> dans le <strong>2e arrondissement</strong>. Elle est desservie par la <strong>ligne 3 du métro parisien</strong>, entre <strong>Quatre-Septembre</strong> (1 station) et <strong>Sentier</strong> (1 station). Bus 20, 39, 74 en correspondance.",
            "Ouverte le <strong>19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong> de la ligne 3.",
            "Face à la sortie : le <strong>Palais Brongniart</strong> (anciennement <strong>Palais de la Bourse de Paris</strong>), édifice néo-classique de <strong>Alexandre-Théodore Brongniart</strong> (1808-1826). <strong>Siège de la Bourse de Paris de 1826 à 1987</strong>, aujourd'hui <strong>centre de congrès</strong>. À proximité : la <strong>Bibliothèque nationale de France site Richelieu</strong> (galerie Mazarin, salle Labrouste)."
        ],
        "hist_title": "1904 : Palais Brongniart, ancien temple de la Bourse",
        "hist": [
            "La station Bourse est <strong>inaugurée le 19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong> de la <strong>ligne 3</strong>.",
            "Le <strong>Palais Brongniart</strong>, face à la sortie de la station, est construit de <strong>1808 à 1826</strong> sous Napoléon Ier, puis sous la Restauration. Œuvre de l'architecte <strong>Alexandre-Théodore Brongniart</strong> (<strong>1739-1813</strong>), achevée par <strong>Éloi Labarre</strong> après sa mort. <strong>Style néo-classique</strong> avec <strong>colonnade corinthienne</strong>. <strong>Siège de la Bourse de Paris de 1826 à 1987</strong>.",
            "L'<strong>activité boursière</strong> y prit fin en <strong>1987</strong> avec la <strong>dématérialisation</strong> (informatisation des marchés). Le bâtiment est devenu <strong>centre de congrès</strong> et est <strong>classé monument historique</strong> en <strong>1987</strong>. À proximité, le <strong>quartier de la BnF Richelieu</strong> (galerie Mazarin, salle Labrouste, l'<strong>Hôtel Tubeuf</strong>) abrite les collections historiques de la Bibliothèque nationale."
        ],
        "faq": [
            ("Quelle ligne dessert Bourse ?", "Uniquement la <strong>M3</strong>. Bus 20, 39, 74."),
            ("Qu'est-ce que le Palais Brongniart ?", "L'ancien <strong>Palais de la Bourse de Paris</strong> (1826-1987), édifice néo-classique d'<strong>Alexandre-Théodore Brongniart</strong>. Aujourd'hui <strong>centre de congrès</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>19 octobre 1904</strong>."),
            ("Pour la BnF Richelieu ?", "<strong>~5 min à pied</strong> via la rue du Quatre-Septembre. Galerie Mazarin et salle Labrouste."),
            ("Pour le Sentier ?", "<strong>M3 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Palais Brongniart</strong> face à la sortie : ancien temple boursier, aujourd'hui centre de congrès.",
            "<strong>BnF site Richelieu</strong> à 5 min à pied : galerie Mazarin, salle Labrouste (rouverte en 2017).",
            "Pour <strong>Opéra</strong> : <strong>M3 directe</strong> (2 stations).",
            "Pour <strong>Châtelet</strong> : <strong>M3 + M14</strong> via Réaumur ou Châtelet directe.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Palais Brongniart, temple néo-classique", "Le <strong>Palais Brongniart</strong>, face à la station, est construit de <strong>1808 à 1826</strong> sous Napoléon Ier et la Restauration. Œuvre de l'architecte <strong>Alexandre-Théodore Brongniart</strong> (1739-1813), achevée par Éloi Labarre. <strong>Style néo-classique</strong>, <strong>colonnade corinthienne</strong> rectangulaire. <strong>Siège de la Bourse de Paris de 1826 à 1987</strong>. L'activité y prit fin avec la <strong>dématérialisation</strong> des marchés. <strong>Centre de congrès</strong> depuis 1987. <strong>Classé monument historique</strong> la même année."),
            ("📚", "BnF Richelieu, écrin des trésors français", "La <strong>Bibliothèque nationale de France site Richelieu</strong>, à 5 min à pied, est le <strong>berceau historique</strong> de la BnF. Abrite la <strong>galerie Mazarin</strong> (XVIIe), la <strong>salle Labrouste</strong> (1868, rouverte en <strong>2017</strong> après rénovation) et la <strong>salle Ovale</strong>. <strong>Collections trésors</strong> : manuscrits médiévaux, livres rares, cartes, estampes (Rembrandt), monnaies (Cabinet des Médailles), photographies (Nadar).")
        ],
        "itin": [
            ("Palais Brongniart", "bourse", "à pied", "Sortie directe", 1),
            ("BnF Richelieu", "bourse", "à pied", "Rue du Quatre-Septembre (5 min)", 5),
            ("Opéra Garnier", "opera", "M3", "M3 directe (2 stations)", 4),
            ("Sentier", "sentier", "M3", "M3 directe (1 station)", 2),
            ("Châtelet", "chatelet", "M3 + M14", "M3 → Réaumur + M11 ou via Opéra", 10),
            ("République", "republique", "M3", "M3 directe (5 stations)", 11)
        ]
    },
    "sentier": {
        "addr": "Rue Réaumur, 75002 Paris", "arr": "2e arrondissement (Paris)",
        "seo": "Station Sentier (M3) rue Réaumur dans le 2e. Quartier du Sentier, historique du textile et de la mode parisienne. Berceau de la Silicon Sentier (start-ups).",
        "tagline": "M3 — quartier du Sentier, mode et start-ups",
        "hero_desc": "Station <strong>Sentier</strong> sur la <strong>rue Réaumur</strong> dans le <strong>2e arrondissement</strong>. Desservie par la <strong>M3</strong>, ouverte le <strong>19 octobre 1904</strong>. Cœur du <strong>quartier du Sentier</strong>, <strong>historique du textile et de la mode parisienne</strong> depuis le XIXe siècle. Berceau de la <strong>« Silicon Sentier »</strong> (start-ups tech).",
        "intros": [
            "La station <strong>Sentier</strong> est implantée sur la <strong>rue Réaumur</strong>, au cœur du <strong>quartier du Sentier</strong>, dans le <strong>2e arrondissement</strong>. Elle est desservie par la <strong>ligne 3 du métro parisien</strong>, entre <strong>Bourse</strong> (1 station) et <strong>Réaumur - Sébastopol</strong> (1 station). Bus 20, 29, 74 en correspondance.",
            "Ouverte le <strong>19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong> de la ligne 3.",
            "Le <strong>quartier du Sentier</strong> est historiquement le <strong>cœur du commerce de textile et de la mode parisienne</strong>. Depuis le <strong>XIXe siècle</strong>, il accueille <strong>grossistes</strong>, <strong>ateliers de confection</strong>, <strong>imprimeries</strong>, <strong>boutiques en gros</strong>. Depuis la fin des années 1990, le quartier accueille également de nombreuses <strong>start-ups tech</strong> (« <strong>Silicon Sentier</strong> »)."
        ],
        "hist_title": "1904 : Sentier, du textile à la tech",
        "hist": [
            "La station Sentier est <strong>inaugurée le 19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong> de la <strong>ligne 3</strong>.",
            "Le <strong>quartier du Sentier</strong> est historiquement le <strong>cœur du commerce textile et de la mode</strong> à Paris. Depuis le <strong>XIXe siècle</strong>, il regroupe <strong>grossistes en textile</strong>, <strong>ateliers de confection</strong>, <strong>magasins de tissus</strong>, <strong>imprimeries de mode</strong>. Au <strong>XXe siècle</strong>, important quartier d'<strong>immigration juive</strong> (notamment d'Europe centrale et orientale) puis <strong>tunisienne et marocaine</strong>.",
            "Depuis la fin des années 1990, le quartier connaît une <strong>mutation tech</strong> avec l'arrivée massive de <strong>start-ups</strong> attirées par les <strong>loyers modérés</strong>, la <strong>centralité parisienne</strong> et l'<strong>écosystème dense</strong>. Surnom : <strong>« Silicon Sentier »</strong>. <strong>Le journal Le Point</strong>, <strong>Meetic</strong>, <strong>Vente-Privée</strong> y ont été fondés ou installés. Quartier en pleine <strong>gentrification</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Sentier ?", "Uniquement la <strong>M3</strong>. Bus 20, 29, 74."),
            ("Qu'est-ce que le quartier du Sentier ?", "Cœur historique du <strong>commerce textile et de la mode</strong> parisienne depuis le XIXe siècle. Aujourd'hui aussi « <strong>Silicon Sentier</strong> » (start-ups tech)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>19 octobre 1904</strong>."),
            ("Pour la rue Saint-Denis ?", "<strong>~3 min à pied</strong>."),
            ("Pour le passage du Caire ?", "<strong>~5 min à pied</strong> via la rue Réaumur."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Quartier du Sentier</strong> : <strong>grossistes textile, ateliers confection</strong>.",
            "<strong>Silicon Sentier</strong> : nombreuses <strong>start-ups tech</strong> depuis les années 2000.",
            "<strong>Passage du Caire</strong> (1798) à proximité : plus ancien passage couvert parisien.",
            "Pour <strong>Châtelet - Les Halles</strong> : <strong>M3 → Réaumur + M4</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🧵", "Quartier du Sentier, mode parisienne", "Le <strong>quartier du Sentier</strong>, au cœur du 2e arrondissement, est historiquement le <strong>centre du commerce textile et de la mode</strong> parisienne. Depuis le <strong>XIXe siècle</strong>, on y trouve <strong>grossistes en tissus, prêt-à-porter, ateliers de confection</strong>. Au XXe siècle, important quartier d'<strong>immigration juive d'Europe centrale</strong> (Pologne, Hongrie) puis <strong>nord-africaine</strong> (Tunisie, Maroc). Le quartier vivait au rythme du <strong>« métier »</strong>."),
            ("💻", "Silicon Sentier, hub start-ups 2000s", "À partir de la fin des années 1990, le quartier du Sentier devient le <strong>« Silicon Sentier »</strong>, <strong>hub français des start-ups internet</strong>. Loyers modérés, centralité, écosystème dense attirent les pionniers du web. <strong>Meetic, Vente-Privée, Cdiscount</strong> y ont été fondés ou installés. <strong>Le Sentier</strong> incarne aujourd'hui la <strong>mutation tech</strong> de Paris, avec ses <strong>incubateurs</strong> et <strong>espaces de coworking</strong>.")
        ],
        "itin": [
            ("Passage du Caire", "sentier", "à pied", "Rue Réaumur (5 min)", 5),
            ("Réaumur - Sébastopol", "reaumur-sebastopol", "M3", "M3 directe (1 station)", 2),
            ("Châtelet - Les Halles", "chatelet-les-halles", "M3 + M4", "M3 → Réaumur + M4", 8),
            ("Opéra Garnier", "opera", "M3", "M3 directe (3 stations)", 6),
            ("République", "republique", "M3", "M3 directe (4 stations)", 9),
            ("Marais (Arts et Métiers)", "arts-et-metiers", "M3", "M3 directe (2 stations)", 4)
        ]
    },
    "temple": {
        "addr": "Rue du Temple, 75003 Paris", "arr": "3e arrondissement (Paris)",
        "seo": "Station Temple (M3) rue du Temple dans le 3e (Marais). Square du Temple, ancien quartier de l'ordre des Templiers. Mairie du 3e.",
        "tagline": "M3 — quartier du Temple, ordre des Templiers",
        "hero_desc": "Station <strong>Temple</strong> sur la <strong>rue du Temple</strong> dans le <strong>3e arrondissement</strong> (Marais). Desservie par la <strong>M3</strong>, ouverte le <strong>19 octobre 1904</strong>. Au cœur du <strong>quartier du Temple</strong>, ancien <strong>siège de l'ordre des Templiers</strong> en France (XIIe-XIVe siècles). <strong>Mairie du 3e arrondissement</strong> à proximité.",
        "intros": [
            "La station <strong>Temple</strong> est implantée sur la <strong>rue du Temple</strong> dans le <strong>3e arrondissement</strong> (Marais). Elle est desservie par la <strong>ligne 3 du métro parisien</strong>, entre <strong>Arts et Métiers</strong> (1 station) et <strong>République</strong> (1 station). Bus 75 en correspondance.",
            "Ouverte le <strong>19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong> de la ligne 3.",
            "Le nom <strong>Temple</strong> rappelle l'<strong>ordre des Templiers</strong>, ordre religieux et militaire fondé en <strong>1129</strong>. Le <strong>quartier du Temple</strong> abritait au Moyen Âge la <strong>commanderie du Temple</strong>, siège français de l'ordre. Aujourd'hui : <strong>square du Temple</strong> (1857), <strong>mairie du 3e arrondissement</strong>, <strong>Carreau du Temple</strong> (halle de marché transformée en centre culturel)."
        ],
        "hist_title": "1904 : Temple, mémoire des Templiers",
        "hist": [
            "La station Temple est <strong>inaugurée le 19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong> de la <strong>ligne 3</strong>.",
            "Le nom <strong>Temple</strong> rappelle l'<strong>ordre des Templiers</strong> (<strong>Pauvres Chevaliers du Christ et du Temple de Salomon</strong>), <strong>ordre religieux et militaire chrétien</strong> fondé en <strong>1129</strong> pour protéger les pèlerins en Terre sainte. Le <strong>quartier du Temple</strong> abritait au Moyen Âge la <strong>commanderie du Temple de Paris</strong>, <strong>siège français de l'ordre</strong>. Vaste enclos avec <strong>donjon</strong>, <strong>église ronde</strong>, <strong>résidences</strong>.",
            "L'<strong>ordre est dissous</strong> par Philippe IV le Bel en <strong>1312</strong>. Le grand maître <strong>Jacques de Molay</strong> est <strong>brûlé vif</strong> sur l'<strong>île de la Cité</strong> en <strong>1314</strong>. La <strong>tour du Temple</strong> (donjon des Templiers) sera convertie en <strong>prison royale</strong>. <strong>Louis XVI, Marie-Antoinette et le dauphin</strong> y sont emprisonnés en <strong>1792-1793</strong> avant leur exécution. La <strong>tour est démolie par Napoléon</strong> en 1808. Aujourd'hui : <strong>square du Temple</strong> (1857) et <strong>Carreau du Temple</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Temple ?", "Uniquement la <strong>M3</strong>. Bus 75."),
            ("Qu'est-ce que l'ordre du Temple ?", "<strong>Ordre religieux et militaire chrétien</strong> fondé en <strong>1129</strong>, dissous par <strong>Philippe IV le Bel</strong> en <strong>1312</strong>. Sa <strong>commanderie française</strong> était dans le quartier."),
            ("Quand a-t-elle ouvert ?", "Le <strong>19 octobre 1904</strong>."),
            ("Où ont été emprisonnés Louis XVI et Marie-Antoinette ?", "Dans la <strong>tour du Temple</strong> (donjon des Templiers), <strong>1792-1793</strong>, avant leur exécution. <strong>Démolie par Napoléon</strong> en 1808."),
            ("Pour la mairie du 3e ?", "<strong>~3 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Square du Temple</strong> (1857) à proximité : jardin paisible, mémoire de l'enclos médiéval.",
            "<strong>Carreau du Temple</strong> : ancienne halle de marché transformée en centre culturel.",
            "<strong>Mairie du 3e arrondissement</strong> à 3 min.",
            "Pour <strong>Arts et Métiers</strong> (musée) : <strong>M3 directe</strong> (1 station).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⚔️", "Ordre des Templiers (1129-1312)", "L'<strong>ordre des Templiers</strong>, ou <strong>Pauvres Chevaliers du Christ et du Temple de Salomon</strong>, est un <strong>ordre religieux et militaire chrétien</strong> fondé en <strong>1129</strong> pour protéger les pèlerins en Terre sainte. Très puissant et riche au XIIIe siècle. <strong>Dissous brutalement par Philippe IV le Bel</strong> en <strong>1312</strong> qui convoitait leurs richesses. Le grand maître <strong>Jacques de Molay</strong> est <strong>brûlé vif</strong> à Paris (île de la Cité) le <strong>18 mars 1314</strong>. Sa célèbre malédiction sur Philippe le Bel et le pape entre dans la légende."),
            ("👑", "Tour du Temple, prison de Louis XVI", "La <strong>tour du Temple</strong> (donjon des Templiers, XIIe siècle), devenue <strong>prison royale</strong>, accueille en <strong>1792-1793</strong> les <strong>derniers prisonniers royaux</strong> : <strong>Louis XVI</strong>, <strong>Marie-Antoinette</strong>, <strong>le dauphin Louis XVII</strong> et <strong>Madame Élisabeth</strong>. Louis XVI y reste enfermé du 13 août 1792 au 21 janvier 1793 (exécution). Le petit <strong>Louis XVII</strong> y meurt en captivité (8 juin 1795). La <strong>tour est démolie par Napoléon</strong> en <strong>1808</strong> pour effacer le souvenir.")
        ],
        "itin": [
            ("Square du Temple", "temple", "à pied", "Sortie (1 min)", 1),
            ("Carreau du Temple", "temple", "à pied", "À proximité (3 min)", 3),
            ("Arts et Métiers (musée)", "arts-et-metiers", "M3", "M3 directe (1 station)", 2),
            ("République", "republique", "M3", "M3 directe (1 station)", 2),
            ("Marais (Saint-Paul)", "saint-paul", "M3 + M1 ou à pied", "À pied via rue Vieille-du-Temple (10 min)", 10),
            ("Châtelet", "chatelet", "M3 + M4", "M3 → Réaumur + M4", 8)
        ]
    },
    "parmentier": {
        "addr": "Avenue Parmentier, 75011 Paris", "arr": "11e arrondissement (Paris)",
        "seo": "Station Parmentier (M3) avenue Parmentier dans le 11e. Nommée d'après Antoine Parmentier (1737-1813), promoteur de la pomme de terre en France.",
        "tagline": "M3 — Antoine Parmentier, popularisateur de la pomme de terre",
        "hero_desc": "Station <strong>Parmentier</strong> sur l'<strong>avenue Parmentier</strong> dans le <strong>11e arrondissement</strong>. Desservie par la <strong>M3</strong>, ouverte le <strong>19 octobre 1904</strong>. Nommée d'après <strong>Antoine Augustin Parmentier</strong> (<strong>1737-1813</strong>), <strong>pharmacien militaire et agronome</strong> qui <strong>popularisa la pomme de terre en France</strong>.",
        "intros": [
            "La station <strong>Parmentier</strong> est implantée sur l'<strong>avenue Parmentier</strong> dans le <strong>11e arrondissement</strong>. Elle est desservie par la <strong>ligne 3 du métro parisien</strong>, entre <strong>République</strong> (1 station) et <strong>Rue Saint-Maur</strong> (1 station). Bus 46 et 75 en correspondance.",
            "Ouverte le <strong>19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong> de la ligne 3.",
            "Le nom <strong>Parmentier</strong> rend hommage à <strong>Antoine Augustin Parmentier</strong> (<strong>1737-1813</strong>), <strong>pharmacien militaire, agronome et nutritionniste français</strong>. Il <strong>popularisa la pomme de terre</strong> en France comme aliment de base, malgré la méfiance initiale (on croyait alors que le tubercule était toxique ou cause de la lèpre)."
        ],
        "hist_title": "1904 : Parmentier et la pomme de terre",
        "hist": [
            "La station Parmentier est <strong>inaugurée le 19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong> de la <strong>ligne 3</strong>.",
            "Le nom <strong>Parmentier</strong> commémore <strong>Antoine Augustin Parmentier</strong> (<strong>12 août 1737 - 17 décembre 1813</strong>), <strong>pharmacien militaire, agronome et nutritionniste français</strong>. Né à Montdidier (Somme). Prisonnier de guerre en Prusse pendant la <strong>guerre de Sept Ans</strong> (1756-1763), il y découvrit la <strong>pomme de terre</strong> comme aliment de base.",
            "À son retour en France, il œuvra pour <strong>populariser la pomme de terre</strong> comme <strong>solution à la famine</strong>. Le tubercule était alors méprisé et même <strong>interdit en France</strong> (1748) car suspecté de provoquer la <strong>lèpre</strong>. Parmentier organisa des <strong>banquets prestigieux</strong> où il servit la pomme de terre sous toutes ses formes, présents au roi <strong>Louis XVI</strong> et à la reine. Il fit même <strong>garder ses champs de pommes de terre à Neuilly</strong> par des soldats le jour... et laisser ouverts la nuit pour que les paysans en volent. <strong>Stratagème efficace</strong>. La <strong>levée de l'interdiction</strong> intervient en <strong>1772</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Parmentier ?", "Uniquement la <strong>M3</strong>. Bus 46 et 75."),
            ("Qui est Parmentier ?", "<strong>Antoine Augustin Parmentier</strong> (1737-1813), <strong>pharmacien militaire et agronome</strong> qui a <strong>popularisé la pomme de terre en France</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>19 octobre 1904</strong>."),
            ("Pourquoi populariser la pomme de terre ?", "Le tubercule était <strong>méprisé et interdit en France</strong> (suspecté de provoquer la lèpre). Parmentier organisa des <strong>banquets prestigieux</strong> et fit garder ses champs par des soldats — stratagème pour exciter la curiosité."),
            ("Pour République ?", "<strong>M3 directe</strong> (1 station, ~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "Pour <strong>République</strong> et son hub multilignes : <strong>M3 directe</strong> (1 station).",
            "Quartier <strong>11e résidentiel</strong> et animé.",
            "Pour <strong>Père Lachaise</strong> : <strong>M3 directe</strong> (4 stations).",
            "<strong>Hachis Parmentier</strong> : plat traditionnel français portant son nom.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🥔", "Parmentier, sauveur de la pomme de terre", "<strong>Antoine Augustin Parmentier</strong> (1737-1813), <strong>pharmacien militaire</strong>. Prisonnier en <strong>Prusse</strong> pendant la <strong>guerre de Sept Ans</strong>, il découvre la <strong>pomme de terre</strong>. De retour en France, il <strong>popularise le tubercule</strong> malgré le <strong>scepticisme</strong>. Banquets de prestige avec pomme de terre servie à Louis XVI et Marie-Antoinette (qui porta des fleurs de pomme de terre à son corsage). <strong>Champs gardés à Neuilly</strong> par soldats le jour — laissés sans surveillance la nuit pour que les paysans volent. <strong>Levée de l'interdiction</strong> en 1772. Plat <strong>hachis Parmentier</strong> en son honneur."),
            ("🏛️", "Académie des sciences et postérité", "<strong>Antoine Parmentier</strong> a été <strong>membre de l'Académie des sciences</strong>. Il a écrit de nombreux ouvrages d'<strong>agronomie et nutrition</strong>. Outre la pomme de terre, il a aussi étudié le <strong>maïs</strong>, la <strong>vigne</strong>, la <strong>conservation des grains</strong>. Inhumé au <strong>cimetière du Père Lachaise</strong> (4 stations de M3 depuis Parmentier). Sa <strong>tombe</strong> y est ornée de <strong>plants de pommes de terre</strong> entretenus en permanence par des fidèles.")
        ],
        "itin": [
            ("République", "republique", "M3", "M3 directe (1 station)", 2),
            ("Père Lachaise", "pere-lachaise", "M3", "M3 directe (4 stations)", 9),
            ("Rue Saint-Maur", "saint-maur", "M3", "M3 directe (1 station)", 2),
            ("Opéra Garnier", "opera", "M3", "M3 directe (7 stations)", 15),
            ("Châtelet", "chatelet", "M3 + M11", "M3 → République + M11", 8),
            ("Bastille", "bastille", "M3 + M5", "M3 → République + M5", 10)
        ]
    },
    "saint-maur": {
        "addr": "Rue Saint-Maur, 75011 Paris", "arr": "11e arrondissement (Paris)",
        "seo": "Station Rue Saint-Maur (M3) rue Saint-Maur dans le 11e. Quartier populaire et résidentiel entre République et Père Lachaise.",
        "tagline": "M3 — rue Saint-Maur, 11e populaire",
        "hero_desc": "Station <strong>Rue Saint-Maur</strong> sur la <strong>rue Saint-Maur</strong> dans le <strong>11e arrondissement</strong>. Desservie par la <strong>M3</strong>, ouverte le <strong>19 octobre 1904</strong>. Quartier <strong>populaire et résidentiel</strong> du <strong>11e</strong>, entre <strong>République</strong> et <strong>Père Lachaise</strong>.",
        "intros": [
            "La station <strong>Rue Saint-Maur</strong> est implantée sur la <strong>rue Saint-Maur</strong> dans le <strong>11e arrondissement</strong>. Elle est desservie par la <strong>ligne 3 du métro parisien</strong>, entre <strong>Parmentier</strong> (1 station) et <strong>Père Lachaise</strong> (1 station). Bus 46, 56, 96 en correspondance.",
            "Ouverte le <strong>19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong> de la ligne 3.",
            "La <strong>rue Saint-Maur</strong>, qui donne son nom à la station, est une <strong>longue voie</strong> du <strong>11e arrondissement</strong> (2 km), reliant la <strong>place du Père-Chaillet</strong> au <strong>boulevard de la Villette</strong>. Le nom rappelle l'<strong>ancienne abbaye Saint-Maur-des-Fossés</strong> (Val-de-Marne). Quartier <strong>populaire et animé</strong>, en mutation gentrification depuis les années 2000."
        ],
        "hist_title": "1904 : rue Saint-Maur et 11e populaire",
        "hist": [
            "La station Rue Saint-Maur est <strong>inaugurée le 19 octobre 1904</strong> avec le tronçon initial <strong>Père Lachaise ↔ Villiers</strong> de la <strong>ligne 3</strong>.",
            "La <strong>rue Saint-Maur</strong>, longue de <strong>2 km</strong>, traverse le <strong>11e arrondissement</strong>. Son nom rappelle l'<strong>abbaye Saint-Maur-des-Fossés</strong> (Val-de-Marne), <strong>monastère bénédictin fondé au VIIe siècle</strong>. Au Moyen Âge, la rue (alors <strong>chemin Saint-Maur</strong>) reliait Paris aux territoires de l'abbaye dans l'est parisien.",
            "Le <strong>11e arrondissement</strong> est historiquement un quartier <strong>populaire et ouvrier</strong>, marqué par l'<strong>artisanat</strong> (meubliers du faubourg Saint-Antoine, doreurs, ébénistes). Il abrita également une importante <strong>immigration juive</strong> au XIXe-XXe siècle. Depuis les années 2000, le quartier connaît une <strong>gentrification</strong> avec installation de <strong>bars, restaurants tendance</strong>, <strong>boutiques</strong>. La rue Saint-Maur en particulier est devenue un <strong>haut lieu de la vie nocturne parisienne</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Rue Saint-Maur ?", "Uniquement la <strong>M3</strong>. Bus 46, 56, 96."),
            ("D'où vient le nom Saint-Maur ?", "De l'<strong>abbaye Saint-Maur-des-Fossés</strong> (Val-de-Marne), <strong>monastère bénédictin fondé au VIIe siècle</strong>. La rue, ancien chemin, menait aux territoires de l'abbaye."),
            ("Quand a-t-elle ouvert ?", "Le <strong>19 octobre 1904</strong>."),
            ("Pour Père Lachaise ?", "<strong>M3 directe</strong> (1 station, ~2 min)."),
            ("Pour République ?", "<strong>M3 directe</strong> (2 stations, ~5 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Rue Saint-Maur</strong> : haut lieu de la <strong>vie nocturne parisienne</strong> (bars, restaurants).",
            "Pour <strong>Père Lachaise</strong> : <strong>M3 directe</strong> (1 station).",
            "Pour <strong>République</strong> : <strong>M3 directe</strong> (2 stations).",
            "Quartier <strong>populaire et animé</strong> du 11e en mutation.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🍷", "Rue Saint-Maur, vie nocturne du 11e", "La <strong>rue Saint-Maur</strong> et ses alentours (rue Oberkampf, rue Jean-Pierre Timbaud) forment l'un des <strong>hauts lieux de la vie nocturne parisienne</strong>. <strong>Bars à cocktails, restaurants tendance, lieux de concerts</strong>. Le quartier a connu une <strong>renaissance</strong> à partir des années 1990 avec l'arrivée du <strong>Café Charbon</strong> (1995) et du <strong>Nouveau Casino</strong>. Aujourd'hui, gentrification continue mais le quartier conserve son identité <strong>populaire et alternative</strong>."),
            ("🏛️", "Abbaye Saint-Maur-des-Fossés", "L'<strong>abbaye Saint-Maur-des-Fossés</strong>, qui donne son nom à la rue, est un <strong>monastère bénédictin fondé au VIIe siècle</strong> dans le <strong>Val-de-Marne</strong>. Au Moyen Âge, l'abbaye possédait de vastes territoires à l'est de Paris. La <strong>rue Saint-Maur</strong> était l'<strong>ancien chemin</strong> qui menait à ces terres depuis Paris. L'abbaye fut <strong>détruite à la Révolution</strong>, ne subsistent que quelques vestiges.")
        ],
        "itin": [
            ("Père Lachaise", "pere-lachaise", "M3", "M3 directe (1 station)", 2),
            ("République", "republique", "M3", "M3 directe (2 stations)", 5),
            ("Parmentier", "parmentier", "M3", "M3 directe (1 station)", 2),
            ("Bastille", "bastille", "M3 + M5", "M3 → République + M5", 12),
            ("Châtelet", "chatelet", "M3 + M11", "M3 → République + M11", 10),
            ("Opéra Garnier", "opera", "M3", "M3 directe (8 stations)", 17)
        ]
    },
    "porte-de-bagnolet": {
        "addr": "Place Édouard-Vaillant, 75020 Paris", "arr": "20e arrondissement (Paris)",
        "seo": "Station Porte de Bagnolet (M3) place Édouard-Vaillant. Porte vers Bagnolet (93). Proche centre commercial Bel-Est, gare routière internationale Gallieni.",
        "tagline": "M3 — porte de Bagnolet, Bel-Est",
        "hero_desc": "Station <strong>Porte de Bagnolet</strong> sur la <strong>place Édouard-Vaillant</strong> dans le <strong>20e arrondissement</strong>. Desservie par la <strong>M3</strong>, ouverte le <strong>27 mars 1971</strong>. À proximité du <strong>centre commercial Bel-Est</strong> et de la <strong>gare routière internationale Gallieni</strong>.",
        "intros": [
            "La station <strong>Porte de Bagnolet</strong> est implantée sur la <strong>place Édouard-Vaillant</strong> dans le <strong>20e arrondissement</strong>, à la <strong>limite de Bagnolet</strong> (Seine-Saint-Denis). Elle est desservie par la <strong>ligne 3 du métro parisien</strong>, entre <strong>Gambetta</strong> (1 station) et <strong>Gallieni</strong> (1 station, terminus est). Bus 57, 76, 102, 122, 351.",
            "Ouverte le <strong>27 mars 1971</strong> avec le <strong>prolongement de la M3</strong> de <strong>Gambetta à Gallieni</strong>. Construction tardive liée à la transformation des portes parisiennes.",
            "À proximité immédiate : la <strong>porte de Bagnolet</strong> (entrée vers la commune de <strong>Bagnolet</strong>, 93), le <strong>centre commercial Bel-Est</strong> (1976), la <strong>gare routière internationale Gallieni</strong> (FlixBus, Eurolines, Ouibus) et le <strong>quartier du Bas-Belleville</strong>."
        ],
        "hist_title": "1971 : prolongement M3 vers Gallieni",
        "hist": [
            "La station Porte de Bagnolet est <strong>inaugurée le 27 mars 1971</strong> avec le <strong>prolongement de la ligne 3</strong> de <strong>Gambetta à Gallieni</strong> (2 stations ajoutées). Ce <strong>prolongement tardif</strong> accompagne la <strong>transformation des portes parisiennes</strong> et l'<strong>urbanisation de la première couronne</strong>.",
            "La <strong>porte de Bagnolet</strong> est l'une des <strong>portes historiques de Paris</strong> sur l'enceinte de Thiers (1841-1845). Elle marque l'<strong>entrée vers la commune de Bagnolet</strong> (Seine-Saint-Denis, ~35 000 habitants). Le nom <strong>place Édouard-Vaillant</strong> rend hommage à <strong>Édouard Vaillant</strong> (1840-1915), <strong>communard et socialiste</strong>.",
            "Le quartier est marqué par le <strong>centre commercial Bel-Est</strong> (inauguré en <strong>1976</strong>), l'un des <strong>premiers grands centres commerciaux</strong> de la périphérie parisienne. À proximité immédiate, la <strong>gare routière internationale Gallieni</strong> (parking de la porte de Bagnolet) est le <strong>principal hub parisien pour les bus internationaux</strong> (FlixBus, BlaBlaCar Bus, Eurolines, Ouibus) — départs vers toute l'Europe."
        ],
        "faq": [
            ("Quelle ligne dessert Porte de Bagnolet ?", "Uniquement la <strong>M3</strong>. Bus 57, 76, 102, 122, 351."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 mars 1971</strong> (prolongement Gambetta ↔ Gallieni)."),
            ("Pour Bel-Est ?", "<strong>~5 min à pied</strong> via la place Édouard-Vaillant."),
            ("Pour la gare routière internationale ?", "<strong>~5 min à pied</strong> ou <strong>M3 → Gallieni</strong> (1 station)."),
            ("Pour Bagnolet (93) ?", "<strong>Sortie directe</strong> vers la commune."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Centre commercial Bel-Est</strong> à 5 min : grand centre des années 1970.",
            "<strong>Gare routière internationale Gallieni</strong> à 5 min : FlixBus, Eurolines, BlaBlaCar Bus vers toute l'Europe.",
            "Pour <strong>Bagnolet (93)</strong> : sortie directe.",
            "Pour <strong>Père Lachaise</strong> : <strong>M3 directe</strong> (3 stations).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🚌", "Gare routière internationale Gallieni", "La <strong>gare routière internationale Gallieni</strong> (Paris-Gallieni), à 5 min de Porte de Bagnolet, est le <strong>principal hub parisien pour les bus internationaux</strong>. <strong>FlixBus, BlaBlaCar Bus, Ouibus, Eurolines</strong> y opèrent. Destinations : toute la France, <strong>Royaume-Uni, Espagne, Italie, Allemagne, Pologne, Roumanie</strong>. Construite en <strong>1976</strong> avec le centre commercial Bel-Est. <strong>~20 millions de voyageurs/an</strong> avant la déréglementation des autocars en 2015."),
            ("🛍️", "Centre commercial Bel-Est (1976)", "Le <strong>centre commercial Bel-Est</strong>, inauguré en <strong>1976</strong>, est l'un des <strong>premiers grands centres commerciaux</strong> de la première couronne parisienne. À cheval sur <strong>Paris (20e) et Bagnolet (93)</strong>. <strong>~120 boutiques</strong>, hypermarché Carrefour, restaurants. Architecture typique des <strong>années 1970</strong>. Modernisé en 2010s mais conserve son atmosphère caractéristique de l'urbanisme commercial post-1968.")
        ],
        "itin": [
            ("Gallieni (terminus M3)", "gallieni", "M3", "M3 directe (1 station, terminus)", 2),
            ("Centre commercial Bel-Est", "porte-de-bagnolet", "à pied", "Place Édouard-Vaillant (5 min)", 5),
            ("Gare routière internationale", "gallieni", "à pied", "Place Édouard-Vaillant (5 min)", 5),
            ("Père Lachaise", "pere-lachaise", "M3", "M3 directe (3 stations)", 6),
            ("République", "republique", "M3", "M3 directe (8 stations)", 17),
            ("Opéra Garnier", "opera", "M3", "M3 directe (14 stations)", 28)
        ]
    },
    "gallieni": {
        "addr": "Avenue du Général-de-Gaulle, 93170 Bagnolet", "arr": "Bagnolet (93)",
        "seo": "Station Gallieni, terminus est M3 à Bagnolet (93). Gare routière internationale (FlixBus, Eurolines). Nommée d'après Joseph Gallieni, héros de la Marne.",
        "tagline": "M3 — terminus est, gare routière internationale, général Gallieni",
        "hero_desc": "Station <strong>Gallieni</strong>, <strong>terminus est de la M3</strong>, à <strong>Bagnolet</strong> (Seine-Saint-Denis, 93). Ouverte le <strong>27 mars 1971</strong> avec le prolongement Gambetta ↔ Gallieni. <strong>Gare routière internationale Paris-Gallieni</strong> à la sortie. Nommée d'après <strong>Joseph Gallieni</strong> (<strong>1849-1916</strong>), <strong>général et maréchal de France</strong>, <strong>« sauveur de Paris »</strong> à la <strong>bataille de la Marne</strong> (1914).",
        "intros": [
            "La station <strong>Gallieni</strong> est <strong>terminus est de la M3</strong>, située à <strong>Bagnolet</strong> (Seine-Saint-Denis, 93). Bus 57, 76, 102, 122, 318, 351. À la sortie : la <strong>gare routière internationale Paris-Gallieni</strong>.",
            "Ouverte le <strong>27 mars 1971</strong> avec le <strong>prolongement de la M3</strong> de Gambetta à Gallieni. Premier terminus M3 hors de Paris.",
            "Le nom <strong>Gallieni</strong> rend hommage à <strong>Joseph Simon Gallieni</strong> (<strong>1849-1916</strong>), <strong>général puis maréchal de France</strong> (à titre posthume, 1921). <strong>Gouverneur militaire de Paris</strong> en <strong>août 1914</strong>, il organise la <strong>défense de Paris</strong> et la <strong>contre-offensive de la bataille de la Marne</strong> (5-12 septembre 1914) — célèbres <strong>taxis de la Marne</strong> qu'il réquisitionne. <strong>« Sauveur de Paris »</strong>."
        ],
        "hist_title": "1971 : terminus est et « sauveur de Paris »",
        "hist": [
            "La station Gallieni est <strong>inaugurée le 27 mars 1971</strong> avec le <strong>prolongement de la M3</strong> de <strong>Gambetta à Gallieni</strong>, premier terminus M3 hors de Paris intra-muros.",
            "Le nom <strong>Gallieni</strong> commémore <strong>Joseph Simon Gallieni</strong> (<strong>24 avril 1849 - 27 mai 1916</strong>), <strong>général puis maréchal de France</strong> (titre posthume, <strong>7 mai 1921</strong>). Officier d'infanterie, il sert d'abord en Algérie, au Sénégal, à Madagascar (gouverneur 1896-1905), au Tonkin.",
            "Le <strong>26 août 1914</strong>, alors que les armées allemandes menacent Paris, Gallieni est nommé <strong>gouverneur militaire de Paris</strong>. Il organise la <strong>défense de la capitale</strong> et la <strong>contre-offensive de la Marne</strong> (<strong>5-12 septembre 1914</strong>). Il <strong>réquisitionne 600 taxis parisiens</strong> (les célèbres <strong>« taxis de la Marne »</strong>) pour transporter en urgence 6000 soldats de la 7e division d'infanterie au front. <strong>Victoire de la Marne</strong>, Paris sauvée. <strong>Mort à Versailles le 27 mai 1916</strong>. Devient « <strong>Sauveur de Paris</strong> »."
        ],
        "faq": [
            ("Quelle ligne dessert Gallieni ?", "Uniquement la <strong>M3</strong> (terminus est). Bus 57, 76, 102, 122, 318, 351."),
            ("Qui est Gallieni ?", "<strong>Joseph Gallieni</strong> (1849-1916), <strong>général puis maréchal de France</strong>. <strong>Gouverneur militaire de Paris</strong> en 1914, organisateur de la <strong>victoire de la Marne</strong>. <strong>« Sauveur de Paris »</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 mars 1971</strong>."),
            ("Pour la gare routière internationale ?", "<strong>Sortie directe</strong>. FlixBus, Eurolines, BlaBlaCar Bus."),
            ("Pour Bagnolet centre ?", "<strong>~10 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>. Ascenseurs récents installés.")
        ],
        "tips": [
            "<strong>Gare routière internationale Paris-Gallieni</strong> à la sortie : bus FlixBus, Eurolines, BlaBlaCar.",
            "<strong>Centre commercial Bel-Est</strong> à 5 min à pied.",
            "Pour <strong>Bagnolet (93)</strong> : sortie directe.",
            "Pour <strong>Père Lachaise</strong> : <strong>M3 directe</strong> (4 stations, ~9 min).",
            "Zone tarifaire <strong>3</strong>, Seine-Saint-Denis."
        ],
        "trivia": [
            ("🚕", "Taxis de la Marne (septembre 1914)", "Lors de la <strong>bataille de la Marne</strong> (5-12 septembre 1914), le <strong>général Gallieni</strong>, gouverneur militaire de Paris, <strong>réquisitionne 600 taxis parisiens</strong> (modèle <em>Renault AG1 Landaulet</em>) pour <strong>transporter en urgence 6000 soldats</strong> de la <strong>7e division d'infanterie</strong> au front de la Marne. <strong>Deux convois</strong> dans la nuit du <strong>6 au 7 septembre</strong>. Cette <strong>opération mythique</strong>, bien que limitée militairement, devint <strong>symbole de l'union sacrée</strong> et de la <strong>victoire de la Marne</strong>. Paris est sauvée."),
            ("🎖️", "Gallieni, « Sauveur de Paris »", "<strong>Joseph Gallieni</strong> (1849-1916), <strong>« Sauveur de Paris »</strong>. Officier dont la carrière le mène en <strong>Algérie, au Sénégal, à Madagascar</strong> (gouverneur 1896-1905, pacification), au <strong>Tonkin</strong>. <strong>Gouverneur militaire de Paris</strong> le 26 août 1914, il organise la <strong>défense de la capitale</strong> et la <strong>victoire de la Marne</strong>. <strong>Ministre de la Guerre</strong> en 1915-1916. <strong>Mort à Versailles le 27 mai 1916</strong>. <strong>Élevé maréchal de France à titre posthume</strong> en 1921.")
        ],
        "itin": [
            ("Gare routière internationale", "gallieni", "à pied", "Sortie directe", 2),
            ("Centre commercial Bel-Est", "porte-de-bagnolet", "à pied", "Place Édouard-Vaillant (5 min)", 5),
            ("Porte de Bagnolet", "porte-de-bagnolet", "M3", "M3 directe (1 station)", 2),
            ("Père Lachaise", "pere-lachaise", "M3", "M3 directe (4 stations)", 9),
            ("République", "republique", "M3", "M3 directe (9 stations)", 19),
            ("Opéra Garnier", "opera", "M3", "M3 directe (15 stations)", 30)
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
