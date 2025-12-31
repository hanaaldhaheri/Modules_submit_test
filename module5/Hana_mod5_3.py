import requests

# Local Ollama server URL
url = "http://localhost:11434/api/generate"

text=input("Enter question:")

data = {
    "model": "gemma3:1b",
    "prompt": text,
    "stream": False
}

response = requests.post(url, json=data)


result=response.json()

print("\nollama respond:")
print (result["response"])