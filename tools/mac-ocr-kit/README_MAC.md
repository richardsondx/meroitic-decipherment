# Rilly lexicon OCR, Mac kit

- What this does: OCRs the Rilly 2003 Vol. II lexicon PDF, pages 15 to 304, into text files, then parses them into a machine-readable lexicon JSON.
- Time: about 11 hours at the fastest measured rate, 133 seconds per page, on a free machine. It is resumable, so you can stop it and restart it, it skips pages already done.
- Your files are already in your Downloads folder, so nothing to download again.

## What you need

- The PDF, already in your Downloads folder: These Rilly EPHE 2003 Vol 2 Lexique meroitique.pdf
- Python 3.11 or newer, check with: python3 --version
- Homebrew, for poppler, check with: brew --version

## Setup, copy and paste these lines one at a time in Terminal

- Make a folder and move into it:
  - mkdir -p ~/rilly-lexicon && cd ~/rilly-lexicon
- Unzip the kit I sent you into that folder, so ocr_all.py, parse_lexicon.py, gold-sample-v1.json, pipeline.md, README_MAC.md, and run_mac.sh are all in ~/rilly-lexicon.
- Install the tools:
  - brew install poppler
  - python3 -m pip install rapidocr-onnxruntime
- Put the PDF in the folder, if it is not already there:
  - cp ~/Downloads/"These Rilly EPHE 2003 Vol 2 Lexique meroitique.pdf" ~/rilly-lexicon/rilly-2003-vol2-lexicon.pdf
- Check the PDF has no text layer, expect 1:
  - pdftotext -f 10 -l 10 rilly-2003-vol2-lexicon.pdf - | wc -c

## Test first, one page, about 2 minutes

- python3 ocr_all.py 15 15
- You should see: page 15: about 30 lines in about 133 seconds
- If that works, the full run will work.

## Full run

- Run it in the background so closing Terminal does not stop it:
  - nohup python3 ocr_all.py 15 304 > ocr-run.log 2>&1 &
- Or just run it in the foreground:
  - python3 ocr_all.py 15 304
- Watch progress:
  - tail -f ocr_progress.log
- Stop it any time with Ctrl-C. Restart it the same way, it skips pages already done.

## After OCR finishes, parse the lexicon

- python3 parse_lexicon.py
- This writes rilly-2003-lexicon-v0.1.json and parse_log.txt in the same folder.
- Spot check: compare parsed entries against gold-sample-v1.json, which holds 10 entries hand-read from the page images.

## Send the results back to me

- Send me these files from ~/rilly-lexicon:
  - rilly-2003-lexicon-v0.1.json
  - parse_log.txt
  - ocr_progress.log
- Or zip the whole ~/rilly-lexicon folder and send the zip.
- I will audit the entries against our 774-entry lexicon and report how many are new.

## If a page fails

- Note the page number from ocr_progress.log and keep going, the run skips it only if its file exists and is not empty.
- Do not edit the PDF or the scripts mid-run.
- If RapidOCR fails to install, tell me the exact error and I will fix the setup step.
