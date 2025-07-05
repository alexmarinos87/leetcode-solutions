# Write your MySQL query statement below
SELECT today.id
FROM Weather AS previous
INNER JOIN Weather AS today
ON today.recordDate = previous.recordDate + INTERVAL 1 Day
WHERE today.temperature > previous.temperature;
