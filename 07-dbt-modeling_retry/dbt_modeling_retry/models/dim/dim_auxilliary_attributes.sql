with aux as (select * from {{ ref('src_auxilliary_attributes') }})

select  
         {{ dbt_utils.generate_surrogate_key(['id']) }} as auxiliary_attribute_id,
        experience_required,
        driver_license,
        access_to_own_car

from aux