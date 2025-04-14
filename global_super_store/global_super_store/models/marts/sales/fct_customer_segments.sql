with sales as (
    select * from {{ ref('int_customer_sales_summary') }}
),

segmented as (
    select *,
        case
            when total_sales > 10000 then 'VIP'
            when total_sales > 5000 then 'Regular'
            else 'Occasional'
        end as customer_segment -- Skapar en egen kolumn för segmentering av kunder där värden baseras på total_sales
    from sales
)

select * from segmented
