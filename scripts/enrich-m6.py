#!/usr/bin/env python3
"""Enrichit M6 18 stations avec contenu T0 Wikipedia FR."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    "kleber": {
        "addr": "Avenue Kléber, 75116 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Kléber (M6) avenue Kléber dans le 16e arrondissement. Nommée d'après le général Jean-Baptiste Kléber (1753-1800). Proche Arc de Triomphe.",
        "tagline": "M6 — avenue Kléber, général Jean-Baptiste Kléber",
        "hero_desc": "Station <strong>Kléber</strong> sur l'<strong>avenue Kléber</strong> dans le <strong>16e arrondissement</strong>, desservie par la <strong>ligne 6 du métro</strong>. Ouverte le <strong>2 octobre 1900</strong> avec le premier tronçon de la ligne (Étoile ↔ Trocadéro lors de l'Exposition universelle). Nommée d'après le <strong>général Jean-Baptiste Kléber</strong> (1753-1800), général de la Révolution française assassiné au Caire en 1800.",
        "intros": [
            "La station <strong>Kléber</strong> est implantée sur l'<strong>avenue Kléber</strong> dans le <strong>16e arrondissement</strong> de Paris. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Charles de Gaulle - Étoile</strong> (1 station) et <strong>Boissière</strong> (1 station). Bus 30 et 92 en correspondance.",
            "Ouverte le <strong>2 octobre 1900</strong>, elle fait partie du premier tronçon Étoile ↔ Trocadéro de la ligne 6, mis en service à l'occasion de l'<strong>Exposition universelle de 1900</strong>.",
            "Le nom <strong>Kléber</strong> rend hommage à <strong>Jean-Baptiste Kléber</strong> (1753-1800), général en chef de l'armée d'Orient après le départ de Bonaparte, <strong>assassiné au Caire le 14 juin 1800</strong>. L'avenue Kléber mène directement à la <strong>place Charles-de-Gaulle (Étoile)</strong> et à l'<strong>Arc de Triomphe</strong>."
        ],
        "hist_title": "1900 : Exposition universelle et général Kléber",
        "hist": [
            "La station Kléber est <strong>inaugurée le 2 octobre 1900</strong> avec le premier tronçon de la <strong>ligne 6 entre Étoile et Trocadéro</strong>, pour desservir les abords de l'<strong>Exposition universelle de 1900</strong>.",
            "Le nom <strong>Kléber</strong> commémore <strong>Jean-Baptiste Kléber</strong> (<strong>1753-1800</strong>), <strong>général français de la Révolution</strong>, né à Strasbourg. Il participe à la <strong>campagne d'Égypte</strong> (1798) avec Bonaparte, puis devient <strong>général en chef de l'armée d'Orient</strong> après le départ de Bonaparte (août 1799). Il remporte la <strong>bataille d'Héliopolis</strong> (mars 1800) mais est <strong>assassiné au Caire le 14 juin 1800</strong> par Soleyman El-Halebi.",
            "L'<strong>avenue Kléber</strong> (1,3 km) relie la <strong>place Charles-de-Gaulle (Étoile)</strong> à la <strong>place du Trocadéro</strong>, ouvrant un axe royal entre Arc de Triomphe et Palais de Chaillot. Elle accueille de nombreux hôtels de luxe, dont l'<strong>hôtel Raphaël</strong> et le <strong>Peninsula Paris</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Kléber ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 30 et 92."),
            ("Quand la station a-t-elle ouvert ?", "Le <strong>2 octobre 1900</strong>, avec le premier tronçon de la ligne 6 (Étoile ↔ Trocadéro), construit pour l'<strong>Exposition universelle de 1900</strong>."),
            ("Qui est Kléber ?", "<strong>Jean-Baptiste Kléber</strong> (1753-1800), général français de la Révolution, commandant en chef de l'armée d'Orient après le départ de Bonaparte d'Égypte. <strong>Assassiné au Caire en 1800</strong>."),
            ("Comment aller à l'Arc de Triomphe ?", "Remonter l'<strong>avenue Kléber</strong> à pied (~10 min), ou prendre la <strong>M6 jusqu'à Charles de Gaulle - Étoile</strong> (1 station)."),
            ("Comment aller au Trocadéro ?", "<strong>M6 directe</strong> : Boissière puis Trocadéro (2 stations, ~4 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station ancienne (1900), pas d'ascenseur. Accès uniquement par escaliers.")
        ],
        "tips": [
            "Pour l'<strong>Arc de Triomphe</strong> : <strong>M6 vers Charles de Gaulle - Étoile</strong> (1 station) ou à pied (~10 min via avenue Kléber).",
            "Pour le <strong>Trocadéro</strong> et la <strong>Tour Eiffel</strong> : <strong>M6 directe</strong> (~5 min).",
            "Quartier hôtels de luxe : <strong>Peninsula Paris</strong>, <strong>Hôtel Raphaël</strong>, <strong>Hôtel Majestic</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros.",
            "Sortie avenue Kléber : nombreuses ambassades et bureaux de prestige."
        ],
        "trivia": [
            ("⚔️", "Général Kléber (1753-1800), assassiné au Caire", "<strong>Jean-Baptiste Kléber</strong>, né le <strong>9 mars 1753 à Strasbourg</strong>, devient général de la Révolution française. Participe à la <strong>campagne d'Égypte</strong> (1798) sous Bonaparte. Devient <strong>commandant en chef de l'armée d'Orient</strong> après le départ de Bonaparte. Remporte la <strong>bataille d'Héliopolis</strong> (20 mars 1800). <strong>Assassiné le 14 juin 1800 au Caire</strong> par un étudiant syrien, Soleyman El-Halebi. Son corps est rapatrié et inhumé à Strasbourg."),
            ("🏨", "Avenue des palaces parisiens", "L'avenue Kléber accueille plusieurs <strong>palaces parisiens</strong> : le <strong>Peninsula Paris</strong> (ancien hôtel Majestic, où fut paraphé en 1973 l'accord de paix mettant fin à la guerre du Vietnam), l'<strong>hôtel Raphaël</strong>, le <strong>Sofitel Paris Le Faubourg</strong>. Elle héberge également plusieurs <strong>ambassades</strong>.")
        ],
        "itin": [
            ("Arc de Triomphe", "arc-de-triomphe", "M6", "M6 vers Charles de Gaulle - Étoile", 4),
            ("Trocadéro et Tour Eiffel", "trocadero", "M6", "M6 vers Trocadéro (2 stations)", 5),
            ("Champs-Élysées", "george-v", "M6 + M1", "M6 → Étoile + M1 direction Vincennes", 8),
            ("Opéra Garnier", "opera", "M6 + M3", "M6 → Étoile + M3", 18),
            ("La Défense", "la-defense", "M6 + M1", "M6 → Étoile + M1 direction La Défense", 12),
            ("Châtelet", "chatelet", "M6 + M1", "M6 → Étoile + M1 direction Vincennes", 22)
        ]
    },
    "boissiere": {
        "addr": "Avenue Kléber, 75116 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Boissière (M6) avenue Kléber dans le 16e arrondissement. Nommée d'après la rue Boissière. Proche Palais de Tokyo et musée Guimet.",
        "tagline": "M6 — entre Kléber et Trocadéro, 16e arrondissement",
        "hero_desc": "Station <strong>Boissière</strong> sur l'<strong>avenue Kléber</strong> dans le <strong>16e arrondissement</strong>, desservie par la <strong>ligne 6 du métro</strong>. Ouverte le <strong>2 octobre 1900</strong> avec le premier tronçon Étoile ↔ Trocadéro de la ligne. Nommée d'après la <strong>rue Boissière</strong> toute proche. À courte distance du <strong>musée Guimet</strong> et du <strong>Palais de Tokyo</strong>.",
        "intros": [
            "La station <strong>Boissière</strong> est implantée sur l'<strong>avenue Kléber</strong> dans le <strong>16e arrondissement</strong>, à proximité de la <strong>rue Boissière</strong> qui lui donne son nom. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Kléber</strong> (1 station) et <strong>Trocadéro</strong> (1 station). Bus 30 et 32 en correspondance.",
            "Ouverte le <strong>2 octobre 1900</strong>, elle fait partie du premier tronçon Étoile ↔ Trocadéro de la ligne 6, mis en service pour l'<strong>Exposition universelle de 1900</strong>.",
            "Le quartier est marqué par les <strong>musées des arts asiatiques</strong> : le <strong>musée Guimet</strong> à proximité (place d'Iéna, 10 min à pied), et le <strong>Palais de Tokyo</strong> (avenue du Président-Wilson). Quartier résidentiel haussmannien chic du <strong>16e</strong>."
        ],
        "hist_title": "1900 : Exposition universelle et avenue Kléber",
        "hist": [
            "La station Boissière est <strong>inaugurée le 2 octobre 1900</strong> avec le premier tronçon Étoile ↔ Trocadéro de la <strong>ligne 6</strong>, en service pour l'<strong>Exposition universelle de 1900</strong>.",
            "Son nom vient de la <strong>rue Boissière</strong> proche, dont l'étymologie évoque les bois (forêts) qui couvraient autrefois le secteur avant son urbanisation au XIXe siècle. Le percement de l'<strong>avenue Kléber</strong> sous Napoléon III a redessiné le quartier en axe haussmannien.",
            "Le quartier accueille plusieurs <strong>musées d'art majeurs</strong> : <strong>musée Guimet</strong> (national des arts asiatiques), <strong>Palais de Tokyo</strong> (art contemporain), <strong>musée d'Art moderne de la Ville de Paris</strong>. Il regroupe également de nombreuses <strong>ambassades</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Boissière ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 30 et 32."),
            ("Quand la station a-t-elle ouvert ?", "Le <strong>2 octobre 1900</strong>, avec le premier tronçon de la ligne 6 (Étoile ↔ Trocadéro) construit pour l'<strong>Exposition universelle de 1900</strong>."),
            ("D'où vient le nom Boissière ?", "De la <strong>rue Boissière</strong> proche. Étymologie évoquant les bois qui couvraient le secteur avant urbanisation."),
            ("Comment aller au musée Guimet ?", "Descendre la rue Boissière vers la <strong>place d'Iéna</strong> (~10 min à pied)."),
            ("Comment aller au Palais de Tokyo ?", "À pied via l'avenue du Président-Wilson (~12 min), ou <strong>M6 jusqu'à Trocadéro</strong> puis descendre."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station ancienne (1900), pas d'ascenseur.")
        ],
        "tips": [
            "Pour le <strong>musée Guimet</strong> : descendre la rue Boissière vers la place d'Iéna (~10 min).",
            "Pour le <strong>Palais de Tokyo</strong> et le <strong>musée d'Art moderne</strong> : ~12 min à pied via avenue du Président-Wilson.",
            "Quartier résidentiel haussmannien chic du 16e arrondissement.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros.",
            "Pour la <strong>Tour Eiffel</strong> : <strong>M6 directe</strong> vers Trocadéro (1 station, vue panoramique recommandée)."
        ],
        "trivia": [
            ("🏛️", "Musée Guimet, arts asiatiques", "Le <strong>musée national des arts asiatiques - Guimet</strong> est l'un des plus importants musées d'arts asiatiques d'Europe. Fondé en <strong>1879 à Lyon par Émile Guimet</strong>, il s'installe à Paris en <strong>1889 place d'Iéna</strong>. Plus de <strong>60 000 œuvres</strong> couvrant l'<strong>Inde, Asie du Sud-Est, Chine, Japon, Corée, Tibet</strong>. À 10 min à pied de la station Boissière."),
            ("🎨", "Palais de Tokyo et art contemporain", "Le <strong>Palais de Tokyo</strong>, construit pour l'<strong>Exposition internationale de 1937</strong>, abrite aujourd'hui un <strong>centre d'art contemporain majeur</strong> (l'aile ouest) et le <strong>musée d'Art moderne de la Ville de Paris</strong> (l'aile est). Programmation expérimentale.")
        ],
        "itin": [
            ("Musée Guimet", "iena", "M6", "M6 ou ~10 min à pied via rue Boissière", 10),
            ("Trocadéro et Tour Eiffel", "trocadero", "M6", "M6 direct (1 station)", 3),
            ("Arc de Triomphe", "charles-de-gaulle-etoile", "M6", "M6 vers Étoile (2 stations)", 5),
            ("Palais de Tokyo et MAM", "alma-marceau", "M6 + M9", "À pied via avenue Président-Wilson", 12),
            ("Champs-Élysées", "george-v", "M6 + M1", "M6 → Étoile + M1", 10),
            ("Opéra Garnier", "opera", "M6 + M3", "M6 → Étoile + M3", 20)
        ]
    },
    "passy": {
        "addr": "Place de Costa Rica, 75116 Paris", "arr": "16e arrondissement (Paris)",
        "seo": "Station Passy (M6) place de Costa Rica dans le 16e arrondissement. Station aérienne offrant une vue sur la Tour Eiffel. Proche maison de Balzac.",
        "tagline": "M6 — aérienne, vue Tour Eiffel, quartier Passy",
        "hero_desc": "Station <strong>Passy</strong>, <strong>aérienne</strong>, place de Costa Rica dans le <strong>16e arrondissement</strong>. Desservie par la <strong>ligne 6 du métro</strong>, ouverte le <strong>24 avril 1903</strong>. <strong>Vue panoramique sur la Tour Eiffel</strong> et la Seine depuis le quai aérien. Cœur du <strong>quartier de Passy</strong> résidentiel chic. Proche de la <strong>maison de Balzac</strong> (musée).",
        "intros": [
            "La station <strong>Passy</strong> est implantée <strong>place de Costa Rica</strong> dans le <strong>16e arrondissement</strong>, au cœur du <strong>quartier historique de Passy</strong>. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Trocadéro</strong> (1 station) et <strong>Bir-Hakeim</strong> (1 station). Bus 32, 70 et 72 en correspondance.",
            "Station <strong>aérienne</strong> située sur le <strong>viaduc de Passy</strong>, elle offre depuis ses quais une <strong>vue panoramique sur la Tour Eiffel</strong> et la <strong>Seine</strong>. Ouverte le <strong>24 avril 1903</strong> avec le prolongement de la ligne 6 (anciennement ligne 2 Sud) jusqu'à Place d'Italie.",
            "Le <strong>quartier de Passy</strong>, ancien village rattaché à Paris en <strong>1860</strong>, est aujourd'hui un quartier résidentiel chic du <strong>16e arrondissement</strong>. Il abrite la <strong>maison de Balzac</strong> (musée littéraire où vécut Honoré de Balzac de 1840 à 1847) et le <strong>cimetière de Passy</strong>."
        ],
        "hist_title": "1903 : Passy, ancien village résidentiel chic",
        "hist": [
            "La station Passy est <strong>inaugurée le 24 avril 1903</strong> avec la mise en service du tronçon <strong>Trocadéro ↔ Place d'Italie</strong> de l'ancienne ligne 2 Sud (devenue ligne 6 en 1907 puis 1942). Elle dessert l'ancien <strong>village de Passy</strong>, rattaché à Paris en <strong>1860</strong> avec d'autres communes périphériques.",
            "<strong>Passy</strong> était au XIXe siècle un village paisible de la périphérie parisienne, connu pour ses <strong>sources d'eaux ferrugineuses</strong>. Il accueillit de nombreuses personnalités : <strong>Honoré de Balzac</strong> y vécut <strong>de 1840 à 1847</strong> dans un pavillon (aujourd'hui musée maison de Balzac), <strong>Marie Curie</strong>, <strong>Marcel Proust</strong>, <strong>Claude Debussy</strong>.",
            "La station bénéficie d'une <strong>position aérienne unique</strong> : depuis ses quais sur le viaduc de Passy, on aperçoit la <strong>Tour Eiffel</strong> et la <strong>Seine</strong>. Le quartier conserve une atmosphère résidentielle chic, avec ses villas, ses jardins privés et le <strong>cimetière de Passy</strong> (où reposent Manet, Debussy, Berthe Morisot)."
        ],
        "faq": [
            ("Quelle ligne dessert Passy ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 32, 70 et 72."),
            ("Passy est-elle une station aérienne ?", "<strong>Oui</strong>. Elle se situe sur le <strong>viaduc de Passy</strong>, offrant une <strong>vue panoramique sur la Tour Eiffel</strong> et la Seine."),
            ("Quand a-t-elle ouvert ?", "Le <strong>24 avril 1903</strong>, avec le prolongement Trocadéro ↔ Place d'Italie (ancienne ligne 2 Sud, devenue ligne 6)."),
            ("Comment aller à la maison de Balzac ?", "<strong>~7 min à pied</strong> via la rue Raynouard. Musée littéraire, anciennement domicile de <strong>Balzac (1840-1847)</strong>."),
            ("Comment aller à la Tour Eiffel ?", "<strong>M6 directe</strong> jusqu'à Bir-Hakeim ou Trocadéro (~5 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station ancienne aérienne (1903), pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Vue iconique sur la Tour Eiffel</strong> depuis le quai aérien — l'une des plus belles vues du métro parisien.",
            "<strong>Maison de Balzac</strong> à 7 min à pied via rue Raynouard. Musée littéraire gratuit (collections permanentes).",
            "Quartier <strong>Passy</strong> résidentiel chic du 16e, atmosphère de village.",
            "<strong>Cimetière de Passy</strong> : tombeaux de Manet, Debussy, Berthe Morisot.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏠", "Maison de Balzac, où vécut l'écrivain", "La <strong>maison de Balzac</strong>, rue Raynouard, est l'<strong>unique demeure parisienne préservée</strong> d'Honoré de Balzac. L'écrivain y résida de <strong>1840 à 1847</strong> sous un faux nom (Monsieur de Brugnol) pour échapper à ses créanciers. Il y rédigea ou corrigea <em>La Cousine Bette</em>, <em>Le Cousin Pons</em>, <em>Splendeurs et misères des courtisanes</em>. Musée littéraire municipal depuis 1949."),
            ("🎵", "Passy, refuge des artistes et compositeurs", "Le quartier de Passy attira de nombreux artistes : <strong>Claude Debussy</strong> y composa <em>La Mer</em> et <em>Pelléas et Mélisande</em>, <strong>Marcel Proust</strong> y résida un temps, <strong>Marie Curie</strong> y vécut. Le <strong>cimetière de Passy</strong> abrite les tombes d'Édouard Manet, Berthe Morisot, Claude Debussy.")
        ],
        "itin": [
            ("Tour Eiffel via Bir-Hakeim", "bir-hakeim", "M6", "M6 directe (1 station)", 4),
            ("Trocadéro", "trocadero", "M6", "M6 directe (1 station)", 3),
            ("Maison de Balzac", "passy", "à pied", "Rue Raynouard (7 min)", 7),
            ("Arc de Triomphe", "charles-de-gaulle-etoile", "M6", "M6 vers Étoile (4 stations)", 10),
            ("Champs-Élysées", "george-v", "M6 + M1", "M6 → Étoile + M1", 14),
            ("Concorde", "concorde", "M6 + M1", "M6 → Étoile + M1 ou M8", 18)
        ]
    },
    "dupleix": {
        "addr": "Boulevard de Grenelle, 75015 Paris", "arr": "15e arrondissement (Paris)",
        "seo": "Station Dupleix (M6) aérienne boulevard de Grenelle dans le 15e arrondissement. Nommée d'après le marquis Joseph-François Dupleix (1697-1763), gouverneur de l'Inde française.",
        "tagline": "M6 — aérienne, Joseph-François Dupleix (Inde française)",
        "hero_desc": "Station <strong>Dupleix</strong>, <strong>aérienne</strong>, sur le <strong>boulevard de Grenelle</strong> dans le <strong>15e arrondissement</strong>. Desservie par la <strong>ligne 6 du métro</strong>, ouverte le <strong>24 avril 1906</strong>. Nommée d'après <strong>Joseph-François Dupleix</strong> (<strong>1697-1763</strong>), <strong>gouverneur général de l'Inde française</strong>. Quartier résidentiel du <strong>15e</strong>, proche de la <strong>Tour Eiffel</strong>.",
        "intros": [
            "La station <strong>Dupleix</strong> est implantée <strong>boulevard de Grenelle</strong> dans le <strong>15e arrondissement</strong>. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Bir-Hakeim</strong> (1 station) et <strong>La Motte-Picquet - Grenelle</strong> (1 station). Bus 80 et 82 en correspondance.",
            "Station <strong>aérienne</strong> située sur le viaduc de la ligne 6, elle offre des vues sur les quartiers de <strong>Grenelle</strong>. Ouverte le <strong>24 avril 1906</strong> avec le tronçon Place d'Italie ↔ Étoile (ancienne ligne 2 Sud devenue ligne 6).",
            "Le nom <strong>Dupleix</strong> rend hommage à <strong>Joseph-François Dupleix</strong> (1697-1763), <strong>gouverneur général des établissements français en Inde</strong> de 1742 à 1754. Il chercha à fonder un <strong>empire colonial français en Inde</strong> mais fut désavoué par la métropole. La <strong>place Dupleix</strong> et le <strong>marché Dupleix</strong> sont proches."
        ],
        "hist_title": "1906 : Grenelle aérien, et Dupleix gouverneur de l'Inde",
        "hist": [
            "La station Dupleix est <strong>inaugurée le 24 avril 1906</strong> avec la mise en service du tronçon <strong>Place d'Italie ↔ Étoile</strong> (ancienne ligne 2 Sud, devenue ligne 6 en 1907 puis 1942).",
            "Le nom <strong>Dupleix</strong> commémore <strong>Joseph-François Dupleix</strong> (<strong>1er janvier 1697 - 10 novembre 1763</strong>), <strong>administrateur colonial français</strong>. Devient <strong>gouverneur de Chandernagor</strong> en 1731, puis <strong>gouverneur général des établissements français en Inde</strong> de 1742 à 1754. Il tente d'établir un <strong>empire colonial français en Inde</strong>, s'oppose aux Britanniques mais est <strong>rappelé en France en 1754</strong>. Il meurt ruiné à Paris en 1763.",
            "Le quartier de <strong>Grenelle</strong>, ancien village rattaché à Paris en <strong>1860</strong>, est aujourd'hui un quartier résidentiel du <strong>15e arrondissement</strong>. La <strong>place Dupleix</strong> (square Dupleix) et le <strong>marché Dupleix</strong> (mercredi et dimanche) sont à proximité. À courte distance de la <strong>Tour Eiffel</strong> via le pont de Bir-Hakeim."
        ],
        "faq": [
            ("Quelle ligne dessert Dupleix ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 80 et 82."),
            ("Dupleix est-elle aérienne ?", "<strong>Oui</strong>. Station aérienne sur le viaduc de la ligne 6, boulevard de Grenelle."),
            ("Qui est Joseph-François Dupleix ?", "<strong>Joseph-François Dupleix</strong> (1697-1763), <strong>gouverneur général des établissements français en Inde</strong> de 1742 à 1754. Tenta d'établir un empire colonial français en Inde."),
            ("Quand a-t-elle ouvert ?", "Le <strong>24 avril 1906</strong>, avec le tronçon Place d'Italie ↔ Étoile."),
            ("Comment aller à la Tour Eiffel ?", "<strong>M6 jusqu'à Bir-Hakeim</strong> (1 station), puis traversée du pont de Bir-Hakeim (~10 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station aérienne ancienne (1906), pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Marché Dupleix</strong> sur le boulevard de Grenelle (mercredi et dimanche matin).",
            "Pour la <strong>Tour Eiffel</strong> : <strong>M6 jusqu'à Bir-Hakeim</strong> (1 station) puis pont (~10 min).",
            "Quartier résidentiel <strong>Grenelle</strong>, atmosphère paisible du 15e.",
            "<strong>Square Dupleix</strong> : espace vert agréable, place de la mairie du 15e.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🇮🇳", "Dupleix, gouverneur de l'Inde française", "<strong>Joseph-François Dupleix</strong> (1697-1763), né à Landrecies, devient à 24 ans <strong>conseiller au Conseil supérieur de Pondichéry</strong>. Nommé <strong>gouverneur de Chandernagor</strong> en 1731, puis <strong>gouverneur général de l'Inde française</strong> de 1742 à 1754. Tente d'établir un <strong>empire colonial français</strong> en Inde, s'allie au Carnatic, affronte les Britanniques (guerres Carnatiques). <strong>Rappelé en France en 1754</strong>, désavoué par la Compagnie des Indes, il meurt ruiné en 1763."),
            ("🏛️", "Quartier Grenelle, ancien village", "<strong>Grenelle</strong>, ancien village rattaché à Paris en <strong>1860</strong>, est aujourd'hui un quartier résidentiel du <strong>15e arrondissement</strong>. Il abrite la <strong>mairie du 15e</strong> (place Dupleix), le <strong>marché Dupleix</strong>, l'<strong>UNESCO</strong> (avenue de Suffren) et débouche sur le <strong>Champ-de-Mars</strong> et la <strong>Tour Eiffel</strong>.")
        ],
        "itin": [
            ("Tour Eiffel via Bir-Hakeim", "bir-hakeim", "M6", "M6 directe (1 station) puis pont", 12),
            ("Champ-de-Mars - Tour Eiffel", "champ-de-mars-tour-eiffel", "M6 + RER C", "M6 → Bir-Hakeim + RER C", 15),
            ("La Motte-Picquet - Grenelle", "la-motte-picquet-grenelle", "M6", "M6 directe (1 station)", 3),
            ("Trocadéro", "trocadero", "M6", "M6 directe (3 stations)", 7),
            ("Concorde", "concorde", "M6 + M8", "M6 → La Motte-Picquet + M8", 18),
            ("Châtelet", "chatelet", "M6 + M1", "M6 → Étoile + M1", 25)
        ]
    },
    "cambronne": {
        "addr": "Place Cambronne, 75015 Paris", "arr": "15e arrondissement (Paris)",
        "seo": "Station Cambronne (M6) aérienne place Cambronne dans le 15e arrondissement. Nommée d'après le général Pierre Cambronne (1770-1842) de la bataille de Waterloo.",
        "tagline": "M6 — aérienne, général Cambronne (Waterloo 1815)",
        "hero_desc": "Station <strong>Cambronne</strong>, <strong>aérienne</strong>, place Cambronne dans le <strong>15e arrondissement</strong>. Desservie par la <strong>ligne 6 du métro</strong>, ouverte le <strong>24 avril 1906</strong>. Nommée d'après le <strong>général Pierre Cambronne</strong> (<strong>1770-1842</strong>), célèbre pour sa résistance à <strong>Waterloo</strong> en 1815. Quartier résidentiel du <strong>15e</strong>, vue Tour Eiffel depuis le quai aérien.",
        "intros": [
            "La station <strong>Cambronne</strong> est implantée <strong>place Cambronne</strong> dans le <strong>15e arrondissement</strong>. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>La Motte-Picquet - Grenelle</strong> (1 station) et <strong>Sèvres - Lecourbe</strong> (1 station). Bus 80 et 49 en correspondance.",
            "Station <strong>aérienne</strong> sur le viaduc de la ligne 6, elle offre des vues sur le 15e arrondissement et permet d'apercevoir la <strong>Tour Eiffel</strong> au nord. Ouverte le <strong>24 avril 1906</strong>.",
            "Le nom <strong>Cambronne</strong> rend hommage au <strong>général Pierre Cambronne</strong> (<strong>1770-1842</strong>), <strong>général de la Garde impériale</strong> sous Napoléon. Resté célèbre pour sa résistance lors de la <strong>bataille de Waterloo</strong> (18 juin 1815) et pour le <strong>« mot de Cambronne »</strong> (« La Garde meurt mais ne se rend pas » selon la légende, ou « Merde ! » selon Cambronne lui-même)."
        ],
        "hist_title": "1906 : viaduc Grenelle et le général Cambronne",
        "hist": [
            "La station Cambronne est <strong>inaugurée le 24 avril 1906</strong> avec la mise en service du tronçon <strong>Place d'Italie ↔ Étoile</strong> (ancienne ligne 2 Sud, devenue ligne 6).",
            "Le nom <strong>Cambronne</strong> commémore <strong>Pierre Jacques Étienne Cambronne</strong> (<strong>26 décembre 1770 - 5 mars 1842</strong>), <strong>général d'Empire</strong>. Engagé volontaire en 1792, il sert sous la Révolution puis l'Empire. <strong>Chevalier de la Légion d'honneur</strong> (1804), <strong>baron d'Empire</strong> (1810). Suit Napoléon à l'<strong>île d'Elbe</strong> (1814-1815).",
            "À <strong>Waterloo</strong>, le 18 juin 1815, il commande la dernière résistance des <strong>chasseurs à pied de la Vieille Garde</strong>. Sommé de se rendre, il aurait répondu selon la légende : <em>« La Garde meurt mais ne se rend pas. »</em> Cambronne lui-même nia cette formule, affirmant avoir répondu : <em>« Merde ! »</em>. Cette dernière exclamation est entrée dans la langue française sous l'expression <strong>« mot de Cambronne »</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Cambronne ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 80 et 49."),
            ("Cambronne est-elle aérienne ?", "<strong>Oui</strong>. Station aérienne sur le viaduc de la ligne 6, place Cambronne."),
            ("Qui est le général Cambronne ?", "<strong>Pierre Cambronne</strong> (1770-1842), général de la Garde impériale sous Napoléon. Célèbre pour sa résistance à <strong>Waterloo</strong> (1815) et le <strong>« mot de Cambronne »</strong>."),
            ("Qu'est-ce que le « mot de Cambronne » ?", "Selon la légende, <em>« La Garde meurt mais ne se rend pas. »</em>. Cambronne lui-même affirma avoir répondu : <em>« Merde ! »</em>. Cette exclamation est entrée dans la langue française."),
            ("Quand a-t-elle ouvert ?", "Le <strong>24 avril 1906</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station aérienne ancienne (1906), pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Vue sur la Tour Eiffel</strong> depuis le quai aérien — au nord.",
            "<strong>Place Cambronne</strong> et square Cambronne : espace vert agréable.",
            "Pour <strong>La Motte-Picquet - Grenelle</strong> (hub M6+M8+M10) : <strong>M6 directe</strong> (1 station).",
            "Quartier résidentiel <strong>15e</strong> paisible et familial.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⚔️", "Général Cambronne et Waterloo", "<strong>Pierre Cambronne</strong> (1770-1842), engagé volontaire en 1792. <strong>Général de la Garde impériale</strong>, il suit Napoléon à l'<strong>île d'Elbe</strong> (1814-1815). À <strong>Waterloo</strong> (18 juin 1815), il commande les chasseurs à pied de la Vieille Garde. Sommé de se rendre, sa réponse est entrée dans la légende : <em>« La Garde meurt mais ne se rend pas. »</em> ou, selon Cambronne lui-même, <em>« Merde ! »</em>. Capturé blessé, prisonnier en Angleterre, il rentre en France en 1816."),
            ("🗣️", "Le « mot de Cambronne »", "L'expression <strong>« mot de Cambronne »</strong> désigne en français le juron <em>« Merde ! »</em> attribué au général à Waterloo. <strong>Victor Hugo</strong>, dans <em>Les Misérables</em>, immortalise la scène : <em>« L'homme qui a gagné la bataille de Waterloo, ce n'est pas Napoléon en déroute, c'est Cambronne en pleine déroute. »</em>")
        ],
        "itin": [
            ("Tour Eiffel via Bir-Hakeim", "bir-hakeim", "M6", "M6 vers Bir-Hakeim (2 stations) puis pont", 15),
            ("La Motte-Picquet - Grenelle", "la-motte-picquet-grenelle", "M6", "M6 directe (1 station)", 3),
            ("Champ-de-Mars - Tour Eiffel", "champ-de-mars-tour-eiffel", "M6 + RER C", "M6 → Bir-Hakeim + RER C", 18),
            ("Concorde", "concorde", "M6 + M8", "M6 → La Motte-Picquet + M8", 20),
            ("Montparnasse", "montparnasse-bienvenue", "M6", "M6 directe (4 stations)", 9),
            ("Châtelet", "chatelet", "M6 + M1", "M6 → Étoile + M1", 28)
        ]
    },
    "sevres-lecourbe": {
        "addr": "Boulevard Garibaldi, 75015 Paris", "arr": "15e arrondissement (Paris)",
        "seo": "Station Sèvres - Lecourbe (M6) aérienne boulevard Garibaldi dans le 15e arrondissement. Nommée d'après la rue de Sèvres et l'avenue Lecourbe.",
        "tagline": "M6 — aérienne, croisement rue de Sèvres et avenue Lecourbe",
        "hero_desc": "Station <strong>Sèvres - Lecourbe</strong>, <strong>aérienne</strong>, sur le <strong>boulevard Garibaldi</strong> dans le <strong>15e arrondissement</strong>. Desservie par la <strong>ligne 6 du métro</strong>, ouverte le <strong>24 avril 1906</strong>. Située au croisement de la <strong>rue de Sèvres</strong> et de l'<strong>avenue Lecourbe</strong>. Quartier résidentiel du <strong>15e</strong>.",
        "intros": [
            "La station <strong>Sèvres - Lecourbe</strong> est implantée <strong>boulevard Garibaldi</strong> dans le <strong>15e arrondissement</strong>, au croisement de la <strong>rue de Sèvres</strong> et de l'<strong>avenue Lecourbe</strong>. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Cambronne</strong> (1 station) et <strong>Pasteur</strong> (1 station). Bus 39, 70 et 88 en correspondance.",
            "Station <strong>aérienne</strong> sur le viaduc de la ligne 6, ouverte le <strong>24 avril 1906</strong> avec le tronçon Place d'Italie ↔ Étoile (ancienne ligne 2 Sud devenue ligne 6).",
            "Le nom combine deux voies : la <strong>rue de Sèvres</strong> (axe historique reliant Paris à la ville de Sèvres, célèbre pour ses porcelaines) et l'<strong>avenue Lecourbe</strong> (nommée d'après le <strong>général Claude Lecourbe</strong>, 1759-1815, général d'Empire). Quartier résidentiel paisible du <strong>15e</strong>."
        ],
        "hist_title": "1906 : viaduc Garibaldi et croisement Sèvres - Lecourbe",
        "hist": [
            "La station Sèvres - Lecourbe est <strong>inaugurée le 24 avril 1906</strong> avec la mise en service du tronçon <strong>Place d'Italie ↔ Étoile</strong> (ancienne ligne 2 Sud, devenue ligne 6).",
            "La <strong>rue de Sèvres</strong> (longue de 2 km) tire son nom de la ville de <strong>Sèvres</strong> (Hauts-de-Seine), célèbre pour ses <strong>porcelaines</strong> de la <strong>Manufacture nationale de Sèvres</strong> (fondée en 1740 à Vincennes, transférée à Sèvres en 1756). L'<strong>avenue Lecourbe</strong> rend hommage au <strong>général Claude Lecourbe</strong> (1759-1815), général d'Empire de la Révolution puis du Premier Empire.",
            "La station se trouve à proximité de l'<strong>UNESCO</strong> (avenue de Suffren) et du <strong>boulevard Garibaldi</strong>, viaduc aérien soutenant la ligne 6. Le boulevard Garibaldi rend hommage à <strong>Giuseppe Garibaldi</strong> (1807-1882), général italien artisan de l'<strong>unification de l'Italie</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Sèvres - Lecourbe ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 39, 70 et 88."),
            ("Sèvres - Lecourbe est-elle aérienne ?", "<strong>Oui</strong>. Station aérienne sur le viaduc de la ligne 6, boulevard Garibaldi."),
            ("D'où vient le nom Sèvres - Lecourbe ?", "Le nom combine la <strong>rue de Sèvres</strong> (ville célèbre pour ses porcelaines) et l'<strong>avenue Lecourbe</strong> (général Claude Lecourbe, 1759-1815)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>24 avril 1906</strong>."),
            ("Comment aller à l'UNESCO ?", "<strong>~10 min à pied</strong> via l'avenue de Suffren."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station aérienne ancienne (1906), pas d'ascenseur.")
        ],
        "tips": [
            "<strong>UNESCO</strong> (siège mondial) à 10 min à pied via avenue de Suffren.",
            "Quartier résidentiel paisible du <strong>15e arrondissement</strong>.",
            "Pour <strong>Pasteur</strong> et l'<strong>Institut Pasteur</strong> : <strong>M6 directe</strong> (1 station).",
            "Pour <strong>Montparnasse</strong> : <strong>M6 directe</strong> (3 stations).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏺", "Manufacture nationale de Sèvres et porcelaines", "La <strong>rue de Sèvres</strong> doit son nom à la ville de Sèvres (Hauts-de-Seine), célèbre pour la <strong>Manufacture nationale de Sèvres</strong>. Fondée en <strong>1740 au château de Vincennes</strong>, transférée à <strong>Sèvres en 1756</strong> sous l'impulsion de la marquise de Pompadour, elle est devenue propriété royale en <strong>1759</strong>. Les <strong>porcelaines de Sèvres</strong> ont équipé les cours européennes et restent un symbole du raffinement artistique français."),
            ("🇮🇹", "Garibaldi, héros de l'unification italienne", "Le <strong>boulevard Garibaldi</strong>, viaduc supportant la ligne 6 au-dessus, rend hommage à <strong>Giuseppe Garibaldi</strong> (1807-1882), <strong>général italien</strong> et figure du Risorgimento. Acteur majeur de l'<strong>unification de l'Italie</strong> (1860 : campagne des Mille en Sicile). Il combattit également pour la France en <strong>1870</strong> lors de la guerre franco-prussienne (armée des Vosges).")
        ],
        "itin": [
            ("UNESCO", "ecole-militaire", "M6 + M8", "À pied via avenue de Suffren (10 min)", 10),
            ("Pasteur", "pasteur", "M6", "M6 directe (1 station)", 3),
            ("Montparnasse", "montparnasse-bienvenue", "M6", "M6 directe (3 stations)", 7),
            ("La Motte-Picquet - Grenelle", "la-motte-picquet-grenelle", "M6", "M6 directe (2 stations)", 5),
            ("Tour Eiffel via Bir-Hakeim", "bir-hakeim", "M6", "M6 vers Bir-Hakeim (3 stations)", 18),
            ("Concorde", "concorde", "M6 + M8", "M6 → La Motte-Picquet + M8", 22)
        ]
    },
    "pasteur": {
        "addr": "Boulevard Pasteur, 75015 Paris", "arr": "15e arrondissement (Paris)",
        "seo": "Station Pasteur (M6+M12) à l'angle des boulevards Pasteur et Vaugirard dans le 15e arrondissement. Nommée d'après Louis Pasteur, à proximité de l'Institut Pasteur.",
        "tagline": "M6 + M12 — Louis Pasteur (1822-1895) et l'Institut Pasteur",
        "hero_desc": "Station <strong>Pasteur</strong> à l'angle des <strong>boulevards Pasteur et de Vaugirard</strong> dans le <strong>15e arrondissement</strong>. Hub <strong>M6 + M12</strong>. Nommée d'après <strong>Louis Pasteur</strong> (<strong>1822-1895</strong>), <strong>chimiste et microbiologiste français</strong>, fondateur de la <strong>microbiologie médicale</strong>. À proximité de l'<strong>Institut Pasteur</strong> et de son <strong>musée</strong>. Ouverte en <strong>1906</strong> (M6) et <strong>1910</strong> (M12).",
        "intros": [
            "La station <strong>Pasteur</strong> est implantée à l'angle du <strong>boulevard Pasteur</strong> et du <strong>boulevard de Vaugirard</strong>, dans le <strong>15e arrondissement</strong>. Elle est desservie par les <strong>lignes 6 et 12</strong> du métro parisien, formant un <strong>nœud de correspondance</strong>. Bus 39, 70, 88, 91 en correspondance.",
            "Quais M6 <strong>aériens</strong> (viaduc), quais M12 <strong>souterrains</strong>. Ouverte le <strong>24 avril 1906</strong> sur la ligne 6 (alors ligne 2 Sud) et le <strong>5 novembre 1910</strong> sur la ligne 12 (Nord-Sud à l'époque). La correspondance interne fut créée par la suite.",
            "Le nom <strong>Pasteur</strong> rend hommage à <strong>Louis Pasteur</strong> (1822-1895), <strong>chimiste et microbiologiste</strong>, fondateur de la <strong>microbiologie médicale</strong>. Il découvre le <strong>vaccin contre la rage</strong> (1885) et démontre le rôle des micro-organismes dans les fermentations (<strong>pasteurisation</strong>). L'<strong>Institut Pasteur</strong>, fondé en 1888, est à courte distance (rue du Docteur Roux)."
        ],
        "hist_title": "1906-1910 : carrefour M6/M12 et Louis Pasteur",
        "hist": [
            "Les quais <strong>ligne 6</strong> ouvrent le <strong>24 avril 1906</strong> (ancienne ligne 2 Sud, devenue ligne 6) avec la mise en service du tronçon Place d'Italie ↔ Étoile. Les quais <strong>ligne 12</strong> ouvrent le <strong>5 novembre 1910</strong> sur la ligne A (devenue ligne 12) du <strong>Nord-Sud</strong> (Compagnie privée fusionnée avec la CMP en 1930).",
            "Le nom <strong>Pasteur</strong> commémore <strong>Louis Pasteur</strong> (<strong>27 décembre 1822 - 28 septembre 1895</strong>), <strong>chimiste et microbiologiste français</strong>. Né à Dole (Jura), il révolutionne la science par ses travaux sur la <strong>fermentation</strong>, la <strong>pasteurisation</strong> (1865), les <strong>maladies infectieuses</strong> et les <strong>vaccins</strong>. Son <strong>vaccin contre la rage</strong> (1885) lui vaut une renommée mondiale.",
            "L'<strong>Institut Pasteur</strong>, à courte distance de la station (rue du Docteur Roux), est <strong>fondé le 14 novembre 1888</strong> par Louis Pasteur sur souscription internationale. <strong>Centre mondial de recherche</strong> en microbiologie, immunologie et maladies infectieuses, il abrite le <strong>musée Pasteur</strong> (appartement de Pasteur conservé, crypte où il repose). <strong>10 prix Nobel</strong> y ont travaillé."
        ],
        "faq": [
            ("Quelles lignes desservent Pasteur ?", "<strong>M6</strong> (quais aériens) et <strong>M12</strong> (quais souterrains). Correspondance interne. Bus 39, 70, 88, 91."),
            ("Qui est Louis Pasteur ?", "<strong>Louis Pasteur</strong> (1822-1895), <strong>chimiste et microbiologiste français</strong>, fondateur de la <strong>microbiologie</strong>. Découvre le <strong>vaccin contre la rage</strong> (1885) et la <strong>pasteurisation</strong>."),
            ("Quand a-t-elle ouvert ?", "Quais M6 : <strong>24 avril 1906</strong>. Quais M12 : <strong>5 novembre 1910</strong>."),
            ("Comment aller à l'Institut Pasteur ?", "<strong>~5 min à pied</strong> via la rue du Docteur Roux. <strong>Musée Pasteur</strong> ouvert au public (sur réservation)."),
            ("Pour Montparnasse ?", "<strong>M6 directe</strong> (2 stations, ~5 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur entre les quais et l'extérieur.")
        ],
        "tips": [
            "<strong>Institut Pasteur</strong> à 5 min à pied (rue du Docteur Roux). <strong>Musée Pasteur</strong> ouvert au public (sur réservation).",
            "<strong>Crypte Louis Pasteur</strong> au sein de l'Institut : tombeau du savant.",
            "Pour <strong>Montparnasse</strong> : <strong>M6 directe</strong> (2 stations, ~5 min).",
            "Pour <strong>République</strong> : <strong>M12 directe</strong> (~22 min).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🧪", "Louis Pasteur, père de la microbiologie", "<strong>Louis Pasteur</strong> (1822-1895), né à Dole (Jura), <strong>chimiste et microbiologiste</strong>. Découvre la <strong>dissymétrie moléculaire</strong> (1848), réfute la <strong>génération spontanée</strong> (1862), invente la <strong>pasteurisation</strong> (1865), met au point le <strong>vaccin contre le choléra des poules</strong> (1879), le <strong>charbon</strong> (1881), la <strong>rage</strong> (<strong>6 juillet 1885</strong> : premier vaccin humain à Joseph Meister). Fonde l'<strong>Institut Pasteur</strong> en 1888."),
            ("🏛️", "Institut Pasteur, fondé en 1888", "L'<strong>Institut Pasteur</strong>, fondé le <strong>14 novembre 1888</strong> par souscription internationale, est aujourd'hui un <strong>centre mondial de recherche</strong> en microbiologie, immunologie et maladies infectieuses. <strong>10 prix Nobel</strong> y ont travaillé (dont Élie Metchnikoff, André Lwoff, Jacques Monod, François Jacob, Luc Montagnier). Le <strong>musée Pasteur</strong> conserve l'appartement où vécut le savant et sa <strong>crypte</strong> dorée par Louis-Olivier Merson.")
        ],
        "itin": [
            ("Institut Pasteur et musée", "pasteur", "à pied", "Rue du Docteur Roux (5 min)", 5),
            ("Montparnasse", "montparnasse-bienvenue", "M6", "M6 directe (2 stations)", 5),
            ("Concorde", "concorde", "M12", "M12 directe (5 stations)", 14),
            ("Saint-Lazare", "saint-lazare", "M12", "M12 directe (8 stations)", 20),
            ("Trocadéro", "trocadero", "M6", "M6 vers Trocadéro (6 stations)", 14),
            ("République", "republique", "M12 + M3", "M12 → Concorde + M3 ou directe via M12", 22)
        ]
    },
    "edgar-quinet": {
        "addr": "Boulevard Edgar Quinet, 75014 Paris", "arr": "14e arrondissement (Paris)",
        "seo": "Station Edgar Quinet (M6) boulevard Edgar Quinet à Montparnasse (14e). Nommée d'après l'historien Edgar Quinet (1803-1875). Marché Edgar Quinet réputé.",
        "tagline": "M6 — Edgar Quinet historien et Montparnasse",
        "hero_desc": "Station <strong>Edgar Quinet</strong> sur le <strong>boulevard Edgar Quinet</strong> dans le <strong>14e arrondissement</strong>, quartier <strong>Montparnasse</strong>. Desservie par la <strong>ligne 6 du métro</strong>, ouverte le <strong>1er février 1909</strong>. Nommée d'après <strong>Edgar Quinet</strong> (<strong>1803-1875</strong>), <strong>historien, écrivain et homme politique français</strong>. Proche du <strong>cimetière du Montparnasse</strong> et du <strong>marché Edgar Quinet</strong> très réputé.",
        "intros": [
            "La station <strong>Edgar Quinet</strong> est implantée sur le <strong>boulevard Edgar Quinet</strong>, dans le <strong>14e arrondissement</strong>, en plein cœur du quartier <strong>Montparnasse</strong>. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Montparnasse - Bienvenüe</strong> (1 station) et <strong>Raspail</strong> (1 station). Bus 28, 58, 91 en correspondance.",
            "Ouverte le <strong>1er février 1909</strong>. À proximité immédiate de la <strong>Tour Montparnasse</strong>, du <strong>cimetière du Montparnasse</strong> (tombes de Baudelaire, Sartre, Beauvoir, Maupassant, Beckett) et du célèbre <strong>marché Edgar Quinet</strong> (mercredi et samedi).",
            "Le nom <strong>Edgar Quinet</strong> commémore <strong>Edgar Quinet</strong> (<strong>1803-1875</strong>), <strong>historien, écrivain et homme politique français</strong>. Professeur au <strong>Collège de France</strong> (chaire des littératures du sud de l'Europe), il est un <strong>républicain libéral</strong> exilé sous le Second Empire."
        ],
        "hist_title": "1909 : Montparnasse et l'historien Edgar Quinet",
        "hist": [
            "La station Edgar Quinet est <strong>inaugurée le 1er février 1909</strong> avec le prolongement de la ligne 6 entre Place d'Italie et <strong>Glacière</strong> (en 1906 : tronçon Place d'Italie ↔ Étoile ; les stations Edgar Quinet et autres sur le tronçon Montparnasse ↔ Bienvenüe ouvrent en 1909-1910).",
            "Le nom <strong>Edgar Quinet</strong> rend hommage à <strong>Edgar Quinet</strong> (<strong>17 février 1803 - 27 mars 1875</strong>), <strong>historien, philosophe, écrivain et homme politique français</strong>. Professeur de littératures étrangères à la <strong>faculté de Lyon</strong> puis au <strong>Collège de France</strong> (chaire des littératures du sud de l'Europe, 1842). <strong>Suspendu en 1846</strong> pour ses cours anti-cléricaux.",
            "<strong>Député de l'Ain</strong> en 1848 puis <strong>député de Paris</strong> en 1871, il s'oppose à <strong>Napoléon III</strong> et s'exile en <strong>Suisse</strong> puis en <strong>Belgique</strong> de 1851 à 1870. Œuvres : <em>Ahasvérus</em> (1833), <em>Le Génie des religions</em> (1842), <em>La Révolution</em> (1865). Le <strong>marché Edgar Quinet</strong>, ouvert sur le boulevard, est l'un des plus réputés de Paris."
        ],
        "faq": [
            ("Quelle ligne dessert Edgar Quinet ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 28, 58, 91."),
            ("Qui est Edgar Quinet ?", "<strong>Edgar Quinet</strong> (1803-1875), <strong>historien, écrivain et homme politique républicain</strong>. Professeur au Collège de France, exilé sous le Second Empire."),
            ("Quand a-t-elle ouvert ?", "Le <strong>1er février 1909</strong>."),
            ("Où se trouve le marché Edgar Quinet ?", "Sur le <strong>boulevard Edgar Quinet</strong>, à la sortie de la station. Marché alimentaire <strong>mercredi et samedi</strong>, marché de la création (artistes) <strong>dimanche</strong>."),
            ("Comment aller au cimetière du Montparnasse ?", "<strong>~3 min à pied</strong>. Tombes de Baudelaire, Sartre, Beauvoir, Maupassant, Beckett, Soutine."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Marché Edgar Quinet</strong> sur le boulevard : alimentaire <strong>mercredi et samedi matin</strong>, <strong>marché de la création</strong> (artistes) <strong>dimanche</strong>.",
            "<strong>Cimetière du Montparnasse</strong> à 3 min à pied. Tombes de Baudelaire, Sartre, Beauvoir, Beckett, Maupassant.",
            "<strong>Tour Montparnasse</strong> et gare Montparnasse à 5 min à pied.",
            "Pour <strong>Châtelet</strong> : <strong>M6 + M4</strong> via Raspail (~15 min).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("📚", "Edgar Quinet, historien républicain exilé", "<strong>Edgar Quinet</strong> (1803-1875), né à Bourg-en-Bresse, <strong>historien, philosophe et homme politique français</strong>. Professeur de littératures étrangères à <strong>Lyon</strong> puis au <strong>Collège de France</strong> (chaire des littératures du sud de l'Europe, <strong>1842</strong>). Ses cours, jugés anti-cléricaux, sont <strong>suspendus en 1846</strong>. <strong>Député républicain</strong> (Ain 1848, Paris 1871), il s'oppose à <strong>Napoléon III</strong> et s'exile à <strong>Bruxelles</strong> puis en <strong>Suisse</strong> de 1851 à 1870."),
            ("🛍️", "Marché Edgar Quinet, l'un des plus réputés", "Le <strong>marché Edgar Quinet</strong> est l'un des marchés alimentaires les plus appréciés de Paris. Ouvert sur le <strong>boulevard Edgar Quinet</strong> en plein <strong>Montparnasse</strong>, il propose les <strong>mercredis et samedis matin</strong> des producteurs maraîchers, poissonniers, fromagers de qualité. Le <strong>dimanche matin</strong>, le boulevard se transforme en <strong>marché de la création</strong> avec artistes et artisans.")
        ],
        "itin": [
            ("Cimetière du Montparnasse", "edgar-quinet", "à pied", "Boulevard Edgar Quinet (3 min)", 3),
            ("Tour Montparnasse", "montparnasse-bienvenue", "M6", "M6 directe (1 station)", 3),
            ("Raspail (Fondation Cartier)", "raspail", "M6", "M6 directe (1 station)", 3),
            ("Châtelet", "chatelet", "M6 + M4", "M6 → Raspail + M4", 15),
            ("Saint-Germain-des-Prés", "saint-germain-des-pres", "M6 + M4", "M6 → Raspail + M4", 10),
            ("Tour Eiffel via Bir-Hakeim", "bir-hakeim", "M6", "M6 directe (5 stations)", 14)
        ]
    },
    "saint-jacques": {
        "addr": "Boulevard Saint-Jacques, 75014 Paris", "arr": "14e arrondissement (Paris)",
        "seo": "Station Saint-Jacques (M6) boulevard Saint-Jacques dans le 14e arrondissement. Nommée d'après la rue Saint-Jacques, ancien chemin de pèlerinage vers Compostelle.",
        "tagline": "M6 — boulevard Saint-Jacques, chemin de Compostelle",
        "hero_desc": "Station <strong>Saint-Jacques</strong> sur le <strong>boulevard Saint-Jacques</strong> dans le <strong>14e arrondissement</strong>. Desservie par la <strong>ligne 6 du métro</strong>, ouverte le <strong>24 avril 1906</strong>. Nommée d'après la <strong>rue Saint-Jacques</strong>, ancien <strong>chemin de pèlerinage</strong> partant de Paris vers <strong>Saint-Jacques-de-Compostelle</strong>. Quartier paisible du <strong>14e</strong>.",
        "intros": [
            "La station <strong>Saint-Jacques</strong> est implantée sur le <strong>boulevard Saint-Jacques</strong> dans le <strong>14e arrondissement</strong>. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Denfert-Rochereau</strong> (1 station) et <strong>Glacière</strong> (1 station). Bus 38 et 88 en correspondance.",
            "Ouverte le <strong>24 avril 1906</strong> avec le tronçon Place d'Italie ↔ Étoile (ancienne ligne 2 Sud, devenue ligne 6).",
            "Le nom <strong>Saint-Jacques</strong> rappelle la <strong>rue Saint-Jacques</strong>, l'une des plus anciennes voies de Paris, axe de l'antique <strong>Lutèce gallo-romaine</strong>. C'était le <strong>point de départ</strong> du <strong>chemin de pèlerinage vers Saint-Jacques-de-Compostelle</strong> (Galice, Espagne) depuis le Moyen Âge. La <strong>tour Saint-Jacques</strong> (4e arr.), à 5 km, marquait ce point de départ."
        ],
        "hist_title": "1906 : boulevard Saint-Jacques et chemin de Compostelle",
        "hist": [
            "La station Saint-Jacques est <strong>inaugurée le 24 avril 1906</strong> avec la mise en service du tronçon <strong>Place d'Italie ↔ Étoile</strong> (ancienne ligne 2 Sud, devenue ligne 6).",
            "La <strong>rue Saint-Jacques</strong> (5e arrondissement, prolongée par le boulevard Saint-Jacques au sud) est l'un des <strong>axes les plus anciens de Paris</strong>. Tracée à l'époque <strong>gallo-romaine</strong> sous le nom de <strong>cardo maximus</strong> de Lutèce, elle reliait Paris au sud (vers Orléans). Au Moyen Âge, elle devient le <strong>point de départ du chemin de pèlerinage</strong> vers <strong>Saint-Jacques-de-Compostelle</strong> (Galice, Espagne).",
            "La <strong>tour Saint-Jacques</strong> (4e arrondissement, à 5 km de la station), unique vestige de l'<strong>église Saint-Jacques-de-la-Boucherie</strong>, marquait le départ symbolique des pèlerins. Le quartier autour de la station est aujourd'hui résidentiel et paisible, à proximité de l'<strong>hôpital Saint-Joseph</strong> et de la <strong>Cité internationale universitaire</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Saint-Jacques ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 38 et 88."),
            ("D'où vient le nom Saint-Jacques ?", "De la <strong>rue Saint-Jacques</strong>, ancien axe romain de Lutèce, devenu au Moyen Âge le <strong>point de départ du chemin de pèlerinage</strong> vers <strong>Saint-Jacques-de-Compostelle</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>24 avril 1906</strong>."),
            ("Comment aller à Denfert-Rochereau ?", "<strong>M6 directe</strong> (1 station, ~2 min)."),
            ("Pour le Quartier latin ?", "<strong>M6 + RER B</strong> via Denfert-Rochereau, ou <strong>M6 + M4</strong> via Raspail."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "Pour <strong>Denfert-Rochereau</strong> et <strong>RER B</strong> : <strong>M6 directe</strong> (1 station).",
            "Quartier résidentiel paisible du 14e arrondissement.",
            "Pour la <strong>Cité internationale universitaire</strong> : <strong>M6 → Denfert + RER B</strong>.",
            "<strong>Hôpital Saint-Joseph</strong> à proximité.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⛪", "Chemin de Saint-Jacques-de-Compostelle", "Le <strong>chemin de Saint-Jacques-de-Compostelle</strong>, ou <em>Camino de Santiago</em>, est un <strong>pèlerinage chrétien millénaire</strong> menant à la cathédrale de Saint-Jacques-de-Compostelle (Galice, Espagne), où sont vénérées les reliques de l'apôtre <strong>saint Jacques le Majeur</strong>. La <strong>rue Saint-Jacques</strong> à Paris fut, dès le Moyen Âge, le point de départ symbolique des pèlerins du nord et de l'est de la France. <strong>Inscrit au patrimoine de l'UNESCO</strong> en 1993 (Espagne) et 1998 (France)."),
            ("🏛️", "Tour Saint-Jacques, vestige du pèlerinage", "La <strong>tour Saint-Jacques</strong> (4e arrondissement), à 5 km de la station, est l'<strong>unique vestige de l'église Saint-Jacques-de-la-Boucherie</strong> (XIIe-XVIe siècles), démolie en 1797. Haute de <strong>54 m</strong>, elle marquait le <strong>départ symbolique du pèlerinage</strong> vers Compostelle. Classée <strong>monument historique en 1862</strong> et <strong>patrimoine mondial de l'UNESCO</strong> en 1998.")
        ],
        "itin": [
            ("Denfert-Rochereau et RER B", "denfert-rochereau", "M6", "M6 directe (1 station)", 2),
            ("Glacière", "glaciere", "M6", "M6 directe (1 station)", 2),
            ("Place d'Italie", "place-d-italie", "M6", "M6 directe (4 stations)", 8),
            ("Quartier latin", "saint-michel-notre-dame", "M6 + RER B", "M6 → Denfert + RER B", 12),
            ("Montparnasse", "montparnasse-bienvenue", "M6", "M6 directe (3 stations)", 7),
            ("Bercy", "bercy", "M6", "M6 directe (10 stations)", 22)
        ]
    },
    "glaciere": {
        "addr": "Boulevard Auguste-Blanqui, 75013 Paris", "arr": "13e arrondissement (Paris)",
        "seo": "Station Glacière (M6) aérienne boulevard Auguste-Blanqui dans le 13e arrondissement. Nommée d'après la rue de la Glacière, rappel des anciennes glacières du quartier.",
        "tagline": "M6 — aérienne, rue de la Glacière (anciennes glacières)",
        "hero_desc": "Station <strong>Glacière</strong>, <strong>aérienne</strong>, sur le <strong>boulevard Auguste-Blanqui</strong> dans le <strong>13e arrondissement</strong>. Desservie par la <strong>ligne 6 du métro</strong>, ouverte le <strong>24 avril 1906</strong>. Nommée d'après la <strong>rue de la Glacière</strong>, rappel des anciennes <strong>glacières</strong> qui fournissaient la glace à Paris jusqu'au XIXe siècle.",
        "intros": [
            "La station <strong>Glacière</strong> est implantée sur le <strong>boulevard Auguste-Blanqui</strong> dans le <strong>13e arrondissement</strong>, au croisement avec la <strong>rue de la Glacière</strong>. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Saint-Jacques</strong> (1 station) et <strong>Corvisart</strong> (1 station). Bus 21 et 62 en correspondance.",
            "Station <strong>aérienne</strong> sur le viaduc de la ligne 6, ouverte le <strong>24 avril 1906</strong>.",
            "Le nom <strong>Glacière</strong> évoque les <strong>anciennes glacières</strong> qui occupaient le quartier jusqu'au XIXe siècle. On y stockait des blocs de <strong>glace naturelle</strong> récoltés en hiver dans la <strong>Bièvre</strong> (rivière aujourd'hui couverte) pour approvisionner Paris en glace toute l'année. Quartier résidentiel paisible du <strong>13e</strong>."
        ],
        "hist_title": "1906 : viaduc Blanqui et anciennes glacières",
        "hist": [
            "La station Glacière est <strong>inaugurée le 24 avril 1906</strong> avec la mise en service du tronçon <strong>Place d'Italie ↔ Étoile</strong> (ancienne ligne 2 Sud, devenue ligne 6).",
            "La <strong>rue de la Glacière</strong>, qui donne son nom à la station, rappelle les <strong>glacières</strong> situées dans le quartier jusqu'au <strong>milieu du XIXe siècle</strong>. Avant l'invention de la <strong>réfrigération mécanique</strong>, la <strong>glace naturelle</strong> récoltée en hiver dans la <strong>Bièvre</strong> et les étangs voisins était stockée dans des <strong>puits glacières</strong> creusés dans le sol. Elle servait à la <strong>conservation des aliments</strong> et au <strong>refroidissement des boissons</strong> dans les cafés et restaurants parisiens.",
            "Le <strong>boulevard Auguste-Blanqui</strong>, qui supporte le viaduc de la ligne 6, rend hommage à <strong>Louis-Auguste Blanqui</strong> (<strong>1805-1881</strong>), <strong>révolutionnaire socialiste français</strong>. Surnommé <em>« L'Enfermé »</em> en raison des <strong>37 ans</strong> passés en prison sous différents régimes pour ses activités révolutionnaires. Acteur des révolutions de 1830, 1848 et 1871 (Commune)."
        ],
        "faq": [
            ("Quelle ligne dessert Glacière ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 21 et 62."),
            ("Glacière est-elle aérienne ?", "<strong>Oui</strong>. Station aérienne sur le viaduc de la ligne 6, boulevard Auguste-Blanqui."),
            ("D'où vient le nom Glacière ?", "De la <strong>rue de la Glacière</strong>, rappel des <strong>anciennes glacières</strong> du quartier (puits où l'on stockait la glace naturelle pour Paris avant la réfrigération mécanique)."),
            ("Quand a-t-elle ouvert ?", "Le <strong>24 avril 1906</strong>."),
            ("Qui est Auguste Blanqui ?", "<strong>Louis-Auguste Blanqui</strong> (1805-1881), <strong>révolutionnaire socialiste français</strong>. Surnommé <em>« L'Enfermé »</em> en raison des 37 ans passés en prison."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station aérienne ancienne (1906), pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Quartier paisible</strong> du 13e arrondissement.",
            "<strong>Vue panoramique sud Paris</strong> depuis le quai aérien.",
            "Pour <strong>Place d'Italie</strong> : <strong>M6 directe</strong> (2 stations).",
            "Pour <strong>Quartier latin</strong> : <strong>M6 + RER B</strong> via Denfert-Rochereau.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🧊", "Glacières de Paris, conservation avant le frigo", "Jusqu'au <strong>milieu du XIXe siècle</strong>, Paris dépendait des <strong>glacières naturelles</strong> pour conserver les aliments. La <strong>glace</strong>, récoltée en hiver dans la <strong>Bièvre</strong>, les étangs de Versailles ou même importée de Norvège, était stockée dans des <strong>puits creusés dans le sol</strong> et isolés de paille. Elle approvisionnait les <strong>cafés, restaurants, hôpitaux</strong> et les bourgeois jusqu'à l'invention de la <strong>réfrigération mécanique</strong> (machine à glace de Carré, 1859) qui rendit l'industrie obsolète."),
            ("⛓️", "Auguste Blanqui, « L'Enfermé »", "<strong>Louis-Auguste Blanqui</strong> (1805-1881), <strong>révolutionnaire socialiste</strong>, théoricien de la <strong>prise du pouvoir par une avant-garde</strong>. Surnommé <em>« L'Enfermé »</em> en raison des <strong>37 ans</strong> passés en prison sous différents régimes (Restauration, Monarchie de Juillet, Second Empire, Troisième République). Acteur des <strong>révolutions de 1830, 1848 et 1871 (Commune)</strong>. Influencera Marx mais sera critiqué par lui (<em>blanquisme</em>).")
        ],
        "itin": [
            ("Place d'Italie", "place-d-italie", "M6", "M6 directe (2 stations)", 4),
            ("Saint-Jacques", "saint-jacques", "M6", "M6 directe (1 station)", 2),
            ("Corvisart", "corvisart", "M6", "M6 directe (1 station)", 2),
            ("Denfert-Rochereau", "denfert-rochereau", "M6", "M6 directe (2 stations)", 4),
            ("Quartier latin", "saint-michel-notre-dame", "M6 + RER B", "M6 → Denfert + RER B", 14),
            ("Montparnasse", "montparnasse-bienvenue", "M6", "M6 directe (4 stations)", 9)
        ]
    },
    "corvisart": {
        "addr": "Boulevard Auguste-Blanqui, 75013 Paris", "arr": "13e arrondissement (Paris)",
        "seo": "Station Corvisart (M6) aérienne boulevard Auguste-Blanqui dans le 13e arrondissement. Nommée d'après le médecin Jean-Nicolas Corvisart (1755-1821), médecin de Napoléon.",
        "tagline": "M6 — aérienne, médecin Corvisart (Napoléon)",
        "hero_desc": "Station <strong>Corvisart</strong>, <strong>aérienne</strong>, sur le <strong>boulevard Auguste-Blanqui</strong> dans le <strong>13e arrondissement</strong>. Desservie par la <strong>ligne 6 du métro</strong>, ouverte le <strong>24 avril 1906</strong>. Nommée d'après <strong>Jean-Nicolas Corvisart</strong> (<strong>1755-1821</strong>), <strong>médecin personnel de Napoléon</strong> et pionnier de la <strong>cardiologie</strong>. <strong>Vue panoramique sud de Paris</strong> depuis le quai aérien.",
        "intros": [
            "La station <strong>Corvisart</strong> est implantée sur le <strong>boulevard Auguste-Blanqui</strong> dans le <strong>13e arrondissement</strong>. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Glacière</strong> (1 station) et <strong>Place d'Italie</strong> (1 station). Bus 27 et 67 en correspondance.",
            "Station <strong>aérienne</strong> sur le viaduc de la ligne 6, elle offre une <strong>vue panoramique</strong> sur le sud de Paris (Butte-aux-Cailles, 13e). Ouverte le <strong>24 avril 1906</strong>.",
            "Le nom <strong>Corvisart</strong> rend hommage à <strong>Jean-Nicolas Corvisart des Marets</strong> (<strong>1755-1821</strong>), <strong>médecin français</strong>, <strong>médecin personnel de Napoléon Ier</strong> à partir de 1804. <strong>Pionnier de la cardiologie</strong>, il introduit en France la <strong>percussion</strong> du thorax. Quartier proche de la <strong>Butte-aux-Cailles</strong>, village pittoresque du 13e."
        ],
        "hist_title": "1906 : viaduc Blanqui et Corvisart, médecin de Napoléon",
        "hist": [
            "La station Corvisart est <strong>inaugurée le 24 avril 1906</strong> avec la mise en service du tronçon <strong>Place d'Italie ↔ Étoile</strong> (ancienne ligne 2 Sud, devenue ligne 6).",
            "Le nom <strong>Corvisart</strong> commémore <strong>Jean-Nicolas Corvisart des Marets</strong> (<strong>15 février 1755 - 18 septembre 1821</strong>), <strong>médecin français</strong>, né à Dricourt (Ardennes). Devient <strong>médecin-chef de l'hôpital de la Charité</strong> à Paris (1788). <strong>Professeur au Collège de France</strong> en clinique médicale (1797).",
            "Devient <strong>médecin personnel de Napoléon Ier</strong> à partir de <strong>1804</strong> et le suit dans ses campagnes. <strong>Baron d'Empire</strong> en 1808. <strong>Pionnier de la cardiologie</strong>, il introduit en France la <strong>percussion thoracique</strong> (méthode d'Auenbrugger) par sa traduction et publication de <em>Nouvelle méthode pour reconnaître les maladies internes de la poitrine</em> (1808). Son <em>Essai sur les maladies du cœur</em> (1806) est considéré comme l'un des <strong>premiers traités modernes de cardiologie</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Corvisart ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 27 et 67."),
            ("Corvisart est-elle aérienne ?", "<strong>Oui</strong>. Station aérienne avec <strong>vue panoramique sud Paris</strong>."),
            ("Qui est Corvisart ?", "<strong>Jean-Nicolas Corvisart</strong> (1755-1821), <strong>médecin personnel de Napoléon Ier</strong>. <strong>Pionnier de la cardiologie</strong> moderne."),
            ("Quand a-t-elle ouvert ?", "Le <strong>24 avril 1906</strong>."),
            ("Comment aller à la Butte-aux-Cailles ?", "<strong>~5 min à pied</strong> en remontant vers la place Verlaine. Quartier pittoresque du 13e."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station aérienne ancienne (1906), pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Butte-aux-Cailles</strong> à 5 min à pied : village pittoresque du 13e, rues pavées, bars et restaurants.",
            "<strong>Piscine de la Butte-aux-Cailles</strong> (1924) : eau de source naturellement chaude.",
            "<strong>Vue panoramique sud Paris</strong> depuis le quai aérien.",
            "Pour <strong>Place d'Italie</strong> : <strong>M6 directe</strong> (1 station).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("❤️", "Corvisart, médecin de Napoléon et père de la cardiologie", "<strong>Jean-Nicolas Corvisart des Marets</strong> (1755-1821), <strong>médecin-chef de l'hôpital de la Charité</strong> (1788), <strong>professeur au Collège de France</strong> (1797). <strong>Médecin personnel de Napoléon Ier</strong> de <strong>1804 à 1815</strong>. Suit Napoléon dans ses campagnes (mais pas en Russie). <strong>Pionnier de la cardiologie</strong>, il introduit en France la <strong>percussion thoracique</strong>. Son <em>Essai sur les maladies du cœur</em> (1806) est considéré comme l'<strong>un des premiers traités modernes de cardiologie</strong>."),
            ("🏡", "Butte-aux-Cailles, village du 13e", "La <strong>Butte-aux-Cailles</strong>, à 5 min à pied de Corvisart, est un <strong>quartier pittoresque</strong> du <strong>13e arrondissement</strong> qui a échappé aux transformations haussmanniennes. Construit sur une <strong>colline de 63 m</strong>, il conserve un <strong>caractère de village</strong> : rues pavées, maisons basses, bars et restaurants animés. La <strong>piscine de la Butte-aux-Cailles</strong> (1924) est alimentée par une <strong>source chaude</strong>.")
        ],
        "itin": [
            ("Place d'Italie", "place-d-italie", "M6", "M6 directe (1 station)", 2),
            ("Butte-aux-Cailles", "place-d-italie", "à pied", "Place Verlaine (5 min)", 5),
            ("Glacière", "glaciere", "M6", "M6 directe (1 station)", 2),
            ("Quartier latin", "saint-michel-notre-dame", "M6 + RER B", "M6 → Denfert + RER B", 16),
            ("Montparnasse", "montparnasse-bienvenue", "M6", "M6 directe (5 stations)", 11),
            ("Bercy", "bercy", "M6", "M6 directe (8 stations)", 17)
        ]
    },
    "nationale": {
        "addr": "Boulevard Vincent-Auriol, 75013 Paris", "arr": "13e arrondissement (Paris)",
        "seo": "Station Nationale (M6) aérienne boulevard Vincent-Auriol dans le 13e arrondissement. Nommée d'après la rue Nationale, à proximité du Chinatown nord.",
        "tagline": "M6 — aérienne, rue Nationale et Chinatown nord",
        "hero_desc": "Station <strong>Nationale</strong>, <strong>aérienne</strong>, sur le <strong>boulevard Vincent-Auriol</strong> dans le <strong>13e arrondissement</strong>. Desservie par la <strong>ligne 6 du métro</strong>, ouverte le <strong>24 avril 1906</strong>. Nommée d'après la <strong>rue Nationale</strong> proche. À proximité du <strong>Chinatown nord</strong> de Paris.",
        "intros": [
            "La station <strong>Nationale</strong> est implantée sur le <strong>boulevard Vincent-Auriol</strong> dans le <strong>13e arrondissement</strong>, près de la <strong>rue Nationale</strong>. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Place d'Italie</strong> (1 station) et <strong>Chevaleret</strong> (1 station). Bus 27, 62 et 89 en correspondance.",
            "Station <strong>aérienne</strong> sur le viaduc de la ligne 6, ouverte le <strong>24 avril 1906</strong>.",
            "Le nom <strong>Nationale</strong> vient de la <strong>rue Nationale</strong>, voie historique du <strong>13e arrondissement</strong>. Le quartier est à la lisière du <strong>Chinatown parisien</strong> et accueille de nombreux <strong>commerces asiatiques</strong>. Quartier en pleine mutation avec les opérations de rénovation urbaine du <strong>13e</strong>."
        ],
        "hist_title": "1906 : viaduc Vincent-Auriol et 13e arrondissement",
        "hist": [
            "La station Nationale est <strong>inaugurée le 24 avril 1906</strong> avec la mise en service du tronçon <strong>Place d'Italie ↔ Étoile</strong> (ancienne ligne 2 Sud, devenue ligne 6).",
            "Le <strong>boulevard Vincent-Auriol</strong> rend hommage à <strong>Vincent Auriol</strong> (<strong>1884-1966</strong>), <strong>premier président de la Quatrième République</strong> (<strong>16 janvier 1947 - 16 janvier 1954</strong>). Socialiste, ministre des Finances du Front populaire (1936), il s'oppose à Pétain en 1940. La rue Nationale, qui donne son nom à la station, est une voie historique du <strong>13e arrondissement</strong>.",
            "Le <strong>13e arrondissement</strong> abrite le <strong>Chinatown de Paris</strong>, principal quartier asiatique de la capitale, formé après l'<strong>arrivée des réfugiés d'Asie du Sud-Est</strong> (Vietnam, Cambodge, Laos) à partir de <strong>1975</strong>. Le quartier compte aujourd'hui plus de <strong>200 commerces asiatiques</strong>, restaurants, supermarchés. Lieu de célébration du <strong>Nouvel An chinois</strong> chaque année."
        ],
        "faq": [
            ("Quelle ligne dessert Nationale ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 27, 62 et 89."),
            ("Nationale est-elle aérienne ?", "<strong>Oui</strong>. Station aérienne sur le viaduc de la ligne 6."),
            ("Quand a-t-elle ouvert ?", "Le <strong>24 avril 1906</strong>."),
            ("Comment aller à Place d'Italie ?", "<strong>M6 directe</strong> (1 station, ~2 min)."),
            ("Pour le Chinatown ?", "<strong>~10 min à pied</strong> vers avenue de Choisy / avenue d'Ivry."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station aérienne ancienne (1906), pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Chinatown</strong> à 10 min à pied via avenue de Choisy/Ivry. Restaurants, commerces asiatiques.",
            "<strong>Nouvel An chinois</strong> célébré chaque année dans le 13e (fin janvier / février).",
            "Pour <strong>Place d'Italie</strong> et son centre commercial : <strong>M6 directe</strong> (1 station).",
            "Pour <strong>Bercy</strong> : <strong>M6 directe</strong> (5 stations).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🇨🇳", "Chinatown de Paris dans le 13e", "Le <strong>13e arrondissement</strong> abrite le <strong>Chinatown de Paris</strong>, principal quartier asiatique de France. Formé à partir de <strong>1975</strong> avec l'<strong>arrivée des réfugiés d'Asie du Sud-Est</strong> (Vietnam, Cambodge, Laos), il s'étend autour des <strong>avenues de Choisy, d'Ivry et de la Porte d'Ivry</strong>. Plus de <strong>200 commerces asiatiques</strong>, restaurants, supermarchés (Tang Frères, Paris Store). Le <strong>défilé du Nouvel An chinois</strong> dans le 13e est l'un des plus importants d'Europe."),
            ("🏛️", "Vincent Auriol, premier président de la IVe", "<strong>Vincent Auriol</strong> (1884-1966), <strong>premier président de la Quatrième République</strong> (16 janvier 1947 - 16 janvier 1954). Avocat, député socialiste de Haute-Garonne, <strong>ministre des Finances du Front populaire</strong> (1936) sous Léon Blum. <strong>S'oppose à Pétain</strong> et vote contre les pleins pouvoirs le 10 juillet 1940 (parmi les 80). Le boulevard Vincent-Auriol, qui supporte le viaduc M6, lui rend hommage.")
        ],
        "itin": [
            ("Place d'Italie", "place-d-italie", "M6", "M6 directe (1 station)", 2),
            ("Chinatown (avenue de Choisy)", "place-d-italie", "à pied", "Avenue de Choisy (10 min)", 10),
            ("Chevaleret", "chevaleret", "M6", "M6 directe (1 station)", 2),
            ("Bercy", "bercy", "M6", "M6 directe (5 stations)", 11),
            ("Quartier latin", "saint-michel-notre-dame", "M6 + RER B", "M6 → Denfert + RER B", 18),
            ("Montparnasse", "montparnasse-bienvenue", "M6", "M6 directe (7 stations)", 15)
        ]
    },
    "chevaleret": {
        "addr": "Rue du Chevaleret, 75013 Paris", "arr": "13e arrondissement (Paris)",
        "seo": "Station Chevaleret (M6) aérienne dans le 13e arrondissement, proche du quartier Olympiades. Nommée d'après la rue du Chevaleret.",
        "tagline": "M6 — aérienne, rue du Chevaleret et quartier Olympiades",
        "hero_desc": "Station <strong>Chevaleret</strong>, <strong>aérienne</strong>, dans le <strong>13e arrondissement</strong>. Desservie par la <strong>ligne 6 du métro</strong>, ouverte le <strong>24 avril 1906</strong>. Nommée d'après la <strong>rue du Chevaleret</strong>. À proximité du <strong>quartier Olympiades</strong> et de la <strong>Bibliothèque François Mitterrand</strong>.",
        "intros": [
            "La station <strong>Chevaleret</strong> est implantée dans le <strong>13e arrondissement</strong>, à proximité de la <strong>rue du Chevaleret</strong>. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Nationale</strong> (1 station) et <strong>Quai de la Gare</strong> (1 station). Bus 89 en correspondance.",
            "Station <strong>aérienne</strong> sur le viaduc de la ligne 6, ouverte le <strong>24 avril 1906</strong>.",
            "Le nom <strong>Chevaleret</strong> vient de la <strong>rue du Chevaleret</strong>, voie historique du <strong>13e arrondissement</strong>. Le quartier est à proximité des <strong>Olympiades</strong> (ensemble de tours résidentielles des années 1970, prolongement du Chinatown) et de la <strong>Bibliothèque nationale de France</strong> (site François Mitterrand)."
        ],
        "hist_title": "1906 : viaduc Vincent-Auriol et rue du Chevaleret",
        "hist": [
            "La station Chevaleret est <strong>inaugurée le 24 avril 1906</strong> avec la mise en service du tronçon <strong>Place d'Italie ↔ Étoile</strong> (ancienne ligne 2 Sud, devenue ligne 6).",
            "La <strong>rue du Chevaleret</strong>, qui donne son nom à la station, est une voie historique du <strong>13e arrondissement</strong>. L'étymologie évoque un <strong>relais de chevaux</strong> (<em>chevalet</em>, petit cheval). Le quartier était autrefois industriel et populaire, le long de la <strong>Seine</strong>.",
            "Le quartier connaît une <strong>profonde transformation</strong> depuis les années 1990 avec la <strong>ZAC Paris-Rive Gauche</strong> : édification de la <strong>Bibliothèque nationale de France - François Mitterrand</strong> (1996), du <strong>quartier Olympiades</strong> (Chinatown nord), de l'<strong>université Paris-Cité</strong> et de <strong>nombreux bureaux et logements neufs</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Chevaleret ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 89."),
            ("Chevaleret est-elle aérienne ?", "<strong>Oui</strong>. Station aérienne sur le viaduc de la ligne 6."),
            ("Quand a-t-elle ouvert ?", "Le <strong>24 avril 1906</strong>."),
            ("Comment aller à la Bibliothèque François Mitterrand ?", "<strong>~10 min à pied</strong> vers le quai François-Mauriac, ou <strong>M6 + M14</strong>."),
            ("Pour les Olympiades ?", "<strong>~10 min à pied</strong>. Quartier de tours résidentielles, prolongement du Chinatown."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station aérienne ancienne (1906), pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Bibliothèque nationale de France - François Mitterrand</strong> à 10 min à pied.",
            "<strong>Quartier Olympiades</strong> : tours résidentielles, Chinatown nord, restaurants asiatiques.",
            "Pour <strong>Bercy</strong> : <strong>M6 directe</strong> (4 stations).",
            "Pour <strong>Quai de la Gare</strong> et vue Seine : <strong>M6 directe</strong> (1 station).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("📚", "Bibliothèque nationale de France - François Mitterrand", "La <strong>BnF site François Mitterrand</strong>, inaugurée le <strong>30 mars 1995</strong> par le président François Mitterrand, est le <strong>plus grand site de la BnF</strong>. Œuvre de l'architecte <strong>Dominique Perrault</strong>, elle se compose de <strong>quatre tours d'angle</strong> en forme de <strong>livres ouverts</strong> (T1 à T4), encadrant un <strong>jardin-forêt central</strong>. Plus de <strong>40 millions de documents</strong>. À 10 min à pied de Chevaleret."),
            ("🌆", "Olympiades, urbanisme dalle des années 1970", "Le <strong>quartier Olympiades</strong>, à proximité de Chevaleret, est un ensemble urbain construit de <strong>1969 à 1977</strong>. Aujourd'hui un <strong>prolongement du Chinatown</strong>, il abrite des restaurants asiatiques, supermarchés et le <strong>complexe résidentiel</strong> des tours nommées d'après les villes olympiques (Sapporo, Tokyo, Mexico, Helsinki, Rome, Athènes, Cortina).")
        ],
        "itin": [
            ("Bibliothèque François Mitterrand", "bibliotheque-francois-mitterrand", "à pied", "Quai François-Mauriac (10 min)", 10),
            ("Quai de la Gare", "quai-de-la-gare", "M6", "M6 directe (1 station)", 2),
            ("Place d'Italie", "place-d-italie", "M6", "M6 directe (2 stations)", 5),
            ("Bercy", "bercy", "M6", "M6 directe (4 stations)", 9),
            ("Olympiades", "olympiades", "à pied", "Quartier Olympiades (10 min)", 10),
            ("Quartier latin", "saint-michel-notre-dame", "M6 + RER B", "M6 → Denfert + RER B", 22)
        ]
    },
    "quai-de-la-gare": {
        "addr": "Boulevard Vincent-Auriol, 75013 Paris", "arr": "13e arrondissement (Paris)",
        "seo": "Station Quai de la Gare (M6) aérienne dans le 13e, à proximité du viaduc d'Austerlitz sur la Seine. Vue panoramique. Proche gare d'Austerlitz et BnF.",
        "tagline": "M6 — aérienne, viaduc d'Austerlitz et vue Seine",
        "hero_desc": "Station <strong>Quai de la Gare</strong>, <strong>aérienne</strong>, dans le <strong>13e arrondissement</strong>. Desservie par la <strong>ligne 6 du métro</strong>, ouverte le <strong>24 avril 1906</strong>. Située juste avant le <strong>viaduc d'Austerlitz</strong>, qui fait traverser la Seine à la ligne 6. <strong>Vue panoramique</strong> sur la Seine et le quartier <strong>Paris-Rive Gauche</strong>.",
        "intros": [
            "La station <strong>Quai de la Gare</strong> est implantée dans le <strong>13e arrondissement</strong>, juste avant que la ligne 6 ne traverse la Seine par le <strong>viaduc d'Austerlitz</strong>. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Chevaleret</strong> (1 station) et <strong>Bercy</strong> (1 station). Bus 89 en correspondance.",
            "Station <strong>aérienne</strong> offrant une <strong>vue panoramique</strong> sur la <strong>Seine</strong> et le quartier <strong>Paris-Rive Gauche</strong>. Ouverte le <strong>24 avril 1906</strong>.",
            "Le nom <strong>Quai de la Gare</strong> rappelle la proximité du <strong>quai éponyme</strong>, le long de la Seine, et de la <strong>gare d'Austerlitz</strong> (rive droite). Le quartier abrite la <strong>Bibliothèque nationale de France - François Mitterrand</strong> et le <strong>port de la Gare</strong> (péniches)."
        ],
        "hist_title": "1906 : viaduc d'Austerlitz et traversée de la Seine",
        "hist": [
            "La station Quai de la Gare est <strong>inaugurée le 24 avril 1906</strong> avec le tronçon <strong>Place d'Italie ↔ Étoile</strong> (ancienne ligne 2 Sud, devenue ligne 6).",
            "Le <strong>viaduc d'Austerlitz</strong>, qui prolonge la ligne 6 à la sortie de la station, est un <strong>pont métallique</strong> construit pour le <strong>métropolitain</strong>. <strong>Long de 140 m</strong>, il est constitué d'un <strong>arc unique en acier</strong> et fait <strong>traverser la Seine</strong> à la ligne 6 entre le 13e et le 12e arrondissement. Il offre l'une des <strong>plus belles vues métro</strong> sur la Seine et la Bibliothèque nationale.",
            "Le quartier <strong>Paris-Rive Gauche</strong>, ZAC créée en 1991, a profondément transformé le secteur depuis les années 1990. Inauguration de la <strong>BnF François Mitterrand</strong> en 1996, construction de l'<strong>université Paris-Cité</strong> (Grands Moulins de Paris), édification de bureaux et logements neufs."
        ],
        "faq": [
            ("Quelle ligne dessert Quai de la Gare ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 89."),
            ("Quai de la Gare est-elle aérienne ?", "<strong>Oui</strong>. Station aérienne sur le viaduc de la ligne 6."),
            ("Le viaduc d'Austerlitz a-t-il une belle vue ?", "<strong>Oui</strong>. Vue iconique sur la <strong>Seine</strong> et la <strong>BnF François Mitterrand</strong> depuis le quai aérien et lors de la traversée du viaduc."),
            ("Quand a-t-elle ouvert ?", "Le <strong>24 avril 1906</strong>."),
            ("Comment aller à la gare d'Austerlitz ?", "<strong>~10 min à pied</strong> via le quai et le pont Charles-de-Gaulle, ou <strong>M6 + M5</strong> via Bercy."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station aérienne ancienne (1906), pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Vue iconique</strong> sur la Seine et la BnF depuis le quai aérien.",
            "<strong>Traversée du viaduc d'Austerlitz</strong> en direction de Bercy : panorama exceptionnel.",
            "<strong>BnF François Mitterrand</strong> à 8 min à pied.",
            "Pour <strong>Bercy</strong> : <strong>M6 directe</strong> (1 station via viaduc).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🌉", "Viaduc d'Austerlitz, métro sur la Seine", "Le <strong>viaduc d'Austerlitz</strong>, pont métallique construit pour le <strong>métropolitain</strong>, fait <strong>traverser la Seine</strong> à la ligne 6 entre les 12e et 13e arrondissements. Œuvre de l'ingénieur <strong>Louis Biette</strong> (1903-1904), il est constitué d'un <strong>arc unique en acier de 140 m</strong>, sans appui dans le fleuve, afin de ne pas gêner la navigation. <strong>Inscrit aux monuments historiques en 1986</strong>. Il offre l'une des <strong>plus belles vues</strong> du métro parisien sur la Seine."),
            ("📚", "Paris-Rive Gauche, transformation urbaine", "Le quartier <strong>Paris-Rive Gauche</strong>, <strong>ZAC créée en 1991</strong>, est l'une des plus grandes opérations d'urbanisme parisiennes depuis Haussmann. Construite sur <strong>130 hectares</strong> d'anciennes friches ferroviaires, elle a vu naître la <strong>BnF François Mitterrand</strong> (1996), l'<strong>université Paris-Cité</strong> (Grands Moulins), des <strong>quartiers neufs</strong> (Massena, Tolbiac).")
        ],
        "itin": [
            ("Bercy", "bercy", "M6", "M6 directe via viaduc d'Austerlitz (1 station)", 3),
            ("BnF François Mitterrand", "bibliotheque-francois-mitterrand", "à pied", "Quai François-Mauriac (8 min)", 8),
            ("Gare d'Austerlitz", "gare-d-austerlitz", "M6 + M5", "M6 → Bercy + M5", 8),
            ("Chevaleret", "chevaleret", "M6", "M6 directe (1 station)", 2),
            ("Place d'Italie", "place-d-italie", "M6", "M6 directe (3 stations)", 6),
            ("Châtelet", "chatelet", "M6 + RER A ou M14", "Bercy + M14, ou via Étoile + M1", 18)
        ]
    },
    "dugommier": {
        "addr": "Rue de Charenton, 75012 Paris", "arr": "12e arrondissement (Paris)",
        "seo": "Station Dugommier (M6) dans le 12e arrondissement. Nommée d'après le général Jacques-François Dugommier (1738-1794), général de la Révolution française.",
        "tagline": "M6 — général Dugommier (Révolution française)",
        "hero_desc": "Station <strong>Dugommier</strong> sur la <strong>rue de Charenton</strong> dans le <strong>12e arrondissement</strong>. Desservie par la <strong>ligne 6 du métro</strong>, ouverte le <strong>1er mars 1909</strong>. Nommée d'après <strong>Jacques-François Dugommier</strong> (<strong>1738-1794</strong>), <strong>général de la Révolution française</strong> vainqueur du <strong>siège de Toulon</strong> (1793). Quartier résidentiel du <strong>12e</strong>.",
        "intros": [
            "La station <strong>Dugommier</strong> est implantée sur la <strong>rue de Charenton</strong> dans le <strong>12e arrondissement</strong>. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Bercy</strong> (1 station) et <strong>Daumesnil</strong> (1 station). Bus 24, 29 et 87 en correspondance.",
            "Ouverte le <strong>1er mars 1909</strong> avec le prolongement de la ligne 6 entre <strong>Place d'Italie</strong> et <strong>Nation</strong> (anciennement ligne 6 prolongée vers l'est).",
            "Le nom <strong>Dugommier</strong> rend hommage à <strong>Jacques-François Coquille dit Dugommier</strong> (<strong>1738-1794</strong>), <strong>général français de la Révolution</strong>. Vainqueur du <strong>siège de Toulon</strong> (décembre 1793) où le jeune <strong>Napoléon Bonaparte</strong> se distingua comme capitaine d'artillerie. <strong>Tué au combat</strong> le <strong>18 novembre 1794</strong> à la <strong>bataille de la Sierra Negra</strong> (Catalogne)."
        ],
        "hist_title": "1909 : prolongement M6 vers Nation et Dugommier",
        "hist": [
            "La station Dugommier est <strong>inaugurée le 1er mars 1909</strong> avec le prolongement de la <strong>ligne 6 entre Place d'Italie et Nation</strong> (via le viaduc d'Austerlitz mis en service en 1906).",
            "Le nom <strong>Dugommier</strong> commémore <strong>Jacques-François Coquille dit Dugommier</strong> (<strong>1er août 1738 - 18 novembre 1794</strong>), <strong>général de la Révolution française</strong> né en Guadeloupe. Officier dans l'<strong>infanterie</strong>, il rejoint l'<strong>armée révolutionnaire</strong> en 1791.",
            "Nommé <strong>général en chef de l'armée d'Italie</strong> en novembre 1793, il <strong>reprend Toulon aux Britanniques</strong> (<strong>siège de Toulon, 19 décembre 1793</strong>) avec l'aide stratégique du jeune <strong>capitaine Bonaparte</strong> (alors 24 ans, futur Napoléon Ier), qui se distingue à cette occasion. Dugommier devient ensuite <strong>général en chef de l'armée des Pyrénées-Orientales</strong> (1794) et est <strong>tué au combat le 18 novembre 1794</strong> à la <strong>bataille de la Sierra Negra</strong> (Catalogne) par un boulet de canon."
        ],
        "faq": [
            ("Quelle ligne dessert Dugommier ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 24, 29 et 87."),
            ("Qui est Dugommier ?", "<strong>Jacques-François Dugommier</strong> (1738-1794), <strong>général de la Révolution française</strong>. Vainqueur du <strong>siège de Toulon</strong> en 1793 (avec le jeune Bonaparte). Tué au combat en Catalogne en 1794."),
            ("Quand a-t-elle ouvert ?", "Le <strong>1er mars 1909</strong>."),
            ("Comment aller à Bercy ?", "<strong>M6 directe</strong> (1 station, ~2 min)."),
            ("Pour Nation ?", "<strong>M6 directe</strong> (3 stations, ~6 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "Pour <strong>Bercy</strong> et son <strong>parc</strong> + <strong>Cinémathèque française</strong> : <strong>M6 directe</strong> (1 station).",
            "Pour <strong>Nation</strong> et son hub multilignes : <strong>M6 directe</strong> (3 stations).",
            "Quartier résidentiel paisible du <strong>12e arrondissement</strong>.",
            "Pour <strong>Daumesnil</strong> (M6+M8) : <strong>M6 directe</strong> (1 station).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("⚔️", "Dugommier, Toulon 1793 et Bonaparte", "<strong>Jacques-François Dugommier</strong> (1738-1794), né en Guadeloupe, <strong>général de la Révolution française</strong>. Sa victoire la plus célèbre est la <strong>reprise de Toulon aux Britanniques</strong> (<strong>siège de Toulon, 19 décembre 1793</strong>), grâce au plan stratégique du jeune <strong>capitaine d'artillerie Bonaparte</strong> (24 ans). C'est à cette occasion que <strong>Napoléon</strong> se révéla, ce qui lança sa carrière fulgurante. Dugommier sera ensuite <strong>tué au combat à la bataille de la Sierra Negra</strong> (Catalogne) le <strong>18 novembre 1794</strong>."),
            ("🎬", "Cinémathèque française à Bercy", "La <strong>Cinémathèque française</strong>, installée au <strong>51 rue de Bercy</strong> (à 2 stations de Dugommier), abrite l'une des <strong>plus grandes collections cinématographiques au monde</strong>. Fondée en <strong>1936 par Henri Langlois</strong> et Georges Franju, elle conserve <strong>plus de 40 000 films</strong>. Installée depuis <strong>2005</strong> dans le bâtiment dessiné par <strong>Frank Gehry</strong> (anciennement American Center, 1994).")
        ],
        "itin": [
            ("Bercy", "bercy", "M6", "M6 directe (1 station)", 2),
            ("Cinémathèque française", "bercy", "M6", "M6 directe (1 station)", 3),
            ("Daumesnil", "daumesnil", "M6", "M6 directe (1 station)", 2),
            ("Nation", "nation", "M6", "M6 directe (3 stations)", 6),
            ("Gare d'Austerlitz", "gare-d-austerlitz", "M6 + M5", "M6 → Bercy + M5", 8),
            ("Place d'Italie", "place-d-italie", "M6", "M6 directe (5 stations)", 11)
        ]
    },
    "daumesnil": {
        "addr": "Place Félix-Éboué, 75012 Paris", "arr": "12e arrondissement (Paris)",
        "seo": "Station Daumesnil (M6 + M8) place Félix-Éboué dans le 12e arrondissement. Hub majeur. Nommée d'après le général Pierre Daumesnil (1776-1832, défenseur de Vincennes).",
        "tagline": "M6 + M8 — général Daumesnil (défenseur de Vincennes)",
        "hero_desc": "Station <strong>Daumesnil</strong>, hub <strong>M6 + M8</strong>, place Félix-Éboué dans le <strong>12e arrondissement</strong>. Nommée d'après <strong>Pierre Daumesnil</strong> (<strong>1776-1832</strong>), <strong>général de l'Empire</strong> et <strong>défenseur du château de Vincennes</strong> en 1814 et 1815. Ouverte en <strong>1909</strong> (M6) et <strong>1931</strong> (M8). Quartier résidentiel du <strong>12e</strong>.",
        "intros": [
            "La station <strong>Daumesnil</strong> est implantée <strong>place Félix-Éboué</strong> dans le <strong>12e arrondissement</strong>. Elle est desservie par les <strong>lignes 6 et 8</strong> du métro parisien, formant un <strong>nœud de correspondance</strong>. Bus 29, 46 et 87 en correspondance.",
            "Quais <strong>M6</strong> ouverts le <strong>1er mars 1909</strong> (avec le prolongement Place d'Italie ↔ Nation). Quais <strong>M8</strong> ouverts le <strong>5 mai 1931</strong> (prolongement de la M8 vers Charenton). Hub majeur du 12e.",
            "Le nom <strong>Daumesnil</strong> rend hommage au <strong>général Pierre Daumesnil</strong> (<strong>1776-1832</strong>), <strong>général d'Empire</strong>, surnommé <strong>« la Jambe de Bois »</strong> (il perdit sa jambe à <strong>Wagram</strong> en 1809). <strong>Défenseur du château de Vincennes</strong> en 1814 et 1815, il refusa de livrer la forteresse aux Alliés avec sa célèbre formule : <em>« Rendez-moi ma jambe, et je vous rendrai Vincennes ! »</em>"
        ],
        "hist_title": "1909-1931 : hub M6/M8 et Daumesnil « la Jambe de Bois »",
        "hist": [
            "Les quais <strong>ligne 6</strong> sont <strong>inaugurés le 1er mars 1909</strong> avec le prolongement Place d'Italie ↔ Nation. Les quais <strong>ligne 8</strong> ouvrent le <strong>5 mai 1931</strong> avec le prolongement de la M8 de la Porte de Charenton vers Daumesnil.",
            "Le nom <strong>Daumesnil</strong> commémore <strong>Pierre Yrieix Daumesnil</strong> (<strong>14 juillet 1776 - 17 août 1832</strong>), <strong>général d'Empire</strong> né à Périgueux. Engagé volontaire en 1793, il sert dans les campagnes de la Révolution puis de l'Empire. <strong>Officier des Grenadiers à pied de la Garde impériale</strong>.",
            "À la <strong>bataille de Wagram</strong> (5-6 juillet 1809), il <strong>perd sa jambe</strong> emportée par un boulet, ce qui lui vaut le surnom de <strong>« la Jambe de Bois »</strong>. <strong>Gouverneur du château de Vincennes</strong> à partir de 1812, il en assure la <strong>défense en 1814 et 1815</strong> face aux Alliés. Sommé de se rendre, il répond par sa formule restée célèbre : <em>« Rendez-moi ma jambe, et je vous rendrai Vincennes ! »</em>. La <strong>place Félix-Éboué</strong> (rebaptisée en 1947) accueille en son centre la <strong>fontaine aux Lions</strong>."
        ],
        "faq": [
            ("Quelles lignes desservent Daumesnil ?", "<strong>M6</strong> (ouverte 1909) et <strong>M8</strong> (ouverte 1931). Bus 29, 46 et 87. Hub du 12e."),
            ("Qui est le général Daumesnil ?", "<strong>Pierre Daumesnil</strong> (1776-1832), <strong>général d'Empire</strong> surnommé <strong>« la Jambe de Bois »</strong>. <strong>Défenseur du château de Vincennes</strong> en 1814-1815."),
            ("Quand a-t-elle ouvert ?", "Quais M6 : <strong>1er mars 1909</strong>. Quais M8 : <strong>5 mai 1931</strong>."),
            ("Comment aller à Bastille ?", "<strong>M8 directe</strong> (~10 min)."),
            ("Pour Bois de Vincennes ?", "<strong>M8 directe</strong> jusqu'à Porte Dorée, ou <strong>M6 → Nation</strong>."),
            ("La station est-elle accessible PMR ?", "<strong>Partiellement</strong>. Ascenseurs côté ligne 8 récemment installés.")
        ],
        "tips": [
            "<strong>Fontaine aux Lions</strong> au centre de la place Félix-Éboué.",
            "Pour <strong>Bastille</strong> : <strong>M8 directe</strong> (~10 min).",
            "Pour le <strong>Bois de Vincennes</strong> et le <strong>château de Vincennes</strong> : <strong>M8 → Porte Dorée</strong> ou <strong>M6 → Nation</strong>.",
            "Pour <strong>Bercy</strong> : <strong>M6 directe</strong> (2 stations).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🦿", "Daumesnil « la Jambe de Bois » défend Vincennes", "<strong>Pierre Daumesnil</strong> (1776-1832), surnommé <strong>« la Jambe de Bois »</strong> après avoir perdu sa jambe à <strong>Wagram</strong> (1809). <strong>Gouverneur du château de Vincennes</strong> à partir de 1812, il refuse de livrer la forteresse aux Alliés en 1814 et 1815. Sa formule restée célèbre : <em>« Rendez-moi ma jambe, et je vous rendrai Vincennes ! »</em>. Le château fut épargné grâce à sa résistance. Une <strong>statue</strong> lui rend hommage au château de Vincennes."),
            ("⛲", "Fontaine aux Lions, place Félix-Éboué", "La <strong>place Félix-Éboué</strong> (rebaptisée en 1947 en hommage à <strong>Félix Éboué</strong>, gouverneur du Tchad rallié à de Gaulle en 1940) accueille en son centre la <strong>fontaine aux Lions</strong>. Cette fontaine monumentale, ornée de <strong>quatre lions en bronze</strong>, fut installée en <strong>1880</strong>. Elle est l'une des plus belles fontaines parisiennes du <strong>Second Empire</strong>.")
        ],
        "itin": [
            ("Bercy", "bercy", "M6", "M6 directe (2 stations)", 4),
            ("Bastille", "bastille", "M8", "M8 directe (5 stations)", 10),
            ("Bois de Vincennes", "porte-doree", "M8", "M8 directe vers Porte Dorée", 8),
            ("Nation", "nation", "M6", "M6 directe (2 stations)", 4),
            ("Opéra", "opera", "M8", "M8 directe (10 stations)", 22),
            ("République", "republique", "M8 + M5", "M8 → Bastille + M5", 14)
        ]
    },
    "bel-air": {
        "addr": "Avenue du Bel-Air, 75012 Paris", "arr": "12e arrondissement (Paris)",
        "seo": "Station Bel-Air (M6) avenue du Bel-Air dans le 12e arrondissement. Petite station résidentielle entre Daumesnil et Picpus.",
        "tagline": "M6 — avenue du Bel-Air, quartier résidentiel 12e",
        "hero_desc": "Station <strong>Bel-Air</strong> sur l'<strong>avenue du Bel-Air</strong> dans le <strong>12e arrondissement</strong>. Desservie par la <strong>ligne 6 du métro</strong>, ouverte le <strong>1er mars 1909</strong>. Petite station de quartier résidentiel, entre <strong>Daumesnil</strong> et <strong>Picpus</strong>. À courte distance du <strong>Bois de Vincennes</strong>.",
        "intros": [
            "La station <strong>Bel-Air</strong> est implantée sur l'<strong>avenue du Bel-Air</strong> dans le <strong>12e arrondissement</strong>. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Daumesnil</strong> (1 station) et <strong>Picpus</strong> (1 station). Bus 29 et 56 en correspondance.",
            "Ouverte le <strong>1er mars 1909</strong> avec le prolongement de la ligne 6 entre <strong>Place d'Italie</strong> et <strong>Nation</strong>.",
            "Le nom <strong>Bel-Air</strong> vient de l'<strong>avenue du Bel-Air</strong>, qui doit elle-même son nom à un <strong>ancien château du Bel-Air</strong>, construit au XVIIIe siècle dans le quartier alors champêtre. Quartier paisible et familial du <strong>12e</strong>, à courte distance du <strong>Bois de Vincennes</strong>."
        ],
        "hist_title": "1909 : prolongement M6 vers Nation et avenue du Bel-Air",
        "hist": [
            "La station Bel-Air est <strong>inaugurée le 1er mars 1909</strong> avec le prolongement de la <strong>ligne 6 entre Place d'Italie et Nation</strong>.",
            "L'<strong>avenue du Bel-Air</strong> tire son nom d'un <strong>ancien château du Bel-Air</strong>, propriété construite au <strong>XVIIIe siècle</strong> dans le quartier alors largement champêtre, en bordure de l'ancienne <strong>route de Vincennes</strong>. Le château a disparu lors de l'urbanisation du <strong>12e arrondissement</strong> au XIXe siècle.",
            "Le quartier est aujourd'hui paisible et résidentiel, marqué par les <strong>immeubles haussmanniens</strong> et l'<strong>architecture du XXe siècle</strong>. Il s'étend à proximité du <strong>Bois de Vincennes</strong>, plus grand espace vert de Paris (~995 hectares), accessible en quelques minutes."
        ],
        "faq": [
            ("Quelle ligne dessert Bel-Air ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 29 et 56."),
            ("D'où vient le nom Bel-Air ?", "De l'<strong>avenue du Bel-Air</strong>, qui doit son nom à un <strong>ancien château du Bel-Air</strong> du XVIIIe siècle."),
            ("Quand a-t-elle ouvert ?", "Le <strong>1er mars 1909</strong>."),
            ("Pour le Bois de Vincennes ?", "<strong>~10 min à pied</strong> via l'avenue du Bel-Air et la cours de Vincennes."),
            ("Pour Nation ?", "<strong>M6 directe</strong> (1 station, ~2 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "Quartier résidentiel paisible du <strong>12e arrondissement</strong>.",
            "Pour le <strong>Bois de Vincennes</strong> : <strong>~10 min à pied</strong> ou <strong>M6 → Nation</strong>.",
            "Pour <strong>Nation</strong> et son hub multilignes : <strong>M6 directe</strong> (1 station).",
            "Pour <strong>Daumesnil</strong> (M6+M8) : <strong>M6 directe</strong> (1 station).",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🌳", "Bois de Vincennes, le plus grand parc de Paris", "Le <strong>Bois de Vincennes</strong>, à courte distance de Bel-Air, est le <strong>plus grand espace vert de Paris</strong> avec <strong>995 hectares</strong>. Ancien <strong>domaine de chasse royal</strong> du XIIe siècle, il est <strong>cédé à la Ville de Paris en 1860</strong> par Napoléon III. Il abrite le <strong>château de Vincennes</strong> (XIVe-XVIIe), le <strong>parc zoologique de Paris</strong>, l'<strong>hippodrome de Vincennes</strong>, le <strong>lac Daumesnil</strong>, le <strong>parc floral</strong>."),
            ("🏰", "Ancien château du Bel-Air", "L'<strong>avenue du Bel-Air</strong> tire son nom d'un <strong>ancien château du Bel-Air</strong>, propriété aristocratique construite au <strong>XVIIIe siècle</strong> sur les terres champêtres en bordure de l'ancienne route de Vincennes. À cette époque, le secteur n'était pas encore urbanisé et offrait une atmosphère bucolique appréciée des Parisiens fortunés cherchant un <strong>« bel air »</strong> hors de la ville polluée. Le château a disparu lors de l'urbanisation haussmannienne du 12e.")
        ],
        "itin": [
            ("Nation", "nation", "M6", "M6 directe (1 station)", 2),
            ("Bois de Vincennes", "porte-doree", "M6 + à pied", "M6 → Nation puis à pied (5 min)", 10),
            ("Daumesnil", "daumesnil", "M6", "M6 directe (1 station)", 2),
            ("Bastille", "bastille", "M6 + M1", "M6 → Nation + M1", 12),
            ("Bercy", "bercy", "M6", "M6 directe (3 stations)", 6),
            ("Place d'Italie", "place-d-italie", "M6", "M6 directe (8 stations)", 17)
        ]
    },
    "picpus": {
        "addr": "Boulevard de Picpus, 75012 Paris", "arr": "12e arrondissement (Paris)",
        "seo": "Station Picpus (M6) boulevard de Picpus dans le 12e arrondissement. Proche du cimetière de Picpus (tombe de La Fayette) et de la Nation.",
        "tagline": "M6 — boulevard de Picpus, cimetière de Picpus (La Fayette)",
        "hero_desc": "Station <strong>Picpus</strong> sur le <strong>boulevard de Picpus</strong> dans le <strong>12e arrondissement</strong>. Desservie par la <strong>ligne 6 du métro</strong>, ouverte le <strong>1er mars 1909</strong>. Proche du <strong>cimetière de Picpus</strong>, où repose <strong>Gilbert du Motier, marquis de La Fayette</strong> (<strong>1757-1834</strong>), héros des révolutions américaine et française.",
        "intros": [
            "La station <strong>Picpus</strong> est implantée sur le <strong>boulevard de Picpus</strong> dans le <strong>12e arrondissement</strong>. Elle est desservie par la <strong>ligne 6 du métro parisien</strong>, entre <strong>Bel-Air</strong> (1 station) et <strong>Nation</strong> (1 station, terminus est de la M6). Bus 56 et 64 en correspondance.",
            "Ouverte le <strong>1er mars 1909</strong> avec le prolongement de la ligne 6 entre <strong>Place d'Italie</strong> et <strong>Nation</strong>.",
            "Le nom <strong>Picpus</strong> rappelle le <strong>quartier de Picpus</strong> et son <strong>cimetière de Picpus</strong>, lieu chargé d'histoire : il accueille les <strong>fosses communes</strong> de <strong>1306 victimes de la Terreur</strong> (guillotinées en 1794 place du Trône-Renversé, aujourd'hui place de la Nation), ainsi que la <strong>tombe de La Fayette</strong>, héros de l'<strong>indépendance américaine</strong>."
        ],
        "hist_title": "1909 : Picpus et tombe de La Fayette",
        "hist": [
            "La station Picpus est <strong>inaugurée le 1er mars 1909</strong> avec le prolongement de la <strong>ligne 6 entre Place d'Italie et Nation</strong>.",
            "Le <strong>cimetière de Picpus</strong>, à 10 min à pied de la station, est un <strong>cimetière privé</strong> très particulier : il accueille les <strong>fosses communes</strong> des <strong>1306 victimes de la Terreur</strong> guillotinées entre le <strong>14 juin et le 27 juillet 1794</strong> sur la <strong>place du Trône-Renversé</strong> (aujourd'hui place de la Nation). Les corps étaient transportés depuis la guillotine jusqu'aux fosses du jardin d'un ancien couvent voisin.",
            "Le cimetière abrite également la <strong>tombe de Gilbert du Motier, marquis de La Fayette</strong> (<strong>1757-1834</strong>), <strong>héros de la guerre d'Indépendance américaine</strong> (1775-1783) et acteur majeur de la <strong>Révolution française</strong>. Recouverte de <strong>terre américaine</strong> rapportée des États-Unis, sa tombe est ornée d'un <strong>drapeau américain</strong> en permanence. Chaque <strong>4 juillet</strong> (Independence Day), une cérémonie y est organisée par l'<strong>ambassade des États-Unis</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Picpus ?", "Uniquement la <strong>ligne 6 du métro</strong>. Bus 56 et 64."),
            ("Qu'est-ce que le cimetière de Picpus ?", "<strong>Cimetière privé</strong> abritant les <strong>fosses communes de 1306 victimes de la Terreur</strong> guillotinées en 1794 place du Trône-Renversé (Nation). Aussi <strong>tombe de La Fayette</strong>."),
            ("Quand a-t-elle ouvert ?", "Le <strong>1er mars 1909</strong>."),
            ("La tombe de La Fayette est-elle accessible ?", "<strong>Oui</strong>. Cimetière ouvert au public (entrée payante, 1€). <strong>Drapeau américain</strong> en permanence sur la tombe."),
            ("Pour Nation ?", "<strong>M6 directe</strong> (1 station, ~2 min). Terminus est de la M6."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Cimetière de Picpus</strong> à 10 min à pied : fosses communes de la Terreur + <strong>tombe de La Fayette</strong>.",
            "<strong>Drapeau américain</strong> permanent sur la tombe de La Fayette. <strong>Cérémonie 4 juillet</strong> chaque année.",
            "Pour <strong>Nation</strong> et son hub multilignes : <strong>M6 directe</strong> (1 station).",
            "Pour <strong>Bois de Vincennes</strong> : <strong>M6 → Nation</strong> puis bus 56/86.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🇺🇸", "La Fayette, héros des deux mondes", "<strong>Gilbert du Motier, marquis de La Fayette</strong> (<strong>6 septembre 1757 - 20 mai 1834</strong>), <strong>héros de l'indépendance américaine</strong> et de la Révolution française. Engagé volontaire dans l'<strong>armée continentale</strong> de Washington en <strong>1777</strong>, il devient <strong>major-général</strong> à 19 ans. Acteur clé de la <strong>victoire de Yorktown</strong> (1781). Sa <strong>tombe</strong> au cimetière de Picpus est recouverte de <strong>terre américaine</strong> et ornée d'un <strong>drapeau américain</strong> en permanence. Chaque <strong>4 juillet</strong>, l'ambassade américaine y organise une cérémonie."),
            ("🪦", "Cimetière de Picpus, mémoire de la Terreur", "Le <strong>cimetière de Picpus</strong>, <strong>cimetière privé</strong> ouvert au public, abrite les <strong>fosses communes</strong> des <strong>1306 victimes</strong> de la <strong>Grande Terreur</strong> guillotinées entre le <strong>14 juin et le 27 juillet 1794</strong> sur la <strong>place du Trône-Renversé</strong> (place de la Nation). Les corps étaient transportés depuis la guillotine jusqu'à ces fosses dans le jardin d'un ancien couvent. Parmi les victimes : poètes, scientifiques, religieux, aristocrates.")
        ],
        "itin": [
            ("Nation", "nation", "M6", "M6 directe (1 station, terminus)", 2),
            ("Cimetière de Picpus", "nation", "à pied", "Boulevard de Picpus (10 min)", 10),
            ("Bel-Air", "bel-air", "M6", "M6 directe (1 station)", 2),
            ("Daumesnil", "daumesnil", "M6", "M6 directe (2 stations)", 4),
            ("Bois de Vincennes", "porte-doree", "M6 + bus", "M6 → Nation + bus 56", 12),
            ("Bercy", "bercy", "M6", "M6 directe (4 stations)", 8)
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
