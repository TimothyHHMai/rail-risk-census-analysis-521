# AI Usage Documentation: Logistic Regression Baseline

## Overview
- **Date:** 2026-02-27
- **Notebook:** `notebooks/phase-3-log-reg-modeling.ipynb`
- **Author:** Phillip Roman
- **AI Tool:** Claude AI (Anthropic - Opus 4.6)
- **Course:** DSCI 521, Drexel University

## Author Contributions
- Selected 6 features from Phase 2 EDA validated through Chi-Square independence tests
- Chose Logistic Regression as the linear baseline model
- Chose to test both default and class-weighted configurations
- Chose 5-fold stratified cross-validation with random_state=521
- Selected weighted F1 as primary metric, per-class precision/recall as secondary, confusion matrix as tertiary
- Chose to include Accident Type in baseline for later comparison
- Specified one-hot encoding for categorical features, standard scaling for numeric
- Chose colorblind-friendly plotting style (tableau-colorblind10)

## AI Contributions
- Coded the sklearn pipeline (ColumnTransformer with OneHotEncoder and StandardScaler)
- Coded the cross-validation loop with score collection
- Coded per-class metrics extraction, confusion matrix plotting, CV comparison chart
- Coded JSON results save/load formatting
- Chose axis labels, scales, and formatting for plots
- Discussed best graph types for presenting results

## AI-Recommended Analysis
- None for this notebook

## Modifications After Generation
- Updated JSON save cell to standardized format matching tuning experiments
- Updated save path from `../results/` to `../results/lr/`
- Removed Cramer's V references (analysis lives in ARM-CBA baseline)
- Verified notebook runs end-to-end after all modifications
