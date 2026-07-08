import numpy as np
import pandas as pd

students = [
    {"name": "Amy", "score": 95},
    {"name": "Tom", "score": np.nan},
    {"name": "Wayne", "score": 76},
    {"name": "Bob", "score": 100},
    {"name": "Ian", "score": np.nan},
]

df = pd.DataFrame(students)

print(df.isna())
print(df.isna().sum())
print(df.dropna())
average = df["score"].mean()
print(df.fillna(average))

df["major"] = ["CS", "Math", np.nan, "Physics", "CS"]

print(df.dropna())

df["score"] = df["score"].fillna(average)
major_na = df[df["major"].isna()].index
print(df.drop(major_na))