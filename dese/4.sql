SELECT city, COUNT(id)
FROM schools
WHERE type = 'Public School'
GROUP BY city
ORDER BY 2 DESC, 1 ASC
LIMIT 10
