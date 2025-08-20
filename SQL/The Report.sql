/*
Given the following tables:

Students (ID, Name, Marks)
Grades (Grade, Min_Mark, Max_Mark)

Write an SQL query to generate a report with the following columns:
- Name (or NULL if Grade < 8)
- Grade
- Marks

Requirements:
- Determine each student's grade based on their marks using the Grades table.
- If a student's grade is 8 or higher, include their name; otherwise, display NULL.
- Sort the results by:
  - Grade in descending order.
  - For students with the same grade:
    - If Grade >= 8, sort by Name alphabetically (ascending).
    - If Grade < 8, sort by Marks in descending order.
*/

Solution:
SELECT 
  CASE WHEN g.min_mark >= 70 THEN s.name ELSE NULL END AS name, 
  grade, 
  marks 
FROM 
  students s 
  JOIN grades g ON s.marks BETWEEN g.min_mark 
  AND g.max_mark 
ORDER BY 
  grade DESC, 
  name, 
  (CASE WHEN name IS NULL THEN grade END) DESC, 
  marks;
