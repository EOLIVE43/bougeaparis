#!/usr/bin/env python3
"""Enrichit M1 — La Défense (terminus ouest, dernier hub manquant)."""
import json
from pathlib import Path
ROOT = Path(__file__).parent.parent
STATIONS = ROOT / "public_html" / "data" / "stations"

CONTENT = {
    "la-defense": {
        "addr": "Esplanade de La Défense, 92800 Puteaux", "arr": "Puteaux (92)",
        "seo": "Station La Défense (M1+RER A+Transilien L+T2), terminus ouest M1 dans le quartier d'affaires La Défense. Grande Arche, CNIT, centre commercial Westfield Les 4 Temps.",
        "tagline": "M1 + RER A + Transilien L + T2 — terminus ouest, La Défense",
        "hero_desc": "Station <strong>La Défense</strong>, <strong>terminus ouest de la M1</strong>, dans le <strong>quartier d'affaires de La Défense</strong> à <strong>Puteaux</strong> (Hauts-de-Seine, 92). Hub multimodal majeur : <strong>M1, RER A, Transilien L, tramway T2</strong>. Ouverte le <strong>1er avril 1992</strong>. À proximité de la <strong>Grande Arche de la Défense</strong> (1989) et du <strong>centre commercial Westfield Les 4 Temps</strong>.",
        "intros": [
            "La station <strong>La Défense</strong> est le <strong>terminus ouest de la M1</strong>, située dans le <strong>quartier d'affaires de La Défense</strong> à <strong>Puteaux</strong> (Hauts-de-Seine, 92). Elle est l'un des <strong>hubs multimodaux les plus importants d'Île-de-France</strong> : <strong>M1, RER A, Transilien L, tramway T2</strong>. Bus 73, 144, 158, 159, 174, 178, 258, 262, 272, 278, 360, 367.",
            "Quais <strong>M1</strong> ouverts le <strong>1er avril 1992</strong> avec le prolongement de la ligne de <strong>Pont de Neuilly à La Défense</strong>. Quais <strong>RER A</strong> ouverts dès <strong>1970</strong>, prolongés en 1973.",
            "Le quartier d'affaires de <strong>La Défense</strong> est le <strong>premier quartier d'affaires d'Europe</strong> par sa surface (~3,5 millions de m² de bureaux). Aménagé à partir de <strong>1958</strong>, il accueille plus de <strong>180 000 salariés</strong>. À la sortie : la <strong>Grande Arche</strong> (1989, Otto von Spreckelsen), le <strong>CNIT</strong> (1958), le <strong>centre commercial Westfield Les 4 Temps</strong> (1981, plus de 250 boutiques)."
        ],
        "hist_title": "1992 : terminus M1 et quartier d'affaires européen",
        "hist": [
            "La station La Défense est <strong>inaugurée le 1er avril 1992</strong> avec le <strong>prolongement de la M1</strong> de <strong>Pont de Neuilly à La Défense - Grande Arche</strong>. Ce <strong>prolongement</strong> termine la <strong>M1</strong> sur l'<strong>axe historique royal</strong> qui relie le <strong>Louvre</strong> à la <strong>Grande Arche</strong>.",
            "Le quartier de <strong>La Défense</strong> tire son nom de la <strong>statue La Défense de Paris</strong> érigée en <strong>1883</strong> pour commémorer la <strong>défense de Paris lors de la guerre franco-prussienne de 1870-1871</strong>. Aménagé comme <strong>quartier d'affaires</strong> à partir de <strong>1958</strong> sous l'impulsion de l'<strong>EPAD</strong> (Établissement public d'aménagement de la Défense). <strong>Premier quartier d'affaires d'Europe</strong> par sa surface.",
            "La <strong>Grande Arche de la Défense</strong>, à 5 min à pied, est inaugurée le <strong>14 juillet 1989</strong> pour le <strong>bicentenaire de la Révolution française</strong>. Œuvre de l'architecte danois <strong>Otto von Spreckelsen</strong> et de l'ingénieur <strong>Erik Reitzel</strong>. <strong>Cube creux</strong> de <strong>110 m de côté</strong>, recouvert de <strong>marbre de Carrare</strong>. Située dans l'<strong>axe historique parisien</strong> (Louvre - Champs-Élysées - Arc de Triomphe - Grande Arche)."
        ],
        "faq": [
            ("Quelles lignes desservent La Défense ?", "<strong>M1</strong> (terminus ouest), <strong>RER A</strong>, <strong>Transilien L</strong>, <strong>tramway T2</strong>. Bus 73, 144, 158, 159, 174, 178, 258, 262, 272, 278, 360, 367."),
            ("Quand a-t-elle ouvert ?", "Quais M1 : <strong>1er avril 1992</strong>. Quais RER A : <strong>1970</strong>."),
            ("Pour la Grande Arche ?", "<strong>~5 min à pied</strong> via le parvis. Cube creux de 110 m (1989, Otto von Spreckelsen)."),
            ("Pour Westfield Les 4 Temps ?", "<strong>Sortie directe</strong>. Plus de 250 boutiques, hypermarché Auchan."),
            ("Pour le CNIT ?", "<strong>~3 min à pied</strong>. Bâtiment 1958, voûte la plus large du monde à l'époque."),
            ("La station est-elle accessible PMR ?", "<strong>Oui</strong>. Ascenseurs et tapis roulants.")
        ],
        "tips": [
            "<strong>Grande Arche</strong> à 5 min à pied : cube creux de 110 m, axe historique parisien.",
            "<strong>Westfield Les 4 Temps</strong> à la sortie : plus de 250 boutiques, hypermarché Auchan, restaurants.",
            "<strong>CNIT</strong> à 3 min à pied : centre des nouvelles industries et technologies (1958).",
            "Pour <strong>Étoile et Champs-Élysées</strong> : <strong>M1 directe</strong> (~10 min).",
            "Zone tarifaire <strong>3</strong>, Hauts-de-Seine."
        ],
        "trivia": [
            ("🏛️", "Grande Arche de la Défense (1989)", "La <strong>Grande Arche de la Défense</strong>, à 5 min à pied, est inaugurée le <strong>14 juillet 1989</strong> pour le <strong>bicentenaire de la Révolution française</strong> par le président <strong>François Mitterrand</strong>. Œuvre de l'architecte danois <strong>Otto von Spreckelsen</strong> et de l'ingénieur <strong>Erik Reitzel</strong>. <strong>Cube creux</strong> de <strong>110 m de côté</strong>, <strong>110 m de haut</strong>, recouvert de <strong>marbre de Carrare</strong>. Située dans l'<strong>axe historique parisien</strong> qui relie le Louvre à la Grande Arche sur 8 km. Symbole moderne de l'<strong>axe royal</strong>."),
            ("🏢", "La Défense, premier quartier d'affaires d'Europe", "Le quartier de <strong>La Défense</strong>, à la sortie, est le <strong>premier quartier d'affaires d'Europe</strong> par sa surface (<strong>~3,5 millions de m² de bureaux</strong>). Aménagé à partir de <strong>1958</strong> sous l'impulsion de l'<strong>EPAD</strong>. <strong>Plus de 180 000 salariés</strong>, 500 entreprises, 1 500 sièges sociaux d'entreprises françaises et internationales. Tours emblématiques : <strong>Tour First</strong> (231 m, plus haute de France hors Tour Eiffel), <strong>Tour Majunga</strong>, <strong>Tour D2</strong>, <strong>Tour Saint-Gobain</strong>.")
        ],
        "itin": [
            ("Grande Arche", "la-defense", "à pied", "Parvis (5 min)", 5),
            ("Westfield Les 4 Temps", "la-defense", "à pied", "Sortie directe", 2),
            ("CNIT", "la-defense", "à pied", "Parvis (3 min)", 3),
            ("Charles de Gaulle - Étoile", "charles-de-gaulle-etoile", "M1", "M1 directe (~10 min)", 10),
            ("Champs-Élysées", "george-v", "M1", "M1 directe (~12 min)", 12),
            ("Châtelet", "chatelet", "M1", "M1 directe (~22 min)", 22)
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
    d["tariff_zone"] = 3
    d["tariff_zone_context"] = "Hauts-de-Seine (92), zone tarifaire 3"
    d["commune"] = "Puteaux"
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
