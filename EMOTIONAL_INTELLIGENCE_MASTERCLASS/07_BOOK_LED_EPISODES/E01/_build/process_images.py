"""Process downloaded public-domain images into the episode's look. Input: scratchpad/img; output: ../assets/*.png|jpg"""
import sys, pathlib
from PIL import Image, ImageOps, ImageFilter, ImageEnhance

SRC = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)
NAVY = (14, 21, 34)


def tint_lines(img, color, bg=None, threshold=200):
    """Dark strokes -> color with alpha; light paper -> transparent (or bg)."""
    g = ImageOps.grayscale(img.convert("RGBA").convert("RGB"))
    alpha = ImageOps.invert(g).point(lambda v: 0 if v < 255 - threshold else min(255, int(v * 1.6)))
    if img.mode == "RGBA":
        a0 = img.split()[3]
        alpha = Image.composite(alpha, Image.new("L", img.size, 0), a0)
    layer = Image.new("RGBA", img.size, color + (255,))
    layer.putalpha(alpha)
    if bg:
        base = Image.new("RGBA", img.size, bg + (255,))
        base.alpha_composite(layer)
        return base
    return layer


# Aristotle: crop to head and shoulders, keep marble color
a = Image.open(SRC / "Aristotle_Altemps_Inv8575.jpg").convert("RGB")
a = ImageEnhance.Contrast(a).enhance(1.08)
a.save(OUT / "aristotle.jpg", quality=88)

# Cajal: teal neurons on navy
c = Image.open(SRC / "Cajal_cortex_drawings.png").convert("RGB")
tint_lines(c, (79, 189, 176), NAVY, 180).convert("RGB").save(OUT / "cajal.jpg", quality=86)

# Brain (Gray 728, lobes): amber contour art on transparent + teal mirrored variant
b = Image.open(SRC / "Gray728.svg.png").convert("RGBA")
edges = ImageOps.grayscale(b.convert("RGB")).filter(ImageFilter.FIND_EDGES)
edges = ImageOps.autocontrast(edges).point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(3))
amber = Image.new("RGBA", b.size, (242, 165, 65, 255)); amber.putalpha(edges)
amber.save(OUT / "brain_lateral.png")
teal = Image.new("RGBA", b.size, (79, 189, 176, 255)); teal.putalpha(edges)
teal.save(OUT / "brain_medial.png")
# full-colour lobes version (frontal lobe visible) for the 'brakes' idea
b.save(OUT / "brain_lobes.png")

# Vitruvian Man: crop the figure (drop the handwriting margins)
v = Image.open(SRC / "Da_Vinci_Vitruve_Luc_Viatour.jpg").convert("RGB")
W, H = v.size
v.crop((int(W * 0.06), int(H * 0.11), int(W * 0.94), int(H * 0.80))).save(OUT / "vitruvian.jpg", quality=88)

# Telephone (CC0)
Image.open(SRC / "Rotary_dial_Telephone_black.jpg").convert("RGB").save(OUT / "telephone.jpg", quality=90)
print(sorted(p.name for p in OUT.iterdir()))
