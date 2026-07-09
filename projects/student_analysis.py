import pandas as pd

df = pd.read_csv("../data/students.csv")

print("=== 데이터 미리보기 ===")
print(df.head())

print("=== 결측치 개수 ===")
print(df.isna().sum())

average_score = df["score"].mean()
df["score"] = df["score"].fillna(average_score)

total_students = len(df)
average_score = df["score"].mean()
max_score = df["score"].max()
min_score = df["score"].min()

top_students = df[df["score"] >= 90]
major_average = df.groupby("major")["score"].mean()

print("========== Student Report ==========")
print(f"총 학생 수 : {total_students}명")
print(f"평균 점수 : {average_score:.2f}")
print(f"최고 점수 : {max_score}")
print(f"최저 점수 : {min_score}")

print("\n90점 이상 학생")
print(top_students)

print("\n전공별 평균")
print(major_average)

report = pd.DataFrame({
    "metric": ["total_students", "average_score", "max_score", "min_score"],
    "value": [total_students, average_score, max_score, min_score]
})

report.to_csv("../reports/students_report.csv", index=False, encoding="utf-8")