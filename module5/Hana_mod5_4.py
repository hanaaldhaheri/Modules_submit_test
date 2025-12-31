import requests

# Local Ollama API endpoint
url = "http://localhost:11434/api/generate"

# Define the system prompt (persona)
SYSTEM_PROMPT = "You are a friendly assistant who explains answers clearly and simply."

def get_ollama_response(user_input):
    # Combine system prompt with user input
    full_prompt = SYSTEM_PROMPT + "\n\nUser: " + user_input + "\nAssistant:"

    data = {
        "model": "gemma3:1b",  # Replace with your installed model
        "prompt": full_prompt,
        "max_tokens": 200,
        "stream": False
    }
    try : 
        response = requests.post(url, json=data)
        return response.json()
    except Exception :
        print("Error")

   
if __name__ == "__main__":
    while True:
        user_input = input("Enter your question (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        output = get_ollama_response(user_input)
        print("LLM response:\n", output["response"])


 #system prompt is like giving the LLM instructions about who it should “be” and how it should behave during a conversation. 
 # It is not part of the user’s question, but it frames the model’s responses.

