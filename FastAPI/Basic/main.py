from fastapi import FastAPI
import uvicorn
import datetime
app = FastAPI()


@app.get("/")
def example():
    print("task done")
    return {"FastAPI": "The fastest modern web framework!"}

@app.get("/now")
def now():
    now = datetime.datetime.now()
    now = now.strftime("Today %d.%m.%Y - now %H:%M")
    return {"Time":now}

@app.get("/greetings")
def greeting():
    return {"Data":"Hello to my new REST API!"}


@app.get("/names")
def greeting():
    return {"name1": "Bek", "name2": "George", "name3": "Mikel"}


if __name__ == "__main__":
    uvicorn.run("main:app")