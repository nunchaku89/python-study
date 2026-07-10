import pandas as pd

df = pd.read_csv("../../data/students.csv")

report = f"""
=========================================
 Student Score Analysis Report
=========================================
      
학생 수 : {df['name'].count()}

평균 점수 : {df['score'].mean():.2f}

최고점 : {df['score'].max()}

최저점 : {df['score'].min()}

결측치 개수 : {df['score'].isna().sum()}

전공별 평균
{df.groupby('major')['score'].mean()}

등급 분포
{df['grade'].value_counts()}

=========================================

전체 학생 20명의 평균점수는 82.88점 이다.

평균 점수가 가장 높게 나타난 전공은 CS 이다.

C등급에 분포된 학생 수가 가장 많다.

결측치 처리가 필요한 record가 3개 있다.
      """

with open("../../reports/student_report.txt", "w", encoding="utf-8") as file:
    file.write(report)