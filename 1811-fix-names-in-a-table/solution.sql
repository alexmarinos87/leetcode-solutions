SELECT
    user_id,
    CONCAT(
        UPPER(SUBSTRING(name, 1, 1)),    -- first letter → uppercase
        LOWER(SUBSTRING(name, 2))        -- rest         → lowercase
    ) AS name
FROM Users
ORDER BY user_id;

