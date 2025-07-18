/* Treat friendship as undirected:
        each row contributes one friend to both participants            */
WITH all_links AS (
    SELECT requester_id AS id , accepter_id AS friend FROM RequestAccepted
    UNION ALL
    SELECT accepter_id  AS id , requester_id AS friend FROM RequestAccepted
)

/*  Count distinct friends per person and pick the top one */
SELECT id,
       COUNT(DISTINCT friend) AS num
FROM   all_links
GROUP  BY id
ORDER  BY num DESC            -- highest friend-count first
LIMIT  1;                     -- test guarantees a single winner

