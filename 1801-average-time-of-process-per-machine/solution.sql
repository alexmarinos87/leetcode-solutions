# Write your MySQL query statement below
WITH start AS(
    SELECT machine_id,
    process_id,
    activity_type,
    timestamp AS start
FROM Activity
WHERE activity_type = "start"
GROUP BY machine_id, process_id),
end AS(
    SELECT machine_id,
        process_id,
        activity_type,
        timestamp AS end
    FROM Activity
    WHERE activity_type ="end"
GROUP BY machine_id, process_id
)
SELECT
    start.machine_id,
    ROUND(AVG(end.end - start.start ),3) AS processing_time
FROM start
JOIN end
ON start.machine_id = end.machine_id AND
    start.process_id = end.process_id
GROUP BY machine_id;
