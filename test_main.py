# -*- coding: utf-8 -*-

"""
TESTS goes here
"""
import pandas as pd
import matplotlib.pyplot as plt
from main import ExtractAndAnalyze

df = ExtractAndAnalyze('https://www.kaggle.com/datasets/stefanoleone992/mutual-funds-and-etfs?select=ETF+prices.csv')


# Extract the price data for the SPY ETF
spy_prices = df['SPY']

# Create a line chart
plt.plot(spy_prices)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('SPY ETF Price History')
plt.show()
