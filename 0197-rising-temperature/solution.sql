SELECT
    t.id
FROM 
    Weather AS t
INNER JOIN
    Weather AS p
ON 
    t.recordDate = p.recordDate + INTERVAL 1 DAY
WHERE 
    t.temperature > p.temperature;
