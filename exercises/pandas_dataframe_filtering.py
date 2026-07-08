import pandas as pd

students = [
    {"name": "Amy", "score": 95, "major": "CS"},
    {"name": "Tom", "score": 88, "major": "Math"},
    {"name": "Wayne", "score": 76, "major": "CS"},
    {"name": "Bob", "score": 100, "major": "Physics"},
    {"name": "Ian", "score": 82, "major": "CS"},
]

products = [
    {"name":"Keyboard","price":50000,"stock":10},
    {"name":"Mouse","price":30000,"stock":0},
    {"name":"Monitor","price":250000,"stock":3},
    {"name":"Laptop","price":1500000,"stock":5},
    {"name":"USB","price":10000,"stock":100}
]

df = pd.DataFrame(students)
df_products = pd.DataFrame(products)

print(df)
print(df["score"])
print(df["score"].mean())
print(df["score"] >= 90)
print(df[df["score"] >= 90])
print(df[df["score"] >= 90]["name"])
print(df[df["major"] == "CS"])
print(df[
    (df["major"] == "CS")
    &
    (df["score"] >= 90)
    ]
)
print(
    df[
        (df["major"] == "Physics")
        |
        (df["score"] >= 95)
    ]
)
print(df[df["score"] >= df["score"].mean()])
print(
    df[
        (df["major"] == "Math")
        |
        (df["score"] >= 90)
    ]
)

print(df_products[df_products["stock"] > 0])
print(df_products[df_products["price"] >= 100000])
print(
    df_products[
        (df_products["stock"] > 0)
        &
        (df_products["price"] >= 100000)
    ]
)