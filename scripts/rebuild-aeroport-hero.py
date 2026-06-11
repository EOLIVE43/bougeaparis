#!/usr/bin/env python3
"""Télécharge + crop 16:9 + génère 12 variantes AVIF/WebP/JPG (400/800/1200/1600).

Usage : python3 scripts/rebuild-aeroport-hero.py <slug> <wikimedia-filename>
Ex.   : python3 scripts/rebuild-aeroport-hero.py paris-orly "Paris Orly Terminal sud (44204798301).jpg"
"""
import sys, urllib.request, urllib.parse, subprocess
from pathlib import Path
from PIL import Image

UA = "BougeaParisBot/1.0 (https://bougeaparis.fr)"
ROOT = Path(__file__).parent.parent
SIZES = (400, 800, 1200, 1600)

def download(filename, dest):
    url = "https://commons.wikimedia.org/wiki/Special:FilePath/" + urllib.parse.quote(filename)
    print(f"Download: {url}")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
        f.write(r.read())
    print(f"  → {dest} ({dest.stat().st_size//1024} KB)")

def crop_16_9(src, dst):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    tw = 16 * h / 9
    if tw <= w:
        # crop horizontally
        x = (w - tw) // 2
        box = (x, 0, x + tw, h)
    else:
        # crop vertically
        th = 9 * w / 16
        y = (h - th) // 2
        box = (0, y, w, y + th)
    cropped = im.crop(box)
    cropped.save(dst, "JPEG", quality=92)
    print(f"  Cropped: {cropped.size[0]}x{cropped.size[1]} → {dst}")
    return dst

def gen_variants(master, slug, out_dir):
    im = Image.open(master)
    base_w = im.width
    for w in SIZES:
        if w > base_w:
            scaled = im.copy()
        else:
            h = round(im.height * w / im.width)
            scaled = im.resize((w, h), Image.LANCZOS)
        jpg_path = out_dir / f"{slug}-{w}.jpg"
        scaled.save(jpg_path, "JPEG", quality=85, optimize=True, progressive=True)
        webp_path = out_dir / f"{slug}-{w}.webp"
        subprocess.run(["cwebp","-q","82","-quiet",str(jpg_path),"-o",str(webp_path)],check=True)
        avif_path = out_dir / f"{slug}-{w}.avif"
        subprocess.run(["avifenc","-q","70","--speed","6",str(jpg_path),str(avif_path)],check=True,capture_output=True)
        print(f"  ✓ {w}px  jpg={jpg_path.stat().st_size//1024}K webp={webp_path.stat().st_size//1024}K avif={avif_path.stat().st_size//1024}K")

def main():
    if len(sys.argv) < 3:
        print("Usage: rebuild-aeroport-hero.py <slug> <wikimedia-filename>")
        sys.exit(1)
    slug, filename = sys.argv[1], sys.argv[2]
    out_dir = ROOT / "public_html" / "assets" / "img" / "aeroports" / slug
    src_dir = out_dir / "source"
    out_dir.mkdir(parents=True, exist_ok=True)
    src_dir.mkdir(parents=True, exist_ok=True)
    raw = src_dir / "wikimedia-raw.jpg"
    download(filename, raw)
    master = src_dir / "wikimedia.jpg"
    crop_16_9(raw, master)
    gen_variants(master, slug, out_dir)
    raw.unlink(missing_ok=True)
    print(f"\n✓ Done: {slug}")

if __name__ == "__main__":
    main()
