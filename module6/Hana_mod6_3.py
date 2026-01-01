import streamlit as st
import sqlite3
from langchain_ollama import ChatOllama


DB = "chat.db"
llm = ChatOllama(model="llama3.1", base_url="http://127.0.0.1:11434", temperature=0.3)

# 1) Create DB table (once)
conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
)
""")
conn.commit()

st.title("Ollama Chat + SQLite")

# 2) UI input
q = st.text_input("Question")
if st.button("Ask") and q.strip():
    # 3) Ask Ollama
    a = llm.invoke(q).content
    st.write("Answer:", a)

    # 4) Save to DB
    cur.execute("INSERT INTO chats (question, answer) VALUES (?, ?)", (q, a))
    conn.commit()
    st.success("Saved ✅")

# 5) Show last 5 chats
if st.button("Show last 5"):
    cur.execute("SELECT question, answer FROM chats ORDER BY id DESC LIMIT 5")
    for qq, aa in cur.fetchall():
        st.write("Q:", qq)
        st.write("A:", aa)
        st.divider()

conn.close()


#This code builds a Streamlit web app that sends user questions to a local Ollama LLM, displays the answers, and stores and retrieves chat history from a SQLite database.
