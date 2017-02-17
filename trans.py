# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:48:09 2017

@author: PBallant
"""
import numpy as np
import matplotlib.pyplot as plt

# import data to pandas
import pandas as pd
df              = pd.read_csv('C:\\Users\\PBallant\\Downloads\\Transactions (4).csv')

# get transaction date from description column
df['transDate'] = df['Description'].str.extract('Date.(\w\w.\w\w\w.\w\w\w\w)', expand = False)
  
# convert date and transDate to datetime type  
df['Date']      = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
df['transDate'] = pd.to_datetime(df['transDate'], format = '%d %b %Y', exact = False)

# remove entries with no datetme and no debit amount
ind             = pd.notnull(df['transDate'])
df              = df[ind]
ind             = pd.notnull(df['Debit'])
df              = df[ind]

# add week number to df
df['weekNum']      = df['transDate'].dt.week.astype('str')
#df['weekNumStr']   = df['weekNum']
df['yearNum']      = df['transDate'].dt.year.astype('str')
#df['yearNumStr']   = df['yearNum'].astype('str')
df['weekIdent']    = df['weekNum'] + df['yearNum']
df['Qdate']        = [date - pd.tseries.offsets.DateOffset(days=1) + pd.tseries.offsets.Week() for date in  df.Date]
df['dayNum']       = df['transDate'].dt.weekday_name

# get unique week identifier
uniqueWeeks = df['weekIdent'].unique()

# get rid of weeks that don't have a full seven days (ie last week of year)
for w in uniqueWeeks:
    if len(df[df['weekIdent'] == w])<7:
        df = df[df['weekIdent'] != w]
        

# pivot
table = df.pivot_table(index = 'weekIdent', columns = 'dayNum', values = 'Debit', fill_value = 0, aggfunc = np.sum)
table['sum'] = table.sum(axis = 1)
table = table.div(table['sum'], axis = 0)
table = table.drop('sum', axis = 1)
table = table[['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']]

plt.figure()
table.boxplot()

plt.figure()
plt.plot(table['Monday'])





       
    


