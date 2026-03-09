# AI Usage Documentation: ARM-CBA Baseline

## Overview
- **Date:** 2026-02-27
- **Notebook:** `notebooks/phase-3-arm-cba-modeling.ipynb`
- **Author:** Phillip Roman
- **AI Tool:** Claude AI (Anthropic - Opus 4.6)
- **Course:** DSCI 521, Drexel University

## Author Contributions
- Structured the notebook into two distinct sections: Part 1 (ARM) and Part 2 (CBA)
- Applied ARM to railroad accident data based on Week 4 lecture notes and Xu et al. (2018)
- Selected Apriori algorithm for rule mining using mlxtend
- Designed the CBA classifier as sklearn-compatible (fit/predict) following Liu et al. (1998)
- Selected same 6 features as LR and RF baselines
- Specified two threshold configurations:
  - High: Support=0.05, Confidence=0.70, Lift=2.0
  - Low: Support=0.005, Confidence=0.40, Lift=1.5
- Thresholds defined once as variables in Setup, reused in both sections
- ARM rules saved as standalone CSV artifacts
- Weighted F1 as primary metric, per-class precision/recall as secondary, confusion matrix as tertiary
- Chose colorblind-friendly plotting style (tableau-colorblind10)
- Noticed Accident Type dominating ARM rules during initial runs, decided to verify with statistical testing
- Added Chi-Square with Bonferroni correction to confirm feature significance

## AI Contributions
- Coded the Apriori frequent itemset mining and association rule generation with mlxtend
- Coded the CBA classifier class implementation (fit/predict wrapping ARM inside sklearn interface)
- Coded the cross-validation loop with score collection
- Coded per-class metrics extraction, confusion matrix plotting, CV comparison chart
- Coded rule export to CSV formatting
- Coded Cramer's V computation and Chi-Square with Bonferroni correction
- Coded JSON results save/load formatting
- Chose axis labels, scales, and formatting for plots

## AI-Recommended Analysis
- Cramer's V for measuring categorical feature association strength with Cause_Category. Used to quantify Accident Type dominance observed during ARM runs.

## Modifications After Generation
- Restructured notebook from single-section to two-section (Part 1: ARM, Part 2: CBA) format
- Replaced hardcoded threshold values with shared variables from Setup
- Updated JSON save cell to standardized format and save path to `../results/cba/`
- Inserted Cramer's V and Bonferroni correction cells after ARM experiments
- Verified notebook runs end-to-end after all modifications
