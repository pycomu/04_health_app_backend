# https://python.plainenglish.io/rest-api-for-beginners-with-python-fastapi-86fa84fcda42

# Importing the FastApi class
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 

from fastapi.responses import HTMLResponse # only for case 2
from fastapi import FastAPI, Request, Form # Form for case 3

# Creating an app object
app = FastAPI()
# depending on your working directory of your virtual enviroment ! here "BMIcalcJinJa2"
templates = Jinja2Templates(directory="BMIcalcJinJa2/templates")
app.mount("/BMIcalcJinJa2/static", StaticFiles(directory="BMIcalcJinJa2/static"), name="static")

#++++++++++++++++++ CASE 1 +++++++++++++++++++++++++++++++ request as "/bmicalc?height=2&weight=77"


# Create BMI calc
@app.get("/bmicalc")
async def calc_bmi(request: Request, height: float, weight: float):
    result = round(weight/ (height*height),2)
    return templates.TemplateResponse("bmi_form1.html", {"request": request, "bmi": result})


#++++++++++++++++++ CASE 2 +++++++++++++++++++++++++++++++ request as "/bmicalc/2,77"

@app.get("/bmicalc/{height},{weight}", response_class=HTMLResponse)
async def calc_bmi(request: Request, height: float, weight: float):
    result = round(weight/ (height*height),2)
    return templates.TemplateResponse("bmi_form1.html", {"request": request, "bmi": result})

#++++++++++++++++++ CASE 3 +++++++++++++++++++++++++++++++ request via entering into HTML file

@app.get("/form")
def form_post(request: Request):
    result = "Enter weight and height"
    return templates.TemplateResponse('bmi_form2.html', context={'request': request, 'bmi': result})

@app.post("/form")
def form_post(request: Request, weight: int = Form(...),height: float  = Form(...)):
    result = round(weight/ (height*height),2)
    return templates.TemplateResponse('bmi_form1.html', context={'request': request, 'bmi': result})

# ++++++++++++++++++

if __name__ == "__main__":
    uvicorn.run("main:app")


