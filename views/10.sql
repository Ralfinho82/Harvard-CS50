SELECT english_title, average_color AS color
FROM views
WHERE artist = 'Hokusai' AND english_title LIKE '%beach%'
ORDER BY average_color ASC
