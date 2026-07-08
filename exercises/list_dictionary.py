students = [
    {"name":"Amy","score":95},
    {"name":"Tom","score":82},
    {"name":"Wayne","score":100},
    {"name":"Bob","score":76},
    {"name":"Ian","score":88}
]

for student in students:
    if student["score"] >= 90:
        print(f"{student["name"]} : {student['score']}")


sum = 0
for student in students:
    sum += student["score"]

print(len(students))
print(f"평균 : {sum / len(students)}")

highest_score = 0
highest_name = ""
for student in students:
    if highest_score < student["score"]:
        highest_score = student["score"]
        highest_name = student["name"]

print(f"최고점\n{highest_name} : {highest_score}")