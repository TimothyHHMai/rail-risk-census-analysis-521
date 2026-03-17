"""
Generate PDFs for all project notebooks.
Run from project root: python pdf_util.py

Requires: pip install "nbconvert[webpdf]" && playwright install chromium
"""
import subprocess
import os

NOTEBOOKS = [
    # Phase 1
    'notebooks/shared/01_proposal_shared.ipynb',

    # Phase 2
    'notebooks/shared/02_eda_shared.ipynb',

    # Phase 3 - Baselines
    'notebooks/classification/03a_log_reg_baseline.ipynb',
    'notebooks/classification/03b_arm_cba_baseline.ipynb',
    'notebooks/classification/03c_rand_forest_baseline.ipynb',

    # Phase 4 - Tuning
    'notebooks/classification/04a_log_reg_tuning.ipynb',
    'notebooks/classification/04b_arm_cba_tuning.ipynb',
    'notebooks/classification/04c_rand_forest_tuning.ipynb',

    # Phase 5 - Final
    'notebooks/classification/05_final_classification_eval.ipynb',
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
