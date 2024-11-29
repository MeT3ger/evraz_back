from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import os
from backend.controllers.zip_preproc import ZipPreproc

#from backend.controllers.handlers import Handlers
#from backend.dtos.backend_front import FrontDTO
from io import BytesIO

app = FastAPI()

@app.post("/zip")
async def zip(file: UploadFile = File(alias="some")):

    if file.content_type != "application/zip":
        raise HTTPException(status_code=400, detail="Uploaded file is not a ZIP archive.")
    
    file_content = await file.read()

    zip_arc = ZipPreproc(BytesIO(file_content))
    archieve = await zip_arc.fill_dict()

    return {"message": "zip"}