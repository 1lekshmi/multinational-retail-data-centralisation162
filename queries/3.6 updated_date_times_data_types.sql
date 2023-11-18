--max length for month
SELECT length(CAST(month AS TEXT))
FROM dim_date_times
GROUP BY month
ORDER BY length(CAST(month AS TEXT)) DESC;
--2
--max length for year
SELECT length(CAST(year AS TEXT))
FROM dim_date_times
GROUP BY year
ORDER BY length(CAST(year AS TEXT)) DESC;
--4
--max length for day
SELECT length(CAST(day AS TEXT))
FROM dim_date_times
GROUP BY day
ORDER BY length(CAST(day AS TEXT)) DESC;
--2
--max length for time_period
SELECT length(CAST(time_period AS TEXT))
FROM dim_date_times
GROUP BY time_period
ORDER BY length(CAST(time_period AS TEXT)) DESC;
--10
--altering data types
ALTER TABLE dim_date_times
ALTER COLUMN month TYPE VARCHAR(2),
    ALTER COLUMN year TYPE VARCHAR(4),
    ALTER COLUMN day TYPE VARCHAR(2),
    ALTER COLUMN time_period TYPE VARCHAR(10),
    ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;