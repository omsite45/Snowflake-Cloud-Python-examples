import snowflake.connector as sn
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas


    
cnn=sn.connect(user='swamilaxmi4',
    password='Omsite@405',
    account='buabvey-qf15468',
    warehouse='PROJECT_WAREHOUSE',
    database='PROJECT_DATABASE',
    schema= 'PROJECT_SCHEMA',
    Role = "ACCOUNTADMIN"
    )
cs=cnn.cursor()

sql = 'create or replace stage data_stage2 file_format = (type = "csv" field_delimiter = "," skip_header = 1)'
cs.execute(sql)

csv_file = 'C:\\Users\\LENOVO\\Desktop\\snowflake\\project_comments.csv'
sql = "PUT file://" + csv_file + " @data_stage2 auto_compress=true"
cs.execute(sql)

sql = 'copy into project_comments from @data_stage2/project_comments.csv.gz file_format = (type = "csv" field_delimiter = "," skip_header = 1 )'\
      'ON_ERROR = "CONTINUE" '

cs.execute(sql)

sql = 'select * from "project_database"."project_schema"."project_comments"'


cs.execute(sql)
for c in cursor:
    print(c)


