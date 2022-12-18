import snowflake.connector as sn
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas


    
cnn=sn.connect(user='swamilaxmi4',
    password='Omsite@405',
    account='buabvey-qf15468',
    warehouse='project_warehouse',
    database='project_database',
    schema= 'project_schema',
    sfRole = "ACCOUNTADMIN"
    )
cs=cnn.cursor()
try:
    cs.execute('select current_version()')
    row=cs.fetchone()
    print(row[0])
    print('Creating Warehouse..')
    sql="create warehouse if not exists project_warehouse"
    cs.execute(sql)
    print('create database  ..')
    sql="create database if not exists project_database "
    cs.execute(sql)
    print('use database ')
    sql="use database project_database"
    cs.execute(sql)
    print('creating schema.. ')
    sql="create schema  if not exists project_schema"
    cs.execute(sql)




    print('creation complete ..')
    sql="use warehouse project_warehouse"
    cs.execute(sql)
    sql="use database project_database"
    cs.execute (sql)
    sql="use schema project_schema"
    cs.execute(sql)
    sql=("create or replace table project_comments"
    "(ID integer , comments string)")
    cs.execute(sql)
    sql=("insert into  project_comments (id, comments)"
         "values(1,'my project ')")
    cs.execute(sql)
    sql=("insert into  project_comments (id, comments)"
         "values(2,'hello there!!!!$$ ')")
    cs.execute(sql)
    sql=("insert into  project_comments (id, comments)"
         "values(3,'my project is new one 4 you$$$$ ')")
    cs.execute(sql)
    print('read some rows!!!!')
    sql="select * from  project_comments"
    cs.execute(sql)
    for row in cs.fetchall():
        print(row)
    print('load data form CSV')
    
    original = r"C:\Users\LENOVO\Desktop\snowflake\project_comments.csv"

    delimiter = ","

    total = pd.read_csv(original, sep = delimiter)
    print(total)
    df=pd.DataFrame(columns=['ID','comments'])
    print(df)


    

    
    print('complete ..')

finally:
    cs.close()
