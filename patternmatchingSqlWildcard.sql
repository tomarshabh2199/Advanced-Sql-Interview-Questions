select order_id, order_date, customer_name
from orders
where customer_name='Andrew%'
where customer_name like 'Andrew%'
where customer_name like '%Allen'
where customer_name like 'A%N'
where customer_name like '%All%'
where cutsomer_name like '_a%' # second charcter  is having a in their name
where customer_name like 'A[np]%'
where cutsomer_name like 'A[^ns]%'
where customer_name like 'A[b-k]%'
-- range
--% 0 or more characters
-- '_' a single character 

-- [] anything within brackets can come