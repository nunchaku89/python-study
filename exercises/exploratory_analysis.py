import pandas as pd

df = pd.read_csv("../data/students.csv")

print(df["score"].describe())

print(
    df.groupby("major")["score"].mean()
)

print(
    df["grade"].value_counts()
)

print(
    pd.crosstab(df["major"], df["grade"])
)

print(
    df.pivot_table(
        values="score",
        index="major",
        columns="grade",
        aggfunc="mean"
    )
)
