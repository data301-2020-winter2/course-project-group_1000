import numpy as np
import pandas as pd
import seaborn as sns
import pandas_profiling as pdp
import matplotlib.pyplot as plt

def load_and_process(csv):
    # Method Chain 1 (load data, rename columns, round values to 2 d.p. and sort 'Charges' descending)
    df1 = (
        pd.read_csv('Medical_Cost.csv')
        .rename(columns = {'age': 'Age', 'sex': 'Gender', 'bmi': 'BMI', 'children': 'Children', 'smoker': 'Smoker', 'region': 'Region', 'charges': 'Charges'})
        .round({'Charges': 2, 'BMI': 2})
        .sort_values('Charges', ascending = False)
    )
    
    # Method Chain 2 (change yes/no to Y/N and regions to abbreviations)
    df2 = (
        df1
        .replace({'yes': 'Y', 'no': 'N'})
        .replace({'southwest': 'SW', 'southeast': 'SE', 'northeast': 'NE', 'northwest': 'NW'})
    )
    
    # return values
    return df2
