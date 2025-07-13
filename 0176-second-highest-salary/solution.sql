WITH ranked AS (
    SELECT
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM Employee
)
SELECT
    MAX(salary) AS SecondHighestSalary      -- MAX() returns NULL if no row
FROM ranked
WHERE rnk = 2;                              -- keep only the “second” rank

