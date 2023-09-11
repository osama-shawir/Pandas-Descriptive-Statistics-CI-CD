# -*- coding: utf-8 -*-
"""Module including AircraftAnalytics function"""
# # Pandas Descriptive Statistics Assignment
# ## Aircraft wildlife strikes data | 1990 - 2015

# In this exercise, we will extract and analyze aircraft wildlife strikes data
# and we will determine the probability of each part of an aircraft getting damaged by an aircraft wildlife strike
import io
import pandas as pd
import matplotlib.pyplot as plt
import requests


# Import the necessary libraries
def AircraftAnalytics():
    """This is a function to run some analytics on aircraft wildlife accidents data"""   
    # Read our data from Google Drive
    file_id = "1TAD7Uyc9PjByt_q13uvGXGeubXnujnUi"
    url = f"https://drive.google.com/uc?id={file_id}"
    # Download the contents of the CSV file
    download = requests.get(url, timeout = 1000).content
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(io.StringIO(download.decode("utf-8")), low_memory=False)
    # Explore the data
    df.head()
    df.info()
    df.describe()
    # # Now we are going to calculate the probability of each part of the flight getting damaged and plot these probabilities
    strikes = {}
    for c in df.columns:
        column_name = c.split(" ")
        # print(len(col_sep), col_sep)
        if len(column_name) > 1 and column_name[1] == "Strike":
            strikes[column_name[0]] = df[column_name[0] + " Damage"].sum() / df[c].sum()
    
    
    # Calculate the probability of each part of the aircraft getting damaged and find the part with the highest damage probability
    plt.bar(strikes.keys(), strikes.values())
    plt.xticks(rotation=90)
    plt.title("Aircraft Part Damage Probability")
    max_damaged_part = max(strikes, key=strikes.get)
    print(max_damaged_part)
    return strikes, max_damaged_part

if __name__ == "__main__":
    s, m = AircraftAnalytics()
