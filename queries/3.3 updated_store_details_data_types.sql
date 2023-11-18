-- finding the max length of store code
SELECT length(CAST(store_code AS TEXT))
FROM dim_store_details
GROUP BY store_code
ORDER BY length(CAST(store_code AS TEXT)) DESC;
--12
-- finding the max length of country_code
SELECT length(CAST(country_code AS TEXT))
FROM dim_store_details
GROUP BY country_code
ORDER BY length(CAST(country_code AS TEXT)) DESC;
--2
--changing N/A to NULL
UPDATE dim_store_details
SET address = NULL
WHERE address = 'N/A';
--
UPDATE dim_store_details
SET longitude = NULL
WHERE longitude = 'N/A';
--
UPDATE dim_store_details
SET locality = NULL
WHERE locality = 'N/A';
--changing data type
ALTER TABLE dim_store_details
ALTER COLUMN longitude TYPE FLOAT USING CAST(longitude AS FLOAT),
    ALTER COLUMN locality TYPE VARCHAR(255),
    ALTER COLUMN store_code TYPE VARCHAR(12),
    ALTER COLUMN staff_numbers TYPE SMALLINT,
    ALTER COLUMN opening_date TYPE DATE USING CAST(opening_date AS DATE),
    ALTER COLUMN store_type TYPE VARCHAR(255),
    ALTER COLUMN latitude TYPE FLOAT USING CAST(latitude AS FLOAT),
    ALTER COLUMN country_code TYPE VARCHAR(2),
    ALTER COLUMN continent TYPE VARCHAR(255);