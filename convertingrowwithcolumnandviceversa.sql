
select * from emp_compensation;

--case statement with sum
select
emp_id,
sum(case when salary_component_type='salary' then val end) as salary,
sum(case when salary_component_type='bonus' then val end) as bonus,
sum(case when salary_component_type='hike_percent' then val end) as hike_percent
into emp_compensation_pivot
from emp_compensation
group by emp_id;


select * from(
select emp_id, 'salary' as salary_compensation_type, salary as val from emp_compensation_pivot
union ALL
select emp_id, 'bonus' as salary_compensation_type, bonus as val from emp_compensation_pivot
UNION ALL
select emp_id, 'hike_percent' as salary_compensation_type, hike_percent as val from emp_compensation_pivot
)a
order by emp_id