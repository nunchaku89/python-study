def greet(name) :
    print(f"안녕하세요 {name}")

def introduce(name, age):
    print(f"안녕하세요\n저는 {name}이고\n{age}살 입니다.")

def multiply(a, b):
    return a * b

def calculate(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    result = f"덧셈 : {add}\n뺄셈 : {sub}\n곱셈 : {mul}\n나눗셈 : {div}"
    print(result)

greet("Amy")

introduce("Tom", 30)

print(multiply(8, 7))

calculate(10, 5)