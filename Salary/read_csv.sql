-- skapa databas i vs code först

CREATE TABLE salaries AS  
SELECT * FROM read_csv_auto('data/salaries(2).csv');



--  sedan i terminalen
--  duckdb hemnet.duckdb < read_csv.sql     # använder duckdb för att köra sql scriptet I CMD ANNARS FUNKAR DET INTE
-- avsluta connection för att ansluta i dbeaver