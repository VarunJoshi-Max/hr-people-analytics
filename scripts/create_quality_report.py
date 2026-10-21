
from pathlib import Path
from datetime import datetime

PROJECT_DIR = Path(__file__).resolve().parent.parent
REPORT_DIR = PROJECT_DIR / "reports"
REPORT_DIR.mkdir(exist_ok=True)

report = """
# HR & People Analytics — Data Quality Report

## Project scope
Initial data-quality checks were performed on the supplied HR CSV datasets.
Raw files were preserved without modification.

## Employee Master
- Records: 5,000
- Unique EmployeeIDs: 5,000
- Duplicate EmployeeIDs: 0
- Missing TerminationDate: 4,295
- Missing ManagerID: 1,232
- Non-positive salaries: 0
- Invalid hire dates: 0
- Termination dates before hire dates: 0
- ManagerIDs not found in Employee Master: 0
- Self-management references: 0

Interpretation:
Missing TerminationDate values match the active employee count.
Missing ManagerID values require business-context review.

## Job History
- Records: 5,000
- Unique employees: 5,000
- Missing StartDate: 0
- Missing EndDate: 5,000
- EmployeeIDs absent from Employee Master: 0
- StartDate before HireDate: 0
- Job title differences versus Employee Master: 0
- Department differences versus Employee Master: 0

Limitation:
All EndDate values are missing, including those for terminated employees.
The reason is not established.

## Recruitment Funnel
- Records: 59,744
- Unique candidates: 59,744
- Unique positions: 1,415
- Invalid application dates: 0
- Invalid stage dates: 0
- Stage dates before application dates: 0
- Future stage dates relative to 2026-10-21: 5,963
- Candidates appearing in multiple stages: 0

Limitation:
Each candidate has one recorded stage. Stage counts cannot establish
candidate-by-candidate conversion between stages.

## Headcount & Attrition
- Records: 954
- Unique RecordIDs: 954
- Missing MonthEnd: 0
- Negative numeric values: 0
- Zero attrition rates: 595
- Zero-rate records with terminations: 0
- Duplicate department-month combinations: 0
- Attrition rates match Terminations / Headcount within 0.00015
- Future MonthEnd records relative to 2026-10-21: 9

Limitation:
Confirm the meaning of future-dated records and the intended rate scale
before final reporting.

## Data handling
- Original CSV files were not modified.
- Findings should be rechecked before final publication.
- Missing values were not automatically replaced or deleted.

## Next steps
1. Validate remaining datasets.
2. Clean data only where justified.
3. Perform exploratory data analysis.
4. Build visualizations and an interactive Power BI dashboard.
5. Document insights, limitations, and recommendations.
"""

output_file = REPORT_DIR / "data_quality_report.md"
output_file.write_text(report.strip() + "\n", encoding="utf-8")

print(f"Report created: {output_file}")
