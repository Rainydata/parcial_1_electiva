from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/info")
def get_info():
    return {
        "name": "fastapi_app",
        "version": "1.0",
        "author": "Bryan, juan manuel",
        "framework": "FastAPI",
        "date": "2021-09-01"

    }

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
