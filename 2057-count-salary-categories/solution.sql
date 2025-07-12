/* 1️⃣  Put every account into one of the three salary buckets */
WITH grouped AS (
    SELECT
        CASE
            WHEN income < 20000               THEN 'Low Salary'
            WHEN income <= 50000              THEN 'Average Salary'   -- 20k-50k inclusive
            ELSE                                   'High Salary'
        END AS category,
        COUNT(*) AS accounts_count
    FROM Accounts
    GROUP BY category
),

/* 2️⃣  Hard-code the list of required categories */
cats AS (
    SELECT 'Low Salary'     AS category UNION ALL
    SELECT 'Average Salary'                UNION ALL
    SELECT 'High Salary'
)

/* 3️⃣  Join the two: missing categories => NULL => COALESCE -> 0 */
SELECT
    c.category,
    COALESCE(g.accounts_count, 0) AS accounts_count
FROM cats      AS c
LEFT JOIN grouped AS g
    ON g.category = c.category;

