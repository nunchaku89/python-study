import pandas as pd

df = pd.read_csv("../data/students.csv")

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())
print(df.head())
print(df.tail())
print(df.isna().sum())