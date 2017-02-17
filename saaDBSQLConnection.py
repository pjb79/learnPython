def createSQLEngine():
    import sqlalchemy
    import urllib
   
    conn_str = ('Driver={SQL Server Native Client 11.0}; Server=(localdb)\MSSQLLocalDB; Database=saaDB; Trusted_Connection=yes;')
    params = urllib.parse.quote_plus(conn_str)    
    db = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
    return db
  

def getUniqueClientIDs(db):
    import sqlalchemy
    db = createSQLEngine()
    import pandas as pd
    dfClientID = pd.read_sql_query("select distinct p.[Master Portfolio ID] as ID, p.[Master Portfolio Name] as Name from dbo.tblPortfolios as p where p.PortfolioType = 'Client'", db)
    
    return dfClientID
    

db = createSQLEngine
dfClientID = getUniqueClientIDs(db)



