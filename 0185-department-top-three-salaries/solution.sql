WITH ranked AS (
    SELECT
        d.name  AS Department,
        e.name  AS Employee,
        e.salary,
        DENSE_RANK() OVER (                 -- ① rank *unique* salaries
            PARTITION BY e.departmentId     --    separately per department
            ORDER BY     e.salary DESC
        ) AS sal_rank
    FROM Employee   AS e
    JOIN Department AS d
      ON d.id = e.departmentId
)
SELECT
    Department,
    Employee,
    salary AS Salary
FROM ranked
WHERE sal_rank <= 3                         -- ② keep only the top-3 ranks
ORDER BY Department, salary DESC;           -- (any order is acceptable)

