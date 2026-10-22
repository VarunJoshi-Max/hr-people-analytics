
import pandas as pd
from pathlib import Path

# Locate the employee dataset
project_dir = Path(__file__).resolve().parent.parent
file_path = (
    project_dir
    / "data"
    / "raw"
    / "PNRao_HR_Analytics_Employee_Master.csv"
)

# Load the data
df = pd.read_csv(file_path)

# Convert dates into proper date format
df["HireDate"] = pd.to_datetime(df["HireDate"], errors="coerce")
df["TerminationDate"] = pd.to_datetime(
    df["TerminationDate"], errors="coerce"
)

# Use the termination date for former employees
# and the latest hire-to-reference period for active employees.
reference_date = pd.Timestamp("2026-10-21")

df["EndDate"] = df["TerminationDate"].fillna(reference_date)

# Calculate tenure in years
df["TenureYears"] = (
    (df["EndDate"] - df["HireDate"]).dt.days / 365.25
)

# Display average tenure by status
print("\nAVERAGE EMPLOYEE TENURE BY STATUS")
print("=" * 45)

summary = df.groupby("Status")["TenureYears"].agg(
    ["count", "mean", "median", "min", "max"]
).round(2)

print(summary)
