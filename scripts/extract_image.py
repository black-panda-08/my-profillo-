"""One-time utility: extract embedded images (e.g. profile photo) from the resume PDF.

Not part of the deployed website. Requires: pip install pymupdf
Run from anywhere:  python scripts/extract_image.py
"""
from pathlib import Path

import fitz
import sys

RESUME = Path(__file__).resolve().parent.parent / "Guru.pdf"

try:
    doc = fitz.open(str(RESUME))
    count = 0
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n - pix.alpha < 4:
                pix.save(f"profile_{count}.png")
            else:
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.save(f"profile_{count}.png")
                pix1 = None
            pix = None
            count += 1
    print(f"Extracted {count} images.")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
