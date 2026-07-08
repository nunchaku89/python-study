numbers = [1, 2, 3, 4, 5]

result = [number * 2 for number in numbers]

print(result)

result = [number * 2
          for number in numbers
          if number % 2 == 0
          ]

print(result)

names = ["WAYNE", "AMY", "TOM"]

result = [name.lower() for name in names]

print(result)

students = [
    {"name":"Amy","score":95},
    {"name":"Tom","score":82},
    {"name":"Wayne","score":100},
    {"name":"Bob","score":76},
    {"name":"Ian","score":88}
]

names = [student["name"] for student in students]

print(names)

names = [student["name"] for student in students if student["score"] > 90]

print(names)

numbers = [number * number for number in numbers]

print(numbers)

numbers = [10,15,20,25,30]

numbers = [number
           for number in numbers
           if number >= 20
           ]

print(numbers)

# students = [student["name"] for student in students]

print(students)

# students = [student["name"]
#            for student in students
#            if student["score"] >= 90
#            ]

students = [print(f"{student["name"]} : {student["score"]}") for student in students]