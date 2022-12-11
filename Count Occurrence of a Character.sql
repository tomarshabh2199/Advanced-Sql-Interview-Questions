-- Count Occurrence of a Character

select name,
replace(name,'  ','') as rep_name ,
len(name)-len(replace(name,' ','')) as cnt
from strings




select name,
replace(name,'AK','') as rep_name ,
len(name)-len(replace(name,'AK','')) as cnt
from strings