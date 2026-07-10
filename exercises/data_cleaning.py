import pandas as pd

students = pd.DataFrame({
    "name": [" Amy", "Tom ", "Wayne", "Bob", "Bob"],
    "major": ["CS", "Math", "CS", "Physics", "Physics"],
    "score": ["95", "88", "76", "100", "100"]
})

print("===== Before Cleaning =====")
students.info()

students["name"] = students["name"].str.strip()
students["score"] = students["score"].astype(int)
students = students.drop_duplicates()

print("===== After Cleaning =====")
students.info()