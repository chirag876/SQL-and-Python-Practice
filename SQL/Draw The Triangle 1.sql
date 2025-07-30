P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

* * * * * 
* * * * 
* * * 
* * 
*
Write a query to print the pattern P(20).

Solution:
WITH stars_cte AS (
    SELECT 20 AS num
    UNION ALL
    SELECT num - 1 FROM stars_cte WHERE num > 1
)
SELECT REPLICATE('* ', num) AS star_line
FROM stars_cte
OPTION (MAXRECURSION 100);
