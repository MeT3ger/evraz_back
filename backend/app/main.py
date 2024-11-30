from fastapi import FastAPI, File, HTTPException, UploadFile

from backend.app.controllers.code_review import code_review
from backend.app.controllers.python_review import python_review
from backend.app.controllers.csharp_review import csharp_review
from backend.app.controllers.typescript_review import typescript_review
from backend.app.controllers.return_pdf import CreatePDF
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
    
    answ_pdf = await CreatePDF.create(refactored_code)
    
    return answ_pdf # dto

@app.post("/file")
async def zip_code_review(file: UploadFile = File(alias="some")):
    if  not file.filename.endswith('.py') and\
        not file.filename.endswith('.cs') and\
        not file.filename.endswith('.ts'):
        raise HTTPException(status_code=400, detail="Uploaded file is not a Python, C# or TypeScript file.")
    
    file_income = file.file.read()
    answer = ''

    if file.filename.endswith('.py'):
        answer = python_review(file_income)
    elif file.filename.endswith('.cs'):
        answer = csharp_review(file_income)
    elif file.filename.endswith('.ts'):
        answer = typescript_review(file_income)

    answ_pdf = await CreatePDF.create(answer)

    return answ_pdf