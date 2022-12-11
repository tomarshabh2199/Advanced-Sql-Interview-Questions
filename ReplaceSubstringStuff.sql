--Replace/Stuff/Substring/Translate |Sql string Functions

select *,
replace(dep_name,'Analytics','Mining') as replace_string,
stuff(dep_name,1,3,'Demo') as stuff_string
substring(dep_name,2,3) as substring_String
translate(dep_name,'AR','ST') as translate_string
from dept
