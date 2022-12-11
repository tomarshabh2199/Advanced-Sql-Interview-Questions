--Aggregation and windows function together in a single query

-- how to use group by and rank(window functions together)
--find top 5 products in each category by sales
--using cte

with sales_value as(
select distinct category, count(distinct Product_Name), sum(sales) as total_sales
from orders 
group by category, Product_Name)
select * from(
select *, rank() over(Partition BY category order by total_sales desc) as rn
from sales_value)A
where rn<=5


---aggreagtionn first then window function operation perform


select * from(
    select category, product_name, sum(sales) as total_sales,
    rank() over(partition by CATEGORY order by sum(sales) desc) as rn
    from orders 
    group by category,product_name
)A
where rn<=5`