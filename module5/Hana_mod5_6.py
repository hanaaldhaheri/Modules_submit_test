import streamlit as st
import requests

URL = "http://localhost:11434/api/generate"
SYSTEM = "You are a helpful assistant."

def ask_llm(q, temp, ctx):
    data = {
        "model": "gemma3:1b",
        "prompt": f"{SYSTEM}\nUser: {q}\nAssistant:",
        "options": {"temperature": temp, "num_ctx": ctx},
        "stream": False
    }
    return requests.post(URL, json=data).json()["response"]

st.title("🤖 LLM Chat")

q = st.text_area("Ask a question")
temp = st.slider("Temperature", 0.0, 1.0, 0.3)
ctx = st.selectbox("Context Window", [2048, 4096, 8192])

if st.button("Ask") and q:
    st.write(ask_llm(q, temp, ctx))

#The code creates a small web app that lets users ask questions and get answers from a local LLM with adjustable behavior.