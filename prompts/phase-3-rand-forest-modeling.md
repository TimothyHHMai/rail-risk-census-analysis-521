# AI Usage Documentation: Random Forest Baseline

## Overview
- **Date:** 2026-02-27
- **Notebook:** `notebooks/phase-3-rand-forest-modeling.ipynb`
- **Author:** Phillip Roman
- **AI Tool:** Claude AI (Anthropic - Opus 4.6)
- **Course:** DSCI 521, Drexel University

## Author Contributions
- Selected same 6 features as LR baseline for direct comparison
- Chose Random Forest as the nonlinear benchmark to test whether complex modeling could beat LR's linear boundaries
- Chose to test both default and class-weighted configurations
- Chose OrdinalEncoder over OneHotEncoder for tree-based model
- Chose 5-fold stratified cross-validation with random_state=521
- Selected weighted F1 as primary metric, per-class precision/recall as secondary, confusion matrix as tertiary
- Chose to include Accident Type in baseline for later comparison
- Included feature importance analysis to see which features RF relies on most
- Chose colorblind-friendly plotting style (tableau-colorblind10)

## AI Contributions
- Coded the sklearn pipeline (ColumnTransformer with OrdinalEncoder)
- Coded the cross-validation loop with score collection
- Coded per-class metrics extraction, confusion matrix plotting, CV comparison chart
- Coded feature importance extraction and bar chart
- Coded JSON results save/load formatting
- Chose axis labels, scales, and formatting for plots
- Discussed best graph types for presenting results

## AI-Recommended Analysis
- None for this notebook

## Modifications After Generation
- Updated JSON save cell to standardized format matching tuning experiments
- Updated save path from `../results/` to `../results/rf/`
- Renamed Gini importance references to Feature Importance throughout
- Removed Cramer's V references (analysis lives in ARM-CBA baseline)
- Verified notebook runs end-to-end after all modifications
