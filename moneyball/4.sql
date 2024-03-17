SELECT players.first_name, players.last_name, salaries.salary
FROM players
JOIN salaries
ON players.id = salaries.player_id
WHERE salaries.year = 2001
ORDER BY 3 ASC, 1 ASC, 2 ASC
LIMIT 50
