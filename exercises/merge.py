import pandas as pd

students = pd.DataFrame({
    "name": ["Amy", "Tom", "Wayne", "Bob"],
    "major": ["CS", "Math", "CS", "Physics"],
    "score": [95, 88, 76, 100]
})

majors = pd.DataFrame({
    "major": ["CS", "Math", "Physics"],
    "department": ["Engineering", "Science", "Science"]
})

result = pd.merge(
    students,
    majors,
    on="major"
)

print(result[["name", "major", "score", "department"]])

def get_dean(major):
    if major == "CS":
        return "Kim"
    elif major == "Physics":
        return "Lee"
    else:
        return "Park"

majors["dean"] = majors["major"].apply(get_dean)

new_result = pd.merge(
    students,
    majors,
    on="major"
)

print(new_result)