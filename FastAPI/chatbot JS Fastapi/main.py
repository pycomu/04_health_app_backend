# Importing the FastApi class
from fastapi import FastAPI, Request, Body
import uvicorn
import datetime

# Creating an app object
app = FastAPI()

# https://stackoverflow.com/questions/64379089/fastapi-how-to-read-body-as-any-valid-json
@app.post("/playback")
async def getInfo(info : Request):
    result = await info.json()
    
    now = datetime.datetime.now()
    now = now.strftime("Day %d.%m.%Y - time %H:%M")

# async def getInfo(payload: dict = Body(...)): # alternative mit Body and payload as dic
#     result = payload

    # print(result)
    # print(result["user"])
    
    return {
        "status" : "SUCCESS",
        "data" : "{} (returned by Chatbot API at {})".format(result["user"], now) }


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)


