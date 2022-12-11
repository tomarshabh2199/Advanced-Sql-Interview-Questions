--Lead/Lag window Analytical Functions
--datepart


select * from orders;

with year_sales as(
    select datepart(year, order_date) as order_year, sum(sales) as sales
    from orders group by region, datepart(year, order_date)
)
select * 
lag(sales,1,0) over(parition by region  order by order_year asc) as prev_year_sales
lead(sales,1,0) over(partition by region order by order_year desc) ad next_year_sales
from year_sales
order by order_year