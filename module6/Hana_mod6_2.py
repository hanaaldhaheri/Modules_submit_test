# import all req. libraries 


from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage


# =========================
# SETTINGS
# =========================
DOC_PATH = "my_file.docx"
EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3.1" #Bigger model gives better answer
#LLM_MODEL = "gemma3:1b"
DB_DIR = "db"

# =========================
# STEP 1: Load document
# =========================
docs = Docx2txtLoader(DOC_PATH).load()

# =========================
# STEP 2: Split document
# =========================
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

# =========================
# STEP 3: Create embeddings
# =========================
embeddings = OllamaEmbeddings(
    model=EMBED_MODEL,
    base_url="http://127.0.0.1:11434"
)

# =========================
# STEP 4: Store in Chroma
# =========================
db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_DIR
)

# =========================
# STEP 5: Create retriever
# =========================
retriever = db.as_retriever(search_kwargs={"k": 3})

# =========================
# STEP 6: Load LLM
# =========================
llm = ChatOllama(
    model=LLM_MODEL,
    base_url="http://127.0.0.1:11434",
    temperature=0.2
)

# =========================
# STEP 7: Ask questions (RAG)
# =========================
while True:
    question = input("\nAsk a question (or type 'exit'): ")
    if question.lower() == "exit":
        break
    context = "\n\n".join([d.page_content for d in docs])
    
    # Retrieve relevant chunks
    docs = retriever.invoke(question)
#If the answer is not in the context, say:
#"I cannot find this information in the document."    
    prompt = f"""
You must answer ONLY using the context below.


<Context>
{context}
</Context>
<Question>
{question}
</Question>
"""
    response = llm.invoke([HumanMessage(content=prompt)])

    print("\nAnswer:")
    print(response.content)


# pip install -U langchain langchain-community langchain-ollama chromadb docx2txt

# pull it for good accurate answer :
#ollama pull llama3.1
#This code loads a Word document, splits it into chunks, stores embeddings in a Chroma vector database,
#  retrieves the most relevant chunks for a user question, and uses a local Ollama LLM to answer questions strictly based on the document content (RAG).
