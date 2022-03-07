

# Importing the FastApi class
from fastapi import FastAPI, Request, Body
import uvicorn
import datetime

# Creating an app object
app = FastAPI()

@app.get("/now")
def now():
    now = datetime.datetime.now()
    now = now.strftime("Today %d.%m.%Y - now %H:%M")
    return {"Time":now}

# Create BMI calc - GET
@app.get("/bmicalc")
async def calc_bmi(height: float, weight: float) -> float: 
    bmi = round(weight/ (height*height),2)
    return {"data": "The calculated BMI is: {} (no json input)".format(bmi) # no html page rendered as response !
    }

# Create BMI calc - POST
@app.post("/bmicalc")
async def calc_bmi(info : Request):
    result = await info.json()
    height = result["height"]
    weight = result["weight"]
    # print(height)
    # print(weight)
    bmi = round(weight/ (height*height),2)
    return {"data": "The calculated BMI is: {} (json input)".format(bmi) # no html page rendered as response !
    }

# https://stackoverflow.com/questions/64379089/fastapi-how-to-read-body-as-any-valid-json
@app.post("/playback")
async def getInfo(info : Request):
    result = await info.json()

# async def getInfo(payload: dict = Body(...)): # alternative mit Body and payload as dic
#     result = payload

    print(result)
    return {
        "status" : "SUCCESS",
        "data" : result }

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)


