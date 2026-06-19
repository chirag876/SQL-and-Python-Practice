/* Give me the Nth highest salary from the Employee table. If there is no Nth highest salary, then return null. */

select distinct Salary as NthHighestSalary
from Employee e1 order by Salary desc
limit 1 offset N-1
