WITH start_events AS (
    SELECT
        machine_id,
        process_id,
        timestamp AS start_ts
    FROM Activity
    WHERE activity_type = 'start'
),                            
end_events AS (
    SELECT
        machine_id,
        process_id,
        timestamp AS end_ts
    FROM Activity
    WHERE activity_type = 'end'
)
SELECT
    s.machine_id,
    ROUND(AVG(e.end_ts - s.start_ts)::numeric, 3) AS processing_time
FROM start_events s
JOIN end_events e
  ON e.machine_id = s.machine_id
 AND e.process_id = s.process_id
GROUP BY
    s.machine_id;

