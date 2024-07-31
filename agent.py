from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai
import re
from get_sql_table import get_table
load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

def get_db_schema(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Query to get the schema of all tables
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';")
    
    # Fetch all the schema definitions
    schema_definitions = cursor.fetchall()
    
    # Combine all schema definitions into a single string
    schema_string = '\n'.join([schema[0] for schema in schema_definitions if schema[0] is not None])
    
    # Close the connection
    conn.close()
    
    return schema_string

table_data = get_table("std_test.db")
schema = get_db_schema("std_test.db")


def sql_query_gen(query, prompt):
    model = genai.GenerativeModel('gemini-pro')
   
    response = model.generate_content([prompt, query])

    cleaned_response = re.sub(r'```sql\n|```', '', response.text).strip()
    return  cleaned_response



prompt = f"""
You are an SQL expert. Convert the following natural language requests into SQL queries. Make sure to read the data schema first to understand what columns you will be working with.

Here is the schema {schema} of the table.

Help me generate SQL query when given an input containing natural language text. The schema and examples are given for your reference. Output only the SQL Query

"""



print(sql_query_gen("Give me SQL query to ensure that the PhoneNumber column of my database is in the format XXX-XXX-XXXX'",prompt))