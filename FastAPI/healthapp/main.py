import email
from multiprocessing import context
from fastapi import FastAPI, Request, Form
import uvicorn
import json

from fastapi.templating import Jinja2Templates # provide HTML templates for input and output
from fastapi.responses import HTMLResponse # for return output as html file
from fastapi.staticfiles import StaticFiles 

app = FastAPI()
templates = Jinja2Templates(directory="healthapp/templates") # path for html templates
dbpath = 'healthapp/health_db.json' # path and file of database in Json
app.mount("/healthapp/templates", StaticFiles(directory="healthapp/templates"), name="static")

@app.get("/", status_code=200)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login", status_code=200, response_class=HTMLResponse)
def login_form(request: Request, username: str = Form(...), password: str = Form(...)):
    with open(dbpath) as f: # read json file and load into data
        data = json.load(f)
    i=0
    for x in data: # loop through data (json file payload) and check for hits
        if data[i]["username"] == username and data[i]["pw"] == password: # account exists in json file ?
            return templates.TemplateResponse("personal.html", context={'request': request, 'email': username, 'pw': password})
        i+=1
    # no account existing, show again login page with a remark
    return templates.TemplateResponse("login.html", {"request": request, 'no_account':"Your account/password does not exist, try again"})

@app.get("/register", status_code=200)
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", status_code=200, response_class=HTMLResponse)
def register_form(request: Request, username: str = Form(...), password: str = Form(...)):
    entry = {'username': username, 'pw': password} # store input in variable entry as dic
   
    with open(dbpath) as f: # read json file and load into data
        data = json.load(f)
    
    i=0
    for x in data: # loop through data (json file payload) and check for already existing username
        if username in data[i]["username"]:
            return templates.TemplateResponse("register.html", {"request": request, 'no_account':"Your username already exists, try again"})
        i+=1

    data.append(entry) # append new entry at array data (content file)

    with open(dbpath,'w') as f: # write back extended content to file
        json.dump(data,f,indent=2)

    return templates.TemplateResponse("login.html", {"request": request, 'no_account':"New account created, login now."})
    




if __name__ == "__main__":
    uvicorn.run("main:app", port=8500,reload=True)