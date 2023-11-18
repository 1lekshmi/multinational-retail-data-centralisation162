-- finding the maximum length of card_number
SELECT length(cast(card_number as text))
FROM orders_table
GROUP BY card_number
ORDER BY length(cast(card_number as text)) DESC;
-- -- -- 19
-- -- finding the maximum length of store_code
SELECT length(cast(store_code as text))
FROM orders_table
GROUP BY store_code
ORDER BY length(cast(store_code as text)) DESC;
-- -- 12
--finding the maximum length of product code
SELECT length(cast(product_code as text))
FROM orders_table
GROUP BY product_code
ORDER BY length(cast(product_code as text)) DESC;
-- 11
-- altering the data types
ALTER TABLE orders_table
ALTER COLUMN card_number TYPE VARCHAR(19),
    ALTER COLUMN store_code TYPE VARCHAR(12),
    ALTER COLUMN product_code TYPE VARCHAR(11),
    ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID,
    ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID,
    ALTER COLUMN product_quantity TYPE SMALLINT;