SELECT teams.name, ROUND (AVG(salaries.salary), 2) AS average_salary
FROM players
JOIN salaries
ON players.id = salaries.player_id
JOIN teams
ON teams.id = salaries.team_id
WHERE salaries.year = 2001
GROUP BY teams.name
ORDER BY 2 ASC
LIMIT 5
