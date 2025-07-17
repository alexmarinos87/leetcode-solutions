WITH
  tot AS (
    SELECT
      to_char(trans_date, 'YYYY-MM') AS month,
      country,
      COUNT(*)            AS trans_count,
      SUM(amount)         AS trans_total_amount
    FROM Transactions
    GROUP BY 1,2
  ),
  app AS (
    SELECT
      to_char(trans_date, 'YYYY-MM') AS month,
      country,
      COUNT(*)            AS approved_count,
      SUM(amount)         AS approved_total_amount
    FROM Transactions
    WHERE state = 'approved'
    GROUP BY 1,2
  )
SELECT
  tot.month,
  tot.country,
  tot.trans_count,
  COALESCE(app.approved_count,       0) AS approved_count,
  tot.trans_total_amount,
  COALESCE(app.approved_total_amount, 0) AS approved_total_amount
FROM tot
LEFT JOIN app
  ON tot.month = app.month
 AND tot.country IS NOT DISTINCT FROM app.country;

-- Other approach
-- SELECT
  -- to_char(trans_date, 'YYYY-MM')               AS month,                  -- YYYY-MM bucket
  -- country,                                                         
  -- COUNT(id)                                     AS trans_count,           -- total transactions
  -- COUNT(id) FILTER (WHERE state='approved')     AS approved_count,        -- approved transactions
  -- SUM(amount)                                   AS trans_total_amount,    -- total amount
  -- COALESCE(
    -- SUM(amount) FILTER (WHERE state='approved'),
    -- 0
  -- )                                              AS approved_total_amount  -- approved amount (0 if none)
-- FROM transactions
-- GROUP BY 1,2;

