SELECT ROUND(
        SUM(product_quantity * dim_products.product_price)
    ) AS total_sales,
    dim_date_times.year AS year,
    dim_date_times.month AS month
FROM orders_table
    LEFT JOIN dim_products ON orders_table.product_code = dim_products.product_code
    LEFT JOIN dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
GROUP BY month,
    year
ORDER BY total_sales DESC;