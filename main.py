# -*- coding: utf-8 -*-
def ExtractAndAnalyze(x):
    """This function extracts data from a csv, stores it into a dataframe, runs exploratory data analytics on it, and returns the dataframe"""
    df = pd.read_csv(x)
    df.describe()
    return df
