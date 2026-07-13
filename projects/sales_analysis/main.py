from analyze import load_data

df = load_data("./data/sales.csv")

describe = df.describe()

result = f"""
DESCRIBE : {describe}
=============================
행 개수 : {df.shape[0]}
열 개수 : {df.shape[1]}
"""

print(result)