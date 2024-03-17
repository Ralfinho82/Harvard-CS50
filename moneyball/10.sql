SELECT players.first_name, players.last_name, salaries.salary, performances.hr, salaries.year
FROM players
JOIN salaries
ON players.id = salaries.player_id
JOIN performances
ON players.id = performances.player_id
WHERE performances.year = salaries.year
ORDER BY players.id ASC, 5 DESC, 4 DESC, 5 DESC
