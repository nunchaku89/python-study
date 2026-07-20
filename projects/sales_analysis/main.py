from analyze import load_data, validate_data, summarize_by_month, summarize_by_category
from pathlib import Path
from report import save_report

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "sales.csv"
OUTPUT_DIR = BASE_DIR / "output"
MONTHLY_REPORT_PATH = OUTPUT_DIR / "monthly_sales.csv"
CATEGORY_REPORT_PATH = OUTPUT_DIR / "category_sales.csv"

def main():
    df = load_data(DATA_PATH)
    validate_data(df)

    monthly_sales = summarize_by_month(df)
    category_sales = summarize_by_category(df)

    print("월별 매출")
    print(monthly_sales)

    print("\n카테고리별 매출")
    print(category_sales)

if __name__ == "__main__":
    main()