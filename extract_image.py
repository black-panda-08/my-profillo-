import fitz
import sys

try:
    doc = fitz.open("Chellaguru_G_Resume.pdf")
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
