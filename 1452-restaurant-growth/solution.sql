/* 1️⃣  Collapse many receipts per day into one “daily total” row */
WITH daily AS (
    SELECT
        visited_on,
        SUM(amount) AS amount                 -- total sales that day
    FROM Customer
    GROUP BY visited_on
),

/* 2️⃣  Compute 7-day running totals and averages */
windowed AS (
    SELECT
        visited_on,
        /* current day + six previous days */
        SUM(amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount_7d,
        ROUND(AVG(amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ), 2) AS avg_7d,
        ROW_NUMBER() OVER (ORDER BY visited_on) AS rn   -- count how many rows seen so far
    FROM daily
)

/* 3️⃣  Emit rows only after we’ve seen seven distinct days */
SELECT
    visited_on,
    amount_7d      AS amount,
    avg_7d         AS average_amount
FROM   windowed
WHERE  rn >= 7                          -- guarantees a full 7-day window
ORDER  BY visited_on;

