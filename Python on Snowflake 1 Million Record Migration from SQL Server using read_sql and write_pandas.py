import snowflake.connector as sn
from snowflake.connector.pandas_tools import write_pandas
import pyodbc as pyo
import sys
import os
import numpy as np
import pandas as pd

print('opening sql server.. ')
cnn_sql=pyo.connect(
    r"Driver={SQL Server};Server=;"
    "Database=; UID=;PWD=;"
    )

cursor = cnn_sql.cursor()
mylist_rep1 = []
print('opened..')
sql="select * from  AdventureWorksLT2019.[SalesLT].[Address];"
df=pd.read_sql(sql, cnn_sql)
rep=df.to_string()
print(rep.replace("\\n", " "))




print('SQL closed')


scnn=sn.connect(user='',
    password='',
    account='',
    warehouse='SAMPLE',
    database='AdventureWorksLT2022',
    schema='Public'
    )
cur=scnn.cursor()
cur.execute("use warehouse SAMPLE_WH_SYS_ADMIN")
cur.execute("Use  AdventureWorksLT2022")
cur.execute("CREATE  TABLE  Address (AddressID int IDENTITY(1,1)  NOT NULL,AddressLine1 string NOT NULL,AddressLine2 STRING,City STRING NOT NULL,StateProvince STRING NOT NULL,CountryRegion STRING NOT NULL,PostalCode STRING NOT NULL,rowguid STRING   NOT NULL,ModifiedDate datetime NOT NULL);")
print('insert into snowflake table')
cs=scnn.cursor()

print("Writing to snowflake table ...")

success, num_chunks, num_rows, output = write_pandas(
            scnn,
            df ,
            "Address",
            quote_identifiers=False
         )
scnn.commit()
scnn.close()
print("Closed..")

