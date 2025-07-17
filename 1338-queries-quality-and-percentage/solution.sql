WITH
  q AS (
    SELECT
      query_name,
      AVG(rating * 1.0 / position) AS avg_ratio
    FROM Queries
    GROUP BY query_name
  ),
  pqp AS (
    SELECT
      query_name,
      SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS pct_poor
    FROM Queries
    GROUP BY query_name
  )
SELECT
  q.query_name,
  ROUND(q.avg_ratio, 2)           AS quality,
  ROUND(pqp.pct_poor,   2)        AS poor_query_percentage
FROM q
JOIN pqp USING (query_name);


