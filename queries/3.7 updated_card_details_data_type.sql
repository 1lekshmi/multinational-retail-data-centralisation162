--max length of card_number
SELECT length(CAST(card_number AS TEXT))
FROM dim_card_details
GROUP BY card_number
ORDER BY length(CAST(card_number AS TEXT)) DESC;
--19
--max length of expiry date
SELECT length(CAST(expiry_date AS TEXT))
FROM dim_card_details
GROUP BY expiry_date
ORDER BY length(CAST(expiry_date AS TEXT)) DESC;
--5
--altering data types
ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE VARCHAR(19),
    ALTER COLUMN expiry_date TYPE VARCHAR(5),
    ALTER COLUMN date_payment_confirmed TYPE DATE USING CAST(date_payment_confirmed AS DATE);