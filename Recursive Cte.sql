--Recursive Cte

with cte_numbers
as(
    select 1 as num --anchor query

    union ALL

    select  num+1 --recursive query
    from cte_numbers
    where num<6 --filter to stop the recursion
)

select num
from cte_numbers;

/*

anchor:1
num=1, 2
num=2, 3
num=3,4
num=4, 5
num=5, 6
*/

-- Leetcode Problem Total sales by year


with r_cte as(


select min(period_start) as dates, max(period_end) as max_date
from sales

UNION ALL
select dateadd(day,1,dates), max_date from r_cte
where dates<max_date
)

SELECT * FROM r_cte
inner join sales
option(maxrecursion 1000);

