SELECT DISTINCT            -- one row per qualifying number
       l1.num AS ConsecutiveNums
FROM   Logs  AS l1
JOIN   Logs  AS l2 ON l2.id = l1.id + 1      -- next row
JOIN   Logs  AS l3 ON l3.id = l1.id + 2      -- row after that
WHERE  l1.num = l2.num                       -- same value in all 3 rows
  AND  l2.num = l3.num;

