# Project Objectives: Nifty 50 Predictive Analysis

This project aims to analyze historical stock market data to predict future trends and assess risk, covering the following key objectives mapped to the INT234 syllabus:

1.  **Financial Data Preprocessing:**
    *   **Goal:** Transform raw daily stock data (Open, High, Low, Close) into a clean, analytical format.
    *   **Tasks:** Handle missing trading days, adjust for stock splits, and calculate technical indicators like Moving Averages and Daily Returns.

2.  **Price Prediction via Regression:**
    *   **Goal:** Develop regression models to forecast the exact closing price of the Nifty 50 index.
    *   **Tasks:** Implement Linear and Polynomial Regression to predict $P_{t+1}$ based on historical features ($P_t, P_{t-1}, Volume$).

3.  **Market Trend Classification:**
    *   **Goal:** Classify market movements into actionable "Buy" or "Sell" signals.
    *   **Tasks:** Use Logistic Regression and SVM to predict the binary direction of the market (Up/Down) based on momentum indicators (RSI, MACD).

4.  **Stock Volatility Clustering:**
    *   **Goal:** Segment Nifty 50 stocks into risk profiles to aid portfolio diversification.
    *   **Tasks:** Apply K-Means clustering to group stocks based on their Annualized Volatility and Average Returns (e.g., "Safe Havens" vs. "High Growth").

5.  **Time Series Forecasting with Deep Learning:**
    *   **Goal:** Capture complex temporal dependencies for long-term forecasting.
    *   **Tasks:** Design and train Long Short-Term Memory (LSTM) networks to predict future index values, outperforming traditional statistical models.

## 6. Viva Voce & Technical Justifications

### Q1: Why use `%matplotlib inline`?
*   **Answer:** This is a "Magic Command" specific to Jupyter Notebooks. It instructs the kernel to display plots directly below the code cell that produced them (inline), rather than opening them in a separate pop-up window. It ensures the analysis flow is visual and continuous.

### Q2: Why use Yahoo Finance (`yfinance`) instead of a static CSV?
*   **Answer:**
    1.  **Real-Time Validity:** Static datasets (like those on Kaggle) are often outdated (e.g., stopping in 2021). Our project uses a **Real-Time API** approach to fetch data up to the current date (2025), making the analysis relevant for *predictive* analytics.
    2.  **Official Source:** `yfinance` fetches data directly from the **NSE (National Stock Exchange)** feed, ensuring we are using official market data, just accessed programmatically for efficiency.

### Q3: Why LSTM for Stock Prediction?
*   **Answer:** Traditional models like Linear Regression assume data points are independent. Stock prices are a *Time Series* where today's price depends on yesterday's. **LSTM (Long Short-Term Memory)** networks are designed specifically to remember these long-term dependencies and sequences, making them superior for financial forecasting.
