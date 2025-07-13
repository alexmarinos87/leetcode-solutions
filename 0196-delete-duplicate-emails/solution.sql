/* Step 1: flag the “extra” rows */
WITH duplicates AS (
    SELECT
        id,
        ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
    FROM Person
)

/* Step 2: delete every row whose row-number > 1 */
DELETE FROM Person
WHERE id IN (SELECT id
             FROM duplicates
             WHERE rn > 1);
