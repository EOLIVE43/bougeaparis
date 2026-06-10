#!/usr/bin/env python3
"""Enrichit M10 Batch B — 3 stations en style ultra-sec (géographie + dates)."""
import json
from pathlib import Path
ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    "mirabeau": {
        "addr": "Quai Louis-Blériot, 75016 Paris",
        "arr": "16e arrondissement (Paris)",
        "seo": "Station Mirabeau (M10) quai Louis-Blériot dans le 16e arrondissement. À proximité du pont Mirabeau (1893-1896) sur la Seine.",
        "tagline": "M10 — pont Mirabeau, rive droite Seine",
        "hero_desc": "Station <strong>Mirabeau</strong> sur le <strong>quai Louis-Blériot</strong> dans le <strong>16e arrondissement</strong>. Desservie par la <strong>ligne 10 du métro</strong>, ouverte le <strong>30 septembre 1913</strong>. Située à proximité immédiate du <strong>pont Mirabeau</strong> (1893-1896), qui enjambe la Seine.",
        "intros": [
            "La station <strong>Mirabeau</strong> est implantée sur le <strong>quai Louis-Blériot</strong> dans le <strong>16e arrondissement</strong>, à l'extrémité ouest de Paris. Elle est desservie par la <strong>ligne 10 du métro parisien</strong>, entre <strong>Chardon-Lagache</strong> (1 station) et <strong>Javel - André Citroën</strong> (1 station). Bus 70 et 72 en correspondance.",
            "La station tire son nom du <strong>pont Mirabeau</strong>, situé à proximité immédiate. Quartier <strong>Auteuil</strong> rive droite de la Seine, atmosphère résidentielle du <strong>16e arrondissement</strong>."
        ],
        "hist_title": "1913 : ouverture et pont Mirabeau",
        "hist": [
            "La station Mirabeau est <strong>inaugurée le 30 septembre 1913</strong> sur le tronçon initial de la <strong>ligne 8</strong>. Intégrée à la <strong>ligne 10</strong> en <strong>1937</strong> lors du remaniement du réseau métro.",
            "La station est nommée d'après le <strong>pont Mirabeau</strong>, ouvrage métallique enjambant la Seine, <strong>construit de 1893 à 1896</strong>. Architectes : <strong>Paul Rabel</strong> et les ingénieurs <strong>Jean Résal</strong> et <strong>Amédée Alby</strong>. Le pont relie le <strong>quai Louis-Blériot</strong> (16e) au <strong>quai André-Citroën</strong> (15e). <strong>Inscrit aux monuments historiques en 1975</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Mirabeau ?", "Uniquement la <strong>M10</strong>. Bus 70 et 72."),
            ("Quand la station a-t-elle ouvert ?", "Le <strong>30 septembre 1913</strong>."),
            ("Pour le pont Mirabeau ?", "<strong>Sortie directe</strong>. Pont métallique (1893-1896), inscrit aux monuments historiques en 1975."),
            ("Pour Roland-Garros ?", "<strong>M10 → Porte d'Auteuil</strong> (5 stations, ~11 min)."),
            ("Pour le Quartier Latin ?", "<strong>M10 directe</strong> (~13 min)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station ancienne (1913), pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Pont Mirabeau</strong> à la sortie : ouvrage métallique 1893-1896.",
            "<strong>Berges de la Seine</strong> à proximité.",
            "Quartier <strong>Auteuil</strong> résidentiel du 16e.",
            "Pour <strong>Quartier Latin</strong> : <strong>M10 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🌉", "Pont Mirabeau, ouvrage métallique 1893-1896", "Le <strong>pont Mirabeau</strong>, à la sortie de la station, est un <strong>pont métallique</strong> enjambant la <strong>Seine</strong> entre le <strong>16e et le 15e arrondissement</strong>. <strong>Construit de 1893 à 1896</strong> par les architectes <strong>Paul Rabel</strong> et les ingénieurs <strong>Jean Résal</strong> et <strong>Amédée Alby</strong>. <strong>173 mètres de long</strong>, structure en <strong>trois arches métalliques</strong>. <strong>Inscrit aux monuments historiques le 29 avril 1975</strong>. L'un des <strong>plus connus de Paris</strong>."),
            ("📜", "Le poème d'Apollinaire (1913)", "Le <strong>pont Mirabeau</strong> est mentionné dans le <strong>célèbre poème</strong> <em>« Le Pont Mirabeau »</em> de <strong>Guillaume Apollinaire</strong>, publié dans son recueil <em>Alcools</em> en <strong>1913</strong>. Vers connus : <em>« Sous le pont Mirabeau coule la Seine / Et nos amours / Faut-il qu'il m'en souvienne »</em>. Le poème évoque le temps qui passe au-dessus du fleuve.")
        ],
        "itin": [
            ("Pont Mirabeau", "mirabeau", "à pied", "Sortie directe", 1),
            ("Javel - André Citroën", "javel-andre-citroen", "M10", "M10 directe (1 station)", 2),
            ("Chardon-Lagache", "chardon-lagache", "M10", "M10 directe (1 station)", 2),
            ("Roland-Garros", "porte-d-auteuil", "M10", "M10 directe (5 stations)", 11),
            ("Quartier Latin", "cluny-la-sorbonne", "M10", "M10 directe (~13 min)", 13),
            ("Gare d'Austerlitz", "gare-d-austerlitz", "M10", "M10 directe (terminus est)", 20)
        ]
    },
    "charles-michels": {
        "addr": "Rue Linois, 75015 Paris",
        "arr": "15e arrondissement (Paris)",
        "seo": "Station Charles Michels (M10) rue Linois dans le 15e arrondissement, quartier Beaugrenelle. Centre commercial Beaugrenelle à proximité.",
        "tagline": "M10 — quartier Beaugrenelle, centre commercial",
        "hero_desc": "Station <strong>Charles Michels</strong> sur la <strong>rue Linois</strong> dans le <strong>15e arrondissement</strong>, au cœur du <strong>quartier Beaugrenelle</strong>. Desservie par la <strong>ligne 10 du métro</strong>, ouverte le <strong>30 septembre 1913</strong>. À proximité du <strong>centre commercial Beaugrenelle</strong> et du <strong>Front de Seine</strong>.",
        "intros": [
            "La station <strong>Charles Michels</strong> est implantée sur la <strong>rue Linois</strong> dans le <strong>15e arrondissement</strong>, au sein du <strong>quartier Beaugrenelle</strong>. Elle est desservie par la <strong>ligne 10 du métro parisien</strong>, entre <strong>Javel - André Citroën</strong> (1 station) et <strong>Avenue Émile Zola</strong> (1 station). Bus 30, 39, 62, 88.",
            "Le quartier est marqué par le <strong>centre commercial Beaugrenelle</strong> et l'ensemble de tours résidentielles du <strong>Front de Seine</strong> (années 1970)."
        ],
        "hist_title": "1913 : station Beaugrenelle, renommée 1945",
        "hist": [
            "La station est <strong>inaugurée le 30 septembre 1913</strong> sous le nom <strong>« Beaugrenelle »</strong>, sur le tronçon initial de la <strong>ligne 8</strong>. Intégrée à la <strong>ligne 10</strong> en <strong>1937</strong>.",
            "Le <strong>27 octobre 1945</strong>, la station est <strong>renommée Charles Michels</strong>. Le quartier autour de la station a connu une <strong>profonde transformation urbaine</strong> dans les années 1970 avec l'édification du <strong>Front de Seine</strong> (ensemble de tours résidentielles le long du quai). Le <strong>centre commercial Beaugrenelle</strong>, inauguré en <strong>1979</strong>, a été <strong>entièrement rénové et rouvert en 2013</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Charles Michels ?", "Uniquement la <strong>M10</strong>. Bus 30, 39, 62, 88."),
            ("Quel était l'ancien nom ?", "<strong>« Beaugrenelle »</strong> de 1913 à 1945."),
            ("Quand a-t-elle ouvert ?", "Le <strong>30 septembre 1913</strong>, renommée en <strong>1945</strong>."),
            ("Pour le centre commercial Beaugrenelle ?", "<strong>~3 min à pied</strong>. Inauguré en 1979, rénové et rouvert en 2013."),
            ("Pour le Front de Seine ?", "<strong>Sortie directe</strong>. Ensemble de tours résidentielles (années 1970)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station ancienne (1913), pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Centre commercial Beaugrenelle</strong> à 3 min à pied (rénové 2013).",
            "<strong>Front de Seine</strong> : tours résidentielles des années 1970.",
            "<strong>Berges de la Seine</strong> à 5 min à pied.",
            "Pour <strong>La Motte-Picquet - Grenelle</strong> : <strong>M10 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🛍️", "Centre commercial Beaugrenelle (1979, rénové 2013)", "Le <strong>centre commercial Beaugrenelle</strong>, à 3 min à pied de la station, est inauguré en <strong>1979</strong> dans le cadre de l'opération d'urbanisme du <strong>Front de Seine</strong>. <strong>Entièrement rénové et rouvert le 23 octobre 2013</strong> après plusieurs années de travaux. <strong>120 boutiques</strong>, <strong>cinéma multiplexe</strong>, restaurants. Surface : <strong>50 000 m²</strong>. Architecture contemporaine intégrant la <strong>vue sur la Seine</strong>."),
            ("🏙️", "Front de Seine, urbanisme des années 1970", "Le <strong>Front de Seine</strong>, à proximité de la station, est un <strong>ensemble de tours résidentielles</strong> construites le long du <strong>quai André-Citroën</strong> dans les <strong>années 1970</strong>. <strong>20 tours</strong>, de <strong>33 étages</strong> en moyenne. Opération d'<strong>urbanisme de dalle</strong>, surélevée par rapport à la Seine. Architecture caractéristique des <strong>grands ensembles modernistes</strong>. Le quartier est aujourd'hui en pleine <strong>rénovation</strong>.")
        ],
        "itin": [
            ("Centre commercial Beaugrenelle", "charles-michels", "à pied", "Rue Linois (3 min)", 3),
            ("Front de Seine", "charles-michels", "à pied", "Quai André-Citroën", 5),
            ("Javel - André Citroën", "javel-andre-citroen", "M10", "M10 directe (1 station)", 2),
            ("Avenue Émile Zola", "avenue-emile-zola", "M10", "M10 directe (1 station)", 2),
            ("La Motte-Picquet - Grenelle", "la-motte-picquet-grenelle", "M10", "M10 directe (2 stations)", 4),
            ("Quartier Latin", "cluny-la-sorbonne", "M10", "M10 directe (~10 min)", 10)
        ]
    },
    "avenue-emile-zola": {
        "addr": "Avenue Émile-Zola, 75015 Paris",
        "arr": "15e arrondissement (Paris)",
        "seo": "Station Avenue Émile Zola (M10) avenue Émile-Zola dans le 15e arrondissement. Quartier Grenelle. Axe est-ouest du 15e.",
        "tagline": "M10 — avenue Émile-Zola, quartier Grenelle",
        "hero_desc": "Station <strong>Avenue Émile Zola</strong> sur l'<strong>avenue Émile-Zola</strong> dans le <strong>15e arrondissement</strong>. Desservie par la <strong>ligne 10 du métro</strong>, ouverte le <strong>30 décembre 1913</strong>. Située au cœur du <strong>quartier Grenelle</strong>, sous l'avenue éponyme qui traverse le <strong>15e arrondissement</strong> d'est en ouest.",
        "intros": [
            "La station <strong>Avenue Émile Zola</strong> est implantée sous l'<strong>avenue Émile-Zola</strong> dans le <strong>15e arrondissement</strong>. Elle est desservie par la <strong>ligne 10 du métro parisien</strong>, entre <strong>Charles Michels</strong> (1 station) et <strong>La Motte-Picquet - Grenelle</strong> (1 station). Bus 70 et 88 en correspondance.",
            "L'<strong>avenue Émile-Zola</strong>, longue de <strong>1,5 km</strong>, constitue un <strong>axe est-ouest</strong> du <strong>quartier Grenelle</strong>. Quartier résidentiel et commerçant du 15e arrondissement."
        ],
        "hist_title": "1913 : ouverture et avenue éponyme",
        "hist": [
            "La station est <strong>inaugurée le 30 décembre 1913</strong> sous le nom <strong>« Avenue Émile-Zola »</strong>, sur le tronçon initial de la <strong>ligne 8</strong>. Intégrée à la <strong>ligne 10</strong> en <strong>1937</strong>.",
            "L'<strong>avenue Émile-Zola</strong> est tracée en <strong>1864</strong> sous le nom de <strong>« rue de Grenelle Saint-Germain »</strong>. <strong>Renommée Avenue Émile-Zola</strong> le <strong>5 octobre 1908</strong>. Elle constitue l'un des <strong>principaux axes</strong> du quartier <strong>Grenelle</strong>, ancien village rattaché à Paris en <strong>1860</strong>."
        ],
        "faq": [
            ("Quelle ligne dessert Avenue Émile Zola ?", "Uniquement la <strong>M10</strong>. Bus 70 et 88."),
            ("Quand la station a-t-elle ouvert ?", "Le <strong>30 décembre 1913</strong>."),
            ("Quand l'avenue a-t-elle été renommée ?", "Le <strong>5 octobre 1908</strong> (ancien nom : rue de Grenelle Saint-Germain, tracée en 1864)."),
            ("Pour La Motte-Picquet - Grenelle (hub) ?", "<strong>M10 directe</strong> (1 station, ~2 min)."),
            ("Pour Beaugrenelle ?", "<strong>M10 → Charles Michels</strong> (1 station)."),
            ("La station est-elle accessible PMR ?", "<strong>Non</strong>. Station ancienne (1913), pas d'ascenseur.")
        ],
        "tips": [
            "<strong>Avenue Émile-Zola</strong> : axe est-ouest du quartier Grenelle.",
            "<strong>Quartier Grenelle</strong> : commerces, marché Grenelle.",
            "Pour <strong>Centre commercial Beaugrenelle</strong> : <strong>M10 → Charles Michels</strong>.",
            "Pour <strong>La Motte-Picquet - Grenelle</strong> (hub M6+M8+M10) : <strong>M10 directe</strong>.",
            "Zone tarifaire <strong>1</strong>, Paris intra-muros."
        ],
        "trivia": [
            ("🏘️", "Quartier Grenelle, ancien village", "Le <strong>quartier Grenelle</strong>, autour de la station, est l'un des <strong>anciens villages rattachés à Paris en 1860</strong>. Devient au <strong>XIXe siècle</strong> un <strong>quartier industriel et populaire</strong>. Aujourd'hui, quartier <strong>résidentiel et commerçant</strong> du <strong>15e arrondissement</strong>. <strong>Marché de Grenelle</strong> sur le <strong>boulevard de Grenelle</strong> (mercredi et dimanche matin)."),
            ("🛣️", "Avenue Émile-Zola, axe est-ouest du 15e", "L'<strong>avenue Émile-Zola</strong>, longue de <strong>1,5 km</strong>, est l'un des <strong>principaux axes du 15e arrondissement</strong>. Tracée en <strong>1864</strong> sous le nom de <strong>« rue de Grenelle Saint-Germain »</strong>, elle est <strong>renommée le 5 octobre 1908</strong>. Elle relie la <strong>rue du Théâtre</strong> à l'ouest au <strong>boulevard de Grenelle</strong> à l'est. Bordée de <strong>commerces de proximité</strong> et d'<strong>immeubles haussmanniens</strong>.")
        ],
        "itin": [
            ("La Motte-Picquet - Grenelle", "la-motte-picquet-grenelle", "M10", "M10 directe (1 station)", 2),
            ("Charles Michels", "charles-michels", "M10", "M10 directe (1 station)", 2),
            ("Centre commercial Beaugrenelle", "charles-michels", "M10", "M10 directe + à pied", 5),
            ("Tour Eiffel via Bir-Hakeim", "bir-hakeim", "M10 + M6", "M10 → La Motte-Picquet + M6", 10),
            ("Quartier Latin", "cluny-la-sorbonne", "M10", "M10 directe (~9 min)", 9),
            ("Gare d'Austerlitz", "gare-d-austerlitz", "M10", "M10 directe (terminus est)", 16)
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
