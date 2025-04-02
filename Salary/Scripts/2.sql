SELECT * FROM salary_sek

--  a) Count number of Data engineers jobs. For simplicity just go for job_title Data Engineer.
SELECT COUNT(job_title) FROM salary_sek
WHERE job_title = 'Data Engineer'

--  b) Count number of unique job titles in total.
SELECT COUNT(DISTINCT job_title) FROM salary_sek


--  c) Find out how many jobs that goes into each salary level.
SELECT COUNT(job_title), salary_level FROM salary_sek
GROUP BY salary_level


--  d) Find out the median and mean salaries for each seniority levels.
SELECT 
	MEDIAN(salary_in_sek) AS "Medianlön i SEK",
	ROUND(MEAN(salary_in_sek)) AS "Medellön i SEK"
FROM salary_sek

--  e) Find out the top earning job titles based on their median salaries and how much they earn.
SELECT job_title, MEDIAN(salary_in_sek) AS medelvärde FROM salary_sek
GROUP BY job_title
ORDER BY medelvärde
DESC
LIMIT 10

--  f) How many percentage of the jobs are fully remote, 50 percent remote and fully not remote.
SELECT 
    (COUNT(CASE WHEN remote_ratio = 100 THEN 1 END) * 100.0) / COUNT(*) AS percentage_remote
FROM salary_sek;

--  g) Pick out a job title of interest and figure out if company size affects the salary. Make a simple analysis as a comprehensive one requires causality investigations which are much harder to find.
SELECT MEAN(salary_in_sek) AS salary, company_size FROM salary_sek
WHERE job_title = 'Data Analyst' 
GROUP BY company_size
ORDER BY salary
DESC

--  h) Feel free to explore other things

-- vilken storlek på kontor jobbar de flesta juniorer (EN)
SELECT COUNT(experience_level), company_size, ROUND(MEDIAN(salary_in_sek)) AS medianlon
FROM main.salary_sek
WHERE experience_level = 'EN'
GROUP BY company_size 
ORDER BY medianlon
DESC
