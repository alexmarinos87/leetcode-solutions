/* 1️⃣  Aggregate February-2020 orders per product */
WITH feb AS (
    SELECT
        product_id,
        SUM(unit) AS unit
    FROM Orders
    WHERE order_date >= '2020-02-01'   -- first day of Feb-2020
      AND order_date <  '2020-03-01'   -- open upper bound (safer than 02-29)
    GROUP BY product_id
    HAVING SUM(unit) >= 100            -- keep products with ≥ 100 units
)

/* 2️⃣  Add product names and return the result */
SELECT
    p.product_name,
    f.unit
FROM feb       AS f
JOIN Products  AS p  ON p.product_id = f.product_id;

