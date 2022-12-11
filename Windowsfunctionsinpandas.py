## Windows functions in pandas

#Problem:Find the employee with 3rd highest salary in each department
select * from(
select *,
row_number() over(PARTITION BY dep_id ORDER BY salary desc) as rnk
from emp )A
where rnk=3


import pyodbc
import pandas as pd

cnxn=pyodbc.connect(driver='{SQL Server}', host='BLR135CG0276ZST',
                      DATABASE='master', Trusted_Connection='yes')


query1="select * from emp;"
df_emp=pd.read_sql(query1,cnxn)


df_emp['rnk']=df_emp.sort_values(['salary'], ascending=False).groupby(['dep_id']).cumcount()
df_result=df_emp.query('rnk==3')

df_result1=df_emp[df_emp['rnk']==3]