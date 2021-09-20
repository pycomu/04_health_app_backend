# https://python.plainenglish.io/rest-api-for-beginners-with-python-fastapi-86fa84fcda42

# Importing the FastApi class
from fastapi import FastAPI
import uvicorn

# Creating an app object
app = FastAPI()


# Create BMI calc
@app.get("/bmicalc")
async def calc_bmi(height: float, weight: float):
    bmi = round(weight/ (height*height),2)
    return {
        "data": "The calculated BMI is: {}".format(bmi)
    }


if __name__ == "__main__":
    uvicorn.run("main:app")


