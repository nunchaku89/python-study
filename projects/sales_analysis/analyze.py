import pandas as pd

REQUIRED_COLUMNS = {"month", "category", "sales"}

def load_data(path):
    return pd.read_csv(path)

def validate_data(df):
    # 1. 데이터가 비어 있는지 검사
    # 2. 필수 컬럼이 모두 있는지 검사
    # 3. sales 컬럼에 결측치가 있는지 검사
    # 문제가 있으면 ValueError를 발생시킨다.
    if df.empty:
        raise ValueError("데이터가 비어있습니다.")

    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        columns = ", ".join(sorted(missing_columns))
        raise ValueError(f"필수 컬럼이 없습니다: {columns}")


    if df["sales"].isnull().any():
        raise ValueError("sales 컬럼에 결측치가 있습니다.")

def summarize_by_month(df):
    grouped = df.groupby("month", as_index=False, sort=False)

    monthly_sales = grouped["sales"].sum()

    monthly_sales = monthly_sales.rename(columns={"sales": "total_sales"})

    return monthly_sales

def summarize_by_category(df):
    grouped = df.groupby("category", as_index=False, sort=False)

    category_sales = grouped["sales"].sum()

    category_sales = category_sales.rename(columns={"sales": "total_sales"})
    
    category_sales = category_sales.sort_values("total_sales", ascending=False)

    category_sales = category_sales.reset_index(drop=True)

    return category_sales