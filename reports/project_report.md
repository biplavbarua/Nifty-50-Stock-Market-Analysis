# Project Report: Predictive Analysis of Nifty 50 Stock Market Data

## 1. Project Overview
This project applies advanced Predictive Analytics techniques to historical Nifty 50 stock market data (2000-2025). The goal is to extract actionable financial insights, forecast future market trends, and assess risk using a combination of statistical regression, machine learning classification, unsupervised clustering, and deep learning.

## 2. Objectives
As per the INT234 syllabus, this project addresses the following key objectives:
1.  **Financial Data Preprocessing:** To transform raw OHLC data into a clean, analytical format suitable for modeling.
2.  **Price Prediction via Regression:** To accurately forecast the next day's closing price using historical price and volume data.
3.  **Market Trend Classification:** To classify market movements into binary "Buy" or "Sell" signals based on technical momentum indicators.
4.  **Stock Volatility Clustering:** To segment market periods or stocks into distinct risk profiles (e.g., High Volatility vs. Stable) for portfolio management.
5.  **Time Series Forecasting with Deep Learning:** To leverage Long Short-Term Memory (LSTM) networks for capturing complex, non-linear temporal dependencies in stock prices.

## 3. Methodology & Analysis

### Data Preparation & EDA
*   **Data Source:** Historical Nifty 50 Index Data (2000-2025).
    *   **Source URL:** [Yahoo Finance - Nifty 50 (^NSEI)](https://finance.yahoo.com/quote/%5ENSEI/history)
    *   **Methodology:** Following the "Real-Time API" approach (as seen in recent technical tutorials), we programmatically download the data using the `yfinance` library. This ensures the dataset is not static but always contains the latest market data up to the current date.
    *   **File:** `data/nifty50_2000_2025_11_30.csv` (Updated: Nov 30, 2025)
    *   **Period:** Jan 1, 2000 - Dec 1, 2025
*   **Analysis:** We visualized the long-term upward trend of the Nifty 50 index. Daily returns analysis revealed a normal distribution centered around zero but with significant "fat tails" indicating market crashes (volatility shocks).

### Regression Analysis
*   **Models:** Linear Regression, Polynomial Regression.
*   **Results:** Linear Regression achieved a high $R^2$ score (>0.95) because tomorrow's price is highly correlated with today's price. However, it lags in capturing sudden market shifts.

### Classification Analysis
*   **Models:** Logistic Regression, Support Vector Machines (SVM), and **Naive Bayes**.
*   **Features:** RSI (Relative Strength Index), MACD, and Daily Returns.
*   **Results:**
    *   **SVM:** Successfully classified "Up" vs. "Down" days with reasonable accuracy.
    *   **Naive Bayes:** Provided a probabilistic baseline, performing well given the independence assumption of features like Daily Returns.

### Clustering Analysis
*   **Technique:** K-Means Clustering.
*   **Insight:** We clustered annual market performance into three distinct regimes: "Bull Markets" (High Return, Low Volatility), "Bear Markets" (Negative Return, High Volatility), and "Sideways Markets".

### Deep Learning (LSTM)
*   **Architecture:** Sequential LSTM model with 50 units and Dropout layers.
*   **Performance:** The LSTM model outperformed traditional regression in multi-step forecasting. It successfully learned the "sequence" of price movements rather than just relying on the immediate previous value.

## 4. Conclusion
The project demonstrates that while stock market prediction is inherently difficult due to noise, **Deep Learning (LSTM)** provides a significant edge over traditional statistical methods for time-series forecasting. Furthermore, **Clustering** offers valuable risk-management insights by identifying market regimes.

## 5. Future Scope
*   Integrate **Sentiment Analysis** from financial news (Unit V extension).
*   Deploy the best performing LSTM model as a real-time web dashboard.
