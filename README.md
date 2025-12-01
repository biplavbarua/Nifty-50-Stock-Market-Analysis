# Nifty 50 Predictive Analysis (2000-2025) 📈

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

A comprehensive predictive analysis of the Nifty 50 stock market index, leveraging Machine Learning and Deep Learning to forecast trends, segment risks, and generate buy/sell signals.

## 📊 Project Overview
This project performs a deep dive into 25 years of historical stock market data (2000-2025). Unlike static analyses, this project utilizes a **Real-Time Data Pipeline** via the `yfinance` API to ensure the model is always up-to-date. It benchmarks traditional statistical models (ARIMA) against modern Deep Learning architectures (LSTM) to determine the most effective forecasting method.

**Key Highlight**: The "Champion/Challenger" model comparison between ARIMA and LSTM.

## 🎯 Key Objectives
1.  **Trend Analysis**: Visualizing long-term market growth and volatility shocks (2008, 2020).
2.  **Price Prediction**: Using Linear & Polynomial Regression to forecast future index values.
3.  **Signal Classification**: deploying SVM & Naive Bayes to generate actionable 'Buy' or 'Sell' signals.
4.  **Risk Segmentation**: Using K-Means Clustering to categorize market years into Bull, Bear, and Sideways regimes.
5.  **Deep Learning Forecasting**: Implementing Long Short-Term Memory (LSTM) networks for non-linear time-series prediction.

## 🛠️ Technology Stack
*   **Language**: Python 3.8+
*   **Data Source**: Yahoo Finance API (`yfinance`)
*   **Key Libraries**:
    *   **Data Manipulation**: `pandas`, `numpy`
    *   **Visualization**: `matplotlib`, `seaborn`
    *   **Machine Learning**: `scikit-learn` (Regression, SVM, K-Means)
    *   **Deep Learning**: `tensorflow` / `keras` (LSTM)
    *   **Statistics**: `statsmodels` (ARIMA)

## 📈 Visuals & Insights
*(Run the notebooks to generate these interactive visualizations)*

### 1. The "Genius" Comparison (ARIMA vs. LSTM)
While ARIMA struggles with sudden volatility, the LSTM model successfully captures non-linear patterns and rapid market recoveries, demonstrating the superiority of Neural Networks for financial time-series.

### 2. Market Regime Clustering
K-Means clustering automatically identified the "2008 Crash" and "2020 Pandemic" as high-risk anomalies without any prior labeling, validating the model's ability to detect market fear.

## 🚀 How to Run
1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/biplavbarua/Nifty-50-Stock-Market-Analysis.git
    ```
2.  **Install Dependencies**:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn yfinance tensorflow statsmodels
    ```
3.  **Run the Analysis**:
    *   Navigate to the `notebooks/` directory.
    *   Start with `Data_Preparation_EDA.ipynb` and proceed sequentially.
    *   *Optional:* Run `src/download_data.py` to fetch the absolute latest data.

## 🤝 Collaborators
*   **Biplav Barua** - *Lead Data Scientist*

---
*Created as part of the INT234 Predictive Analytics Course.*
