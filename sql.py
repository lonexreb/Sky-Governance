import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('std_test.db')
cursor = conn.cursor()

# Function to drop all tables in the database, except for sqlite_sequence
def drop_all_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        if table[0] != 'sqlite_sequence':
            cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")
    conn.commit()

# Drop all tables
drop_all_tables(cursor)

# Create the Students table with relevant columns
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    Email TEXT,
    PhoneNumber TEXT,
    Address TEXT,
    DateOfBirth TEXT,
    EnrollmentDate TEXT,
    Major TEXT,
    GPA REAL,
    Graduated TEXT
)
''')

# Insert 20 rows of data with various date formats
students = [
    ('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St', '01-02-20000', '2021.06.15', 'Computer Science', 5.0, 'Null'),
    ('Jane', 'Smith', 'jane.smith@example.com', '1235677890', '456 Elm St', '1998-12-04', '2021-06-15', 'Biology', 3.8, 'No'),
    ('Alice', 'Johnson', 'alice.j@example.com', '1231237890', '789 Oak St', '1999-04-05', '2021-06-15', 'Chemistry', -3.6, 'No'),
    ('Bob', 'Brown', 'bob.brown@example.com', '0984567890', '101 Maple St', '03-14-1997', '2021-06-15', 'Mathematics', 3.2, 'Yes'),
    ('Charlie', 'Davis', 'charlie.davis@example.com', '1234567428', '202 Pine St', '2001-07-23', '2021/06/16', 'Physics', 4.3, 'Null'),
    ('Daisy', 'Miller', 'daisy.miller@example.com', '1298347890', '303 Cedar St', '10-1996-10', '2021/06/16', 'English', -5.3, 'Null'),
    ('Edward', 'Wilson', 'edward.w@example.com', '9836167890', '404 Birch St', '2002-09-09', '2021-06-16', 'History', 3.1, 'No'),
    ('Fiona', 'Taylor', 'fiona.taylor@example.com', '123894890', '505 Spruce St', '1999-11-30', '2021-06-16', 'Art', -2.0, 'No'),
    ('George', 'Anderson', 'george.anderson@example.com', '8903767890', '606 Fir St', '1998-02-19', '2021-06-17', 'Music', -0.5, 'Yes'),
    ('Hannah', 'Thomas', 'hannah.thomas@example.com', '11937567890', '707 Poplar St', '2000-05-03', '2021.06.17', 'Philosophy', 3.5, 'No'),
    ('Irene', 'Jackson', 'irene.jackson@example.com', '1231029890', '808 Ash St', '1995-06-01', '2021-06-17', 'Psychology', 3.8, 'Yes'),
    ('Jack', 'White', 'jack.white@example.com', '1234567123', '909 Willow St', '12-25-1997', '2021-06-17', 'Sociology', 3.2, 'Yes'),
    ('Karen', 'Harris', 'karen.harris@example.com', '1234569385', '1010 Cherry St', '1998-04-18', '2021-06-18', 'Political Science', 3.4, 'No'),
    ('Leo', 'Clark', 'leo.clark@example.com', '5920567890', '1111 Chestnut St', '1997-07-14', '2021-06-18', 'Engineering', -3.6, 'Yes'),
    ('Mia', 'Lewis', 'mia.lewis@example.com', '0396567890', '1212 Pine St', '1996-08-22', '2021-06-18', 'Economics', 3.7, 'Yes'),
    ('Noah', 'Robinson', 'noah.robinson@example.com', '7820567890', '1313 Cedar St', '1999-05-05', '2021/06/18', 'Business', 3.5, 'No'),
    ('Olivia', 'Walker', 'olivia.walker@example.com', '0491347890', '1414 Birch St', '09-30-1995', '2021-06-19', 'Nursing', 3.9, 'Yes'),
    ('Paul', 'Hall', 'paul.hall@example.com', '1391037429', '1515 Spruce St', '06-1998-06', '2021/06/19', 'Education', 3.4, 'Null'),
    ('Quinn', 'Allen', 'quinn.allen@example.com', '2234433890', '1616 Fir St', '2000-12-15', '2021-06-19', 'Law', 6.3, 'No'),
    ('Rose', 'Young', 'rose.young@example.com', '2594567890', '1717 Poplar St', '10-1996-29', '2022.06.19', 'Medicine', 3.8, 'Yes')
]

# Insert the data into the table without specifying StudentID
cursor.executemany('''
INSERT INTO Students (FirstName, LastName, Email, PhoneNumber, Address, DateOfBirth, EnrollmentDate, Major, GPA, Graduated)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', students)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
