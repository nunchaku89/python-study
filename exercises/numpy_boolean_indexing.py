import numpy as np

scores = np.array([
95,
88,
76,
100,
82,
91,
67
])

names = np.array([
"Amy",
"Tom",
"Wayne",
"Bob",
"Ian",
"Jane",
"Sara"
])

print(f"90점 이상 : {scores[scores >= 90]}")
print(f"80 ~ 90점 : {scores[(scores <= 90) & (scores >= 80)]}")
print(f"80점 미만 : {scores[scores < 80]}")
print(f"평균 : {scores.sum() / len(scores)}")
print(f"평균 이상 : {scores[scores >= (scores.sum() / len(scores))]}")
print(f"90점 이상 학생 : {names[scores >= 90]}")