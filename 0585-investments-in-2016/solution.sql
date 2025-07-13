/* Find rows whose 2015 value appears more than once
   and whose (lat, lon) combo is unique. */
WITH dup_2015 AS (                     -- tiv_2015 shared by ≥ 2 policies
        SELECT tiv_2015
        FROM   Insurance
        GROUP  BY tiv_2015
        HAVING COUNT(*) > 1
),
uniq_city AS (                         -- (lat,lon) occurs exactly once
        SELECT lat , lon
        FROM   Insurance
        GROUP  BY lat , lon
        HAVING COUNT(*) = 1
)

SELECT
    ROUND(SUM(i.tiv_2016), 2) AS tiv_2016
FROM   Insurance AS i
WHERE  i.tiv_2015 IN (SELECT tiv_2015          FROM dup_2015)
  AND (i.lat , i.lon) IN (SELECT lat , lon     FROM uniq_city);

