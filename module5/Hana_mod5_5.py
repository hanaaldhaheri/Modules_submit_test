import requests

URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = (
    "You are a helpful and clear AI assistant. "
    "Explain answers step by step when needed."
)

def ask_llm(user_input):
    prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_input}\nAssistant:"

    data = {
        "model": "gemma3:1b",
        "prompt": prompt,

        # 🔧 LLM settings
        "options": {
            "temperature": 0.3,   # lower = more factual
            "num_ctx": 4096       # context window size
        },

        "stream": False
    }

    response = requests.post(URL, json=data)
    response.raise_for_status()

    return response.json()["response"]

if __name__ == "__main__":
    while True:
        user_input = input("Ask something (or 'exit'): ")
        if user_input.lower() == "exit":
            break

        answer = ask_llm(user_input)
        print("\nLLM response:\n", answer)