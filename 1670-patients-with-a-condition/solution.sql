SELECT
    patient_id,
    patient_name,
    conditions
FROM Patients
/* ────────── core test ──────────
   (^| )      → start-of-string OR a single space
   DIAB1      → prefix we care about
*/
WHERE conditions ~  '(^| )DIAB1'
      -- SQL Server:   conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%'
;

