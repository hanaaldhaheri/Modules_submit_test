import sqlite3
import time

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

# Step 2: Get columns of the table
cursor.execute(f"PRAGMA table_info({table_name});")
columns = cursor.fetchall()
if len(columns) < 3:
    print("Table has less than 2 columns besides id, cannot proceed.")
    conn.close()
    exit()
col_names = [columns[1][1], columns[2][1]]  # first two columns after id
print("Columns to update:", col_names)

# Step 3: Get the first row
cursor.execute(f"SELECT * FROM {table_name} ORDER BY id LIMIT 1;")
row = cursor.fetchone()
if not row:
    print("No rows found in table.")
    conn.close()
    exit()

row_id = row[0]
original_values = (row[1], row[2])
print("Original row:", row)

# Step 4: Update the row
new_values = ('Hana', '29')  # temporary values
cursor.execute(f"""
    UPDATE {table_name}
    SET {col_names[0]}=?, {col_names[1]}=?
    WHERE id=?
""", (*new_values, row_id))
conn.commit()
print("Row updated! Watching changes for 15 seconds:")

# Step 5: Print row every second
for i in range(15):
    cursor.execute(f"SELECT * FROM {table_name} WHERE id=?", (row_id,))
    print(cursor.fetchone())
    time.sleep(1)

# Step 6: Revert the row
cursor.execute(f"""
    UPDATE {table_name}
    SET {col_names[0]}=?, {col_names[1]}=?
    WHERE id=?
""", (*original_values, row_id))
conn.commit()
print("Row reverted back! Final row:")
cursor.execute(f"SELECT * FROM {table_name} WHERE id=?", (row_id,))
print(cursor.fetchone())

conn.close()

# the code picks the first table and row,temporarily updates two columns while printing the changes every second for 15 seconds,
#  then reverts the row back to its original values.