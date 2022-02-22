"""Module Docstrings"""
import pandas as pd
import utils as utils

df = pd.read_csv("data/census.csv")

# remove whitespace in column names
df.columns = df.columns.str.replace(' ', '')

# remove whitespace in values
cat_cols = df.select_dtypes('object').columns
df[cat_cols] = df[cat_cols].apply(lambda x: x.str.strip())

# only store columns that we will use
df = df[utils.predict_cols + utils.target_col]

df.dropna(inplace=True)

df.to_csv("data_cleaned/census_cleaned.csv", index=False)
