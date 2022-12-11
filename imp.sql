with cte as(
select 
transcation_date :: date as transcation_date,
sum(case WHEN type='withdrawal' then -1*amount
else amount end) as amount
from transcations
group by transcation_date :: date
order by transcation_date :: date
)
select transcation_date,
amount
sum(amount) over(partition by extract(year from transcation_date) extract(month from transcation_datekkkkkkkkkkkk),
order by transcation_date) as cum_sum
from cte
;