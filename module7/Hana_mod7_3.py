from fastapi import FastAPI
from datetime import datetime


app= FastAPI()

@app.post("/health")
def health_server():
    return {
        "status": "healthy",
        "server_time": datetime.now()
    }

@app.get("/")
def home():
    return {"message": "FastAPI server is running successfully"}


#uvicorn Hana_mod7_3:app --reload