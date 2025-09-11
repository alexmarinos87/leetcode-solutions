# Write your MySQL query statement below
SELECT
    ROUND(SUM(CASE WHEN delivery = "immediate" THEN 1.00 ELSE 0.00 END) * 100.00/ COUNT(*),2) AS immediate_percentage 
FROM(
    SELECT delivery_id, customer_id,
        CASE WHEN MIN(order_date) = MIN(customer_pref_delivery_date) THEN "immediate" ELSE "scheduled" END AS delivery,
        MIN(order_date) AS first_order
    FROM Delivery
    GROUP BY customer_id
) AS first_orders