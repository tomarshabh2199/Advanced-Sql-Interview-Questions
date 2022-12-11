# creating conditional columns in pandas

# NAN-Not A Number
import pandas as pd
df=pd.read_csv('orders.csv')
df[df['city']]=='Bangalore'
df.loc[df['city']=='Bangalore','state']='karnatka'
df.loc[df['city']=='Chennai','state']='TamilNadu'
df.loc[df['city']=='Mysore','state']='Karnatka'
df.loc[df['city'].isin(['Bangalore','Mysore']),'state']='karnatka'

df.loc[df['profit']<=250,'profit_category']='Low Profit'
df.loc[(df['profit']>250) & df['profit']<=500, 'profit_category']='Medium Profit'

df.loc[df['profit']>500, 'profit_category']='high profit'