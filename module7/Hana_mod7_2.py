import requests
import streamlit as st 


st.title ("Ollama chat")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if not question.strip():
        st.warning ("PLEASE type a question")
    else:

        url="http://localhost:11434/api/chat"
        
        user_prompt = {
             "role": "user",
           "content": question
                        }
        
        data={
            "model":"llama3.1",
            "messages":[user_prompt],
            "stream":False
        }

    r = requests.post(url, json=data, timeout=300)
    r.raise_for_status()
    result = r.json()

    st.subheader("Answer")
    st.write(result["message"]["content"])