"""
Generate PDFs for all project notebooks.
Run from project root: python pdf_util.py

Requires: pip install "nbconvert[webpdf]" && playwright install chromium
"""
import subprocess
import os

NOTEBOOKS = [
    # Phase 1
    'notebooks/phase-1-proposal.ipynb',

    # Phase 2
    'notebooks/phase-2-cause-code-eda.ipynb',

    # Phase 3 - Baselines
    'notebooks/phase-3-log-reg-modeling.ipynb',
    'notebooks/phase-3-rand-forest-modeling.ipynb',
    'notebooks/phase-3-arm-cba-modeling.ipynb',

    # Phase 3 - Tuning
    'notebooks/lr-tuning-experiments.ipynb',
    'notebooks/rf-tuning-experiments.ipynb',
    'notebooks/cba-tuning-experiments.ipynb',

    # Phase 3 - Final
    'notebooks/final-evaluation.ipynb',
]

OUTPUT_DIR = 'pdfs'

if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    success = 0
    failed = 0

    for nb in NOTEBOOKS:
        if not os.path.exists(nb):
            print(f"SKIP: {nb} not found")
            continue

        print(f"Converting: {nb}")
        result = subprocess.run([
            'jupyter', 'nbconvert',
            '--to', 'webpdf',
            '--output-dir', OUTPUT_DIR,
            nb
        ], capture_output=True, text=True)

        if result.returncode == 0:
            print(f"  OK")
            success += 1
        else:
            print(f"  FAILED: {result.stderr[:200]}")
            failed += 1

    print(f"\nDone. {success} converted, {failed} failed.")
    print(f"PDFs in {OUTPUT_DIR}/")
