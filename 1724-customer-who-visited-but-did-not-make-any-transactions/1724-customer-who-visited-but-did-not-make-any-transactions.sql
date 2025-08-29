# Write your MySQL query statement below
SELECT
    v.customer_id,
    COUNT(v.visit_id) - COUNT(v.visit_id = t.visit_id) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t
ON v.visit_id = t.visit_id
GROUP BY v.customer_id HAVING COUNT(v.visit_id) - COUNT(v.visit_id = t.visit_id) != 0;