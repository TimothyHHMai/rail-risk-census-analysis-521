# AI Usage Documentation: Logistic Regression Tuning Experiments

## Overview
- **Date:** 2026-02-27
- **Notebook:** `notebooks/lr-tuning-experiments.ipynb`
- **Author:** Phillip Roman
- **AI Tool:** Claude AI (Anthropic - Opus 4.6)
- **Course:** DSCI 521, Drexel University

## Author Contributions
- Designed 6 experiments across feature selection and hyperparameter tuning
- Experiment 1: Decided to remove Accident Type based on ARM rule dominance observed in ARM-CBA baseline
- Experiment 2: Chose to compare Track Type vs Signalization due to correlation (r = -0.52) found in Phase 2
- Experiment 3: Chose to compare raw RUCC_2023 vs binned RUCC_Metro_Adjacency, selected RUCC_Metro_Adjacency for interpretability
- Experiment 4: Specified GridSearchCV with C values and class_weight options for L-BFGS/L2
- Experiment 5a/5b: Chose to test SAGA solver with L1 penalty to examine feature sparsity, decided to run with and without Accident Type to demonstrate its dominance
- Experiment 6: Specified GridSearchCV on SAGA/L1 configuration
- Determined that defaults were optimal based on grid search results
- Chose to save all experiment results as standardized JSON for cross-notebook comparison
- Chose colorblind-friendly plotting style (tableau-colorblind10)

## AI Contributions
- Coded the helper functions (build_lr_pipeline, run_cv_experiment, save_experiment, compare_experiments, plot functions)
- Coded the GridSearchCV implementation
- Coded the L1 sparsity coefficient extraction and analysis
- Coded per-class metrics extraction, comparison charts, CV fold plots
- Coded JSON results save/load formatting
- Chose axis labels, scales, and formatting for plots
- Discussed best graph types for presenting results

## AI-Recommended Analysis
- L1 sparsity analysis to examine which features carry zero weight per cause class. I directed the experiment; AI recommended examining per-class coefficient patterns.

## Modifications After Generation
- Removed Cramer's V and Gini importance references throughout (analysis lives in ARM-CBA baseline)
- Fixed JSON key references to match standardized format (cv_mean, cv_scores)
- Built final model save cell to export lr_tuned_pipeline.pkl
- Verified notebook runs end-to-end after all modifications
