SELECT players.first_name, players.last_name, salaries.salary / performances.h AS dollars_per_hit
FROM players
JOIN salaries
ON players.id = salaries.player_id
JOIN performances
ON players.id = performances.player_id
WHERE salaries.year = 2001 AND performances.year = 2001 AND performances.h > 0
ORDER BY 3 ASC, 1 ASC, 2 ASC
LIMIT 10
