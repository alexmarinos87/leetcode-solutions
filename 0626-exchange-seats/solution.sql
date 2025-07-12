/* get total rows once so we know whether the “next” row exists */
WITH max_row AS (
    SELECT MAX(id) AS max_id
    FROM   Seat
)

SELECT
    /* new id after swapping rules */
    CASE
        /* odd row that is **not** the last one → move forward by 1 */
        WHEN s.id % 2 = 1 AND s.id + 1 <= m.max_id THEN s.id + 1
        /* even row → move back by 1 */
        WHEN s.id % 2 = 0                               THEN s.id - 1
        /* the very last row of an odd set → stays put */
        ELSE                                                 s.id
    END AS id,
    s.student
FROM Seat   AS s
CROSS JOIN max_row AS m          -- just to read m.max_id in the CASE
ORDER BY id;                     -- final result must be id-ascending

