from fastapi import FastAPI
from backend.app.api.code_review import router

app = FastAPI()

app.include_router(router)