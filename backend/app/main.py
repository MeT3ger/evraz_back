from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

from backend.controllers.handlers import Handlers
from backend.dtos.backend_front import FrontDTO

app = FastAPI()

@app.post("/zip")
async def zip(file: UploadFile = File(alias="some")):
    # buisness skinny logic
    
    file_content = await file.read()
    
    decoded = file_content.decode("utf-8", errors="ignore")
    
    print(type(decoded))
    # zip = FrontDTO.Requests.zip(data)
    
    # validate data +  zipParse + processing + go to mistral + return response
    # response_corrections = await Handlers.code_style_fix(zip)
    
    # dto = FrontDTO.Responses.zip(response_corrections)
    return {"message": "zip"}