import numpy as np
import pandas as pd

scores = np.array([95, 88, 76, 100, 82])

print(f"평균 : {scores.mean()}")
print(f"중앙값 : {np.median(scores)}")
print(f"최댓값 : {scores.max()}")
print(f"최솟값 : {scores.min()}")
print(f"표준편차 : {scores.std()}")

df = pd.DataFrame([95, 88, 76, 100, 82], columns=['score'])

print(f"평균 : {df["score"].mean()}")
print(f"중앙값 : {np.median(df["score"])}")
print(f"최댓값 : {df["score"].max()}")
print(f"최솟값 : {df["score"].min()}")
print(f"표준편차 : {df["score"].std()}")


class_a = np.array([80, 81, 79, 80, 80])
class_b = np.array([40, 100, 60, 90, 30])

mean_a = class_a.mean()
mean_b = class_b.mean()
std_a = class_a.std()
std_b = class_b.std()

print(f"mean_a : {mean_a}")
print(f"mean_b : {mean_b}")
print(f"std_a : {std_a}")
print(f"std_b : {std_b}")