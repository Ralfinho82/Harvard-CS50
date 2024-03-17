SELECT districts.name, expenditures.per_pupil_expenditure
FROM expenditures
JOIN districts
ON expenditures.district_id = districts.id
WHERE districts.name NOT LIKE '%District%'
GROUP BY districts.name
ORDER BY expenditures.per_pupil_expenditure DESC
LIMIT 10
