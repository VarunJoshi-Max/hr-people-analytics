

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

    # Keep the original date values for data-quality checks.
    raw_termination_dates = df["TerminationDate"].copy()

    df["HireDate"] = pd.to_datetime(
        df["HireDate"], errors="coerce"
    )
    df["TerminationDate"] = pd.to_datetime(
        df["TerminationDate"], errors="coerce"
    )

    print("EMPLOYEE MASTER DATA QUALITY REPORT")
    print("-" * 45)

    print(f"Total records: {len(df):,}")
    print(f"Unique EmployeeIDs: {df['EmployeeID'].nunique():,}")
    print(
        "Duplicate EmployeeIDs:",
        df["EmployeeID"].duplicated().sum()
    )

    print("\nMissing values:")
    print(df.isna().sum().to_string())

    print("\nSalary validation:")
    print(f"Zero or negative salaries: {(df['Salary'] <= 0).sum()}")

    print("\nDate validation:")
    print(f"Invalid hire dates: {df['HireDate'].isna().sum()}")

    invalid_termination_dates = (
        raw_termination_dates.notna()
        & raw_termination_dates.astype(str).str.strip().ne("")
        & df["TerminationDate"].isna()
    )
    print(
        "Invalid nonblank termination dates:",
        invalid_termination_dates.sum()
    )

    invalid_date_order = (
        df["TerminationDate"].notna()
        & (df["TerminationDate"] < df["HireDate"])
    )
    print(
        "Termination before hire:",
        invalid_date_order.sum()
    )

    print("\nMissing ManagerID by employee status:")
    print(
        df.loc[df["ManagerID"].isna(), "Status"]
        .value_counts(dropna=False)
        .to_string()
    )

    
    print("\nMissing ManagerID by department:")
    print(
        df.loc[df["ManagerID"].isna(), "Department"]
        .value_counts(dropna=False)
        .to_string()
    )

    print("\nMissing ManagerID by job title (top 10):")
    print(
        df.loc[df["ManagerID"].isna(), "JobTitle"]
        .value_counts()
        .head(10)
        .to_string()
    )


    print("\nEmployee status values:")
    print(df["Status"].value_counts(dropna=False).to_string())

    active_with_termination = (
        df["Status"].eq("Active")
        & df["TerminationDate"].notna()
    )
    print(
        "\nActive employees with a termination date:",
        active_with_termination.sum()
    )

    
    print("\nManagerID relationship validation:")

    valid_employee_ids = set(df["EmployeeID"].dropna())

    manager_ids = df["ManagerID"].dropna().astype(str).str.strip()
    missing_manager_records = ~manager_ids.isin(valid_employee_ids)

    print(
        "ManagerIDs not found in Employee Master:",
        missing_manager_records.sum()
    )

    print(
        "Employees who appear to manage themselves:",
        (
            df["EmployeeID"].astype(str).str.strip()
            == df["ManagerID"].astype(str).str.strip()
        ).sum()
    )

if __name__ == "__main__":
    main()
