# -*- coding: utf-8 -*-

import pandas as pd

def ExtractAndAnalyze(x):
    """This function extracts data from a csv, stores it into a dataframe, runs exploratory data analytics on it, and returns the data"""
    df = pd.read_csv(x)
