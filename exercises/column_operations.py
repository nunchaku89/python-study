import pandas as pd

students = [
    {"name": "Amy", "score": 95},
    {"name": "Tom", "score": 88},
    {"name": "Wayne", "score": 76},
    {"name": "Bob", "score": 100},
]

df = pd.DataFrame(students)

df["bonus"] = df["score"] + 5
df["ratio"] = df["score"] / 100
df["message"] = df["name"] + "학생"

score = df["score"]
grade = []

for sc in score:
    if sc >= 90:
        grade.append("A")
    elif sc >= 80:
        grade.append("B")
    else:
        grade.append("C")

df["grade"] = grade

print(df)

print(type(df["score"]))

print(type(df["grade"]))