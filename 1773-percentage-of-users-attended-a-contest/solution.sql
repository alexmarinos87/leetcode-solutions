SELECT
  r.contest_id,
  ROUND(
    COUNT(DISTINCT r.user_id) * 100.0
    / (SELECT COUNT(*) FROM Users),
    2
  ) AS percentage
FROM Register AS r
GROUP BY r.contest_id
ORDER BY
  percentage DESC,
  r.contest_id ASC;

-- Other method:
--WITH
  -- 1) Count how many users registered in each contest
  -- regs AS (
   -- SELECT
    --  contest_id,
    --  COUNT(DISTINCT user_id) AS reg_count
    -- FROM Register
    -- GROUP BY contest_id
  -- ),
  -- 2) Compute the total number of users once
  -- totals AS (
    -- SELECT
      -- COUNT(*) AS total_users
    -- FROM Users
  -- )

-- 3) Cross join so `total_users` is available alongside each contest’s reg_count
-- SELECT
  -- r.contest_id,
  -- ROUND(
    -- r.reg_count * 100.0
    --/  t.total_users,
    -- 2
  -- ) AS percentage
-- FROM regs AS r
-- CROSS JOIN totals AS t
-- ORDER BY
  -- percentage DESC,
  -- r.contest_id ASC;

