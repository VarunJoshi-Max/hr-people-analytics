
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "PNRao_HR_Analytics_Employee_Master.csv"
)


def main():
    df = pd.read_csv(DATA_FILE)

    summary = pd.crosstab(
        df["PerformanceRating"],
        df["Status"]
    )

    summary["Total"] = summary.sum(axis=1)

    summary["TerminatedPct"] = (
        summary["Terminated"] / summary["Total"] * 100
    )

    print("PERFORMANCE RATING AND EMPLOYEE STATUS")
    print("=" * 50)
    print(summary.round(2).to_string())

    print("\nTermination share within each rating:")
    print(
        summary["TerminatedPct"]
        .sort_values(ascending=False)
        .round(2)
        .to_string()
    )


if __name__ == "__main__":
    main()
