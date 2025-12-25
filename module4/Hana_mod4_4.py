import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect("table_view.db")
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);
""")
cursor.execute("DELETE FROM students;")

cursor.execute("""
INSERT INTO students (name, age)
VALUES
    ('Shamsa', 20),
    ('Meera', 22),
    ('Alia', 19);
""")

# Query to view tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:")
for table in tables:
    print(table[0])

conn.commit()


cursor.execute("SELECT * FROM students;")
rows = cursor.fetchall()

print("\nStudents table:")
for row in rows:
    print(row)

    conn.close()



#This code connects to an SQLite database, displays the database tables, and prints all records from the students table.