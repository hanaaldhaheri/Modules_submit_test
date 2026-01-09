import fastmcp
import sqlite3
import requests
import json
import random
import string

mcp = fastmcp.FastMCP()
DB = "users.db"

# ---------- Database ----------
def get_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            phone TEXT,
            user_key TEXT
        )
    """)
    conn.commit()
    return conn, c

# ---------- LLM ----------
def ask_ollama(prompt):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:1b",
            "prompt": prompt,
            "stream": False
        }
    ).json()
    return r.get("response", "")

# ---------- MCP TOOLS ----------
@mcp.tool(name="add_user:")
def add_user(name: str):
    conn, c = get_db()
    phone = f"555-{random.randint(1000,9999)}"
    key = ''.join(random.choices(string.ascii_uppercase, k=5))
    c.execute(
        "INSERT INTO users (name, phone, user_key) VALUES (?,?,?)",
        (name, phone, key)
    )
    conn.commit()
    conn.close()
    return {"status": "user added", "name": name}

@mcp.tool(name="list_all_users:")
def list_users():
    conn, c = get_db()
    c.execute("SELECT id, name, phone, user_key FROM users")
    rows = c.fetchall()
    conn.close()
    return rows

@mcp.tool(name="ask_DB:")
def ask_database(question: str):
    conn, c = get_db()
    #c.execute("SELECT COUNT(*) FROM users")
    c.execute("SELECT * FROM users")
    #count = c.fetchone()[0]
    all_users = c.fetchall()
    conn.close()

    context = f"Users in database : {all_users}"
    answer = ask_ollama(context + " Question: " + question)

    return {
        "answer": answer
    }

# ---------- RUN MCP ----------
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
