SELECT salaries.salary
FROM players
JOIN performances
ON players.id = performances.player_id
JOIN salaries
ON salaries.player_id = players.id
WHERE salaries.year = 2001 AND performances.hr = (SELECT MAX(performances.hr) FROM performances)
LIMIT 1
