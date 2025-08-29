# Write your MySQL query statement below
SELECT
    uni.unique_id,
    e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS uni
ON e.id = uni.id;
