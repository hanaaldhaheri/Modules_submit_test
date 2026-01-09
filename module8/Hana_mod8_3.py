import fastmcp
import requests, json

mcp = fastmcp.FastMCP()

def ask_ollama(question):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:1b",
            "prompt": question,
            "stream": False
        }
    ).json()
    return r.get("response", "")

@mcp.tool(name="ollama_chat")
def ollama_chat(question: str):
    return {
        "question": question,
        "answer": ask_ollama(question)
    }

if __name__ == "__main__":
    mcp.run(transport="streamable-http")