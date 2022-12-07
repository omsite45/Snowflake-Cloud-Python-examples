import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pyodbc as pyo
import sys
import os
import numpy as np
import pandas as pd

print('opening sql server.. ')
cnn_sql=pyo.connect(
    r"Driver={SQL Server};Server=DESKTOP-1OACCVP\SQLEXPRESS;"
    "Database=AdventureWorksLT2019; UID=sa1;PWD=sa;"
    )

cursor = cnn_sql.cursor()

print('opened..')

sql="exec USP_ddl_script_all_tables 'address'"
df=pd.read_sql(sql,cnn_sql)
rep=df.to_string()
print(rep.replace("\\n", " "))

cnn_sql.close()
