# import modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

# close any existing plts
plt.close("all")

# import daabase and dividend yields as dataframes
dbRet       = pd.read_excel('C:\\D\\F_SVN\\prod\\database\\database.xlsx',sheetname = 'returns', header = 0, skiprows = [1,2,3,4,5,6,7,8,9,10], index_col = 0)
dbDY        = pd.read_excel('C:\\D\\F_SVN\\prod\\database\\database_dividendYields.xlsx',sheetname = 'dividendYields', header = 0, skiprows = [1,2,3,4,5,6,7,8], index_col = 0)

# get only the R300 and dy_R3000 components
r3000Ret    = dbRet[['R3000']]
r3000DY     = dbDY[['dy_R3000']]

# combine the two merging on the date index
r3000       = pd.merge(r3000Ret, r3000DY, how = 'inner', left_index = True, right_index = True)

# adjust data in new dataframe
r3000['dy_R3000']   = r3000['dy_R3000']/100
r3000.sort_index(inplace = True)
r3000['R3000_cum']  = (1+r3000['R3000']).cumprod()
r3000['R3000_ann']  = r3000['R3000'].rolling(12).apply(lambda x: np.prod(1+x)-1)
     
# create plot of dy vs total ret
plt.figure ()
plt.scatter(r3000['dy_R3000'], r3000['R3000'])
plt.show   ()

# plot R3000 index values
plt.figure()
plt.plot  (r3000['R3000_cum'])
plt.show  ()


# get annual
annualR3000 = r3000.loc[:,['R3000_ann','dy_R3000']].iloc[range(11, len(r3000), 12),:]
plt.figure ()
plt.scatter(annualR3000['dy_R3000'], annualR3000['R3000_ann'])
plt.title  ('Russell 3000 DY vs Russell 3000 Total Return')
plt.xlabel ('Russell 3000 DY')
plt.ylabel ('Russell 3000 TR')
plt.show   ()


# import equity val database
dbEV                = pd.read_excel('C:\\D\\F_SVN\\prod\\database\\database_equityVal.xlsx',sheetname = 'MSCIEquityVal', header = 0, skiprows = [1,2,3,4,5,6,7,8], index_col = 0, na_values = [' '])
dbEV                = dbEV[['E_USD_MSCI_pi','E_USD_MSCI_dy','E_USD_MSCI_pe']]
#dbEV.dropna(how = 'any', inplace = True)
dbEV.sort_index(inplace = True)

# convert to annual timesteps           
dbEV = dbEV.iloc[range(len(dbEV)-1,0,-12),:]
dbEV.sort_index(inplace = True)            

dbEV['deltaPE']         = dbEV['E_USD_MSCI_pe']/dbEV['E_USD_MSCI_pe'].shift()-1
dbEV['deltaDY']         = dbEV['E_USD_MSCI_dy']-dbEV['E_USD_MSCI_dy'].shift()  
dbEV['priceReturn']     = dbEV['E_USD_MSCI_pi']/dbEV['E_USD_MSCI_pi'].shift()-1
dbEV['Earnings']        = dbEV['E_USD_MSCI_pi']/dbEV['E_USD_MSCI_pe'] 
dbEV['earningsGrowth']  = dbEV['Earnings']/dbEV['Earnings'].shift()-1

    

dbDisAgg                    = dbEV['E_USD_MSCI_dy'].apply(lambda x: math.log(1+x)).to_frame('log(1+DY)')
dbDisAgg['multRev']         = dbEV['E_USD_MSCI_pe']/dbEV['E_USD_MSCI_pe'].shift()
dbDisAgg['multRev']         = dbDisAgg['multRev'].apply(lambda x: math.log(x))
dbDisAgg['earningsGrowth']  = dbEV['earningsGrowth'].apply(lambda x: math.log(1+x))
dbDisAgg['totalReturn']     = dbDisAgg['log(1+DY)'] + dbDisAgg['multRev'] + dbDisAgg['earningsGrowth']

print(dbDisAgg.corr())

plt.figure()
colNames = dbDisAgg.columns.tolist()
for i in range(4):
    for j in range(4):

        plt.subplot (4,4,4*i+j+1)
        plt.scatter (dbDisAgg.iloc[:,i],dbDisAgg.iloc[:,j])
        plt.title   (colNames[i] + ' / ' + colNames[j])
        plt.xlabel  (colNames[i])
        plt.ylabel  (colNames[j])

plt.show()
    