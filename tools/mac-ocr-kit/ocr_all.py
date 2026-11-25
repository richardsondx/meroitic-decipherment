#!/usr/bin/env python3
"""Batch OCR for Rilly 2003 Vol. II lexicon (scanned pages, no text layer).

Source images are the embedded JPEGs in raw/img/page-NNN-XXX.jpg, one full
page scan per PDF page (largest JPEG per page wins; page 3 has two).
Writes raw/page_NNN.ocr.txt, one line per OCR line: "<conf>\\t<text>",
sorted top-to-bottom, left-to-right. Skips pages already OCR'd, so the
run is resumable. Usage:
    python3 ocr_all.py [first_page] [last_page]
Defaults: 4 to 304. Pages 1-3 have a real text layer (HAL cover) and are skipped.
"""
import glob
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = HERE / "raw"
IMG = RAW / "img"


def page_image(pdf_page: int):
    """Largest embedded JPEG for a PDF page, or None."""
    cands = glob.glob(str(IMG / f"page-{pdf_page:03d}-*.jpg"))
    if not cands:
        return None
    return max(cands, key=lambda f: os.path.getsize(f))


def main():
    first = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    last = int(sys.argv[2]) if len(sys.argv) > 2 else 304
    from rapidocr_onnxruntime import RapidOCR
    eng = RapidOCR(use_angle_cls=False)
    log = open(HERE / "ocr_progress.log", "a")
    for p in range(first, last + 1):
        out = RAW / f"page_{p:03d}.ocr.txt"
        if out.exists() and out.stat().st_size > 0:
            continue
        img = page_image(p)
        if img is None:
            print(f"page {p}: no image, skipped", flush=True)
            continue
        t0 = time.time()
        result, _ = eng(img)
        lines = []
        for box, text, conf in (result or []):
            y = sum(pt[1] for pt in box) / 4.0
            x = sum(pt[0] for pt in box) / 4.0
            lines.append((y, x, conf, text))
        lines.sort(key=lambda t: (round(t[0] / 20), t[1]))
        with open(out, "w") as f:
            for _, _, conf, text in lines:
                f.write(f"{conf:.2f}\t{text}\n")
        msg = f"page {p}: {len(lines)} lines in {time.time() - t0:.1f}s"
        print(msg, flush=True)
        log.write(msg + "\n")
        log.flush()
    log.close()
    print("OCR batch done", flush=True)


if __name__ == "__main__":
    main()
