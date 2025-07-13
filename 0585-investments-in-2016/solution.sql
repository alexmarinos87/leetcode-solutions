WITH dup_2015 AS (                 -- tiv_2015 that appear ≥ 2 times
        SELECT tiv_2015
        FROM   Insurance
        GROUP  BY tiv_2015
        HAVING COUNT(*) > 1
),
uniq_city AS (                     -- (lat,lon) that appear exactly once
        SELECT lat, lon
        FROM   Insurance
        GROUP  BY lat, lon
        HAVING COUNT(*) = 1
)

SELECT ROUND(SUM(i.tiv_2016)::numeric, 2) AS tiv_2016
FROM   Insurance AS i
JOIN   dup_2015   USING (tiv_2015)        -- keeps only shared-2015 rows
JOIN   uniq_city  USING (lat, lon);       -- …that are in a unique city

