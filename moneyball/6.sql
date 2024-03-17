SELECT teams.name, SUM(performances.h) AS total_hits
FROM players
JOIN performances
ON players.id = performances.player_id
JOIN teams
ON teams.id = performances.team_id
WHERE performances.year = 2001
GROUP BY teams.name
ORDER BY 2 DESC
LIMIT 5
