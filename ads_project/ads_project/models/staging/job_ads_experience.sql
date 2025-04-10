WITH job_ads_data AS (
    SELECT
        job_id,  -- Använd rätt alias istället för "id" OSV.
        job_title,  
        company_name,
        city,
        region,
        employment_type,
        salary_type,
        min_hours,
        max_hours,
        publication_date,
        contact_email,
        contact_name,
        contact_phone,
        job_description
    FROM {{ ref('job_ads') }}
),
experience_data AS (
    SELECT 
        job_id,
        {{ convert_to_lowercase('label') }} AS required_experience
    FROM staging.data_field_job_ads__must_have__work_experiences
)
SELECT 
    job_ads_data.*, 
    experience_data.required_experience
FROM job_ads_data
LEFT JOIN experience_data
    ON job_ads_data.job_id = experience_data.job_id
