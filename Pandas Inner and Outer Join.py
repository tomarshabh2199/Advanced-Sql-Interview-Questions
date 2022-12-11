#Pandas Inner and Outer Join


select * from emp
inner join dept
on emp.dep_id=dept.dept_id


import pyodbc
import pandas as pd

cnxn=pyodbc.connect(driver='{SQL SERVER}', host='BLR135CG0276ZST',
                      database='master', Trusted_Connection='yes')

 
query1="select * from emp;"
df_emp=pd.read_sql(query1,cnxn)


query2="select dep_id as dept_id, dep_name from dept;"
df_dept=pd.read_sql(query2,cnxn)

#pd.merge
df_inner_join=pd.merge(left=df_emp, right=df_dept,how='inner',left_on='dep_id', right_on='dept_id')
df_left_join=pd.merge(left=df_emp, right=df_dept,how='left',left_on='dep_id', right_on='dept_id')
df_right_join=pd.merge(left=df_emp, right=df_dept,how='right',left_on='dep_id', right_on='dept_id')
df_outer_join=pd.merge(left=df_emp, right=df_dept,how='outer',left_on='dep_id', right_on='dept_id')



 