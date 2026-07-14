from analyze import load_data
import matplotlib.pyplot as plt

df = load_data("./data/sales.csv")

head = df.head()
info = df.info()
summary = df.describe()

result = f"""
==============================
Sales Dataset Summary
==============================

행 개수 : {df.shape[0]}
열 개수 : {df.shape[1]}

기술 통계
{head}
==============================
{info}
==============================
{summary}
"""

print(result)