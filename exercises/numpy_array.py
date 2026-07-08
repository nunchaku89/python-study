import numpy as np

scores = np.array([95, 88, 76, 100, 82])

print(f"평균 : {scores.mean()}")
print(f"최대값 : {scores.max()}")
print(f"최소값 : {scores.min()}")
print(f"합계 : {scores.sum()}")
print(f"+5 : {scores + 5}")
print(f"+10% : {scores * 1.1}")
print(f"90점 이상 : {scores >= 90}")