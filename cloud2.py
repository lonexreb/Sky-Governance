import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
   
}

# Function to connect to the MySQL database
def connect_to_database(config):
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return None

# Function to drop all tables in the database
def drop_all_tables(cursor):
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    for (table,) in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table};")

# Function to create the Students table
def create_teachers_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(15),
    Address VARCHAR(255),
    DateOfBirth DATE,
    HireDate DATE,
    Department VARCHAR(100),
    Degree VARCHAR(50),
    YOE INT,
    Position VARCHAR(50)
);
    ''')

# Function to insert data into the Students table
def insert_teacher_data(cursor, teachers):
    cursor.executemany('''
    INSERT INTO Students (FirstName, LastName, email, PhoneNumber, Address, DateOfBirth, HireDate, Department, Degree, YOE,Position)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', teachers)

# Main workflow
def main():
    # Connect to the database
    conn = connect_to_database(config)
    if conn is None:
        return
    cursor = conn.cursor()

    # Drop all tables
    drop_all_tables(cursor)

    # Create the Students table
    create_teachers_table(cursor)

    # Data to insert
 
    teachers = [
    ('Thomas', 'Anderson', 'thomas.anderson@example.com', '5948132067', '789 Elm St', '1975-03-12', '2010-08-25', 'Computer Science', 'PhD', 15, 'Professor'),
    ('Laura', 'Martin', 'laura.martin@example.com', '2317984056', '123 Oak St', '1980-07-20', '2012-09-01', 'Biology', 'PhD', 12, 'Associate Professor'),
    ('Henry', 'Brown', 'henry.brown@example.com', '3402516789', '456 Pine St', '1985-10-30', '2015-01-15', 'Chemistry', 'PhD', 9, 'Assistant Professor'),
    ('Angela', 'Smith', 'angela.smith@example.com', '1780935462', '789 Maple St', '1970-05-22', '2005-07-10', 'Mathematics', 'PhD', 19, 'Professor'),
    ('Robert', 'Clark', 'robert.clark@example.com', '6054913278', '101 Birch St', '1983-12-11', '2011-03-20', 'Physics', 'PhD', 13, 'Associate Professor'),
    ('Nancy', 'Adams', 'nancy.adams@example.com', '3194862570', '202 Willow St', '1978-09-25', '2008-06-30', 'English', 'MA', 16, 'Senior Lecturer'),
    ('Patrick', 'White', 'patrick.white@example.com', '5704169238', '303 Cedar St', '1981-11-07', '2013-11-10', 'History', 'PhD', 11, 'Associate Professor'),
    ('Susan', 'Miller', 'susan.miller@example.com', '4217985360', '404 Fir St', '1977-01-18', '2007-05-15', 'Art', 'MFA', 17, 'Senior Lecturer'),
    ('James', 'Wilson', 'james.wilson@example.com', '9586037124', '505 Spruce St', '1986-02-04', '2014-08-23', 'Music', 'PhD', 10, 'Assistant Professor'),
    ('Margaret', 'Lewis', 'margaret.lewis@example.com', '7132945680', '606 Poplar St', '1972-06-15', '2003-04-05', 'Philosophy', 'PhD', 21, 'Professor'),
    ('Daniel', 'Johnson', 'daniel.johnson@example.com', '2365148970', '707 Ash St', '1984-03-22', '2010-11-18', 'Psychology', 'PhD', 14, 'Associate Professor'),
    ('Barbara', 'Thompson', 'barbara.thompson@example.com', '1650879342', '808 Cherry St', '1976-08-29', '2006-09-14', 'Sociology', 'PhD', 18, 'Professor'),
    ('Steven', 'Harris', 'steven.harris@example.com', '7523890416', '909 Chestnut St', '1982-12-13', '2013-02-12', 'Political Science', 'PhD', 11, 'Associate Professor'),
    ('Jennifer', 'Young', 'jennifer.young@example.com', '9843621507', '1010 Spruce St', '1987-04-08', '2016-05-09', 'Engineering', 'PhD', 8, 'Assistant Professor'),
    ('Michael', 'Walker', 'michael.walker@example.com', '4178095623', '1111 Pine St', '1980-11-19', '2010-10-20', 'Economics', 'PhD', 14, 'Associate Professor')
]
    # Insert data into the table
    insert_teacher_data(cursor, teachers)

    # Commit the transaction
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
