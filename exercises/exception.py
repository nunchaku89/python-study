try:
    number = int(input("숫자를 입력해주세요 : "))

    print(number)

except ValueError:
    print("숫자만 입력해주세요.")

try:
    with open("anonymous.txt", "r", encoding="utf-8") as file:
        file.read()

except FileNotFoundError:
    print("존재하지 않는 파일입니다.")

scores = [
    "95",
    "88",
    "abc",
    "70",
    "hello",
    "100"
]
sum = 0
length = len(scores)
for scr in scores:
    try:
        sum += int(scr)
    except ValueError:
        length -= 1
        print(f"{scr}는 제외합니다.")
    
avg = sum / length
print(f"평균 : {avg}")

students = [
    {"name":"Amy","score":"95"},
    {"name":"Tom","score":"abc"},
    {"name":"Wayne","score":"100"},
    {"name":"Bob","score":"80"}
]

student_sum = 0
student_length = len(students)
for student in students:
    try:
        student_sum += int(student["score"])
    except ValueError:
        student_length -= 1
        print(f"{student["score"]}는 제외합니다.")

student_avg = student_sum / student_length
print(f"학생 평균 : {student_avg}")