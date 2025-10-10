WITH fuel_efficiency AS (
    SELECT
        trip_id,
        driver_id,
        trip_date,
        distance_km,
        fuel_consumed,
        distance_km / fuel_consumed AS efficiency
    FROM trips
),
half_year_efficiency AS (
    SELECT
        driver_id,
        CASE
            WHEN MONTH(trip_date) BETWEEN 1 AND 6 THEN 'first_half'
            ELSE 'second_half'
        END AS part_year,
        AVG(distance_km / fuel_consumed) AS avg_efficiency
    FROM fuel_efficiency
    GROUP BY driver_id,
             CASE WHEN MONTH(trip_date) BETWEEN 1 AND 6 THEN 'first_half' ELSE 'second_half' END
),
driver_avg_comparison AS (
    SELECT
        driver_id,
        MAX(CASE WHEN part_year = 'first_half' THEN avg_efficiency END) AS first_half_avg,
        MAX(CASE WHEN part_year = 'second_half' THEN avg_efficiency END) AS second_half_avg
    FROM half_year_efficiency
    GROUP BY driver_id
),
improved_drivers AS (
    SELECT
        driver_id,
        ROUND(first_half_avg, 2) AS first_half_avg,
        ROUND(second_half_avg, 2) AS second_half_avg,
        ROUND(second_half_avg - first_half_avg, 2) AS efficiency_improvement
    FROM driver_avg_comparison
    WHERE first_half_avg IS NOT NULL
      AND second_half_avg IS NOT NULL
      AND second_half_avg > first_half_avg
)
SELECT
    d.driver_id,
    dr.driver_name,
    d.first_half_avg,
    d.second_half_avg,
    d.efficiency_improvement
FROM improved_drivers d
JOIN drivers dr
  ON d.driver_id = dr.driver_id
ORDER BY d.efficiency_improvement DESC, dr.driver_name ASC;

