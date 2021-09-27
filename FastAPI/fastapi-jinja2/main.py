

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", port=8000, reload=True)

# go to http://127.0.0.1:8000/docs
