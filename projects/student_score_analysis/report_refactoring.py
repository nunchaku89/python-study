import pandas as pd
import matplotlib.pyplot as plt
from analyze import load_data, analyze
from create_report import create_report

df = load_data("../../data/students.csv")

result = analyze(df)

# print(create_report(result= result))

major_mean = result["major_mean"]
plt.bar(major_mean.index, major_mean.values)
plt.show()