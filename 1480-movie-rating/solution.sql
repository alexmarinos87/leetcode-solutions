/* 1️⃣  Count how many ratings each user has written */
WITH user_counts AS (
    SELECT u.name,
           COUNT(*) AS reviews
    FROM   Users        AS u
    JOIN   MovieRating  AS r  ON r.user_id = u.user_id
    GROUP  BY u.name
),

/* 2️⃣  Pick the single user with the most reviews (tie → lexicographically first) */
best_user AS (
    SELECT name      AS results
    FROM   user_counts
    ORDER  BY reviews DESC,          -- most reviews first …
              name                  -- … tie-breaker
    LIMIT  1
),

/* 3️⃣  Average rating per movie in Feb-2020 */
feb_averages AS (
    SELECT m.title,
           AVG(r.rating) AS avg_rating
    FROM   Movies       AS m
    JOIN   MovieRating  AS r  ON r.movie_id = m.movie_id
    WHERE  r.created_at >= '2020-02-01'
      AND  r.created_at <  '2020-03-01'      -- open upper bound is safe
    GROUP  BY m.title
),

/* 4️⃣  Pick the single top-rated movie (tie → lexicographically first) */
best_movie AS (
    SELECT title     AS results
    FROM   feb_averages
    ORDER  BY avg_rating DESC,       -- highest average first …
              title                 -- … tie-breaker
    LIMIT  1
)

/* 5️⃣  Stitch the two answers together */
SELECT results FROM best_user
UNION ALL
SELECT results FROM best_movie;

