WITH latest AS (
    SELECT product_id,
           new_price,
           ROW_NUMBER() OVER (
               PARTITION BY product_id
               ORDER BY change_date DESC
           ) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)
SELECT
    p.product_id,
    COALESCE(MAX(CASE WHEN l.rn = 1 THEN l.new_price END), 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) AS p
LEFT JOIN latest AS l
  ON l.product_id = p.product_id
GROUP BY p.product_id;

