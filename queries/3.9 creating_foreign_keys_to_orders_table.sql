-- orders_table have 120123 records while dim_card_details have 15258 which mean there are some card details that aren't in the dim_card_details
--
--selecting all the card_numbers in orders_table that are not in dim_card_details
SELECT orders_table.card_number
FROM orders_table
    LEFT JOIN dim_card_details ON orders_table.card_number = dim_card_details.card_number
WHERE dim_card_details.card_number IS NULL;
-- inserting all card detials from orders_table into dim_card_detials
INSERT INTO dim_card_details (card_number)
SELECT DISTINCT orders_table.card_number
FROM orders_table
WHERE orders_table.card_number NOT IN (
        SELECT dim_card_details.card_number
        FROM dim_card_details
    );
--
SELECT orders_table.user_uuid
FROM orders_table
    LEFT JOIN dim_users ON orders_table.user_uuid = dim_users.user_uuid
WHERE dim_users.user_uuid IS NULL;
--
INSERT INTO dim_users (user_uuid)
SELECT DISTINCT orders_table.user_uuid
FROM orders_table
WHERE orders_table.user_uuid NOT IN (
        SELECT dim_users.user_uuid
        FROM dim_users
    );
--
SELECT orders_table.store_code
FROM orders_table
    LEFT JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
WHERE dim_store_details.store_code IS NULL;
-- 
INSERT INTO dim_store_details (store_code)
SELECT DISTINCT orders_table.store_code
FROM orders_table
WHERE orders_table.store_code NOT IN (
        SELECT dim_store_details.store_code
        FROM dim_store_details
    );
--
SELECT orders_table.product_code
FROM orders_table
    LEFT JOIN dim_products ON orders_table.product_code = dim_products.product_code
WHERE dim_products.product_code IS NULL;
--
INSERT INTO dim_products (product_code)
SELECT DISTINCT orders_table.product_code
FROM orders_table
WHERE orders_table.product_code NOT IN (
        SELECT dim_products.product_code
        FROM dim_products
    );
--
--adding foreign keys
ALTER TABLE orders_table
ADD FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid);
--
ALTER TABLE orders_table
ADD FOREIGN KEY (user_uuid) REFERENCES dim_users(user_uuid);
--
ALTER TABLE orders_table
ADD FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number);
-- 
ALTER TABLE orders_table
ADD FOREIGN KEY (store_code) REFERENCES dim_store_details(store_code);
-- 
ALTER TABLE orders_table
ADD FOREIGN KEY (product_code) REFERENCES dim_products(product_code);