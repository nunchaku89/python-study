import pandas as pd

df = pd.DataFrame({
    "study_hours": [1,2,3,4,5,6,7,8],
    "score": [55,60,65,72,80,85,92,98]
})

corr = df["study_hours"].corr(df["score"])
print(corr)

df = pd.DataFrame({
    "exercise_time": [1,2,3,4,5,6],
    "body_fat": [30,28,25,22,20,18]
})

print(df.corr(numeric_only=True))