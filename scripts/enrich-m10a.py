#!/usr/bin/env python3
"""Enrichit M10 Batch A — 12 stations safe."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    "boulogne-pont-de-saint-cloud": {
        "addr": "Avenue Charles-de-Gaulle, 92100 Boulogne-Billancourt", "arr": "Boulogne-Billancourt (92)",
        "seo": "Station Boulogne - Pont de Saint-Cloud, terminus ouest M10 à Boulogne-Billancourt (92). Proche du Parc des Princes et du Pont de Saint-Cloud sur la Seine.",
        "tagline": "M10 — terminus ouest, Boulogne-Billancourt",
        "hero_desc": "Station <strong>Boulogne - Pont de Saint-Cloud</strong>, <strong>terminus ouest de la M10</strong>, à <strong>Boulogne-Billancourt</strong> (Hauts-de-Seine, 92). Ouverte le <strong>3 octobre 1981</strong>. À proximité du <strong>Pont de Saint-Cloud</strong> sur la Seine et du <strong>Parc des Princes</strong>.",
        "intros": [
            "La station <strong>Boulogne - Pont de Saint-Cloud</strong> est <strong>terminus ouest de la M10</strong>, située à <strong>Boulogne-Billancourt</strong> (Hauts-de-Seine, 92). Bus 52, 72, 123, 126, 175, 426, 467.",
            "Ouverte le <strong>3 octobre 1981</strong> avec le prolongement de la ligne 10 de <strong>Porte d'Auteuil à Boulogne - Pont de Saint-Cloud</strong>. Dernier prolongement ouest de la ligne.",
            "À proximité : le <strong>Pont de Saint-Cloud</strong>, qui enjambe la Seine vers <strong>Saint-Cloud</strong>, et le <strong>Parc des Princes</strong>, <strong>stade emblématique</strong> du <strong>Paris Saint-Germain</strong> (48 712 places, inauguré en 1972). <strong>Boulogne-Billancourt</strong> est la <strong>plus grande commune des Hauts-de-Seine</strong> par sa population (~120 000 habitants)."
        ],
        "hist_title": "1981 : prolongement M10 vers Boulogne",
        "hist": [
            "La station est <strong>inaugurée le 3 octobre 1981</strong> avec le <strong>prolongement de la ligne 10</strong> de <strong>Porte d'Auteuil à Boulogne - Pont de Saint-Cloud</strong> (2 stations ajoutées).",
            "Le <strong>Pont de Saint-Cloud</strong>, qui donne son nom à la station, est un <strong>pont de la Seine</strong> reliant <strong>Boulogne-Billancourt</strong> à <strong>Saint-Cloud</strong>. Une première version remonte au <strong>XVIIe siècle</strong>, plusieurs reconstructions ont suivi.",
            "<strong>Boulogne-Billancourt</strong> est née de la fusion en <strong>1924</strong> des communes de <strong>Boulogne-sur-Seine</strong> et de <strong>Billancourt</strong>. Au <strong>XXe siècle</strong>, ville industrielle célèbre pour les <strong>usines Renault</strong> (1898-1992) sur l'<strong>île Seguin</strong>. Aujourd'hui, ~120 000 habitants, l'une des plus importantes communes d'Île-de-France."
        ],
        "faq": [
            ("Quelle ligne dessert Boulogne - Pont de Saint-Cloud ?", "Uniquement la <strong>M10</strong> (terminus ouest). Bus 52, 72, 123, 126, 175, 426, 467."),
            ("Quand a-t-elle ouvert ?", "Le <strong>3 octobre 1981</strong>."),
            ("Pour le Parc des Princes ?", "<strong>~10 min à pied</strong> ou bus 175."),
            ("Pour Saint-Cloud ?", "<strong>Sortie directe</strong> via le Pont de Saint-Cloud."),
            ("Pour le Quartier Latin ?", "<strong>M10 directe</strong> (~22 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>. Station des années 1980.")
        ],
        "tips": [
            "<strong>Parc des Princes</strong> (PSG) à 10 min à pied ou bus 175.",
            "<strong>Pont de Saint-Cloud</strong> et Saint-Cloud à la sortie.",
            "<strong>Boulogne-Billancourt</strong> : ~120 000 habitants, ancien fief Renault.",
            "Pour <strong>Quartier Latin</strong> : <strong>M10 directe</strong> (~22 min).",
            "Zone tarifaire <strong>2</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("⚽", "Parc des Princes, stade du PSG", "Le <strong>Parc des Princes</strong>, à 10 min à pied, est le <strong>stade emblématique</strong> du <strong>Paris Saint-Germain</strong> (PSG). <strong>48 712 places</strong>. <strong>Inauguré en 1972</strong>, conçu par l'architecte <strong>Roger Taillibert</strong> (auteur du stade olympique de Montréal). Accueille les <strong>matchs du PSG</strong> en Ligue 1 et Champions League, ainsi que des matchs internationaux."),
            ("🏭", "Usines Renault et île Seguin", "<strong>Boulogne-Billancourt</strong> fut au <strong>XXe siècle</strong> un haut lieu de l'<strong>industrie automobile française</strong> avec les <strong>usines Renault</strong> sur l'<strong>île Seguin</strong> (1898-1992). À son apogée, l'usine employait <strong>30 000 ouvriers</strong>. Aujourd'hui, l'île Seguin est reconvertie en <strong>quartier culturel</strong> avec la <strong>Seine Musicale</strong> (auditorium de Shigeru Ban, 2017).")
        ],
        "itin": [
            ("Parc des Princes", "porte-de-saint-cloud", "M10 + M9 ou à pied", "À pied (10 min) ou bus 175", 10),
            ("Saint-Cloud", "boulogne-pont-de-saint-cloud", "à pied", "Pont de Saint-Cloud", 8),
            ("Boulogne - Jean Jaurès", "boulogne-jean-jaures", "M10", "M10 directe (1 station)", 2),
            ("Quartier Latin", "cluny-la-sorbonne", "M10", "M10 directe (~22 min)", 22),
            ("Gare d'Austerlitz", "gare-d-austerlitz", "M10", "M10 directe (terminus est)", 28),
            ("La Défense", "la-defense", "M10 + M1", "M10 → Pont-Neuilly + M1 ou via Porte d'Auteuil", 25)
        ]
    },
    "boulogne-jean-jaures": {
        "addr": "Avenue Jean-Baptiste-Clément, 92100 Boulogne-Billancourt", "arr": "Boulogne-Billancourt (92)",
        "seo": "Station Boulogne - Jean Jaurès (M10) à Boulogne-Billancourt. Nommée d'après Jean Jaurès (1859-1914), homme politique socialiste et historien français.",
        "tagline": "M10 — Jean Jaurès, fondateur du socialisme français",
        "hero_desc": "Station <strong>Boulogne - Jean Jaurès</strong> à <strong>Boulogne-Billancourt</strong> (Hauts-de-Seine, 92). Desservie par la <strong>M10</strong>, ouverte le <strong>3 octobre 1980</strong>. Nommée d'après <strong>Jean Jaurès</strong> (<strong>1859-1914</strong>), <strong>homme politique français</strong>, <strong>fondateur du Parti socialiste français</strong>.",
        "intros": [
            "La station <strong>Boulogne - Jean Jaurès</strong> est implantée à <strong>Boulogne-Billancourt</strong> (Hauts-de-Seine, 92). Elle est desservie par la <strong>ligne 10 du métro</strong>, entre <strong>Boulogne - Pont de Saint-Cloud</strong> (1 station, terminus ouest) et <strong>Porte d'Auteuil</strong> (1 station). Bus 52, 72, 123, 175.",
            "Ouverte le <strong>3 octobre 1980</strong> avec le prolongement de la ligne 10 de <strong>Porte d'Auteuil à Boulogne - Jean Jaurès</strong>.",
            "Le nom <strong>Jean Jaurès</strong> rend hommage à <strong>Jean Jaurès</strong> (<strong>1859-1914</strong>), <strong>homme politique français</strong>, <strong>historien</strong>, <strong>journaliste</strong>. <strong>Agrégé de philosophie</strong>, élu <strong>député du Tarn</strong> à plusieurs reprises. <strong>Cofondateur</strong> du journal <em>L'Humanité</em> (1904) et de la <strong>SFIO</strong> (Section française de l'Internationale ouvrière, 1905). Inhumé au <strong>Panthéon</strong> en <strong>1924</strong>."
        ],
        "hist_title": "1980 : Jean Jaurès et le socialisme français",
        "hist": [
            "La station est <strong>inaugurée le 3 octobre 1980</strong> avec le <strong>prolongement de la ligne 10</strong> de <strong>Porte d'Auteuil à Boulogne - Jean Jaurès</strong>.",
            "Le nom <strong>Jean Jaurès</strong> commémore <strong>Jean Jaurès</strong> (<strong>3 septembre 1859 - 31 juillet 1914</strong>), <strong>homme politique, historien et journaliste français</strong>. Né à <strong>Castres</strong> (Tarn). <strong>Agrégé de philosophie</strong> à 22 ans, il est <strong>élu député du Tarn</strong> en 1885.",
            "<strong>Cofondateur du journal <em>L'Humanité</em></strong> en <strong>1904</strong>, et de la <strong>SFIO</strong> (Section française de l'Internationale ouvrière) en <strong>1905</strong>. <strong>Pacifiste convaincu</strong>, il tente d'empêcher la <strong>Première Guerre mondiale</strong>. <strong>Inhumé au Panthéon</strong> le <strong>23 novembre 1924</strong>. La <strong>mairie de Boulogne-Billancourt</strong> est à proximité de la station."
        ],
        "faq": [
            ("Quelle ligne dessert Boulogne - Jean Jaurès ?", "Uniquement la <strong>M10</strong>. Bus 52, 72, 123, 175."),
            ("Qui est Jean Jaurès ?", "<strong>Jean Jaurès</strong> (1859-1914), <strong>homme politique français</strong>. <strong>Cofondateur</strong> du journal <em>L'Humanité</em> (1904) et de la <strong>SFIO</strong> (1905). <strong>Pacifiste</strong>. Inhumé au <strong>Panthéon</strong> en 1924."),
            ("Quand a-t-elle ouvert ?", "Le <strong>3 octobre 1980</strong>."),
            ("Pour la mairie de Boulogne ?", "<strong>~5 min à pied</strong>."),
            ("Pour le Quartier Latin ?", "<strong>M10 directe</strong> (~20 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Mairie de Boulogne-Billancourt</strong> à 5 min à pied.",
            "<strong>Avenue Jean-Baptiste-Clément</strong> : axe principal de Boulogne.",
            "Pour <strong>Parc des Princes</strong> : <strong>M10 → Boulogne Pont de Saint-Cloud</strong>.",
            "Pour <strong>Quartier Latin</strong> : <strong>M10 directe</strong>.",
            "Zone tarifaire <strong>2</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("📚", "Jean Jaurès, fondateur de L'Humanité", "<strong>Jean Jaurès</strong> (1859-1914), <strong>agrégé de philosophie</strong> à 22 ans, devient <strong>député du Tarn</strong> en 1885. <strong>Cofondateur du journal <em>L'Humanité</em></strong> en <strong>1904</strong> (toujours en publication), et de la <strong>SFIO</strong> (Section française de l'Internationale ouvrière) en <strong>1905</strong>. <strong>Grand orateur</strong>, défenseur du <strong>capitaine Dreyfus</strong>. <strong>Pacifiste convaincu</strong>, il tente jusqu'à la dernière minute d'<strong>empêcher la Première Guerre mondiale</strong>. <strong>Inhumé au Panthéon</strong> le 23 novembre 1924."),
            ("🏛️", "Panthéon, 1924", "L'<strong>inhumation de Jean Jaurès au Panthéon</strong> a lieu le <strong>23 novembre 1924</strong>, dix ans après sa mort. La cérémonie est <strong>massive</strong> : cortège populaire, foule immense, hommage rendu par le président <strong>Gaston Doumergue</strong> et le président du Conseil <strong>Édouard Herriot</strong>. Symbolise la <strong>réconciliation républicaine</strong> autour de la mémoire pacifiste de Jaurès. Le slogan <em>« Jaurès, debout ! »</em> reste un symbole fort.")
        ],
        "itin": [
            ("Mairie de Boulogne-Billancourt", "boulogne-jean-jaures", "à pied", "Avenue Jean-Baptiste-Clément (5 min)", 5),
            ("Boulogne - Pont de Saint-Cloud", "boulogne-pont-de-saint-cloud", "M10", "M10 directe (1 station, terminus)", 2),
            ("Porte d'Auteuil", "porte-d-auteuil", "M10", "M10 directe (1 station)", 2),
            ("Parc des Princes", "porte-de-saint-cloud", "M10 + M9", "M10 → Porte d'Auteuil + M9", 8),
            ("Quartier Latin", "cluny-la-sorbonne", "M10", "M10 directe (~20 min)", 20),
            ("La Défense", "la-defense", "M10 + M1", "Via Porte d'Auteuil + RER C ou bus", 22)
        ]
    },
    "porte-d-auteuil": {
        "addr": "Avenue de la Porte-d'Auteuil, 75016 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Porte d'Auteuil (M10) accès au Stade Roland-Garros, Hippodrome d'Auteuil, Bois de Boulogne et Jardin des Serres d'Auteuil.",
        "tagline": "M10 — Roland-Garros, Hippodrome, Bois de Boulogne",
        "hero_desc": "Station <strong>Porte d'Auteuil</strong> sur l'<strong>avenue de la Porte-d'Auteuil</strong> dans le <strong>16e arrondissement</strong>. Desservie par la <strong>M10</strong>, ouverte le <strong>30 septembre 1913</strong>. Accès direct au <strong>Stade Roland-Garros</strong>, à l'<strong>Hippodrome d'Auteuil</strong>, au <strong>Bois de Boulogne</strong> et au <strong>Jardin des Serres d'Auteuil</strong>.",
        "intros": [
            "La station <strong>Porte d'Auteuil</strong> est implantée sur l'<strong>avenue de la Porte-d'Auteuil</strong> dans le <strong>16e arrondissement</strong>, à la limite du <strong>Bois de Boulogne</strong>. Elle est desservie par la <strong>ligne 10 du métro</strong>, entre <strong>Boulogne - Jean Jaurès</strong> (1 station) et <strong>Michel-Ange - Molitor</strong> (1 station). Bus 22, 32, 52, 62, 123, 175, 241, 421, 460.",
            "Ouverte le <strong>30 septembre 1913</strong> avec le tronçon initial de la <strong>ligne 8</strong>. Devient station de la <strong>ligne 10</strong> en <strong>1937</strong>.",
            "À la sortie : le <strong>Stade Roland-Garros</strong> (Internationaux de France de tennis), l'<strong>Hippodrome d'Auteuil</strong> (courses d'obstacles), le <strong>Bois de Boulogne</strong> (846 ha), le <strong>Jardin des Serres d'Auteuil</strong> (serres XIXe siècle). Une <strong>station de tourisme</strong> très fréquentée pendant le <strong>tournoi de Roland-Garros</strong> (fin mai - début juin)."
        ],
        "hist_title": "1913 : porte du Bois de Boulogne et Roland-Garros",
        "hist": [
            "La station Porte d'Auteuil est <strong>inaugurée le 30 septembre 1913</strong> sur le tronçon initial de la <strong>ligne 8</strong>. Elle devient station de la <strong>ligne 10</strong> en <strong>1937</strong> lors d'un remaniement du réseau.",
            "Le <strong>Stade Roland-Garros</strong>, à 5 min à pied, est le <strong>stade emblématique des Internationaux de France de tennis</strong>. Inauguré en <strong>1928</strong> pour la <strong>défense de la Coupe Davis</strong> gagnée par les Mousquetaires français. Nommé d'après <strong>Roland Garros</strong> (1888-1918), <strong>aviateur français</strong>. <strong>34 364 places</strong>, courts répartis sur <strong>12 hectares</strong>.",
            "Le <strong>Jardin des Serres d'Auteuil</strong>, à proximité, est un <strong>jardin botanique</strong> avec <strong>cinq serres monumentales</strong> en fer et verre construites de <strong>1895 à 1898</strong> par <strong>Jean-Camille Formigé</strong>. <strong>Classé monument historique</strong>. L'<strong>Hippodrome d'Auteuil</strong> (1873), à proximité, est le <strong>plus important hippodrome français de courses d'obstacles</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Porte d'Auteuil ?", "Uniquement la <strong>M10</strong>. Bus 22, 32, 52, 62, 123, 175, 241, 421, 460."),
            ("Pour Roland-Garros ?", "<strong>~5 min à pied</strong>. Tournoi fin mai - début juin."),
            ("Pour le Bois de Boulogne ?", "<strong>Sortie directe</strong>."),
            ("Pour le Jardin des Serres d'Auteuil ?", "<strong>~5 min à pied</strong>."),
            ("Pour l'Hippodrome d'Auteuil ?", "<strong>~10 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station ancienne (1913).")
        ],
        "tips": [
            "<strong>Stade Roland-Garros</strong> à 5 min : Internationaux de France de tennis (fin mai - début juin).",
            "<strong>Jardin des Serres d'Auteuil</strong> à 5 min : serres monumentales (1895-1898).",
            "<strong>Hippodrome d'Auteuil</strong> à 10 min : courses d'obstacles.",
            "<strong>Bois de Boulogne</strong> à la sortie : 846 hectares.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎾", "Roland-Garros et Coupe Davis 1928", "Le <strong>Stade Roland-Garros</strong>, à 5 min à pied, est le <strong>stade emblématique des Internationaux de France</strong> (Grand Chelem sur terre battue). <strong>Inauguré en 1928</strong> pour permettre la <strong>défense de la Coupe Davis</strong> gagnée en 1927 par les <strong>« Mousquetaires »</strong> (Lacoste, Borotra, Cochet, Brugnon). Nommé d'après <strong>Roland Garros</strong> (1888-1918), <strong>aviateur français</strong> premier à <strong>traverser la Méditerranée</strong> en avion (1913). <strong>34 364 places</strong> sur <strong>12 hectares</strong>."),
            ("🌺", "Jardin des Serres d'Auteuil", "Le <strong>Jardin des Serres d'Auteuil</strong>, à 5 min à pied, est un <strong>jardin botanique</strong> avec <strong>cinq serres monumentales</strong> en <strong>fer et verre</strong> construites de <strong>1895 à 1898</strong> par <strong>Jean-Camille Formigé</strong>. <strong>Classé monument historique</strong>. <strong>Grande serre tropicale</strong>, serres aux palmiers, fougères, aquatiques. Plus de <strong>5 000 espèces</strong>.")
        ],
        "itin": [
            ("Roland-Garros", "porte-d-auteuil", "à pied", "Avenue Gordon-Bennett (5 min)", 5),
            ("Jardin des Serres d'Auteuil", "porte-d-auteuil", "à pied", "Avenue Gordon-Bennett (5 min)", 5),
            ("Bois de Boulogne", "porte-d-auteuil", "à pied", "Sortie directe", 2),
            ("Michel-Ange - Molitor", "michel-ange-molitor", "M10", "M10 directe (1 station)", 2),
            ("Boulogne", "boulogne-jean-jaures", "M10", "M10 directe (1 station)", 2),
            ("Quartier Latin", "cluny-la-sorbonne", "M10", "M10 directe (~18 min)", 18)
        ]
    },
    "michel-ange-molitor": {
        "addr": "Avenue de Versailles, 75016 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Michel-Ange - Molitor (M9+M10) avenue de Versailles dans le 16e. Hub 9 et 10. Proche de la Piscine Molitor (1929, rouverte en 2014).",
        "tagline": "M9 + M10 — Michel-Ange et la Piscine Molitor",
        "hero_desc": "Station <strong>Michel-Ange - Molitor</strong>, hub <strong>M9 + M10</strong>, sur l'<strong>avenue de Versailles</strong> dans le <strong>16e arrondissement</strong>. Quais <strong>M9</strong> ouverts le <strong>27 mai 1923</strong>, quais <strong>M10</strong> intégrés en <strong>1937</strong>. Proche de la <strong>Piscine Molitor</strong>, piscine Art Déco emblématique inaugurée en <strong>1929</strong>, rouverte en <strong>2014</strong>.",
        "intros": [
            "La station <strong>Michel-Ange - Molitor</strong> est implantée sur l'<strong>avenue de Versailles</strong> dans le <strong>16e arrondissement</strong>. Elle est desservie par les <strong>lignes 9 et 10</strong> du métro, formant un <strong>hub de correspondance</strong>. Bus 22, 52, 62, PC1 en correspondance.",
            "Quais <strong>ligne 9</strong> ouverts le <strong>27 mai 1923</strong> avec le tronçon <strong>Trocadéro ↔ Exelmans</strong>. Quais <strong>ligne 10</strong> intégrés en <strong>1937</strong> lors d'un remaniement du réseau.",
            "Le nom combine la <strong>rue Michel-Ange</strong> (hommage à <strong>Michel-Ange Buonarroti</strong>, 1475-1564, sculpteur et peintre italien de la <strong>Renaissance</strong>) et la <strong>rue Molitor</strong> (général d'Empire <strong>Gabriel Jean Joseph Molitor</strong>, 1770-1849). À proximité : la <strong>Piscine Molitor</strong>, emblématique."
        ],
        "hist_title": "1923-1937 : hub M9/M10 et Renaissance italienne",
        "hist": [
            "Les quais <strong>ligne 9</strong> sont <strong>inaugurés le 27 mai 1923</strong> avec le tronçon <strong>Trocadéro ↔ Exelmans</strong>. Les quais <strong>ligne 10</strong> sont intégrés en <strong>1937</strong> lors du remaniement du réseau métro.",
            "Le nom <strong>Michel-Ange</strong> rend hommage à <strong>Michel-Ange Buonarroti</strong> (<strong>6 mars 1475 - 18 février 1564</strong>), <strong>sculpteur, peintre, architecte et poète italien</strong> de la <strong>Renaissance</strong>. Œuvres : <em>David</em> (1501-1504), <em>Pietà</em> (1498-1499), <strong>plafond de la chapelle Sixtine</strong> (1508-1512), <em>Le Jugement dernier</em> (1536-1541), <strong>basilique Saint-Pierre</strong> de Rome (architecte 1546-1564).",
            "La <strong>Piscine Molitor</strong>, à proximité (avenue de la Porte-Molitor), est une <strong>piscine emblématique</strong> de Paris. <strong>Inaugurée le 1er mai 1929</strong> par les nageurs <strong>Aileen Riggin</strong> et <strong>Johnny Weissmuller</strong> (futur Tarzan au cinéma). Style <strong>Art Déco</strong>, deux bassins (été 50 m, hiver 33 m). <strong>Fermée en 1989</strong>, devenue lieu culturel underground. <strong>Rouverte en 2014</strong> après reconstruction, intégrée à un hôtel."
        ],
        "faq": [
            ("Quelles lignes desservent Michel-Ange - Molitor ?", "<strong>M9</strong> et <strong>M10</strong>. Hub du 16e. Bus 22, 52, 62, PC1."),
            ("Qui est Michel-Ange ?", "<strong>Michel-Ange Buonarroti</strong> (1475-1564), <strong>sculpteur, peintre et architecte italien</strong> de la <strong>Renaissance</strong>. Auteur du <em>David</em>, de la <strong>chapelle Sixtine</strong>."),
            ("Quand a-t-elle ouvert ?", "Quais M9 : <strong>27 mai 1923</strong>. Quais M10 : intégrés en <strong>1937</strong>."),
            ("Pour la Piscine Molitor ?", "<strong>~5 min à pied</strong>. Piscine Art Déco rouverte en 2014."),
            ("Pour Roland-Garros ?", "<strong>~10 min à pied</strong> ou <strong>M10 → Porte d'Auteuil</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Piscine Molitor</strong> à 5 min à pied : piscine Art Déco (1929), rouverte en 2014.",
            "Hub <strong>M9 + M10</strong> du 16e arrondissement.",
            "Pour <strong>Roland-Garros</strong> : 10 min à pied ou <strong>M10 → Porte d'Auteuil</strong>.",
            "Pour <strong>Bois de Boulogne</strong> : <strong>M10 → Porte d'Auteuil</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏊", "Piscine Molitor depuis 1929", "La <strong>Piscine Molitor</strong>, à 5 min à pied, est une <strong>piscine emblématique</strong> de Paris. <strong>Inaugurée le 1er mai 1929</strong> par <strong>Aileen Riggin</strong> et <strong>Johnny Weissmuller</strong> (futur Tarzan au cinéma). Style <strong>Art Déco</strong>, deux bassins (été 50 m, hiver 33 m). Lieu de baignade chic des années 1930. <strong>Fermée en 1989</strong>, le site devint un <strong>lieu culturel underground</strong> et un haut lieu du <strong>street art</strong>. <strong>Rouverte le 19 mai 2014</strong> après reconstruction, intégrée à un hôtel MGallery Sofitel."),
            ("🎨", "Michel-Ange, génie de la Renaissance", "<strong>Michel-Ange Buonarroti</strong> (<strong>1475-1564</strong>), <strong>sculpteur, peintre, architecte et poète italien</strong>. Figure majeure de la <strong>Renaissance italienne</strong>. Œuvres : <em>David</em> (1501-1504), <em>Pietà</em> de la basilique Saint-Pierre (1498-1499), <strong>plafond de la chapelle Sixtine</strong> (1508-1512), <em>Le Jugement dernier</em> (1536-1541). <strong>Architecte de la basilique Saint-Pierre de Rome</strong> (1546-1564, conception du dôme). Considéré comme l'un des plus grands artistes de tous les temps.")
        ],
        "itin": [
            ("Piscine Molitor", "michel-ange-molitor", "à pied", "Avenue de la Porte-Molitor (5 min)", 5),
            ("Roland-Garros", "porte-d-auteuil", "M10", "M10 directe (1 station)", 4),
            ("Porte d'Auteuil", "porte-d-auteuil", "M10", "M10 directe (1 station)", 2),
            ("Michel-Ange - Auteuil", "michel-ange-auteuil", "M9 + M10", "M9 ou M10 directes", 2),
            ("Trocadéro", "trocadero", "M9", "M9 directe (5 stations)", 11),
            ("Quartier Latin", "cluny-la-sorbonne", "M10", "M10 directe (~17 min)", 17)
        ]
    },
    "michel-ange-auteuil": {
        "addr": "Avenue de Versailles, 75016 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Michel-Ange - Auteuil (M9+M10) avenue de Versailles dans le 16e. Hub 9 et 10. Quartier d'Auteuil résidentiel chic, proche musée Marmottan.",
        "tagline": "M9 + M10 — quartier d'Auteuil et Avenue Mozart",
        "hero_desc": "Station <strong>Michel-Ange - Auteuil</strong>, hub <strong>M9 + M10</strong>, sur l'<strong>avenue de Versailles</strong> dans le <strong>16e arrondissement</strong>. Quais <strong>M9</strong> ouverts le <strong>27 mai 1923</strong>, quais <strong>M10</strong> intégrés en <strong>1937</strong>. <strong>Quartier d'Auteuil</strong>, résidentiel chic du <strong>16e</strong>.",
        "intros": [
            "La station <strong>Michel-Ange - Auteuil</strong> est implantée sur l'<strong>avenue de Versailles</strong> dans le <strong>16e arrondissement</strong>. Elle est desservie par les <strong>lignes 9 et 10</strong> du métro parisien, formant un <strong>hub de correspondance</strong>. Bus 22, 52, 62, 70 en correspondance.",
            "Quais <strong>ligne 9</strong> ouverts le <strong>27 mai 1923</strong> avec le tronçon Trocadéro ↔ Exelmans. Quais <strong>ligne 10</strong> intégrés en <strong>1937</strong> lors du remaniement du réseau.",
            "Le quartier d'<strong>Auteuil</strong>, ancien village rattaché à Paris en <strong>1860</strong>, est aujourd'hui un quartier <strong>résidentiel chic</strong> du <strong>16e arrondissement</strong>. À proximité : le <strong>musée Marmottan Monet</strong> (Claude Monet) et l'<strong>avenue Mozart</strong>, axe principal du quartier."
        ],
        "hist_title": "1923-1937 : hub M9/M10 et village d'Auteuil",
        "hist": [
            "Les quais <strong>ligne 9</strong> sont <strong>inaugurés le 27 mai 1923</strong> avec le tronçon <strong>Trocadéro ↔ Exelmans</strong>. Les quais <strong>ligne 10</strong> sont intégrés en <strong>1937</strong>.",
            "Le quartier d'<strong>Auteuil</strong>, ancien <strong>village rattaché à Paris en 1860</strong>, conserve une atmosphère résidentielle chic. Connu pour ses <strong>villas</strong>, ses <strong>hôtels particuliers</strong> et ses <strong>jardins privés</strong>. De nombreux artistes et écrivains y ont vécu : <strong>Léon Daudet</strong>, <strong>Marcel Proust</strong>, <strong>Léon Bloy</strong>.",
            "Le <strong>musée Marmottan Monet</strong>, à proximité (2 rue Louis-Boilly), abrite la <strong>plus grande collection au monde d'œuvres de Claude Monet</strong>. <strong>Inauguré en 1934</strong>, légué à l'Académie des Beaux-Arts par <strong>Paul Marmottan</strong>. Le tableau <em>« Impression, soleil levant »</em> (1872), à l'origine du nom <strong>« impressionnisme »</strong>, y est conservé."
        ],
        "faq": [
            ("Quelles lignes desservent Michel-Ange - Auteuil ?", "<strong>M9</strong> et <strong>M10</strong>. Hub du 16e. Bus 22, 52, 62, 70."),
            ("Quand a-t-elle ouvert ?", "Quais M9 : <strong>27 mai 1923</strong>. Quais M10 : intégrés en <strong>1937</strong>."),
            ("Pour le musée Marmottan Monet ?", "<strong>~10 min à pied</strong>. Plus grande collection de Monet au monde."),
            ("Pour Roland-Garros ?", "<strong>M10 → Porte d'Auteuil</strong> (2 stations)."),
            ("Pour Trocadéro et Tour Eiffel ?", "<strong>M9 directe</strong> vers Trocadéro (~10 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Musée Marmottan Monet</strong> à 10 min à pied : plus grande collection Monet au monde.",
            "<strong>Avenue Mozart</strong> : axe principal d'Auteuil.",
            "Quartier <strong>Auteuil</strong> résidentiel chic du 16e.",
            "Pour <strong>Trocadéro</strong> et <strong>Tour Eiffel</strong> : <strong>M9 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎨", "Musée Marmottan Monet et Impressionnisme", "Le <strong>musée Marmottan Monet</strong>, à 10 min à pied, abrite la <strong>plus grande collection d'œuvres de Claude Monet au monde</strong>. <strong>Inauguré en 1934</strong>, légué à l'<strong>Académie des Beaux-Arts</strong> par <strong>Paul Marmottan</strong>. <strong>Don de Michel Monet</strong> (fils du peintre) en <strong>1966</strong> : 165 œuvres, dont les célèbres <strong>« Nymphéas »</strong>. Le tableau <em>« Impression, soleil levant »</em> (1872), <strong>œuvre fondatrice de l'impressionnisme</strong>, y est conservé."),
            ("🏘️", "Village d'Auteuil", "Le <strong>village d'Auteuil</strong>, ancien <strong>village rattaché à Paris en 1860</strong>, conserve une atmosphère résidentielle chic dans le <strong>16e arrondissement</strong>. De nombreux <strong>artistes et écrivains</strong> y ont vécu : <strong>Marcel Proust</strong>, <strong>Léon Daudet</strong>, <strong>Léon Bloy</strong>, le compositeur <strong>Charles Gounod</strong>. <strong>Église Notre-Dame d'Auteuil</strong> (1880), <strong>Villa Montmorency</strong> (lotissement luxueux fondé en 1853).")
        ],
        "itin": [
            ("Musée Marmottan Monet", "michel-ange-auteuil", "à pied", "Rue Louis-Boilly (10 min)", 10),
            ("Roland-Garros", "porte-d-auteuil", "M10", "M10 directe (2 stations)", 5),
            ("Trocadéro et Tour Eiffel", "trocadero", "M9", "M9 directe (~10 min)", 10),
            ("Michel-Ange - Molitor", "michel-ange-molitor", "M9 + M10", "M9 ou M10 directes", 2),
            ("Église d'Auteuil", "eglise-d-auteuil", "M10", "M10 directe (1 station)", 2),
            ("Quartier Latin", "cluny-la-sorbonne", "M10", "M10 directe (~16 min)", 16)
        ]
    },
    "eglise-d-auteuil": {
        "addr": "Avenue Mozart, 75016 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Église d'Auteuil (M10) avenue Mozart dans le 16e. Église Notre-Dame d'Auteuil (1880). Quartier résidentiel chic d'Auteuil.",
        "tagline": "M10 — Notre-Dame d'Auteuil, quartier d'Auteuil",
        "hero_desc": "Station <strong>Église d'Auteuil</strong> sur l'<strong>avenue Mozart</strong> dans le <strong>16e arrondissement</strong>. Desservie par la <strong>M10</strong>, ouverte le <strong>30 septembre 1913</strong>. À proximité : l'<strong>église Notre-Dame d'Auteuil</strong> (<strong>1880</strong>), au cœur de l'<strong>ancien village d'Auteuil</strong>.",
        "intros": [
            "La station <strong>Église d'Auteuil</strong> est implantée sur l'<strong>avenue Mozart</strong> dans le <strong>16e arrondissement</strong>. Elle est desservie par la <strong>ligne 10 du métro</strong>, entre <strong>Michel-Ange - Auteuil</strong> (1 station) et <strong>Chardon-Lagache</strong> (1 station). Bus 22, 52, 62.",
            "Ouverte le <strong>30 septembre 1913</strong> avec le tronçon initial de la <strong>ligne 8</strong>. Intégrée à la <strong>ligne 10</strong> en <strong>1937</strong>.",
            "Le nom <strong>Église d'Auteuil</strong> rappelle la proximité de l'<strong>église Notre-Dame d'Auteuil</strong>, construite de <strong>1877 à 1892</strong> par <strong>Émile Vaudremer</strong>. Style <strong>néo-byzantin</strong>, dédiée à la <strong>Vierge Marie</strong>. Au cœur du <strong>quartier d'Auteuil</strong>, ancien village rattaché à Paris en <strong>1860</strong>."
        ],
        "hist_title": "1913 : Notre-Dame d'Auteuil",
        "hist": [
            "La station Église d'Auteuil est <strong>inaugurée le 30 septembre 1913</strong> sur le tronçon initial de la <strong>ligne 8</strong>. Intégrée à la <strong>ligne 10</strong> en <strong>1937</strong>.",
            "L'<strong>église Notre-Dame d'Auteuil</strong>, à proximité, est <strong>construite de 1877 à 1892</strong> par l'architecte <strong>Émile Vaudremer</strong> (1829-1914). Style <strong>néo-byzantin</strong>, dédiée à la <strong>Vierge Marie</strong>. Remplace une <strong>chapelle plus ancienne</strong> du <strong>village d'Auteuil</strong>.",
            "Le quartier d'<strong>Auteuil</strong>, ancien <strong>village rattaché à Paris en 1860</strong>, conserve son atmosphère résidentielle. L'<strong>avenue Mozart</strong>, axe principal, rend hommage à <strong>Wolfgang Amadeus Mozart</strong> (1756-1791), <strong>compositeur autrichien</strong>. À proximité : <strong>musée Marmottan Monet</strong>, <strong>villa Montmorency</strong> (lotissement luxueux 1853)."
        ],
        "faq": [
            ("Quelle ligne dessert Église d'Auteuil ?", "Uniquement la <strong>M10</strong>. Bus 22, 52, 62."),
            ("Pour Notre-Dame d'Auteuil ?", "<strong>Sortie directe</strong>. Église néo-byzantine (1877-1892)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>30 septembre 1913</strong>."),
            ("Pour le musée Marmottan ?", "<strong>~5 min à pied</strong>."),
            ("Pour Roland-Garros ?", "<strong>M10 → Porte d'Auteuil</strong> (3 stations, ~7 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station ancienne (1913).")
        ],
        "tips": [
            "<strong>Notre-Dame d'Auteuil</strong> (1877-1892) : église néo-byzantine.",
            "<strong>Musée Marmottan Monet</strong> à 5 min à pied.",
            "<strong>Avenue Mozart</strong> : axe principal d'Auteuil.",
            "Pour <strong>Roland-Garros</strong> : <strong>M10 → Porte d'Auteuil</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⛪", "Notre-Dame d'Auteuil (1877-1892)", "L'<strong>église Notre-Dame d'Auteuil</strong>, à la sortie de la station, est construite de <strong>1877 à 1892</strong> par l'architecte <strong>Émile Vaudremer</strong>. <strong>Style néo-byzantin</strong> avec influence romane. Dédiée à la <strong>Vierge Marie</strong>. Façade ornée d'une <strong>rosace</strong>. Remplace une <strong>chapelle plus ancienne</strong> du village d'Auteuil, devenue trop petite après le rattachement à Paris (1860) et la croissance du quartier."),
            ("🏡", "Villa Montmorency, enclave luxueuse", "La <strong>Villa Montmorency</strong>, à proximité, est un <strong>lotissement résidentiel fermé</strong> créé en <strong>1853</strong> sur les terres de l'ancien <strong>château de Boufflers</strong>. <strong>180 demeures</strong>, l'une des <strong>adresses les plus chères de Paris</strong>. Résidents historiques ou actuels : <strong>Carla Bruni-Sarkozy</strong>, <strong>Vincent Bolloré</strong>, <strong>Henri Salvador</strong>, <strong>Patrick Bruel</strong>. Accès réservé aux résidents.")
        ],
        "itin": [
            ("Notre-Dame d'Auteuil", "eglise-d-auteuil", "à pied", "Sortie directe", 1),
            ("Musée Marmottan Monet", "michel-ange-auteuil", "M10 + à pied", "À pied (~5 min)", 5),
            ("Michel-Ange - Auteuil", "michel-ange-auteuil", "M10", "M10 directe (1 station)", 2),
            ("Chardon-Lagache", "chardon-lagache", "M10", "M10 directe (1 station)", 2),
            ("Roland-Garros", "porte-d-auteuil", "M10", "M10 directe (3 stations)", 7),
            ("Quartier Latin", "cluny-la-sorbonne", "M10", "M10 directe (~14 min)", 14)
        ]
    },
    "chardon-lagache": {
        "addr": "Rue Chardon-Lagache, 75016 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Chardon-Lagache (M10) rue Chardon-Lagache dans le 16e. Quartier résidentiel d'Auteuil, proche Maison de Radio France.",
        "tagline": "M10 — rue Chardon-Lagache, quartier d'Auteuil",
        "hero_desc": "Station <strong>Chardon-Lagache</strong> sur la <strong>rue Chardon-Lagache</strong> dans le <strong>16e arrondissement</strong>. Desservie par la <strong>M10</strong>, ouverte le <strong>30 septembre 1913</strong>. <strong>Quartier résidentiel d'Auteuil</strong>. Proche de la <strong>Maison de la Radio</strong> (Maison de Radio France).",
        "intros": [
            "La station <strong>Chardon-Lagache</strong> est implantée sur la <strong>rue Chardon-Lagache</strong> dans le <strong>16e arrondissement</strong>. Elle est desservie par la <strong>ligne 10 du métro</strong>, entre <strong>Église d'Auteuil</strong> (1 station) et <strong>Mirabeau</strong> (1 station). Bus 22 et 72.",
            "Ouverte le <strong>30 septembre 1913</strong> sur le tronçon initial de la <strong>ligne 8</strong>. Intégrée à la <strong>ligne 10</strong> en <strong>1937</strong>.",
            "Le nom <strong>Chardon-Lagache</strong> rend hommage à <strong>Marie-Louise Chardon-Lagache</strong> (1789-1875), <strong>philanthrope</strong> qui fonda en 1855 un <strong>hospice</strong> dans le quartier. Quartier résidentiel paisible du <strong>16e</strong>, proche de la <strong>Maison de la Radio</strong>."
        ],
        "hist_title": "1913 : tronçon Auteuil et philanthropie",
        "hist": [
            "La station Chardon-Lagache est <strong>inaugurée le 30 septembre 1913</strong> sur le tronçon initial de la <strong>ligne 8</strong>. Intégrée à la <strong>ligne 10</strong> en <strong>1937</strong>.",
            "Le nom <strong>Chardon-Lagache</strong> rend hommage à <strong>Marie-Louise Chardon-Lagache</strong> (<strong>1789-1875</strong>), <strong>philanthrope française</strong>. Elle fonda en <strong>1855</strong> un <strong>hospice pour personnes âgées</strong> dans le quartier d'Auteuil — l'<strong>hospice Chardon-Lagache</strong>, qui existe toujours (devenu <strong>hôpital Chardon-Lagache</strong>).",
            "Le quartier est aujourd'hui résidentiel paisible du <strong>16e arrondissement</strong>. À proximité : la <strong>Maison de la Radio</strong> (Maison de Radio France, inaugurée en <strong>1963</strong> par le général de Gaulle, conçue par <strong>Henry Bernard</strong>), siège de <strong>Radio France</strong>. Rénovée et rouverte en <strong>2014</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Chardon-Lagache ?", "Uniquement la <strong>M10</strong>. Bus 22 et 72."),
            ("Qui est Chardon-Lagache ?", "<strong>Marie-Louise Chardon-Lagache</strong> (1789-1875), <strong>philanthrope française</strong>. Fondatrice d'un <strong>hospice</strong> dans le quartier en 1855."),
            ("Quand a-t-elle ouvert ?", "Le <strong>30 septembre 1913</strong>."),
            ("Pour la Maison de la Radio ?", "<strong>~10 min à pied</strong> via l'avenue du Président-Kennedy."),
            ("Pour la Seine ?", "<strong>~5 min à pied</strong> via l'avenue du Président-Kennedy."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station ancienne (1913).")
        ],
        "tips": [
            "<strong>Maison de la Radio</strong> à 10 min à pied : siège de Radio France.",
            "Quartier résidentiel paisible du <strong>16e</strong>.",
            "Pour <strong>Bois de Boulogne</strong> : <strong>M10 → Porte d'Auteuil</strong>.",
            "Pour <strong>Quartier Latin</strong> : <strong>M10 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("📻", "Maison de la Radio (1963)", "La <strong>Maison de la Radio</strong> (devenue <strong>Maison de Radio France</strong> en 2014), à 10 min à pied, est le <strong>siège de Radio France</strong>. <strong>Inaugurée le 14 décembre 1963</strong> par le général <strong>de Gaulle</strong>. Conçue par l'architecte <strong>Henry Bernard</strong>, <strong>bâtiment circulaire</strong> de <strong>500 mètres de circonférence</strong> autour d'une <strong>tour centrale de 70 m</strong>. Plus de <strong>4 000 employés</strong>. <strong>Rénovée et rouverte en 2014</strong>."),
            ("🏥", "Hospice Chardon-Lagache (1855)", "L'<strong>hospice Chardon-Lagache</strong>, fondé en <strong>1855</strong> par la <strong>philanthrope Marie-Louise Chardon-Lagache</strong>, accueillait des <strong>personnes âgées démunies</strong> du quartier d'Auteuil. Devenu <strong>hôpital Chardon-Lagache</strong>, il existe toujours et fait partie de l'<strong>Assistance publique - Hôpitaux de Paris (AP-HP)</strong>. Spécialisé en <strong>gériatrie</strong>.")
        ],
        "itin": [
            ("Maison de la Radio", "ranelagh", "M10 + bus", "À pied (~10 min) ou bus 72", 10),
            ("Église d'Auteuil", "eglise-d-auteuil", "M10", "M10 directe (1 station)", 2),
            ("Mirabeau", "mirabeau", "M10", "M10 directe (1 station)", 2),
            ("Roland-Garros", "porte-d-auteuil", "M10", "M10 directe (4 stations)", 8),
            ("Musée Marmottan Monet", "michel-ange-auteuil", "M10", "M10 directe (2 stations)", 5),
            ("Quartier Latin", "cluny-la-sorbonne", "M10", "M10 directe (~13 min)", 13)
        ]
    },
    "javel-andre-citroen": {
        "addr": "Quai André-Citroën, 75015 Paris", "arr": "15e arrondissement (Paris)",
        "seo": "Station Javel - André Citroën (M10) dans le 15e. Parc André Citroën (1992) et RER C Javel à proximité. Hommage à André Citroën, industriel automobile.",
        "tagline": "M10 — Parc André Citroën et industrie automobile",
        "hero_desc": "Station <strong>Javel - André Citroën</strong> sur le <strong>quai André-Citroën</strong> dans le <strong>15e arrondissement</strong>. Desservie par la <strong>M10</strong>, ouverte le <strong>30 septembre 1913</strong>. À proximité du <strong>Parc André Citroën</strong> (<strong>14 ha</strong>, jardin contemporain ouvert en <strong>1992</strong>) et de la <strong>gare RER C Javel</strong>.",
        "intros": [
            "La station <strong>Javel - André Citroën</strong> est implantée sur le <strong>quai André-Citroën</strong>, le long de la Seine, dans le <strong>15e arrondissement</strong>. Elle est desservie par la <strong>ligne 10 du métro</strong>, entre <strong>Mirabeau</strong> (1 station) et <strong>Charles Michels</strong> (1 station). À courte distance de la <strong>gare RER C Javel</strong>. Bus 30, 42, 62, 70, 88, PC1.",
            "Ouverte le <strong>30 septembre 1913</strong> avec le tronçon initial de la <strong>ligne 8</strong>. Intégrée à la <strong>ligne 10</strong> en <strong>1937</strong>. Renommée <strong>« Javel - André Citroën »</strong> en <strong>1993</strong> à l'occasion de l'inauguration du Parc André Citroën.",
            "Le <strong>Parc André Citroën</strong>, à la sortie, est l'un des <strong>grands parcs contemporains</strong> de Paris (<strong>14 hectares</strong>, ouvert en <strong>1992</strong>). Conçu par les architectes <strong>Patrick Berger</strong>, <strong>Jean-François Jodry</strong>, <strong>Jean-Paul Viguier</strong> et les paysagistes <strong>Gilles Clément</strong> et <strong>Alain Provost</strong>. Hommage à <strong>André Citroën</strong> (<strong>1878-1935</strong>), <strong>industriel français</strong>, fondateur des automobiles <strong>Citroën</strong> en 1919."
        ],
        "hist_title": "1913 : ancien Javel, devenu André Citroën",
        "hist": [
            "La station Javel est <strong>inaugurée le 30 septembre 1913</strong> sur le tronçon initial de la <strong>ligne 8</strong>. Intégrée à la <strong>ligne 10</strong> en <strong>1937</strong>.",
            "Renommée <strong>« Javel - André Citroën »</strong> en <strong>1993</strong>, à l'occasion de l'<strong>inauguration du Parc André Citroën</strong> (1992). Le nom <strong>Javel</strong> rappelle l'<strong>ancien village de Javel</strong>, rattaché à Paris en <strong>1860</strong>. <strong>Étymologie</strong> incertaine, peut-être lié à <em>Gevald</em>, ancien lieu-dit. La <strong>fabrique de Javel</strong> y produisit dès <strong>1779</strong> l'<strong>eau de Javel</strong> (chlorure de sodium hypochlorite, désinfectant).",
            "<strong>André Citroën</strong> (<strong>5 février 1878 - 3 juillet 1935</strong>), <strong>industriel français</strong>. Fonde en <strong>1919</strong> la <strong>Société anonyme des automobiles Citroën</strong>. Premier constructeur français de production en série (modèle <strong>Type A</strong>, 1919). Pionnier du <strong>marketing</strong> (illumination de la Tour Eiffel aux couleurs Citroën, 1925-1934). <strong>Croisière Noire</strong> (1924-1925) et <strong>Croisière Jaune</strong> (1931-1932). <strong>Usines Citroën</strong> du quai de Javel (1915-1980), remplacées par le <strong>Parc André Citroën</strong> en 1992."
        ],
        "faq": [
            ("Quelle ligne dessert Javel - André Citroën ?", "<strong>M10</strong> et à proximité <strong>RER C Javel</strong>. Bus 30, 42, 62, 70, 88, PC1."),
            ("Quand a-t-elle ouvert ?", "Le <strong>30 septembre 1913</strong>, renommée en <strong>1993</strong>."),
            ("Pour le Parc André Citroën ?", "<strong>Sortie directe</strong>. 14 hectares, jardin contemporain (1992)."),
            ("Pour le RER C Javel ?", "<strong>~3 min à pied</strong>."),
            ("Qui est André Citroën ?", "<strong>André Citroën</strong> (1878-1935), <strong>industriel français</strong>. <strong>Fondateur des automobiles Citroën</strong> en <strong>1919</strong>. Pionnier de la production automobile en série."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station ancienne (1913).")
        ],
        "tips": [
            "<strong>Parc André Citroën</strong> à la sortie : 14 ha, jardin contemporain, <strong>ballon captif</strong> (panorama Paris).",
            "<strong>RER C Javel</strong> à 3 min à pied : vers Versailles, Saint-Quentin, aéroport CDG.",
            "<strong>Berges de la Seine</strong> à proximité.",
            "Pour <strong>Quartier Latin</strong> : <strong>M10 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🌳", "Parc André Citroën (1992), 14 hectares", "Le <strong>Parc André Citroën</strong>, à la sortie de la station, est l'un des <strong>grands parcs contemporains de Paris</strong> (<strong>14 hectares</strong>, ouvert en <strong>1992</strong>). Construit sur les anciennes <strong>usines Citroën</strong> du quai de Javel (1915-1980). Conçu par les architectes <strong>Patrick Berger</strong>, <strong>Jean-François Jodry</strong>, <strong>Jean-Paul Viguier</strong> et les paysagistes <strong>Gilles Clément</strong> et <strong>Alain Provost</strong>. <strong>Six jardins thématiques</strong>, <strong>grandes serres</strong>, <strong>esplanade centrale</strong> et célèbre <strong>ballon captif</strong> (panorama de Paris depuis 150 m d'altitude)."),
            ("🚗", "André Citroën, pionnier automobile", "<strong>André Citroën</strong> (1878-1935), <strong>industriel français</strong>. <strong>Fonde la Société anonyme des automobiles Citroën</strong> en <strong>1919</strong>. <strong>Premier constructeur français</strong> à appliquer les <strong>méthodes de production de masse</strong> (Type A, 1919). Pionnier du <strong>marketing automobile</strong> : <strong>illumination de la Tour Eiffel aux couleurs Citroën</strong> de <strong>1925 à 1934</strong>. <strong>Expéditions célèbres</strong> : <strong>Croisière Noire</strong> à travers l'Afrique (1924-1925), <strong>Croisière Jaune</strong> à travers l'Asie (1931-1932).")
        ],
        "itin": [
            ("Parc André Citroën", "javel-andre-citroen", "à pied", "Sortie directe", 2),
            ("RER C Javel (vers Versailles)", "javel-andre-citroen", "à pied", "Rue Saint-Charles (3 min)", 3),
            ("Charles Michels", "charles-michels", "M10", "M10 directe (1 station)", 2),
            ("Mirabeau", "mirabeau", "M10", "M10 directe (1 station)", 2),
            ("Quartier Latin", "cluny-la-sorbonne", "M10", "M10 directe (~11 min)", 11),
            ("Gare d'Austerlitz", "gare-d-austerlitz", "M10", "M10 directe (terminus est)", 18)
        ]
    },
    "segur": {
        "addr": "Avenue de Ségur, 75007 Paris", "arr": "7e arrondissement (Paris)",
        "seo": "Station Ségur (M10) avenue de Ségur dans le 7e. Hommage au maréchal de Ségur. Quartier 7e proche Champ-de-Mars, École Militaire, UNESCO.",
        "tagline": "M10 — avenue de Ségur, quartier 7e",
        "hero_desc": "Station <strong>Ségur</strong> sur l'<strong>avenue de Ségur</strong> dans le <strong>7e arrondissement</strong>. Desservie par la <strong>M10</strong>, ouverte le <strong>30 décembre 1923</strong>. Hommage à <strong>Philippe Henri, marquis de Ségur</strong> (<strong>1724-1801</strong>), <strong>maréchal de France</strong>. Quartier institutionnel proche de l'<strong>UNESCO</strong>, du <strong>Champ-de-Mars</strong> et de l'<strong>École Militaire</strong>.",
        "intros": [
            "La station <strong>Ségur</strong> est implantée sur l'<strong>avenue de Ségur</strong> dans le <strong>7e arrondissement</strong>. Elle est desservie par la <strong>ligne 10 du métro</strong>, entre <strong>La Motte-Picquet - Grenelle</strong> (1 station) et <strong>Duroc</strong> (1 station). Bus 28, 80, 82, 92.",
            "Ouverte le <strong>30 décembre 1923</strong> avec le tronçon initial <strong>Invalides ↔ Croix-Rouge</strong> de la <strong>ligne 10</strong> (à l'époque, ligne autonome reliant Invalides à Sèvres-Babylone).",
            "Le nom <strong>Ségur</strong> rend hommage à <strong>Philippe Henri, marquis de Ségur</strong> (<strong>1724-1801</strong>), <strong>maréchal de France</strong> et <strong>secrétaire d'État à la Guerre</strong> sous Louis XVI (1780-1787). Quartier institutionnel : à proximité de l'<strong>UNESCO</strong> (siège mondial avenue de Ségur, 1958), du <strong>Champ-de-Mars</strong> et de l'<strong>École Militaire</strong>."
        ],
        "hist_title": "1923 : Ségur, maréchal de France",
        "hist": [
            "La station Ségur est <strong>inaugurée le 30 décembre 1923</strong> avec le tronçon initial de la <strong>ligne 10</strong> entre <strong>Invalides et Croix-Rouge</strong> (station fermée depuis 1939).",
            "Le nom <strong>Ségur</strong> rend hommage à <strong>Philippe Henri, marquis de Ségur</strong> (<strong>20 janvier 1724 - 3 octobre 1801</strong>), <strong>maréchal de France</strong>. Carrière militaire dans les <strong>guerres de Succession d'Autriche</strong> et de <strong>Sept Ans</strong>. <strong>Secrétaire d'État à la Guerre</strong> sous <strong>Louis XVI</strong> de <strong>1780 à 1787</strong>.",
            "Le quartier est aujourd'hui institutionnel : <strong>UNESCO</strong> (Organisation des Nations Unies pour l'éducation, la science et la culture, siège mondial inauguré en <strong>1958</strong> par <strong>Marcel Breuer</strong>, <strong>Pier Luigi Nervi</strong> et <strong>Bernard Zehrfuss</strong>). À proximité également le <strong>Champ-de-Mars</strong>, l'<strong>École Militaire</strong> (1751, Ange-Jacques Gabriel)."
        ],
        "faq": [
            ("Quelle ligne dessert Ségur ?", "Uniquement la <strong>M10</strong>. Bus 28, 80, 82, 92."),
            ("Qui est le marquis de Ségur ?", "<strong>Philippe Henri, marquis de Ségur</strong> (1724-1801), <strong>maréchal de France</strong>. <strong>Secrétaire d'État à la Guerre</strong> sous Louis XVI (1780-1787)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>30 décembre 1923</strong>."),
            ("Pour l'UNESCO ?", "<strong>~5 min à pied</strong> via l'avenue de Ségur."),
            ("Pour la Tour Eiffel ?", "<strong>~15 min à pied</strong> via le Champ-de-Mars."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>UNESCO</strong> à 5 min à pied : siège mondial (1958).",
            "<strong>Champ-de-Mars</strong> et <strong>Tour Eiffel</strong> à 15 min à pied.",
            "<strong>École Militaire</strong> (1751) à proximité.",
            "Quartier institutionnel et ambassades du <strong>7e</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🌍", "UNESCO, siège mondial depuis 1958", "L'<strong>UNESCO</strong> (Organisation des Nations Unies pour l'éducation, la science et la culture), à 5 min à pied, a son <strong>siège mondial</strong> au <strong>7 place de Fontenoy</strong>. <strong>Inauguré le 3 novembre 1958</strong>. Conçu par les architectes <strong>Marcel Breuer</strong> (États-Unis), <strong>Pier Luigi Nervi</strong> (Italie) et <strong>Bernard Zehrfuss</strong> (France). <strong>Bâtiment Y</strong> en forme d'étoile à trois branches. <strong>193 États membres</strong>. <strong>Œuvres d'art</strong> : Picasso, Miró, Calder, Tapiès."),
            ("🎖️", "Maréchal de Ségur, ministre de Louis XVI", "<strong>Philippe Henri, marquis de Ségur</strong> (1724-1801), <strong>maréchal de France</strong>. Sert dans les <strong>guerres de Succession d'Autriche</strong> et de <strong>Sept Ans</strong>. <strong>Secrétaire d'État à la Guerre</strong> sous Louis XVI de <strong>1780 à 1787</strong>. <strong>Édit de Ségur (1781)</strong> : impose à tous les officiers de l'<strong>armée royale</strong> de prouver <strong>quatre quartiers de noblesse</strong>. Mesure controversée qui frustre la noblesse de robe et la bourgeoisie.")
        ],
        "itin": [
            ("UNESCO", "ecole-militaire", "M10 + à pied", "À pied (5 min)", 5),
            ("Champ-de-Mars et Tour Eiffel", "champ-de-mars-tour-eiffel", "M10 + RER C", "À pied (15 min) ou M10 + RER C", 15),
            ("Duroc", "duroc", "M10", "M10 directe (1 station)", 2),
            ("Invalides", "invalides", "M13 + M10", "M10 → Duroc + M13", 7),
            ("Quartier Latin", "cluny-la-sorbonne", "M10", "M10 directe (~10 min)", 10),
            ("Gare d'Austerlitz", "gare-d-austerlitz", "M10", "M10 directe (terminus est)", 15)
        ]
    },
    "duroc": {
        "addr": "Boulevard des Invalides, 75007 Paris", "arr": "7e arrondissement (Paris)",
        "seo": "Station Duroc (M10+M13) boulevard des Invalides. Hub M10 et M13. Hommage au maréchal Duroc, proche des Invalides et du Bon Marché.",
        "tagline": "M10 + M13 — Duroc, grand maréchal du palais",
        "hero_desc": "Station <strong>Duroc</strong>, hub <strong>M10 + M13</strong>, sur le <strong>boulevard des Invalides</strong> dans le <strong>7e arrondissement</strong>. Quais <strong>M10</strong> ouverts le <strong>30 décembre 1923</strong>, quais <strong>M13</strong> le <strong>20 février 1973</strong>. Hommage au <strong>maréchal Duroc</strong> (<strong>1772-1813</strong>), <strong>grand maréchal du palais</strong> de Napoléon.",
        "intros": [
            "La station <strong>Duroc</strong> est implantée sur le <strong>boulevard des Invalides</strong> dans le <strong>7e arrondissement</strong>. Elle est desservie par les <strong>lignes 10 et 13</strong> du métro parisien, formant un <strong>hub de correspondance</strong>. Bus 28, 39, 70, 87, 92 en correspondance.",
            "Quais <strong>ligne 10</strong> ouverts le <strong>30 décembre 1923</strong> avec le tronçon initial de la M10. Quais <strong>ligne 13</strong> ouverts le <strong>20 février 1973</strong> avec le prolongement de la M13 vers le sud.",
            "Le nom <strong>Duroc</strong> rend hommage à <strong>Géraud Christophe Michel Duroc, duc de Frioul</strong> (<strong>1772-1813</strong>), <strong>général d'Empire</strong> et <strong>grand maréchal du palais</strong> de Napoléon. À proximité : le <strong>Bon Marché</strong> (premier grand magasin parisien, 1838) et les <strong>Invalides</strong> (hôtel des Invalides, tombeau de Napoléon)."
        ],
        "hist_title": "1923-1973 : hub M10/M13 et maréchal Duroc",
        "hist": [
            "Les quais <strong>ligne 10</strong> sont <strong>inaugurés le 30 décembre 1923</strong> avec le tronçon initial de la M10. Les quais <strong>ligne 13</strong> ouvrent le <strong>20 février 1973</strong> avec le prolongement de la M13 entre <strong>Miromesnil et Champs-Élysées - Clemenceau</strong> puis vers le sud.",
            "Le nom <strong>Duroc</strong> rend hommage à <strong>Géraud Christophe Michel Duroc, duc de Frioul</strong> (<strong>25 octobre 1772 - 23 mai 1813</strong>), <strong>général d'Empire</strong> et <strong>grand maréchal du palais</strong> de Napoléon Ier. Né à Pont-à-Mousson (Meurthe-et-Moselle).",
            "<strong>Ami intime de Napoléon</strong> depuis le <strong>siège de Toulon</strong> (1793), il devient <strong>aide de camp</strong> puis <strong>grand maréchal du palais</strong> (organisation de la cour impériale). Diplomate, il négocie plusieurs traités. <strong>Mort au combat</strong> à la <strong>bataille de Bautzen</strong> (Saxe) le <strong>23 mai 1813</strong>. Napoléon, présent, fut bouleversé : <em>« Adieu, mon ami. Reposez en paix ! »</em>. Inhumé aux <strong>Invalides</strong>."
        ],
        "faq": [
            ("Quelles lignes desservent Duroc ?", "<strong>M10</strong> et <strong>M13</strong>. Hub. Bus 28, 39, 70, 87, 92."),
            ("Qui est Duroc ?", "<strong>Géraud Duroc</strong> (1772-1813), <strong>grand maréchal du palais</strong> de Napoléon. Ami intime de l'Empereur. Inhumé aux <strong>Invalides</strong>."),
            ("Quand a-t-elle ouvert ?", "Quais M10 : <strong>30 décembre 1923</strong>. Quais M13 : <strong>20 février 1973</strong>."),
            ("Pour les Invalides ?", "<strong>~10 min à pied</strong> ou <strong>M13 → Varenne</strong>."),
            ("Pour Le Bon Marché ?", "<strong>~5 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Le Bon Marché</strong> à 5 min à pied : premier grand magasin parisien (1838).",
            "<strong>Invalides</strong> et <strong>tombeau de Napoléon</strong> à 10 min à pied.",
            "Hub <strong>M10 + M13</strong> du 7e arrondissement.",
            "Pour <strong>Saint-Germain-des-Prés</strong> : <strong>M10 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎖️", "Duroc, ami intime de Napoléon", "<strong>Géraud Duroc</strong> (1772-1813), <strong>grand maréchal du palais</strong> de Napoléon. Né à Pont-à-Mousson. <strong>Ami intime de Napoléon</strong> depuis le <strong>siège de Toulon</strong> (1793). <strong>Aide de camp</strong>, puis <strong>grand maréchal du palais</strong> (organise la cour impériale, dirige la maison de l'Empereur). Diplomate négociant plusieurs traités. <strong>Mort au combat</strong> à la <strong>bataille de Bautzen</strong> (Saxe) le <strong>23 mai 1813</strong>. Napoléon, présent à ses côtés, fut bouleversé. <strong>Inhumé aux Invalides</strong>."),
            ("🛍️", "Le Bon Marché, premier grand magasin", "<strong>Le Bon Marché</strong>, à 5 min à pied, est le <strong>premier grand magasin</strong> du genre dans le monde. Fondé en <strong>1838</strong> par les frères <strong>Videau</strong>, repris en <strong>1852</strong> par <strong>Aristide Boucicaut</strong>, qui révolutionne le commerce de détail : <strong>prix fixes</strong>, <strong>libre entrée</strong>, <strong>livraisons à domicile</strong>, <strong>soldes</strong>, <strong>catalogue de vente par correspondance</strong>. Inspire Émile Zola pour son roman <em>Au Bonheur des Dames</em> (1883).")
        ],
        "itin": [
            ("Le Bon Marché", "sevres-babylone", "M10", "M10 directe (1 station)", 3),
            ("Invalides et tombeau de Napoléon", "invalides", "M13", "M13 directe", 5),
            ("Saint-Germain-des-Prés", "saint-germain-des-pres", "M10 + M4", "M10 → Sèvres-Babylone + M12 ou via Mabillon", 8),
            ("Montparnasse", "montparnasse-bienvenue", "M13", "M13 directe (3 stations)", 7),
            ("Tour Eiffel via Champ-de-Mars", "champ-de-mars-tour-eiffel", "M10 + RER C", "M10 → Ségur + à pied", 15),
            ("Quartier Latin", "cluny-la-sorbonne", "M10", "M10 directe (~8 min)", 8)
        ]
    },
    "vaneau": {
        "addr": "Rue de Sèvres, 75007 Paris", "arr": "7e arrondissement (Paris)",
        "seo": "Station Vaneau (M10) rue de Sèvres dans le 7e. Quartier institutionnel proche du Bon Marché, de Sciences Po et de la rue du Bac.",
        "tagline": "M10 — rue Vaneau, quartier 7e",
        "hero_desc": "Station <strong>Vaneau</strong> sur la <strong>rue de Sèvres</strong> dans le <strong>7e arrondissement</strong>. Desservie par la <strong>M10</strong>, ouverte le <strong>30 décembre 1923</strong>. Quartier institutionnel du <strong>7e</strong>, proche du <strong>Bon Marché</strong>, de la <strong>rue du Bac</strong> et de plusieurs <strong>ministères</strong>.",
        "intros": [
            "La station <strong>Vaneau</strong> est implantée sur la <strong>rue de Sèvres</strong> dans le <strong>7e arrondissement</strong>. Elle est desservie par la <strong>ligne 10 du métro</strong>, entre <strong>Duroc</strong> (1 station) et <strong>Sèvres - Babylone</strong> (1 station). Bus 39, 70, 87.",
            "Ouverte le <strong>30 décembre 1923</strong> avec le tronçon initial de la <strong>ligne 10</strong>.",
            "Le nom <strong>Vaneau</strong> rappelle la <strong>rue Vaneau</strong> à proximité. Quartier institutionnel et résidentiel du <strong>7e arrondissement</strong>, à proximité du <strong>Bon Marché</strong>, de plusieurs <strong>ministères</strong> (Affaires étrangères, Défense, Outre-Mer), de la <strong>rue du Bac</strong> et de l'<strong>hôtel Matignon</strong> (Premier ministre)."
        ],
        "hist_title": "1923 : ligne 10 et 7e institutionnel",
        "hist": [
            "La station Vaneau est <strong>inaugurée le 30 décembre 1923</strong> avec le tronçon initial de la <strong>ligne 10</strong>.",
            "La <strong>rue Vaneau</strong>, qui donne son nom à la station, est une voie du <strong>7e arrondissement</strong>. Le nom rend hommage à <strong>Louis Vaneau</strong>, jeune étudiant en pharmacie engagé dans les <strong>Trois Glorieuses</strong> (Révolution de juillet 1830).",
            "Le quartier est aujourd'hui <strong>institutionnel et résidentiel</strong> : à proximité du <strong>Bon Marché</strong> (1838), de la <strong>rue du Bac</strong> (commerces, antiquaires, librairies), de plusieurs <strong>ministères</strong> du <strong>7e</strong>. <strong>Sciences Po</strong> (Institut d'études politiques de Paris) à proximité (rue Saint-Guillaume)."
        ],
        "faq": [
            ("Quelle ligne dessert Vaneau ?", "Uniquement la <strong>M10</strong>. Bus 39, 70, 87."),
            ("Quand a-t-elle ouvert ?", "Le <strong>30 décembre 1923</strong>."),
            ("Pour le Bon Marché ?", "<strong>~3 min à pied</strong>."),
            ("Pour Sciences Po ?", "<strong>~10 min à pied</strong>."),
            ("Pour le musée d'Orsay ?", "<strong>~15 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Le Bon Marché</strong> à 3 min : premier grand magasin (1838).",
            "<strong>Rue du Bac</strong> à proximité : commerces, antiquaires, librairies.",
            "<strong>Sciences Po</strong> à 10 min à pied.",
            "Quartier institutionnel et résidentiel du <strong>7e</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Quartier institutionnel du 7e", "Le <strong>7e arrondissement</strong>, autour de la station Vaneau, est l'un des <strong>plus institutionnels de Paris</strong>. Concentre plusieurs <strong>ministères</strong> : <strong>ministère des Affaires étrangères</strong> (Quai d'Orsay), <strong>ministère de la Défense</strong> (Hôtel de Brienne), <strong>ministère de l'Outre-mer</strong>. <strong>Hôtel Matignon</strong> (Premier ministre) à proximité. <strong>Assemblée nationale</strong> au <strong>Palais Bourbon</strong>. Quartier d'<strong>ambassades</strong> et d'<strong>hôtels particuliers</strong>."),
            ("🛍️", "Rue du Bac, art de vivre parisien", "La <strong>rue du Bac</strong>, à proximité, est l'une des <strong>plus prestigieuses rues du 7e</strong>. Long de 1,2 km, elle concentre <strong>antiquaires</strong>, <strong>librairies anciennes</strong>, <strong>galeries d'art</strong>, <strong>fleuristes</strong>, <strong>fromageries</strong> et <strong>chocolateries de luxe</strong>. <strong>Marché de la rue de Sèvres</strong> à proximité. Quartier d'<strong>art de vivre parisien</strong>.")
        ],
        "itin": [
            ("Le Bon Marché", "sevres-babylone", "M10", "M10 directe (1 station) ou à pied (3 min)", 3),
            ("Rue du Bac", "rue-du-bac", "M10 + M12", "M10 → Sèvres-Babylone + M12", 6),
            ("Sciences Po", "saint-germain-des-pres", "M10 + M4", "À pied (10 min)", 10),
            ("Musée d'Orsay", "musee-d-orsay", "M10 + RER C", "M10 → Sèvres-Babylone + M12", 15),
            ("Quartier Latin", "cluny-la-sorbonne", "M10", "M10 directe (~7 min)", 7),
            ("Saint-Germain-des-Prés", "saint-germain-des-pres", "M10 + M4", "M10 → Mabillon + à pied", 7)
        ]
    },
    "cardinal-lemoine": {
        "addr": "Rue du Cardinal-Lemoine, 75005 Paris", "arr": "5e arrondissement (Paris)",
        "seo": "Station Cardinal Lemoine (M10) rue du Cardinal-Lemoine dans le 5e (Quartier Latin). Ernest Hemingway logea au 74 rue du Cardinal-Lemoine en 1921-1923.",
        "tagline": "M10 — rue du Cardinal-Lemoine, Hemingway et Quartier Latin",
        "hero_desc": "Station <strong>Cardinal Lemoine</strong> sur la <strong>rue du Cardinal-Lemoine</strong> dans le <strong>5e arrondissement</strong>, au cœur du <strong>Quartier Latin</strong>. Desservie par la <strong>M10</strong>, ouverte le <strong>26 avril 1931</strong>. <strong>Ernest Hemingway</strong> logea au <strong>74 rue du Cardinal-Lemoine</strong> de <strong>1921 à 1923</strong>.",
        "intros": [
            "La station <strong>Cardinal Lemoine</strong> est implantée sur la <strong>rue du Cardinal-Lemoine</strong> dans le <strong>5e arrondissement</strong>, au cœur du <strong>Quartier Latin</strong>. Elle est desservie par la <strong>ligne 10 du métro</strong>, entre <strong>Maubert - Mutualité</strong> (1 station) et <strong>Jussieu</strong> (1 station). Bus 47, 86, 89.",
            "Ouverte le <strong>26 avril 1931</strong> avec le prolongement de la <strong>ligne 10</strong> entre <strong>Maubert - Mutualité et Jussieu</strong>.",
            "Le nom <strong>Cardinal Lemoine</strong> rend hommage à <strong>Jean Lemoine</strong> (<strong>v. 1250 - 22 août 1313</strong>), <strong>cardinal et juriste français</strong>, fondateur en <strong>1302</strong> du <strong>collège du Cardinal-Lemoine</strong> dans le Quartier Latin (collège de l'<strong>université de Paris</strong>). <strong>Ernest Hemingway</strong> logea au <strong>74 rue du Cardinal-Lemoine</strong> de <strong>1921 à 1923</strong> avec son épouse Hadley."
        ],
        "hist_title": "1931 : Cardinal Lemoine et collèges médiévaux",
        "hist": [
            "La station Cardinal Lemoine est <strong>inaugurée le 26 avril 1931</strong> avec le prolongement de la <strong>ligne 10</strong> entre <strong>Maubert - Mutualité et Jussieu</strong>.",
            "Le nom <strong>Cardinal Lemoine</strong> rend hommage à <strong>Jean Lemoine</strong> (<strong>v. 1250 - 22 août 1313</strong>), <strong>cardinal et juriste français</strong>. <strong>Cardinal en 1294</strong>, membre du <strong>conseil du roi Philippe IV le Bel</strong>. Fonde en <strong>1302</strong> le <strong>collège du Cardinal-Lemoine</strong> dans le Quartier Latin, l'un des <strong>collèges de l'université de Paris</strong>.",
            "<strong>Ernest Hemingway</strong> (<strong>1899-1961</strong>), <strong>écrivain américain</strong>, futur <strong>Prix Nobel de littérature 1954</strong>, logea avec son épouse <strong>Hadley</strong> au <strong>74 rue du Cardinal-Lemoine</strong> de <strong>1921 à 1923</strong>. Il y rédigea ses <strong>premiers articles de presse</strong> pour le <em>Toronto Star</em>. Il évoquera ce séjour dans <em>Paris est une fête</em> (publié posthume en 1964). Une <strong>plaque commémorative</strong> est apposée sur l'immeuble."
        ],
        "faq": [
            ("Quelle ligne dessert Cardinal Lemoine ?", "Uniquement la <strong>M10</strong>. Bus 47, 86, 89."),
            ("Quand a-t-elle ouvert ?", "Le <strong>26 avril 1931</strong>."),
            ("Qui est le Cardinal Lemoine ?", "<strong>Jean Lemoine</strong> (v. 1250-1313), <strong>cardinal et juriste français</strong>. Fonde en <strong>1302</strong> le <strong>collège du Cardinal-Lemoine</strong> de l'université de Paris."),
            ("Où vécut Hemingway ?", "Au <strong>74 rue du Cardinal-Lemoine</strong> de <strong>1921 à 1923</strong> avec son épouse Hadley. <strong>Plaque commémorative</strong> sur l'immeuble."),
            ("Pour le Panthéon ?", "<strong>~5 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>74 rue du Cardinal-Lemoine</strong> : <strong>Hemingway</strong> y vécut (1921-1923). Plaque commémorative.",
            "<strong>Panthéon</strong> à 5 min à pied.",
            "<strong>Jardin du Luxembourg</strong> à 15 min à pied.",
            "Cœur du <strong>Quartier Latin</strong> : Sorbonne, librairies, cafés littéraires.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("📚", "Hemingway au 74 rue du Cardinal-Lemoine", "<strong>Ernest Hemingway</strong> (1899-1961), <strong>écrivain américain</strong>, futur <strong>Prix Nobel de littérature 1954</strong>, logea au <strong>74 rue du Cardinal-Lemoine</strong> de <strong>1921 à 1923</strong> avec son épouse <strong>Hadley Richardson</strong>. <strong>Premier appartement parisien</strong> du jeune couple. Hemingway, correspondant pour le <em>Toronto Star</em>, fréquente alors les milieux littéraires parisiens : <strong>Gertrude Stein</strong>, <strong>James Joyce</strong>, <strong>Ezra Pound</strong>, <strong>F. Scott Fitzgerald</strong>. Il évoquera ce séjour dans son livre <em>Paris est une fête</em> (publié posthume en 1964). <strong>Plaque commémorative</strong> sur l'immeuble."),
            ("⛪", "Collège du Cardinal-Lemoine (1302)", "Le <strong>collège du Cardinal-Lemoine</strong>, fondé en <strong>1302</strong> par le <strong>cardinal Jean Lemoine</strong>, était l'un des <strong>collèges de l'université de Paris médiévale</strong>. <strong>Spécialisé dans le droit canon</strong>. Acceptait des <strong>étudiants pauvres du diocèse d'Amiens</strong>. Le collège a fonctionné jusqu'à la <strong>Révolution française</strong> (1792). Les bâtiments ont disparu, mais le nom subsiste dans la rue et la station de métro.")
        ],
        "itin": [
            ("Panthéon", "cardinal-lemoine", "à pied", "Rue du Cardinal-Lemoine (5 min)", 5),
            ("Jardin du Luxembourg", "luxembourg", "M10 + RER B", "À pied (15 min) ou RER B", 15),
            ("Sorbonne", "cluny-la-sorbonne", "M10", "M10 directe (2 stations)", 4),
            ("Jussieu", "jussieu", "M10", "M10 directe (1 station)", 2),
            ("Notre-Dame de Paris", "saint-michel-notre-dame", "M10 + à pied", "À pied (10 min)", 10),
            ("Gare d'Austerlitz", "gare-d-austerlitz", "M10", "M10 directe (terminus est)", 5)
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
        except Exception as e: print(f"✗ {slug}: {e}", file=sys.stderr)
