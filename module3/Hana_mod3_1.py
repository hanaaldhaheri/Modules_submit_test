from fastapi import FastAPI
app=FastAPI()
@app.get("/hello")
def hello(name:str):
    return {"message":f"Hello {"Hana_Al_Dhaheri"}"}



#The code creates a simple FastAPI app with a /hello prompt that takes a parameter which is a name from the URL and returns.