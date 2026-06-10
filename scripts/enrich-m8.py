#!/usr/bin/env python3
"""Enrichit M8 — 26 stations T0 (biographies sensibles neutralisées)."""
import json
from pathlib import Path
ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    "balard": {
        "addr": "Rue Balard, 75015 Paris", "arr": "15e arrondissement (Paris)",
        "seo": "Station Balard, terminus ouest M8 dans le 15e. Hexagone Balard (Ministère des Armées 2015). Tramway T3a en correspondance.",
        "tagline": "M8 — terminus ouest, Hexagone Balard",
        "hero_desc": "Station <strong>Balard</strong>, <strong>terminus ouest de la M8</strong>, sur la <strong>rue Balard</strong> dans le <strong>15e arrondissement</strong>. Ouverte le <strong>27 juillet 1937</strong>. À proximité de l'<strong>Hexagone Balard</strong>, siège du <strong>Ministère des Armées</strong> (2015). Correspondance <strong>tramway T3a</strong>.",
        "intros": [
            "La station <strong>Balard</strong> est le <strong>terminus ouest de la M8</strong>, sur la <strong>rue Balard</strong> dans le <strong>15e arrondissement</strong>. Elle est desservie par la <strong>M8</strong> et le <strong>tramway T3a</strong>. Bus 39, 42, 88, 169.",
            "Ouverte le <strong>27 juillet 1937</strong> avec le <strong>prolongement de la M8</strong> de Porte d'Auteuil (alors terminus) à Balard.",
            "À proximité : l'<strong>Hexagone Balard</strong>, siège du <strong>Ministère des Armées</strong> inauguré en <strong>2015</strong>. <strong>~9 500 militaires et civils</strong>. Quartier en transformation depuis les années 2010."
        ],
        "hist_title": "1937 : terminus ouest et Hexagone Balard",
        "hist": [
            "La station Balard est <strong>inaugurée le 27 juillet 1937</strong> comme <strong>terminus ouest de la M8</strong>.",
            "L'<strong>Hexagone Balard</strong>, à proximité, est inauguré le <strong>5 novembre 2015</strong>. <strong>Siège du Ministère des Armées</strong> regroupant <strong>~9 500 personnels</strong> militaires et civils auparavant dispersés. <strong>Conçu par Nicolas Michelin</strong>. <strong>340 000 m²</strong> sur <strong>8 hectares</strong>.",
            "Le quartier autour de la station est en <strong>profonde transformation</strong> depuis les années 2010 avec l'<strong>Hexagone Balard</strong> et l'<strong>aménagement Front-de-Seine</strong>. Le <strong>tramway T3a</strong>, en correspondance directe, est <strong>prolongé jusqu'à Porte d'Asnières</strong> en 2018."
        ],
        "faq": [
            ("Quelles lignes desservent Balard ?", "<strong>M8</strong> (terminus ouest) et <strong>tramway T3a</strong>. Bus 39, 42, 88, 169."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 juillet 1937</strong>."),
            ("Qu'est-ce que l'Hexagone Balard ?", "<strong>Siège du Ministère des Armées</strong> (2015), 340 000 m², ~9 500 personnels."),
            ("Pour le centre de Paris ?", "<strong>M8 directe</strong> vers Concorde (~16 min)."),
            ("Pour la Tour Eiffel ?", "<strong>M8 → École Militaire</strong> + à pied (~10 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Hexagone Balard</strong> à proximité : Ministère des Armées.",
            "<strong>Tramway T3a</strong> en correspondance directe.",
            "Pour <strong>Tour Eiffel</strong> : <strong>M8 → École Militaire</strong>.",
            "Pour <strong>Concorde</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Hexagone Balard (2015), Ministère des Armées", "L'<strong>Hexagone Balard</strong>, à proximité de la station, est <strong>inauguré le 5 novembre 2015</strong>. <strong>Siège du Ministère des Armées</strong> regroupant <strong>~9 500 militaires et civils</strong> auparavant dispersés sur <strong>15 sites</strong>. Conçu par l'architecte <strong>Nicolas Michelin</strong>. <strong>340 000 m²</strong> sur <strong>8 hectares</strong>. Surnommé <strong>« le Pentagone à la française »</strong>."),
            ("🚊", "Tramway T3a Maréchaux", "Le <strong>tramway T3a</strong>, en correspondance, circule sur les <strong>boulevards des Maréchaux</strong> au sud de Paris. <strong>Inauguré en 2006</strong> entre Pont du Garigliano et Porte d'Ivry. <strong>Prolongé jusqu'à Porte d'Asnières</strong> en 2018. <strong>~12 km</strong>, <strong>~150 000 voyageurs/jour</strong>.")
        ],
        "itin": [
            ("Hexagone Balard", "balard", "à pied", "Sortie + 5 min", 5),
            ("Tramway T3a", "balard", "T3a", "Correspondance directe", 1),
            ("Tour Eiffel via École Militaire", "ecole-militaire", "M8", "M8 directe (~10 min)", 10),
            ("Concorde", "concorde", "M8", "M8 directe (~16 min)", 16),
            ("Opéra Garnier", "opera", "M8", "M8 directe (~20 min)", 20),
            ("Bastille", "bastille", "M8", "M8 directe (~25 min)", 25)
        ]
    },
    "lourmel": {
        "addr": "Rue de Lourmel, 75015 Paris", "arr": "15e arrondissement (Paris)",
        "seo": "Station Lourmel (M8) rue de Lourmel dans le 15e. Quartier résidentiel et commerçant du 15e.",
        "tagline": "M8 — rue de Lourmel, 15e résidentiel",
        "hero_desc": "Station <strong>Lourmel</strong> sur la <strong>rue de Lourmel</strong> dans le <strong>15e arrondissement</strong>. Desservie par la <strong>M8</strong>, ouverte le <strong>27 juillet 1937</strong>. Quartier résidentiel et commerçant du <strong>15e</strong>.",
        "intros": [
            "La station <strong>Lourmel</strong> est implantée sur la <strong>rue de Lourmel</strong> dans le <strong>15e arrondissement</strong>. Elle est desservie par la <strong>M8</strong>, entre <strong>Balard</strong> (1 station, terminus) et <strong>Boucicaut</strong> (1 station). Bus 39, 42.",
            "Ouverte le <strong>27 juillet 1937</strong> avec le <strong>prolongement de la M8</strong> à Balard.",
            "La <strong>rue de Lourmel</strong>, qui donne son nom à la station, rend hommage à <strong>Frédéric de Lourmel</strong> (1811-1854), <strong>général français</strong> mort à la bataille de l'Alma pendant la guerre de Crimée. Quartier résidentiel et commerçant du <strong>15e</strong>."
        ],
        "hist_title": "1937 : prolongement Balard et rue Lourmel",
        "hist": [
            "La station Lourmel est <strong>inaugurée le 27 juillet 1937</strong> avec le <strong>prolongement de la M8</strong> à Balard.",
            "Le nom <strong>Lourmel</strong> rend hommage à <strong>Frédéric de Lourmel</strong> (<strong>1811-1854</strong>), <strong>général français</strong> mort lors de la <strong>bataille de l'Alma</strong> (20 septembre 1854) pendant la <strong>guerre de Crimée</strong>.",
            "Le quartier autour de la station fait partie du <strong>15e arrondissement</strong>, <strong>arrondissement le plus peuplé de Paris</strong> (~240 000 habitants). Quartier résidentiel et commerçant."
        ],
        "faq": [
            ("Quelle ligne dessert Lourmel ?", "Uniquement la <strong>M8</strong>. Bus 39, 42."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 juillet 1937</strong>."),
            ("Qui est Lourmel ?", "<strong>Frédéric de Lourmel</strong> (1811-1854), <strong>général français</strong> mort à la bataille de l'Alma."),
            ("Pour la Tour Eiffel ?", "<strong>M8 → École Militaire</strong>."),
            ("Pour Concorde ?", "<strong>M8 directe</strong> (~14 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier résidentiel du <strong>15e</strong>.",
            "Pour <strong>Balard</strong> et <strong>tramway T3a</strong> : <strong>M8 directe</strong>.",
            "Pour <strong>Tour Eiffel</strong> : <strong>M8 → École Militaire</strong>.",
            "Pour <strong>Concorde</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⚔️", "Bataille de l'Alma (1854)", "La <strong>bataille de l'Alma</strong>, <strong>20 septembre 1854</strong>, est l'une des <strong>premières batailles majeures</strong> de la <strong>guerre de Crimée</strong>. <strong>Victoire des alliés franco-britanniques-ottomans</strong> sur l'<strong>armée russe</strong>. La <strong>rivière Alma</strong> (Crimée) donne son nom à la victoire. À Paris, le <strong>pont de l'Alma</strong> (1856) et la <strong>place de l'Alma</strong> commémorent la victoire."),
            ("🏘️", "15e, arrondissement le plus peuplé", "Le <strong>15e arrondissement</strong> est le <strong>plus peuplé de Paris</strong> avec <strong>~240 000 habitants</strong>. Comprend les anciens villages de <strong>Grenelle</strong>, <strong>Vaugirard</strong> et <strong>Javel</strong>, rattachés à Paris en <strong>1860</strong>. Plusieurs <strong>institutions majeures</strong> : <strong>Institut Pasteur</strong>, <strong>UNESCO</strong>, <strong>Beaugrenelle</strong>, <strong>Tour Eiffel</strong> (limite avec 7e).")
        ],
        "itin": [
            ("Balard (terminus + T3a)", "balard", "M8", "M8 directe (1 station)", 2),
            ("Boucicaut", "boucicaut", "M8", "M8 directe (1 station)", 2),
            ("École Militaire (Tour Eiffel)", "ecole-militaire", "M8", "M8 directe (~8 min)", 8),
            ("Concorde", "concorde", "M8", "M8 directe (~14 min)", 14),
            ("Opéra Garnier", "opera", "M8", "M8 directe (~18 min)", 18),
            ("Bastille", "bastille", "M8", "M8 directe (~23 min)", 23)
        ]
    },
    "boucicaut": {
        "addr": "Rue de la Convention, 75015 Paris", "arr": "15e arrondissement (Paris)",
        "seo": "Station Boucicaut (M8) rue de la Convention dans le 15e. Hommage à Aristide Boucicaut (1810-1877), fondateur du Bon Marché.",
        "tagline": "M8 — Boucicaut, fondateur du Bon Marché",
        "hero_desc": "Station <strong>Boucicaut</strong> sur la <strong>rue de la Convention</strong> dans le <strong>15e arrondissement</strong>. Desservie par la <strong>M8</strong>, ouverte le <strong>27 juillet 1937</strong>. Hommage à <strong>Aristide Boucicaut</strong> (<strong>1810-1877</strong>), fondateur du <strong>Bon Marché</strong>, <strong>premier grand magasin parisien</strong>.",
        "intros": [
            "La station <strong>Boucicaut</strong> est implantée sur la <strong>rue de la Convention</strong> dans le <strong>15e arrondissement</strong>. Elle est desservie par la <strong>M8</strong>, entre <strong>Lourmel</strong> (1 station) et <strong>Félix Faure</strong> (1 station). Bus 42, 62, 70.",
            "Ouverte le <strong>27 juillet 1937</strong> avec le <strong>prolongement de la M8</strong> à Balard.",
            "Le nom <strong>Boucicaut</strong> rend hommage à <strong>Aristide Boucicaut</strong> (<strong>1810-1877</strong>), <strong>marchand français</strong>, <strong>fondateur du Bon Marché</strong>, <strong>premier grand magasin parisien</strong> (1852). À proximité : l'<strong>ancien hôpital Boucicaut</strong>."
        ],
        "hist_title": "1937 : Boucicaut et révolution commerciale",
        "hist": [
            "La station Boucicaut est <strong>inaugurée le 27 juillet 1937</strong> avec le <strong>prolongement de la M8</strong> à Balard.",
            "Le nom <strong>Boucicaut</strong> rend hommage à <strong>Aristide Boucicaut</strong> (<strong>14 juillet 1810 - 26 décembre 1877</strong>), <strong>marchand français</strong>. Avec son épouse <strong>Marguerite Boucicaut</strong>, il <strong>révolutionne le commerce de détail</strong> en transformant en <strong>1852</strong> une petite boutique en <strong>premier grand magasin parisien</strong> : <strong>Au Bon Marché</strong>.",
            "Le <strong>Bon Marché</strong> introduit de nombreuses <strong>innovations commerciales</strong> : <strong>prix fixes</strong> (sans marchandage), <strong>libre entrée</strong>, <strong>livraisons à domicile</strong>, <strong>soldes</strong>, <strong>catalogue de vente par correspondance</strong>, <strong>caisses de retraite et de prévoyance</strong> pour les employés. <strong>Émile Zola</strong> s'en inspira pour son roman <em>Au Bonheur des Dames</em> (1883). L'<strong>ancien hôpital Boucicaut</strong>, à proximité, a été reconverti en <strong>logements</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Boucicaut ?", "Uniquement la <strong>M8</strong>. Bus 42, 62, 70."),
            ("Qui est Aristide Boucicaut ?", "<strong>Aristide Boucicaut</strong> (1810-1877), <strong>marchand français</strong>, <strong>fondateur du Bon Marché</strong> (1852), <strong>premier grand magasin parisien</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 juillet 1937</strong>."),
            ("Quelles innovations apporta-t-il ?", "<strong>Prix fixes</strong>, <strong>libre entrée</strong>, <strong>livraisons à domicile</strong>, <strong>soldes</strong>, <strong>catalogue de vente par correspondance</strong>."),
            ("Pour Le Bon Marché ?", "<strong>M8 + M10</strong> via Sèvres-Babylone. Le grand magasin existe toujours."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Hommage à <strong>Aristide Boucicaut</strong>, fondateur du Bon Marché (1852).",
            "<strong>Ancien hôpital Boucicaut</strong> reconverti en logements.",
            "Pour <strong>Tour Eiffel</strong> : <strong>M8 → École Militaire</strong>.",
            "Pour <strong>Le Bon Marché</strong> : <strong>M8 + M10</strong> via Sèvres-Babylone.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🛍️", "Le Bon Marché, premier grand magasin (1852)", "<strong>Aristide Boucicaut</strong> (1810-1877) transforme en <strong>1852</strong> une petite boutique en <strong>premier grand magasin parisien</strong> : <strong>Au Bon Marché</strong>. Il <strong>révolutionne le commerce de détail</strong> avec : <strong>prix fixes</strong> (sans marchandage), <strong>libre entrée</strong>, <strong>livraisons à domicile</strong>, <strong>soldes</strong>, <strong>catalogue de vente par correspondance</strong>, <strong>caisses de retraite</strong>. Modèle suivi par Printemps (1865), Galeries Lafayette (1893), Samaritaine (1869)."),
            ("📚", "Zola, Au Bonheur des Dames (1883)", "Le roman <em><strong>Au Bonheur des Dames</strong></em> (1883) d'<strong>Émile Zola</strong> est <strong>inspiré du Bon Marché</strong> et de la <strong>révolution commerciale</strong> menée par <strong>Aristide Boucicaut</strong>. <strong>11e roman</strong> de la série des <em>Rougon-Macquart</em>. Zola y dépeint le <strong>basculement</strong> entre l'<strong>ancien commerce</strong> (petites boutiques) et le <strong>nouveau modèle</strong> des grands magasins.")
        ],
        "itin": [
            ("Lourmel", "lourmel", "M8", "M8 directe (1 station)", 2),
            ("Félix Faure", "felix-faure", "M8", "M8 directe (1 station)", 2),
            ("Le Bon Marché", "sevres-babylone", "M8 + M10", "M8 → La Motte-Picquet + M10", 12),
            ("École Militaire (Tour Eiffel)", "ecole-militaire", "M8", "M8 directe (~6 min)", 6),
            ("Concorde", "concorde", "M8", "M8 directe (~12 min)", 12),
            ("Opéra Garnier", "opera", "M8", "M8 directe (~16 min)", 16)
        ]
    },
    "felix-faure": {
        "addr": "Avenue Félix-Faure, 75015 Paris", "arr": "15e arrondissement (Paris)",
        "seo": "Station Félix Faure (M8) avenue Félix-Faure dans le 15e. Hommage à Félix Faure (1841-1899), Président de la République 1895-1899.",
        "tagline": "M8 — Félix Faure, Président République 1895-1899",
        "hero_desc": "Station <strong>Félix Faure</strong> sur l'<strong>avenue Félix-Faure</strong> dans le <strong>15e arrondissement</strong>. Desservie par la <strong>M8</strong>, ouverte le <strong>27 juillet 1937</strong>. Hommage à <strong>Félix Faure</strong> (<strong>1841-1899</strong>), <strong>Président de la République française</strong> de <strong>1895 à 1899</strong>.",
        "intros": [
            "La station <strong>Félix Faure</strong> est implantée sur l'<strong>avenue Félix-Faure</strong> dans le <strong>15e arrondissement</strong>. Elle est desservie par la <strong>M8</strong>, entre <strong>Boucicaut</strong> (1 station) et <strong>Commerce</strong> (1 station). Bus 70, 89.",
            "Ouverte le <strong>27 juillet 1937</strong> avec le <strong>prolongement de la M8</strong> à Balard.",
            "Le nom <strong>Félix Faure</strong> rend hommage à <strong>Félix Faure</strong> (<strong>30 janvier 1841 - 16 février 1899</strong>), <strong>homme politique français</strong>, <strong>Président de la République française</strong> du <strong>17 janvier 1895 au 16 février 1899</strong>. Son <strong>mandat</strong> est marqué par l'<strong>affaire Dreyfus</strong> et l'<strong>Exposition universelle de 1900</strong> en préparation."
        ],
        "hist_title": "1937 : avenue et 7e Président République",
        "hist": [
            "La station Félix Faure est <strong>inaugurée le 27 juillet 1937</strong> avec le <strong>prolongement de la M8</strong> à Balard.",
            "Le nom <strong>Félix Faure</strong> rend hommage à <strong>Félix Faure</strong> (<strong>30 janvier 1841 - 16 février 1899</strong>), <strong>homme politique français</strong>, <strong>7e Président de la République française</strong>. Né au Havre. <strong>Tanneur</strong> de profession, puis <strong>député républicain</strong> du Havre à partir de 1881.",
            "<strong>Ministre de la Marine</strong> (1894-1895). <strong>Élu Président</strong> le <strong>17 janvier 1895</strong> à la place de Casimir-Perier démissionnaire. Son mandat (1895-1899) est marqué par le <strong>renforcement de l'alliance franco-russe</strong>, le <strong>début de l'affaire Dreyfus</strong>, la <strong>préparation de l'Exposition universelle de 1900</strong>. <strong>Décédé en cours de mandat</strong> le 16 février 1899."
        ],
        "faq": [
            ("Quelle ligne dessert Félix Faure ?", "Uniquement la <strong>M8</strong>. Bus 70, 89."),
            ("Qui est Félix Faure ?", "<strong>Félix Faure</strong> (1841-1899), <strong>Président de la République française</strong> (1895-1899)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 juillet 1937</strong>."),
            ("Quel mandat ?", "<strong>17 janvier 1895 au 16 février 1899</strong>."),
            ("Pour la Tour Eiffel ?", "<strong>M8 → École Militaire</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Avenue Félix-Faure</strong> : axe résidentiel du 15e.",
            "Pour <strong>École Militaire</strong> et <strong>Tour Eiffel</strong> : <strong>M8 directe</strong>.",
            "Pour <strong>Concorde</strong> : <strong>M8 directe</strong>.",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Félix Faure, 7e Président République", "<strong>Félix Faure</strong> (1841-1899), <strong>7e Président de la République française</strong>. Né au Havre, <strong>tanneur</strong>, puis <strong>député républicain</strong>. <strong>Ministre de la Marine</strong> (1894-1895). <strong>Président de 1895 à 1899</strong>. Renforcement de l'<strong>alliance franco-russe</strong> (visite à Saint-Pétersbourg en 1897, accueil du tsar Nicolas II à Paris en 1896). <strong>Début de l'affaire Dreyfus</strong>. <strong>Préparation de l'Exposition universelle de 1900</strong>."),
            ("🇫🇷🇷🇺", "Alliance franco-russe", "Sous le mandat de <strong>Félix Faure</strong>, la <strong>France et la Russie</strong> consolident leur <strong>alliance</strong>. <strong>Visite du tsar Nicolas II</strong> à Paris en <strong>1896</strong> (accueil triomphal). <strong>Voyage de Félix Faure en Russie</strong> en <strong>1897</strong>. <strong>Pose de la première pierre du pont Alexandre III</strong> en 1896 (en présence du tsar). Cette alliance perdura jusqu'à la <strong>Révolution russe de 1917</strong>.")
        ],
        "itin": [
            ("École Militaire (Tour Eiffel)", "ecole-militaire", "M8", "M8 directe (~4 min)", 4),
            ("Commerce", "commerce", "M8", "M8 directe (1 station)", 2),
            ("Boucicaut", "boucicaut", "M8", "M8 directe (1 station)", 2),
            ("Concorde", "concorde", "M8", "M8 directe (~10 min)", 10),
            ("Opéra Garnier", "opera", "M8", "M8 directe (~14 min)", 14),
            ("Bastille", "bastille", "M8", "M8 directe (~20 min)", 20)
        ]
    },
    "commerce": {
        "addr": "Rue du Commerce, 75015 Paris", "arr": "15e arrondissement (Paris)",
        "seo": "Station Commerce (M8) rue du Commerce dans le 15e. Rue piétonne et commerçante du quartier Grenelle.",
        "tagline": "M8 — rue du Commerce, Grenelle",
        "hero_desc": "Station <strong>Commerce</strong> sur la <strong>rue du Commerce</strong> dans le <strong>15e arrondissement</strong>. Desservie par la <strong>M8</strong>, ouverte le <strong>27 juillet 1937</strong>. La <strong>rue du Commerce</strong> est l'une des <strong>rues commerçantes</strong> du <strong>quartier Grenelle</strong>.",
        "intros": [
            "La station <strong>Commerce</strong> est implantée sur la <strong>rue du Commerce</strong> dans le <strong>15e arrondissement</strong>. Elle est desservie par la <strong>M8</strong>, entre <strong>Félix Faure</strong> (1 station) et <strong>La Motte-Picquet - Grenelle</strong> (1 station). Bus 39, 70, 80.",
            "Ouverte le <strong>27 juillet 1937</strong> avec le <strong>prolongement de la M8</strong> à Balard.",
            "La <strong>rue du Commerce</strong>, qui donne son nom à la station, est l'une des <strong>rues commerçantes</strong> du <strong>quartier Grenelle</strong>. <strong>Atmosphère de village</strong> avec ses commerces de bouche, boutiques de prêt-à-porter, restaurants. <strong>Partiellement piétonne</strong>."
        ],
        "hist_title": "1937 : Grenelle, ancien village rattaché 1860",
        "hist": [
            "La station Commerce est <strong>inaugurée le 27 juillet 1937</strong> avec le <strong>prolongement de la M8</strong>.",
            "La <strong>rue du Commerce</strong>, qui donne son nom à la station, est l'une des <strong>rues commerçantes</strong> du <strong>quartier Grenelle</strong>. <strong>Atmosphère de village</strong> avec ses commerces de bouche, boutiques, restaurants. <strong>Partiellement piétonne</strong> depuis 2002.",
            "Le quartier <strong>Grenelle</strong> est l'un des <strong>anciens villages rattachés à Paris en 1860</strong>. Quartier <strong>résidentiel et commerçant</strong> du <strong>15e arrondissement</strong>. À proximité : la <strong>Tour Eiffel</strong>, la <strong>place du Commerce</strong>, le <strong>marché de Grenelle</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Commerce ?", "Uniquement la <strong>M8</strong>. Bus 39, 70, 80."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 juillet 1937</strong>."),
            ("Qu'est-ce que la rue du Commerce ?", "<strong>Rue commerçante</strong> du <strong>quartier Grenelle</strong>, partiellement piétonne depuis 2002."),
            ("Pour la Tour Eiffel ?", "<strong>M8 → École Militaire</strong> ou <strong>~15 min à pied</strong>."),
            ("Pour La Motte-Picquet - Grenelle (hub) ?", "<strong>M8 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Rue du Commerce</strong> partiellement piétonne : boutiques, restaurants, ambiance de village.",
            "<strong>Place du Commerce</strong> à proximité.",
            "Pour <strong>La Motte-Picquet - Grenelle</strong> (hub M6+M8+M10) : <strong>M8 directe</strong>.",
            "Pour <strong>Tour Eiffel</strong> : <strong>M8 → École Militaire</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🛍️", "Rue du Commerce, village urbain", "La <strong>rue du Commerce</strong>, qui donne son nom à la station, est l'une des <strong>rues commerçantes les plus animées du 15e</strong>. <strong>Partiellement piétonne</strong> depuis <strong>2002</strong>. <strong>Atmosphère de village urbain</strong> avec ses <strong>commerces de bouche</strong>, <strong>boutiques de prêt-à-porter</strong>, <strong>restaurants</strong>, <strong>cafés</strong>. <strong>Marché de Grenelle</strong> à proximité (mercredi et dimanche)."),
            ("🏘️", "Grenelle, ancien village rattaché", "Le quartier <strong>Grenelle</strong>, autour de la station, est l'un des <strong>anciens villages rattachés à Paris en 1860</strong>. <strong>Étymologie</strong> incertaine : peut-être <em>Garennelle</em> (« petite garenne »). Au XIXe siècle, <strong>quartier industriel</strong> avec ses <strong>usines</strong>. Aujourd'hui résidentiel et commerçant. <strong>Mairie du 15e</strong> à proximité (place Dupleix).")
        ],
        "itin": [
            ("La Motte-Picquet - Grenelle", "la-motte-picquet-grenelle", "M8", "M8 directe (1 station)", 2),
            ("École Militaire (Tour Eiffel)", "ecole-militaire", "M8", "M8 directe (~3 min)", 3),
            ("Tour Eiffel", "champ-de-mars-tour-eiffel", "M8 + RER C", "M8 → École Militaire + à pied", 10),
            ("Concorde", "concorde", "M8", "M8 directe (~8 min)", 8),
            ("Bastille", "bastille", "M8", "M8 directe (~18 min)", 18),
            ("Opéra", "opera", "M8", "M8 directe (~12 min)", 12)
        ]
    },
    "ecole-militaire": {
        "addr": "Place de l'École Militaire, 75007 Paris", "arr": "7e arrondissement (Paris)",
        "seo": "Station École Militaire (M8) place de l'École Militaire dans le 7e. École Militaire (1751, Louis XV, Gabriel). Champ-de-Mars et Tour Eiffel.",
        "tagline": "M8 — École Militaire (1751), Champ-de-Mars, Tour Eiffel",
        "hero_desc": "Station <strong>École Militaire</strong> sur la <strong>place de l'École Militaire</strong> dans le <strong>7e arrondissement</strong>. Desservie par la <strong>M8</strong>, ouverte le <strong>13 juillet 1913</strong>. À la sortie : l'<strong>École Militaire</strong> (<strong>1751</strong>, Louis XV, architecture <strong>Ange-Jacques Gabriel</strong>). <strong>Champ-de-Mars</strong> et <strong>Tour Eiffel</strong> à proximité.",
        "intros": [
            "La station <strong>École Militaire</strong> est implantée sur la <strong>place de l'École Militaire</strong> dans le <strong>7e arrondissement</strong>. Elle est desservie par la <strong>M8</strong>, entre <strong>La Motte-Picquet - Grenelle</strong> (1 station) et <strong>La Tour-Maubourg</strong> (1 station). Bus 28, 80, 87, 92.",
            "Ouverte le <strong>13 juillet 1913</strong> avec le tronçon initial de la <strong>M8</strong>.",
            "À la sortie : l'<strong>École Militaire</strong>, <strong>édifice du XVIIIe siècle</strong> construit de <strong>1751 à 1772</strong> sous <strong>Louis XV</strong> par l'<strong>architecte Ange-Jacques Gabriel</strong>. <strong>Champ-de-Mars</strong> et <strong>Tour Eiffel</strong> à courte distance. <strong>UNESCO</strong> à proximité."
        ],
        "hist_title": "1913 : École Militaire (1751) et Champ-de-Mars",
        "hist": [
            "La station École Militaire est <strong>inaugurée le 13 juillet 1913</strong> avec le tronçon initial de la <strong>M8</strong> (Beaugrenelle ↔ Opéra).",
            "L'<strong>École Militaire</strong>, à la sortie, est un <strong>édifice du XVIIIe siècle</strong> construit de <strong>1751 à 1772</strong> sous <strong>Louis XV</strong>. Conçue par l'<strong>architecte Ange-Jacques Gabriel</strong> (1698-1782), <strong>premier architecte du roi</strong>, également auteur du <strong>Petit Trianon</strong> et de la <strong>place de la Concorde</strong>. <strong>Façade néo-classique</strong> avec <strong>colonnade corinthienne</strong>.",
            "Initialement, <strong>établissement militaire d'élite</strong> destiné à former des <strong>officiers d'origine modeste</strong>. <strong>Napoléon Bonaparte</strong> y étudia comme <strong>cadet</strong> en <strong>1784</strong> (un an au lieu de deux, en raison de ses brillants résultats). Le <strong>Champ-de-Mars</strong>, à l'origine <strong>terrain d'exercices militaires</strong>, est aujourd'hui un <strong>parc public</strong> (24 hectares) au pied de la <strong>Tour Eiffel</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert École Militaire ?", "Uniquement la <strong>M8</strong>. Bus 28, 80, 87, 92."),
            ("Quand a-t-elle ouvert ?", "Le <strong>13 juillet 1913</strong>."),
            ("Qu'est-ce que l'École Militaire ?", "<strong>Édifice du XVIIIe</strong> construit de <strong>1751 à 1772</strong> sous Louis XV par <strong>Ange-Jacques Gabriel</strong>. <strong>Napoléon</strong> y étudia en 1784."),
            ("Pour la Tour Eiffel ?", "<strong>~10 min à pied</strong> via le Champ-de-Mars."),
            ("Pour l'UNESCO ?", "<strong>~5 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>École Militaire</strong> à la sortie : édifice de Gabriel (1751-1772).",
            "<strong>Tour Eiffel</strong> et <strong>Champ-de-Mars</strong> à 10 min à pied.",
            "<strong>UNESCO</strong> à 5 min à pied : siège mondial (1958).",
            "<strong>Hôtel des Invalides</strong> et <strong>tombeau de Napoléon</strong> à 15 min à pied.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎖️", "École Militaire (1751-1772), Gabriel et Louis XV", "L'<strong>École Militaire</strong>, à la sortie, est un <strong>édifice du XVIIIe siècle</strong> construit de <strong>1751 à 1772</strong> sous <strong>Louis XV</strong>. Conçue par l'<strong>architecte Ange-Jacques Gabriel</strong> (1698-1782), <strong>premier architecte du roi</strong>, également auteur du <strong>Petit Trianon</strong> et de la <strong>place de la Concorde</strong>. <strong>Façade néo-classique</strong> avec <strong>colonnade corinthienne</strong>. Initialement <strong>établissement militaire d'élite</strong>. <strong>Napoléon Bonaparte</strong> y étudia comme <strong>cadet</strong> en <strong>1784</strong>."),
            ("🗼", "Champ-de-Mars, du terrain militaire au parc", "Le <strong>Champ-de-Mars</strong>, à proximité, est à l'origine un <strong>terrain d'exercices militaires</strong> de l'École Militaire. Au cours du XIXe siècle, transformé en <strong>parc public</strong> de <strong>24 hectares</strong>. Lieu emblématique des <strong>Expositions universelles</strong> de <strong>1855, 1867, 1878, 1889</strong> (Tour Eiffel construite à cette occasion), <strong>1900</strong>. Aujourd'hui, <strong>l'un des parcs les plus visités de Paris</strong>, au pied de la <strong>Tour Eiffel</strong>.")
        ],
        "itin": [
            ("École Militaire", "ecole-militaire", "à pied", "Sortie directe", 1),
            ("Tour Eiffel", "champ-de-mars-tour-eiffel", "à pied", "Champ-de-Mars (10 min)", 10),
            ("UNESCO", "ecole-militaire", "à pied", "5 min à pied", 5),
            ("Invalides et Napoléon", "invalides", "M8", "M8 directe (2 stations)", 4),
            ("Concorde", "concorde", "M8", "M8 directe (~6 min)", 6),
            ("Opéra Garnier", "opera", "M8", "M8 directe (~10 min)", 10)
        ]
    },
    "la-tour-maubourg": {
        "addr": "Boulevard de La Tour-Maubourg, 75007 Paris", "arr": "7e arrondissement (Paris)",
        "seo": "Station La Tour-Maubourg (M8) boulevard de La Tour-Maubourg dans le 7e. Esplanade des Invalides à proximité.",
        "tagline": "M8 — La Tour-Maubourg, Esplanade des Invalides",
        "hero_desc": "Station <strong>La Tour-Maubourg</strong> sur le <strong>boulevard de La Tour-Maubourg</strong> dans le <strong>7e arrondissement</strong>. Desservie par la <strong>M8</strong>, ouverte le <strong>13 juillet 1913</strong>. À proximité de l'<strong>Esplanade des Invalides</strong> et du <strong>Pont Alexandre III</strong>.",
        "intros": [
            "La station <strong>La Tour-Maubourg</strong> est implantée sur le <strong>boulevard de La Tour-Maubourg</strong> dans le <strong>7e arrondissement</strong>. Elle est desservie par la <strong>M8</strong>, entre <strong>École Militaire</strong> (1 station) et <strong>Invalides</strong> (1 station). Bus 28, 49, 63, 69, 80, 87, 92.",
            "Ouverte le <strong>13 juillet 1913</strong> avec le tronçon initial de la <strong>M8</strong>.",
            "Le nom <strong>La Tour-Maubourg</strong> rend hommage à <strong>Marie Charles César de Faÿ, comte de Latour-Maubourg</strong> (<strong>1756-1831</strong>), <strong>général français</strong>. À courte distance : l'<strong>Esplanade des Invalides</strong> et l'<strong>Hôtel des Invalides</strong>."
        ],
        "hist_title": "1913 : La Tour-Maubourg et Invalides",
        "hist": [
            "La station La Tour-Maubourg est <strong>inaugurée le 13 juillet 1913</strong> avec le tronçon initial de la <strong>M8</strong>.",
            "Le nom <strong>La Tour-Maubourg</strong> rend hommage à <strong>Marie Charles César de Faÿ, comte de Latour-Maubourg</strong> (<strong>22 mai 1756 - 28 mai 1831</strong>), <strong>général français</strong>. <strong>Pair de France</strong> sous la Restauration. <strong>Ministre de la Guerre</strong> (1819-1821).",
            "À proximité : l'<strong>Esplanade des Invalides</strong>, vaste espace ouvert devant l'<strong>Hôtel des Invalides</strong>. L'<strong>Hôtel national des Invalides</strong>, fondé par <strong>Louis XIV</strong> en <strong>1670</strong>, accueille le <strong>tombeau de Napoléon</strong> sous le <strong>dôme</strong> de <strong>Jules Hardouin-Mansart</strong>. Le <strong>Pont Alexandre III</strong> (1900) est également à courte distance."
        ],
        "faq": [
            ("Quelle ligne dessert La Tour-Maubourg ?", "Uniquement la <strong>M8</strong>. Bus 28, 49, 63, 69, 80, 87, 92."),
            ("Qui est La Tour-Maubourg ?", "<strong>Marie Charles César de Faÿ, comte de Latour-Maubourg</strong> (1756-1831), <strong>général français</strong>. <strong>Ministre de la Guerre</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>13 juillet 1913</strong>."),
            ("Pour l'Hôtel des Invalides ?", "<strong>~5 min à pied</strong> via l'Esplanade."),
            ("Pour le Pont Alexandre III ?", "<strong>~10 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Esplanade des Invalides</strong> à 5 min à pied.",
            "<strong>Hôtel des Invalides</strong> et <strong>tombeau de Napoléon</strong> à 7 min.",
            "<strong>Pont Alexandre III</strong> (1900) à 10 min.",
            "Pour <strong>Tour Eiffel</strong> : <strong>M8 → École Militaire</strong> ou à pied.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Hôtel des Invalides (1670), Louis XIV", "L'<strong>Hôtel national des Invalides</strong>, à courte distance, est fondé par <strong>Louis XIV</strong> en <strong>1670</strong> pour <strong>accueillir les soldats blessés et invalides</strong>. <strong>Architecte Libéral Bruant</strong>. <strong>Dôme</strong> ajouté par <strong>Jules Hardouin-Mansart</strong> (1679-1706). <strong>Tombeau de Napoléon Ier</strong> sous le dôme depuis <strong>1840</strong> (<strong>Retour des cendres</strong>). <strong>Musée de l'Armée</strong>, <strong>musée des Plans-Reliefs</strong>, <strong>cathédrale Saint-Louis</strong>."),
            ("🌉", "Pont Alexandre III (1900)", "Le <strong>pont Alexandre III</strong>, à 10 min à pied, est l'un des <strong>plus emblématiques ponts parisiens</strong>. Construit pour l'<strong>Exposition universelle de 1900</strong>. <strong>Inauguré en 1900</strong> en présence du <strong>tsar Nicolas II</strong>. <strong>Style Belle Époque</strong> avec <strong>candélabres dorés</strong>, <strong>statues allégoriques</strong>, <strong>arc unique de 107 m</strong>. <strong>Classé monument historique</strong>. Symbole de l'<strong>alliance franco-russe</strong> sous le règne de Félix Faure.")
        ],
        "itin": [
            ("Hôtel des Invalides", "invalides", "M8", "M8 directe (1 station)", 2),
            ("Tombeau de Napoléon", "invalides", "M8", "M8 directe + à pied", 5),
            ("Pont Alexandre III", "invalides", "à pied", "Esplanade + 10 min", 10),
            ("Tour Eiffel", "champ-de-mars-tour-eiffel", "M8 + RER C", "M8 → École Militaire + à pied", 14),
            ("Concorde", "concorde", "M8", "M8 directe (~4 min)", 4),
            ("Opéra Garnier", "opera", "M8", "M8 directe (~8 min)", 8)
        ]
    },
    "richelieu-drouot": {
        "addr": "Boulevard Haussmann, 75009 Paris", "arr": "9e arrondissement (Paris)",
        "seo": "Station Richelieu - Drouot (M8+M9) boulevard Haussmann dans le 9e. Hôtel Drouot, ventes aux enchères depuis 1852. Cardinal de Richelieu.",
        "tagline": "M8 + M9 — Hôtel Drouot, ventes aux enchères",
        "hero_desc": "Station <strong>Richelieu - Drouot</strong>, hub <strong>M8 + M9</strong>, sur le <strong>boulevard Haussmann</strong> dans le <strong>9e arrondissement</strong>. Quais <strong>M8</strong> ouverts en <strong>1913</strong>, quais <strong>M9</strong> en <strong>1933</strong>. À proximité de l'<strong>Hôtel Drouot</strong> (1852), célèbre <strong>maison de ventes aux enchères</strong>.",
        "intros": [
            "La station <strong>Richelieu - Drouot</strong> est implantée sur le <strong>boulevard Haussmann</strong> dans le <strong>9e arrondissement</strong>. Elle est desservie par les <strong>lignes 8 et 9</strong>, formant un <strong>hub de correspondance</strong>. Bus 20, 32, 39, 67, 74, 85.",
            "Quais <strong>M8</strong> ouverts le <strong>13 juillet 1913</strong> avec le tronçon initial. Quais <strong>M9</strong> ouverts le <strong>10 décembre 1933</strong> avec le prolongement de la M9.",
            "Les noms <strong>Richelieu</strong> et <strong>Drouot</strong> rendent hommage : <strong>Richelieu</strong> au <strong>Cardinal de Richelieu</strong> (<strong>1585-1642</strong>), <strong>ministre de Louis XIII</strong> ; <strong>Drouot</strong> à <strong>Antoine Drouot</strong> (<strong>1774-1847</strong>), <strong>général d'Empire</strong>. L'<strong>Hôtel Drouot</strong>, célèbre <strong>maison de ventes aux enchères</strong>, est à proximité."
        ],
        "hist_title": "1913-1933 : hub M8/M9 et Hôtel Drouot",
        "hist": [
            "Les quais <strong>M8</strong> sont <strong>inaugurés le 13 juillet 1913</strong>. Les quais <strong>M9</strong> ouvrent le <strong>10 décembre 1933</strong>.",
            "Le nom <strong>Richelieu</strong> rend hommage à <strong>Armand Jean du Plessis, cardinal de Richelieu</strong> (<strong>1585-1642</strong>), <strong>ministre de Louis XIII</strong> de <strong>1624 à 1642</strong>. <strong>Renforce l'absolutisme royal</strong>. <strong>Fondateur de l'Académie française</strong> (1635). Inspiration du personnage de Richelieu dans <em>Les Trois Mousquetaires</em> d'Alexandre Dumas.",
            "L'<strong>Hôtel Drouot</strong>, à proximité (9 rue Drouot), est <strong>fondé en 1852</strong> comme <strong>hôtel des ventes mobilières</strong>. <strong>Principale maison de ventes aux enchères</strong> de France. <strong>~500 000 objets vendus par an</strong>. <strong>Reconstruit en 1976</strong> dans son architecture actuelle. <strong>Antiquités, mobilier, peintures, sculptures, livres anciens, bijoux</strong>."
        ],
        "faq": [
            ("Quelles lignes desservent Richelieu - Drouot ?", "<strong>M8</strong> et <strong>M9</strong>. Hub du 9e."),
            ("Qui est Richelieu ?", "<strong>Cardinal de Richelieu</strong> (1585-1642), <strong>ministre de Louis XIII</strong>. <strong>Fondateur de l'Académie française</strong>."),
            ("Qu'est-ce que l'Hôtel Drouot ?", "<strong>Principale maison de ventes aux enchères</strong> de France, <strong>fondée en 1852</strong>. ~500 000 objets vendus/an."),
            ("Quand a-t-elle ouvert ?", "Quais M8 : <strong>13 juillet 1913</strong>. Quais M9 : <strong>10 décembre 1933</strong>."),
            ("Pour l'Hôtel Drouot ?", "<strong>~3 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Hôtel Drouot</strong> à 3 min : ventes aux enchères ouvertes au public.",
            "Hub <strong>M8 + M9</strong> du 9e.",
            "Pour <strong>Galeries Lafayette</strong> : <strong>M9 directe</strong> (1 station).",
            "Pour <strong>Opéra Garnier</strong> : <strong>M8 directe</strong> (1 station).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Cardinal de Richelieu, ministre de Louis XIII", "<strong>Armand Jean du Plessis, cardinal de Richelieu</strong> (<strong>1585-1642</strong>), <strong>ministre de Louis XIII</strong> de <strong>1624 à 1642</strong>. <strong>Renforce l'absolutisme royal</strong> contre les grands seigneurs et les protestants (<strong>siège de La Rochelle</strong> 1627-1628). <strong>Fondateur de l'Académie française</strong> en <strong>1635</strong>. Politique étrangère : entrée dans la <strong>guerre de Trente Ans</strong> aux côtés des protestants. <strong>Modèle de l'État centralisé</strong> à la française. Inspiration du <strong>personnage de Richelieu</strong> dans <em>Les Trois Mousquetaires</em> d'<strong>Alexandre Dumas</strong>."),
            ("🔨", "Hôtel Drouot, ventes aux enchères depuis 1852", "L'<strong>Hôtel Drouot</strong>, à 3 min à pied (9 rue Drouot), est <strong>fondé le 1er juin 1852</strong> comme <strong>hôtel des ventes mobilières</strong>. <strong>Principale maison de ventes aux enchères de France</strong>. <strong>~500 000 objets vendus par an</strong>, <strong>~150 000 lots</strong>. <strong>Reconstruit en 1976</strong> dans son architecture moderne. <strong>Ventes publiques</strong> ouvertes à tous (sans réservation), <strong>~3 000 lots/semaine</strong>. <strong>Antiquités, mobilier, peintures, sculptures, livres anciens, bijoux, instruments</strong>.")
        ],
        "itin": [
            ("Hôtel Drouot", "richelieu-drouot", "à pied", "Rue Drouot (3 min)", 3),
            ("Galeries Lafayette", "chaussee-d-antin-la-fayette", "M9", "M9 directe (1 station)", 2),
            ("Opéra Garnier", "opera", "M8", "M8 directe (1 station)", 2),
            ("Grands Boulevards", "grands-boulevards", "M8", "M8 directe (1 station)", 2),
            ("Bastille", "bastille", "M8", "M8 directe (~14 min)", 14),
            ("Concorde", "concorde", "M8", "M8 directe (~6 min)", 6)
        ]
    },
    "grands-boulevards": {
        "addr": "Boulevard Poissonnière, 75009 Paris", "arr": "9e arrondissement (Paris)",
        "seo": "Station Grands Boulevards (M8+M9) boulevard Poissonnière dans le 9e. Musée Grévin, Théâtre des Variétés, passages couverts.",
        "tagline": "M8 + M9 — Grands Boulevards, Musée Grévin",
        "hero_desc": "Station <strong>Grands Boulevards</strong>, hub <strong>M8 + M9</strong>, sur le <strong>boulevard Poissonnière</strong> dans le <strong>9e arrondissement</strong>. À proximité du <strong>Musée Grévin</strong>, du <strong>Théâtre des Variétés</strong> et des <strong>passages couverts</strong> historiques.",
        "intros": [
            "La station <strong>Grands Boulevards</strong> est implantée sur le <strong>boulevard Poissonnière</strong> dans le <strong>9e arrondissement</strong>. Elle est desservie par les <strong>lignes 8 et 9</strong>, formant un <strong>hub de correspondance</strong>. Bus 20, 39, 48, 67, 74, 85.",
            "Quais <strong>M8</strong> ouverts le <strong>13 juillet 1913</strong>. Quais <strong>M9</strong> ouverts le <strong>10 décembre 1933</strong>. Renommée <strong>« Grands Boulevards »</strong> en <strong>1998</strong> (anciennement « Rue Montmartre »).",
            "À proximité : le <strong>Musée Grévin</strong> (1882), <strong>musée de cire</strong>, le <strong>Théâtre des Variétés</strong> (1807), les <strong>passages Jouffroy et Verdeau</strong>. Cœur des <strong>Grands Boulevards</strong> de Paris."
        ],
        "hist_title": "1913 : Grands Boulevards de Louis XIV",
        "hist": [
            "Les quais <strong>M8</strong> sont <strong>inaugurés le 13 juillet 1913</strong>. Les quais <strong>M9</strong> ouvrent le <strong>10 décembre 1933</strong>. <strong>Renommée « Grands Boulevards »</strong> en <strong>1998</strong> (auparavant « Rue Montmartre »).",
            "Les <strong>Grands Boulevards</strong>, qui donnent leur nom à la station, sont une <strong>série d'axes haussmanniens</strong> tracés à partir de <strong>1670</strong> sous <strong>Louis XIV</strong> sur l'emplacement de l'<strong>ancienne enceinte de Charles V</strong> (XIVe siècle). Étendus et embellis sous <strong>Haussmann</strong> au XIXe siècle.",
            "Hauts lieux de la <strong>vie parisienne</strong> depuis le <strong>XVIIIe siècle</strong>, ils sont marqués par les <strong>théâtres</strong> (Théâtre des Variétés 1807, Théâtre de la Renaissance, Théâtre du Gymnase), les <strong>cafés</strong> (Café Frascati, Café Cardinal), les <strong>passages couverts</strong> (Jouffroy 1846, Verdeau 1847, Panoramas 1799). Le <strong>Musée Grévin</strong>, à proximité (10 boulevard Montmartre), est <strong>fondé en 1882</strong>."
        ],
        "faq": [
            ("Quelles lignes desservent Grands Boulevards ?", "<strong>M8</strong> et <strong>M9</strong>. Hub du 9e."),
            ("Quel était l'ancien nom ?", "<strong>« Rue Montmartre »</strong> (1913-1998)."),
            ("Pour le Musée Grévin ?", "<strong>~2 min à pied</strong> (10 boulevard Montmartre)."),
            ("Pour le Théâtre des Variétés ?", "<strong>~3 min à pied</strong>."),
            ("Pour les passages couverts ?", "<strong>Passage Jouffroy</strong> et <strong>Verdeau</strong> à proximité immédiate."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Musée Grévin</strong> à 2 min : musée de cire fondé en 1882.",
            "<strong>Passages Jouffroy et Verdeau</strong> à proximité : passages couverts XIXe.",
            "<strong>Théâtre des Variétés</strong> (1807) à 3 min.",
            "Pour <strong>Opéra Garnier</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🕯️", "Musée Grévin (1882), musée de cire", "Le <strong>Musée Grévin</strong>, à 2 min à pied (10 boulevard Montmartre), est <strong>fondé en 1882</strong> par <strong>Arthur Meyer</strong> (journaliste) et <strong>Alfred Grévin</strong> (caricaturiste). <strong>Musée de cire</strong> à l'image du Madame Tussauds londonien. <strong>~250 personnages</strong> historiques et contemporains : <strong>Napoléon, Louis XIV, Picasso, De Gaulle, Brigitte Bardot, Elvis Presley</strong>. <strong>Décors historiques</strong> (Versailles, Hollywood). <strong>~700 000 visiteurs/an</strong>."),
            ("🎭", "Passages Jouffroy et Verdeau", "Les <strong>passages Jouffroy</strong> (1846) et <strong>Verdeau</strong> (1847), à proximité immédiate, sont parmi les <strong>plus beaux passages couverts</strong> de Paris. <strong>Verrières</strong>, <strong>mosaïques au sol</strong>, <strong>devantures boutiques XIXe</strong>. <strong>Premier passage chauffé</strong> à Paris (Jouffroy). <strong>Librairies anciennes, antiquaires, salons de thé, boutiques curieuses</strong>. <strong>Patrimoine emblématique</strong> du <strong>Paris du XIXe siècle</strong>.")
        ],
        "itin": [
            ("Musée Grévin", "grands-boulevards", "à pied", "Boulevard Montmartre (2 min)", 2),
            ("Passage Jouffroy", "grands-boulevards", "à pied", "Sortie directe", 2),
            ("Théâtre des Variétés", "grands-boulevards", "à pied", "Boulevard Montmartre (3 min)", 3),
            ("Opéra Garnier", "opera", "M8", "M8 directe (2 stations)", 4),
            ("Bastille", "bastille", "M8", "M8 directe (~12 min)", 12),
            ("Galeries Lafayette", "chaussee-d-antin-la-fayette", "M9", "M9 directe (2 stations)", 4)
        ]
    },
    "saint-sebastien-froissart": {
        "addr": "Boulevard Beaumarchais, 75003 Paris", "arr": "3e arrondissement (Paris)",
        "seo": "Station Saint-Sébastien - Froissart (M8) boulevard Beaumarchais dans le 3e. Musée Picasso (Hôtel Salé) à proximité. Marais nord.",
        "tagline": "M8 — Musée Picasso et Marais nord",
        "hero_desc": "Station <strong>Saint-Sébastien - Froissart</strong> sur le <strong>boulevard Beaumarchais</strong> dans le <strong>3e arrondissement</strong>. Desservie par la <strong>M8</strong>, ouverte le <strong>5 mai 1931</strong>. À proximité du <strong>Musée Picasso</strong> (Hôtel Salé) et du <strong>quartier du Marais nord</strong>.",
        "intros": [
            "La station <strong>Saint-Sébastien - Froissart</strong> est implantée sur le <strong>boulevard Beaumarchais</strong> dans le <strong>3e arrondissement</strong>. Elle est desservie par la <strong>M8</strong>, entre <strong>Filles du Calvaire</strong> (1 station) et <strong>Chemin Vert</strong> (1 station). Bus 96.",
            "Ouverte le <strong>5 mai 1931</strong> avec le <strong>prolongement de la M8</strong> de Richelieu-Drouot vers Porte de Charenton.",
            "Le nom <strong>Saint-Sébastien</strong> rappelle l'<strong>impasse Saint-Sébastien</strong>. <strong>Froissart</strong> rend hommage à <strong>Jean Froissart</strong> (<strong>1337-1410</strong>), <strong>chroniqueur français</strong> du Moyen Âge. À proximité : le <strong>Musée Picasso</strong> (Hôtel Salé, XVIIe), le <strong>Marché des Enfants Rouges</strong>."
        ],
        "hist_title": "1931 : Marais nord et Musée Picasso",
        "hist": [
            "La station Saint-Sébastien - Froissart est <strong>inaugurée le 5 mai 1931</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Froissart</strong> rend hommage à <strong>Jean Froissart</strong> (<strong>vers 1337 - vers 1410</strong>), <strong>chroniqueur et poète français du Moyen Âge</strong>. Auteur des <strong>Chroniques de Froissart</strong>, <strong>œuvre majeure</strong> sur la <strong>guerre de Cent Ans</strong> et la <strong>chevalerie</strong>.",
            "À proximité : le <strong>Musée Picasso</strong> (5 rue de Thorigny), installé dans l'<strong>Hôtel Salé</strong>, <strong>hôtel particulier XVIIe</strong> construit par <strong>Pierre Aubert de Fontenay</strong> en <strong>1656-1659</strong>. <strong>Musée ouvert en 1985</strong> après <strong>donation de la famille Picasso</strong>. <strong>~5 000 œuvres</strong> de <strong>Pablo Picasso</strong> (peintures, sculptures, dessins, gravures, céramiques). Le <strong>Marché des Enfants Rouges</strong>, <strong>plus ancien marché couvert de Paris</strong> (1615), est à proximité."
        ],
        "faq": [
            ("Quelle ligne dessert Saint-Sébastien - Froissart ?", "Uniquement la <strong>M8</strong>. Bus 96."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 mai 1931</strong>."),
            ("Pour le Musée Picasso ?", "<strong>~5 min à pied</strong> (Hôtel Salé, rue de Thorigny)."),
            ("Pour le Marché des Enfants Rouges ?", "<strong>~7 min à pied</strong>. Plus ancien marché couvert de Paris (1615)."),
            ("Pour la place des Vosges ?", "<strong>~10 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Musée Picasso</strong> à 5 min à pied : Hôtel Salé XVIIe, ~5 000 œuvres.",
            "<strong>Marché des Enfants Rouges</strong> à 7 min : plus ancien marché couvert de Paris (1615).",
            "<strong>Place des Vosges</strong> à 10 min à pied : plus ancienne place royale de Paris.",
            "<strong>Quartier du Marais</strong> à proximité : hôtels particuliers XVIIe.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎨", "Musée Picasso (1985), Hôtel Salé", "Le <strong>Musée Picasso</strong>, à 5 min à pied (5 rue de Thorigny), est installé dans l'<strong>Hôtel Salé</strong>, <strong>hôtel particulier XVIIe</strong> construit par <strong>Pierre Aubert de Fontenay</strong>, <strong>fermier de la gabelle</strong> (impôt sur le sel), d'où le surnom <strong>« Salé »</strong>. <strong>Architecte Jean Boullier</strong>. Musée <strong>ouvert en 1985</strong> après <strong>donation de la famille Picasso</strong> en règlement de droits de succession. <strong>~5 000 œuvres</strong> de <strong>Pablo Picasso</strong> : peintures, sculptures, dessins, gravures, céramiques."),
            ("🛍️", "Marché des Enfants Rouges (1615)", "Le <strong>Marché des Enfants Rouges</strong>, à 7 min à pied, est le <strong>plus ancien marché couvert de Paris</strong>. <strong>Créé en 1615</strong> sous <strong>Louis XIII</strong>. Nom hérité de l'<strong>orphelinat voisin</strong> (créé en 1534) dont les enfants portaient des <strong>vêtements rouges</strong>. <strong>Restauré en 2000</strong>. Aujourd'hui : <strong>cuisines du monde</strong> (italienne, libanaise, japonaise, marocaine, antillaise), <strong>maraîchers</strong>, <strong>fleuristes</strong>.")
        ],
        "itin": [
            ("Musée Picasso", "saint-sebastien-froissart", "à pied", "Rue de Thorigny (5 min)", 5),
            ("Marché des Enfants Rouges", "filles-du-calvaire", "à pied", "Rue de Bretagne (7 min)", 7),
            ("Place des Vosges", "saint-paul", "à pied", "10 min à pied", 10),
            ("République", "republique", "M8 + M3", "M8 → Filles du Calvaire + à pied", 8),
            ("Bastille", "bastille", "M8", "M8 directe (2 stations)", 4),
            ("Châtelet", "chatelet", "M8 + M1", "M8 → Bastille + M1", 10)
        ]
    },
    "chemin-vert": {
        "addr": "Boulevard Beaumarchais, 75011 Paris", "arr": "11e arrondissement (Paris)",
        "seo": "Station Chemin Vert (M8) boulevard Beaumarchais dans le 11e. Quartier Bastille/Marais.",
        "tagline": "M8 — Chemin-Vert, 11e Bastille",
        "hero_desc": "Station <strong>Chemin Vert</strong> sur le <strong>boulevard Beaumarchais</strong> dans le <strong>11e arrondissement</strong>. Desservie par la <strong>M8</strong>, ouverte le <strong>5 mai 1931</strong>. Quartier <strong>Bastille / Marais</strong>.",
        "intros": [
            "La station <strong>Chemin Vert</strong> est implantée sur le <strong>boulevard Beaumarchais</strong> dans le <strong>11e arrondissement</strong>. Elle est desservie par la <strong>M8</strong>, entre <strong>Saint-Sébastien - Froissart</strong> (1 station) et <strong>Bastille</strong> (1 station). Bus 20, 65, 96.",
            "Ouverte le <strong>5 mai 1931</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Chemin Vert</strong> rappelle la <strong>rue du Chemin-Vert</strong> à proximité. Étymologie évoquant un <strong>ancien chemin de verdure</strong> traversant l'<strong>ancien territoire rural</strong> du XIIIe siècle, avant l'urbanisation du quartier."
        ],
        "hist_title": "1931 : Chemin-Vert et Bastille",
        "hist": [
            "La station Chemin Vert est <strong>inaugurée le 5 mai 1931</strong> avec le <strong>prolongement de la M8</strong> de Richelieu-Drouot vers Porte de Charenton.",
            "La <strong>rue du Chemin-Vert</strong>, qui donne son nom à la station, est tracée au <strong>XVIIIe siècle</strong>. Son nom évoque un <strong>ancien chemin de verdure</strong> traversant le <strong>territoire rural</strong> du nord-est parisien, avant l'urbanisation du quartier.",
            "Le quartier autour de la station fait partie du <strong>11e arrondissement</strong>, à proximité de <strong>Bastille</strong> et du <strong>Marais</strong>. <strong>Boulevard Beaumarchais</strong> tracé sous Haussmann. À courte distance : la <strong>Cirque d'Hiver Bouglione</strong> (1852) à Filles du Calvaire."
        ],
        "faq": [
            ("Quelle ligne dessert Chemin Vert ?", "Uniquement la <strong>M8</strong>. Bus 20, 65, 96."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 mai 1931</strong>."),
            ("D'où vient le nom Chemin-Vert ?", "D'un <strong>ancien chemin de verdure</strong> du XVIIIe siècle traversant le territoire rural du quartier."),
            ("Pour Bastille ?", "<strong>M8 directe</strong> (1 station)."),
            ("Pour le Marais ?", "<strong>~5 min à pied</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong> (1 station).",
            "<strong>Quartier du Marais</strong> à 5 min à pied.",
            "<strong>Cirque d'Hiver Bouglione</strong> (1852) à 5 min à pied.",
            "Pour <strong>République</strong> : <strong>~8 min à pied</strong> ou bus.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🎪", "Cirque d'Hiver Bouglione (1852)", "Le <strong>Cirque d'Hiver Bouglione</strong>, à 5 min à pied, est le <strong>plus ancien cirque permanent du monde</strong> encore en activité. <strong>Construit en 1852</strong> par l'architecte <strong>Jacques-Ignace Hittorff</strong>. <strong>Inauguré par Napoléon III</strong> sous le nom <strong>« Cirque Napoléon »</strong>. <strong>Bâtiment en forme de polygone à 20 côtés</strong>. <strong>Famille Bouglione</strong> propriétaire depuis <strong>1934</strong>. <strong>Classé monument historique en 1975</strong>. <strong>~30 spectacles/an</strong>."),
            ("🏘️", "11e, du faubourg ouvrier au quartier tendance", "Le <strong>11e arrondissement</strong> (~150 000 habitants) est historiquement un <strong>quartier populaire et ouvrier</strong>. <strong>Faubourg Saint-Antoine</strong>, ancien quartier des <strong>artisans du meuble</strong>. À partir des années 1990, <strong>gentrification</strong> avec installation de <strong>bars, restaurants tendance</strong> autour des rues <strong>Oberkampf, Jean-Pierre Timbaud, Saint-Maur</strong>.")
        ],
        "itin": [
            ("Bastille", "bastille", "M8", "M8 directe (1 station)", 2),
            ("Marais (Place des Vosges)", "saint-paul", "M8 + M1", "M8 → Bastille + M1", 6),
            ("Cirque d'Hiver Bouglione", "filles-du-calvaire", "à pied", "5 min à pied", 5),
            ("République", "republique", "à pied + bus", "8 min à pied", 8),
            ("Châtelet", "chatelet", "M8 + M1", "M8 → Bastille + M1", 8),
            ("Concorde", "concorde", "M8", "M8 directe (~10 min)", 10)
        ]
    },
    "ledru-rollin": {
        "addr": "Rue du Faubourg-Saint-Antoine, 75012 Paris", "arr": "12e arrondissement (Paris)",
        "seo": "Station Ledru-Rollin (M8) rue du Faubourg-Saint-Antoine dans le 12e. Marché d'Aligre à proximité. Hommage à Alexandre Ledru-Rollin.",
        "tagline": "M8 — Ledru-Rollin, Marché d'Aligre",
        "hero_desc": "Station <strong>Ledru-Rollin</strong> sur la <strong>rue du Faubourg-Saint-Antoine</strong> dans le <strong>12e arrondissement</strong>. Desservie par la <strong>M8</strong>, ouverte le <strong>5 mai 1931</strong>. Hommage à <strong>Alexandre Ledru-Rollin</strong> (<strong>1807-1874</strong>), <strong>homme politique français</strong>. <strong>Marché d'Aligre</strong> à proximité.",
        "intros": [
            "La station <strong>Ledru-Rollin</strong> est implantée sur la <strong>rue du Faubourg-Saint-Antoine</strong> dans le <strong>12e arrondissement</strong>. Elle est desservie par la <strong>M8</strong>, entre <strong>Bastille</strong> (1 station) et <strong>Faidherbe - Chaligny</strong> (1 station). Bus 20, 76, 86, 91.",
            "Ouverte le <strong>5 mai 1931</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Ledru-Rollin</strong> rend hommage à <strong>Alexandre Auguste Ledru, dit Ledru-Rollin</strong> (<strong>1807-1874</strong>), <strong>avocat et homme politique français</strong>. <strong>Député républicain</strong>. À proximité : le <strong>Marché d'Aligre</strong>, l'un des <strong>plus animés de Paris</strong>."
        ],
        "hist_title": "1931 : Ledru-Rollin et Faubourg Saint-Antoine",
        "hist": [
            "La station Ledru-Rollin est <strong>inaugurée le 5 mai 1931</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Ledru-Rollin</strong> rend hommage à <strong>Alexandre Auguste Ledru, dit Ledru-Rollin</strong> (<strong>2 février 1807 - 31 décembre 1874</strong>), <strong>avocat et homme politique français</strong>. <strong>Député républicain</strong>.",
            "Le quartier autour de la station, le <strong>Faubourg Saint-Antoine</strong>, est historiquement <strong>quartier des artisans du meuble</strong> depuis le XIIIe siècle. Privilèges accordés par <strong>Louis XI</strong> en 1471. <strong>Centre d'effervescence</strong> pendant la <strong>Révolution française</strong> (prise de la Bastille). Le <strong>Marché d'Aligre</strong>, à proximité, comprend un <strong>marché alimentaire</strong> et un <strong>marché aux puces</strong> (tous les jours sauf lundi)."
        ],
        "faq": [
            ("Quelle ligne dessert Ledru-Rollin ?", "Uniquement la <strong>M8</strong>. Bus 20, 76, 86, 91."),
            ("Qui est Ledru-Rollin ?", "<strong>Alexandre Ledru-Rollin</strong> (1807-1874), <strong>avocat et homme politique républicain</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 mai 1931</strong>."),
            ("Pour le Marché d'Aligre ?", "<strong>~5 min à pied</strong>. Marché alimentaire + marché aux puces."),
            ("Pour Bastille ?", "<strong>M8 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Marché d'Aligre</strong> à 5 min : un des plus animés de Paris.",
            "<strong>Faubourg Saint-Antoine</strong> : ancien quartier des artisans du meuble.",
            "Pour <strong>Bastille</strong> et son <strong>Opéra</strong> : <strong>M8 directe</strong>.",
            "Pour <strong>Châtelet</strong> : <strong>M8 + M1</strong> via Bastille.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🛍️", "Marché d'Aligre, l'un des plus animés", "Le <strong>Marché d'Aligre</strong>, à 5 min à pied, est l'un des <strong>marchés les plus animés de Paris</strong>. Comprend trois parties : le <strong>marché alimentaire à ciel ouvert</strong> (place d'Aligre), le <strong>marché couvert Beauvau</strong> (1843), et le <strong>marché aux puces d'Aligre</strong> (brocante). <strong>Ouvert tous les jours sauf lundi</strong>. <strong>Atmosphère populaire et multi-ethnique</strong>. <strong>Prix attractifs</strong>."),
            ("🪑", "Faubourg Saint-Antoine, quartier du meuble", "Le <strong>Faubourg Saint-Antoine</strong>, autour de la station, est historiquement le <strong>quartier des artisans du meuble</strong> depuis le <strong>XIIIe siècle</strong>. <strong>Privilèges accordés par Louis XI</strong> en <strong>1471</strong> permettent aux artisans d'exercer hors des corporations parisiennes. <strong>Centre d'effervescence révolutionnaire</strong> en 1789 (<strong>prise de la Bastille</strong>) et 1848. <strong>Quartier traditionnel des ébénistes, doreurs, tapissiers</strong>. Tradition aujourd'hui en déclin mais quelques <strong>cours-ateliers</strong> historiques subsistent.")
        ],
        "itin": [
            ("Marché d'Aligre", "ledru-rollin", "à pied", "Place d'Aligre (5 min)", 5),
            ("Bastille", "bastille", "M8", "M8 directe (1 station)", 2),
            ("Opéra Bastille", "bastille", "M8", "M8 directe (1 station)", 3),
            ("Châtelet", "chatelet", "M8 + M1", "M8 → Bastille + M1", 10),
            ("Place des Vosges", "saint-paul", "M8 + M1", "M8 → Bastille + M1", 8),
            ("Reuilly - Diderot", "reuilly-diderot", "M8", "M8 directe (2 stations)", 4)
        ]
    },
    "faidherbe-chaligny": {
        "addr": "Rue du Faubourg-Saint-Antoine, 75011 Paris", "arr": "11e arrondissement (Paris)",
        "seo": "Station Faidherbe - Chaligny (M8) rue du Faubourg-Saint-Antoine dans le 11e. Hommage au général Louis Faidherbe (Sénégal).",
        "tagline": "M8 — Faidherbe, gouverneur du Sénégal",
        "hero_desc": "Station <strong>Faidherbe - Chaligny</strong> sur la <strong>rue du Faubourg-Saint-Antoine</strong> dans le <strong>11e arrondissement</strong>. Desservie par la <strong>M8</strong>, ouverte le <strong>5 mai 1931</strong>. Hommage à <strong>Louis Faidherbe</strong> (<strong>1818-1889</strong>), <strong>général et gouverneur du Sénégal</strong>.",
        "intros": [
            "La station <strong>Faidherbe - Chaligny</strong> est implantée sur la <strong>rue du Faubourg-Saint-Antoine</strong> dans le <strong>11e arrondissement</strong>. Elle est desservie par la <strong>M8</strong>, entre <strong>Ledru-Rollin</strong> (1 station) et <strong>Reuilly - Diderot</strong> (1 station). Bus 20, 56, 76, 86.",
            "Ouverte le <strong>5 mai 1931</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Faidherbe</strong> rend hommage à <strong>Louis Léon César Faidherbe</strong> (<strong>1818-1889</strong>), <strong>général français</strong>, <strong>gouverneur du Sénégal</strong> (1854-1865). <strong>Chaligny</strong> rappelle la <strong>rue Chaligny</strong> à proximité."
        ],
        "hist_title": "1931 : Faidherbe, gouverneur du Sénégal",
        "hist": [
            "La station Faidherbe - Chaligny est <strong>inaugurée le 5 mai 1931</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Faidherbe</strong> rend hommage à <strong>Louis Léon César Faidherbe</strong> (<strong>3 juin 1818 - 28 septembre 1889</strong>), <strong>général français</strong>. <strong>Gouverneur du Sénégal</strong> de <strong>1854 à 1861</strong> puis de <strong>1863 à 1865</strong>.",
            "<strong>Polytechnicien</strong>, officier du <strong>génie</strong>. <strong>Élargit le territoire colonial sénégalais</strong>, <strong>développe Saint-Louis du Sénégal</strong>, <strong>construit la route Saint-Louis - Dakar</strong>. <strong>Étude des populations africaines</strong> (linguistique, ethnographie). <strong>Commande l'armée du Nord</strong> lors de la <strong>guerre de 1870</strong>. La <strong>rue Chaligny</strong> rend hommage à <strong>François Chaligny</strong>, riche propriétaire du XVIIIe siècle qui possédait des terrains dans le quartier."
        ],
        "faq": [
            ("Quelle ligne dessert Faidherbe - Chaligny ?", "Uniquement la <strong>M8</strong>. Bus 20, 56, 76, 86."),
            ("Qui est Faidherbe ?", "<strong>Louis Faidherbe</strong> (1818-1889), <strong>général</strong>, <strong>gouverneur du Sénégal</strong> (1854-1865)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 mai 1931</strong>."),
            ("Pour Bastille ?", "<strong>M8 directe</strong> (2 stations)."),
            ("Pour Nation ?", "<strong>M8 + M2</strong> via Reuilly - Diderot."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier <strong>résidentiel</strong> du 11e/12e.",
            "<strong>Faubourg Saint-Antoine</strong> : ancien quartier des artisans.",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong>.",
            "Pour <strong>Marché d'Aligre</strong> : <strong>M8 → Ledru-Rollin</strong> + à pied.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🌍", "Faidherbe, gouverneur du Sénégal", "<strong>Louis Léon César Faidherbe</strong> (1818-1889), <strong>général français</strong>, <strong>gouverneur du Sénégal</strong> de <strong>1854 à 1861</strong> puis de <strong>1863 à 1865</strong>. <strong>Polytechnicien</strong> (1838), officier du <strong>génie</strong>. <strong>Élargit le territoire colonial sénégalais</strong>. <strong>Développe Saint-Louis du Sénégal</strong> (ancienne capitale). <strong>Construit la route Saint-Louis - Dakar</strong>. <strong>Étude des populations africaines</strong> : <strong>Grammaire et vocabulaire de la langue poul</strong>. <strong>Commande l'armée du Nord</strong> lors de la guerre de 1870."),
            ("🏛️", "11e/12e résidentiel et populaire", "Le quartier autour de la station fait partie des <strong>11e et 12e arrondissements</strong>. <strong>Ancien faubourg ouvrier</strong> du XIXe siècle, en <strong>gentrification progressive</strong>. <strong>Faubourg Saint-Antoine</strong> traditionnellement <strong>quartier des artisans du meuble</strong>. Tradition aujourd'hui en déclin.")
        ],
        "itin": [
            ("Bastille", "bastille", "M8", "M8 directe (2 stations)", 4),
            ("Marché d'Aligre", "ledru-rollin", "M8 + à pied", "M8 → Ledru-Rollin + 5 min", 7),
            ("Reuilly - Diderot", "reuilly-diderot", "M8", "M8 directe (1 station)", 2),
            ("Nation", "nation", "M8 + M2", "M8 → Reuilly + M2 ou M8 directe", 8),
            ("Place des Vosges", "saint-paul", "M8 + M1", "M8 → Bastille + M1", 10),
            ("Châtelet", "chatelet", "M8 + M1", "M8 → Bastille + M1", 12)
        ]
    },
    "montgallet": {
        "addr": "Rue de Reuilly, 75012 Paris", "arr": "12e arrondissement (Paris)",
        "seo": "Station Montgallet (M8) rue de Reuilly dans le 12e. Rue Montgallet célèbre pour ses magasins d'informatique d'occasion.",
        "tagline": "M8 — Montgallet, informatique d'occasion",
        "hero_desc": "Station <strong>Montgallet</strong> sur la <strong>rue de Reuilly</strong> dans le <strong>12e arrondissement</strong>. Desservie par la <strong>M8</strong>, ouverte le <strong>5 mai 1931</strong>. La <strong>rue Montgallet</strong> est célèbre pour ses <strong>nombreuses boutiques d'informatique d'occasion et de pièces détachées</strong>.",
        "intros": [
            "La station <strong>Montgallet</strong> est implantée sur la <strong>rue de Reuilly</strong> dans le <strong>12e arrondissement</strong>. Elle est desservie par la <strong>M8</strong>, entre <strong>Reuilly - Diderot</strong> (1 station) et <strong>Daumesnil</strong> (1 station). Bus 46, 86.",
            "Ouverte le <strong>5 mai 1931</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Montgallet</strong> rend hommage à un <strong>ancien propriétaire</strong> du quartier au XVIIIe siècle. La <strong>rue Montgallet</strong> est aujourd'hui célèbre pour ses <strong>nombreuses boutiques d'informatique d'occasion, de pièces détachées et de réparations</strong>."
        ],
        "hist_title": "1931 : Montgallet et informatique d'occasion",
        "hist": [
            "La station Montgallet est <strong>inaugurée le 5 mai 1931</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Montgallet</strong> rend hommage à un <strong>ancien propriétaire</strong> du quartier au <strong>XVIIIe siècle</strong>, dont les terrains furent lotis lors de l'urbanisation du <strong>faubourg Saint-Antoine</strong>.",
            "Aujourd'hui, la <strong>rue Montgallet</strong> est <strong>célèbre pour ses nombreuses boutiques d'informatique</strong> : <strong>ordinateurs neufs et d'occasion</strong>, <strong>pièces détachées</strong>, <strong>périphériques</strong>, <strong>réparations</strong>, <strong>récupération de données</strong>. <strong>~30 boutiques</strong> sur ~200 m. <strong>Concentration unique</strong> à Paris, fréquentée par <strong>professionnels et particuliers</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Montgallet ?", "Uniquement la <strong>M8</strong>. Bus 46, 86."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 mai 1931</strong>."),
            ("Qu'est-ce que la rue Montgallet ?", "Rue <strong>célèbre pour ses ~30 boutiques d'informatique d'occasion</strong>, pièces détachées, réparations."),
            ("Pour réparer un ordinateur ?", "<strong>Rue Montgallet</strong> à la sortie : ~30 boutiques d'informatique."),
            ("Pour Daumesnil (hub M6+M8) ?", "<strong>M8 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "<strong>Rue Montgallet</strong> : ~30 boutiques d'informatique d'occasion.",
            "<strong>Réparation, pièces détachées, ordinateurs neufs et occasion</strong>.",
            "Pour <strong>Daumesnil</strong> (hub M6+M8) : <strong>M8 directe</strong>.",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("💻", "Rue Montgallet, mecque de l'informatique", "La <strong>rue Montgallet</strong> est <strong>célèbre dans le monde de l'informatique parisien</strong>. <strong>~30 boutiques</strong> spécialisées dans l'<strong>informatique d'occasion</strong> sur environ <strong>200 m</strong>. <strong>Ordinateurs neufs et d'occasion</strong>, <strong>pièces détachées</strong> (cartes mères, disques durs, RAM, processeurs), <strong>périphériques</strong>, <strong>réparations</strong>, <strong>récupération de données</strong>. <strong>Concentration unique</strong> en France. Fréquentée par <strong>professionnels et particuliers</strong>. Tradition née dans les années 1990 lors de l'<strong>essor des PC</strong>."),
            ("🏘️", "Quartier de Reuilly", "Le quartier autour de la station fait partie du <strong>12e arrondissement</strong>, secteur résidentiel et commerçant à proximité de <strong>Bastille</strong> et <strong>Nation</strong>. <strong>Faubourg Saint-Antoine</strong> historiquement <strong>quartier des artisans du meuble</strong>. Aujourd'hui, mix de <strong>petites maisons, immeubles haussmanniens, ateliers reconvertis</strong>.")
        ],
        "itin": [
            ("Rue Montgallet (informatique)", "montgallet", "à pied", "Sortie directe", 1),
            ("Daumesnil (hub M6+M8)", "daumesnil", "M8", "M8 directe (1 station)", 2),
            ("Reuilly - Diderot", "reuilly-diderot", "M8", "M8 directe (1 station)", 2),
            ("Bastille", "bastille", "M8", "M8 directe (3 stations)", 6),
            ("Bercy (M6+M14)", "bercy", "M8 + M14", "M8 → Daumesnil + M6", 8),
            ("Nation", "nation", "M8 + M2", "M8 → Reuilly + M2", 10)
        ]
    },
    "michel-bizot": {
        "addr": "Avenue du Général Michel-Bizot, 75012 Paris", "arr": "12e arrondissement (Paris)",
        "seo": "Station Michel Bizot (M8) avenue du Général Michel-Bizot dans le 12e. Quartier 12e résidentiel.",
        "tagline": "M8 — Michel Bizot, 12e résidentiel",
        "hero_desc": "Station <strong>Michel Bizot</strong> sur l'<strong>avenue du Général Michel-Bizot</strong> dans le <strong>12e arrondissement</strong>. Desservie par la <strong>M8</strong>, ouverte le <strong>5 mai 1931</strong>. Hommage à <strong>Michel Bizot</strong> (<strong>1795-1855</strong>), <strong>général français</strong>.",
        "intros": [
            "La station <strong>Michel Bizot</strong> est implantée sur l'<strong>avenue du Général Michel-Bizot</strong> dans le <strong>12e arrondissement</strong>. Elle est desservie par la <strong>M8</strong>, entre <strong>Daumesnil</strong> (1 station) et <strong>Porte Dorée</strong> (1 station). Bus 46.",
            "Ouverte le <strong>5 mai 1931</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Michel Bizot</strong> rend hommage à <strong>Michel Bizot</strong> (<strong>1795-1855</strong>), <strong>général français</strong> du XIXe siècle. Quartier <strong>résidentiel</strong> du <strong>12e arrondissement</strong>."
        ],
        "hist_title": "1931 : Michel Bizot et 12e résidentiel",
        "hist": [
            "La station Michel Bizot est <strong>inaugurée le 5 mai 1931</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Michel Bizot</strong> rend hommage à <strong>Michel Bizot</strong> (<strong>1795-1855</strong>), <strong>général français</strong> du XIXe siècle. <strong>Polytechnicien</strong>, officier du <strong>génie</strong>. Participa à la <strong>guerre de Crimée</strong> (1853-1856).",
            "Le quartier autour de la station fait partie du <strong>12e arrondissement</strong>, secteur <strong>résidentiel</strong>. À proximité : le <strong>Bois de Vincennes</strong> et le <strong>Palais de la Porte Dorée</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Michel Bizot ?", "Uniquement la <strong>M8</strong>. Bus 46."),
            ("Qui est Michel Bizot ?", "<strong>Michel Bizot</strong> (1795-1855), <strong>général français</strong> du XIXe siècle."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 mai 1931</strong>."),
            ("Pour le Bois de Vincennes ?", "<strong>M8 → Porte Dorée</strong> (1 station)."),
            ("Pour Daumesnil ?", "<strong>M8 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Quartier résidentiel du <strong>12e</strong>.",
            "Pour <strong>Bois de Vincennes</strong> : <strong>M8 → Porte Dorée</strong>.",
            "Pour <strong>Palais de la Porte Dorée</strong> : <strong>M8 directe</strong> (1 station).",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "12e arrondissement, contrastes", "Le <strong>12e arrondissement</strong> (~145 000 habitants) présente un mix de <strong>quartiers résidentiels</strong>, du <strong>secteur Bercy</strong> (Cinémathèque française, parc de Bercy, nouveaux quartiers), du <strong>Faubourg Saint-Antoine</strong> (artisans du meuble), et du <strong>Bois de Vincennes</strong>. <strong>Mairie</strong> place Daumesnil. <strong>Promenade plantée</strong> (1993) reconvertie d'une ancienne voie ferrée."),
            ("🌳", "Bois de Vincennes à proximité", "Le <strong>Bois de Vincennes</strong>, à courte distance via la <strong>M8 → Porte Dorée</strong>, est le <strong>plus grand espace vert de Paris</strong> avec <strong>995 hectares</strong>. <strong>Cédé à la Ville de Paris en 1860</strong> par Napoléon III. Abrite : <strong>château de Vincennes</strong>, <strong>parc zoologique de Paris</strong> (rénové 2014), <strong>hippodrome</strong>, <strong>lac Daumesnil</strong>, <strong>parc floral</strong>, <strong>Cartoucherie</strong> (théâtre).")
        ],
        "itin": [
            ("Daumesnil", "daumesnil", "M8", "M8 directe (1 station)", 2),
            ("Porte Dorée (Palais)", "porte-doree", "M8", "M8 directe (1 station)", 2),
            ("Bois de Vincennes", "porte-doree", "M8", "M8 directe (1 station)", 5),
            ("Bastille", "bastille", "M8", "M8 directe (~10 min)", 10),
            ("Nation", "nation", "M8 + M2", "M8 → Reuilly + M2", 8),
            ("Place de la République", "republique", "M8", "M8 directe (~16 min)", 16)
        ]
    },
    "porte-doree": {
        "addr": "Avenue Daumesnil, 75012 Paris", "arr": "12e arrondissement (Paris)",
        "seo": "Station Porte Dorée (M8) avenue Daumesnil dans le 12e. Palais de la Porte Dorée (Cité immigration + aquarium tropical). Bois de Vincennes.",
        "tagline": "M8 — Palais de la Porte Dorée et Bois de Vincennes",
        "hero_desc": "Station <strong>Porte Dorée</strong> sur l'<strong>avenue Daumesnil</strong> dans le <strong>12e arrondissement</strong>. Desservie par la <strong>M8</strong>, ouverte le <strong>5 mai 1931</strong>. À la sortie : le <strong>Palais de la Porte Dorée</strong> (1931), <strong>Musée de l'Histoire de l'Immigration</strong> et <strong>aquarium tropical</strong>. <strong>Bois de Vincennes</strong>. Correspondance <strong>tramway T3a</strong>.",
        "intros": [
            "La station <strong>Porte Dorée</strong> est implantée sur l'<strong>avenue Daumesnil</strong> dans le <strong>12e arrondissement</strong>, à la <strong>limite sud-est de Paris</strong>. Elle est desservie par la <strong>M8</strong> et le <strong>tramway T3a</strong>. Bus 46, 86, 87, 325.",
            "Ouverte le <strong>5 mai 1931</strong>.",
            "À la sortie : le <strong>Palais de la Porte Dorée</strong>, <strong>édifice Art Déco</strong> construit pour l'<strong>Exposition coloniale de 1931</strong>. Abrite le <strong>Musée national de l'histoire de l'Immigration</strong> et un <strong>aquarium tropical</strong>. Le <strong>Bois de Vincennes</strong> à courte distance."
        ],
        "hist_title": "1931 : Palais Porte Dorée et Exposition coloniale",
        "hist": [
            "La station Porte Dorée est <strong>inaugurée le 5 mai 1931</strong> avec le <strong>prolongement de la M8</strong>, à l'occasion de l'<strong>Exposition coloniale internationale de 1931</strong>.",
            "Le <strong>Palais de la Porte Dorée</strong>, à la sortie, est <strong>construit pour l'Exposition coloniale de 1931</strong>. Architectes : <strong>Albert Laprade</strong> et <strong>Léon Jaussely</strong>. <strong>Style Art Déco</strong>. <strong>Façade ornée d'un haut-relief sculpté</strong> par <strong>Alfred Janniot</strong>.",
            "Abrite aujourd'hui le <strong>Musée national de l'histoire de l'Immigration</strong> (depuis 2007) et un <strong>aquarium tropical</strong> (depuis 1931, l'un des <strong>plus anciens d'Europe</strong>). <strong>15 000 poissons et reptiles</strong>. Le <strong>Bois de Vincennes</strong>, à courte distance, est le <strong>plus grand espace vert de Paris</strong> (995 hectares). <strong>Tramway T3a</strong> en correspondance."
        ],
        "faq": [
            ("Quelles lignes desservent Porte Dorée ?", "<strong>M8</strong> et <strong>tramway T3a</strong>. Bus 46, 86, 87, 325."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 mai 1931</strong>."),
            ("Qu'est-ce que le Palais de la Porte Dorée ?", "<strong>Édifice Art Déco</strong> construit pour l'<strong>Exposition coloniale de 1931</strong>. Musée Immigration + aquarium tropical."),
            ("Pour le Musée Immigration ?", "<strong>Sortie directe</strong>."),
            ("Pour l'aquarium tropical ?", "<strong>Sortie directe</strong>. 15 000 poissons et reptiles."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Palais de la Porte Dorée</strong> à la sortie : Musée Immigration + aquarium tropical.",
            "<strong>Bois de Vincennes</strong> à courte distance.",
            "<strong>Tramway T3a</strong> en correspondance.",
            "Pour <strong>parc zoologique</strong> : ~10 min à pied.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏛️", "Palais de la Porte Dorée (1931)", "Le <strong>Palais de la Porte Dorée</strong>, à la sortie, est <strong>construit pour l'Exposition coloniale internationale de 1931</strong>. Architectes : <strong>Albert Laprade</strong> et <strong>Léon Jaussely</strong>. <strong>Style Art Déco</strong>. <strong>Façade ornée d'un haut-relief sculpté</strong> par <strong>Alfred Janniot</strong> représentant les <strong>territoires coloniaux français</strong>. <strong>Salons décorés</strong> par <strong>Pierre Ducos de La Haille</strong>. <strong>Classé monument historique</strong>. Aujourd'hui : <strong>Musée national de l'histoire de l'Immigration</strong> (2007) + <strong>aquarium tropical</strong> (1931)."),
            ("🐠", "Aquarium tropical (1931)", "L'<strong>aquarium tropical du Palais de la Porte Dorée</strong>, à la sortie, est l'un des <strong>plus anciens aquariums d'Europe</strong>. <strong>Inauguré en 1931</strong> pour l'Exposition coloniale. <strong>~15 000 poissons et reptiles</strong>. <strong>~84 bassins</strong>. <strong>Poissons tropicaux</strong> (eau douce et eau de mer), <strong>crocodiles</strong>, <strong>tortues</strong>. <strong>Rénové en 2007</strong>.")
        ],
        "itin": [
            ("Palais de la Porte Dorée", "porte-doree", "à pied", "Sortie directe", 1),
            ("Aquarium tropical", "porte-doree", "à pied", "Sortie directe", 2),
            ("Bois de Vincennes", "porte-doree", "à pied", "5 min à pied", 5),
            ("Parc zoologique de Paris", "porte-doree", "à pied", "10 min à pied", 10),
            ("Tramway T3a", "porte-doree", "T3a", "Correspondance directe", 1),
            ("Bastille", "bastille", "M8", "M8 directe (~12 min)", 12)
        ]
    },
    "porte-de-charenton": {
        "addr": "Avenue Daumesnil, 75012 Paris", "arr": "12e arrondissement (Paris)",
        "seo": "Station Porte de Charenton (M8) avenue Daumesnil dans le 12e. Boulevard Périphérique. Bois de Vincennes proche.",
        "tagline": "M8 — Porte de Charenton, limite Paris",
        "hero_desc": "Station <strong>Porte de Charenton</strong> sur l'<strong>avenue Daumesnil</strong> dans le <strong>12e arrondissement</strong>. Desservie par la <strong>M8</strong>, ouverte le <strong>5 mai 1931</strong>. À la <strong>limite sud-est de Paris</strong>, à proximité du <strong>boulevard Périphérique</strong> et du <strong>Bois de Vincennes</strong>.",
        "intros": [
            "La station <strong>Porte de Charenton</strong> est implantée sur l'<strong>avenue Daumesnil</strong> dans le <strong>12e arrondissement</strong>, à la <strong>limite sud-est de Paris</strong>. Elle est desservie par la <strong>M8</strong>, entre <strong>Porte Dorée</strong> (1 station) et <strong>Liberté</strong> (1 station, banlieue). Bus 46, 109, 111, 325.",
            "Ouverte le <strong>5 mai 1931</strong>.",
            "À proximité : le <strong>boulevard Périphérique</strong> et la <strong>commune de Charenton-le-Pont</strong> (Val-de-Marne). Le <strong>Bois de Vincennes</strong> à courte distance."
        ],
        "hist_title": "1931 : porte sud-est et Charenton",
        "hist": [
            "La station Porte de Charenton est <strong>inaugurée le 5 mai 1931</strong>.",
            "Le nom <strong>Porte de Charenton</strong> rappelle l'<strong>ancienne porte de l'enceinte de Thiers</strong> (1844-1929), qui marquait la <strong>sortie de Paris vers Charenton-le-Pont</strong>.",
            "<strong>Charenton-le-Pont</strong> (~30 000 habitants), commune du <strong>Val-de-Marne</strong>. <strong>Étymologie</strong> : du latin <em>Carentum</em>, peut-être nom d'un domaine gallo-romain. Connue pour l'<strong>asile de Charenton</strong> (ancien hôpital psychiatrique, fondé en 1641, où fut interné le <strong>marquis de Sade</strong>). Aujourd'hui, ville résidentielle."
        ],
        "faq": [
            ("Quelle ligne dessert Porte de Charenton ?", "Uniquement la <strong>M8</strong>. Bus 46, 109, 111, 325."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 mai 1931</strong>."),
            ("Pour Charenton-le-Pont ?", "<strong>M8 directe</strong> (1 station vers Liberté)."),
            ("Pour le Bois de Vincennes ?", "<strong>M8 → Porte Dorée</strong> + à pied."),
            ("Pour Bastille ?", "<strong>M8 directe</strong> (~14 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>.")
        ],
        "tips": [
            "Pour <strong>Charenton-le-Pont</strong> : <strong>M8 directe</strong>.",
            "Pour <strong>Bois de Vincennes</strong> : <strong>M8 → Porte Dorée</strong>.",
            "Pour <strong>Palais de la Porte Dorée</strong> : <strong>M8 directe</strong> (1 station).",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏘️", "Charenton-le-Pont, commune historique", "<strong>Charenton-le-Pont</strong> (~30 000 habitants), commune du <strong>Val-de-Marne</strong>. <strong>Étymologie</strong> : du latin <em>Carentum</em> (domaine gallo-romain). Connue pour l'<strong>ancien asile de Charenton</strong> (fondé en 1641 par les frères de Saint-Jean-de-Dieu), <strong>premier asile psychiatrique de France</strong>. Le <strong>marquis de Sade</strong> y fut interné de <strong>1801 à 1814</strong>. Aujourd'hui, ville résidentielle dynamique."),
            ("🚇", "Enceinte de Thiers et portes parisiennes", "L'<strong>enceinte de Thiers</strong>, construite de <strong>1841 à 1844</strong>, était le <strong>dernier mur d'enceinte de Paris</strong>. <strong>33 km de long</strong>, <strong>61 portes</strong>. Démolie de <strong>1919 à 1929</strong>. Les <strong>noms des portes</strong> survivent dans les stations métro : <strong>Porte de Charenton, Porte Dorée, Porte de Vincennes, Porte d'Italie, etc.</strong>")
        ],
        "itin": [
            ("Liberté (Charenton)", "liberte", "M8", "M8 directe (1 station)", 2),
            ("Palais Porte Dorée", "porte-doree", "M8", "M8 directe (1 station)", 2),
            ("Bois de Vincennes", "porte-doree", "M8 + à pied", "M8 → Porte Dorée + à pied", 7),
            ("Bastille", "bastille", "M8", "M8 directe (~14 min)", 14),
            ("Nation", "nation", "M8 + M2", "M8 → Reuilly + M2", 16),
            ("Châtelet", "chatelet", "M8 + M1", "M8 → Bastille + M1", 20)
        ]
    },
    "liberte": {
        "addr": "Rue de Paris, 94220 Charenton-le-Pont", "arr": "Charenton-le-Pont (94)",
        "seo": "Station Liberté (M8) à Charenton-le-Pont (94). Place de la Liberté. Quartier Charenton-le-Pont.",
        "tagline": "M8 — Charenton-le-Pont",
        "hero_desc": "Station <strong>Liberté</strong> à <strong>Charenton-le-Pont</strong> (Val-de-Marne, 94). Desservie par la <strong>M8</strong>, ouverte le <strong>5 mai 1931</strong>. Quartier <strong>Charenton-le-Pont</strong>.",
        "intros": [
            "La station <strong>Liberté</strong> est implantée à <strong>Charenton-le-Pont</strong> (Val-de-Marne, 94). Elle est desservie par la <strong>M8</strong>, entre <strong>Porte de Charenton</strong> (1 station) et <strong>Charenton - Écoles</strong> (1 station). Bus 24, 109, 111, 180.",
            "Ouverte le <strong>5 mai 1931</strong>.",
            "Le nom <strong>Liberté</strong> rappelle la <strong>place de la Liberté</strong> à proximité. <strong>Charenton-le-Pont</strong> (~30 000 habitants), commune du <strong>Val-de-Marne</strong>."
        ],
        "hist_title": "1931 : Liberté et Charenton-le-Pont",
        "hist": [
            "La station Liberté est <strong>inaugurée le 5 mai 1931</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Liberté</strong> rappelle la <strong>place de la Liberté</strong> à proximité, nom commun donné à de nombreuses places sous la <strong>IIIe République</strong>.",
            "<strong>Charenton-le-Pont</strong> (~30 000 habitants), commune du <strong>Val-de-Marne</strong>. À proximité : la <strong>confluence de la Marne et de la Seine</strong>, le <strong>Bois de Vincennes</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Liberté ?", "Uniquement la <strong>M8</strong>. Bus 24, 109, 111, 180."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 mai 1931</strong>."),
            ("Quelle commune ?", "<strong>Charenton-le-Pont</strong> (Val-de-Marne, 94)."),
            ("Pour la confluence Marne-Seine ?", "<strong>~10 min à pied</strong>."),
            ("Pour Bastille ?", "<strong>M8 directe</strong> (~16 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Charenton-le-Pont</strong> commune dynamique du 94.",
            "<strong>Confluence Marne-Seine</strong> à 10 min à pied.",
            "Pour <strong>Bois de Vincennes</strong> : <strong>M8 → Porte Dorée</strong>.",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>2</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("🌊", "Confluence Marne-Seine", "À proximité de la station, la <strong>Marne</strong> conflue avec la <strong>Seine</strong>. La <strong>Marne</strong>, <strong>514 km</strong>, est le <strong>principal affluent de la Seine</strong>. Confluence à <strong>Charenton-le-Pont</strong>. <strong>Quais aménagés</strong> en promenade. Point de vue sur la Seine et la Marne."),
            ("🏘️", "Charenton-le-Pont, commune historique", "<strong>Charenton-le-Pont</strong> (~30 000 habitants), commune du <strong>Val-de-Marne</strong>. <strong>Étymologie</strong> : du latin <em>Carentum</em>. Connue pour l'<strong>ancien asile de Charenton</strong> (1641), <strong>premier asile psychiatrique de France</strong>. Le <strong>marquis de Sade</strong> y fut interné. Aujourd'hui, <strong>ville résidentielle dynamique</strong>, <strong>quartier de Bercy 2</strong>, <strong>centre commercial Bercy 2</strong>.")
        ],
        "itin": [
            ("Charenton - Écoles", "charenton-ecoles", "M8", "M8 directe (1 station)", 2),
            ("Confluence Marne-Seine", "liberte", "à pied", "10 min à pied", 10),
            ("Bercy 2", "liberte", "à pied", "5 min à pied", 5),
            ("Bastille", "bastille", "M8", "M8 directe (~16 min)", 16),
            ("Bois de Vincennes", "porte-doree", "M8", "M8 directe (2 stations)", 6),
            ("Châtelet", "chatelet", "M8 + M1", "M8 → Bastille + M1", 22)
        ]
    },
    "charenton-ecoles": {
        "addr": "Rue de Paris, 94220 Charenton-le-Pont", "arr": "Charenton-le-Pont (94)",
        "seo": "Station Charenton - Écoles (M8) à Charenton-le-Pont (94). Centre commerçant et marché de Charenton.",
        "tagline": "M8 — Charenton-le-Pont centre",
        "hero_desc": "Station <strong>Charenton - Écoles</strong> à <strong>Charenton-le-Pont</strong> (Val-de-Marne, 94). Desservie par la <strong>M8</strong>, ouverte le <strong>5 mai 1931</strong>. Centre commerçant de la commune.",
        "intros": [
            "La station <strong>Charenton - Écoles</strong> est implantée à <strong>Charenton-le-Pont</strong> (Val-de-Marne, 94). Elle est desservie par la <strong>M8</strong>, entre <strong>Liberté</strong> (1 station) et <strong>École vétérinaire de Maisons-Alfort</strong> (1 station). Bus 24, 109, 111, 180.",
            "Ouverte le <strong>5 mai 1931</strong>.",
            "<strong>Centre commerçant</strong> de Charenton-le-Pont. À proximité : le <strong>marché de Charenton</strong>, les <strong>commerces de proximité</strong>."
        ],
        "hist_title": "1931 : Charenton centre commerçant",
        "hist": [
            "La station Charenton - Écoles est <strong>inaugurée le 5 mai 1931</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Écoles</strong> rappelle les <strong>établissements scolaires</strong> à proximité.",
            "<strong>Charenton-le-Pont</strong> (~30 000 habitants), commune du <strong>Val-de-Marne</strong>. Centre commerçant avec <strong>marché de Charenton</strong>, <strong>boutiques</strong>, <strong>restaurants</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Charenton - Écoles ?", "Uniquement la <strong>M8</strong>. Bus 24, 109, 111, 180."),
            ("Quand a-t-elle ouvert ?", "Le <strong>5 mai 1931</strong>."),
            ("Pour le marché de Charenton ?", "<strong>~5 min à pied</strong>."),
            ("Pour Bastille ?", "<strong>M8 directe</strong> (~18 min)."),
            ("Pour l'École vétérinaire d'Alfort ?", "<strong>M8 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Marché de Charenton</strong> à 5 min à pied.",
            "<strong>Centre commerçant</strong> de la commune.",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong>.",
            "Pour <strong>École vétérinaire d'Alfort</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>2</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("🛍️", "Charenton-le-Pont, commune dynamique", "<strong>Charenton-le-Pont</strong> (~30 000 habitants), commune du <strong>Val-de-Marne</strong>. Quartier <strong>résidentiel et commerçant</strong> dynamique. <strong>Marché de Charenton</strong> à proximité. <strong>Centre commercial Bercy 2</strong> (1990) accessible à pied. Ancien <strong>asile de Charenton</strong> (1641-1969) reconverti en <strong>hôpital général</strong>."),
            ("🚇", "Faubourg Saint-Antoine et axe est-ouest", "L'<strong>axe de la M8</strong> dessert la <strong>continuité historique</strong> entre <strong>Paris centre (Faubourg Saint-Antoine)</strong> et la <strong>banlieue est (Charenton, Maisons-Alfort, Créteil)</strong>. Cette continuité <strong>remonte au XVIIIe siècle</strong> avec le développement des <strong>faubourgs ouvriers</strong>.")
        ],
        "itin": [
            ("Marché de Charenton", "charenton-ecoles", "à pied", "5 min à pied", 5),
            ("École vétérinaire Alfort", "ecole-veterinaire-de-maisons-alfort", "M8", "M8 directe (1 station)", 2),
            ("Liberté", "liberte", "M8", "M8 directe (1 station)", 2),
            ("Bastille", "bastille", "M8", "M8 directe (~18 min)", 18),
            ("Bois de Vincennes", "porte-doree", "M8", "M8 directe (3 stations)", 8),
            ("Créteil - Préfecture", "creteil-prefecture", "M8", "M8 directe (~14 min)", 14)
        ]
    },
    "ecole-veterinaire-de-maisons-alfort": {
        "addr": "Avenue du Général-de-Gaulle, 94700 Maisons-Alfort", "arr": "Maisons-Alfort (94)",
        "seo": "Station École vétérinaire de Maisons-Alfort (M8) à Maisons-Alfort (94). École nationale vétérinaire d'Alfort (1766), une des plus anciennes au monde.",
        "tagline": "M8 — École nationale vétérinaire d'Alfort (1766)",
        "hero_desc": "Station <strong>École vétérinaire de Maisons-Alfort</strong> à <strong>Maisons-Alfort</strong> (Val-de-Marne, 94). Desservie par la <strong>M8</strong>, ouverte le <strong>5 mai 1931</strong>. À la sortie : l'<strong>École nationale vétérinaire d'Alfort</strong>, fondée en <strong>1766</strong>, <strong>une des plus anciennes écoles vétérinaires au monde</strong>.",
        "intros": [
            "La station <strong>École vétérinaire de Maisons-Alfort</strong> est implantée à <strong>Maisons-Alfort</strong> (Val-de-Marne, 94). Elle est desservie par la <strong>M8</strong>, entre <strong>Charenton - Écoles</strong> (1 station) et <strong>Maisons-Alfort - Stade</strong> (1 station). Bus 24, 103, 107, 217.",
            "Ouverte le <strong>5 mai 1931</strong>.",
            "À la sortie : l'<strong>École nationale vétérinaire d'Alfort (EnvA)</strong>, fondée en <strong>1766</strong> sous <strong>Louis XV</strong> par <strong>Claude Bourgelat</strong>. <strong>Une des plus anciennes écoles vétérinaires au monde</strong> (2e après celle de Lyon, 1762). <strong>~600 étudiants</strong>."
        ],
        "hist_title": "1931 : École vétérinaire d'Alfort (1766)",
        "hist": [
            "La station est <strong>inaugurée le 5 mai 1931</strong>.",
            "L'<strong>École nationale vétérinaire d'Alfort (EnvA)</strong>, à la sortie, est fondée en <strong>1766</strong> sous <strong>Louis XV</strong> par <strong>Claude Bourgelat</strong> (1712-1779), <strong>écuyer du roi</strong> et <strong>fondateur de l'enseignement vétérinaire moderne</strong>.",
            "<strong>2e plus ancienne école vétérinaire au monde</strong>, après celle de <strong>Lyon</strong> (1762, également fondée par Bourgelat). <strong>~600 étudiants</strong>. <strong>Formation des vétérinaires</strong>, recherche en <strong>santé animale</strong>, <strong>épidémiologie</strong>. <strong>Musée Fragonard</strong> ouvert au public : <strong>« écorchés » d'Honoré Fragonard</strong> (XVIIIe), <strong>collection anatomique</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert École vétérinaire de Maisons-Alfort ?", "Uniquement la <strong>M8</strong>. Bus 24, 103, 107, 217."),
            ("Quand l'École a-t-elle été fondée ?", "En <strong>1766</strong> par <strong>Claude Bourgelat</strong> sous Louis XV."),
            ("Quand la station a-t-elle ouvert ?", "Le <strong>5 mai 1931</strong>."),
            ("Pour le Musée Fragonard ?", "<strong>~5 min à pied</strong> dans l'enceinte de l'École vétérinaire."),
            ("Pour Châtelet ?", "<strong>M8 directe</strong> (~24 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>École nationale vétérinaire d'Alfort</strong> à la sortie : 2e plus ancienne au monde.",
            "<strong>Musée Fragonard</strong> ouvert au public : « écorchés » et collection anatomique.",
            "Pour <strong>Châtelet</strong> : <strong>M8 directe</strong>.",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("🐴", "École vétérinaire d'Alfort (1766)", "L'<strong>École nationale vétérinaire d'Alfort (EnvA)</strong>, à la sortie, est fondée en <strong>1766</strong> sous <strong>Louis XV</strong> par <strong>Claude Bourgelat</strong> (1712-1779), <strong>écuyer du roi</strong> et <strong>fondateur de l'enseignement vétérinaire moderne</strong>. <strong>2e plus ancienne école vétérinaire au monde</strong>, après celle de <strong>Lyon</strong> (1762, également fondée par Bourgelat). <strong>~600 étudiants</strong>. <strong>Domaine de 9 hectares</strong>. <strong>Formation de 5 ans</strong>. <strong>Inscrite aux monuments historiques</strong>."),
            ("💀", "Musée Fragonard, « écorchés »", "Le <strong>Musée Fragonard</strong>, dans l'enceinte de l'École vétérinaire, est ouvert au public. <strong>Collection d'« écorchés »</strong> réalisés par <strong>Honoré Fragonard</strong> (<strong>1732-1799</strong>), <strong>cousin du peintre Jean-Honoré Fragonard</strong>. <strong>Anatomiste de génie</strong>, il développa une <strong>technique unique</strong> de <strong>conservation des cadavres</strong> permettant de les <strong>écorcher</strong> tout en <strong>conservant les muscles et les vaisseaux</strong>. <strong>Œuvre la plus célèbre</strong> : <em>Cavalier de l'Apocalypse</em>. <strong>Curiosité macabre du XVIIIe</strong>.")
        ],
        "itin": [
            ("École vétérinaire", "ecole-veterinaire-de-maisons-alfort", "à pied", "Sortie directe", 1),
            ("Musée Fragonard", "ecole-veterinaire-de-maisons-alfort", "à pied", "Enceinte École (5 min)", 5),
            ("Maisons-Alfort - Stade", "maisons-alfort-stade", "M8", "M8 directe (1 station)", 2),
            ("Charenton - Écoles", "charenton-ecoles", "M8", "M8 directe (1 station)", 2),
            ("Bastille", "bastille", "M8", "M8 directe (~20 min)", 20),
            ("Châtelet", "chatelet", "M8 + M1", "M8 → Bastille + M1", 24)
        ]
    },
    "maisons-alfort-stade": {
        "addr": "Avenue du Général-de-Gaulle, 94700 Maisons-Alfort", "arr": "Maisons-Alfort (94)",
        "seo": "Station Maisons-Alfort - Stade (M8) à Maisons-Alfort (94). Stade Léo Lagrange. Quartier résidentiel.",
        "tagline": "M8 — Maisons-Alfort, Stade Léo Lagrange",
        "hero_desc": "Station <strong>Maisons-Alfort - Stade</strong> à <strong>Maisons-Alfort</strong> (Val-de-Marne, 94). Desservie par la <strong>M8</strong>, ouverte le <strong>27 avril 1972</strong>. À proximité du <strong>Stade Léo Lagrange</strong>.",
        "intros": [
            "La station <strong>Maisons-Alfort - Stade</strong> est implantée à <strong>Maisons-Alfort</strong> (Val-de-Marne, 94). Elle est desservie par la <strong>M8</strong>, entre <strong>École vétérinaire de Maisons-Alfort</strong> (1 station) et <strong>Maisons-Alfort - Les Juilliottes</strong> (1 station). Bus 24, 103, 107.",
            "Ouverte le <strong>27 avril 1972</strong> avec le <strong>prolongement de la M8</strong> de Charenton - Écoles à Maisons-Alfort - Les Juilliottes.",
            "À proximité : le <strong>Stade Léo Lagrange</strong> de Maisons-Alfort. <strong>Maisons-Alfort</strong> (~54 000 habitants), commune dynamique du <strong>Val-de-Marne</strong>."
        ],
        "hist_title": "1972 : prolongement M8 vers Maisons-Alfort",
        "hist": [
            "La station Maisons-Alfort - Stade est <strong>inaugurée le 27 avril 1972</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Stade</strong> rappelle le <strong>Stade Léo Lagrange</strong> à proximité, équipement sportif communal. Hommage à <strong>Léo Lagrange</strong> (1900-1940), <strong>homme politique français</strong>, <strong>sous-secrétaire d'État aux Sports</strong> du Front populaire.",
            "<strong>Maisons-Alfort</strong> (~54 000 habitants), commune du <strong>Val-de-Marne</strong>. Quartier résidentiel et commerçant à proximité de la station."
        ],
        "faq": [
            ("Quelle ligne dessert Maisons-Alfort - Stade ?", "Uniquement la <strong>M8</strong>. Bus 24, 103, 107."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 avril 1972</strong>."),
            ("Pour le Stade Léo Lagrange ?", "<strong>~5 min à pied</strong>."),
            ("Pour Bastille ?", "<strong>M8 directe</strong> (~22 min)."),
            ("Pour Maisons-Alfort - Les Juilliottes ?", "<strong>M8 directe</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Stade Léo Lagrange</strong> à 5 min à pied.",
            "Quartier résidentiel de <strong>Maisons-Alfort</strong> (94).",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong>.",
            "Pour <strong>Créteil</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("🏟️", "Stade Léo Lagrange (Maisons-Alfort)", "Le <strong>Stade Léo Lagrange</strong>, à 5 min à pied, est un <strong>équipement sportif communal</strong> de <strong>Maisons-Alfort</strong>. Hommage à <strong>Léo Lagrange</strong> (<strong>1900-1940</strong>), <strong>sous-secrétaire d'État aux Sports et à l'organisation des Loisirs</strong> du <strong>Front populaire</strong> (1936-1937). <strong>Promoteur du sport populaire</strong> et du <strong>tourisme social</strong>. De nombreux <strong>équipements sportifs</strong> français portent son nom."),
            ("🏘️", "Maisons-Alfort, commune dynamique 94", "<strong>Maisons-Alfort</strong> (~54 000 habitants), commune du <strong>Val-de-Marne</strong>. <strong>Étymologie</strong> : <em>Maison</em> + <em>Alfort</em>, ancien lieu-dit. Connue pour l'<strong>École nationale vétérinaire d'Alfort</strong> (1766). Commune <strong>résidentielle et commerçante</strong>. <strong>Confluence de la Seine et de la Marne</strong> à proximité.")
        ],
        "itin": [
            ("Stade Léo Lagrange", "maisons-alfort-stade", "à pied", "5 min à pied", 5),
            ("École vétérinaire Alfort", "ecole-veterinaire-de-maisons-alfort", "M8", "M8 directe (1 station)", 2),
            ("Maisons-Alfort - Les Juilliottes", "maisons-alfort-les-juilliottes", "M8", "M8 directe (1 station)", 2),
            ("Créteil - Préfecture", "creteil-prefecture", "M8", "M8 directe (3 stations)", 8),
            ("Bastille", "bastille", "M8", "M8 directe (~22 min)", 22),
            ("Châtelet", "chatelet", "M8 + M1", "M8 → Bastille + M1", 26)
        ]
    },
    "maisons-alfort-les-juilliottes": {
        "addr": "Avenue du Général-Leclerc, 94700 Maisons-Alfort", "arr": "Maisons-Alfort (94)",
        "seo": "Station Maisons-Alfort - Les Juilliottes (M8) à Maisons-Alfort (94). Quartier Les Juilliottes résidentiel.",
        "tagline": "M8 — Maisons-Alfort, quartier Les Juilliottes",
        "hero_desc": "Station <strong>Maisons-Alfort - Les Juilliottes</strong> à <strong>Maisons-Alfort</strong> (Val-de-Marne, 94). Desservie par la <strong>M8</strong>, ouverte le <strong>27 avril 1972</strong>. Quartier <strong>Les Juilliottes</strong>, secteur résidentiel.",
        "intros": [
            "La station <strong>Maisons-Alfort - Les Juilliottes</strong> est implantée à <strong>Maisons-Alfort</strong> (Val-de-Marne, 94). Elle est desservie par la <strong>M8</strong>, entre <strong>Maisons-Alfort - Stade</strong> (1 station) et <strong>Créteil - L'Échat</strong> (1 station). Bus 107, 217.",
            "Ouverte le <strong>27 avril 1972</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Les Juilliottes</strong> rappelle l'<strong>ancien hameau</strong> et <strong>secteur résidentiel</strong> de Maisons-Alfort. Quartier résidentiel paisible."
        ],
        "hist_title": "1972 : prolongement et quartier Les Juilliottes",
        "hist": [
            "La station Maisons-Alfort - Les Juilliottes est <strong>inaugurée le 27 avril 1972</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>Les Juilliottes</strong> rappelle l'<strong>ancien hameau</strong> et secteur résidentiel de <strong>Maisons-Alfort</strong>. Quartier <strong>résidentiel paisible</strong>.",
            "<strong>Maisons-Alfort</strong> (~54 000 habitants), commune du <strong>Val-de-Marne</strong>. À courte distance : <strong>Créteil</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Maisons-Alfort - Les Juilliottes ?", "Uniquement la <strong>M8</strong>. Bus 107, 217."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 avril 1972</strong>."),
            ("Pour Créteil ?", "<strong>M8 directe</strong>."),
            ("Pour Bastille ?", "<strong>M8 directe</strong> (~24 min)."),
            ("Quartier ?", "<strong>Les Juilliottes</strong>, secteur résidentiel paisible."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "Quartier <strong>Les Juilliottes</strong> résidentiel paisible.",
            "Pour <strong>Créteil - Préfecture</strong> : <strong>M8 directe</strong>.",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong>.",
            "Pour <strong>École vétérinaire Alfort</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("🏘️", "Quartier Les Juilliottes", "Le <strong>quartier des Juilliottes</strong>, autour de la station, est un <strong>secteur résidentiel paisible</strong> de <strong>Maisons-Alfort</strong>. Nom rappelant l'<strong>ancien hameau</strong>. Quartier de <strong>petites maisons et immeubles modernes</strong>."),
            ("🚇", "Prolongement M8 vers Créteil (1972)", "Le <strong>prolongement de la M8 du 27 avril 1972</strong> de <strong>Charenton-Écoles à Maisons-Alfort - Les Juilliottes</strong> est l'un des <strong>premiers grands prolongements en banlieue</strong> du métro parisien. <strong>3 nouvelles stations</strong> ajoutées. Prolongé en <strong>1973</strong> à <strong>Créteil - L'Échat</strong>, puis en <strong>1974</strong> à <strong>Créteil - Université</strong> et en <strong>2011</strong> jusqu'à <strong>Créteil - Pointe du Lac</strong> (terminus actuel).")
        ],
        "itin": [
            ("Maisons-Alfort - Stade", "maisons-alfort-stade", "M8", "M8 directe (1 station)", 2),
            ("Créteil - L'Échat", "creteil-l-echat", "M8", "M8 directe (1 station)", 2),
            ("Créteil - Préfecture", "creteil-prefecture", "M8", "M8 directe (2 stations)", 5),
            ("École vétérinaire Alfort", "ecole-veterinaire-de-maisons-alfort", "M8", "M8 directe (2 stations)", 4),
            ("Bastille", "bastille", "M8", "M8 directe (~24 min)", 24),
            ("Châtelet", "chatelet", "M8 + M1", "M8 → Bastille + M1", 28)
        ]
    },
    "creteil-l-echat": {
        "addr": "Avenue du Général-de-Gaulle, 94010 Créteil", "arr": "Créteil (94)",
        "seo": "Station Créteil - L'Échat (M8) à Créteil (94). Hôpital Henri-Mondor (AP-HP) à proximité.",
        "tagline": "M8 — Créteil L'Échat, hôpital Henri-Mondor",
        "hero_desc": "Station <strong>Créteil - L'Échat</strong> à <strong>Créteil</strong> (Val-de-Marne, 94). Desservie par la <strong>M8</strong>, ouverte le <strong>27 avril 1973</strong>. À proximité de l'<strong>hôpital Henri-Mondor</strong>.",
        "intros": [
            "La station <strong>Créteil - L'Échat</strong> est implantée à <strong>Créteil</strong> (Val-de-Marne, 94). Elle est desservie par la <strong>M8</strong>, entre <strong>Maisons-Alfort - Les Juilliottes</strong> (1 station) et <strong>Créteil - Université</strong> (1 station). Bus 117, 217, 281, 393.",
            "Ouverte le <strong>27 avril 1973</strong> avec le <strong>prolongement de la M8</strong> de Maisons-Alfort - Les Juilliottes à Créteil - L'Échat.",
            "À proximité : l'<strong>hôpital Henri-Mondor</strong>, établissement de l'<strong>Assistance publique - Hôpitaux de Paris (AP-HP)</strong>. <strong>~1 000 lits</strong>, spécialisé en <strong>greffes et chirurgie cardio-thoracique</strong>."
        ],
        "hist_title": "1973 : Créteil L'Échat et hôpital",
        "hist": [
            "La station Créteil - L'Échat est <strong>inaugurée le 27 avril 1973</strong> avec le <strong>prolongement de la M8</strong>.",
            "Le nom <strong>L'Échat</strong> rappelle le <strong>quartier de l'Échat</strong> à Créteil. Étymologie incertaine.",
            "L'<strong>hôpital Henri-Mondor</strong>, à proximité, est inauguré en <strong>1969</strong>. <strong>Assistance publique - Hôpitaux de Paris (AP-HP)</strong>. <strong>~1 000 lits</strong>. Spécialisé en <strong>greffes</strong> (foie, rein, cœur), <strong>chirurgie cardio-thoracique</strong>, <strong>neurosciences</strong>. <strong>Université Paris-Est Créteil (UPEC)</strong>, <strong>Faculté de médecine</strong>. Hommage à <strong>Henri Mondor</strong> (1885-1962), <strong>chirurgien français</strong>, <strong>académicien</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Créteil - L'Échat ?", "Uniquement la <strong>M8</strong>. Bus 117, 217, 281, 393."),
            ("Quand a-t-elle ouvert ?", "Le <strong>27 avril 1973</strong>."),
            ("Pour l'hôpital Henri-Mondor ?", "<strong>~5 min à pied</strong>. AP-HP, ~1 000 lits."),
            ("Pour Créteil - Université ?", "<strong>M8 directe</strong> (1 station)."),
            ("Pour Bastille ?", "<strong>M8 directe</strong> (~26 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Hôpital Henri-Mondor</strong> (AP-HP) à 5 min à pied.",
            "<strong>Faculté de médecine UPEC</strong> à proximité.",
            "Pour <strong>Créteil - Université</strong> : <strong>M8 directe</strong>.",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("🏥", "Hôpital Henri-Mondor", "L'<strong>hôpital Henri-Mondor</strong>, à 5 min à pied, est inauguré en <strong>1969</strong>. <strong>Assistance publique - Hôpitaux de Paris (AP-HP)</strong>. <strong>~1 000 lits</strong>. Spécialisé en <strong>greffes</strong> (foie, rein, cœur), <strong>chirurgie cardio-thoracique</strong>, <strong>neurosciences</strong>. Hommage à <strong>Henri Mondor</strong> (1885-1962), <strong>chirurgien français</strong>, <strong>académicien</strong> (Académie française et Académie de médecine). <strong>Faculté de médecine UPEC</strong> à proximité."),
            ("🎓", "UPEC, université de Paris-Est Créteil", "L'<strong>Université Paris-Est Créteil (UPEC)</strong>, anciennement <strong>Paris XII</strong>, est l'<strong>une des plus jeunes universités françaises</strong>. <strong>Fondée en 1970</strong>. <strong>~30 000 étudiants</strong>. <strong>Plusieurs facultés</strong> : <strong>médecine, droit, économie, sciences humaines</strong>. <strong>Campus principal à Créteil</strong> (Mail des Mèches), <strong>autres sites</strong> à Vitry, Saint-Maur.")
        ],
        "itin": [
            ("Hôpital Henri-Mondor", "creteil-l-echat", "à pied", "5 min à pied", 5),
            ("Créteil - Université", "creteil-universite", "M8", "M8 directe (1 station)", 2),
            ("UPEC (Faculté médecine)", "creteil-universite", "M8 + à pied", "M8 + 5 min", 7),
            ("Créteil - Préfecture", "creteil-prefecture", "M8", "M8 directe (2 stations)", 5),
            ("Bastille", "bastille", "M8", "M8 directe (~26 min)", 26),
            ("Châtelet", "chatelet", "M8 + M1", "M8 → Bastille + M1", 30)
        ]
    },
    "creteil-universite": {
        "addr": "Avenue du Général-de-Gaulle, 94010 Créteil", "arr": "Créteil (94)",
        "seo": "Station Créteil - Université (M8) à Créteil (94). Université Paris-Est Créteil (UPEC) à proximité. Quartier universitaire.",
        "tagline": "M8 — Créteil, Université Paris-Est",
        "hero_desc": "Station <strong>Créteil - Université</strong> à <strong>Créteil</strong> (Val-de-Marne, 94). Desservie par la <strong>M8</strong>, ouverte le <strong>10 septembre 1974</strong>. À proximité de l'<strong>Université Paris-Est Créteil (UPEC)</strong>.",
        "intros": [
            "La station <strong>Créteil - Université</strong> est implantée à <strong>Créteil</strong> (Val-de-Marne, 94). Elle est desservie par la <strong>M8</strong>, entre <strong>Créteil - L'Échat</strong> (1 station) et <strong>Créteil - Préfecture</strong> (1 station). Bus 81, 117, 281.",
            "Ouverte le <strong>10 septembre 1974</strong> avec le <strong>prolongement de la M8</strong>.",
            "À proximité : l'<strong>Université Paris-Est Créteil (UPEC)</strong>, anciennement <strong>Paris XII</strong>. <strong>Fondée en 1970</strong>. <strong>~30 000 étudiants</strong>."
        ],
        "hist_title": "1974 : Université Paris-Est Créteil",
        "hist": [
            "La station Créteil - Université est <strong>inaugurée le 10 septembre 1974</strong> avec le <strong>prolongement de la M8</strong>.",
            "L'<strong>Université Paris-Est Créteil (UPEC)</strong>, à proximité, est <strong>fondée en 1970</strong> sous le nom <strong>Paris XII</strong>. <strong>~30 000 étudiants</strong>. <strong>Plusieurs facultés</strong> : <strong>médecine, droit, économie, sciences humaines, sciences et technologie</strong>.",
            "<strong>Créteil</strong> (~91 000 habitants), <strong>préfecture du Val-de-Marne</strong>. Ville en <strong>profonde transformation</strong> depuis les années 1960-1970, devenue <strong>centre administratif majeur</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Créteil - Université ?", "Uniquement la <strong>M8</strong>. Bus 81, 117, 281."),
            ("Quand a-t-elle ouvert ?", "Le <strong>10 septembre 1974</strong>."),
            ("Pour l'Université Paris-Est Créteil (UPEC) ?", "<strong>~5 min à pied</strong>. ~30 000 étudiants."),
            ("Pour Créteil - Préfecture ?", "<strong>M8 directe</strong> (1 station)."),
            ("Pour Bastille ?", "<strong>M8 directe</strong> (~28 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Université Paris-Est Créteil (UPEC)</strong> à 5 min à pied.",
            "<strong>~30 000 étudiants</strong>.",
            "Pour <strong>Créteil - Préfecture</strong> et <strong>Centre commercial Créteil-Soleil</strong> : <strong>M8 directe</strong>.",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("🎓", "UPEC (1970), une des plus jeunes universités", "L'<strong>Université Paris-Est Créteil (UPEC)</strong>, à 5 min à pied, est <strong>fondée en 1970</strong>. <strong>~30 000 étudiants</strong>. <strong>Plusieurs facultés</strong> : <strong>médecine, droit, économie, sciences humaines, sciences et technologie</strong>. Anciennement <strong>Paris XII</strong>. <strong>Campus principal</strong> (Mail des Mèches), <strong>autres sites</strong> à <strong>Vitry, Saint-Maur, Senart, Fontainebleau</strong>. <strong>UPEC fait partie de la ComUE Paris-Est Sup</strong>."),
            ("🏛️", "Créteil, préfecture du 94", "<strong>Créteil</strong> (~91 000 habitants), <strong>préfecture du Val-de-Marne</strong>. <strong>Étymologie</strong> : du latin <em>Cristolium</em>. Ville en <strong>profonde transformation</strong> depuis les années 1960-1970, devenue <strong>centre administratif majeur</strong>. <strong>Préfecture du Val-de-Marne</strong>, <strong>Hôtel de Ville</strong>, <strong>Centre commercial Créteil-Soleil</strong> (1974), <strong>Lac de Créteil</strong>.")
        ],
        "itin": [
            ("Université Paris-Est Créteil (UPEC)", "creteil-universite", "à pied", "5 min à pied", 5),
            ("Créteil - Préfecture", "creteil-prefecture", "M8", "M8 directe (1 station)", 2),
            ("Centre commercial Créteil-Soleil", "creteil-prefecture", "M8 + à pied", "M8 → Créteil Préfecture + à pied", 5),
            ("Créteil - L'Échat (hôpital)", "creteil-l-echat", "M8", "M8 directe (1 station)", 2),
            ("Bastille", "bastille", "M8", "M8 directe (~28 min)", 28),
            ("Châtelet", "chatelet", "M8 + M1", "M8 → Bastille + M1", 32)
        ]
    },
    "creteil-prefecture": {
        "addr": "Avenue du Général-de-Gaulle, 94000 Créteil", "arr": "Créteil (94)",
        "seo": "Station Créteil - Préfecture (M8) à Créteil (94). Préfecture du Val-de-Marne. Centre commercial Créteil-Soleil (1974).",
        "tagline": "M8 — Créteil, Préfecture du Val-de-Marne",
        "hero_desc": "Station <strong>Créteil - Préfecture</strong> à <strong>Créteil</strong> (Val-de-Marne, 94). Desservie par la <strong>M8</strong>, ouverte le <strong>10 septembre 1974</strong>. À la sortie : la <strong>Préfecture du Val-de-Marne</strong> et le <strong>Centre commercial Créteil-Soleil</strong>.",
        "intros": [
            "La station <strong>Créteil - Préfecture</strong> est implantée à <strong>Créteil</strong> (Val-de-Marne, 94). Elle est desservie par la <strong>M8</strong>, entre <strong>Créteil - Université</strong> (1 station) et <strong>Créteil - Pointe du Lac</strong> (1 station, terminus). Bus 81, 117, 217, 281, 308.",
            "Ouverte le <strong>10 septembre 1974</strong> avec le <strong>prolongement de la M8</strong>.",
            "À la sortie : la <strong>Préfecture du Val-de-Marne</strong> (Hôtel du département, 1974) et le <strong>Centre commercial Créteil-Soleil</strong> (1974, <strong>~200 boutiques</strong>)."
        ],
        "hist_title": "1974 : Préfecture du 94 et Créteil-Soleil",
        "hist": [
            "La station Créteil - Préfecture est <strong>inaugurée le 10 septembre 1974</strong> avec le <strong>prolongement de la M8</strong>.",
            "La <strong>Préfecture du Val-de-Marne</strong>, à la sortie, est inaugurée en <strong>1974</strong> dans le cadre de la <strong>création du département du Val-de-Marne</strong> (loi du 10 juillet 1964, mise en application en 1968). <strong>Architecte Daniel Badani</strong>. <strong>Style moderniste</strong>.",
            "Le <strong>Centre commercial Créteil-Soleil</strong>, à la sortie, est inauguré en <strong>1974</strong>. <strong>~200 boutiques</strong>, <strong>~15 millions de visiteurs/an</strong>. <strong>Plus grand centre commercial du Val-de-Marne</strong>. <strong>Rénové en 2015</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Créteil - Préfecture ?", "Uniquement la <strong>M8</strong>. Bus 81, 117, 217, 281, 308."),
            ("Quand a-t-elle ouvert ?", "Le <strong>10 septembre 1974</strong>."),
            ("Pour la Préfecture du Val-de-Marne ?", "<strong>Sortie directe</strong>."),
            ("Pour le Centre commercial Créteil-Soleil ?", "<strong>Sortie directe</strong>. ~200 boutiques."),
            ("Pour le terminus Créteil - Pointe du Lac ?", "<strong>M8 directe</strong> (1 station, terminus)."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>.")
        ],
        "tips": [
            "<strong>Préfecture du Val-de-Marne</strong> à la sortie.",
            "<strong>Centre commercial Créteil-Soleil</strong> à la sortie : ~200 boutiques.",
            "Pour <strong>Créteil - Pointe du Lac</strong> (terminus) : <strong>M8 directe</strong>.",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("🏛️", "Préfecture du Val-de-Marne (1974)", "La <strong>Préfecture du Val-de-Marne</strong>, à la sortie, est inaugurée en <strong>1974</strong> dans le cadre de la <strong>création du département du Val-de-Marne</strong> (loi du 10 juillet 1964, mise en application en 1968). <strong>Architecte Daniel Badani</strong>. <strong>Style moderniste</strong>. Centre administratif majeur. Le <strong>Val-de-Marne</strong> (~1,4 million d'habitants) est l'un des <strong>3 départements de la petite couronne</strong>."),
            ("🛍️", "Créteil-Soleil (1974), centre commercial majeur", "Le <strong>Centre commercial Créteil-Soleil</strong>, à la sortie, est inauguré en <strong>1974</strong>. <strong>~200 boutiques</strong>, <strong>~15 millions de visiteurs/an</strong>. <strong>Plus grand centre commercial du Val-de-Marne</strong>. <strong>Forme circulaire</strong> caractéristique. <strong>Rénové et agrandi en 2015</strong>. <strong>Cinéma multiplexe</strong>, restaurants, hypermarché Carrefour.")
        ],
        "itin": [
            ("Préfecture du Val-de-Marne", "creteil-prefecture", "à pied", "Sortie directe", 1),
            ("Centre commercial Créteil-Soleil", "creteil-prefecture", "à pied", "Sortie directe", 2),
            ("Créteil - Pointe du Lac (terminus)", "creteil-pointe-du-lac", "M8", "M8 directe (1 station)", 2),
            ("Créteil - Université (UPEC)", "creteil-universite", "M8", "M8 directe (1 station)", 2),
            ("Bastille", "bastille", "M8", "M8 directe (~30 min)", 30),
            ("Châtelet", "chatelet", "M8 + M1", "M8 → Bastille + M1", 34)
        ]
    },
    "creteil-pointe-du-lac": {
        "addr": "Avenue Pasteur-Vallery-Radot, 94000 Créteil", "arr": "Créteil (94)",
        "seo": "Station Créteil - Pointe du Lac, terminus sud-est M8 à Créteil (94). Ouverte en 2011 avec l'extension. Lac de Créteil à proximité.",
        "tagline": "M8 — terminus sud-est, Lac de Créteil (2011)",
        "hero_desc": "Station <strong>Créteil - Pointe du Lac</strong>, <strong>terminus sud-est de la M8</strong>, à <strong>Créteil</strong> (Val-de-Marne, 94). Ouverte le <strong>8 octobre 2011</strong>. À proximité du <strong>Lac de Créteil</strong>.",
        "intros": [
            "La station <strong>Créteil - Pointe du Lac</strong> est le <strong>terminus sud-est de la M8</strong>, à <strong>Créteil</strong> (Val-de-Marne, 94). Bus 117, 217, 281, 308, 393.",
            "Ouverte le <strong>8 octobre 2011</strong> avec le <strong>prolongement de la M8</strong> de Créteil - Préfecture à Créteil - Pointe du Lac.",
            "À proximité : le <strong>Lac de Créteil</strong>, <strong>plan d'eau artificiel de 40 hectares</strong> au cœur de la ville. <strong>Base nautique</strong>, <strong>promenades</strong>, <strong>activités sportives</strong>."
        ],
        "hist_title": "2011 : extension sud-est et Lac de Créteil",
        "hist": [
            "La station Créteil - Pointe du Lac est <strong>inaugurée le 8 octobre 2011</strong> comme <strong>terminus sud-est de la M8</strong>, avec le <strong>prolongement de la M8</strong> de Créteil - Préfecture.",
            "Le <strong>Lac de Créteil</strong>, à proximité, est un <strong>plan d'eau artificiel</strong> de <strong>40 hectares</strong> créé dans les années 1970 dans le cadre de l'<strong>urbanisme nouveau de Créteil</strong>. <strong>Base nautique</strong>, <strong>promenades</strong>, <strong>activités sportives</strong> (aviron, kayak, voile).",
            "<strong>Créteil</strong> (~91 000 habitants), <strong>préfecture du Val-de-Marne</strong>, est en pleine <strong>extension urbaine</strong>. Quartier <strong>Pointe du Lac</strong> en développement avec de <strong>nouveaux logements et bureaux</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Créteil - Pointe du Lac ?", "Uniquement la <strong>M8</strong> (terminus). Bus 117, 217, 281, 308, 393."),
            ("Quand a-t-elle ouvert ?", "Le <strong>8 octobre 2011</strong>."),
            ("Pour le Lac de Créteil ?", "<strong>~10 min à pied</strong>."),
            ("Pour Créteil - Préfecture ?", "<strong>M8 directe</strong> (1 station)."),
            ("Pour Bastille ?", "<strong>M8 directe</strong> (~32 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Oui</strong>. Station moderne (2011).")
        ],
        "tips": [
            "<strong>Lac de Créteil</strong> à 10 min à pied : 40 hectares, base nautique.",
            "<strong>Promenades et activités sportives</strong> au Lac.",
            "Pour <strong>Centre commercial Créteil-Soleil</strong> : <strong>M8 → Préfecture</strong>.",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong>.",
            "Zone tarifaire <strong>3</strong>, Val-de-Marne."
        ],
        "trivia": [
            ("🚇", "Extension 2011, terminus sud-est M8", "L'<strong>extension de 2011</strong>, qui ouvre cette station, prolonge la <strong>M8</strong> de <strong>Créteil - Préfecture à Créteil - Pointe du Lac</strong>. <strong>1 nouvelle station</strong> ajoutée. <strong>1 km de prolongement</strong>. Permet le <strong>désenclavement du quartier de la Pointe du Lac</strong>, secteur résidentiel en développement."),
            ("🏊", "Lac de Créteil, 40 hectares", "Le <strong>Lac de Créteil</strong>, à 10 min à pied, est un <strong>plan d'eau artificiel</strong> de <strong>40 hectares</strong> créé dans les années 1970 dans le cadre de l'<strong>urbanisme nouveau de Créteil</strong>. <strong>Base nautique</strong>, <strong>promenades</strong>, <strong>activités sportives</strong> (aviron, kayak, voile, pédalo). <strong>Faune et flore variées</strong>. <strong>Plage</strong> en été. <strong>Cœur vert de Créteil</strong>.")
        ],
        "itin": [
            ("Lac de Créteil", "creteil-pointe-du-lac", "à pied", "10 min à pied", 10),
            ("Créteil - Préfecture", "creteil-prefecture", "M8", "M8 directe (1 station)", 2),
            ("Centre commercial Créteil-Soleil", "creteil-prefecture", "M8 + à pied", "M8 + 2 min", 5),
            ("Créteil - Université (UPEC)", "creteil-universite", "M8", "M8 directe (2 stations)", 5),
            ("Bastille", "bastille", "M8", "M8 directe (~32 min)", 32),
            ("Châtelet", "chatelet", "M8 + M1", "M8 → Bastille + M1", 36)
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
        if "Charenton" in c["arr"]:
            zone = 2
        else:
            zone = 3
        d["tariff_zone"] = zone
        d["tariff_zone_context"] = f"Val-de-Marne (94), zone tarifaire {zone}"
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
