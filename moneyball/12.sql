WITH least_expensive_hits AS (
    SELECT
        players.id AS player_id,
        salaries.salary / performances.h AS dollar_per_hit
    FROM players
    JOIN salaries ON players.id = salaries.player_id
    JOIN performances ON players.id = performances.player_id
    WHERE salaries.year = 2001
    AND performances.year = 2001
    AND performances.h > 0
    AND performances.rbi > 0
    ORDER BY dollar_per_hit ASC
    LIMIT 10
),
least_expensive_rbis AS (
    SELECT
        players.id AS player_id,
        salaries.salary / performances.rbi AS dollar_per_rbi
    FROM players
    JOIN salaries ON players.id = salaries.player_id
    JOIN performances ON players.id = performances.player_id
    WHERE salaries.year = 2001
    AND performances.year = 2001
    AND performances.h > 0
    AND performances.rbi > 0
    ORDER BY dollar_per_rbi ASC
    LIMIT 10
)
SELECT p.last_name, p.first_name
FROM least_expensive_hits AS h
JOIN least_expensive_rbis AS r ON h.player_id = r.player_id
JOIN players AS p ON h.player_id = p.id
ORDER BY p.id;
