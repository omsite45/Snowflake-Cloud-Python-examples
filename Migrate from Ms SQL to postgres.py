import psycopg2
from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os


hostname='localhost'
database='AdventureWorks'
username='postgres'
pwdg='sa'
port_id=5432
conn=None

cur=None

conn=psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=pwdg,
    port=port_id)




cur=conn.cursor()



conn.commit()
#import needed libraries


#get password from environmnet var
pwd = os.environ['PGPASS']
uid = os.environ['PGUID']
#sql db details
driver = "{SQL Server }"

server = "DESKTOP-1OACCVP\SQLEXPRESS"
database = "AdventureWorksLT2019;"


#extract data from sql server
def extract():
    try:
        src_conn = pyodbc.connect(r"Driver={SQL Server};Server=DESKTOP-1OACCVP\SQLEXPRESS;" "Database=AdventureWorksLT2019; UID=sa1;PWD=sa;"
                          )
        src_cursor = src_conn.cursor()
        # execute query
        src_cursor.execute(""" select  t.name as table_name from sys.tables t where t.name  NOT in ('ErrorLog','BuildVersion') """)
        src_tables = src_cursor.fetchall()
        for tbl in src_tables:
            df = pd.read_sql_query(f'select * FROM [AdventureWorksLT2019].[SalesLT].{tbl[0]}', src_conn)
            load(df, tbl[0])
            
            
    except Exception as e:
        print("Data extract error: " + str(e))
    finally:
        src_conn.close()

#load data to postgres
def load(df, tbl):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql://{username}:{pwdg}@{hostname}:5432/AdventureWorks')

        print(f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}')
        # save df to postgres
        df.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False)
        rows_imported += len(df)
        # add elapsed time to final print out
        print("Data imported successful")
    except Exception as e:
        print("Data load error: " + str(e))

try:
    #call extract function
    extract()
except Exception as e:
    print("Error while extracting data: " + str(e))
