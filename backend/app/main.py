from fastapi import FastAPI, File, HTTPException, UploadFile

from backend.app.controllers.code_review import code_review
from backend.extensions.ZipFile import ZipFile

app = FastAPI()

@app.post("/foo")
async def foo():
    return {"message": "Hello, World!"}


@app.post("/zip")
async def zip_code_review(file: UploadFile = File(alias="some")):
    if file.content_type != "application/zip":
        raise HTTPException(status_code=400, detail="Uploaded file is not a ZIP archive.")
    zip = ZipFile(file)
    
    refactored_code = await code_review(zip)
    
    # dto = PDF_dto.json(refactored_code)
    
    return refactored_code # dto