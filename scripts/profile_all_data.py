
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data" / "raw"


def main():
    csv_files = sorted(DATA_DIR.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in data/raw.")
        return

    print("HR ANALYTICS: ALL DATASET PROFILE")
    print("=" * 60)

    for file_path in csv_files:
        df = pd.read_csv(file_path, low_memory=False)

        print(f"\nDataset: {file_path.name}")
        print("-" * 60)
        print(f"Rows: {len(df):,}")
        print(f"Columns: {len(df.columns)}")
        print(f"Exact duplicate rows: {df.duplicated().sum():,}")

        missing = df.isna().sum()
        missing = missing[missing > 0]

        if missing.empty:
            print("Missing values: None")
        else:
            print("Missing values:")
            print(missing.to_string())

        id_columns = [
            col for col in df.columns
            if col.lower() == "id" or col.lower().endswith("id")
        ]

        for col in id_columns:
            duplicates = df[col].dropna().duplicated().sum()
            print(f"Repeated values in {col}: {duplicates:,}")


if __name__ == "__main__":
    main()
