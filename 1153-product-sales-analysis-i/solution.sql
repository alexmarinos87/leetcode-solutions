SELECT
    p.product_name,
    s.price,
    s.year
FROM
    Sales AS s 
LEFT JOIN
    Product AS p
ON
    s.product_id = p.product_id;
