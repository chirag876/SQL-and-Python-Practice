/*
Given the following tables:

Company (company_code, founder)
Lead_Manager (lead_manager_code, company_code)
Senior_Manager (senior_manager_code, lead_manager_code, company_code)
Manager (manager_code, senior_manager_code, lead_manager_code, company_code)
Employee (employee_code, manager_code, senior_manager_code, lead_manager_code, company_code)

Write an SQL query to output:
- company_code
- founder
- total number of distinct lead managers
- total number of distinct senior managers
- total number of distinct managers
- total number of distinct employees

Sort the results by company_code in ascending order (alphabetically).
Use LEFT JOIN to include all companies, even if they have no employees at certain levels.
Use COUNT(DISTINCT column_name) to count unique individuals for each role.
*/

Solution: 
SELECT c.company_code,
       c.founder,
       COUNT(DISTINCT e.lead_manager_code) AS total_lead_managers,
       COUNT(DISTINCT e.senior_manager_code) AS total_senior_managers,
       COUNT(DISTINCT e.manager_code) AS total_managers,
       COUNT(DISTINCT e.employee_code) AS total_employees
FROM Company c
    LEFT JOIN Employee e
        ON c.company_code = e.company_code
GROUP BY c.company_code,
         c.founder
ORDER BY c.company_code ASC