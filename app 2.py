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

prompt_std = f"""
Here is the data of my sql table {table_data}. Give me recommendations to fix standardization issues according to 
standard data governance protocols. Here are some good practices -

1. Make sure the Columns have proper Datatype ->
StudentID INT AUTO_INCREMENT PRIMARY KEY,     -- Primary key with auto-increment
    FirstName VARCHAR(255),                       -- Variable length string for first names
    LastName VARCHAR(255),                        -- Variable length string for last names
    Email VARCHAR(255),                           -- Variable length string for email addresses
    PhoneNumber VARCHAR(20),                      -- Variable length string for phone numbers
    Address VARCHAR(255),                         -- Variable length string for addresses
    DateOfBirth DATE,                             -- Date type for date of birth
    EnrollmentDate DATE,                          -- Date type for enrollment date
    Major VARCHAR(255),                           -- Variable length string for majors
    GPA DECIMAL(3, 2),                            -- Decimal type for GPA with 2 decimal places
    Graduated ENUM('Yes', 'No')                   -- Enum type for graduated status

3. For the GPA, write an SQL query that fixes negative value into positive values. If the positive value is greater than 4 then subtract 4 from the value.
4. For the Graduated column, write an SQL query that ensures that the responses are either Yes or No. If the respone is "Null", then it should be converted to No.
5. Change DateOfBirth column from YYYY-MM-DD to MM-DD-YYYY
6. Change EnrollmentDate column from YYYY-MM-DD to MM-DD-YYYY
7. Important - Each recommendation should only be for one specific column
8. Important - If the same recommendation applied to multiple columns, Give all of them as separate recommendations for each column
Give context based recommendations specific to the table provided. Do not use fullstop, only sentences.
If the rule is in one line,come up with a query as one single recommendation

Important -> Your recommendations will be then passed along to another AI system that generates SQL queries based on the natural language input. So make sure that the recommendation is precise
Make sure to give all the recommendations without a title, just a sentence of what needs to be down. Make sure the output is a list
consisting of all the recommendations as a separate element of the list. this is important as I  will call another method that executes
these reommendations as sql queries. The output should be in the format of a python list. []
Make sure you recommend based on the schema provided, not general recommendations
Important -> Do not number your recommendations
Important -> Make sure the Date recommendations are different for every column

"""

# Query is the NL text to be converted into SQL query; prompt is how you want the model to behave
# Takes in array of natural language prompts and outputs a list of sql queries
def sql_query_gen(query, prompt):
    model = genai.GenerativeModel('gemini-pro')
   
    response = model.generate_content([prompt, query])

    cleaned_response = re.sub(r'```sql\n|```', '', response.text).strip()
    return  cleaned_response

# # Returns a list of SQL queries to be executed
# def sql_query_list(query_list):
#     result = []
#     for q in query_list:
#         query = sql_query_gen(q,prompt)
#         result.append(query)
    
#     return result

model = genai.GenerativeModel('gemini-pro')
response2 = model.generate_content([prompt_std, "Give me recommendations"])

recommendation_list = [line.lstrip('- ').strip() for line in response2.text.split('\n')]

print(recommendation_list)

