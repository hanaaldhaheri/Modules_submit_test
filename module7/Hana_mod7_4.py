import sqlite3
import random
import string

# Connect to SQLite DB
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    user_key TEXT
)
""")

def random_user():
    name = random.choice(["Meera", "Sara", "Rowdha", "Saif"])
    phone = f"555-{random.randint(1000, 9999)}"
    user_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return name, phone, user_key

# Insert random users
for _ in range(5):
    user = random_user()
    cursor.execute(
        "INSERT INTO users (name, phone, user_key) VALUES (?, ?, ?)",
        user
    )
    print("Inserted:", user)

conn.commit()

# Verify insert
print("\nAll users in DB:")
for row in cursor.execute("SELECT * FROM users"):
    print(row)

conn.close()
print("\nDone")



