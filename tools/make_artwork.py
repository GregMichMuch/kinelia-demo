"""Draws the demo posters (600 x 900) and channel logos (512 x 512).

Run: python3 tools/make_artwork.py <fonts_dir>
Fonts: Bricolage Grotesque and Instrument Sans (SIL Open Font License).
Posters are original abstract designs made for this demo, without any text (the app
writes the title itself): they contain no frame, logo or artwork from the films.
"""
import math
import random
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).parent))
from catalog import CHANNELS, FILMS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "posters"
FONTS = Path(sys.argv[1])
TITLE = str(FONTS / "BricolageGrotesque-700.ttf")
TEXT = str(FONTS / "InstrumentSans-500.ttf")
TEXT_B = str(FONTS / "InstrumentSans-700.ttf")

W, H = 600, 900


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def gradient(size, top, bottom):
    w, h = size
    img = Image.new("RGB", size)
    d = ImageDraw.Draw(img)
    for y in range(h):
        d.line([(0, y), (w, y)], fill=mix(top, bottom, y / (h - 1)))
    return img


def fit_font(draw, text, path, max_w, start, min_size=36):
    size = start
    while size > min_size:
        f = ImageFont.truetype(path, size)
        widest = max(draw.textlength(line, font=f) for line in text.split("\n"))
        if widest <= max_w:
            return f
        size -= 4
    return ImageFont.truetype(path, min_size)


def wrap_title(title):
    words = title.split()
    if len(title) <= 12 or len(words) == 1:
        return title
    best, best_score = title, 10 ** 9
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        score = abs(len(a) - len(b))
        if score < best_score:
            best, best_score = f"{a}\n{b}", score
    return best


def motif(layer, kind, c1, c2, c3, rnd):
    d = ImageDraw.Draw(layer)
    if kind == "grid":
        for x in range(-40, W + 40, 38):
            d.line([(x, 0), (x + 120, 640)], fill=c3 + (40,), width=1)
        for y in range(40, 640, 38):
            d.line([(0, y), (W, y - 30)], fill=c3 + (28,), width=1)
        d.ellipse([170, 150, 430, 410], outline=c3 + (220,), width=6)
        d.ellipse([255, 235, 345, 325], fill=c2 + (255,))
    elif kind == "orbits":
        for i, r in enumerate(range(60, 330, 45)):
            d.ellipse([300 - r, 330 - r * 0.45, 300 + r, 330 + r * 0.45], outline=c3 + (150 - i * 15,), width=3)
        d.ellipse([240, 270, 360, 390], fill=c2 + (255,))
        d.ellipse([440, 200, 470, 230], fill=c3 + (255,))
    elif kind == "split":
        d.rectangle([0, 0, W, H], fill=c1 + (255,))
        d.rectangle([0, 0, W // 2, 640], fill=c2 + (255,))
        d.ellipse([170, 160, 430, 420], fill=c1 + (255,))
        d.pieslice([170, 160, 430, 420], 0, 180, fill=c3 + (255,))
    elif kind == "strokes":
        for _ in range(22):
            x = rnd.randint(-100, W)
            y = rnd.randint(40, 600)
            d.line([(x, y), (x + rnd.randint(200, 420), y - rnd.randint(80, 220))],
                   fill=(c2 if rnd.random() > .35 else c3) + (rnd.randint(120, 230),), width=rnd.randint(3, 16))
    elif kind == "mountains":
        for i, (base, alpha) in enumerate([(520, 120), (580, 190), (640, 255)]):
            pts = [(0, H)]
            for x in range(0, W + 60, 60):
                pts.append((x, base - rnd.randint(40, 220) + i * 20))
            pts.append((W, H))
            d.polygon(pts, fill=mix(c2, c1, .25 + i * .3) + (alpha,))
        d.ellipse([400, 110, 500, 210], fill=c3 + (230,))
    elif kind == "rings":
        for r in range(260, 20, -34):
            d.ellipse([300 - r, 340 - r, 300 + r, 340 + r], outline=(c2 if r % 68 else c3) + (200,), width=10)
        d.ellipse([270, 310, 330, 370], fill=c3 + (255,))
    elif kind == "sun":
        d.rectangle([0, 0, W, H], fill=c1 + (255,))
        for a in range(0, 360, 15):
            x = 300 + math.cos(math.radians(a)) * 420
            y = 330 + math.sin(math.radians(a)) * 420
            d.polygon([(300, 330), (x, y), (x + 40, y + 40)], fill=c2 + (70,))
        d.ellipse([200, 230, 400, 430], fill=c2 + (255,))
        d.polygon([(120, 520), (300, 470), (480, 520), (300, 545)], fill=c3 + (255,))
    elif kind == "mandala":
        for k in range(12):
            a = math.radians(k * 30)
            x, y = 300 + math.cos(a) * 140, 330 + math.sin(a) * 140
            d.ellipse([x - 70, y - 70, x + 70, y + 70], outline=c2 + (220,), width=4)
        d.ellipse([220, 250, 380, 410], fill=c2 + (255,))
        d.ellipse([270, 300, 330, 360], fill=c3 + (255,))


def poster(film):
    c1, c2, c3 = (rgb(c) for c in film["palette"])
    rnd = random.Random(film["slug"])
    img = gradient((W, H), mix(c1, c3, .08), c1).convert("RGBA")
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    motif(layer, film["motif"], c1, c2, c3, rnd)
    img = Image.alpha_composite(img, layer)
    # bottom shade for text legibility
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shade)
    for y in range(560, H):
        sd.line([(0, y), (W, y)], fill=(0, 0, 0, int(200 * (y - 560) / (H - 560))))
    img = Image.alpha_composite(img, shade)
    # No text on the poster: the app writes the title over it.
    img.convert("RGB").save(OUT / f"{film['slug']}.jpg", quality=90)


def logo(ch):
    bg, fg = (rgb(c) for c in ch["colors"])
    img = Image.new("RGB", (512, 512), bg)
    d = ImageDraw.Draw(img)
    d.ellipse([56, 56, 456, 456], outline=fg, width=10)
    f = fit_font(d, ch["mark"], TITLE, 330, 120, 40)
    d.multiline_text((256, 256), ch["mark"], font=f, fill=fg, anchor="mm", align="center", spacing=4)
    img.save(OUT / f"{ch['logo']}.png")


if __name__ == "__main__":
    for film in FILMS:
        if not film.get("existing"):
            poster(film)
    for ch in CHANNELS:
        logo(ch)
    print("artwork written to", OUT)
