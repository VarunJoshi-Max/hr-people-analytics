
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


def plot_average_salary_by_department(df, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)

    avg_salary = (
        df.groupby("Department")["Salary"]
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(10, 6))
    avg_salary.plot(kind="barh", edgecolor="black")

    plt.title("Average Salary by Department")
    plt.xlabel("Average Salary")
    plt.ylabel("Department")
    plt.tight_layout()

    output_file = output_dir / "average_salary_by_department.png"
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"Department salary chart saved to: {output_file}")


def plot_employee_count_by_department(df, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)

    employee_count = (
        df.groupby("Department")["EmployeeID"]
        .nunique()
        .sort_values()
    )

    plt.figure(figsize=(10, 6))
    employee_count.plot(kind="barh", edgecolor="black")

    plt.title("Employee Count by Department")
    plt.xlabel("Number of Employees")
    plt.ylabel("Department")
    plt.tight_layout()

    output_file = output_dir / "employee_count_by_department.png"
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"Employee count chart saved to: {output_file}")

    
def plot_employee_status(df, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)

    status_counts = df["Status"].value_counts()

    plt.figure(figsize=(8, 6))
    plt.pie(
        status_counts,
        labels=status_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Employee Status Distribution")
    plt.tight_layout()

    output_file = output_dir / "employee_status_distribution.png"
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"Employee status chart saved to: {output_file}")


def plot_performance_rating(df, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)

    rating_counts = (
        df["PerformanceRating"]
        .dropna()
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(8, 6))
    rating_counts.plot(kind="bar", edgecolor="black")

    plt.title("Employee Performance Rating Distribution")
    plt.xlabel("Performance Rating")
    plt.ylabel("Number of Employees")
    plt.xticks(rotation=0)
    plt.tight_layout()

    output_file = output_dir / "performance_rating_distribution.png"
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"Performance rating chart saved to: {output_file}")

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
    plot_average_salary_by_department(df, output_dir)
    plot_employee_count_by_department(df, output_dir)
    plot_employee_status(df, output_dir)
    plot_performance_rating(df, output_dir)

if __name__ == "__main__":
    main()
