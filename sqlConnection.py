import pyodbc
import sqlalchemy
import urllib

conn_str = ('Driver={SQL Server Native Client 11.0}; Server=(localdb)\MSSQLLocalDB; Database=saaDB; Trusted_Connection=yes;')
params = urllib.parse.quote_plus(conn_str)

engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
  
conn = pyodbc.connect(conn_str)



import pandas as pd

#df = pd.read_sql_query('select assetClass, varName from tblAssets where franking>0', conn)
df = pd.read_sql_query('select assetClass, varName from tblAssets where franking>0', engine)

