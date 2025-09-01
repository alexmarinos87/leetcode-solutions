SELECT t.id
FROM Weather AS t
JOIN Weather AS y
  ON y.recordDate = t.recordDate - 1 
WHERE t.temperature > y.temperature;

