import numpy as np
import pandas as pd

scores = np.array([95,88,76,100,82])

print(scores[0])
print(scores[-1])
print(scores[:3])
print(scores[-2:])

students = [
    {"name":"Amy","score":95},
    {"name":"Tom","score":88},
    {"name":"Wayne","score":76},
    {"name":"Bob","score":100},
    {"name":"Ian","score":82}
]

df = pd.DataFrame(students)

print(df.iloc[0])
print(df.iloc[:3])
print(df.iloc[0,0])
print(df.iloc[1,1])

df.index = [
    "A",
    "B",
    "C",
    "D",
    "E"
]

print(df.loc["C"])
print(df.iloc[2])