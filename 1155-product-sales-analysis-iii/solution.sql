-- find the first year each product was sold …
WITH first_sale AS (
    SELECT product_id,
           MIN(`year`) AS first_year
    FROM   Sales
    GROUP  BY product_id
)
-- … and return every sale made in that first year
SELECT  s.product_id,
        f.first_year,
        s.quantity,
        s.price
FROM    Sales AS s
JOIN    first_sale AS f
       ON s.product_id = f.product_id
      AND s.`year`    = f.first_year;
