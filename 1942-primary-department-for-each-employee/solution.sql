SELECT
    employee_id,
    COALESCE(                                    -- pick the primary dept if it exists …
        MAX(CASE WHEN primary_flag = 'Y' THEN department_id END),
        MAX(department_id)                       -- … otherwise the (only) dept they have
    ) AS department_id
FROM Employee
GROUP BY employee_id;

