#  python pandas aggregation  with group by

import pandas as pd
df=pd.read_csv('orders.csv')
df.sales.max()

## select category, city, avg(sales), min(sales), max(profit),max(sales) from 
df group by category, city


df.groupby('category').sales.max()

df.groupby('category').sales.agg(['mean','max','min','count'])

df.groupby('category').agg({'sales':mean,'profit':max})



df.groupby('category').agg({'sales':min, 'profit':max}).plot(kind='bar')