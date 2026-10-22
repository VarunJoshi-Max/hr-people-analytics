
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "PNRao_HR_Analytics_Employee_Master.csv"
)


def plot_salary_distribution(df, output_dir):
    output_dir.mkdir(exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.hist(df["Salary"], bins=20, edgecolor="black")

    plt.title("Distribution of Employee Salaries")
    plt.xlabel("Salary")
    plt.ylabel("Number of Employees")
    plt.tight_layout()

    output_file = output_dir / "salary_distribution.png"
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"\nSalary chart saved to: {output_file}")


def main():
    df = pd.read_csv(DATA_FILE)

    print("EMPLOYEE MASTER — EXPLORATORY DATA ANALYSIS")
    print("=" * 55)

    print(f"\nTotal employee records: {len(df):,}")
    print(f"Unique employees: {df['EmployeeID'].nunique():,}")

    print("\n1. Employee status distribution")
    print(df["Status"].value_counts().to_string())

    print("\n2. Headcount by department")
    print(
        df.groupby("Department")["EmployeeID"]
        .nunique()
        .sort_values(ascending=False)
        .to_string()
    )

    print("\n3. Salary summary")
    print(
        df["Salary"]
        .describe()
        .round(2)
        .to_string()
    )

    print("\n4. Average salary by department")
    print(
        df.groupby("Department")["Salary"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
        .to_string()
    )

    print("\n5. Performance rating distribution")
    print(
        df["PerformanceRating"]
        .value_counts()
        .sort_index()
        .to_string()
    )
        
    output_dir = PROJECT_DIR / "reports" / "charts"
    plot_salary_distribution(df, output_dir)

if __name__ == "__main__":
    main()
