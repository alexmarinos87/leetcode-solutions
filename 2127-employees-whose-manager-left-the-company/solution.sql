SELECT e.employee_id
FROM   Employees AS e
LEFT   JOIN Employees AS m             -- try to find this employee’s manager
       ON  e.manager_id = m.employee_id
WHERE  e.salary      < 30000           -- salary condition
  AND  e.manager_id IS NOT NULL        -- they do have (or had) a manager
  AND  m.employee_id IS NULL           -- …but that manager no longer exists
ORDER  BY e.employee_id;
