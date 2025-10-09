WITH ranked_reviews AS (
    SELECT
        employee_id,
        review_date,
        rating,
        ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY review_date DESC) AS rn
    FROM performance_reviews
),
last_three AS (
    SELECT
        employee_id,
        rating,
        rn
    FROM ranked_reviews
    WHERE rn <= 3
),
aggregated AS (
    SELECT
        employee_id,
        MAX(CASE WHEN rn = 1 THEN rating END) AS latest_rating,
        MAX(CASE WHEN rn = 2 THEN rating END) AS mid_rating,
        MAX(CASE WHEN rn = 3 THEN rating END) AS earliest_rating
    FROM last_three
    GROUP BY employee_id
),
improving AS (
    SELECT
        employee_id,
        (latest_rating - earliest_rating) AS improvement_score
    FROM aggregated
    WHERE earliest_rating < mid_rating
      AND mid_rating < latest_rating
)
SELECT
    e.employee_id,
    e.name,
    i.improvement_score
FROM improving i
JOIN employees e ON e.employee_id = i.employee_id
ORDER BY i.improvement_score DESC, e.name ASC;
