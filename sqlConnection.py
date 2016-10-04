import pyodbc
conn_str = ('Driver={SQL Server Native Client 11.0}; Server=(localdb)\MSSQLLocalDB; Database=saaDB; Trusted_Connection=yes;')
    
conn = pyodbc.connect(conn_str)

import pandas as pd

df = pd.read_sql_query('select assetClass, varName from tblAssets where franking>0', conn)
