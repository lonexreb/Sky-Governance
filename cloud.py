import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'admin',
    'password': 'Krazy!101',
    'host': 'cloudy.cryo4gycgbmn.us-east-1.rds.amazonaws.com',
    'database': 'cloudy'
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
def create_students_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        StudentID INT AUTO_INCREMENT PRIMARY KEY,
        FirstName TEXT,
        LastName TEXT,
        Email TEXT,
        PhoneNumber TEXT,
        Address TEXT,
        DateOfBirth DATE,
        EnrollmentDate DATE,
        Major TEXT,
        GPA FLOAT,
        Graduated VARCHAR(10)
    )
    ''')

# Function to insert data into the Students table
def insert_students_data(cursor, students):
    cursor.executemany('''
    INSERT INTO Students (FirstName, LastName, Email, PhoneNumber, Address, DateOfBirth, EnrollmentDate, Major, GPA, Graduated)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', students)

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
    create_students_table(cursor)

    # Data to insert
    students = [
    ('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St', '2000-01-02', '2021-06-15', 'Computer Science', 5.0, 'Null'),
    ('Jane', 'Smith', 'jane.smith@example.com', '1235677890', '456 Elm St', '1998-12-04', '2021-06-15', 'Biology', 3.8, 'No'),
    ('Alice', 'Johnson', 'alice.j@example.com', '1231237890', '789 Oak St', '1999-04-05', '2021-06-15', 'Chemistry', -3.6, 'No'),
    ('Bob', 'Brown', 'bob.brown@example.com', '0984567890', '101 Maple St', '1997-03-14', '2021-06-15', 'Mathematics', 3.2, 'Yes'),
    ('Charlie', 'Davis', 'charlie.davis@example.com', '1234567428', '202 Pine St', '2001-07-23', '2021-06-16', 'Physics', 4.3, 'Null'),
    ('Daisy', 'Miller', 'daisy.miller@example.com', '1298347890', '303 Cedar St', '1996-10-10', '2021-06-16', 'English', -5.3, 'Null'),
    ('Edward', 'Wilson', 'edward.w@example.com', '9836167890', '404 Birch St', '2002-09-09', '2021-06-16', 'History', 3.1, 'No'),
    ('Fiona', 'Taylor', 'fiona.taylor@example.com', '123894890', '505 Spruce St', '1999-11-30', '2021-06-16', 'Art', -2.0, 'No'),
    ('George', 'Anderson', 'george.anderson@example.com', '8903767890', '606 Fir St', '1998-02-19', '2021-06-17', 'Music', -0.5, 'Yes'),
    ('Hannah', 'Thomas', 'hannah.thomas@example.com', '11937567890', '707 Poplar St', '2000-05-03', '2021-06-17', 'Philosophy', 3.5, 'No'),
    ('Irene', 'Jackson', 'irene.jackson@example.com', '1231029890', '808 Ash St', '1995-06-01', '2021-06-17', 'Psychology', 3.8, 'Yes'),
    ('Jack', 'White', 'jack.white@example.com', '1234567123', '909 Willow St', '1997-12-25', '2021-06-17', 'Sociology', 3.2, 'Yes'),
    ('Karen', 'Harris', 'karen.harris@example.com', '1234569385', '1010 Cherry St', '1998-04-18', '2021-06-18', 'Political Science', 3.4, 'No'),
    ('Leo', 'Clark', 'leo.clark@example.com', '5920567890', '1111 Chestnut St', '1997-07-14', '2021-06-18', 'Engineering', -3.6, 'Yes'),
    ('Mia', 'Lewis', 'mia.lewis@example.com', '0396567890', '1212 Pine St', '1996-08-22', '2021-06-18', 'Economics', 3.7, 'Yes'),
    ('Noah', 'Robinson', 'noah.robinson@example.com', '7820567890', '1313 Cedar St', '1999-05-05', '2021-06-18', 'Business', 3.5, 'No'),
    ('Olivia', 'Walker', 'olivia.walker@example.com', '0491347890', '1414 Birch St', '1995-09-30', '2021-06-19', 'Nursing', 3.9, 'Yes'),
    ('Paul', 'Hall', 'paul.hall@example.com', '1391037429', '1515 Spruce St', '1998-06-06', '2021-06-19', 'Education', 3.4, 'Null'),
    ('Quinn', 'Allen', 'quinn.allen@example.com', '2234433890', '1616 Fir St', '2000-12-15', '2021-06-19', 'Law', 6.3, 'No'),
    ('Rose', 'Young', 'rose.young@example.com', '2594567890', '1717 Poplar St', '1996-10-29', '2022-06-19', 'Medicine', 3.8, 'Yes')
]
    # Insert data into the table
    insert_students_data(cursor, students)

    # Update phone numbers to the format XXX-XXX-XXXX
#     q = """UPDATE Students
# SET DateOfBirth = DATE_FORMAT(STR_TO_DATE(DateOfBirth, '%m-%d-%Y'), '%m-%d-%Y');
# """
#     cursor.execute(q)
   

    # Commit the transaction
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
