# Write your MySQL query statement below
SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person As p
LEFT JOIN Address AS a
ON p.personId = a.personId;
