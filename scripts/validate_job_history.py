
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data" / "raw"

JOB_FILE = DATA_DIR / "PNRao_HR_Analytics_Job_History.csv"
EMPLOYEE_FILE = DATA_DIR / "PNRao_HR_Analytics_Employee_Master.csv"


def main():
    jobs = pd.read_csv(JOB_FILE)
    employees = pd.read_csv(EMPLOYEE_FILE)

    jobs["StartDate"] = pd.to_datetime(
        jobs["StartDate"], errors="coerce"
    )
    jobs["EndDate"] = pd.to_datetime(
        jobs["EndDate"], errors="coerce"
    )
    employees["HireDate"] = pd.to_datetime(
        employees["HireDate"], errors="coerce"
    )

    print("JOB HISTORY VALIDATION")
    print("=" * 45)

    print(f"Total job history records: {len(jobs):,}")
    print(f"Unique employees in job history: {jobs['EmployeeID'].nunique():,}")
    print(f"Missing StartDate: {jobs['StartDate'].isna().sum():,}")
    print(f"Missing EndDate: {jobs['EndDate'].isna().sum():,}")

    print(
        "StartDate after EndDate:",
        (
            jobs["StartDate"].notna()
            & jobs["EndDate"].notna()
            & (jobs["StartDate"] > jobs["EndDate"])
        ).sum()
    )

    print(
        "Job History EmployeeIDs absent from Employee Master:",
        (~jobs["EmployeeID"].isin(employees["EmployeeID"])).sum()
    )

    comparison = jobs.merge(
        employees[["EmployeeID", "HireDate", "JobTitle", "Department"]],
        on="EmployeeID",
        how="left",
        suffixes=("_history", "_master")
    )

    print(
        "StartDate before HireDate:",
        (
            comparison["StartDate"].notna()
            & comparison["HireDate"].notna()
            & (comparison["StartDate"] < comparison["HireDate"])
        ).sum()
    )

    print(
        "JobTitle differs from Employee Master:",
        (
            comparison["JobTitle_history"]
            != comparison["JobTitle_master"]
        ).sum()
    )

    print(
        "Department differs from Employee Master:",
        (
            comparison["Department_history"]
            != comparison["Department_master"]
        ).sum()
    )

    
    job_status = jobs.merge(
        employees[["EmployeeID", "Status"]],
        on="EmployeeID",
        how="left"
    )

    print("\nEndDate missing by employee status:")
    print(
        job_status.assign(
            EndDateMissing=job_status["EndDate"].isna()
        )
        .groupby("Status")["EndDateMissing"]
        .agg(["sum", "count"])
        .to_string()
    )

if __name__ == "__main__":
    main()
