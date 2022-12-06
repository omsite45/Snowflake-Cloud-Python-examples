import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pyodbc as pyo
import pandas as pd

print('opening sql server.. ')
cnn_sql=(
    r"Driver={SQL Server};Server=DESKTOP-1OACCVP\SQLEXPRESS;"
    "Database=AdventureWorksLT2019; UID=sa1;PWD=sa;"
    )
cnn=pyo.connect(cnn_sql)
print('opened..')

sql="select * from SalesLT.Address;"

df=pd.read_sql(sql,cnn)
print(df.head(10))
print(df.tail(10))
cnn.close()

print('create snowflake table ..  ')
#sql=("use ADVENTUREWORKSLT2022.public")

sql= ("create or replace table SalesLT_Address_python"
    "(AddressID integer , AddressLine1 string, AddressLine2 string, City string, StateProvince string, CountryRegion string, PostalCode string,rowguid string, ModifiedDate datetime)"
    )
scnn=snowflake.connector.connect(
    user='swamilaxmi4',
    password='Abcdefg@4',
    account='pz26212.ap-southeast-1',
    warehouse='SAMPLE_WH_SYS_ADMIN',
    database='ADVENTUREWORKSLT2022',
    schema='public'
    )
cs=scnn.cursor()

#success, nchunks, nrows,_=write_pandas(scnn, df, 'SalesLT_Address_python')
success, num_chunks, num_rows, output = write_pandas(
            conn=scnn,
            df=df,
            table_name='SalesLT_Address_python',
            quote_identifiers=False
         )


print('writing to snowflake table .. ')

scnn.close()
print('Snowflake closed.. ')
print('get some data..  ')
sql="select top 100 from SalesLT_Address_python;"
#df_result=cs.fetch_pandas_all()
scnn.close()
#prin(df.result)
#sql=("insert into SalesLT_Address_python"
#"select * from SalesLT.Address")
#cnn.close()

print('closed')
