# Write your MySQL query statement below
WITH all_users AS(
    SELECT COUNT(*) AS count_all_users FROM Users
),
contest_users AS(
    SELECT
        contest_id,
        COUNT(DISTINCT user_id) AS registered_users
    FROM Register
    GROUP BY contest_id
)
SELECT cu.contest_id, ROUND(cu.registered_users *100.00 /au.count_all_users,2) AS percentage
FROM contest_users cu
CROSS JOIN all_users au
ORDER BY percentage DESC, cu.contest_id ASC;