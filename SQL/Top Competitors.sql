/*
Given the following tables:

Hackers (hacker_id, name)
Challenges (challenge_id, hacker_id, difficulty_level)
Difficulty (difficulty_level, score)
Submissions (submission_id, hacker_id, challenge_id, score)

Write an SQL query to find hackers who achieved full scores (as defined in the Difficulty table) in more than one challenge. Output:
- hacker_id
- name

Requirements:
- A full score is when a hacker's submission score for a challenge equals the maximum score for that challenge's difficulty level.
- Count each challenge only once per hacker, even if they have multiple submissions for it.
- Sort the results by:
  - Number of full-score challenges in descending order.
  - If the number of full-score challenges is the same, sort by hacker_id in ascending order.
*/

Solution:
SELECT 
  h.hacker_id, 
  h.name 
FROM 
  Hackers h 
  JOIN Submissions s ON h.hacker_id = s.hacker_id 
  JOIN Challenges c ON s.challenge_id = c.challenge_id 
  JOIN Difficulty d ON c.difficulty_level = d.difficulty_level 
WHERE 
  s.score = d.score 
GROUP BY 
  h.hacker_id, 
  h.name 
HAVING 
  COUNT(DISTINCT s.challenge_id) > 1 
ORDER BY 
  COUNT(DISTINCT s.challenge_id) DESC, 
  h.hacker_id ASC;
