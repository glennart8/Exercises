with stg_job_ads as (select * from {{ source('job_ads', 'stg_ads') }})

select  occupation__label,
        id,
        employer__workplace,
        workplace_address__municipality,    
        relevance,
        number_of_vacancies as vacancies,
        application_deadline,
from stg_job_ads


