SELECT first_name, last_name, debut
FROM players
WHERE birth_city = 'Pittsburgh' AND birth_state = 'PA'
ORDER BY 3 DESC, 1, 2
