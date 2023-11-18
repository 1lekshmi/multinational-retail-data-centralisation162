SELECT COUNT(product_quantity) AS number_of_sales,
    SUM(product_quantity) AS product_quantity_count,
    CASE
        WHEN dim_store_details.store_type = 'Web Portal' THEN 'Web'
        ELSE 'Offline'
    END AS location
FROM orders_table
    LEFT JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
GROUP BY location
ORDER BY product_quantity_count;