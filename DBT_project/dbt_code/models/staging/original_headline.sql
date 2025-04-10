-- En CTE - COMMON TABLE EXPRESSION
WITH staging_data AS ( --  Skapar en tillfällig staging_datatabell
    SELECT * FROM ads.staging.data_field_job_ads
)
SELECT headline, description__text FROM staging_data