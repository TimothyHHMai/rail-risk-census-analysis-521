# AI Usage Documentation: Final Evaluation

## Overview
- **Date:** 2026-02-28
- **Notebook:** `notebooks/final-evaluation.ipynb`
- **Author:** Phillip Roman
- **AI Tool:** Claude AI (Anthropic - Opus 4.6)
- **Course:** DSCI 521, Drexel University

## Author Contributions
- Designed the final evaluation as a single notebook that loads all three tuned models and runs them on the locked test set
- Test set opened for the first time in this notebook - no model selection or tuning decisions were influenced by test data
- Chose to compare LR, RF, and CBA side-by-side on same test data
- Selected evaluation sections: summary table (CV vs test F1), per-class F1 comparison, confusion matrices, PR curves, error analysis, Accident Type impact summary
- Designed error analysis to examine model agreement and shared errors
- Included CBA rule interpretability section to highlight CBA's unique operational value
- Chose paired t-test on CV fold scores with Bonferroni correction for statistical comparison between models
- Chose colorblind-friendly plotting style (tableau-colorblind10)

## AI Contributions
- Coded model loading and test set prediction generation
- Coded per-class metrics extraction and grouped bar chart
- Coded 1x3 confusion matrix grid
- Coded PR curves per cause category for LR and RF
- Coded model agreement and shared error analysis
- Coded Accident Type impact comparison table (loading baseline JSONs)
- Coded JSON results save formatting for test results
- Chose axis labels, scales, and formatting for plots
- CBAClassifier class copied from cba-tuning-experiments.ipynb to enable pickle loading

## AI-Recommended Analysis
- PR curves as additional evaluation beyond confusion matrices
- Model agreement analysis examining where all three models agree vs disagree

## Modifications After Generation
- All code cells initially commented out to prevent accidental test set access before team review
- Uncommented and ran with teammate Dave present
- Added CBAClassifier class definition to setup for pickle compatibility
- Verified notebook runs end-to-end after all modifications
