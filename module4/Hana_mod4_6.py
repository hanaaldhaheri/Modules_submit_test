import sqlite3
import random
import string

# Connect to your database
db_file = 'table_view.db'  
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Step 1: Pick the first table automatically
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
if not tables:
    print("No tables found in database.")
    conn.close()
    exit()
table_name = tables[0][0]
print("Using table:", table_name)

# Step 2: Add new column if it doesn't exist
cursor.execute(f"PRAGMA table_info({table_name});")
columns = [col[1] for col in cursor.fetchall()]
if 'missing_field' not in columns:
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN missing_field TEXT;")
    print("Added column 'missing_field'.")
else:
    print("Column 'missing_field' already exists.")

# Step 3: Update all rows with a random character
cursor.execute(f"SELECT id FROM {table_name};")
rows = cursor.fetchall()
for (row_id,) in rows:
    random_char = random.choice(string.ascii_letters)  # A-Z, a-z
    cursor.execute(f"""
        UPDATE {table_name}
        SET missing_field=?
        WHERE id=?
    """, (random_char, row_id))

conn.commit()
print(f"Populated 'missing_field' with random characters for {len(rows)} rows.")

# Step 4: Show first 5 rows as sample
cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
for row in cursor.fetchall():
    print(row)

conn.close()
