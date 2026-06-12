#!/usr/bin/env python3
"""Génère un PNG + WebP du tracé d'une ligne pour Google Images.

Usage : python3 scripts/generate-line-image.py t7
Dependencies : pip install matplotlib Pillow
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

data = json.loads(DATA.read_text())
stations = data["stations"]
color = data.get("color", "#0F6E56")
code = data["code"]

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("⚠ Installer : pip3 install matplotlib --break-system-packages")
    sys.exit(1)

lats = [s["lat"] for s in stations]
lngs = [s["lng"] for s in stations]
names = [s["name"] for s in stations]

fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
ax.plot(lngs, lats, color=color, linewidth=5, zorder=2,
        solid_capstyle="round", solid_joinstyle="round")

for i, (lat, lng, name, st) in enumerate(zip(lats, lngs, names, stations)):
    is_term = st.get("is_terminus", False)
    ax.scatter(lng, lat, s=240 if is_term else 140,
               color="white", edgecolors=color, linewidth=3 if is_term else 2, zorder=3)
    ax.annotate(name, (lng, lat),
                xytext=(0, 14 if i % 2 == 0 else -18), textcoords="offset points",
                ha="center",
                fontsize=10 if is_term else 8,
                fontweight="bold" if is_term else "normal",
                color="#1a1a1a",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="none", alpha=0.85))

ax.set_title(f"Plan ligne {code} — {names[0]} ↔ {names[-1]}",
             fontsize=14, fontweight="bold", pad=15)
ax.set_aspect("equal")
ax.axis("off")
plt.tight_layout()

def slugify(s):
    s = s.lower().replace(" - ", "-").replace(" ", "-").replace("'", "")
    s = (s.replace("é","e").replace("è","e").replace("ê","e")
           .replace("à","a").replace("î","i").replace("ç","c").replace("œ","oe"))
    return re.sub(r"-+","-", s).strip("-")

slug = f"{code.lower()}-trace-{slugify(names[0])}-{slugify(names[-1])}"
png = OUT / f"{slug}.png"
plt.savefig(png, dpi=110, bbox_inches="tight", facecolor="#F8FBFA", edgecolor="none", pil_kwargs={"optimize": True})
plt.close()
print(f"✓ PNG : {png}")

try:
    from PIL import Image
    webp = OUT / f"{slug}.webp"
    Image.open(png).save(webp, "WEBP", quality=82, method=6)
    saved = round((1 - webp.stat().st_size / png.stat().st_size) * 100)
    print(f"✓ WebP : {webp} (-{saved}%)")
except ImportError:
    print("⚠ Pillow non installé : skip WebP")
print(f"\nSlug : {slug}")
