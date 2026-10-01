"""E02 images. Input: folder with the raw Commons download; output: ../assets/.
Other images (cajal, brain_*) are reused from E01 (copied server-side between the two artifacts)."""
import sys, pathlib
from PIL import Image, ImageEnhance

SRC = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)
im = Image.open(SRC / "Socrates_Louvre.jpg").convert("RGB")
im = ImageEnhance.Brightness(ImageEnhance.Contrast(im).enhance(1.1)).enhance(0.92)
im.save(OUT / "socrates.jpg", quality=88)
print(sorted(p.name for p in OUT.iterdir()))
