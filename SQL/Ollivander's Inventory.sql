/*
Given the following tables:

Wands (id, code, coins_needed, power)
Wands_Property (code, age, is_evil)

Write an SQL query to find non-evil wands (is_evil = 0) that have the highest power for each wizard age group. If multiple wands have the same maximum power for an age, select the one with the lowest cost (coins_needed). Output:
- id
- age
- coins_needed
- power

Requirements:
- Exclude evil wands (is_evil = 1).
- For each age, select the wand with the highest power; if tied, pick the one with the lowest coins_needed.
- Sort results by:
  - power in descending order.
  - For the same power, sort by age in descending order.
*/

SELECT 
  w.id, 
  wpro.age, 
  w.coins_needed, 
  w.power 
FROM 
  Wands as w 
  JOIN Wands_Property as wpro ON w.code = wpro.code 
WHERE 
  wpro.is_evil = 0 
  AND w.coins_needed = (
    SELECT 
      Min(w2.coins_needed) 
    FROM 
      Wands as w2 
      JOIN Wands_Property as wpro2 ON w2.code = wpro2.code 
    WHERE 
      wpro2.is_evil = 0 
      AND wpro.age = wpro2.age 
      AND w.power = w2.power
  ) 
ORDER BY 
  w.power DESC, 
  wpro.age DESC;
