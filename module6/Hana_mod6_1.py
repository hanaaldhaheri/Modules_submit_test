# LangChain 1.2.0 compatible imports
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# --- Load DOCX file ---
loader = UnstructuredWordDocumentLoader("my_file.docx")
docs = loader.load()

# --- Split into chunks ---
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(docs)

# --- Create embeddings ---
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# --- Create vector store ---
db = Chroma.from_documents(chunks, embeddings)

# --- Create retriever ---
retriever = db.as_retriever(search_kwargs={"k": 3})

# --- Query ---

query = input("Ask question : ") 
results = retriever.invoke(query)

# --- Print results ---
for i, doc in enumerate(results, 1):
    print(f"\nResult {i}:\n{doc.page_content}")

#DOCX → Load → Split → Embed → Chroma → Top-3 Retrieval    
#The code loads a DOCX file, splits it into chunks,
#  converts the chunks into embeddings, stores them in a vector database,
#  and retrieves the top 3 most relevant chunks for a query.