-- Calculate Mode in SQL
 
select * from mode;


--Method 1 CTE
with freq_cte(
select id, count(id) as freq 
from MODE
group by id)
select * from freq_cte
where freq=(select max(freq) from freq_cte);


with freq_cte as(
    select id, count(*) as freq from mode group by id)
    , rnk_cte as(
        select *,
        rank() over(partition by freq desc) as rn
        from freq_cte)
        select * from rnk_cte where rn=1
)