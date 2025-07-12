WITH boarded AS (
    SELECT
        person_name,
        turn,
        SUM(weight) OVER (ORDER BY turn) AS running_kg   -- cumulative weight
    FROM Queue
)
SELECT person_name
FROM   boarded
WHERE  running_kg <= 1000               -- still under the limit
ORDER  BY turn DESC                      -- farthest we got onto the bus
LIMIT 1;                                 -- keep that single person

