--Methods to calculate Median with sql


--Method 1 with medain using row_number
with cte as(select *,
row_number() over(order by emp_age asc)as rn_asc,
row_number() over(order by emp_age desc) as rn_desc
from emp
where emp_id<10
)
select *, avg(emp_age) from cte
where abs(rn_asc-rn_desc)<=1
order by emp_age;

--Method 2 :median using percentile_cont
select *,
percentile_Count(0.5) within group (order by emp_age) over() as median
from emp
where emp_id<10;