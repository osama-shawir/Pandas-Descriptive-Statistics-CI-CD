# -*- coding: utf-8 -*-

"""
TESTS goes here
"""

from main import ExtractAndAnalyze

data = ExtractAndAnalyze('https://www.kaggle.com/datasets/stefanoleone992/mutual-funds-and-etfs?select=ETF+prices.csv')

# Extract the price data for the SPY ETF
spy_prices = data['SPY']

# Create a line chart
matplotlib.pyplot.plot(spy_prices)
matplotlib.pyplot.xlabel('Date')
matplotlib.pyplot.ylabel('Price')
matplotlib.pyplot.title('SPY ETF Price History')
matplotlib.pyplot.show()

