with orders as (
    select * from {{ ref('stg_orders') }} -- 1:a select - hämta data från stg_orders
),

aggregated as (
    select -- 2:a select - sammanställer data, aggregerar
        customer_id,
        customer_name,
        segment,
        country,
        count(distinct order_id) as total_orders,
        sum(sales) as total_sales,
        sum(profit) as total_profit,
        avg(sales) as avg_order_value
    from orders
    group by customer_id, customer_name, segment, country
)

select * from aggregated -- 3:e select - returnerar den aggregerade datan
