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

## import data to pandas and prepare 
df              = pd.read_csv('C:\\Users\\pjbca\\Downloads\\Transactions.csv')
#df              = pd.read_csv('C:\\Users\\PBallant\\Downloads\\Transactions (4).csv')

# drop unwanted columns
df.drop(['Credit', 'Balance'], axis = 1, inplace = True)


# get transaction date from description column
df['transDate'] = df['Description'].str.extract('Date.(\w\w.\w\w\w.\w\w\w\w)', expand = False)
  
# convert date and transDate to datetime type  
df['Date']      = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
df['transDate'] = pd.to_datetime(df['transDate'], format = '%d %b %Y', exact = False)

# for entries with no trans date uses ordinary date
df['transDate'].fillna(df['Date'], inplace=True)

# add week number to df
df['dayNum']    = df['transDate'].dt.weekday
df['weekBegin'] = df.apply(lambda x: x['transDate'] - dt.timedelta(days=x['dayNum']), axis=1)
df['dayName']   = df['transDate'].dt.weekday_name
df['monthEnd']  = df['transDate'] + pd.tseries.offsets.MonthEnd(1)
df.drop('dayNum', axis=1, inplace = True)

# remove entries with no debit amount
ind             = pd.notnull(df['Debit'])
df              = df[ind]

# adjust entries where cash is taken
df['cash']                      = df['Description'].str.extract('Cash amount \$(\d*\.\d*)<BR', expand = False).fillna(0).astype('float')
ind                             = df['cash'] > 0
dfCash                          = df.loc[ind,:]
dfCash['Description']           = 'Cash'
dfCash['Debit']                 = -dfCash['cash']
df.loc[ind,'Debit']             = df.loc[ind, 'Debit'] + df.loc[ind, 'cash']
df                              = df.append(dfCash)
df                              = df.drop('cash', axis = 1)

df.loc[df['Description'].str.contains('ATM owner fee'),['Description']] = 'Cash'

del dfCash

# copy dataframe for use in day of week calcs
dfWeekDay = df.copy()

# get unique week identifier
uniqueWeeks     = dfWeekDay['weekBegin'].unique()

# get rid of weeks that don't have a full seven days (ie last week of year)
for w in uniqueWeeks:
    if len(dfWeekDay[dfWeekDay['weekBegin'] == w].unique())<7:
        dfWeekDay = dfWeekDay[dfWeekDay['weekBegin'] != w]
        

# pivot
daysOfWeek      = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

table           = dfWeekDay.pivot_table(index = 'weekBegin', columns = 'dayName', values = 'Debit', fill_value = 0, aggfunc = np.sum)
table['sum']    = table.sum(axis = 1)
table           = table.div(table['sum'], axis = 0)
table           = table.drop('sum', axis = 1)
table           = table[daysOfWeek]

# create plots of percentage of spending by day of week
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
    

# calc proportion of cash used
dfCash              = df.loc[df['Description']=='Cash'].groupby(by = 'monthEnd').sum()
dfNotCash           = df.loc[df['Description']!='Cash'].groupby(by = 'monthEnd').sum()
dfCash              = pd.merge(dfCash, dfNotCash, how='outer', left_index=True, right_index=True)
dfCash['pctCash']   = dfCash['Debit_x']/dfCash['Debit_y']

del dfNotCash

plt.figure()
plt.plot(dfCash['pctCash'])
plt.ylim([0,0.5])

# break out sales description
df['vendor']  = df['Description'].str.extract('(.*).-.Receipt', expand = False)
df['vendor']  = df['vendor'].str.extract('(.*).-', expand = False)




       
    


