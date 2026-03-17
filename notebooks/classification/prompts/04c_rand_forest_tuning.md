# AI Usage Documentation: Random Forest Tuning Experiments

## Overview
- **Date:** 2026-02-27
- **Notebook:** `notebooks/rf-tuning-experiments.ipynb`
- **Author:** Phillip Roman
- **AI Tool:** Claude AI (Anthropic - Opus 4.6)
- **Course:** DSCI 521, Drexel University

## Author Contributions
- Designed 3 experiments for RF tuning
- Experiment 1: Removed Accident Type using same locked feature set from LR tuning
- Experiment 2: Analyzed feature importance redistribution after Accident Type removal
- Experiment 3: Specified GridSearchCV with 216 configurations across tree count, depth, leaf size, feature sampling, and class weighting
- Feature selection decisions (Track Type, RUCC encoding) carried forward from LR tuning - no need to re-test on RF
- Chose to compare feature importance rankings against Phase 2 Chi-Square results
- Chose colorblind-friendly plotting style (tableau-colorblind10)

## AI Contributions
- Coded the sklearn pipeline (ColumnTransformer with OrdinalEncoder)
- Coded the cross-validation loop with score collection
- Coded feature importance extraction and side-by-side bar charts
- Coded GridSearchCV implementation (216 configurations)
- Coded per-class metrics extraction, confusion matrix plotting, CV comparison chart
- Coded JSON results save/load formatting
- Chose axis labels, scales, and formatting for plots
- Discussed best graph types for presenting results

## AI-Recommended Analysis
- Feature importance redistribution as a standalone experiment to visualize how importance shifts after removing the dominant variable

## Modifications After Generation
- Renamed Gini importance references to Feature Importance throughout
- Removed Cramer's V references (replaced with Chi-Square from Phase 2)
- Fixed JSON key references to match standardized format (cv_mean, cv_scores)
- Verified notebook runs end-to-end after all modifications
