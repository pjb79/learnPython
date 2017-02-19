# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:48:09 2017

@author: PBallant
"""
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd


plt.close('all')

# import data to pandas
df              = pd.read_csv('C:\\Users\\pjbca\\Downloads\\Transactions.csv')

# drop unwanted columns
df.drop(['Credit', 'Balance'], axis = 1, inplace = True)

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
df['dayNum']    = df['transDate'].dt.weekday
df['weekBegin'] = df.apply(lambda x: x['transDate'] - dt.timedelta(days=x['dayNum']), axis=1)
df['dayName']   = df['transDate'].dt.weekday_name
df['monthEnd']  = df['transDate'] + pd.tseries.offsets.MonthEnd(1)

# get unique week identifier
uniqueWeeks     = df['weekBegin'].unique()

# get rid of weeks that don't have a full seven days (ie last week of year)
for w in uniqueWeeks:
    if len(df[df['weekBegin'] == w])<7:
        df = df[df['weekBegin'] != w]
        

# pivot
daysOfWeek      = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

table           = df.pivot_table(index = 'weekBegin', columns = 'dayName', values = 'Debit', fill_value = 0, aggfunc = np.sum)
table['sum']    = table.sum(axis = 1)
table           = table.div(table['sum'], axis = 0)
table           = table.drop('sum', axis = 1)
table           = table[daysOfWeek]


# create plots
plt.figure()
table.boxplot()
plt.ylim([0,1])
plt.ylabel('Percentage of Weekly Spend')

plt.figure()
for d in daysOfWeek:
    plt.subplot(3,3,daysOfWeek.index(d)+1)
    plt.plot(table[d])
    plt.ylim([0,1])
    plt.ylabel('Percentage of Weekly Spend')
    plt.title(d)
    
# get cash
df['cash']  = df['Description'].str.extract('Cash amount \$(\d*\.\d*)<BR', expand = False).fillna(0).astype('float')
df['cash1'] = df.loc[df['Description'].str.contains('ATM owner fee'),['Debit']]
df['cash1'] = df['cash1'].fillna(0)
df['cash']  = -1*df['cash'] + df['cash1']
df          = df.drop('cash1', axis = 1)

dfCash              = df.groupby(by = 'monthEnd').sum()
dfCash['pctCash']   = dfCash['cash'] / dfCash['Debit']
plt.figure()
plt.plot(dfCash['pctCash'])


# break out sales description
df['vendor']  = df['Description'].str.extract('(.*).-.Receipt', expand = False)
df['vendor']  = df['vendor'].str.extract('(.*).-', expand = False)




       
    


