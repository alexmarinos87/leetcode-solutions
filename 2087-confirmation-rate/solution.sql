# Write your MySQL query statement below
SELECT
    s.user_id,
    ROUND(CASE WHEN COUNT(DISTINCT c.time_stamp) = 0 THEN 0 
    ELSE COUNT(DISTINCT conf.time_stamp)/ COUNT(DISTINCT c.time_stamp) END ,2) AS confirmation_rate
FROM Signups AS s
LEFT JOIN Confirmations AS c
ON s.user_id = c.user_id
LEFT JOIN (SELECT user_id, time_stamp, action FROM Confirmations WHERE action = "confirmed") AS conf
ON conf.user_id = s.user_id
GROUP BY s.user_id;
