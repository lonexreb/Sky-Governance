import sqlite3
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to the SQLite database
def connect_to_db(db_path):
    conn = sqlite3.connect(db_path)
    return conn

def get_table_names(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    return table_names

def get_table_schema(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    schema = cursor.fetchall()
    return schema


def get_table_data(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name};")
    data = cursor.fetchall()
    return data

def create_schema_dict(conn):
    table_names = get_table_names(conn)
    schema = {table: get_table_schema(conn, table) for table in table_names}
    data = {table: get_table_data(conn, table) for table in table_names}
    return schema, data

def create_prompt(schema, data):
    prompt = "Table Schema: \n"
    
    for table, columns in schema.items():
        prompt += f"Table: {table}\n"
        for column in columns:
            prompt += f"  Column: {column[1]} - Type: {column[2]}\n"
        prompt += "\n"
        
        prompt += f"Data in {table}:\n"
        for row in data[table]:
            prompt += f"  {row}\n"
        prompt += "\n"
    
    prompt += "Recommendations:\n"
    return prompt



# Main function to run the script
def get_table(db_path):
    conn = connect_to_db(db_path)
    schema, data = create_schema_dict(conn)
    prompt = create_prompt(schema, data)
    
    return prompt

# Run the main function
if __name__ == "__main__":
    db_path = 'std_test.db'
    rez = get_table(db_path)
    print(rez)
