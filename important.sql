
create table candidates (
emp_id int,
experience varchar(20),
salary int
);

delete from candidates;

insert into candidates 
values
(1,'Junior',10000),
(2,'Junior',15000),
(3,'Junior',40000),
(4,'Senior',16000),
(5,'Senior',20000),
(6,'Senior',50000);


with total_sal as(
select *, sum(salary) over(PARTITION BY experience order by salary asc rows betwwen unbounded preceding and current row) as running_sal
from candidates)
, seniors as (select * from total_sal
where experience='senior' and running_sal<=70000)

select * from total_sal
where experience='junior' and running_Sal<=70000-(select sum(salary) from seniors)
union ALL
select * from seniors

;