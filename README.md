# Nifty 50 Predictive Analysis Project

## Overview
This project performs a comprehensive predictive analysis of the Nifty 50 stock market index using historical data from 2000 to 2025. It covers all units of the INT234 syllabus, including Regression, Classification, Clustering, and Deep Learning (LSTM).

*   **Data Source:** Yahoo Finance (Real-time data via `yfinance` API)
*   **Dataset:** `data/nifty50_2000_2025_11_30.csv` (Updated: Nov 30, 2025)
*   **Period:** Jan 1, 2000 - Dec 1, 2025

## Project Structure
```
├── data/                   # Dataset (Nifty 50 Historical Data)
├── notebooks/              # Jupyter Notebooks for analysis
│   ├── Data_Preparation_EDA.ipynb
│   ├── Regression_Price_Prediction.ipynb
│   ├── Classification_Signal_Prediction.ipynb
│   ├── Clustering_Risk_Segmentation.ipynb
│   ├── Deep_Learning_LSTM_Forecasting.ipynb
│   ├── Time_Series_Forecasting_ARIMA.ipynb  # Statistical Baseline (The "Genius" Addition)
│   └── Model_Evaluation.ipynb
├── reports/                # Project Report and Presentation
│   ├── project_report.md
│   ├── presentation.md
│   └── objectives.md
├── src/                    # Source code for data downloading
│   └── download_data.py
└── README.md               # Project Documentation
```

## Setup Instructions

1.  **Prerequisites:**
    *   Python 3.8+
    *   Jupyter Notebook
    *   Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `yfinance`, `tensorflow`

2.  **Installation:**
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn yfinance tensorflow
    ```

3.  **Running the Analysis:**
    *   Navigate to the `notebooks/` directory.
    *   Open and run the notebooks in logical order (Data Prep -> Regression -> Classification -> etc.).

## Objectives Covered
*   **Data Preparation & EDA:** Trend Analysis.
*   **Regression Analysis:** Price Prediction.
*   **Classification:** Buy/Sell Signals (SVM, Naive Bayes).
*   **Clustering:** Risk Segmentation.
*   **Deep Learning:** LSTM Time-Series Forecasting.

## Author
Biplav Barua
