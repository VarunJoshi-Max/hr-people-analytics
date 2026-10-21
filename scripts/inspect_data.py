from pathlib import Path

import pandas as pd

# Locate the folder containing the original CSV files.
PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"


def inspect_csv(file_path):
    """Inspect a CSV file without modifying it."""
    print("\n" + "=" * 70)
    print(f"FILE: {file_path.name}")
    print("=" * 70)

    try:
        df = pd.read_csv(file_path, low_memory=False)

        print(f"\nRows: {len(df):,}")
        print(f"Columns: {len(df.columns)}")

        print("\nColumn names:")
        print(df.columns.tolist())

        print("\nData types:")
        print(df.dtypes.to_string())

        print("\nMissing values per column:")
        print(df.isna().sum().to_string())

        print(f"\nDuplicate rows: {df.duplicated().sum():,}")

        print("\nFirst 5 rows:")
        print(df.head().to_string(index=False))

    except Exception as error:
        print(f"Could not inspect {file_path.name}: {error}")


def main():
    csv_files = sorted(RAW_DATA_DIR.glob("*.csv"))

    if not csv_files:
        print(f"No CSV files found in: {RAW_DATA_DIR}")
        return

    print(f"Found {len(csv_files)} CSV files.")

    for file_path in csv_files:
        inspect_csv(file_path)


if __name__ == "__main__":
    main()
