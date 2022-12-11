
#Find duplicate and delete duplicate rows from pandas dataframe python


import pandas as pd

df.emp_id.duplicated()
df.emp_id.duplicated().sum()#how many duplicate are there

df[df.emp_id.duplicated()]

df[~df.emp_id.duplicated()] #reverse condition


#drop duplicate

df.drop_duplicates() # checking full row

df.drop_duplicates(subset=['emp_id']) 

df.drop_duplicates(subset=['emp_id'], keep='last', inplace='true')