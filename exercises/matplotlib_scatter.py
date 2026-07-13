import matplotlib.pyplot as plt

exercise_time = [1,2,3,4,5,6]
body_fat = [30,28,25,22,20,18]

plt.figure(figsize=(8 ,5))

plt.scatter(exercise_time, body_fat)

plt.title("Exercise Time vs Body Fat")

plt.xlabel("Exercise Time")

plt.ylabel("Body Fat")

plt.tight_layout()

plt.show()