SELECT
    p.product_id,
    COALESCE(
        ( SELECT new_price
          FROM   Products AS px
          WHERE  px.product_id = p.product_id
            AND  px.change_date <= '2019-08-16'
          ORDER  BY px.change_date DESC          -- latest price on or before the date
          LIMIT  1                               -- pick that single price
        ),
        10                                         -- fallback: still at initial price
    ) AS price
FROM  (SELECT DISTINCT product_id FROM Products) AS p;

