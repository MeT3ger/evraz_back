from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse

from backend.app.controllers.code_review import code_review
from backend.extensions.ZipFile import ZipFile
from backend.app.controllers.return_pdf import CreatePDF

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
    
    pdf = await CreatePDF.create(refactored_code)
    
    return StreamingResponse(
        pdf, 
        media_type='application/pdf', 
        headers={"Content-Disposition": "attachment; filename=document.pdf"}
    )