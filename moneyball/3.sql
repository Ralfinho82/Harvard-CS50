SELECT performances.year, performances.hr
FROM players
JOIN performances
ON players.id = performances.player_id
WHERE players.first_name = 'Ken' AND players.last_name = 'Griffey' AND players.birth_year = 1969
ORDER BY 1 DESC
