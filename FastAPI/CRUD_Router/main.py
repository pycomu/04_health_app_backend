# https://www.youtube.com/watch?v=62pP9pfzNRs
# https://github.com/BekBrace/FastAPI_Crash_Course

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", port=8000, reload=True)

# go to http://127.0.0.1:8000/docs
