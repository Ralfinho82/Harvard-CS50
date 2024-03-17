SELECT first_name AS Firstname, last_name AS Surename
FROM players
WHERE birth_city = 'New York' AND birth_year LIKE '198%'
ORDER BY 1, 2
