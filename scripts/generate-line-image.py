#!/usr/bin/env python3
"""Génère PNG + WebP haute qualité du tracé d'une ligne avec watermark BougeaParis.

Style header inspiré de metroparis.paris :
  • Logo carré teal "B" blanc (haut-gauche)
  • "BougeaParis" noir gras + ".fr" teal
  • Séparateur vertical gris
  • Titre du plan centré
  • Compteur stations à droite

Usage : python3 scripts/generate-line-image.py t7
Deps  : pip install matplotlib Pillow
"""
import sys, json, re
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: generate-line-image.py <line_code>")
    sys.exit(1)

CODE = sys.argv[1].lower()
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / f"public_html/data/lines-tram/{CODE}.json"
OUT  = ROOT / "public_html/assets/images/lines"
OUT.mkdir(parents=True, exist_ok=True)

# Charte BougeaParis
TEAL = "#0F6E56"
DARK = "#1a1a1a"
GRAY = "#cccccc"
BG   = "#FFFFFF"

data = json.loads(DATA.read_text())
stations = data["stations"]
color = data.get("color", TEAL)
code = data["code"]
n = len(stations)

try:
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch
except ImportError:
    print("⚠ Installer : pip3 install matplotlib --break-system-packages")
    sys.exit(1)

lats = [s["lat"] for s in stations]
lngs = [s["lng"] for s in stations]
names = [s["name"] for s in stations]

# Figure 1200x675 (16:9 Discover optimal)
fig = plt.figure(figsize=(12, 6.75), dpi=100, facecolor=BG)

# === HEADER (12% top) — watermark style metroparis.paris ===
header_ax = fig.add_axes([0, 0.88, 1, 0.12])
header_ax.set_xlim(0, 100); header_ax.set_ylim(0, 10)
header_ax.axis("off")

# Logo carré teal "B"
logo_size = 6
logo_x = 1.2; logo_y = 2
header_ax.add_patch(FancyBboxPatch(
    (logo_x, logo_y), logo_size, logo_size,
    boxstyle="round,pad=0.15",
    facecolor=TEAL, edgecolor="none", zorder=2,
))
header_ax.text(logo_x + logo_size/2, logo_y + logo_size/2, "B",
               ha="center", va="center",
               fontsize=24, fontweight="bold", color="white", zorder=3)

# "BougeaParis" + ".fr" — calcul bbox dynamique pour éviter superposition
text_x = logo_x + logo_size + 1.5
text_main = header_ax.text(text_x, 5, "BougeaParis", ha="left", va="center",
                            fontsize=15, fontweight="bold", color=DARK)

# Forcer rendu intermédiaire pour mesurer la bbox réelle
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
inv = header_ax.transData.inverted()

bbox_main = text_main.get_window_extent(renderer=renderer).transformed(inv)
fr_x = bbox_main.x1 + 0.2

text_fr = header_ax.text(fr_x, 5, ".fr", ha="left", va="center",
                          fontsize=15, fontweight="bold", color=TEAL)
fig.canvas.draw()
bbox_fr = text_fr.get_window_extent(renderer=renderer).transformed(inv)

# Séparateur vertical gris discret après ".fr"
sep_x = bbox_fr.x1 + 1.5
header_ax.plot([sep_x, sep_x], [1.8, 8.2], color=GRAY, linewidth=1, zorder=1)

# Titre du plan centré
title = f"Plan ligne {code} — {names[0]} ↔ {names[-1]}"
header_ax.text(50, 5, title, ha="center", va="center",
               fontsize=13, fontweight="bold", color=DARK)

# Compteur stations droite
header_ax.text(98.5, 5, f"{n} stations", ha="right", va="center",
               fontsize=11, fontweight="600", color="#666")

# === ZONE CARTE (sous header) ===
map_ax = fig.add_axes([0.02, 0.03, 0.96, 0.83])

map_ax.plot(lngs, lats, color=color, linewidth=5, zorder=2,
            solid_capstyle="round", solid_joinstyle="round")

for i, (lat, lng, name, st) in enumerate(zip(lats, lngs, names, stations)):
    is_term = st.get("is_terminus", False)
    map_ax.scatter(lng, lat,
                   s=240 if is_term else 140,
                   color="white", edgecolors=color,
                   linewidth=3 if is_term else 2, zorder=3)
    map_ax.annotate(name, (lng, lat),
                    xytext=(0, 14 if i % 2 == 0 else -18),
                    textcoords="offset points", ha="center",
                    fontsize=10 if is_term else 8,
                    fontweight="bold" if is_term else "normal",
                    color=DARK,
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                              edgecolor="none", alpha=0.85))

map_ax.set_aspect("equal")
map_ax.axis("off")

# === SAUVEGARDE ===
def slugify(s):
    s = s.lower().replace(" - ", "-").replace(" ", "-").replace("'", "")
    s = (s.replace("é","e").replace("è","e").replace("ê","e")
           .replace("à","a").replace("î","i").replace("ç","c").replace("œ","oe"))
    return re.sub(r"-+", "-", s).strip("-")

slug = f"{code.lower()}-trace-{slugify(names[0])}-{slugify(names[-1])}"
png = OUT / f"{slug}.png"
plt.savefig(png, dpi=110, bbox_inches="tight",
            facecolor=BG, edgecolor="none",
            pil_kwargs={"optimize": True})
plt.close()
print(f"✓ PNG  : {png} ({png.stat().st_size//1024} KB)")

try:
    from PIL import Image
    webp = OUT / f"{slug}.webp"
    Image.open(png).save(webp, "WEBP", quality=82, method=6)
    pct = round((1 - webp.stat().st_size / png.stat().st_size) * 100)
    print(f"✓ WebP : {webp} ({webp.stat().st_size//1024} KB, -{pct}%)")
except ImportError:
    print("⚠ Pillow non installé : skip WebP")

print(f"\nSlug : {slug}")
print(f"Watermark : BougeaParis.fr (style metroparis.paris)")
