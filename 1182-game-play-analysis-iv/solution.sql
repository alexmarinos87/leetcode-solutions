WITH first_login AS (              -- each player’s first‑ever login date
    SELECT player_id,
           MIN(event_date) AS first_date
    FROM   activity
    GROUP  BY player_id
),
next_day_flag AS (                 -- did the player come back the next day?
    SELECT f.player_id,
           CASE
               WHEN EXISTS ( SELECT 1
                             FROM   activity a
                             WHERE  a.player_id = f.player_id
                               AND  a.event_date = f.first_date + INTERVAL '1 day' )
               THEN 1              -- yes: logged in on first_date + 1
               ELSE 0              -- no: absent the next day
           END AS returned_next_day
    FROM   first_login f
)
SELECT ROUND( AVG(returned_next_day)::numeric , 2 ) AS fraction
FROM   next_day_flag;

