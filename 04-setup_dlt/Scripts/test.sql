SELECT * FROM staging.netflix LIMIT 10;

SELECT * FROM staging.netflix 
WHERE imdb_score > 4
ORDER BY imdb_score
DESC

SELECT * FROM staging.netflix 
WHERE imdb_score < 4 AND language = 'English'
ORDER BY imdb_score
ASC

SELECT * FROM staging.netflix
WHERE genre = 'Documentary' AND Language != 'English'
ORDER BY premiere -- blir fel, visar månaderna i stället för årtalen
ASC

-- Måste konvertera till datetime för att sortera efter år
SELECT * FROM staging.netflix
WHERE genre = 'Documentary' AND Language != 'English'
ORDER BY STRPTIME(premiere, '%B %d, %Y') ASC;

-- Visa svenska filmer
SELECT * FROM staging.netflix
WHERE Language LIKE '%Swedish%'
ORDER BY STRPTIME(premiere, '%B %d, %Y') ASC;
