-- HEMNET DATA ANALYZING

-- b Make a wildcard selection to checkout the data
SELECT * from hemnet
WHERE commune LIKE 'Gamla Enskede%'

-- c Find out how many rows there are in the table
SELECT COUNT(*) FROM hemnet

-- d Describe the table that you have ingested to see the columns and data types.
DESC;

-- e) Find out the 5 most expensive homes sold.
SELECT * FROM hemnet
ORDER BY final_price 
DESC 
LIMIT 5

-- f) Find out the 5 cheapest homes sold.
SELECT * FROM hemnet
ORDER BY final_price 
LIMIT 5

-- g) Find out statistics on minimum, mean, median and maximum prices of homes sold.
SELECT MIN(final_price) FROM hemnet
SELECT MAX(final_price) FROM hemnet
SELECT MEDIAN(final_price) FROM hemnet
SELECT AVG(final_price) FROM hemnet

-- eller
SELECT 
 	MIN(final_price) AS 'Minimum Price',
 	MAX(final_price) AS 'Maximum Price', 
 	AVG(final_price) AS 'Average Price'
 	FROM hemnet

-- eller för att få ut information om objekten
SELECT 'Lowest' AS price_category, address, commune, final_price
FROM hemnet
WHERE final_price = (SELECT MIN(final_price) FROM hemnet)
UNION ALL
SELECT 'Highest' AS price_category, address, commune, final_price
FROM hemnet
WHERE final_price = (SELECT MAX(final_price) FROM hemnet)
ORDER BY final_price;

-- h) Find out statistics on minimum, mean, median and maximum prices of price per area.
SELECT commune AS Commune, 
       MIN(final_price) AS 'Minimum Price', 
       MAX(final_price) AS 'Maximum Price',
       ROUND(AVG(final_price), 2) AS 'Average Price'
FROM hemnet
GROUP BY commune;

-- i) How many unique communes are represented in the dataset.
SELECT COUNT(DISTINCT commune) FROM hemnet

-- j) How many percentage of homes cost more than 10 million?
SELECT 
    (COUNT(CASE WHEN final_price > 10000000 THEN 1 END) * 100.0) / COUNT(*) AS percentage_above_10_million
FROM hemnet;

-- k) Feel free to explore anything else you find interesting in this dataset.

-- ta fram medelvärdet för kvadratmeterpris för varje kommun
SELECT commune, ROUND(AVG(price_per_area)) FROM hemnet
GROUP BY commune
ORDER BY AVG(price_per_area)
DESC

-- visa den största skillnaden mellan utropspris och slutpris
SELECT MAX(final_price - asked_price) AS "Störst skillnad"
FROM hemnet;

-- eller
SELECT commune, address, final_price - asked_price AS "Störst skillnad"
FROM hemnet
WHERE final_price - asked_price = (
    SELECT MAX(final_price - asked_price)
    FROM hemnet)

-- visa skillanderna mellan uttrop och slutpris i stigande ordning
SELECT commune, address, MAX(final_price - asked_price) AS "Störst skillnad"
FROM hemnet
GROUP BY commune, address
ORDER BY MAX(final_price - asked_price)
ASC

