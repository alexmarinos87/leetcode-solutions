-- Step 1: find managers with ≥5 reports
WITH mgr_counts AS (
  SELECT
    managerId,
    COUNT(*) AS cnt_reports
  FROM Employee
  WHERE managerId IS NOT NULL
  GROUP BY managerId
  HAVING COUNT(*) >= 5
)
-- Step 2: join back to get manager names
SELECT
  e.name
FROM
  mgr_counts AS mc
  JOIN Employee AS e
    ON e.id = mc.managerId;
