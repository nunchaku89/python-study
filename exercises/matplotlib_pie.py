import matplotlib.pyplot as plt

majors = ["CS", "Math", "Physics"]
counts = [7, 6, 7]

plt.pie(
    counts,
    labels=majors,
autopct="%1.1f%%",
startangle=90
)

plt.title("Major Ratio")

plt.show()