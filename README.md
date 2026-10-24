# HR & People Analytics Dashboard | Power BI

## Project Overview

The HR & People Analytics Dashboard is an interactive business intelligence project developed using Microsoft Power BI. It consolidates human resources data into a multi-page report to help analyze workforce composition, attrition, compensation, performance, employee engagement, training, recruitment, and succession planning.

The project demonstrates how data modeling, DAX measures, and interactive visualizations can support data-driven HR decision-making.

## Business Objectives

- Monitor workforce size and employee status.
- Analyze workforce trends and attrition rates.
- Compare compensation and performance across departments.
- Evaluate employee engagement and training metrics.
- Monitor open positions and succession planning.
- Present HR metrics through interactive dashboards.

## Dashboard Pages

### 1. HR Executive Overview
Provides a high-level summary of workforce composition, including total employees, active employees, terminated employees, terminated-employee rate, and average latest recorded salary.

### 2. Workforce & Attrition Analysis
Explores monthly headcount trends, monthly attrition rates, departmental headcount, hiring activity, and employee terminations.

### 3. Compensation & Performance
Compares average latest recorded salary and performance ratings across departments.

### 4. Employee Engagement & Training
Analyzes employee engagement, work-life balance, manager feedback, training completion, training scores, and completed training records across departments.

### 5. Recruitment & Workforce Planning
Highlights open positions by department, employees in succession planning, and total succession plans.

## Key Findings

The following findings are based on the current dashboard results:

- The employee master table contains 5,000 employees, including 4,295 active employees and 705 employees marked as terminated.
- Production has the highest departmental headcount, with 584 employees.
- Sales has the highest average latest recorded salary, at approximately ₹1.26 lakh.
- Human Resources has the highest average performance rating, at approximately 3.53.
- Marketing has the highest average employee engagement score, at approximately 3.51.
- All training records in the dataset are marked Completed, and the average training score is 88.
- Sales has the highest number of open positions, with 352.

These findings describe the current dashboard results and do not independently establish the causes behind the observed differences.

## Tools & Technologies

- **Microsoft Power BI Desktop** — Dashboard development and visualization
- **Power Query** — Data preparation and transformation
- **DAX** — Measures and calculations
- **Microsoft Excel / CSV** — Source data
- **Git and GitHub** — Version control and project documentation

*Only list tools that you actually used in the project.*

## Data Model

The project uses dimension tables and fact tables to organize HR information for analysis.

### Dimension Tables
- `dim_Employee`
- `dim_Department`
- `DimDate`
- `dim_Skills`

### Fact Tables
- `fact_Compensation`
- `fact_PerformanceReviews`
- `fact_HeadcountAttrition`
- `fact_OpenPositions`
- `fact_TrainingRecords`
- `fact_EngagementSurveys`
- `fact_LeaveAttendance`
- `fact_JobHistory`
- `fact_SuccessionPlanning`
- `factless_EmployeeSkills`

The model uses relationships between employee, department, date, and business-event data to support reporting. Some relationships use different keys or inactive relationship paths where required by the model.

## Key Measures

Examples of the DAX measures developed for the dashboard include:

- Total Employees
- Active Employees
- Terminated Employees
- Employee Attrition Rate
- Latest Recorded Salary
- Average Latest Salary
- Average Performance Rating
- Average Engagement Score
- Average Work-Life Balance Score
- Average Manager Feedback Score
- Training Completion Rate
- Average Training Score
- Open Positions Count
- Total Succession Plans

The measures support workforce monitoring and comparisons across departments and reporting periods.

## Business Recommendations

Based on the observed metrics, HR stakeholders could:

1. Review staffing requirements and recruitment priorities across departments.
2. Compare compensation by role, grade, experience, and performance to assess pay equity.
3. Investigate employee survey feedback to identify opportunities to improve engagement.
4. Evaluate training effectiveness using learning outcomes and post-training performance, not completion status alone.
5. Review succession coverage for critical positions and validate successor readiness.

These are recommendations for further investigation rather than claims that the dashboard has established specific causes.

## Repository Structure

```text
hr-people-analytics/
│
├── data/
│   └── raw/
│
├── powerbi/
│   └── HR_People_Analytics.pbix
│
├── screenshots/
│   ├── hr-executive-overview.png
│   ├── workforce-attrition-analysis.png
│   ├── compensation-performance.png
│   ├── engagement-training.png
│   └── recruitment-workforce-planning.png
│
└── README.md
```

*Update the structure if your actual repository uses different folder names. Keep large or sensitive source files out of GitHub when appropriate.*

## Limitations

- Employee-level termination status and monthly attrition rates represent different metrics and should not be interpreted interchangeably.
- Average latest recorded salary reflects available compensation records and may not represent current payroll for every employee.
- The training completion rate reflects the status of training records in the dataset, not necessarily completion of every required course by every employee.
- Department-level averages can conceal differences between individual employees and roles.
- The dashboard identifies patterns but does not establish causation.

## Conclusion

This project demonstrates the use of Power BI to transform HR data into an interactive reporting solution. It brings together workforce, compensation, performance, engagement, training, recruitment, and succession-planning metrics to support HR analysis and evidence-based decision-making.

## Author

**Varun Joshi**

MBA in Finance | HR & People Analytics | Power BI

[GitHub Profile](https://github.com/VarunJoshi-Max)
