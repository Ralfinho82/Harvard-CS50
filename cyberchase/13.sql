SELECT title
FROM episodes
WHERE episode_in_season = 1 AND air_date LIKE '2002%' OR episode_in_season = 1 AND air_date LIKE '2003%'
