# Write your MySQL query statement below
SELECT euni.unique_id,
        e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS euni
ON e.id = euni.id;

