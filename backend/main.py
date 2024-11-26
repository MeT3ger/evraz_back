from fastapi import FastAPI
import uuid

app = FastAPI()

@app.get("/ping")
def read_root():
    return { "pong": uuid.uuid4() }
