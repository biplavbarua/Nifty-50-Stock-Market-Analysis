# Project Objectives: Nifty 50 Predictive Analysis

This project aims to analyze historical stock market data to predict future trends and assess risk, covering the following key objectives mapped to the INT234 syllabus:

1.  **Financial Data Preprocessing (Unit I):**
    *   **Goal:** Transform raw daily stock data (Open, High, Low, Close) into a clean, analytical format.
    *   **Tasks:** Handle missing trading days, adjust for stock splits, and calculate technical indicators like Moving Averages and Daily Returns.

2.  **Price Prediction via Regression (Unit II):**
    *   **Goal:** Develop regression models to forecast the exact closing price of the Nifty 50 index.
    *   **Tasks:** Implement Linear and Polynomial Regression to predict $P_{t+1}$ based on historical features ($P_t, P_{t-1}, Volume$).

3.  **Market Trend Classification (Unit III):**
    *   **Goal:** Classify market movements into actionable "Buy" or "Sell" signals.
    *   **Tasks:** Use Logistic Regression and SVM to predict the binary direction of the market (Up/Down) based on momentum indicators (RSI, MACD).

4.  **Stock Volatility Clustering (Unit IV):**
    *   **Goal:** Segment Nifty 50 stocks into risk profiles to aid portfolio diversification.
    *   **Tasks:** Apply K-Means clustering to group stocks based on their Annualized Volatility and Average Returns (e.g., "Safe Havens" vs. "High Growth").

5.  **Time Series Forecasting with Deep Learning (Unit V & VI):**
    *   **Goal:** Capture complex temporal dependencies for long-term forecasting.
    *   **Tasks:** Design and train Long Short-Term Memory (LSTM) networks to predict future index values, outperforming traditional statistical models.
