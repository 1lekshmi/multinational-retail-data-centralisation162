-- date_uuid = dim_date_times
--user_uuid = dim_users
--card_number = dim_card_details
--store_code = dim_store_details
--product_code = dim_products
--product_quantity
--- 
ALTER TABLE dim_date_times
ADD PRIMARY KEY (date_uuid);
--
ALTER TABLE dim_users
ADD PRIMARY KEY (user_uuid);
--
ALTER TABLE dim_card_details
ADD PRIMARY KEY (card_number);
--
ALTER TABLE dim_store_details
ADD PRIMARY KEY (store_code);
--
ALTER TABLE dim_products
ADD PRIMARY KEY (product_code);