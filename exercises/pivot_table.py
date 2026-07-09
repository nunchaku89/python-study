import pandas as pd

students = pd.DataFrame({
    "name": ["Amy", "Tom", "Wayne", "Bob", "Jane", "Ian"],
    "major": ["CS", "Math", "CS", "Physics", "Math", "Physics"],
    "grade": ["A", "B", "C", "A", "A", "B"],
    "score": [95, 88, 76, 100, 92, 84]
})

pivot_major = students.pivot_table(
    values="score",
    index="major",
    aggfunc="mean"
)

pivot_major_grade = students.pivot_table(
    values="score",
    index="major",
    columns="grade",
    aggfunc="mean"
)

pivot_count = students.pivot_table(
    values="name",
    index="major",
    aggfunc="count"
)

pivot_major_grade_mean = students.pivot_table(
    values="score",
    index="major",
    columns="grade",
    aggfunc="mean"
)

pivot_major_grade_max = students.pivot_table(
    values="score",
    index="major",
    columns="grade",
    aggfunc="max"
)

pivot_major_grade_min = students.pivot_table(
    values="score",
    index="major",
    columns="grade",
    aggfunc="min"
)

print(pivot_major_grade_mean)
print(pivot_major_grade_max)
print(pivot_major_grade_min)