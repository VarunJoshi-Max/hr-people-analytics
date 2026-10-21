
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "PNRao_HR_Analytics_Headcount___Attrition_Summary.csv"
)


def main():
    df = pd.read_csv(DATA_FILE)

    df["MonthEnd"] = pd.to_datetime(
        df["MonthEnd"], errors="coerce"
    )

    print("HEADCOUNT & ATTRITION VALIDATION")
    print("=" * 45)

    print(f"Total records: {len(df):,}")
    print(f"Unique RecordIDs: {df['RecordID'].nunique():,}")
    print(f"Missing MonthEnd: {df['MonthEnd'].isna().sum()}")

    print("\nDate range:")
    print("Earliest:", df["MonthEnd"].min())
    print("Latest:", df["MonthEnd"].max())

    print("\nNumeric validation:")
    for col in ["Headcount", "Hires", "Terminations", "AttritionRate"]:
        print(f"{col} below zero: {(df[col] < 0).sum()}")

    print("\nHeadcount equal to zero:")
    print((df["Headcount"] == 0).sum())

    print("\nAttrition rate summary:")
    print(df["AttritionRate"].describe().to_string())

    print("\nAttrition rate above 100:")
    print((df["AttritionRate"] > 100).sum())

    print("\nRecords per department:")
    print(df["Department"].value_counts().to_string())

    
    print("\nZero attrition rate:")
    print((df["AttritionRate"] == 0).sum())

    print("\nDuplicate department-month combinations:")
    print(
        df.duplicated(subset=["Department", "MonthEnd"]).sum()
    )

    print("\nAttrition rate by department:")
    print(
        df.groupby("Department")["AttritionRate"]
        .agg(["mean", "min", "max"])
        .sort_values("mean", ascending=False)
        .to_string()
    )

    # Compare the stored rate with two possible formulas.
    expected_rate_headcount = (
        df["Terminations"] / df["Headcount"]
    )

    mismatch = (
        (df["AttritionRate"] - expected_rate_headcount).abs()
        > 0.00015
    )

    print(
        "\nRecords where rate differs from terminations/headcount "
        "by more than 0.00015:",
        mismatch.sum()
    )
    
    zero_rate = df["AttritionRate"] == 0

    print("\nZero attrition rate cross-check:")
    print("Records with zero rate:", zero_rate.sum())
    print(
        "Zero-rate records with terminations:",
        (zero_rate & (df["Terminations"] > 0)).sum()
    )
    print(
        "Zero-rate records with no terminations:",
        (zero_rate & (df["Terminations"] == 0)).sum()
    )

    print("\nFuture MonthEnd records:")
    print((df["MonthEnd"] > pd.Timestamp("2026-10-21")).sum())

if __name__ == "__main__":
    main()
