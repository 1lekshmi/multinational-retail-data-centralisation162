-- renaming removed column to still_available
ALTER TABLE dim_products
    RENAME COLUMN removed to still_available;
--max length of EAN
SELECT length(CAST("EAN" AS TEXT))
FROM dim_products
GROUP BY "EAN"
ORDER BY length(CAST("EAN" AS TEXT)) DESC;
--17
--max length of product code
SELECT length(CAST(product_code AS TEXT))
FROM dim_products
GROUP BY product_code
ORDER BY length(CAST(product_code AS TEXT)) DESC;
--11
--max length of weight class
SELECT length(CAST(weight_class AS TEXT))
FROM dim_products
GROUP BY weight_class
ORDER BY length(CAST(weight_class AS TEXT)) DESC;
--14
--altering the data type
ALTER TABLE dim_products
ALTER COLUMN product_price TYPE FLOAT USING CAST(product_price AS FLOAT),
    ALTER COLUMN weight TYPE FLOAT USING CAST(weight AS FLOAT),
    ALTER COLUMN "EAN" TYPE VARCHAR(17),
    ALTER COLUMN product_code TYPE VARCHAR(11),
    ALTER COLUMN date_added TYPE DATE USING CAST(date_added AS DATE),
    ALTER COLUMN uuid TYPE UUID USING uuid::UUID,
    ALTER COLUMN still_available TYPE BOOL USING(still_available = 'Still_avaliable'),
    ALTER COLUMN weight_class TYPE VARCHAR(14);