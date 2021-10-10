# https://python.plainenglish.io/build-apis-fast-using-fastapi-and-python-e83b59031a34
# https://github.com/PriyavKaneria/FastAPI-ToDo-List-application

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()
# depending on your working directory of your virtual enviroment ! here "TodoList"
templates = Jinja2Templates(directory="TodoList/templates")
dbpath = 'TodoList/database.json' # path and file of database in Json

@app.get("/")
async def root(request: Request):
    with open(dbpath) as f:
        data = json.load(f)
    return templates.TemplateResponse("todolist.html",{"request":request,"tododict":data})

@app.get("/delete/{id}")
async def delete_todo(request: Request, id: str):
    with open(dbpath) as f:
        data = json.load(f)
    del data[id]
    with open(dbpath,'w') as f:
        json.dump(data,f)
    return RedirectResponse("/", 303)

@app.get("/update/{id}")
async def update_todo(request: Request, id: str):
    with open(dbpath) as f:
        data = json.load(f)
    update = data[id]
    print(data[id])
    return templates.TemplateResponse("todolist_up.html",{"request":request,"tododict":update})

@app.post("/add")
async def add_todo(request: Request):
    with open(dbpath) as f:
        data = json.load(f)
    formdata = await request.form()
    newdata = {}
    i=1
    for id in data:
        newdata[str(i)] = data[id]
        i+=1
    newdata[str(i)] = formdata["newtodo"]
    # print(newdata)
    with open(dbpath,'w') as f:
        json.dump(newdata,f)
    return RedirectResponse("/", 303)

if __name__ == "__main__":
    uvicorn.run("main:app")