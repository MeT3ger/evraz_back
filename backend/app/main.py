from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
import os
from backend.controllers.zip_preproc import ZipPreproc

from backend.controllers.handlers import Handlers
from backend.dtos.backend_front import FrontDTO
import aiofiles
from io import BytesIO
import zipfile

app = FastAPI()

@app.post("/zip")
async def zip(file: UploadFile = File(alias="some")):

    if file.content_type != "application/zip":
        raise HTTPException(status_code=400, detail="Uploaded file is not a ZIP archive.")
    
    file_content = await file.read()
    file_location = 'reseived.json'

    file_location = f"data/data_reseived/reseived.json"

    zip_arc = ZipPreproc(BytesIO(file_content))
    #await zip_arc.display_json()
    await zip_arc.create_json(file_location)

    return {"message": "zip"}