with job_details as (select * from {{ ref('src_job_details') }})

select  
        {{ dbt_utils.generate_surrogate_key(['id'])}} as job_details_id,
        headline, 
        description, 
        description_html, 
        coalesce(duration, 'ej angiven') as duration,  -- för att ersätta nollvärden
        salary_type, 
        coalesce(salary_description, 'ej angiven') as salary_description, 
        working_hourse_type,
        scope_of_work_min,
        scope_of_work_max
from job_details