--Case When Statement

select *, 
case 
   when emp_age=12 then'baby'
   when emp_age<20 then 'kids'
   when emp_age>20 and emp_age<=40 then 'Adult'
   else 'Old'
END as emp_age_bucket
from emp
order by emp_age;




select emp_name, salary, dept.dept_name,
case
    when dept_name='Analytics' then salary+0.2*salary
    when dept_name='IT' then salary+0.15*salary
    else salary+0.25*salary
End as new_salary
from emp