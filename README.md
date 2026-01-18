# Urban/Rural Railroad Risk Analysis
## DSCI 521 Group Project

An analysis of railroad accident risk profiles across urban and rural environments by combining FRA accident data with US Census Bureau population metrics.

## Description
We have decided on combining two datasets: the FRA railroad accident data (Form 54) and US Census data to analyze urban/rural risk for railroads. We will combine or merge the data on the County FIPS code.

## Data Sources
*Original links provided by team:*

* **Railroad Dataset (FRA Form 54):**
    [Rail Equipment Accident/Incident Data](https://data.transportation.gov/Railroads/Rail-Equipment-Accident-Incident-Data-Form-54-/85tf-25kj/about_data)
* **Census Dataset (USDA RUCC):**
    [USDA Rural-Urban Continuum Codes](https://www.ers.usda.gov/data-products/rural-urban-continuum-codes)

## Directory Structure
* `data/`: Raw and processed datasets. **Note:** Please ZIP all CSVs before uploading.
* `notebooks/`: Main analysis steps
* `src/`: Python scripts and helper modules
* `explore/`: Experimental or scratchpad notebooks
* `results/`: Final figures and tables
* `scratch/`: Local temporary files (not synced)

## Getting Started

### Prerequisites
* Python 3.8+
* `pandas`, `requests`, `census`

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/TimothyHHMai/rail-risk-census-analysis-521.git](https://github.com/TimothyHHMai/rail-risk-census-analysis-521.git)
    ```

2.  **Download the Data (Step 1):**
    * Download the CSVs from the links in the **Data Sources** section above.

3.  **Organize the Data (Step 2):**
    * Move the downloaded CSV files into the `data/raw/` folder.
    * *Note: If you plan to push data to GitHub, please compress the CSVs into .zip format first.*

4.  **Install Dependencies:**
    ```bash
    pip install pandas requests census
    ```

## Authors
* Timothy Mai
* Dave Woodford
* Phillip Roman

---
---

# Appendix: DSCI 611 Professor's Recommended Setup (Advanced)
*The following is from the course template. It includes instructions for using `uv` and `pre-commit` hooks if the team decides to adopt them.*

## Development Environment & Setup

### Software Setup
This template is designed to work with the following tools:
-   **Visual Studio Code** for editing.
-   **[`uv`](https://astral.sh/uv/)** for managing Python environments and dependencies. (See: [uv All the Way: Your Go-to Python](https://www.marvelousmlops.io/p/uv-all-the-way-your-go-to-python))
-   **`pre-commit`** for enforcing source code formatting. (See: [Welcome to Pre-commit Heaven](https://www.marvelousmlops.io/p/welcome-to-pre-commit-heaven?utm_source=publication-search))

### Installation (using uv)
1.  Install `uv`:
    -   Mac: `brew install uv pre-commit`
    -   Windows: `winget install astral-sh.uv`
2.  Install project dependencies:
    ```console
    $ uv sync
    $ . ./.venv/bin/activate
    ```
3.  Set up `pre-commit`:
    ```console
    $ pre-commit install
    ```