WITH staging_data AS (
    SELECT * FROM {{ ref('original_headline') }}
)

SELECT 
    CASE
        WHEN headline = 'Data Engineer' THEN 'Junior Data Engineer' -- CASE-sensitive och enkelfnuttar!
        ELSE headline
    END AS job_title,
    description__text AS description
FROM staging_data