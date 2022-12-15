--working with null values in SQL

insert into customers values(1,'ankit','M',null, null)

select * from customers;
select * from customers where dob is null;
select *, isnull(age,11) from customers;
select *, isnull(dob,'2001-01-01'), coalesce(dob,'2002-01-02',null,'2003-03-01') 
from customers;

select count(*) from customers;

select count(Age) from customers;

select count(isnull(Age,0)) from customers;

select Avg(age) from customers;

select avg(isnull(age,0)) from customers;

