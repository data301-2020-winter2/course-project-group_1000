import numpy as np
import pandas as pd
import seaborn as sns
import pandas_profiling as pdp
import matplotlib.pyplot as plt



# load and process function
def load_and_process(csv):
    # Method Chain 1 (Load Data and Rename Columns)
    df1 = (
        pd.read_csv(csv)
        .rename(columns = {'age': 'Age', 'sex': 'Gender', 'bmi': 'BMI', 'children': 'Children', 'smoker': 'Smoker', 'region': 'Region', 'charges': 'Charges'})
    )
    
    # Method Chain 2 (Change yesNo and Region)
    df2 = (
        df1
        .replace({'yes': 'Yes', 'no': 'No'})
        .replace({'southwest': 'SW', 'southeast': 'SE', 'northeast': 'NE', 'northwest': 'NW'})
    )
    
    # Method Chain 3 (Round Charges & BMI and sort by Charges)
    df3 = (
        df2
        .round({'Charges': 2, 'BMI': 2})
        .sort_values('Charges', ascending = True)
    )
    
    # return values
    return df3
