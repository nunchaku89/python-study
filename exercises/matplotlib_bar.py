import matplotlib.pyplot as plt

majors = ["CS", "Math", "Physics"]

scores = [86, 84.8, 78.17]

plt.bar(majors, scores)

plt.title("Major scores")

plt.xlabel("Major")

plt.ylabel("Scores")

plt.show()