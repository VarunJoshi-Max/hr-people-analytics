# HR & People Analytics Dashboard | Power BI

## 1. Project Overview

The **HR & People Analytics Dashboard** is a business intelligence project developed using Microsoft Power BI to analyze workforce data and present HR metrics through interactive visualizations.

The project covers multiple areas of human resource management, including workforce composition, headcount, attrition, compensation, employee performance, engagement, training, recruitment, and succession planning.

Python was used for data processing, Power BI for dashboard development and analysis, and Git and GitHub for version control and project hosting.

The objective is to transform HR data into meaningful insights that help stakeholders understand workforce patterns and identify areas requiring further investigation.

## 2. Business Objectives

- Analyze workforce composition and employee status.
- Examine headcount trends, hires, terminations, and monthly attrition.
- Compare recorded compensation and performance across departments.
- Evaluate employee engagement, work-life balance, and manager feedback.
- Analyze training completion records and training assessment scores.
- Identify departmental recruitment requirements.
- Examine employee participation in succession planning.
- Present HR metrics through interactive dashboards to support data-driven decision-making.

## 3. Dashboard Pages

The Power BI report contains five pages.

### Page 1: HR Executive Overview

Provides a consolidated overview of the workforce and key HR indicators.

**Key metrics:**
- Total employees
- Active employees
- Terminated employees
- Employee status distribution
- Department-wise headcount

**Purpose:** Provide a high-level view of workforce composition and help stakeholders identify areas for further analysis.

### Page 2: Workforce & Attrition Analysis

Examines workforce changes and employee movement over time.

**Key analyses:**
- Monthly headcount trend
- Monthly attrition trend
- Monthly hires versus terminations
- Total hires
- Total terminations
- Year-based filtering

**Purpose:** Help stakeholders examine workforce trends and identify periods that may require further investigation.

### Page 3: Compensation & Performance

Compares compensation and performance indicators across departments.

**Key analyses:**
- Average recorded salary by department
- Average performance score by department

**Purpose:** Support departmental comparisons and identify areas for further review of compensation and performance patterns.

### Page 4: Employee Engagement & Training

Analyzes employee engagement indicators and training outcomes.

**Key analyses:**
- Average engagement score by department
- Average training score by department
- Completed training records by department
- Average work-life balance score
- Average manager feedback score
- Training completion rate

**Purpose:** Help stakeholders review engagement patterns and training outcomes and identify potential employee development opportunities.

### Page 5: Recruitment & Workforce Planning

Examines recruitment requirements and succession planning.

**Key analyses:**
- Total open positions
- Open positions by department
- Employees in primary succession planning
- Total succession plans

**Purpose:** Help stakeholders understand recruitment demand and review succession planning coverage.

## 4. Key Findings

The following findings are based on the metrics displayed in the dashboard.

| Metric | Finding |
|---|---|
| Total employees | 5,000 |
| Active employees | 4,295 |
| Terminated employees | 705 |
| Terminated employees as a share of employee records | 14.1% |
| Highest headcount department | Production — 584 |
| Lowest headcount department | R&D — 517 |
| Highest average recorded salary | Sales — approximately ₹1.26 lakh |
| Lowest average recorded salary | HR — approximately ₹71,063 |
| Highest average performance score | HR — approximately 3.53 |
| Lowest average performance score | Logistics — approximately 3.45 |
| Highest average engagement score | Marketing — approximately 3.51 |
| Lowest average engagement score | Logistics — approximately 3.45 |
| Average work-life balance score | 3 |
| Average manager feedback score | 4 |
| Training completion rate | 100% of the training records represented |
| Average training score | 88 |
| Total open positions | 1,415 |
| Department with the most open positions | Sales — 352 |
| Employees in primary succession planning | 1,234 |
| Total succession plans | 1,415 |

**Interpretation note:** The 14.1% figure represents terminated employees as a proportion of all employee records. It should not be interpreted as the monthly or annual attrition rate.

## 5. Business Recommendations

### 1. Improve Workforce Planning

Review departmental headcount alongside open positions to understand staffing requirements. Investigate the high number of open positions in Sales and assess whether the recruitment demand aligns with business needs.

### 2. Review Compensation Differences

Investigate departmental salary differences using additional information such as job roles, experience, seniority, and responsibilities. Average salary alone cannot establish whether compensation is equitable.

### 3. Investigate Engagement and Performance

Explore factors that may contribute to differences in employee engagement and performance scores. Additional employee feedback and workforce information can help identify appropriate interventions.

### 4. Evaluate Training Effectiveness

Review training assessment scores and connect training participation with relevant performance or skill-development outcomes. Training completion alone does not demonstrate that employees have acquired or applied the intended skills.

### 5. Strengthen Recruitment and Succession Planning

Review open positions alongside succession plans to identify critical roles and potential internal talent pipelines. Validate succession coverage and employee readiness before making workforce planning decisions.

## 6. Tools & Technologies

- **Python:** Data processing and preparation.
- **Microsoft Power BI Desktop:** Data visualization, dashboard development, and reporting.
- **Git:** Version control and tracking project changes.
- **GitHub:** Repository hosting and project documentation.

## 7. Data Model

The project uses dimension and fact tables to organize HR information for analysis.

### Dimension Tables

| Table | Purpose |
|---|---|
| `dim_Employee` | Employee-level information |
| `dim_Department` | Department details |
| `DimDate` | Date dimension for time-based analysis |
| `dim_Skills` | Skill-related information |

### Fact Tables

| Table | Purpose |
|---|---|
| `fact_Compensation` | Compensation information |
| `fact_PerformanceReviews` | Employee performance review records |
| `fact_HeadcountAttrition` | Monthly headcount, hires, terminations, and attrition metrics |
| `fact_OpenPositions` | Recruitment and open-position information |
| `fact_TrainingRecords` | Training records and outcomes |
| `fact_EngagementSurveys` | Employee engagement survey information |
| `fact_LeaveAttendance` | Leave and attendance information |
| `fact_JobHistory` | Employee job-history records |
| `fact_SuccessionPlanning` | Succession planning information |
| `factless_EmployeeSkills` | Employee-to-skill associations |

The development model also contained a `fact_EmployeeStatus` table with loading disabled.

## 8. Key HR Metrics

The dashboard includes metrics covering the following areas:

- Workforce composition
- Active and terminated employees
- Headcount trends
- Hires and terminations
- Attrition rate
- Average recorded salary
- Average performance score
- Average engagement score
- Work-life balance
- Manager feedback
- Training completion and assessment scores
- Open positions
- Employees in succession planning
- Total succession plans

These metrics enable users to explore HR indicators and compare departments or time periods where the underlying data and report filters support those comparisons.

## 9. Limitations and Considerations

- The 14.1% terminated employee share is based on employee records and is not a period-based attrition rate.
- Average recorded salary may not represent current payroll unless the underlying records and calculation have been validated for that purpose.
- The training completion rate describes the available training records; it does not independently establish that every employee completed every mandatory course.
- Department-level averages may conceal differences across job roles, employee groups, and experience levels.
- Observed differences between departments do not establish cause and effect.
- Recruitment and succession planning metrics should be validated against actual business requirements before operational decisions are made.

## 10. Conclusion

The HR & People Analytics Dashboard demonstrates the use of Power BI to bring multiple HR data areas into a unified reporting environment.

By combining workforce analysis, attrition, compensation, performance, engagement, training, recruitment, and succession planning, the project provides a structured view of key HR metrics.

The dashboard demonstrates practical application of data processing, data visualization, interactive reporting, and business-focused analysis.

It also highlights how HR analytics can help stakeholders identify patterns, investigate potential issues, and make more informed workforce planning decisions.


## 11. Author

**Varun Joshi**  
MBA in Finance | HR & People Analytics | Power BI

[GitHub Profile](https://github.com/VarunJoshi-Max)

---

*This project was developed for portfolio and learning purposes.*
