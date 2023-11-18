with time_concat AS(
    SELECT TO_TIMESTAMP(
            (
                year || '-' || month || '-' || day || ' ' || timestamp
            ),
            'YYYY-MM-DD HH24:MI:SS'
        ) as joined_date,
        year
    FROM dim_date_times
    ORDER BY joined_date DESC
),
time_diff as(
    SELECT year,
        joined_date,
        LEAD(joined_date, 1) OVER (
            ORDER BY joined_date DESC
        ) as time_diff
    FROM time_concat
)
SELECT year,
    AVG((joined_date - time_diff)) AS actual_time_taken
FROM time_diff
GROUP BY year
ORDER BY actual_time_taken DESC;