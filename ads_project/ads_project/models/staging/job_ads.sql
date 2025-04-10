-- models/staging/job_ads.sql

WITH staging_data AS (
    SELECT * FROM {{ source('staging', 'data_field_job_ads') }}
)

SELECT
    id AS job_id,
    headline AS job_title,
    employer__name AS company_name,
    workplace_address__city AS city,
    workplace_address__region AS region,
    employment_type__label AS employment_type,
    salary_type__label AS salary_type,
    scope_of_work__min AS min_hours,
    scope_of_work__max AS max_hours,
    publication_date,
    application_details__email AS contact_email,
    application_details__reference AS contact_name,
    application_details__other AS contact_phone,
    description__text AS job_description,
    relevance -- extra kolumn
FROM staging_data
