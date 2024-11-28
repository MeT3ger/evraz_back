from fastapi import FastAPI

from backend.controllers.handlers import Handlers
from backend.dtos.backend_front import FrontDTO

app = FastAPI()

@app.get("/zip")
async def zip(data):
    # buisness skinny logic
    
    zip = FrontDTO.Requests.zip(data)
    
    # validate data +  zipParse + processing + go to mistral + return response
    response_corrections = await Handlers.code_style_fix(zip)
    
    dto = FrontDTO.Responses.zip(response_corrections)
    return dto