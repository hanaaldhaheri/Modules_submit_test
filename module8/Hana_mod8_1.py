# - open bash, type "cmd" in search box
# - run "npx @modelcontextprotocol/inspector"
# 1. after nodejs installation, we can run inspector using "npx @modelcontextprotocol/inspector"

# 2. install libraries
#    pip install fastmcp

import fastmcp
import datetime
import random

mcp = fastmcp.FastMCP()

@mcp.tool(name="system_date")
def system_date():
    return datetime.datetime.now().isoformat()

@mcp.tool(name="random_int")
def random_int():
    return str(random.randint(1, 100))


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
