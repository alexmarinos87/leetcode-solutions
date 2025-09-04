SELECT m.name
FROM Employee AS m
JOIN Employee AS r
  ON r.managerId = m.id
GROUP BY m.id, m.name
HAVING COUNT(*) >= 5;

