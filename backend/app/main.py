from fastapi import FastAPI, File, HTTPException, Header, UploadFile
from fastapi.responses import StreamingResponse

from backend.app.controllers.code_review import code_review_zip, code_review_file
from backend.extensions.ZipFile import ZipFile
from backend.app.controllers.return_pdf import CreatePDF
from data.consts.languague import Language

app = FastAPI()

@app.post("/foo")
async def foo():
    return {"message": "Hello, World!"}


@app.post("/zip")
async def zip_code_review(type: Language = Header(), file: UploadFile = File(alias="some")):
    if file.content_type != "application/zip":
        raise HTTPException(status_code=400, detail="Uploaded file is not a ZIP archive.")
    zip = ZipFile(file)
    
    
    refactored_code = await code_review_zip(zip, Language.python) # TODO:
        
    
    pdf = CreatePDF.create(refactored_code) 

    return StreamingResponse(
        pdf, 
        media_type='application/pdf; charset=UTF-8"', 
        headers={"Content-Disposition": "attachment; filename=document.pdf"}
    )
    
@app.post("/file")
async def zip_code_review(type: Language = Header(), file: UploadFile = File(alias="some")):
    file_income = file.file.read()

    mistral_answer = code_review_file(file_income, file.filename[-2:])
    # elif file.filename.endswith('.ts'):
    #     answer = typescript_review(file_income)clear

    # answ_pdf = await CreatePDF.create(answer)

    return { "type": type }