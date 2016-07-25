import numpy as np
import pandas as pd
import os


df=pd.read_excel("C:\\D\\F_SVN\\prod\\cntl files\\2016-06\\cntl_allRegions_placemat.xls")

n = len(df.index)

for r in range(0,n):
    if(pd.isnull(df.iloc[r,0])):
        df.iloc[r,0] = df.iloc[r-1,0]
        
ind = df['account name'] == "Standard"
df = df.loc[ind,:]

searchDirs = df['directories to be searched']
ind = pd.notnull(searchDirs)
searchDirs = searchDirs[ind].tolist()

searchDirs = [str.replace(d,'YYYY_MM','2016-06') for d in searchDirs]
searchDirs = [str.replace(d,'Y:\\Forecasting & Simulation','c:\d\mirror') for d in searchDirs]    

varNames = df['variable name (If blank, all variables are obtained)']
ind = pd.notnull(varNames)
varNames = varNames[ind].tolist()

flm = os.listdir(searchDirs[0])
        
    





