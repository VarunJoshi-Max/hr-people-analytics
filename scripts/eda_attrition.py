
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

    summary = (
        df.groupby("Department")
        .agg(
            TotalRecords=("EmployeeID", "nunique"),
            Terminated=("Status", lambda s: (s == "Terminated").sum()),
            Active=("Status", lambda s: (s == "Active").sum()),
        )
    )

    summary["TerminationRate"] = (
        summary["Terminated"] / summary["TotalRecords"] * 100
    )

    summary = summary.sort_values(
        "TerminationRate", ascending=False
    )

    print("TERMINATION RATE BY DEPARTMENT")
    print("=" * 45)
    print(summary.round(2).to_string())


if __name__ == "__main__":
    main()
