WITH first_orders AS (
    /* each customer's earliest order */
    SELECT  d.*
    FROM    delivery d
    JOIN   (SELECT customer_id,
                   MIN(order_date) AS first_date
            FROM   delivery
            GROUP  BY customer_id) f
      ON  d.customer_id = f.customer_id
     AND  d.order_date  = f.first_date
)
SELECT ROUND(
           100.0 * SUM( (order_date = customer_pref_delivery_date)::int )   -- immediate first orders
                 / COUNT(*)                                                -- total first orders
           , 2) AS immediate_percentage
FROM   first_orders;    

