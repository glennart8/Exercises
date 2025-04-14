with source as (
    select * from raw_orders
),

renamed as (
    select
        "Order ID" as order_id,
        "Order Date" as order_date,
        "Ship Date" as ship_date,
        "Ship Mode" as ship_mode,
        "Customer ID" as customer_id,
        "Customer Name" as customer_name,
        segment,
        city,
        state,
        country,
        "Postal Code" as postal_code,
        market,
        region,
        "Product ID" as product_id,
        category,
        "Sub-Category" as sub_category,
        "Product Name" as product_name,
        cast(sales as float) as sales,
        quantity,
        discount,
        cast(profit as float) as profit,
        "Shipping Cost" as shipping_cost,
        "Order Priority" as order_priority
    from source
)

select * from renamed


--- Sist i konsolen  ---

-- >> dbt debug         # kolla att allt är rätt kopplat
-- >> dbt run           # kör modellerna
-- >> dbt test          # kör testerna i schema.yml
-- >> dbt docs generate # skapa dokumentation
-- >> dbt docs serve    # öppna dokumentation i browser