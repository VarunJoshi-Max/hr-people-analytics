
import pandas as pd
from pathlib import Path

# Find the project folder
project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "data" / "raw" / "PNRao_HR_Analytics_Employee_Master.csv"

# Load employee data
df = pd.read_csv(file_path)

# Calculate salary statistics for each employee status
salary_summary = df.groupby("Status")["Salary"].agg(
    ["count", "mean", "median", "min", "max"]
).round(2)

# Display the results
print("\nSALARY COMPARISON BY EMPLOYEE STATUS")
print("=" * 50)
print(salary_summary)
