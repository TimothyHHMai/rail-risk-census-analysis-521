# AI Usage Documentation: CBA Tuning Experiments

## Overview
- **Date:** 2026-02-27
- **Notebook:** `notebooks/cba-tuning-experiments.ipynb`
- **Author:** Phillip Roman
- **AI Tool:** Claude AI (Anthropic - Opus 4.6)
- **Course:** DSCI 521, Drexel University

## Author Contributions
- Designed 3 experiments addressing CBA's class imbalance problem
- Experiment 1: Removed Accident Type, kept same thresholds as baseline to measure CBA-specific drop
- Experiment 2: Introduced undersampling before rule mining to give minority classes (Signal, Environmental) equal representation
- Experiment 3: Specified threshold grid search across 4 support levels and 3 confidence levels (12 configurations)
- Decided that undersampling happens only during rule mining, evaluation stays on original imbalanced data
- Chose to save tuned rules as CSV artifacts for reproducibility
- Selected weighted F1 as primary metric, per-class precision/recall as secondary, confusion matrix as tertiary
- Chose colorblind-friendly plotting style (tableau-colorblind10)

## AI Contributions
- Coded the CBAClassifier with undersample parameter added to fit() method
- Coded the threshold grid search loop
- Coded the cross-validation loop with score collection
- Coded per-class metrics extraction, confusion matrix plotting, CV comparison chart
- Coded rule export to CSV formatting
- Coded JSON results save/load formatting
- Chose axis labels, scales, and formatting for plots
- Discussed best graph types for presenting results

## AI-Recommended Analysis
- None for this notebook

## Modifications After Generation
- Fixed JSON key references to match standardized format (cv_mean, cv_scores)
- Verified notebook runs end-to-end after all modifications
