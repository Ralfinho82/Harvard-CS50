SELECT districts.name
FROM expenditures
JOIN districts
ON expenditures.district_id = districts.id
GROUP BY districts.name
HAVING expenditures.pupils = 64
