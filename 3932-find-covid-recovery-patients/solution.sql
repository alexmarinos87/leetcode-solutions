WITH ordered_tests AS (
    SELECT
        patient_id,
        test_date,
        result,
        ROW_NUMBER() OVER (PARTITION BY patient_id ORDER BY test_date) AS rn
    FROM covid_tests
),
first_positive AS (
    SELECT
        patient_id,
        MIN(test_date) AS first_positive_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
),
first_negative_after AS (
    SELECT
        c.patient_id,
        MIN(c.test_date) AS first_negative_date
    FROM covid_tests c
    JOIN first_positive p
        ON c.patient_id = p.patient_id
       AND c.test_date > p.first_positive_date
    WHERE c.result = 'Negative'
    GROUP BY c.patient_id
),
recovered AS (
    SELECT
        p.patient_id,
        p.first_positive_date,
        n.first_negative_date,
        DATEDIFF(n.first_negative_date, p.first_positive_date) AS recovery_time
    FROM first_positive p
    JOIN first_negative_after n
        ON p.patient_id = n.patient_id
)
SELECT
    pa.patient_id,
    pa.patient_name,
    pa.age,
    r.recovery_time
FROM recovered r
JOIN patients pa ON pa.patient_id = r.patient_id
ORDER BY r.recovery_time ASC, pa.patient_name ASC;

