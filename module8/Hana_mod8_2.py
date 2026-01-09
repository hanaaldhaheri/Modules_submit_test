# - open bash, type "cmd" in search box
# - run "npx @modelcontextprotocol/inspector"
# 1. after nodejs installation, we can run inspector using "npx @modelcontextprotocol/inspector"

# 2. install libraries
#    pip install fastmcp

# make MCP to connect to any SQL database you created to provide the 
# information via the MCP viewer.

import fastmcp
import datetime
import random
import sqlite3,json,string
mcp = fastmcp.FastMCP()

def mcp_users():
    db = sqlite3.connect("users.db")
    c = db.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, user_key TEXT)")
    c.execute("INSERT INTO users (name, phone, user_key) VALUES (?,?,?)",
              (random.choice(["Meera","Sara","Saif"]),
               f"555-{random.randint(1000,9999)}",
               ''.join(random.choices(string.ascii_uppercase, k=5))))

    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    db.commit()
    db.close()

    return rows

@mcp.tool(name="list_users")
def list_users():
    return json.dumps(mcp_users(), indent=2)



if __name__ == "__main__":
    mcp.run(transport="streamable-http")
