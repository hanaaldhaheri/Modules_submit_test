from fastapi import FastAPI
from datetime import datetime

app=FastAPI()
@app.get("/message")
def message(text:str):
    return{
        "message":text,
        "timestamp":datetime.utcnow().isoformat()
    }



#This code creates a FastAPI that receives a text from the URL and returns it back along with the current UTC time.




