SELECT
    s.user_id,
    -- count how many “confirmed” rows,
    -- divide by total rows, null‐safe, default to 0
    ROUND(COALESCE(
      SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END)
      * 1.0
      / NULLIF(COUNT(c.action), 0)
    , 0),2) AS confirmation_rate
FROM
    Signups AS s
LEFT JOIN
    Confirmations AS c
  ON
    s.user_id = c.user_id
GROUP BY
    s.user_id;

