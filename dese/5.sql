SELECT city, COUNT(id)
FROM schools
WHERE type = 'Public School'
GROUP BY city
HAVING COUNT(id) <= 3
ORDER BY 2 DESC, 1 ASC
