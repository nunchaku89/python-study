import matplotlib.pyplot as plt

scores = [
    58, 60, 65, 68,
    72, 75, 76, 78,
    81, 82, 84, 85,
    88, 90, 92, 94,
    95, 96, 98, 100
]

plt.figure(figsize=(8, 5))
plt.hist(scores, bins=5)
plt.title("점수 분포표")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# bin 값이 클 수록 그래프가 촘촘하게 그려진다