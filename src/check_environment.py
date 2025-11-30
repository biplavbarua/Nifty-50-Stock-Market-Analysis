import sys
import os

print("--- Environment Check ---")
print(f"Python Executable: {sys.executable}")
print(f"Python Version: {sys.version}")

print("\n--- Checking Libraries ---")

try:
    import pandas as pd
    print("✅ pandas is installed.")
except ImportError:
    print("❌ pandas is MISSING.")

try:
    import numpy as np
    print("✅ numpy is installed.")
except ImportError:
    print("❌ numpy is MISSING.")

try:
    import yfinance as yf
    print("✅ yfinance is installed.")
except ImportError:
    print("❌ yfinance is MISSING.")

try:
    import tensorflow as tf
    print(f"✅ tensorflow is installed (Version: {tf.__version__}).")
except ImportError:
    print("❌ tensorflow is MISSING. (This is expected if you are not using the .venv kernel)")

print("\n--- Diagnosis ---")
if ".venv" in sys.executable:
    print("✅ GREAT! You are using the correct virtual environment (.venv).")
    print("Your notebooks should run correctly.")
else:
    print("⚠️  WARNING: You are NOT using the project environment.")
    print(f"You are currently using: {sys.executable}")
    print("Please switch your VS Code Kernel to the one that ends with '.venv'")
