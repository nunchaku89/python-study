import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def analyze(df):
    return {
        "student_count": df["name"].count(),
        "average": df["score"].mean(),
        "max": df["score"].max(),
        "min": df["score"].min(),
        "missing": df["score"].isna().sum(),
        "major_mean": df.groupby("major")["score"].mean(),
        "grade_count": df["grade"].value_counts()
    }