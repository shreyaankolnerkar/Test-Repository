from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read():
    return {"Fast API Running"}
