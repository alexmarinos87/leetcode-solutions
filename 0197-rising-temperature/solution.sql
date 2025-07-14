-- ANSI-SQL / PostgreSQL style
SELECT curr.id
FROM   Weather  AS curr
WHERE  EXISTS (
         SELECT 1
         FROM   Weather AS prev
         WHERE  prev.recordDate = curr.recordDate - INTERVAL '1 DAY'
           AND  curr.temperature > prev.temperature
       );
