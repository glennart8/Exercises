SELECT * FROM salaries

--A
UPDATE salaries
SET employment_type = CASE
	WHEN employment_type = 'FT' THEN 'Full Time'
	WHEN employment_type = 'PT' THEN 'Part Time'
	WHEN employment_type = 'FL' THEN 'Freelance'
	WHEN employment_type = 'CT' THEN 'Contract'
END

--B
UPDATE salaries
SET company_size = CASE
	WHEN company_size = 'S' THEN 'Small'
	WHEN company_size = 'M' THEN 'Medium'
	WHEN company_size = 'L' THEN 'Large'
END

--C

-- lägg till ny kolumn
ALTER TABLE salaries
ADD salary_in_sek DECIMAL(15, 2)

-- lägg in bärdet från salary och skriv ut i svenska kronor
UPDATE salaries
SET salary_in_sek = salary * 10.03

--D Make a salary column with Swedish currency for monthly salary.
ALTER TABLE salaries
ADD mountly_salary_sek DECIMAL(15, 2)

UPDATE salaries
SET mountly_salary_sek = salary_in_sek / 12

--E  Make a salary_level column with the following categories: low, medium, high, insanely_high. Decide your thresholds for each category. Make it base on the monthly salary in SEK.
ALTER TABLE salaries
ADD salary_level VARCHAR(250)

UPDATE salaries
SET salary_level = CASE
	WHEN mountly_salary_sek BETWEEN 0 AND 50000 THEN 'Low'
	WHEN mountly_salary_sek BETWEEN 50000 AND 100000 THEN 'Medium'
	WHEN mountly_salary_sek BETWEEN 100000 AND 150000 THEN 'High'
	WHEN mountly_salary_sek > 150000 THEN 'Insanely High'
END

--F Choose the following columns to include in your table: experience_level, employment_type, job_title, salary_annual_sek, salary_monthly_sek, remote_ratio, company_size, salary_level

-- skapar en ny tabell med dessa kolumner
CREATE TABLE salary_sek AS 
SELECT experience_level, employment_type, job_title, salary_in_sek, mountly_salary_sek, remote_ratio, company_size, salary_level FROM salaries












