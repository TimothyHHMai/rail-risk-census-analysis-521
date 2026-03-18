# Urban/Rural Railroad Risk Analysis
## DSCI 521 Group Project - Drexel University

An analysis of railroad accident risk profiles across urban and rural environments by combining FRA accident data with USDA Rural-Urban Continuum Codes.

## Project Overview

Starting from a shared proposal and EDA, the project split into two parallel analysis tracks:

**Classification (Phillip Roman & Dave Woodford):** Can environmental and operational features predict railroad accident cause categories? Three models compared: Association Rule Mining + Classification Based on Associations (ARM-CBA), Logistic Regression, and Random Forest.

**Regression (Timothy Mai & Matt Dolin):** Predicting accident damage costs using feature selection and regression modeling.

Both tracks use the same FRA Form 54 dataset and shared EDA.

## Directory Structure

```
.
├── data/
│   ├── raw/                          # Original source data
│   ├── processed/                    # Cleaned and engineered data
│   │   └── arm_rules/                # ARM rules saved as CSV artifacts
│   └── splits/                       # Train/test splits (80/20, stratified)
├── notebooks/
│   ├── shared/                       # Shared proposal and EDA
│   │   ├── 01_proposal_shared.ipynb
│   │   └── 02_eda_shared.ipynb
│   ├── classification/               # Classification analysis (Phillip & Dave)
│   │   ├── 03a_log_reg_baseline.ipynb
│   │   ├── 03b_arm_cba_baseline.ipynb
│   │   ├── 03c_rand_forest_baseline.ipynb
│   │   ├── 04a_log_reg_tuning.ipynb
│   │   ├── 04b_arm_cba_tuning.ipynb
│   │   ├── 04c_rand_forest_tuning.ipynb
│   │   ├── 05_final_classification_eval.ipynb
│   │   ├── models/                   # Saved baseline and tuned model pickles
│   │   ├── results/                  # Experiment results as JSON (lr/, rf/, cba/)
│   │   ├── prompts/                  # AI usage documentation (one per notebook)
│   │   ├── pdfs/                     # PDF exports of all shared and classification notebooks
│   │   └── pdf_util.py              # Script to regenerate all PDFs
│   └── regression/                   # Regression analysis (Timothy & Matt)
│       ├── cost_prediction.ipynb
│       └── featureSelection.ipynb
│       ├── models/                   # Saved regression models
│       └── pdfs/                     # PDF exports of all shared and classification notebooks
├── explore/                          # Experimental and scratchpad notebooks
├── requirements.txt
└── README.md
```

## Notebook Guide

### Shared (Both Teams)
1. `01_proposal_shared.ipynb` - Project proposal, data loading, initial merge
2. `02_eda_shared.ipynb` - Exploratory data analysis, feature engineering, Chi-Square tests, train/test split creation

### Classification (Phillip & Dave)

**Baselines (Phase 3):**

3. `03a_log_reg_baseline.ipynb` - Logistic Regression baseline with 6 features
4. `03b_arm_cba_baseline.ipynb` - ARM rule mining (Part 1) and CBA classification (Part 2) with Cramer's V verification of Accident Type dominance
5. `03c_rand_forest_baseline.ipynb` - Random Forest baseline as nonlinear benchmark

**Tuning (Phase 3):**

6. `04a_log_reg_tuning.ipynb` - Feature selection experiments (Accident Type removal, Track Type vs Signalization, RUCC encoding), GridSearchCV, L1 sparsity analysis
7. `04b_arm_cba_tuning.ipynb` - Undersampling for minority class rule mining, threshold grid search
8. `04c_rand_forest_tuning.ipynb` - Feature importance redistribution, GridSearchCV (216 configurations)

**Final Evaluation:**

9. `05_final_classification_eval.ipynb` - Side-by-side comparison of all three tuned models on the locked test set. No model training is performed in this notebook. The test set was locked throughout all baseline and tuning experiments and opened only here for final evaluation.

**Artifacts:**
- Baseline and tuned model pipelines saved as pickle files in `notebooks/classification/models/`
- Experiment results saved as JSON in `notebooks/classification/results/` (organized by `lr/`, `rf/`, `cba/`)
- ARM rules saved as CSV in `data/processed/arm_rules/`
- PDF exports of all shared and classification notebooks available in `notebooks/classification/pdfs/` (regenerate with `python pdf_util.py`)

**Challenges/Limitations:**
- Accident cause code class imbalance made it difficult to predict signal and environmental accidents
- Undersampling to mine rules for rare cause codes lowered model performance for predicting more common accident causes
- ARM/CBA models were trained using only the top 6 features

### Regression (Timothy & Matt)

**Notebooks:**
- `featureSelection.ipynb` - Feature selection for regression
- `cost_prediction.ipynb` - Cost prediction EDA and modeling

**Artifacts:**
- Compressed models saved as joblib files in `notebooks/regression/models`
- PDF exports of all regression notebooks available in `notebooks/regression/pdfs/`

**Challenges:**
- Nonlinear relationships between features and target (log of total damage cost) resulted in higher error and lower R2 scores
- More complex models tended to overfit on the training data and perform poorly on the testing data. This mostly applied to the decision tree regressor, though it was also true for some neural network architectures
- The damage costs for accidents of each cause code correlated with different features, which made it difficult to accurately predict costs for all accidents in a single model

## Data Sources

- **FRA Form 54:** [Rail Equipment Accident/Incident Data](https://data.transportation.gov/Railroads/Rail-Equipment-Accident-Incident-Data-Form-54-/85tf-25kj/about_data) - 34,551 railroad accidents (2012-2024)
- **USDA RUCC 2023:** [Rural-Urban Continuum Codes](https://www.ers.usda.gov/data-products/rural-urban-continuum-codes) - County-level urban/rural classification

## AI Usage

Classification notebooks were created with assistance from Claude AI (Anthropic). Each classification notebook has a corresponding `prompt.md` in `notebooks/classification/prompts/` documenting author contributions and AI contributions. The shared notebooks and regression notebooks were not AI-assisted.

## Authors

- **Phillip Roman** - Classification
- **Dave Woodford** - Classification
- **Timothy Mai** - Regression
- **Matt Dolin** - Regression

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/TimothyHHMai/rail-risk-census-analysis-521.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Data files are included in `data/raw/` as compressed CSVs.
