import pandas as pd

df = pd.read_csv("../data/students.csv")

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

def get_pass(score):
    if score >= 80:
        return "Pass"
    else:
        return "Fail"

df["grade"] = df["score"].apply(get_grade)
df["result"] = df["score"].apply(get_pass)

print(df[["name", "score", "grade", "result"]])