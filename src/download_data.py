import yfinance as yf
import pandas as pd
import os
from datetime import datetime

def download_nifty_data():
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Nifty 50 Ticker Symbol on Yahoo Finance is ^NSEI
    ticker = "^NSEI"
    end_date = datetime.today().strftime('%Y-%m-%d')
    print(f"Downloading data for {ticker} from 2000-01-01 to {end_date}...")
    
    data = yf.download(ticker, start="2000-01-01", end=end_date)
    
    if not data.empty:
        # Save to CSV
        file_path = 'data/nifty50_2000_2025_11_30.csv'
        data.to_csv(file_path)
        print(f"Successfully saved data to {file_path}")
        print(f"Shape: {data.shape}")
        print(data.head())
    else:
        print("Failed to download data. Please check your internet connection or ticker symbol.")

if __name__ == "__main__":
    download_nifty_data()
