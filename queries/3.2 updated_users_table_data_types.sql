-- finding the max length of country code
SELECT length(cast(country_code as text))
FROM dim_users
GROUP BY country_code
ORDER BY length(cast(country_code as text)) DESC;
-- 3
-- changing the data type
ALTER TABLE dim_users
ALTER COLUMN first_name TYPE VARCHAR(255),
    ALTER COLUMN last_name TYPE VARCHAR(255),
    ALTER COLUMN date_of_birth TYPE DATE USING CAST(date_of_birth AS DATE),
    ALTER COLUMN country_code TYPE VARCHAR(3),
    ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID,
    ALTER COLUMN join_date TYPE DATE USING CAST(join_date AS DATE);