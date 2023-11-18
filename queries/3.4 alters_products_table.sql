--removes the £ sign
UPDATE dim_products
SET product_price = REPLACE(product_price, '£', '');
--adds the weight class column
ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR;
--assigning the correct weight class according to the weight
UPDATE dim_products
SET weight_class = CASE
        WHEN weight < 2.0 THEN 'Light'
        WHEN weight >= 2.0
        AND weight < 40.0 THEN 'Mid_Sized'
        WHEN weight >= 40.0
        AND weight < 140 THEN 'Heavy'
        WHEN weight >= 140.0 THEN 'Truck_Required'
    END;