import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-1OACCVP\SQLEXPRESS;"
                      "Database=AdventureWorksLT2019;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT top 5 * FROM [AdventureWorksLT2019].[SalesLT].[Address]')

for row in cursor:
    print('row = %r' % (row,))
