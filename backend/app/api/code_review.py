from backend.extensions.pdf_buffer import CreatePDF
from backend.extensions.zip_file import ZipFile
from fastapi.responses import StreamingResponse
from backend.app.controllers.code_review import code_review_file, code_review_zip
from data.consts.languague import Language
from fastapi import APIRouter, File, UploadFile, Header

router = APIRouter()

@router.post("/foo")
async def foo():
    return {"message": "Hello, World!"}

@router.post("/zip")
async def zip_code_review(type: Language = Header(), file: UploadFile = File(alias="some")):
    zip = ZipFile(file)
    
    refactored_code = await code_review_zip(zip, type)
    if refactored_code['error'] != None:
        refactored_code = {"choices": [{"message": {"content": ""}}]}
        
    pdf = CreatePDF.create(refactored_code) 

    return StreamingResponse(
        pdf, 
        media_type='application/pdf; charset=UTF-8"', 
        headers={"Content-Disposition": "attachment; filename=document.pdf"}
    )
    
@router.post("/file")
async def zip_code_review(type: Language = Header(), file: UploadFile = File(alias="some")):
    refactored_code = await code_review_file(file, type)
    if refactored_code['error'] != None:
        refactored_code = {"choices": [{"message": {"content": ""}}]}
        
    pdf = CreatePDF.create(refactored_code)

    return StreamingResponse(
        pdf, 
        media_type='application/pdf; charset=UTF-8"', 
        headers={"Content-Disposition": "attachment; filename=document.pdf"}
    )