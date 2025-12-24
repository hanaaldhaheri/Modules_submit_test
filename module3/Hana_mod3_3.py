from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
app=FastAPI()

@app.post("/api/text")
async def handle_text(request:Request):
    bdy = await request.body()
    print('got request', bdy)
    try:
        data = await request.json()
        print('data', data)
        if "Text" not in data:
            return JSONResponse(
                status_code=442,
                content={
                    "error": "Text field is required"
                }
            )
        return{
            "message": "Success",
                "Text": data["Text"]
            }
    except json.JSONDecodeError as msg:
        print(msg)
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid JSON body"}
        )
    

    
    # we use this curl -X POST http://127.0.0.1:8000/api/text -H "Content-Type: application/json" -d "{""Text"": ""abcd""}"
    #This code creates a FastAPI POST API that reads JSON data, checks if it is valid and contains "Text" it will show message=success 
    #in the terminal window it will show 200 OK.
    # if we show something else than text the message shows = error and in terminal window returns an error 442.