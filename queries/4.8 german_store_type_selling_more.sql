SELECT ROUND(
        SUM(product_quantity * dim_products.product_price)
    ) AS total_sales,
    dim_store_details.store_type AS store_type,
    dim_store_details.country_code AS country_code
FROM orders_table
    LEFT JOIN dim_products ON orders_table.product_code = dim_products.product_code
    LEFT JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
WHERE dim_store_details.country_code = 'DE'
GROUP BY store_type,
    country_code
ORDER BY total_sales;