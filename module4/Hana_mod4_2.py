import sqlite3

# Name of the database file
db_file = "task_2.db"

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create the 'tasks' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Commit changes and close the connection
conn.commit()
conn.close()

print(f"Database '{db_file}' created with table 'tasks'.")