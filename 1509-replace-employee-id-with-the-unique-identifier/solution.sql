SELECT
    uni.unique_id,
    e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS uni
ON e.id = uni.id
ORDER BY uni.unique_id DESC;
