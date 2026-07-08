name = input("이름을 입력하세요 : ")

with open("study_log.txt", "a", encoding="utf-8") as file:
    file.write(f"{name}님이 Python을 공부했습니다.")