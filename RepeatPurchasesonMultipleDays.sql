
select count(1) as users_num from(
select user_id, product_id ,count(distinct purchase_date:: date )as p_date , * 
from  purchases
group by user_id, product_id
having count(distinct purchase_date:: date )>1
)A