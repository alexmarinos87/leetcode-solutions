SELECT m.name
FROM Employee AS m
JOIN (
   SELECT managerId
   FROM Employee
   GROUP BY managerId
   HAVING COUNT(*) >= 5
) AS grp
  ON m.id = grp.managerId;

