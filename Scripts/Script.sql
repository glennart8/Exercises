SELECT * FROM salaries

-- ändra förkorningarna i kolumnen
UPDATE salaries
SET employment_type = 'Full time'
WHERE employment_type = 'FT';

UPDATE salaries
SET employment_type = 'Contract'
WHERE employment_type = 'CT';

UPDATE salaries
SET employment_type = 'Part time'
WHERE employment_type = 'PT';

UPDATE salaries
SET employment_type = 'Freelance'
WHERE employment_type = 'FT';

--  b) Do similar for company size, but you have to figure out what the abbreviations could stand for.
UPDATE salaries
SET company_size = CASE
	WHEN company_size = 'M' THEN 'Medium'
	WHEN company_size = 'L' THEN 'Large'
	WHEN company_size = 'S' THEN 'Small'
END

--  c) Make a salary column with Swedish currency for yearly salary.

-- skapa kolumn
ALTER TABLE salaries
ADD salary_in_sek DECIMAL(15, 2);
-- beräkna och lägg in värdet i kolumnen
UPDATE salaries
SET salary_in_sek = salary * 10.03


--  d) Make a salary column with Swedish currency for monthly salary.


--  e) Make a salary_level column with the following categories: low, medium, high, insanely_high. Decide your thresholds for each category. Make it base on the monthly salary in SEK.


--  f) Choose the following columns to include in your table: experience_level, employment_type, job_title, salary_annual_sek, salary_monthly_sek, remote_ratio, company_size, salary_level


--  g) Think of other transformation that you want to do.
