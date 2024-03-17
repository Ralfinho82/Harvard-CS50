SELECT districts.name, expenditures.per_pupil_expenditure, staff_evaluations.exemplary
FROM districts
JOIN expenditures
ON districts.id = expenditures.district_id
JOIN staff_evaluations
ON districts.id = staff_evaluations.district_id
--JOIN schools
--ON schools.district_id = districts.id
--JOIN graduation_rates
--ON graduation_rates.school_id = schools.id
WHERE expenditures.per_pupil_expenditure > (
    SELECT AVG(expenditures.per_pupil_expenditure)
    FROM expenditures
) AND staff_evaluations.exemplary > (
    SELECT AVG(staff_evaluations.exemplary)
    FROM staff_evaluations
) AND districts.type = 'Public School District'
AND districts.state = 'MA'
ORDER BY 3 DESC, 2 DESC
