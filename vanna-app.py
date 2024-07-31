import vanna as vn
import os
import mysql.connector
from mysql.connector import errorcode
import pandas as pd

from vanna.remote import VannaDefault

api_key = 'f050503f26a64e449a8f474fd3c28a52'


# Connect to MySQL
host = "cloudy.cryo4gycgbmn.us-east-1.rds.amazonaws.com"
user = "admin"
password = "Krazy!101"
database = "cloudy"

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
vn = VannaDefault(model='sqlm', api_key=api_key)

vn.connect_to_mysql(host='cloudy.cryo4gycgbmn.us-east-1.rds.amazonaws.com', dbname='cloudy', user='admin', password='Krazy!101', port=3306)

def get_db_schema(db_host, db_user, db_password, db_name):
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()
    
    # Query to get the schema of all tables
    cursor.execute("SHOW TABLES;")
    
    # Fetch all table names
    tables = cursor.fetchall()
    
    schema_definitions = []
    
    for table in tables:
        table_name = table[0]
        cursor.execute(f"SHOW CREATE TABLE `{table_name}`;")
        create_table_stmt = cursor.fetchone()[1]
        schema_definitions.append(create_table_stmt)
    
    # Combine all schema definitions into a single string
    schema_string = '\n'.join(schema_definitions)
    
    # Close the connection
    cursor.close()
    conn.close()
    
    return schema_string

schema = get_db_schema(host,user,password,database)
#print(schema)

#vn.train(ddl=schema)
# vn.train(sql = """ UPDATE Students
# SET PhoneNumber = CONCAT(
#     SUBSTRING(PhoneNumber, 1, 3), '-', 
#     SUBSTRING(PhoneNumber, 4, 3), '-', 
#     SUBSTRING(PhoneNumber, 7, 4)
# )
# WHERE LENGTH(PhoneNumber) = 10;
# """)

# vn.train(sql = """UPDATE Students
# SET DateOfBirth = DATE_FORMAT(STR_TO_DATE(DateOfBirth, '%Y-%m-%d'), '%m-%d-%Y')
# WHERE DateOfBirth IS NOT NULL;
# """)

# vn.train(sql = """
# UPDATE Students
# SET GPA = CASE
#     WHEN GPA < 0 THEN ABS(GPA)
#     WHEN GPA > 4 THEN GPA - 4
#     ELSE GPA
# END;

# """)

# vn.train(sql = """UPDATE Students
# SET Graduated = CASE
#     WHEN Graduated IS NULL OR Graduated = 'Null' THEN 'No'
#     WHEN Graduated NOT IN ('Yes', 'No') THEN 'No'
#     ELSE Graduated
# END;""")

#print(vn.generate_sql("For the GPA, write an SQL query that fixes negative value into positive values. If the positive value is greater than 4 then subtract 4 from the value."))
#print(vn.generate_sql("Make sure the PhoneNumber column is formatted in XXX-XXX-XXXX format"))
#print(vn.generate_sql("Change Graduated column datatype to ENUM(\'Yes\', \'No\') and convert Null responses to No."))

print(vn.generate_sql("Change Column Major Datatype to VARCHAR(255)."))