# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Define the stock ticker symbol
ticker = "SBIN.NS" # Replace with any other stock symbol

# Set up the real-time data stream
stream = yf.Ticker(ticker).history(period="1d", interval="1m")

# Continuously retrieve and analyze data
while True:
    # Get the latest data
    stock_data = stream.tail(10) # Retrieve the last 10 minutes of data

    # Convert the stock data into a Pandas DataFrame
    df = pd.DataFrame(stock_data)

    # Calculate the moving average of the closing price over a 5-minute period
    ma_5 = df['Close'].rolling(window=5).mean()

    # Print the latest data and moving average
    print("Latest data:")
    print(df.tail())
    print("5-minute moving average:")
    print(ma_5.tail())

    # Visualize the closing price data over time
    plt.plot(df['Close'])
    plt.plot(ma_5)
    plt.title("Real-Time Closing Price and Moving Average of " + ticker + " Stock")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.show()

    # Wait for some time before retrieving the next batch of data
    time.sleep(10)