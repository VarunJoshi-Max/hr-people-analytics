\# HR \& People Analytics — Exploratory Data Analysis Report



\## 1. Project Overview



\### Objective

The objective of this project is to analyze employee data to understand workforce composition, salary distribution, departmental differences, performance ratings, and employee termination patterns.



\### Tools Used

\- Python

\- pandas for data analysis

\- Matplotlib for data visualization

\- Git and GitHub for version control

\- Power BI for interactive dashboard development



\### Dataset Overview

The Employee Master dataset contains 5,000 employee records and 12 columns, including EmployeeID, Department, JobTitle, Gender, HireDate, TerminationDate, Salary, PerformanceRating, and Status.



The wider project contains 12 CSV datasets covering employee information, compensation, job history, recruitment, performance, training, leave, engagement, headcount, succession planning, and skills.



\## 2. Data Quality and Preparation



Initial data inspection and validation were performed using Python.



Key findings:

\- The Employee Master dataset contains 5,000 records and 5,000 unique EmployeeIDs.

\- No duplicate EmployeeIDs were found.

\- There are 4,295 active employees and 705 terminated employees.

\- TerminationDate is missing for 4,295 employees, consistent with the active employee count.

\- ManagerID is missing for 1,232 employees and requires careful interpretation.

\- Salary values were checked for missing or non-positive values.

\- Date fields and employee status relationships were validated.



Raw datasets are excluded from version control to avoid publishing potentially sensitive employee information.



\## 3. Exploratory Data Analysis — Key Findings



\### Finding 1: Workforce Composition

The dataset contains 5,000 employees, of whom 4,295 (85.9%) are active and 705 (14.1%) are terminated. This describes the status distribution in the dataset and should not be interpreted as an annual attrition rate.



\### Finding 2: Salary Distribution

The average salary is 91,055.05, while the median salary is 75,585.50. The mean being higher than the median suggests that higher salaries may be pulling the average upward.



\### Finding 3: Salary Differences Across Departments

Sales has the highest average salary at 122,533.66, followed by Quality Control at 110,767.01. Human Resources has the lowest average salary at 69,551.67. These differences may reflect different roles and job structures; further analysis is needed before drawing conclusions about pay fairness.



\### Finding 4: Department Headcount

Production has the largest workforce with 584 employees, while Research \& Development has the smallest with 517 employees. These figures describe the distribution of employees across departments.



\### Finding 5: Performance Ratings

Performance ratings are distributed relatively evenly: rating 2 has 1,248 employees, rating 3 has 1,217, rating 4 has 1,286, and rating 5 has 1,249. Rating 4 is the most common rating in this dataset.



\### Finding 6: Termination and Performance Rating

The termination share within each performance rating is approximately:

\- Rating 2: 13.94%

\- Rating 3: 13.89%

\- Rating 4: 13.61%

\- Rating 5: 14.97%



The differences are relatively small. These results do not establish that performance ratings cause employee termination.



\### Finding 7: Tenure by Employee Status

Terminated employees have an average recorded tenure of 3.00 years, compared with 4.43 years so far for active employees. Because active employees are still employed, this comparison should be interpreted cautiously.



\### Finding 8: Salary by Employee Status

Active employees have an average salary of 91,183.39, compared with 90,273.16 for terminated employees. The difference is small, so salary alone may not explain termination patterns.



\## 4. Business Recommendations



\### Recommendation 1: Investigate Department-Level Retention

Review employee exit information, tenure, and engagement by department to understand why termination patterns differ. Prioritize further investigation rather than assuming that a department's higher termination share identifies the cause.



\### Recommendation 2: Review Compensation Across Departments

Compare salaries within similar job titles, experience levels, and responsibilities before making compensation decisions. Department averages alone are not sufficient to determine whether pay is fair.



\### Recommendation 3: Explore Employee Engagement

Analyze engagement survey responses alongside tenure and employee status, where data permits, to identify potential areas for improvement in employee experience.



\## 5. Limitations



\- The analysis describes the available dataset and does not establish causation.

\- The employee status proportions are not annual attrition rates.

\- Active employee tenure is measured up to the analysis reference date, while terminated employee tenure uses recorded termination dates.

\- Salary currency and units should be confirmed before presenting salary figures with a currency symbol.

\- Recruitment stage dates include some future dates relative to the analysis reference date and should be investigated before calculating recruitment timing metrics.



\## 6. Conclusion



The analysis provides an overview of workforce composition, salary differences, department headcount, performance ratings, and recorded tenure. The findings can guide further investigation into retention, compensation, and engagement. The next project phase is to build an interactive Power BI dashboard that presents these measures clearly and allows users to explore results by department and employee status.



