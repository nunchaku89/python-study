import pandas as pd

df = pd.read_csv("../data/students.csv")

mean_by_major = df.groupby("major")["score"].mean()
print(mean_by_major)

students_count_by_major = df.groupby("major").size()
print(students_count_by_major)

max_score_by_major = df.groupby("major")["score"].max()
print(max_score_by_major)

result = df.groupby("major")["score"].agg(
    ["mean", "max", "min", "count"]
)
print(result)
