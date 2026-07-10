import pandas as pd

df = pd.read_csv("../data/students.csv")

major_count = df["major"].value_counts()
print(major_count)

major_normalized_count = df["major"].value_counts(normalize=True)
print(major_normalized_count)

grade_count = df["grade"].value_counts()
print(grade_count)

cross_major_grade = pd.crosstab(df["major"], df["grade"])
print(cross_major_grade)
