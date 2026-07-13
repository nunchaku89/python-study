import matplotlib.pyplot as plt

#과제1
months = [
    "Jan", "Feb", "Mar",
    "Apr", "May", "Jun"
]

sales = [
    120, 150, 170,
    165, 190, 220
]

plt.figure(figsize=(8, 5))

plt.plot(
    months,
    sales,
    marker="o",
    linewidth=2
    )

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.tight_layout()

plt.show()

#과제2
weeks = [
    "Week1",
    "Week2",
    "Week3",
    "Week4"
]

weight = [
    72,
    71.5,
    71.0,
    70.8
]

plt.figure(figsize=(8, 5))

plt.plot(
    weeks,
    weight,
    marker="o",
    linewidth=3
)

plt.title("Weight and Weeks")

plt.xlabel("Weeks")

plt.ylabel("Weights")

plt.tight_layout()

plt.show()