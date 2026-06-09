#!/usr/bin/env python3
"""Enrichit les 16 JSONs M4 avec contenu T0 Wikipedia FR (mode condense)."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    # ====== M4 NORD - 18e arr ======
    "simplon": {
        "seo": "Station Simplon : M4 dans le 18e arrondissement de Paris, ouverte en 1908 avec la ligne 4 originelle. Entre Porte de Clignancourt et Marcadet-Poissonniers.",
        "tagline": "M4 — porte d'entrée du 18e",
        "hero_desc": "Station ouverte le <strong>21 avril 1908</strong> avec la mise en service de la ligne 4 originelle (Porte de Clignancourt ↔ Châtelet). Nom inspiré du <strong>col du Simplon</strong> (Alpes suisses), via la rue du Simplon dans le 18e. À proximité : la <strong>Goutte d'Or</strong> et le <strong>boulevard Ney</strong> (boulevard des Maréchaux).",
        "intros": [
            "La station <strong>Simplon</strong> est située dans le <strong>18e arrondissement de Paris</strong>, sous la <strong>rue du Simplon</strong> près du boulevard Ney. Elle est desservie uniquement par la <strong>ligne 4 du métro</strong> (Porte de Clignancourt ↔ Bagneux - Lucie Aubrac), entre <strong>Porte de Clignancourt</strong> (1 station vers le nord, terminus) et <strong>Marcadet-Poissonniers</strong> (1 station vers le sud, correspondance M12). Bus 60, 85.",
            "Ouverte le <strong>21 avril 1908</strong>, la station fait partie du tronçon historique originel de la M4 (Porte de Clignancourt ↔ Châtelet). Le nom <strong>Simplon</strong> est inspiré du <strong>col du Simplon</strong> (2 005 m d'altitude) reliant la Suisse à l'Italie, dont une rue voisine porte le nom — usage courant au XIXᵉ siècle de baptiser les rues du nord parisien d'après les cols alpins.",
            "Le quartier autour est résidentiel et populaire. À proximité : le <strong>square de Clignancourt</strong>, le <strong>boulevard Ney</strong> (boulevard des Maréchaux, jalon avant la Petite Ceinture historique), et l'extrémité nord de la <strong>Goutte d'Or</strong>. Affluence quotidienne modérée."
        ],
        "hist_title": "Une station de 1908 sur l'axe nord-sud historique",
        "hist": [
            "La station <strong>Simplon</strong> est inaugurée le <strong>21 avril 1908</strong> avec la mise en service de la <strong>ligne 4 originelle</strong> (Porte de Clignancourt ↔ Châtelet, 9 stations). La M4 fait partie des <strong>premières lignes du métro parisien</strong> (après les M1 1900, M2 1903, M3 1904).",
            "Le tronçon nord (Porte de Clignancourt ↔ Châtelet) ouvre en 1908. La <strong>traversée sous la Seine</strong> (Châtelet ↔ Cité ↔ Saint-Michel) est réalisée en 1910 par une <strong>technique d'immersion de caissons</strong> sous-fluviaux — première mondiale à l'époque. La ligne atteint Porte d'Orléans en 1910, puis Mairie de Montrouge en 2013 et Bagneux - Lucie Aubrac en 2022.",
            "Configuration classique : <strong>2 quais latéraux</strong> sous voûte en pierre meulière, longueur 75 m, 2 voies. Décoration originelle conservée (céramique blanche biseautée). Pas de correspondance autre que la M4. Fréquentation : ~3,5 millions/an (rang ~150)."
        ],
        "faq": [
            ("Quelle ligne dessert Simplon ?", "Uniquement la <strong>M4</strong> (Porte de Clignancourt ↔ Bagneux - Lucie Aubrac). Bus 60, 85."),
            ("Pourquoi le nom Simplon ?", "De la <strong>rue du Simplon</strong>, elle-même nommée d'après le <strong>col du Simplon</strong> (2 005 m d'altitude), col alpin reliant la Suisse à l'Italie. Usage courant au XIXᵉ siècle de baptiser les rues nord parisiennes d'après les cols alpins."),
            ("Quand a-t-elle ouvert ?", "Le <strong>21 avril 1908</strong>, avec le tronçon originel de la M4 (Porte de Clignancourt ↔ Châtelet)."),
            ("Comment aller à Châtelet ?", "<strong>M4 directe</strong> : ~10 min (6 stations vers le sud)."),
            ("Comment rejoindre les Puces de Saint-Ouen ?", "<strong>M4 vers Porte de Clignancourt</strong> (1 station, terminus nord) + 5 min à pied vers le marché aux Puces."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. M4 historique 1908 : accessibilité PMR partielle ou en cours d'aménagement.")
        ],
        "tips": [
            "Pour <strong>Puces de Saint-Ouen</strong> : M4 vers Porte de Clignancourt + 5 min à pied.",
            "Pour <strong>Marcadet-Poissonniers</strong> (correspondance M12) : M4 directe (1 station).",
            "Pour <strong>Gare du Nord</strong> : M4 directe (4 stations vers le sud).",
            "Quartier résidentiel — peu de commerces immédiats sortie métro.",
            "Boulevard Ney à 2 min — vue sur les Maréchaux."
        ],
        "trivia": [
            ("🏔️", "Col du Simplon — origine du nom", "Le nom <strong>Simplon</strong> vient du <strong>col du Simplon</strong> (2 005 m d'altitude), col alpin reliant la <strong>Suisse à l'Italie</strong>. Usage courant à Paris au XIXᵉ siècle de baptiser les rues d'après les cols alpins (Mont-Cenis, Petit-Saint-Bernard, etc.). La rue du Simplon a transmis son nom à la station de métro M4 en 1908."),
            ("🚇", "Ligne 4 originelle (1908)", "La station fait partie du <strong>tronçon originel de la ligne 4</strong>, mise en service le <strong>21 avril 1908</strong> entre Porte de Clignancourt et Châtelet (9 stations). La M4 est la <strong>première ligne nord-sud</strong> du réseau parisien et fut prolongée sous la Seine en 1910 par une technique d'immersion de caissons sous-fluviaux (première mondiale).")
        ],
        "itin": [
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Bagneux (6 stations)", 12),
            ("Porte de Clignancourt via M4", "porte-de-clignancourt", "M4", "M4 direction Porte de Clignancourt (1 station)", 2),
            ("Marcadet-Poissonniers via M4", "marcadet-poissonniers", "M4", "M4 direction Bagneux (1 station)", 2),
            ("Gare du Nord via M4", "gare-du-nord", "M4", "M4 direction Bagneux (4 stations)", 8),
            ("Saint-Michel via M4", "saint-michel", "M4", "M4 direction Bagneux (8 stations)", 17),
            ("Montparnasse via M4", "montparnasse-bienvenue", "M4", "M4 direction Bagneux (12 stations)", 25)
        ]
    },
    "marcadet-poissonniers": {
        "seo": "Station Marcadet-Poissonniers : M4 + M12 dans le 18e arr., correspondance majeure nord parisien. À 10 min de Montmartre et du Sacré-Cœur.",
        "tagline": "M4 + M12 — accès Goutte d'Or et Montmartre",
        "hero_desc": "Station <strong>Marcadet-Poissonniers</strong> dans le <strong>18e arrondissement</strong>, à l'intersection du boulevard Barbès et de la rue Marcadet. Desservie par <strong>M4</strong> (ouverte 21 avril 1908) et <strong>M12</strong> (ouverte 5 novembre 1912). À <strong>10 min</strong> : <strong>Montmartre</strong> (Sacré-Cœur, place du Tertre) et la <strong>Goutte d'Or</strong> (quartier multiculturel africain).",
        "intros": [
            "La station <strong>Marcadet-Poissonniers</strong> est située dans le <strong>18e arrondissement de Paris</strong>, à l'intersection du <strong>boulevard Barbès</strong> et de la <strong>rue Marcadet</strong>. Elle est desservie par <strong>2 lignes</strong> : <strong>M4</strong> (Porte de Clignancourt ↔ Bagneux) et <strong>M12</strong> (Aubervilliers - Front populaire ↔ Mairie d'Issy). Bus 31, 56, 60, 85.",
            "La station <strong>M4</strong> ouvre le <strong>21 avril 1908</strong> avec le tronçon originel (Porte de Clignancourt ↔ Châtelet). La station <strong>M12</strong> est ajoutée le <strong>5 novembre 1912</strong> avec la mise en service de la ligne A de la <strong>Nord-Sud</strong> (compagnie privée concurrente de la CMP), reliant Porte de Versailles à Pigalle. La M12 est intégrée à la RATP en 1930.",
            "À <strong>10 min à pied</strong> : la <strong>colline de Montmartre</strong>, avec la <strong>basilique du Sacré-Cœur</strong> (1875-1914), la <strong>place du Tertre</strong> (peintres en plein air) et l'<strong>Espace Dalí</strong>. À <strong>5 min</strong> : la <strong>Goutte d'Or</strong>, quartier multiculturel d'origine maghrébine et africaine, avec le <strong>Marché Barbès</strong> (textile) et la <strong>rue de la Goutte d'Or</strong> (mosquée Al-Fath)."
        ],
        "hist_title": "1908 : M4, 1912 : Nord-Sud (M12), correspondance historique",
        "hist": [
            "La station <strong>M4</strong> ouvre le <strong>21 avril 1908</strong> avec le tronçon originel de la M4 (Porte de Clignancourt ↔ Châtelet, 9 stations).",
            "Le <strong>5 novembre 1912</strong>, la <strong>Compagnie Nord-Sud</strong> ouvre la ligne A (futur M12) entre <strong>Porte de Versailles et Notre-Dame de Lorette</strong>, prolongée à Pigalle puis Jules Joffrin (1916). Marcadet-Poissonniers devient alors un <strong>point de correspondance majeur du nord parisien</strong>. La Nord-Sud était une compagnie privée concurrente de la CMP, intégrée à la <strong>RATP en 1930</strong> sous la nationalisation.",
            "La station permet de relier rapidement les axes nord-sud (M12 vers Pigalle/Madeleine) et nord-est (M4 vers Châtelet/Saint-Michel). Fréquentation : ~6 millions/an. À 10 min à pied : <strong>Montmartre</strong> et le <strong>Sacré-Cœur</strong>, l'un des sites les plus visités de Paris (~10 millions/an). Affluence touristique modérée à la station elle-même."
        ],
        "faq": [
            ("Quelles lignes desservent Marcadet-Poissonniers ?", "<strong>M4</strong> (1908) et <strong>M12</strong> (1912, ex-Nord-Sud). Bus 31, 56, 60, 85."),
            ("Comment aller à Montmartre / Sacré-Cœur ?", "<strong>10 min à pied</strong> en direction du nord-ouest (rue Custine → Lamarck → escaliers). Plus rapide : M12 jusqu'à <strong>Jules Joffrin</strong> + 8 min à pied."),
            ("Qu'est-ce que la Nord-Sud ?", "La <strong>Compagnie du chemin de fer électrique souterrain Nord-Sud de Paris</strong>, compagnie privée concurrente de la CMP. Ouvre la ligne A (futur M12) en 1912. Intégrée à la <strong>RATP en 1930</strong>. Le préfixe « Nord-Sud » désigne aujourd'hui les lignes 12 et 13."),
            ("Comment rejoindre la Goutte d'Or ?", "<strong>5 min à pied</strong> en direction du sud-est. Quartier multiculturel maghrébin/africain avec marché Barbès, mosquée Al-Fath."),
            ("Comment aller à Châtelet ?", "<strong>M4 directe</strong> : ~12 min (7 stations vers le sud)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Stations historiques 1908/1912 : accessibilité PMR partielle.")
        ],
        "tips": [
            "Pour <strong>Montmartre/Sacré-Cœur</strong> : M12 vers Jules Joffrin + 8 min à pied.",
            "Pour <strong>Goutte d'Or</strong> : 5 min à pied sud-est.",
            "Pour <strong>Châtelet</strong> : M4 directe (~12 min).",
            "Pour <strong>Madeleine</strong> : M12 directe (~15 min).",
            "Marché Barbès (textile) à 5 min — produits multiculturels."
        ],
        "trivia": [
            ("🚇", "Nord-Sud — compagnie privée concurrente (1912)", "La M12, à Marcadet-Poissonniers depuis le <strong>5 novembre 1912</strong>, fut construite par la <strong>Compagnie Nord-Sud</strong>, société privée concurrente de la CMP (Compagnie du Métropolitain de Paris). La Nord-Sud distinguait visuellement ses stations par des <strong>céramiques colorées</strong> (vert/turquoise) au lieu du blanc CMP. Intégrée à la <strong>RATP en 1930</strong> sous la nationalisation. Le « N » de Nord-Sud apparaît encore sur certains éléments d'origine."),
            ("⛪", "Sacré-Cœur de Montmartre à 10 min", "À <strong>10 min à pied</strong>, la <strong>basilique du Sacré-Cœur de Montmartre</strong> (1875-1914, architecte Paul Abadie), monument emblématique du sommet de la <strong>colline de Montmartre</strong> (130 m). Style romano-byzantin. <strong>~10 millions de visiteurs/an</strong>, l'un des sites les plus visités de France après la Tour Eiffel.")
        ],
        "itin": [
            ("Montmartre via M12", "montmartre", "M12 + à pied", "M12 jusqu'à Jules Joffrin (2 stations) + 8 min", 15),
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Bagneux (7 stations)", 14),
            ("Goutte d'Or", "goutte-or", "à pied", "5 min sud-est", 5),
            ("Madeleine via M12", "madeleine", "M12", "M12 direction Mairie d'Issy", 15),
            ("Gare du Nord via M4", "gare-du-nord", "M4", "M4 direction Bagneux (3 stations)", 6),
            ("Bagneux - Lucie Aubrac via M4", "bagneux-lucie-aubrac", "M4", "M4 terminus sud", 35)
        ]
    },
    "chateau-rouge": {
        "seo": "Station Château Rouge : M4 dans le 18e arr., cœur de la Goutte d'Or et du quartier africain de Paris. Marché Dejean iconique, l'un des plus diversifiés de Paris.",
        "tagline": "M4 — cœur de la Goutte d'Or et de l'Afrique parisienne",
        "hero_desc": "Station <strong>Château Rouge</strong> ouverte le <strong>21 avril 1908</strong> avec la M4 originelle. Située dans le <strong>18e arrondissement</strong>, au cœur de la <strong>Goutte d'Or</strong>, quartier multiculturel d'origine africaine subsaharienne et maghrébine. À la sortie : le <strong>marché Dejean</strong>, l'un des marchés alimentaires les plus diversifiés de Paris (Afrique de l'Ouest, Antilles, Maghreb).",
        "intros": [
            "La station <strong>Château Rouge</strong> est située dans le <strong>18e arrondissement de Paris</strong>, sur la <strong>place du Château-Rouge</strong>. Elle est desservie uniquement par la <strong>M4</strong> (Porte de Clignancourt ↔ Bagneux - Lucie Aubrac), entre <strong>Marcadet-Poissonniers</strong> (1 station nord, correspondance M12) et <strong>Barbès - Rochechouart</strong> (1 station sud, correspondance M2). Bus 31, 56.",
            "Ouverte le <strong>21 avril 1908</strong> avec le tronçon originel de la M4 (Porte de Clignancourt ↔ Châtelet). Le nom <strong>« Château Rouge »</strong> vient d'une ancienne <strong>guinguette du XVIIIᵉ siècle</strong> qui occupait l'emplacement, dénommée « Le Château Rouge » à cause de la couleur de sa façade.",
            "À la sortie : le <strong>marché Dejean</strong>, l'un des <strong>marchés alimentaires les plus diversifiés de Paris</strong>. Spécialités : <strong>Afrique de l'Ouest</strong> (Sénégal, Mali, Côte d'Ivoire), <strong>Antilles</strong>, <strong>Maghreb</strong>. Au cœur de la <strong>Goutte d'Or</strong>, quartier emblématique de la diversité parisienne, immortalisé par Émile Zola dans <em>L'Assommoir</em> (1877)."
        ],
        "hist_title": "Une guinguette du XVIIIᵉ et la Goutte d'Or multiculturelle",
        "hist": [
            "Le nom <strong>« Château Rouge »</strong> vient d'une ancienne <strong>guinguette parisienne du XVIIIᵉ siècle</strong> qui occupait l'emplacement actuel de la place. La guinguette était baptisée d'après la <strong>couleur rouge de sa façade</strong>. Lieu de fête populaire jusqu'au XIXᵉ siècle, puis disparu lors de la transformation haussmannienne.",
            "La station <strong>M4</strong> est inaugurée le <strong>21 avril 1908</strong> avec le tronçon originel (Porte de Clignancourt ↔ Châtelet).",
            "Le quartier de la <strong>Goutte d'Or</strong> a une histoire singulière. Au XIXᵉ siècle, quartier populaire ouvrier (carriers, blanchisseuses, marchands ambulants), immortalisé par <strong>Émile Zola</strong> dans <em>L'Assommoir</em> (1877). Au XXᵉ siècle, accueille successivement des vagues d'immigration : <strong>italiens, polonais, espagnols (avant 1939)</strong>, puis <strong>maghrébins (1960-70s)</strong>, puis <strong>africains subsahariens (1980s+)</strong>. Aujourd'hui : quartier le plus diversifié de Paris en termes d'origines.",
            "À la sortie : le <strong>marché Dejean</strong>, marché alimentaire ouvert tous les jours sauf lundi. Spécialités africaines : <strong>légumes-feuilles</strong> (ngalakh, gombos, baobabs), <strong>poissons d'eau douce africains</strong>, <strong>épices</strong>, <strong>tissus wax</strong>. Cœur économique de la <strong>diaspora africaine parisienne</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Château Rouge ?", "Uniquement la <strong>M4</strong>. Bus 31, 56."),
            ("Pourquoi le nom Château Rouge ?", "D'une ancienne <strong>guinguette du XVIIIᵉ siècle</strong> baptisée « Le Château Rouge » à cause de la <strong>couleur rouge de sa façade</strong>. La guinguette a disparu au XIXᵉ siècle avec la transformation haussmannienne."),
            ("Qu'est-ce que le marché Dejean ?", "L'un des <strong>marchés alimentaires les plus diversifiés de Paris</strong>, à la sortie de la station. Spécialités <strong>Afrique de l'Ouest</strong> (Sénégal, Mali, Côte d'Ivoire), <strong>Antilles</strong>, <strong>Maghreb</strong>. Ouvert mardi-dimanche."),
            ("Qu'est-ce que la Goutte d'Or ?", "Quartier multiculturel du 18e arr. parisien. Au XIXᵉ : populaire ouvrier (Zola, L'Assommoir 1877). Au XXᵉ : vagues d'immigration italienne, polonaise, espagnole, maghrébine, africaine. Aujourd'hui : quartier le plus diversifié de Paris."),
            ("Comment aller à Châtelet ?", "<strong>M4 directe</strong> : ~10 min (5 stations vers le sud)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. M4 historique 1908.")
        ],
        "tips": [
            "<strong>Marché Dejean</strong> à la sortie — meilleur marché africain de Paris.",
            "<strong>Goutte d'Or</strong> en flânant — quartier vivant et coloré.",
            "Pour <strong>Sacré-Cœur</strong> : 15 min à pied direction nord-ouest.",
            "Pour <strong>Châtelet</strong> : M4 directe (~10 min).",
            "Vigilance pickpockets standard quartier dense."
        ],
        "trivia": [
            ("🏰", "Une guinguette du XVIIIᵉ siècle", "Le nom <strong>« Château Rouge »</strong> vient d'une ancienne <strong>guinguette parisienne du XVIIIᵉ siècle</strong>. À l'époque, les guinguettes étaient des établissements en périphérie de Paris où l'on buvait et dansait pour <strong>échapper à l'octroi parisien</strong> (taxe sur les boissons). « Le Château Rouge » devait sa couleur à un <strong>enduit rouge sur sa façade</strong>. Lieu de fête populaire jusqu'au XIXᵉ. Disparu avec la transformation haussmannienne."),
            ("🌍", "Marché Dejean — cœur africain de Paris", "À la sortie de la station, le <strong>marché Dejean</strong> est l'un des <strong>marchés alimentaires les plus diversifiés de Paris</strong>. Spécialités : <strong>Afrique de l'Ouest</strong> (Sénégal, Mali, Côte d'Ivoire), <strong>Antilles</strong>, <strong>Maghreb</strong>. Produits emblématiques : feuilles de manioc, gombos, poissons d'eau douce africains (capitaine, mâchoiron), épices, tissus wax. Cœur économique de la <strong>diaspora africaine parisienne</strong>. Ouvert mardi-dimanche.")
        ],
        "itin": [
            ("Marché Dejean", "marche-dejean", "à pied", "Sortie directe", 1),
            ("Sacré-Cœur Montmartre", "sacre-coeur", "à pied", "15 min direction nord-ouest", 15),
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Bagneux (5 stations)", 10),
            ("Gare du Nord via M4", "gare-du-nord", "M4", "M4 direction Bagneux (3 stations)", 6),
            ("Barbès via M4", "barbes-rochechouart", "M4", "M4 direction Bagneux (1 station)", 2),
            ("Saint-Michel via M4", "saint-michel", "M4", "M4 direction Bagneux (8 stations)", 16)
        ]
    },
    "barbes-rochechouart": {
        "seo": "Station Barbès - Rochechouart : M2 + M4 dans le 10e/18e arr. Station mythique parisienne, aérienne sur le viaduc M2. Tati Barbès historique.",
        "tagline": "M2 + M4 — station aérienne mythique du nord parisien",
        "hero_desc": "Station <strong>Barbès - Rochechouart</strong> à la jonction <strong>10e, 18e</strong> et limite 9e arrondissements. Desservie par <strong>M2</strong> (ouverte 21 avril 1903, aérienne sur viaduc) et <strong>M4</strong> (ouverte 21 avril 1908, souterraine). Station <strong>mythique parisienne</strong> : l'une des rares à voir circuler le métro en surface dans Paris intra-muros, sur le <strong>viaduc M2</strong>. Quartier emblématique de la diversité du nord parisien.",
        "intros": [
            "La station <strong>Barbès - Rochechouart</strong> est située à la <strong>jonction des 9e, 10e et 18e arrondissements</strong>, sous (et au-dessus de) le boulevard Barbès et le boulevard de la Chapelle. Elle est desservie par <strong>2 lignes</strong> : <strong>M2</strong> (Porte Dauphine ↔ Nation, aérienne sur viaduc) et <strong>M4</strong> (Porte de Clignancourt ↔ Bagneux, souterraine). Bus 30, 31, 38, 56, 65, 350.",
            "La station <strong>M2</strong> ouvre le <strong>21 avril 1903</strong> avec le viaduc aérien de la M2. La station <strong>M4</strong> est ajoutée le <strong>21 avril 1908</strong> avec le tronçon originel de la M4. <strong>Coïncidence historique notable : les 2 lignes ont ouvert le même jour de mois et même mois, à 5 ans d'écart.</strong>",
            "La station est <strong>mythique du paysage parisien</strong> : l'une des rares où le métro circule <strong>en surface dans Paris intra-muros</strong>, sur le viaduc aérien de la M2 (entre Anvers et La Chapelle). Quartier emblématique du nord populaire et multiculturel parisien. À proximité : <strong>marché Barbès</strong> (textile), <strong>Tati Barbès</strong> (historique, magasins discount fermés en 2021), <strong>boulevard Rochechouart</strong>."
        ],
        "hist_title": "Une station aérienne mythique (M2 1903, M4 1908)",
        "hist": [
            "La station <strong>M2</strong> ouvre le <strong>21 avril 1903</strong> avec le <strong>viaduc aérien</strong> de la M2 entre Anvers et La Chapelle. La M2 était conçue pour relier les portes ouest et est de Paris, en passant par le nord. Le viaduc aérien permet de franchir la déclivité de Montmartre.",
            "La station <strong>M4</strong> est ajoutée le <strong>21 avril 1908</strong> avec le tronçon originel de la M4 (Porte de Clignancourt ↔ Châtelet). Coïncidence historique : <strong>même date d'ouverture (21 avril)</strong> pour les 2 lignes, à 5 ans d'écart.",
            "Le quartier <strong>Barbès</strong> est emblématique du <strong>Paris populaire et multiculturel</strong>. Au XIXᵉ siècle : quartier ouvrier. Au XXᵉ : vagues d'immigration italienne, espagnole, maghrébine, africaine. Le <strong>marché Barbès</strong> (textile et alimentaire) est l'un des plus fréquentés de Paris.",
            "<strong>Tati Barbès</strong> (1948-2021) : célèbre chaîne de magasins discount populaires français, dont le <strong>magasin historique</strong> était situé à 100 m de la station. Logo rose et blanc carrelé. Fermé en 2021 après faillite de la marque. Lieu emblématique du commerce populaire parisien.",
            "Station <strong>aérienne sur viaduc M2</strong> : configuration rare dans Paris intra-muros. La voûte du viaduc est en métallerie rivetée, témoin de l'<strong>architecture industrielle du XIXᵉ siècle</strong>. Fréquentation : ~10 millions/an."
        ],
        "faq": [
            ("Quelles lignes desservent Barbès - Rochechouart ?", "<strong>M2</strong> (1903, aérienne sur viaduc) et <strong>M4</strong> (1908, souterraine). Bus 30, 31, 38, 56, 65, 350."),
            ("Pourquoi la station est-elle aérienne ?", "Seule la <strong>M2 est aérienne sur viaduc</strong> entre Anvers et La Chapelle, pour franchir la déclivité de Montmartre. La M4 reste souterraine. Configuration rare dans Paris intra-muros."),
            ("Qu'est-ce que Tati Barbès ?", "Célèbre chaîne de magasins discount populaires français (1948-2021), dont le <strong>magasin historique</strong> était à 100 m de la station. Logo rose et blanc carrelé iconique. <strong>Fermé en 2021</strong> après faillite. Lieu emblématique du commerce populaire parisien."),
            ("Comment aller au Sacré-Cœur ?", "<strong>10 min à pied</strong> direction nord (boulevard Rochechouart → Anvers). Plus rapide : <strong>M2 vers Anvers</strong> (1 station) + 7 min à pied + funiculaire."),
            ("Comment aller à Gare du Nord ?", "<strong>M4 directe</strong> : 1 station vers le sud (~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. M2 aérienne 1903 et M4 1908 : accessibilité PMR partielle ou en cours d'aménagement.")
        ],
        "tips": [
            "<strong>Vue aérienne</strong> depuis le quai M2 — rare dans Paris intra-muros.",
            "Pour <strong>Sacré-Cœur</strong> : M2 vers Anvers (1 station) + funiculaire.",
            "Pour <strong>Gare du Nord</strong> : M4 directe (1 station).",
            "Marché Barbès (textile) à 5 min.",
            "Vigilance pickpockets élevée quartier dense."
        ],
        "trivia": [
            ("🚇", "Station aérienne — rare dans Paris intra-muros", "Seule la <strong>M2 à Barbès - Rochechouart est aérienne sur viaduc</strong>, configuration rare dans Paris intra-muros (les autres viaducs M2/M6 sont à la périphérie). Le viaduc franchit la déclivité de Montmartre entre Anvers et La Chapelle. Voûte en <strong>métallerie rivetée</strong> du XIXᵉ siècle. Ouverte le <strong>21 avril 1903</strong>."),
            ("🛍️", "Tati Barbès (1948-2021) — empire du discount populaire", "À <strong>100 m</strong> de la station, le <strong>magasin historique Tati Barbès</strong> (1948-2021) était l'un des plus emblématiques du commerce populaire parisien. Fondé par <strong>Jules Ouaki</strong> en 1948. Logo <strong>rose et blanc carrelé</strong> iconique, repris dans le design graphique et la mode. Apogée années 1980-1990 : ~100 magasins en France. <strong>Fermé en 2021</strong> après faillite de la marque (concurrence du e-commerce et des Primark).")
        ],
        "itin": [
            ("Gare du Nord via M4", "gare-du-nord", "M4", "M4 direction Bagneux (1 station)", 2),
            ("Sacré-Cœur via M2", "sacre-coeur", "M2 + funiculaire", "M2 jusqu'à Anvers + 7 min + funiculaire", 15),
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Bagneux (4 stations)", 8),
            ("Nation via M2", "nation", "M2", "M2 direction Nation", 25),
            ("Marché Barbès", "marche-barbes", "à pied", "5 min sortie directe", 5),
            ("Saint-Michel via M4", "saint-michel", "M4", "M4 direction Bagneux (7 stations)", 14)
        ]
    },
    "chateau-d-eau": {
        "seo": "Station Château d'Eau : M4 dans le 10e arr., boulevard de Strasbourg. Quartier de la presse historique et coiffeurs afro emblématiques.",
        "tagline": "M4 — quartier de la presse et coiffeurs afro",
        "hero_desc": "Station <strong>Château d'Eau</strong> ouverte le <strong>21 avril 1908</strong> avec la M4 originelle. Située dans le <strong>10e arrondissement</strong>, sur le <strong>boulevard de Strasbourg</strong> à proximité de la rue du Château d'Eau. Quartier historique de la <strong>presse parisienne</strong> (siège de plusieurs grands journaux au XIXᵉ-XXᵉ) et de la <strong>coiffure afro</strong> (rue du Château d'Eau emblématique).",
        "intros": [
            "La station <strong>Château d'Eau</strong> est située dans le <strong>10e arrondissement de Paris</strong>, sur le <strong>boulevard de Strasbourg</strong> à l'intersection avec la rue du Château d'Eau. Elle est desservie uniquement par la <strong>M4</strong>, entre <strong>Strasbourg - Saint-Denis</strong> (1 station sud, M8+M9) et <strong>Gare de l'Est</strong> (1 station nord, M5+M7). Bus 32, 38, 39, 47.",
            "Ouverte le <strong>21 avril 1908</strong> avec le tronçon originel de la M4 (Porte de Clignancourt ↔ Châtelet). Le nom <strong>« Château d'Eau »</strong> vient d'un ancien <strong>château d'eau monumental</strong> qui occupait la place du Château-d'Eau (aujourd'hui place de la République adjacente), démoli au XIXᵉ siècle.",
            "Le quartier autour est historiquement celui de la <strong>presse parisienne</strong> : siège de plusieurs grands journaux au XIXᵉ-XXᵉ siècle (Le Figaro, Le Matin, etc.). Aujourd'hui, la <strong>rue du Château d'Eau</strong> est mondialement connue comme <strong>l'épicentre de la coiffure afro à Paris</strong> : ~200 salons sur 800 m, clientèle de la diaspora africaine et antillaise."
        ],
        "hist_title": "1908 : un château d'eau monumental disparu",
        "hist": [
            "La station <strong>M4</strong> ouvre le <strong>21 avril 1908</strong> avec le tronçon originel de la M4 (Porte de Clignancourt ↔ Châtelet).",
            "Le nom <strong>« Château d'Eau »</strong> vient d'un <strong>château d'eau monumental</strong> qui occupait l'actuelle place de la République (à 200 m de la station). Construit en <strong>1811</strong> par l'architecte <strong>Pierre-Simon Girard</strong> (ingénieur en chef du canal de l'Ourcq), il s'agissait d'une <strong>fontaine monumentale</strong> alimentant les marchés du quartier en eau du canal de l'Ourcq. Détruit lors du percement des grands boulevards par <strong>Haussmann en 1869</strong>.",
            "Au XIXᵉ siècle, le quartier est <strong>l'épicentre de la presse parisienne</strong> : siège du <strong>Figaro</strong> rue du Faubourg-Montmartre, du <strong>Matin</strong> boulevard Poissonnière, et de nombreux autres. Activité d'imprimerie, papeterie, distribution. Décline au XXᵉ siècle avec le déménagement des journaux vers la périphérie.",
            "Aujourd'hui, la <strong>rue du Château d'Eau</strong> est mondialement connue comme <strong>l'épicentre de la coiffure afro à Paris</strong>. Environ <strong>200 salons de coiffure et instituts de beauté afro</strong> sur 800 mètres : <strong>defrisage</strong>, <strong>tressage</strong>, <strong>extensions</strong>, <strong>perruques</strong>. Clientèle issue de la diaspora africaine, antillaise et maghrébine. Phénomène urbain unique en Europe."
        ],
        "faq": [
            ("Quelle ligne dessert Château d'Eau ?", "Uniquement la <strong>M4</strong>. Bus 32, 38, 39, 47."),
            ("Pourquoi le nom Château d'Eau ?", "D'un <strong>château d'eau monumental</strong> construit en 1811 par Pierre-Simon Girard sur l'actuelle place de la République, alimentant les marchés en eau du canal de l'Ourcq. <strong>Détruit en 1869</strong> par Haussmann."),
            ("Qu'est-ce que la rue du Château d'Eau ?", "L'<strong>épicentre de la coiffure afro à Paris</strong>. Environ <strong>200 salons de coiffure et instituts de beauté afro</strong> sur 800 m. Defrisage, tressage, extensions, perruques. Clientèle de la diaspora africaine et antillaise. Phénomène urbain unique en Europe."),
            ("Comment aller à Châtelet ?", "<strong>M4 directe</strong> : ~8 min (4 stations vers le sud)."),
            ("Comment aller à Place de la République ?", "<strong>5 min à pied</strong> direction sud-est."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. M4 historique 1908.")
        ],
        "tips": [
            "<strong>Rue du Château d'Eau</strong> à pied — épicentre coiffure afro de Paris.",
            "Pour <strong>République</strong> : 5 min à pied.",
            "Pour <strong>Châtelet</strong> : M4 directe (~8 min).",
            "Pour <strong>Gare de l'Est</strong> : M4 directe (1 station).",
            "Quartier mixte commerce/multicultural."
        ],
        "trivia": [
            ("⛲", "Un château d'eau monumental de 1811", "Le nom vient d'un <strong>château d'eau monumental</strong> construit en <strong>1811</strong> par l'architecte <strong>Pierre-Simon Girard</strong> (ingénieur en chef du canal de l'Ourcq). Il s'agissait d'une <strong>fontaine monumentale</strong> sur l'actuelle place de la République, alimentant les marchés du quartier en eau du canal de l'Ourcq. <strong>Détruit en 1869</strong> lors du percement des grands boulevards par Haussmann. Vestige de l'urbanisme préhaussmannien."),
            ("💇", "Rue du Château d'Eau — épicentre afro coiffure", "Mondialement connue comme <strong>l'épicentre de la coiffure afro à Paris</strong>. Environ <strong>200 salons de coiffure et instituts de beauté</strong> sur 800 mètres. Spécialités : <strong>defrisage</strong>, <strong>tressage</strong>, <strong>extensions</strong>, <strong>perruques</strong>. Clientèle de la <strong>diaspora africaine, antillaise et maghrébine</strong>. Phénomène urbain unique en Europe, attirant clientèle internationale (Londres, Bruxelles, Berlin).")
        ],
        "itin": [
            ("Rue du Château d'Eau", "rue-chateau-eau", "à pied", "Sortie directe", 1),
            ("République", "republique", "à pied", "5 min sud-est", 5),
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Bagneux (4 stations)", 8),
            ("Gare de l'Est via M4", "gare-de-l-est", "M4", "M4 direction Porte de Clignancourt (1 station)", 2),
            ("Gare du Nord via M4", "gare-du-nord", "M4", "M4 direction Porte de Clignancourt (2 stations)", 4),
            ("Strasbourg - Saint-Denis via M4", "strasbourg-saint-denis", "M4", "M4 direction Bagneux (1 station)", 2)
        ]
    },
    "strasbourg-saint-denis": {
        "seo": "Station Strasbourg - Saint-Denis : M4 + M8 + M9 dans le 10e arr. À côté des Portes Saint-Denis et Saint-Martin (arcs triomphaux de Louis XIV). Hub central des grands boulevards.",
        "tagline": "M4 + M8 + M9 — Portes triomphales Louis XIV",
        "hero_desc": "Station <strong>Strasbourg - Saint-Denis</strong> dans le <strong>10e arrondissement</strong>, à l'intersection des boulevards Saint-Denis, Saint-Martin et Sébastopol. Desservie par <strong>3 lignes</strong> : <strong>M4</strong> (1908), <strong>M8</strong> (1931) et <strong>M9</strong> (1933). À 100 m : la <strong>Porte Saint-Denis</strong> (1672, arc triomphal de François Blondel pour Louis XIV) et la <strong>Porte Saint-Martin</strong> (1674, Pierre Bullet). Hub central des grands boulevards.",
        "intros": [
            "La station <strong>Strasbourg - Saint-Denis</strong> est située dans le <strong>10e arrondissement de Paris</strong>, à l'intersection des <strong>boulevards Saint-Denis, Saint-Martin et de Sébastopol</strong>. Elle est desservie par <strong>3 lignes</strong> : <strong>M4</strong> (Porte de Clignancourt ↔ Bagneux), <strong>M8</strong> (Balard ↔ Pointe du Lac), <strong>M9</strong> (Pont de Sèvres ↔ Mairie de Montreuil). Bus 20, 38, 39, 47.",
            "La station <strong>M4</strong> ouvre le <strong>21 avril 1908</strong> avec le tronçon originel. La <strong>M8</strong> est ajoutée le <strong>5 mai 1931</strong>, la <strong>M9</strong> le <strong>10 décembre 1933</strong>. Hub central commercial et de transit, au cœur des grands boulevards parisiens.",
            "À <strong>100 m</strong> : la <strong>Porte Saint-Denis</strong> (1672), arc triomphal commandé par <strong>Louis XIV</strong> à l'architecte <strong>François Blondel</strong> pour célébrer ses victoires sur le Rhin et en Hollande. À 200 m : la <strong>Porte Saint-Martin</strong> (1674), commandée à <strong>Pierre Bullet</strong> pour célébrer la prise de Besançon et la victoire de Cassel. Les 2 portes sont des <strong>vestiges des fortifications de Charles V</strong> (XIVᵉ), reconverties par Louis XIV en arcs de triomphe."
        ],
        "hist_title": "1672/1674 : 2 arcs triomphaux de Louis XIV, 1908-1933 : 3 lignes métro",
        "hist": [
            "À <strong>100 m</strong> de la station : la <strong>Porte Saint-Denis</strong>, arc triomphal érigé en <strong>1672</strong> par <strong>François Blondel</strong> pour célébrer les <strong>victoires de Louis XIV sur le Rhin</strong>. Hauteur : 24,65 m. Inscription : <em>« LUDOVICO MAGNO »</em> (« au grand Louis »). Premier monument érigé à Paris pour Louis XIV.",
            "À <strong>200 m</strong> : la <strong>Porte Saint-Martin</strong>, arc triomphal érigé en <strong>1674</strong> par <strong>Pierre Bullet</strong> pour célébrer la <strong>prise de Besançon et la victoire de Cassel</strong>. Hauteur : 18 m. Bas-reliefs : <em>« LUDOVICO MAGNO VESONTIONE SEQUANIS BIS CAPTIS »</em>. Plus petite et plus délicate que la Porte Saint-Denis.",
            "Les <strong>2 portes</strong> sont des <strong>vestiges des fortifications de Charles V</strong> (XIVᵉ siècle, enceinte fortifiée). Reconverties par Louis XIV en <strong>arcs de triomphe</strong> dans le cadre de sa politique d'embellissement de Paris (avec les Tuileries, les Champs-Élysées, etc.).",
            "Le métro arrive en <strong>3 étapes</strong> : <strong>M4 en 1908</strong> (tronçon originel), <strong>M8 en 1931</strong>, <strong>M9 en 1933</strong>. La station devient ainsi un <strong>hub central majeur du métro parisien</strong>, au cœur du quartier commercial des grands boulevards.",
            "Aujourd'hui, le quartier reste un <strong>pôle commercial actif</strong> : grands boulevards (Saint-Denis, Saint-Martin), passages couverts (passage Brady, passage du Prado), restaurants, théâtres. Affluence touristique modérée pour les portes triomphales et les passages couverts."
        ],
        "faq": [
            ("Quelles lignes desservent Strasbourg - Saint-Denis ?", "<strong>M4</strong> (1908), <strong>M8</strong> (1931), <strong>M9</strong> (1933). Bus 20, 38, 39, 47."),
            ("Où sont les Portes Saint-Denis et Saint-Martin ?", "<strong>Porte Saint-Denis</strong> à 100 m sur le boulevard Saint-Denis (1672, François Blondel). <strong>Porte Saint-Martin</strong> à 200 m sur le boulevard Saint-Martin (1674, Pierre Bullet). Vestiges des fortifications de Charles V reconvertis par Louis XIV en arcs triomphaux."),
            ("Comment aller à Châtelet ?", "<strong>M4 directe</strong> : ~6 min (3 stations vers le sud)."),
            ("Comment aller à République ?", "<strong>M9 directe</strong> : 1 station (2 min) OR à pied 5 min."),
            ("Quels sont les passages couverts proches ?", "<strong>Passage Brady</strong> (1828, restaurants indiens) à 5 min. <strong>Passage du Prado</strong> (1925) à 5 min. <strong>Galerie Vivienne</strong> (1823) à 15 min."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Stations historiques 1908-1933 : accessibilité PMR partielle.")
        ],
        "tips": [
            "<strong>Porte Saint-Denis et Saint-Martin</strong> à 100-200 m — arcs triomphaux Louis XIV.",
            "<strong>Passage Brady</strong> à 5 min — restaurants indiens.",
            "Pour <strong>République</strong> : M9 directe (1 station) ou 5 min à pied.",
            "Pour <strong>Châtelet</strong> : M4 directe (~6 min).",
            "Hub commercial — affluence forte heures de pointe."
        ],
        "trivia": [
            ("🏛️", "Porte Saint-Denis (1672) — premier monument Louis XIV à Paris", "À <strong>100 m</strong>, la <strong>Porte Saint-Denis</strong> est un <strong>arc triomphal</strong> érigé en <strong>1672</strong> par l'architecte <strong>François Blondel</strong> pour célébrer les <strong>victoires de Louis XIV sur le Rhin et en Hollande</strong>. Hauteur : <strong>24,65 m</strong>. Inscription : <em>« LUDOVICO MAGNO »</em> (« au grand Louis »). <strong>Premier monument érigé à Paris pour Louis XIV</strong>. Reconverti depuis un ancien vestige des fortifications de Charles V (XIVᵉ siècle)."),
            ("🚇", "Hub 3 lignes — M4 (1908), M8 (1931), M9 (1933)", "Strasbourg - Saint-Denis est l'un des <strong>hubs centraux du métro parisien</strong> avec <strong>3 lignes</strong> : <strong>M4</strong> (1908, tronçon originel Porte de Clignancourt ↔ Châtelet), <strong>M8</strong> (1931, Opéra ↔ Porte de Charenton), <strong>M9</strong> (1933, Trocadéro ↔ Porte de Saint-Cloud). Construction en 3 étapes sur 25 ans. Au cœur du quartier commercial des grands boulevards.")
        ],
        "itin": [
            ("Porte Saint-Denis", "porte-saint-denis", "à pied", "100 m direct", 2),
            ("Porte Saint-Martin", "porte-saint-martin", "à pied", "200 m direct", 3),
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Bagneux (3 stations)", 6),
            ("République via M9", "republique", "M9", "M9 direction Mairie de Montreuil (1 station)", 2),
            ("Passage Brady (restos indiens)", "passage-brady", "à pied", "5 min direct", 5),
            ("Bastille via M8", "bastille", "M8", "M8 direction Pointe du Lac", 12)
        ]
    },
    "reaumur-sebastopol": {
        "seo": "Station Réaumur - Sébastopol : M3 + M4 dans le 2e arr., cœur du Sentier (quartier mode et tech). Croisement historique des grands axes parisiens.",
        "tagline": "M3 + M4 — Sentier, quartier mode et tech",
        "hero_desc": "Station <strong>Réaumur - Sébastopol</strong> dans le <strong>2e arrondissement</strong>, à l'intersection de la <strong>rue Réaumur</strong> et du <strong>boulevard de Sébastopol</strong>. Desservie par <strong>M3</strong> (ouverte 19 octobre 1904) et <strong>M4</strong> (ouverte 21 avril 1908). Cœur du <strong>quartier du Sentier</strong>, historiquement <strong>capitale française du textile et de la mode</strong>, aujourd'hui également pôle <strong>tech parisien</strong> (start-ups).",
        "intros": [
            "La station <strong>Réaumur - Sébastopol</strong> est située dans le <strong>2e arrondissement de Paris</strong>, à l'intersection de la <strong>rue Réaumur</strong> et du <strong>boulevard de Sébastopol</strong>. Elle est desservie par <strong>2 lignes</strong> : <strong>M3</strong> (Pont de Levallois ↔ Gallieni) et <strong>M4</strong> (Porte de Clignancourt ↔ Bagneux - Lucie Aubrac). Bus 20, 38, 39, 47.",
            "La station <strong>M3</strong> ouvre le <strong>19 octobre 1904</strong> avec le tronçon Père Lachaise ↔ Villiers de la M3. La station <strong>M4</strong> est ajoutée le <strong>21 avril 1908</strong> avec le tronçon originel de la M4. Cas particulier : la station se nommait initialement <strong>« Rue Saint-Denis »</strong> sur la M3, renommée en 1907.",
            "Au cœur du <strong>quartier du Sentier</strong>, historiquement <strong>capitale française du textile et de la mode</strong> depuis le XIXᵉ siècle. Ateliers de confection, grossistes en tissus, boutiques de prêt-à-porter. Au XXIᵉ, le Sentier s'est diversifié vers le <strong>tech</strong> (start-ups internet, agences digitales, espaces de coworking). Surnommé <strong>« Silicon Sentier »</strong>."
        ],
        "hist_title": "1904 : M3, 1908 : M4, et le Sentier mode/tech",
        "hist": [
            "La station <strong>M3</strong> ouvre le <strong>19 octobre 1904</strong> avec le tronçon Père Lachaise ↔ Villiers. Initialement nommée <strong>« Rue Saint-Denis »</strong>, renommée <strong>« Réaumur - Sébastopol »</strong> en 1907.",
            "La station <strong>M4</strong> est ajoutée le <strong>21 avril 1908</strong> avec le tronçon originel de la M4 (Porte de Clignancourt ↔ Châtelet).",
            "Les noms : <strong>René-Antoine Ferchault de Réaumur</strong> (1683-1757), savant et naturaliste français, inventeur du thermomètre Réaumur. Le <strong>boulevard de Sébastopol</strong> commémore la <strong>bataille de Sébastopol</strong> (1854-1855) durant la guerre de Crimée — l'une des victoires de Napoléon III.",
            "Le quartier autour est le <strong>Sentier</strong>, historiquement <strong>capitale française du textile et de la mode</strong> depuis le XIXᵉ siècle. Concentration unique d'ateliers de confection, grossistes en tissus, boutiques de prêt-à-porter. Origine de nombreuses marques françaises : Tati, Mango, Etam, etc.",
            "Au XXIᵉ siècle, le Sentier se diversifie vers le <strong>tech parisien</strong>. Surnommé <strong>« Silicon Sentier »</strong> dans les années 2000 (Free, Deezer, Vente-Privée, Sarenza, BlaBlaCar) ont leurs sièges historiques dans le quartier ou à proximité. Le <strong>Numa</strong>, premier espace de coworking français (2008), était installé rue du Caire."
        ],
        "faq": [
            ("Quelles lignes desservent Réaumur - Sébastopol ?", "<strong>M3</strong> (1904) et <strong>M4</strong> (1908). Bus 20, 38, 39, 47."),
            ("Pourquoi le nom Réaumur ?", "De <strong>René-Antoine Ferchault de Réaumur</strong> (1683-1757), savant français, naturaliste et physicien, <strong>inventeur du thermomètre Réaumur</strong>. La rue Réaumur a été ouverte à la fin du XIXᵉ siècle."),
            ("Qu'est-ce que le Sentier ?", "Quartier du 2e arrondissement, historiquement <strong>capitale française du textile et de la mode</strong> depuis le XIXᵉ siècle. Au XXIᵉ : également pôle <strong>tech parisien</strong> (« Silicon Sentier ») avec Free, Deezer, Vente-Privée, BlaBlaCar."),
            ("Comment aller à Châtelet ?", "<strong>M4 directe</strong> : ~4 min (2 stations vers le sud)."),
            ("Comment aller à Opéra ?", "<strong>M3 directe</strong> : ~5 min (3 stations vers Pont de Levallois)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Stations historiques 1904/1908.")
        ],
        "tips": [
            "<strong>Sentier (quartier mode)</strong> à pied — explorer les ateliers et grossistes.",
            "Pour <strong>Opéra</strong> : M3 directe (~5 min).",
            "Pour <strong>Châtelet</strong> : M4 directe (~4 min).",
            "Pour <strong>République</strong> : M3 directe (~7 min).",
            "Quartier dense en boutiques de prêt-à-porter et textile."
        ],
        "trivia": [
            ("🌡️", "René-Antoine de Réaumur — inventeur du thermomètre Réaumur", "Le nom <strong>Réaumur</strong> vient de <strong>René-Antoine Ferchault de Réaumur</strong> (1683-1757), savant français polymorphe : <strong>physicien, naturaliste, métallurgiste</strong>. <strong>Inventeur du thermomètre Réaumur</strong> (échelle thermométrique 0-80°, où 0°R = 0°C = congélation eau et 80°R = 100°C = ébullition eau). Étudie aussi l'<strong>acier</strong>, les <strong>insectes</strong> (6 volumes de <em>Mémoires pour servir à l'histoire des insectes</em>). Membre de l'Académie des sciences. La rue Réaumur a été ouverte à la fin du XIXᵉ siècle."),
            ("💻", "Silicon Sentier — pôle tech parisien", "Le quartier du <strong>Sentier</strong>, capitale historique du textile, est devenu au XXIᵉ siècle un <strong>pôle tech parisien</strong>, surnommé <strong>« Silicon Sentier »</strong>. Sièges historiques de start-ups françaises : <strong>Free</strong> (Xavier Niel), <strong>Deezer</strong>, <strong>Vente-Privée</strong> (Veepee), <strong>Sarenza</strong>, <strong>BlaBlaCar</strong>. Le <strong>Numa</strong>, premier espace de coworking français (2008), était installé rue du Caire. Symbole de l'<strong>écosystème tech parisien</strong> émergent au cœur d'un quartier historiquement industriel.")
        ],
        "itin": [
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Bagneux (2 stations)", 4),
            ("Opéra via M3", "opera", "M3", "M3 direction Pont de Levallois", 7),
            ("République via M3", "republique", "M3", "M3 direction Gallieni", 7),
            ("Gare du Nord via M4", "gare-du-nord", "M4", "M4 direction Porte de Clignancourt (3 stations)", 6),
            ("Sentier (quartier mode)", "sentier", "à pied", "Sortie directe", 1),
            ("Saint-Michel via M4", "saint-michel", "M4", "M4 direction Bagneux (4 stations)", 8)
        ]
    },
    "etienne-marcel": {
        "seo": "Station Étienne Marcel : M4 dans le 2e arr., tour Jean-sans-Peur (vestige médiéval rare). Sentier quartier mode à proximité.",
        "tagline": "M4 — Tour Jean-sans-Peur (vestige médiéval)",
        "hero_desc": "Station <strong>Étienne Marcel</strong> ouverte le <strong>21 avril 1908</strong> avec la M4 originelle. Située dans le <strong>2e arrondissement</strong>, à l'intersection des rues Étienne-Marcel et de Turbigo. À <strong>200 m</strong> : la <strong>Tour Jean-sans-Peur</strong> (1408-1411), l'un des très rares <strong>vestiges médiévaux du Paris civil</strong>, ancienne tour-donjon des ducs de Bourgogne.",
        "intros": [
            "La station <strong>Étienne Marcel</strong> est située dans le <strong>2e arrondissement de Paris</strong>, à l'intersection des <strong>rues Étienne-Marcel et de Turbigo</strong>. Elle est desservie uniquement par la <strong>M4</strong> (Porte de Clignancourt ↔ Bagneux), entre <strong>Réaumur-Sébastopol</strong> (1 station nord, M3+M4) et <strong>Les Halles</strong> (1 station sud, hub méga RER A/B/D + M1/M7/M11/M14). Bus 29, 38.",
            "Ouverte le <strong>21 avril 1908</strong> avec le tronçon originel de la M4 (Porte de Clignancourt ↔ Châtelet). Le nom <strong>« Étienne Marcel »</strong> commémore <strong>Étienne Marcel</strong> (1302-1358), <strong>prévôt des marchands de Paris</strong> (équivalent maire au Moyen Âge), figure majeure de la révolte parisienne contre le pouvoir royal en 1357-1358.",
            "À <strong>200 m</strong> : la <strong>Tour Jean-sans-Peur</strong> (1408-1411), l'un des <strong>très rares vestiges médiévaux du Paris civil</strong>. Ancienne tour-donjon des <strong>ducs de Bourgogne</strong>, construite par <strong>Jean Sans Peur</strong> (duc de Bourgogne, oncle de Charles VI) pour se protéger après l'assassinat de Louis d'Orléans (frère du roi) en 1407. Tour de 27 m de haut, structure militaire médiévale rare à Paris."
        ],
        "hist_title": "Étienne Marcel (1358) et Tour Jean-sans-Peur (1411)",
        "hist": [
            "La station <strong>M4</strong> ouvre le <strong>21 avril 1908</strong> avec le tronçon originel de la M4 (Porte de Clignancourt ↔ Châtelet).",
            "Le nom <strong>Étienne Marcel</strong> commémore <strong>Étienne Marcel</strong> (1302-1358), <strong>prévôt des marchands de Paris</strong> (équivalent maire au Moyen Âge). Figure majeure de la <strong>révolte parisienne</strong> contre le pouvoir royal en 1357-1358 sous Charles V (alors dauphin Charles), durant les troubles de la Jacquerie. Tué le 31 juillet 1358 par les royalistes lors de la reprise de Paris. Considéré comme l'un des premiers <strong>défenseurs des libertés municipales parisiennes</strong>.",
            "À <strong>200 m</strong> de la station : la <strong>Tour Jean-sans-Peur</strong>, l'un des <strong>très rares vestiges médiévaux du Paris civil</strong>. Construite entre <strong>1408 et 1411</strong> par <strong>Jean Sans Peur</strong> (duc de Bourgogne 1371-1419, oncle de Charles VI), pour se protéger après l'assassinat de <strong>Louis d'Orléans</strong> (frère du roi) en 1407 — assassinat commandité par Jean Sans Peur lui-même.",
            "<strong>Tour de 27 mètres de haut</strong>, structure militaire médiévale rare à Paris (la plupart des fortifications médiévales civiles ont été détruites au XIXᵉ par Haussmann). Située dans la cour de l'<strong>hôtel d'Artois</strong> (siège bourguignon à Paris). <strong>Voûte d'escalier en spirale</strong> en pierre, décor sculpté représentant le <strong>chêne, l'aubépine et le houblon</strong> — symboles bourguignons. Ouverte au public comme musée historique.",
            "Aujourd'hui, le quartier autour de la station est partagé entre le <strong>Sentier</strong> (mode, tech) et le secteur historique parisien. Boutiques de prêt-à-porter, ateliers, cafés."
        ],
        "faq": [
            ("Quelle ligne dessert Étienne Marcel ?", "Uniquement la <strong>M4</strong>. Bus 29, 38."),
            ("Qui est Étienne Marcel ?", "<strong>Étienne Marcel</strong> (1302-1358), <strong>prévôt des marchands de Paris</strong> (maire) au Moyen Âge. Figure de la révolte parisienne contre le pouvoir royal en 1357-1358 (Jacquerie). Tué le 31 juillet 1358 par les royalistes. Considéré comme l'un des premiers défenseurs des <strong>libertés municipales parisiennes</strong>."),
            ("Où est la Tour Jean-sans-Peur ?", "<strong>200 m</strong> de la station. Construite 1408-1411 par <strong>Jean Sans Peur</strong>, duc de Bourgogne. <strong>27 m de haut</strong>, ancienne tour-donjon. L'un des très rares vestiges médiévaux du Paris civil. Ouverte au public comme musée."),
            ("Comment aller à Châtelet ?", "<strong>M4 directe</strong> : ~3 min (2 stations vers le sud)."),
            ("Comment aller à Saint-Michel ?", "<strong>M4 directe</strong> : ~6 min (4 stations vers le sud)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. M4 historique 1908.")
        ],
        "tips": [
            "<strong>Tour Jean-sans-Peur</strong> à 200 m — musée historique, vestige médiéval rare.",
            "<strong>Sentier (quartier mode)</strong> à 5 min.",
            "Pour <strong>Châtelet</strong> : M4 directe (~3 min).",
            "Pour <strong>Les Halles</strong> : M4 directe (1 station).",
            "Quartier mixte commerce/historique."
        ],
        "trivia": [
            ("⚔️", "Étienne Marcel — révolté parisien (1358)", "<strong>Étienne Marcel</strong> (1302-1358), <strong>prévôt des marchands de Paris</strong> (équivalent maire au Moyen Âge), est l'une des figures les plus marquantes de l'histoire municipale parisienne. <strong>Leader de la révolte parisienne</strong> contre le pouvoir royal en 1357-1358 sous Charles V (alors dauphin), durant les troubles de la Jacquerie. <strong>Tué le 31 juillet 1358</strong> par les royalistes lors de la reprise de Paris. Considéré comme l'un des premiers <strong>défenseurs des libertés municipales</strong>. Statue équestre devant l'Hôtel de Ville de Paris."),
            ("🏰", "Tour Jean-sans-Peur (1411) — vestige médiéval rare", "À <strong>200 m</strong> de la station, la <strong>Tour Jean-sans-Peur</strong> (1408-1411) est l'un des <strong>très rares vestiges médiévaux du Paris civil</strong>. Construite par <strong>Jean Sans Peur</strong> (duc de Bourgogne 1371-1419), oncle de Charles VI, pour se protéger après l'<strong>assassinat de Louis d'Orléans</strong> (frère du roi) en 1407 — meurtre commandité par Jean Sans Peur lui-même. <strong>Tour de 27 m</strong>, voûte d'escalier en spirale, décor sculpté de chênes, aubépines et houblons (symboles bourguignons). Musée historique ouvert au public.")
        ],
        "itin": [
            ("Tour Jean-sans-Peur", "tour-jean-sans-peur", "à pied", "200 m direct", 3),
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Bagneux (2 stations)", 3),
            ("Les Halles via M4", "les-halles", "M4", "M4 direction Bagneux (1 station)", 2),
            ("Saint-Michel via M4", "saint-michel", "M4", "M4 direction Bagneux (4 stations)", 6),
            ("Sentier (mode)", "sentier", "à pied", "5 min nord", 5),
            ("Gare du Nord via M4", "gare-du-nord", "M4", "M4 direction Porte de Clignancourt (4 stations)", 8)
        ]
    },
    "les-halles": {
        "seo": "Station Les Halles : M4 dans le 1er arr., Forum des Halles, Saint-Eustache, Bourse de Commerce. Hub mégastation Châtelet-Les Halles le plus important d'Europe.",
        "tagline": "M4 — Forum des Halles, hub majeur du centre Paris",
        "hero_desc": "Station <strong>Les Halles</strong> ouverte le <strong>21 avril 1908</strong> avec la M4 originelle. Située dans le <strong>1er arrondissement</strong>, sous le <strong>Forum des Halles</strong>. Correspondance par voirie avec <strong>Châtelet - Les Halles</strong> (RER A + RER B + RER D, mega-hub le plus important d'Europe). À 100 m : <strong>Forum des Halles</strong> (centre commercial 1979, rénové 2016), <strong>Saint-Eustache</strong> (église gothique-Renaissance), <strong>Bourse de Commerce</strong> (Pinault Collection 2021).",
        "intros": [
            "La station <strong>Les Halles</strong> est située dans le <strong>1er arrondissement de Paris</strong>, sous le <strong>Forum des Halles</strong>. Elle est desservie par la <strong>M4</strong> (Porte de Clignancourt ↔ Bagneux). Correspondance par voirie (200 m) avec <strong>Châtelet - Les Halles</strong> (RER A + RER B + RER D, M1 + M7 + M11 + M14 à Châtelet adjacent) — <strong>hub méga le plus important d'Europe</strong> en correspondance. Bus 38, 67.",
            "Ouverte le <strong>21 avril 1908</strong> avec le tronçon originel de la M4 (Porte de Clignancourt ↔ Châtelet). Le quartier des <strong>Halles centrales de Paris</strong> a une histoire millénaire : marché alimentaire principal de Paris depuis le <strong>XIIᵉ siècle</strong>, jusqu'au <strong>transfert vers Rungis en 1969</strong>. Les anciennes Halles Baltard (1854-1973) ont été démolies pour faire place au <strong>Forum des Halles</strong> (1979).",
            "À proximité directe : le <strong>Forum des Halles</strong> (centre commercial souterrain ouvert 1979, rénové 2010-2016 par Berger & Anziutti), l'<strong>église Saint-Eustache</strong> (1532-1632, gothique-Renaissance, l'une des plus grandes de Paris), la <strong>Bourse de Commerce - Pinault Collection</strong> (édifice 1763-1889 par Bélanger, transformé en musée d'art contemporain en 2021 par Tadao Andō), et la <strong>Canopée des Halles</strong> (toiture caractéristique 2016)."
        ],
        "hist_title": "Les Halles centrales (XIIᵉ-1969), Forum (1979), rénovation (2016)",
        "hist": [
            "Le <strong>quartier des Halles</strong> a été le <strong>marché alimentaire principal de Paris depuis le XIIᵉ siècle</strong>. Établi par le roi <strong>Louis VI le Gros</strong> en 1135 sur l'emplacement actuel. Lieu central de l'approvisionnement parisien pendant <strong>800 ans</strong> : <em>« le ventre de Paris »</em> selon Émile Zola dans son roman éponyme (1873).",
            "Au XIXᵉ siècle, l'architecte <strong>Victor Baltard</strong> conçoit les <strong>12 pavillons en fonte et verre</strong> (1854-1874), considérés comme <strong>chef-d'œuvre de l'architecture industrielle</strong>. Les Halles Baltard fonctionnent jusqu'en <strong>1969</strong>, où le marché est <strong>transféré à Rungis</strong> (sous De Gaulle / Pompidou) pour des raisons d'hygiène et de circulation.",
            "<strong>1971-1973</strong> : démolition des pavillons Baltard (très contestée, vue rétrospectivement comme erreur urbanistique). Seul un pavillon est <strong>démonté et reconstruit à Nogent-sur-Marne</strong> (préservation). <strong>Polémique nationale</strong>.",
            "<strong>1979</strong> : ouverture du <strong>Forum des Halles</strong> (centre commercial souterrain, ~150 boutiques). Conception : Claude Vasconi et Georges Pencreac'h. <strong>2010-2016</strong> : rénovation complète par <strong>Berger & Anziutti</strong>. Nouvelle toiture iconique : la <strong>Canopée</strong> (acier+verre, 18 000 m², 14 m de haut). Surface totale : ~75 000 m².",
            "La station <strong>M4</strong> a été inaugurée le <strong>21 avril 1908</strong>. Elle est reliée par voirie (200 m) à la station <strong>Châtelet - Les Halles</strong> (RER A 1977, RER B 1981, RER D 1995) — <strong>hub méga le plus important d'Europe</strong> en correspondance (~750 000 voyageurs/jour, 9 lignes : M1, M4, M7, M11, M14 + RER A, B, D)."
        ],
        "faq": [
            ("Quelle ligne dessert Les Halles ?", "Uniquement la <strong>M4</strong>. Correspondance voirie (200 m) avec <strong>Châtelet - Les Halles</strong> (RER A + RER B + RER D) et Châtelet adjacent (M1 + M7 + M11 + M14). <strong>Mega-hub le plus important d'Europe</strong>."),
            ("Qu'est-ce que le Forum des Halles ?", "<strong>Centre commercial souterrain</strong> ouvert en <strong>1979</strong> (Claude Vasconi, Georges Pencreac'h) sur l'emplacement des anciennes Halles centrales transférées à Rungis en 1969. Rénovation complète <strong>2010-2016</strong> par <strong>Berger & Anziutti</strong> : nouvelle <strong>Canopée</strong> iconique (acier+verre, 18 000 m²)."),
            ("Qu'est-ce que la Bourse de Commerce ?", "Édifice <strong>1763-1889</strong> (Bélanger) sur l'ancien hôtel de Soissons. Transformé en <strong>musée d'art contemporain</strong> par <strong>Tadao Andō</strong> (architecte japonais) et inauguré en <strong>2021</strong> comme <strong>Bourse de Commerce - Pinault Collection</strong>. Collection d'art contemporain de François Pinault. À 100 m de la station."),
            ("Où est Saint-Eustache ?", "<strong>Église Saint-Eustache</strong> à 100 m, l'une des plus grandes de Paris. Construite <strong>1532-1632</strong> dans un style <strong>gothique-Renaissance</strong>. Mariages historiques : <strong>Louis XIV baptisé ici</strong> (1638), <strong>Richelieu baptisé ici</strong> (1585), <strong>Molière baptisé ici</strong> (1622). Concerts d'orgue réputés."),
            ("Comment aller à Saint-Michel ?", "<strong>M4 directe</strong> : ~5 min (3 stations vers le sud)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>. Forum des Halles entièrement PMR ; quais M4 partiellement accessibles via ascenseurs.")
        ],
        "tips": [
            "<strong>Forum des Halles</strong> (~150 boutiques) à la sortie directe.",
            "<strong>Canopée des Halles</strong> à voir — toiture iconique 2016.",
            "<strong>Saint-Eustache</strong> à 100 m — église historique (baptême Louis XIV, Molière, Richelieu).",
            "<strong>Bourse de Commerce - Pinault Collection</strong> à 200 m — art contemporain Tadao Andō.",
            "Pour <strong>Châtelet</strong> : M4 directe (1 station) OU voirie 200 m."
        ],
        "trivia": [
            ("🥬", "Le ventre de Paris (XIIᵉ-1969)", "Le <strong>quartier des Halles</strong> a été le <strong>marché alimentaire principal de Paris depuis le XIIᵉ siècle</strong>. Établi par <strong>Louis VI le Gros</strong> en 1135. <em>« Le ventre de Paris »</em> selon Émile Zola dans son roman éponyme (1873). <strong>12 pavillons Baltard</strong> (1854-1874), chef-d'œuvre architecture industrielle. <strong>Transfert à Rungis en 1969</strong> sous De Gaulle / Pompidou. <strong>Démolition 1971-1973</strong> (un seul pavillon préservé, démonté à Nogent-sur-Marne). <strong>Forum des Halles 1979</strong>, rénové 2016."),
            ("⛪", "Saint-Eustache (1532-1632) — baptême Louis XIV, Molière", "L'<strong>église Saint-Eustache</strong> à 100 m est l'une des plus grandes de Paris (105 m de long, 44 m de haut). Construite <strong>1532-1632</strong> dans un style <strong>gothique-Renaissance</strong> unique. Baptisés ici : <strong>Louis XIV</strong> (1638), <strong>Molière</strong> (1622), <strong>Richelieu</strong> (1585), <strong>Madame de Pompadour</strong> (1721). Mariage de <strong>Lully</strong> ici (1662). <strong>Orgue Ducroquet</strong> (1854) parmi les plus grands de France, concerts réputés. Tombeau de Colbert.")
        ],
        "itin": [
            ("Forum des Halles", "forum-des-halles", "à pied", "Sortie directe", 1),
            ("Saint-Eustache", "saint-eustache", "à pied", "100 m direct", 2),
            ("Bourse de Commerce Pinault", "bourse-commerce-pinault", "à pied", "200 m direct", 3),
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Bagneux (1 station)", 2),
            ("Châtelet-Les Halles RER A/B/D", "chatelet-les-halles", "à pied", "Voirie 200 m", 3),
            ("Saint-Michel via M4", "saint-michel", "M4", "M4 direction Bagneux (3 stations)", 5)
        ]
    },
}

# Partie 2 : 7 stations restantes (saint-michel, saint-sulpice, saint-placide, raspail, alesia, mairie-de-montrouge, bagneux-lucie-aubrac)
CONTENT.update({
    "saint-michel": {
        "seo": "Station Saint-Michel : M4 dans le 6e arr., correspondance RER B et RER C par la gare Saint-Michel - Notre-Dame. Quartier Latin, Sorbonne, fontaine Saint-Michel, Sainte-Chapelle proche.",
        "tagline": "M4 + RER B + RER C — Quartier Latin, Notre-Dame, Sorbonne",
        "hero_desc": "Station <strong>Saint-Michel</strong> ouverte le <strong>9 janvier 1910</strong> avec le prolongement M4 sous la Seine. Située dans le <strong>6e arrondissement</strong>, à la <strong>place Saint-Michel</strong> sur la rive gauche. Correspondance par voirie avec la gare RER <strong>Saint-Michel - Notre-Dame</strong> (RER B + RER C). Cœur du <strong>Quartier Latin</strong> : <strong>fontaine Saint-Michel</strong> (1860), accès à la <strong>Sorbonne</strong>, <strong>Notre-Dame de Paris</strong> sur la rive opposée, <strong>Sainte-Chapelle</strong>, <strong>Saint-Séverin</strong>.",
        "intros": [
            "La station <strong>Saint-Michel</strong> est située dans le <strong>6e arrondissement de Paris</strong>, sur la <strong>place Saint-Michel</strong>, rive gauche de la Seine. Elle est desservie par la <strong>M4</strong> (Porte de Clignancourt ↔ Bagneux). Correspondance par voirie (50 m) avec la gare RER <strong>Saint-Michel - Notre-Dame</strong> (<strong>RER B + RER C</strong>). Bus 21, 27, 38, 85, 96.",
            "Ouverte le <strong>9 janvier 1910</strong> avec le <strong>prolongement de la M4 sous la Seine</strong> (Châtelet → Cité → Saint-Michel → Vavin). Cette traversée sous-fluviale a été réalisée par la <strong>technique d'immersion de caissons</strong> — première mondiale à l'époque pour un tunnel de métro.",
            "Au cœur du <strong>Quartier Latin</strong>, l'un des quartiers étudiants les plus emblématiques de Paris. À la sortie : la <strong>fontaine Saint-Michel</strong> (1860, Gabriel Davioud, sculpture archange Michel terrassant le démon), point de ralliement touristique majeur. À 200-500 m : <strong>Notre-Dame de Paris</strong> (rive opposée, île de la Cité), <strong>Sainte-Chapelle</strong>, <strong>Conciergerie</strong>, <strong>Saint-Séverin</strong>, <strong>Cluny-La Sorbonne</strong>, et accès au quartier piéton de la <strong>rue de la Huchette</strong>."
        ],
        "hist_title": "1910 : la traversée sous-fluviale, et la fontaine Saint-Michel",
        "hist": [
            "La station <strong>Saint-Michel</strong> est inaugurée le <strong>9 janvier 1910</strong> avec le <strong>prolongement de la M4 sous la Seine</strong> (Châtelet ↔ Vavin via Cité, Saint-Michel, Odéon, Saint-Sulpice, Saint-Placide, Montparnasse).",
            "<strong>Première mondiale technique</strong> : la <strong>traversée sous-fluviale</strong> de la Seine a été réalisée par la <strong>technique d'immersion de caissons sous-fluviaux</strong>. 5 caissons en béton ont été préfabriqués en surface puis immergés dans le lit du fleuve pour former le tunnel. Innovation majeure de l'ingénieur <strong>Fulgence Bienvenüe</strong>, « père du métro parisien ».",
            "La <strong>fontaine Saint-Michel</strong> à la sortie de la station est l'une des plus reconnaissables de Paris. Construite en <strong>1860</strong> par l'architecte <strong>Gabriel Davioud</strong> (auteur des fontaines Davioud) avec sculpture de <strong>Francisque Joseph Duret</strong> représentant <strong>l'archange saint Michel terrassant le démon</strong>. Hauteur totale : 26 m. Façade en pierre rouge des Vosges et bronze.",
            "Le <strong>Quartier Latin</strong> autour est l'un des plus anciens quartiers étudiants d'Europe. Université de Paris (Sorbonne) fondée au <strong>XIIIᵉ siècle</strong>. <strong>Quartier des étudiants en latin</strong> (langue d'enseignement universitaire), d'où le nom. Aujourd'hui : <strong>Sorbonne</strong>, <strong>Collège de France</strong>, <strong>Cluny</strong>, <strong>École Polytechnique historique</strong>, nombreuses librairies (Joseph Gibert, etc.).",
            "Touristique majeur : <strong>Notre-Dame de Paris</strong> à 200 m sur la rive opposée (incendiée 15 avril 2019, rouverte 7 décembre 2024), <strong>Sainte-Chapelle</strong> (1248), <strong>Conciergerie</strong>, <strong>Saint-Séverin</strong> (XIIIᵉ-XVᵉ), <strong>Saint-Julien-le-Pauvre</strong> (XIIᵉ, plus ancienne église de Paris), Saint-Michel est l'un des accès les plus utilisés au cœur historique."
        ],
        "faq": [
            ("Quelles lignes desservent Saint-Michel ?", "<strong>M4</strong> + correspondance RER B + RER C via la gare RER <strong>Saint-Michel - Notre-Dame</strong> à 50 m. Bus 21, 27, 38, 85, 96."),
            ("Comment aller à Notre-Dame ?", "<strong>5 min à pied</strong> en traversant le Petit-Pont vers l'île de la Cité. Notre-Dame réouverte le <strong>7 décembre 2024</strong> après l'incendie du 15 avril 2019."),
            ("Où est la Sainte-Chapelle ?", "<strong>10 min à pied</strong> sur l'île de la Cité. <strong>Sainte-Chapelle</strong> (1248), chef-d'œuvre du gothique rayonnant commandé par Saint Louis. Vitraux exceptionnels (~15 m de haut)."),
            ("Comment aller à la Sorbonne ?", "<strong>10 min à pied</strong> direction sud (rue Saint-Jacques)."),
            ("Comment aller à Châtelet ?", "<strong>M4 directe</strong> : 1 station vers le nord (~3 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>. M4 historique 1910 : ascenseurs partiels. Gare RER plus accessible.")
        ],
        "tips": [
            "<strong>Notre-Dame de Paris</strong> à 5 min — réouverte décembre 2024.",
            "<strong>Sainte-Chapelle</strong> à 10 min — vitraux exceptionnels.",
            "<strong>Sorbonne</strong> à 10 min — accès Quartier Latin.",
            "<strong>Fontaine Saint-Michel</strong> à la sortie — point de ralliement.",
            "<strong>Librairies Gibert</strong> au boulevard Saint-Michel."
        ],
        "trivia": [
            ("⛪", "Traversée sous la Seine par caissons immergés (1910)", "Le <strong>prolongement de la M4 sous la Seine</strong>, inauguré le <strong>9 janvier 1910</strong>, est une <strong>première mondiale technique</strong>. La <strong>traversée sous-fluviale</strong> a été réalisée par la <strong>technique d'immersion de caissons</strong> : 5 caissons en béton ont été préfabriqués en surface puis immergés dans le lit du fleuve pour former le tunnel. Innovation majeure de l'ingénieur <strong>Fulgence Bienvenüe</strong> (1852-1936), « père du métro parisien ». Technique reprise depuis dans le monde entier (tunnel Eurotunnel inclus partiellement)."),
            ("🗡️", "Fontaine Saint-Michel (1860) — archange terrassant le démon", "À la sortie de la station, la <strong>fontaine Saint-Michel</strong> est l'une des plus reconnaissables de Paris. Construite en <strong>1860</strong> par l'architecte <strong>Gabriel Davioud</strong> (auteur de plusieurs fontaines parisiennes haussmanniennes). Sculpture centrale de <strong>Francisque Joseph Duret</strong> représentant <strong>l'archange saint Michel terrassant le démon</strong>. <strong>26 m de haut</strong>. Façade en pierre rouge des Vosges et bronze. Point de ralliement touristique et étudiant emblématique du Quartier Latin.")
        ],
        "itin": [
            ("Notre-Dame de Paris", "notre-dame", "à pied", "5 min via Petit-Pont", 5),
            ("Sainte-Chapelle", "sainte-chapelle", "à pied", "10 min île de la Cité", 10),
            ("Sorbonne", "sorbonne", "à pied", "10 min sud rue Saint-Jacques", 10),
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Porte de Clignancourt (1 station)", 3),
            ("Saint-Germain-des-Prés via M4", "saint-germain-des-pres", "M4", "M4 direction Bagneux (2 stations)", 4),
            ("Aéroport CDG via RER B", "cdg-aeroport", "RER B", "Gare RER + RER B direct CDG", 35)
        ]
    },
    "saint-sulpice": {
        "seo": "Station Saint-Sulpice : M4 dans le 6e arr. Église Saint-Sulpice (2e plus grande de Paris), place Saint-Sulpice avec fontaine Visconti, Da Vinci Code.",
        "tagline": "M4 — Église Saint-Sulpice (2e plus grande de Paris)",
        "hero_desc": "Station <strong>Saint-Sulpice</strong> ouverte le <strong>9 janvier 1910</strong> avec le prolongement M4. Située dans le <strong>6e arrondissement</strong>, près de la <strong>place Saint-Sulpice</strong>. À 200 m : l'<strong>église Saint-Sulpice</strong> (1646-1745), <strong>2ᵉ plus grande église de Paris</strong> après Notre-Dame. <strong>Fontaine Visconti</strong> (1844) au centre de la place. <strong>Da Vinci Code</strong> de Dan Brown (2003) a popularisé le sujet du gnomon de Saint-Sulpice.",
        "intros": [
            "La station <strong>Saint-Sulpice</strong> est située dans le <strong>6e arrondissement de Paris</strong>, sous la <strong>rue du Vieux-Colombier</strong> à proximité de la <strong>place Saint-Sulpice</strong>. Elle est desservie uniquement par la <strong>M4</strong>, entre <strong>Saint-Germain-des-Prés</strong> (1 station nord) et <strong>Saint-Placide</strong> (1 station sud). Bus 39, 58, 63, 70, 84, 87, 96.",
            "Ouverte le <strong>9 janvier 1910</strong> avec le prolongement de la M4 sous la Seine (Châtelet ↔ Vavin).",
            "À <strong>200 m</strong> : l'<strong>église Saint-Sulpice</strong>, <strong>2ᵉ plus grande église de Paris</strong> après Notre-Dame. Construction sur <strong>plus d'un siècle</strong> (1646-1745) par plusieurs architectes successifs (Christophe Gamard, Louis Le Vau, Daniel Gittard, Gilles-Marie Oppenord, Giovanni Servandoni). <strong>Façade asymétrique</strong> (tours différentes). <strong>~113 m de long, 58 m de large, 33 m de haut</strong>. <strong>Place Saint-Sulpice</strong> avec la <strong>fontaine Visconti</strong> (1844) au centre."
        ],
        "hist_title": "1646-1745 : un siècle pour construire la 2ᵉ église de Paris",
        "hist": [
            "La station <strong>M4</strong> ouvre le <strong>9 janvier 1910</strong> avec le prolongement de la M4 sous la Seine (Châtelet ↔ Vavin via la traversée sous-fluviale).",
            "L'<strong>église Saint-Sulpice</strong>, à 200 m, est la <strong>2ᵉ plus grande église de Paris</strong> après Notre-Dame de Paris. Construction sur <strong>plus d'un siècle</strong> (1646-1745) par plusieurs architectes successifs : <strong>Christophe Gamard</strong> (début), <strong>Louis Le Vau</strong> (jusqu'en 1670), <strong>Daniel Gittard</strong>, <strong>Gilles-Marie Oppenord</strong>, <strong>Giovanni Servandoni</strong> (façade 1733-1745).",
            "Caractéristiques : <strong>113 m de long, 58 m de large, 33 m de haut</strong>. <strong>Façade asymétrique</strong> due aux tours inégales (tour nord par Servandoni inachevée, tour sud par Maclaurin 1788). Style classique français à l'antique.",
            "Intérieur célèbre : <strong>orgue Cavaillé-Coll (1862)</strong>, l'un des plus grands de France (102 jeux, 6 588 tuyaux). <strong>Fresques de Delacroix</strong> dans la chapelle des Saints-Anges (1855-1861) : <em>« Le combat de Jacob avec l'ange »</em> et <em>« Héliodore chassé du Temple »</em>. <strong>Gnomon de Saint-Sulpice</strong> (1727, méridienne) — popularisé mondialement par le roman <strong>Da Vinci Code de Dan Brown (2003)</strong>.",
            "<strong>Place Saint-Sulpice</strong> avec la <strong>fontaine Visconti</strong> (1844, Louis Visconti, sculpture des 4 cardinaux Bossuet, Fénelon, Massillon, Fléchier). Place réaménagée en zone semi-piétonne. Quartier prisé : librairies, cafés (Café de la Mairie), boutiques mode et déco haut de gamme."
        ],
        "faq": [
            ("Quelle ligne dessert Saint-Sulpice ?", "Uniquement la <strong>M4</strong>. Bus 39, 58, 63, 70, 84, 87, 96."),
            ("Qu'est-ce que l'église Saint-Sulpice ?", "<strong>2ᵉ plus grande église de Paris</strong> après Notre-Dame. Construite <strong>1646-1745</strong> par plusieurs architectes (Gamard, Le Vau, Gittard, Oppenord, Servandoni). <strong>113 m de long, 58 m de large</strong>. Façade asymétrique. Orgue Cavaillé-Coll (1862) parmi les plus grands de France."),
            ("C'est l'église du Da Vinci Code ?", "<strong>Oui, partiellement</strong>. Le roman <strong>Da Vinci Code</strong> (Dan Brown, 2003) met en scène le <strong>gnomon de Saint-Sulpice</strong> (1727, méridienne pour calculer l'équinoxe). Le roman a popularisé l'église dans le monde entier. Une plaque dans l'église précise que l'intrigue du roman est fictionnelle."),
            ("Où sont les fresques de Delacroix ?", "Dans la <strong>chapelle des Saints-Anges</strong> de l'église. Réalisées par <strong>Eugène Delacroix</strong> entre <strong>1855 et 1861</strong> : <em>« Le combat de Jacob avec l'ange »</em> et <em>« Héliodore chassé du Temple »</em>. Chefs-d'œuvre du romantisme français."),
            ("Comment aller à Saint-Germain-des-Prés ?", "<strong>M4 directe</strong> : 1 station vers le nord (~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. M4 historique 1910.")
        ],
        "tips": [
            "<strong>Église Saint-Sulpice</strong> à 200 m — 2e plus grande de Paris.",
            "<strong>Fresques Delacroix</strong> dans la chapelle des Saints-Anges.",
            "<strong>Fontaine Visconti</strong> sur la place — réaménagement piéton.",
            "Pour <strong>Saint-Germain-des-Prés</strong> : M4 directe (1 station).",
            "Cafés et boutiques mode/déco haut de gamme du 6e."
        ],
        "trivia": [
            ("⛪", "Église Saint-Sulpice — 2ᵉ plus grande de Paris", "L'<strong>église Saint-Sulpice</strong> à 200 m est la <strong>2ᵉ plus grande église de Paris</strong> après Notre-Dame. Construite sur <strong>plus d'un siècle (1646-1745)</strong> par plusieurs architectes successifs. <strong>113 m de long, 58 m de large, 33 m de haut</strong>. <strong>Façade asymétrique</strong> caractéristique : tours inégales (tour sud achevée par Maclaurin en 1788, tour nord inachevée). Intérieur : <strong>orgue Cavaillé-Coll (1862)</strong> parmi les plus grands de France (102 jeux, 6 588 tuyaux), <strong>fresques d'Eugène Delacroix</strong> dans la chapelle des Saints-Anges (1855-1861)."),
            ("🔍", "Gnomon de Saint-Sulpice (1727) — Da Vinci Code", "Le <strong>gnomon de Saint-Sulpice</strong>, méridienne installée en <strong>1727</strong>, est devenu mondialement célèbre grâce au <strong>roman Da Vinci Code de Dan Brown (2003)</strong>. La méridienne traverse l'église nord-sud, marquée par une ligne de cuivre au sol, et permettait de calculer l'équinoxe (date de Pâques) à partir de la position du soleil. Le roman fictionnalise cet objet comme « ligne rose ». Une plaque dans l'église précise que l'intrigue du roman est fictionnelle. Le succès du roman a multiplié les visites touristiques.")
        ],
        "itin": [
            ("Église Saint-Sulpice", "saint-sulpice-eglise", "à pied", "200 m direct", 3),
            ("Place Saint-Sulpice (fontaine Visconti)", "place-saint-sulpice", "à pied", "200 m direct", 3),
            ("Saint-Germain-des-Prés via M4", "saint-germain-des-pres", "M4", "M4 direction Porte de Clignancourt (1 station)", 2),
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Porte de Clignancourt (4 stations)", 8),
            ("Montparnasse via M4", "montparnasse-bienvenue", "M4", "M4 direction Bagneux (3 stations)", 6),
            ("Saint-Michel via M4", "saint-michel", "M4", "M4 direction Porte de Clignancourt (2 stations)", 4)
        ]
    },
    "saint-placide": {
        "seo": "Station Saint-Placide : M4 dans le 6e arr., Le Bon Marché (1er grand magasin moderne au monde, 1852). Quartier prisé rive gauche.",
        "tagline": "M4 — Le Bon Marché (1er grand magasin moderne 1852)",
        "hero_desc": "Station <strong>Saint-Placide</strong> ouverte le <strong>9 janvier 1910</strong> avec le prolongement M4. Située dans le <strong>6e arrondissement</strong>, sous la <strong>rue de Rennes</strong>. À <strong>5 min</strong> : <strong>Le Bon Marché Rive Gauche</strong> (1852), <strong>premier grand magasin moderne au monde</strong>, créé par Aristide Boucicaut. Quartier rive gauche prisé.",
        "intros": [
            "La station <strong>Saint-Placide</strong> est située dans le <strong>6e arrondissement de Paris</strong>, sous la <strong>rue de Rennes</strong> à proximité de la rue Saint-Placide. Elle est desservie uniquement par la <strong>M4</strong>, entre <strong>Saint-Sulpice</strong> (1 station nord) et <strong>Montparnasse-Bienvenüe</strong> (1 station sud, hub M6+M12+M13+TGV Gare Montparnasse). Bus 39, 70, 96.",
            "Ouverte le <strong>9 janvier 1910</strong> avec le prolongement de la M4 sous la Seine (Châtelet ↔ Vavin).",
            "À <strong>5 min à pied</strong> : <strong>Le Bon Marché Rive Gauche</strong>, le <strong>premier grand magasin moderne au monde</strong>. Fondé en <strong>1852</strong> par <strong>Aristide Boucicaut</strong> à partir d'un petit magasin de nouveautés. Innovation révolutionnaire : <strong>prix fixés et affichés</strong> (vs. marchandage), <strong>retour des marchandises possible</strong>, <strong>entrée libre sans obligation d'achat</strong>, <strong>livraison à domicile</strong>. Modèle copié dans le monde entier. Aujourd'hui propriété <strong>LVMH</strong>, dédié au luxe et à la mode."
        ],
        "hist_title": "Le Bon Marché (1852) — révolution du commerce moderne",
        "hist": [
            "La station <strong>M4</strong> ouvre le <strong>9 janvier 1910</strong> avec le prolongement de la M4 sous la Seine (Châtelet ↔ Vavin).",
            "Le nom <strong>Saint-Placide</strong> vient de la <strong>rue Saint-Placide</strong> elle-même nommée d'après <strong>saint Placide</strong> (515-565), moine bénédictin italien, disciple de saint Benoît, missionnaire en Sicile. Rue ouverte au XVIIᵉ siècle.",
            "Le <strong>Bon Marché Rive Gauche</strong>, à 5 min de la station, est le <strong>premier grand magasin moderne au monde</strong>. Fondé en <strong>1852</strong> par <strong>Aristide Boucicaut</strong> (1810-1877) et sa femme <strong>Marguerite Boucicaut</strong> (1816-1887) à partir d'un petit magasin de nouveautés acheté en 1838.",
            "<strong>Révolution commerciale</strong> : Boucicaut introduit des innovations qui changeront le commerce mondial. <strong>Prix fixés et affichés</strong> (vs. marchandage traditionnel), <strong>retour des marchandises possible si insatisfaction</strong>, <strong>entrée libre sans obligation d'achat</strong>, <strong>livraison à domicile</strong>, <strong>catalogues postaux</strong>, <strong>soldes saisonnières</strong>. Concept de <em>« grand magasin »</em> exporté dans le monde entier.",
            "Bâtiment actuel : architecture de <strong>Louis-Charles Boileau et Gustave Eiffel</strong> (1869-1887). <strong>Verrière monumentale</strong>, structure métallique typique. <strong>Émile Zola</strong> s'en inspire pour son roman <em>« Au Bonheur des Dames »</em> (1883).",
            "Aujourd'hui, le Bon Marché est propriété de <strong>LVMH</strong> (Bernard Arnault, depuis 1984). Spécialisé dans le <strong>luxe et la mode haut de gamme</strong>. Adjacent : <strong>La Grande Épicerie de Paris</strong>, l'une des plus prestigieuses épiceries fines du monde."
        ],
        "faq": [
            ("Quelle ligne dessert Saint-Placide ?", "Uniquement la <strong>M4</strong>. Bus 39, 70, 96."),
            ("Où est le Bon Marché ?", "<strong>5 min à pied</strong> de la station. <strong>Le Bon Marché Rive Gauche</strong>, premier grand magasin moderne au monde (1852, Aristide Boucicaut). Aujourd'hui propriété LVMH, dédié au luxe."),
            ("Pourquoi le Bon Marché est-il historique ?", "Fondé en <strong>1852</strong> par <strong>Aristide Boucicaut</strong>, le Bon Marché est le <strong>premier grand magasin moderne au monde</strong>. Innovations révolutionnaires : prix fixés et affichés, retour possible, entrée libre, livraison à domicile, catalogues. Modèle exporté mondialement."),
            ("Émile Zola a-t-il écrit sur le Bon Marché ?", "<strong>Oui</strong>. Le roman <em>« Au Bonheur des Dames »</em> (1883) d'<strong>Émile Zola</strong> est directement inspiré du Bon Marché et d'Aristide Boucicaut. Décrit la révolution commerciale et sociale du grand magasin parisien."),
            ("Comment aller à Montparnasse ?", "<strong>M4 directe</strong> : 1 station vers le sud (~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. M4 historique 1910.")
        ],
        "tips": [
            "<strong>Le Bon Marché Rive Gauche</strong> à 5 min — premier grand magasin moderne.",
            "<strong>La Grande Épicerie de Paris</strong> adjacente au Bon Marché.",
            "Pour <strong>Montparnasse</strong> (gare TGV + M6/M12/M13) : M4 directe (1 station).",
            "Pour <strong>Saint-Germain-des-Prés</strong> : M4 directe (2 stations).",
            "Rue de Rennes — boutiques mode haut de gamme."
        ],
        "trivia": [
            ("🛍️", "Le Bon Marché (1852) — 1er grand magasin moderne au monde", "À <strong>5 min à pied</strong>, <strong>Le Bon Marché Rive Gauche</strong> est le <strong>premier grand magasin moderne au monde</strong>. Fondé en <strong>1852</strong> par <strong>Aristide Boucicaut</strong> (1810-1877) et sa femme Marguerite. <strong>Innovations révolutionnaires</strong> : prix fixés et affichés (vs marchandage), retour des marchandises possible, entrée libre sans obligation d'achat, livraison à domicile, catalogues postaux, soldes. Modèle copié mondialement (Harrods Londres 1849, Macy's NY 1858, Wertheim Berlin 1875). Architecture <strong>Louis-Charles Boileau + Gustave Eiffel</strong> (1869-1887)."),
            ("📚", "« Au Bonheur des Dames » — Zola s'inspire du Bon Marché", "Le roman <em>« Au Bonheur des Dames »</em> (1883) d'<strong>Émile Zola</strong>, 11e volume de la série <em>Les Rougon-Macquart</em>, est <strong>directement inspiré du Bon Marché et d'Aristide Boucicaut</strong>. Zola décrit la révolution commerciale et sociale du grand magasin parisien : prix bas, attraction client, conditions de travail des employés, déclin des petits commerces traditionnels. Roman emblématique du naturalisme français.")
        ],
        "itin": [
            ("Le Bon Marché Rive Gauche", "bon-marche", "à pied", "5 min direction nord-est", 5),
            ("La Grande Épicerie de Paris", "grande-epicerie", "à pied", "5 min direct", 5),
            ("Saint-Sulpice via M4", "saint-sulpice", "M4", "M4 direction Porte de Clignancourt (1 station)", 2),
            ("Montparnasse via M4", "montparnasse-bienvenue", "M4", "M4 direction Bagneux (1 station)", 2),
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Porte de Clignancourt (5 stations)", 10),
            ("Saint-Germain-des-Prés via M4", "saint-germain-des-pres", "M4", "M4 direction Porte de Clignancourt (2 stations)", 4)
        ]
    },
    "raspail": {
        "seo": "Station Raspail : M4 + M6 dans le 14e arr. Boulevard Raspail, Cimetière Montparnasse, fondation Cartier pour l'art contemporain.",
        "tagline": "M4 + M6 — Cimetière Montparnasse, fondation Cartier",
        "hero_desc": "Station <strong>Raspail</strong> dans le <strong>14e arrondissement</strong>, à l'intersection du boulevard Raspail et du boulevard du Montparnasse. Desservie par <strong>M4</strong> (ouverte 30 octobre 1909) et <strong>M6</strong> (ouverte 24 avril 1906 sur le viaduc aérien). À proximité : le <strong>Cimetière du Montparnasse</strong> (~36 000 sépultures, Sartre, Beauvoir, Baudelaire), la <strong>Fondation Cartier pour l'art contemporain</strong> (Jean Nouvel 1994), et le <strong>boulevard Raspail</strong>.",
        "intros": [
            "La station <strong>Raspail</strong> est située dans le <strong>14e arrondissement de Paris</strong>, à l'intersection du <strong>boulevard Raspail</strong> et du <strong>boulevard du Montparnasse</strong>. Elle est desservie par <strong>2 lignes</strong> : <strong>M4</strong> (Porte de Clignancourt ↔ Bagneux) et <strong>M6</strong> (Charles de Gaulle - Étoile ↔ Nation, aérienne sur viaduc à proximité). Bus 38, 68, 82, 91.",
            "La station <strong>M6</strong> ouvre le <strong>24 avril 1906</strong> avec le tronçon Place d'Italie ↔ Étoile (au-dessus du sol, sur viaduc aérien). La station <strong>M4</strong> est ajoutée le <strong>30 octobre 1909</strong> avec le prolongement de la M4 vers Porte d'Orléans.",
            "À proximité (5-10 min à pied) : le <strong>Cimetière du Montparnasse</strong> (1824, ~19 hectares, 36 000 sépultures), où reposent <strong>Sartre et Beauvoir</strong> (même tombe), <strong>Baudelaire</strong>, <strong>Maupassant</strong>, <strong>Susan Sontag</strong>. Et la <strong>Fondation Cartier pour l'art contemporain</strong> (1994, architecte <strong>Jean Nouvel</strong>) — bâtiment iconique en verre et acier, expositions d'art contemporain renommées."
        ],
        "hist_title": "1906 : M6, 1909 : M4, et le Cimetière Montparnasse",
        "hist": [
            "Le nom <strong>Raspail</strong> commémore <strong>François-Vincent Raspail</strong> (1794-1878), <strong>chimiste, médecin et homme politique français</strong>. Pionnier de l'<strong>histologie cellulaire</strong> et de la <strong>microscopie</strong>. Député républicain, candidat à la présidentielle de 1848. Le boulevard Raspail a été ouvert en 1907.",
            "La station <strong>M6</strong> ouvre le <strong>24 avril 1906</strong> avec le tronçon <strong>Place d'Italie ↔ Étoile</strong> de la M6 (aérienne sur viaduc). À cette date, Raspail est une station de la M2 Sud (renommée M6 plus tard).",
            "La station <strong>M4</strong> est ajoutée le <strong>30 octobre 1909</strong> avec le prolongement de la M4 vers Porte d'Orléans.",
            "À <strong>5 min à pied</strong> : le <strong>Cimetière du Montparnasse</strong>, créé en <strong>1824</strong>, l'un des plus grands de Paris (~19 hectares, ~36 000 sépultures). Sépultures célèbres : <strong>Charles Baudelaire</strong> (1867), <strong>Guy de Maupassant</strong> (1893), <strong>Jean-Paul Sartre et Simone de Beauvoir</strong> (même tombe), <strong>Susan Sontag</strong>, <strong>Samuel Beckett</strong>, <strong>Serge Gainsbourg</strong>, <strong>Marguerite Duras</strong>, <strong>Émile Durkheim</strong>.",
            "À <strong>10 min à pied</strong> : la <strong>Fondation Cartier pour l'art contemporain</strong>, fondée en <strong>1984</strong> par Cartier, installée en <strong>1994</strong> dans son bâtiment actuel boulevard Raspail. Architecte : <strong>Jean Nouvel</strong>. <strong>Bâtiment iconique en verre et acier</strong> qui semble flotter parmi les arbres préservés du jardin de Théodore Vibert. Expositions d'art contemporain renommées.",
            "Le quartier est partagé entre le <strong>Montparnasse historique</strong> (cafés artistes années 1920 — La Coupole, Le Dôme — à proximité Vavin) et la <strong>rive gauche bourgeoise</strong> du boulevard Raspail."
        ],
        "faq": [
            ("Quelles lignes desservent Raspail ?", "<strong>M4</strong> (1909) et <strong>M6</strong> (1906, aérienne sur viaduc à proximité). Bus 38, 68, 82, 91."),
            ("Où est le Cimetière du Montparnasse ?", "<strong>5 min à pied</strong>. Créé en 1824, ~19 ha, ~36 000 sépultures. Sépultures célèbres : <strong>Sartre et Beauvoir</strong> (même tombe), <strong>Baudelaire</strong>, <strong>Maupassant</strong>, <strong>Beckett</strong>, <strong>Gainsbourg</strong>, <strong>Duras</strong>."),
            ("Où est la Fondation Cartier ?", "<strong>10 min à pied</strong> au sud sur le boulevard Raspail. <strong>Fondation Cartier pour l'art contemporain</strong> (1984), installée 1994 dans son bâtiment actuel par <strong>Jean Nouvel</strong>. Bâtiment iconique verre+acier."),
            ("Qui est Raspail ?", "<strong>François-Vincent Raspail</strong> (1794-1878), <strong>chimiste, médecin et homme politique français</strong>. Pionnier de l'<strong>histologie cellulaire</strong> et de la <strong>microscopie</strong>. Député républicain, candidat à la présidentielle 1848."),
            ("Comment aller à Montparnasse ?", "<strong>M4 directe</strong> : 1 station vers le nord (~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. Stations historiques 1906/1909.")
        ],
        "tips": [
            "<strong>Cimetière du Montparnasse</strong> à 5 min — sépultures Sartre, Beauvoir, Baudelaire.",
            "<strong>Fondation Cartier</strong> (Jean Nouvel) à 10 min — art contemporain.",
            "Pour <strong>Montparnasse (gare TGV)</strong> : M4 directe (1 station).",
            "Pour <strong>Tour Eiffel</strong> via M6 : ~15 min (terminus Bir-Hakeim).",
            "Pour <strong>Vavin</strong> (cafés artistes Montparnasse) : 5 min à pied."
        ],
        "trivia": [
            ("⚱️", "Cimetière du Montparnasse — Sartre, Beauvoir, Baudelaire", "À <strong>5 min à pied</strong>, le <strong>Cimetière du Montparnasse</strong> (1824) est l'un des plus grands cimetières de Paris (~19 ha, ~36 000 sépultures). <strong>Sépultures célèbres</strong> : <strong>Jean-Paul Sartre et Simone de Beauvoir</strong> (même tombe, division 20), <strong>Charles Baudelaire</strong> (1867, division 6), <strong>Guy de Maupassant</strong>, <strong>Samuel Beckett</strong>, <strong>Serge Gainsbourg</strong> (division 1), <strong>Marguerite Duras</strong>, <strong>Susan Sontag</strong>, <strong>Émile Durkheim</strong>, <strong>Tristan Tzara</strong>, <strong>Camille Saint-Saëns</strong>. Lieu de pèlerinage littéraire et philosophique."),
            ("🏛️", "Fondation Cartier (Jean Nouvel 1994)", "À <strong>10 min à pied</strong> au sud, la <strong>Fondation Cartier pour l'art contemporain</strong> est installée depuis <strong>1994</strong> dans un bâtiment iconique de <strong>Jean Nouvel</strong>. Concept : <strong>architecture transparente</strong> en verre et acier qui semble flotter parmi les <strong>arbres préservés</strong> du jardin de Théodore Vibert (botaniste XIXᵉ). Fondation créée en <strong>1984</strong> par Cartier. Expositions d'art contemporain renommées (Jean-Michel Othoniel, Cai Guo-Qiang, Patti Smith, Jean-Michel Alberola)."),
        ],
        "itin": [
            ("Cimetière du Montparnasse", "cimetiere-montparnasse", "à pied", "5 min direct", 5),
            ("Fondation Cartier", "fondation-cartier", "à pied", "10 min sud bd Raspail", 10),
            ("Montparnasse via M4", "montparnasse-bienvenue", "M4", "M4 direction Porte de Clignancourt (1 station)", 2),
            ("Tour Eiffel via M6", "tour-eiffel", "M6", "M6 direction Étoile jusqu'à Bir-Hakeim", 15),
            ("Vavin (cafés artistes)", "vavin", "à pied", "5 min nord", 5),
            ("Place d'Italie via M6", "place-italie", "M6", "M6 direction Nation", 10)
        ]
    },
    "alesia": {
        "seo": "Station Alésia : M4 dans le 14e arr., avenue du Général Leclerc. Quartier résidentiel sud parisien, statue de Léon Bourgeois.",
        "tagline": "M4 — quartier sud parisien Alésia",
        "hero_desc": "Station <strong>Alésia</strong> ouverte le <strong>30 octobre 1909</strong> avec le prolongement M4 vers Porte d'Orléans. Située dans le <strong>14e arrondissement</strong>, à l'intersection de l'<strong>avenue du Général Leclerc</strong> et de l'<strong>avenue d'Alésia</strong>. Nom inspiré de la <strong>bataille d'Alésia</strong> (52 av. J.-C., défaite de Vercingétorix par Jules César). Quartier résidentiel sud parisien.",
        "intros": [
            "La station <strong>Alésia</strong> est située dans le <strong>14e arrondissement de Paris</strong>, à l'intersection de l'<strong>avenue du Général Leclerc</strong> et de l'<strong>avenue d'Alésia</strong>. Elle est desservie uniquement par la <strong>M4</strong> (Porte de Clignancourt ↔ Bagneux), entre <strong>Mouton-Duvernet</strong> (1 station nord) et <strong>Mairie de Montrouge</strong> (1 station sud). Bus 38, 62, 68.",
            "Ouverte le <strong>30 octobre 1909</strong> avec le prolongement de la M4 vers Porte d'Orléans (alors terminus sud). Configuration souterraine standard à 2 voies / 2 quais latéraux.",
            "Le nom <strong>« Alésia »</strong> commémore la <strong>bataille d'Alésia</strong> (52 av. J.-C.), au cours de laquelle <strong>Jules César</strong> battit le chef gaulois <strong>Vercingétorix</strong>, mettant fin à la guerre des Gaules. L'<strong>avenue d'Alésia</strong> a été ouverte au XIXᵉ siècle dans le quartier nouvellement loti du 14e."
        ],
        "hist_title": "1909 : prolongement M4 vers Porte d'Orléans",
        "hist": [
            "La station <strong>M4</strong> est inaugurée le <strong>30 octobre 1909</strong> avec le <strong>prolongement de la M4 vers Porte d'Orléans</strong> (alors terminus sud, depuis Vavin). Configuration souterraine standard à 2 voies et 2 quais latéraux.",
            "Le nom <strong>« Alésia »</strong> commémore la <strong>bataille d'Alésia</strong>, événement majeur de l'histoire antique de la Gaule. En <strong>septembre 52 av. J.-C.</strong>, <strong>Jules César</strong> bat le chef arverne <strong>Vercingétorix</strong> au siège d'Alésia (Alise-Sainte-Reine en Bourgogne aujourd'hui, ou Chaux-des-Crotenay selon les hypothèses). Cette défaite marque la <strong>fin de la guerre des Gaules</strong> et le début de la <strong>conquête romaine de la Gaule</strong>.",
            "L'<strong>avenue d'Alésia</strong> a été ouverte au XIXᵉ siècle dans le cadre du <strong>développement urbain du 14e arrondissement</strong>, ancien quartier des fermes et des nouveaux quartiers résidentiels post-Haussmann.",
            "Le quartier autour est aujourd'hui <strong>résidentiel et tranquille</strong>, avec une population mixte (familles, étudiants). Plusieurs <strong>marchés couverts</strong> et <strong>boutiques de quartier</strong>. La <strong>statue de Léon Bourgeois</strong> (1851-1925, président du Conseil et prix Nobel de la paix 1920) se trouve à proximité.",
            "Affluence quotidienne modérée. Station appréciée des familles habitant le 14e."
        ],
        "faq": [
            ("Quelle ligne dessert Alésia ?", "Uniquement la <strong>M4</strong> (Porte de Clignancourt ↔ Bagneux - Lucie Aubrac). Bus 38, 62, 68."),
            ("Pourquoi le nom Alésia ?", "De la <strong>bataille d'Alésia</strong> (52 av. J.-C.), où <strong>Jules César</strong> battit le chef gaulois <strong>Vercingétorix</strong>, mettant fin à la guerre des Gaules. L'avenue d'Alésia a été ouverte au XIXᵉ siècle dans le 14e."),
            ("Comment aller à Montparnasse ?", "<strong>M4 directe</strong> : ~6 min (3 stations vers le nord)."),
            ("Comment aller à Châtelet ?", "<strong>M4 directe</strong> : ~14 min (8 stations vers le nord)."),
            ("Quel est le quartier autour ?", "Quartier <strong>résidentiel tranquille du 14e arrondissement</strong>. Marchés couverts, boutiques de quartier, statue de Léon Bourgeois (Nobel de la paix 1920) à proximité."),
            ("La station est-elle accessible PMR ?", "<strong>Non, pas entièrement</strong>. M4 historique 1909.")
        ],
        "tips": [
            "Pour <strong>Montparnasse (gare TGV)</strong> : M4 directe (~6 min).",
            "Pour <strong>Châtelet</strong> : M4 directe (~14 min).",
            "Pour <strong>Mairie de Montrouge</strong> : M4 directe (1 station vers le sud).",
            "Quartier résidentiel — restaurants de quartier, marchés couverts.",
            "Marché aux Puces de Vanves accessible via Porte de Vanves (M13 + bus)."
        ],
        "trivia": [
            ("⚔️", "Bataille d'Alésia (52 av. J.-C.) — fin de la guerre des Gaules", "Le nom <strong>« Alésia »</strong> commémore la <strong>bataille d'Alésia</strong>, événement majeur de l'histoire antique. En <strong>septembre 52 av. J.-C.</strong>, <strong>Jules César</strong> bat le chef arverne <strong>Vercingétorix</strong> au siège d'Alésia. <strong>Lieu géographique</strong> : Alise-Sainte-Reine en Bourgogne selon thèse officielle (XIXᵉ), Chaux-des-Crotenay (Jura) selon thèse alternative. Cette défaite marque la <strong>fin de la guerre des Gaules</strong> et le début de la <strong>conquête romaine de la Gaule</strong>. Vercingétorix sera étranglé à Rome 6 ans plus tard, après le triomphe de César."),
            ("🏅", "Léon Bourgeois (1851-1925) — Nobel de la paix 1920", "La <strong>statue de Léon Bourgeois</strong> est à proximité de la station. <strong>Léon Bourgeois</strong> (1851-1925), <strong>homme politique français</strong> : président du Conseil (1895-1896), ministre, sénateur. <strong>Prix Nobel de la paix 1920</strong> pour son rôle dans la création de la <strong>Société des Nations</strong> (ancêtre de l'ONU) après la Première Guerre mondiale. Théoricien du <strong>solidarisme</strong>, doctrine philosophique et politique influente sous la IIIᵉ République.")
        ],
        "itin": [
            ("Montparnasse via M4", "montparnasse-bienvenue", "M4", "M4 direction Porte de Clignancourt (3 stations)", 6),
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Porte de Clignancourt (8 stations)", 14),
            ("Mairie de Montrouge via M4", "mairie-de-montrouge", "M4", "M4 direction Bagneux (1 station)", 2),
            ("Mouton-Duvernet via M4", "mouton-duvernet", "M4", "M4 direction Porte de Clignancourt (1 station)", 2),
            ("Saint-Michel via M4", "saint-michel", "M4", "M4 direction Porte de Clignancourt (6 stations)", 11),
            ("Bagneux - Lucie Aubrac via M4", "bagneux-lucie-aubrac", "M4", "M4 terminus sud (2 stations)", 5)
        ]
    },
    "mairie-de-montrouge": {
        "seo": "Station Mairie de Montrouge : M4 à Montrouge (92), ouverte en 2013 avec le prolongement M4 hors Paris. Mairie de Montrouge et Beffroi, commune des Hauts-de-Seine.",
        "tagline": "M4 — Hôtel de Ville de Montrouge (92)",
        "hero_desc": "Station <strong>Mairie de Montrouge</strong> ouverte le <strong>23 mars 2013</strong> avec le prolongement de la M4 au-delà de Paris. Située à <strong>Montrouge</strong> (Hauts-de-Seine, 92), sur l'<strong>avenue de la République</strong>. À la sortie : l'<strong>Hôtel de Ville de Montrouge</strong> et son <strong>Beffroi</strong>. Première station M4 hors Paris depuis 1910.",
        "intros": [
            "La station <strong>Mairie de Montrouge</strong> est située à <strong>Montrouge</strong> (Hauts-de-Seine, 92), sur l'<strong>avenue de la République</strong>. Elle est desservie uniquement par la <strong>M4</strong> (Porte de Clignancourt ↔ Bagneux - Lucie Aubrac), entre <strong>Alésia</strong> (1 station nord, Paris 14e) et <strong>Montrouge</strong> (1 station sud, ouverte 2022). Bus 28, 68, 126, 188, 191, 195.",
            "Ouverte le <strong>23 mars 2013</strong> avec le <strong>prolongement sud de la M4</strong> de Porte d'Orléans à Mairie de Montrouge — <strong>premier prolongement M4 hors Paris depuis 1910</strong>. La M4 dépasse alors les limites traditionnelles de Paris intra-muros, marquant l'intégration métropolitaine.",
            "À la sortie : l'<strong>Hôtel de Ville de Montrouge</strong> (1882-1885, architecte Émile Renaud), mairie de la commune de <strong>Montrouge</strong> (~50 000 habitants). À côté : le <strong>Beffroi de Montrouge</strong>, salle de spectacle municipale. À 10 min : le <strong>Salon de Montrouge</strong> (art contemporain émergent, tenu chaque année depuis 1955)."
        ],
        "hist_title": "Montrouge (commune Hauts-de-Seine) et prolongement M4 (2013)",
        "hist": [
            "La station <strong>Mairie de Montrouge</strong> est inaugurée le <strong>23 mars 2013</strong> avec le <strong>prolongement sud de la M4</strong> de Porte d'Orléans à Mairie de Montrouge. <strong>Premier prolongement M4 hors Paris depuis 1910</strong> (date où la ligne atteignait Porte d'Orléans). La station dépasse les limites traditionnelles de Paris intra-muros.",
            "<strong>Montrouge</strong> est une commune des <strong>Hauts-de-Seine (92)</strong>, limitrophe de Paris (14e arrondissement). <strong>~50 000 habitants</strong>. Étymologie : <em>« Mons Rufus »</em> en latin médiéval (mont rouge, en référence à l'argile rouge du sol). Commune depuis le Moyen Âge.",
            "L'<strong>Hôtel de Ville de Montrouge</strong> à la sortie de la station a été construit entre <strong>1882 et 1885</strong> par l'architecte <strong>Émile Renaud</strong>. Style éclectique néo-Renaissance. <strong>Restauré récemment</strong> dans les années 2010. Adjacent : le <strong>Beffroi de Montrouge</strong>, salle de spectacle municipale moderne.",
            "À <strong>10 min</strong> : le <strong>Salon de Montrouge</strong>, manifestation d'art contemporain dédiée aux jeunes artistes émergents. <strong>Tenu chaque année depuis 1955</strong>. Plus important salon de découverte des jeunes artistes en France.",
            "Affluence quotidienne croissante depuis l'ouverture du métro. Montrouge devient progressivement quartier d'extension de Paris pour les familles cherchant des logements plus grands et accessibles."
        ],
        "faq": [
            ("Quelle ligne dessert Mairie de Montrouge ?", "Uniquement la <strong>M4</strong>. Bus 28, 68, 126, 188, 191, 195."),
            ("Quand a-t-elle ouvert ?", "Le <strong>23 mars 2013</strong>, avec le <strong>prolongement sud de la M4</strong> de Porte d'Orléans à Mairie de Montrouge. Premier prolongement M4 hors Paris depuis 1910."),
            ("Quelle est la commune ?", "<strong>Montrouge</strong>, commune des <strong>Hauts-de-Seine (92)</strong>, limitrophe de Paris (14e arr.). <strong>~50 000 habitants</strong>. Étymologie : <em>« Mons Rufus »</em> (mont rouge, argile du sol)."),
            ("Qu'est-ce que le Salon de Montrouge ?", "Manifestation d'<strong>art contemporain</strong> dédiée aux <strong>jeunes artistes émergents</strong>. <strong>Tenu chaque année depuis 1955</strong>. Plus important salon de découverte de jeunes artistes en France."),
            ("Comment aller à Châtelet ?", "<strong>M4 directe</strong> : ~16 min (9 stations vers le nord)."),
            ("La station est-elle accessible PMR ?", "<strong>Oui, entièrement</strong>. Station moderne 2013 conforme aux normes PMR.")
        ],
        "tips": [
            "<strong>Hôtel de Ville de Montrouge</strong> à la sortie — bâtiment 1882-1885.",
            "<strong>Beffroi de Montrouge</strong> — salle de spectacle.",
            "<strong>Salon de Montrouge</strong> (art contemporain émergent) chaque année.",
            "Pour <strong>Châtelet</strong> : M4 directe (~16 min).",
            "Zone tarifaire 2 — vérifier votre titre transport.",
            "Pour <strong>Bagneux - Lucie Aubrac</strong> : M4 terminus sud (1 station)."
        ],
        "trivia": [
            ("🏛️", "Premier prolongement M4 hors Paris (2013)", "La station <strong>Mairie de Montrouge</strong> (ouverte 23 mars 2013) marque le <strong>premier prolongement de la M4 hors Paris depuis 1910</strong>. La M4 avait atteint Porte d'Orléans (terminus sud à Paris) en 1910. Aucun prolongement pendant 103 ans. Le passage hors Paris symbolise l'<strong>intégration métropolitaine</strong> et l'extension de l'agglomération parisienne. Suivi par Bagneux - Lucie Aubrac en 2022 (2 stations supplémentaires)."),
            ("🎨", "Salon de Montrouge — jeunes artistes émergents depuis 1955", "À <strong>10 min</strong> : le <strong>Salon de Montrouge</strong>, manifestation d'<strong>art contemporain dédiée aux jeunes artistes émergents</strong>. <strong>Tenu chaque année depuis 1955</strong>, en mai au Beffroi de Montrouge. <strong>Plus important salon de découverte des jeunes artistes en France</strong>. Souvent qualifié de « pépinière » du marché de l'art français. Artistes révélés : Yan Pei-Ming, Sophie Calle (avant célébrité), Annette Messager, etc.")
        ],
        "itin": [
            ("Hôtel de Ville Montrouge", "hotel-ville-montrouge", "à pied", "Sortie directe", 1),
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Porte de Clignancourt (9 stations)", 16),
            ("Montparnasse via M4", "montparnasse-bienvenue", "M4", "M4 direction Porte de Clignancourt (4 stations)", 8),
            ("Saint-Michel via M4", "saint-michel", "M4", "M4 direction Porte de Clignancourt (7 stations)", 13),
            ("Bagneux - Lucie Aubrac via M4", "bagneux-lucie-aubrac", "M4", "M4 terminus sud (1 station)", 3),
            ("Salon de Montrouge", "salon-montrouge", "à pied", "10 min direct", 10)
        ]
    },
    "bagneux-lucie-aubrac": {
        "seo": "Station Bagneux - Lucie Aubrac : M4 à Bagneux (92), terminus sud, ouverte le 13 janvier 2022. Nommée d'après Lucie Aubrac, résistante française.",
        "tagline": "M4 — Terminus sud Bagneux, Lucie Aubrac résistante",
        "hero_desc": "Station <strong>Bagneux - Lucie Aubrac</strong>, <strong>terminus sud de la M4</strong>, ouverte le <strong>13 janvier 2022</strong>. Située à <strong>Bagneux</strong> (Hauts-de-Seine, 92). Nommée d'après <strong>Lucie Aubrac</strong> (1912-2007), <strong>résistante française</strong> emblématique de la Seconde Guerre mondiale, professeure d'histoire. Aboutissement du prolongement M4 en banlieue sud.",
        "intros": [
            "La station <strong>Bagneux - Lucie Aubrac</strong> est située à <strong>Bagneux</strong> (Hauts-de-Seine, 92), sur l'<strong>avenue Albert-Petit</strong>. Elle est <strong>terminus sud de la ligne 4 du métro</strong> (Porte de Clignancourt ↔ Bagneux - Lucie Aubrac), entre <strong>Montrouge</strong> (1 station vers le nord) et le terminus. Bus 162, 188, 191, 197, 297, V1.",
            "Ouverte le <strong>13 janvier 2022</strong> avec le <strong>prolongement sud de la M4</strong> de Mairie de Montrouge à Bagneux - Lucie Aubrac (2 stations ajoutées : Montrouge + Bagneux). Station moderne avec accessibilité PMR totale, portes palières, voie de retournement automatique.",
            "Le nom <strong>« Lucie Aubrac »</strong> commémore <strong>Lucie Aubrac</strong> (1912-2007), <strong>résistante française</strong> emblématique de la Seconde Guerre mondiale. <strong>Professeure d'histoire</strong>. Avec son mari <strong>Raymond Aubrac</strong>, elle participe à la création du mouvement de résistance <strong>« Libération-Sud »</strong> (1940). Elle est connue pour avoir organisé en octobre 1943 l'<strong>évasion spectaculaire de son mari</strong> et de 13 autres résistants des griffes de la Gestapo lyonnaise (Klaus Barbie). Auteure de <em>Ils partiront dans l'ivresse</em> (1984)."
        ],
        "hist_title": "Lucie Aubrac (1912-2007) et le prolongement M4 (2022)",
        "hist": [
            "La station <strong>Bagneux - Lucie Aubrac</strong> est inaugurée le <strong>13 janvier 2022</strong> avec le <strong>prolongement sud de la M4</strong> de Mairie de Montrouge à Bagneux - Lucie Aubrac. 2 stations ajoutées : Montrouge (intermédiaire) et Bagneux (terminus). Aboutissement de 25 ans de planification (étude initiale 1990s).",
            "Station moderne conforme aux dernières normes : <strong>accessibilité PMR totale</strong>, <strong>portes palières</strong>, <strong>voie de retournement automatique</strong>, signalétique tactile, ascenseurs vers tous les niveaux.",
            "Le nom <strong>« Lucie Aubrac »</strong> commémore <strong>Lucie Aubrac</strong> (1912-2007), <strong>résistante française</strong>. <strong>Née Bernard à Mâcon</strong>, mariée à <strong>Raymond Aubrac</strong> en 1939. Professeure d'histoire-géographie. Avec son mari, fonde le mouvement de résistance <strong>« Libération-Sud »</strong> en 1940 (zone non occupée).",
            "<strong>Acte héroïque</strong> : en <strong>octobre 1943</strong>, alors que Raymond Aubrac est arrêté par la <strong>Gestapo lyonnaise de Klaus Barbie</strong> avec Jean Moulin, Lucie organise une <strong>évasion spectaculaire</strong>. Elle simule être sa fiancée, demande à le voir, et organise l'<strong>attaque du fourgon</strong> qui le transporte le 21 octobre 1943. Raymond et 13 autres résistants sont libérés. Lucie, enceinte de leur deuxième enfant, fuit avec lui à Londres via l'Espagne.",
            "Après la guerre : militante engagée (anticolonialisme, féminisme, pacifisme). Conférences dans les lycées et les écoles sur la Résistance. <strong>Récit autobiographique <em>« Ils partiront dans l'ivresse »</em></strong> (1984, adapté au cinéma par Claude Berri en 1997 avec Carole Bouquet). <strong>Décédée en 2007</strong> à 94 ans. <strong>Panthéonisée symboliquement</strong> (sans transfert, refusé par la famille) en 2015 avec Geneviève de Gaulle-Anthonioz.",
            "La <strong>commune de Bagneux</strong> (~42 000 habitants) compte plusieurs lieux nommés d'après des résistants et personnalités progressistes. Choix politique de la municipalité communiste historique pour nommer la nouvelle station métro."
        ],
        "faq": [
            ("Quelle ligne dessert Bagneux - Lucie Aubrac ?", "Uniquement la <strong>M4</strong> (terminus sud). Bus 162, 188, 191, 197, 297, V1."),
            ("Quand a-t-elle ouvert ?", "Le <strong>13 janvier 2022</strong>, avec le prolongement sud de la M4 (2 stations ajoutées : Montrouge + Bagneux)."),
            ("Qui était Lucie Aubrac ?", "<strong>Lucie Aubrac</strong> (1912-2007), <strong>résistante française</strong> emblématique. Professeure d'histoire. Co-fondatrice du mouvement <strong>« Libération-Sud »</strong> (1940). Connue pour avoir organisé en octobre 1943 l'<strong>évasion spectaculaire de son mari Raymond Aubrac</strong> et 13 autres résistants des mains de la Gestapo lyonnaise. Auteure de <em>« Ils partiront dans l'ivresse »</em> (1984)."),
            ("Quelle est la commune ?", "<strong>Bagneux</strong>, commune des <strong>Hauts-de-Seine (92)</strong>. ~42 000 habitants. Limitrophe de Paris et Montrouge."),
            ("Comment aller à Châtelet ?", "<strong>M4 directe</strong> : ~18 min (10 stations vers le nord)."),
            ("La station est-elle accessible PMR ?", "<strong>Oui, entièrement</strong>. Station moderne 2022 conforme aux dernières normes PMR.")
        ],
        "tips": [
            "<strong>Station moderne 2022</strong> — accessibilité PMR totale.",
            "Pour <strong>Châtelet</strong> : M4 directe (~18 min).",
            "Pour <strong>Montparnasse (gare TGV)</strong> : M4 directe (~10 min).",
            "Zone tarifaire 2 — vérifier votre titre transport.",
            "Quartier banlieue sud — peu de commerces immédiats sortie métro.",
            "Pour <strong>Mairie de Montrouge</strong> : M4 directe (1 station vers le nord)."
        ],
        "trivia": [
            ("🎖️", "Lucie Aubrac (1912-2007) — Résistante héroïque", "<strong>Lucie Aubrac</strong> (née Bernard, 1912-2007) est l'une des <strong>résistantes françaises les plus emblématiques</strong> de la Seconde Guerre mondiale. <strong>Professeure d'histoire-géographie</strong>. Co-fondatrice avec son mari Raymond Aubrac du mouvement <strong>« Libération-Sud »</strong> en 1940. Acte héroïque : <strong>octobre 1943</strong>, elle organise l'<strong>évasion spectaculaire</strong> de Raymond et 13 autres résistants des griffes de la <strong>Gestapo lyonnaise de Klaus Barbie</strong>. Récit autobiographique <em>« Ils partiront dans l'ivresse »</em> (1984), adapté au cinéma par Claude Berri (1997, avec Carole Bouquet). <strong>Panthéonisée symboliquement</strong> en 2015 (sans transfert, refusé par la famille)."),
            ("🚇", "Prolongement M4 2022 — 2 stations ajoutées", "Le <strong>prolongement sud de la M4</strong> ouvre le <strong>13 janvier 2022</strong> avec <strong>2 stations ajoutées</strong> : Montrouge (intermédiaire) et Bagneux - Lucie Aubrac (terminus). Aboutissement de <strong>25 ans de planification</strong> (étude initiale années 1990). La M4 passe ainsi de 27 à 29 stations totales. Bagneux - Lucie Aubrac devient le 2e terminus M4 hors Paris (après Mairie de Montrouge en 2013).")
        ],
        "itin": [
            ("Châtelet via M4", "chatelet", "M4", "M4 direction Porte de Clignancourt (10 stations)", 18),
            ("Montparnasse via M4", "montparnasse-bienvenue", "M4", "M4 direction Porte de Clignancourt (5 stations)", 10),
            ("Saint-Michel via M4", "saint-michel", "M4", "M4 direction Porte de Clignancourt (8 stations)", 15),
            ("Mairie de Montrouge via M4", "mairie-de-montrouge", "M4", "M4 direction Porte de Clignancourt (1 station)", 2),
            ("Bagneux centre-ville", "bagneux-centre", "à pied", "10 min direct", 10),
            ("Saint-Germain-des-Prés via M4", "saint-germain-des-pres", "M4", "M4 direction Porte de Clignancourt (7 stations)", 13)
        ]
    }
})

def enrich(slug, c):
    p = STATIONS / f"{slug}.json"
    d = json.loads(p.read_text())
    d["published"] = True
    d.pop("_doc", None); d.pop("_todo", None)
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
    # Defaults
    if not d.get("services"):
        d["services"] = {
            "wifi": {"available": False, "location_detail": "", "coverage_detail": ""},
            "toilets": {"public_paid": {"available": False}, "public_free": {"available": False, "location": "", "access": ""}},
            "atm": {"available": True, "banks_count_estimate": "plusieurs", "locations": []},
            "ratp_office": {"available": False, "location": "", "services": ""},
            "left_luggage": {"ratp_available": False, "third_party": []},
            "shopping_dining": {"main_location": "", "details": "Commerces de quartier autour de la station.", "secondary": ""}
        }
    if not d.get("safety") or not d.get("safety", {}).get("tips"):
        d["safety"] = {
            "audit_status": "pending", "audit_date": None, "level": "", "agents": None, "police": None,
            "tips": ["Station métro Paris — vigilance pickpockets standard.", "Affluence variable selon heures de pointe.", "Présence agents IDFM intermittente."],
            "notes": "Audit RATP/IDFM spécifique non disponible."
        }
    if not d.get("accessibility"):
        d["accessibility"] = {
            "audit_status": "pending", "audit_date": None, "level": "",
            "stats": {"elevators_count": 0, "accessible_lines": 0, "total_lines": len(d.get("lines",[]))},
            "details": "Accessibilité PMR à vérifier en station."
        }
    p.write_text(json.dumps(d, indent=4, ensure_ascii=False) + "\n")
    print(f"✓ {slug}")

if __name__ == "__main__":
    for slug, c in CONTENT.items():
        try:
            enrich(slug, c)
        except Exception as e:
            print(f"✗ {slug}: {e}", file=sys.stderr)
