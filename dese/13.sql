SELECT districts.name, expenditures.per_pupil_expenditure, staff_evaluations.needs_improvement, staff_evaluations.unsatisfactory
FROM expenditures
JOIN districts
ON expenditures.district_id = districts.id
JOIN staff_evaluations
ON staff_evaluations.district_id = districts.id
JOIN graduation_rates
ON graduation_rates.school_id = staff_evaluations.id
ORDER BY 4 DESC, 3 DESC, 2 DESC
