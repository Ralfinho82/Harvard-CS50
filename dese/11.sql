SELECT s.name, e.per_pupil_expenditure, g.graduated
FROM expenditures e
JOIN districts d
ON e.district_id = d.id
JOIN schools s
ON s.district_id = d.id
JOIN graduation_rates g
ON g.school_id = s.id
ORDER BY 2 DESC, 1 ASC
