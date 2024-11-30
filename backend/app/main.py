from fastapi import FastAPI, File, HTTPException, UploadFile
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
async def zip_code_review(file: UploadFile = File(alias="some")):
    if file.content_type != "application/zip":
        raise HTTPException(status_code=400, detail="Uploaded file is not a ZIP archive.")
    zip = ZipFile(file)
    
    refactored_code = await code_review_zip(zip, Language.python) # TODO:
    
    print(refactored_code)
    
    pdf = await CreatePDF.create(refactored_code)
    
    return StreamingResponse(
        pdf, 
        media_type='application/pdf', 
        headers={"Content-Disposition": "attachment; filename=document.pdf"}
    )
    
# @app.post("/file")
# async def zip_code_review(file: UploadFile = File(alias="some")):
#     if  not file.filename.endswith('.py') and\
#         not file.filename.endswith('.cs') and\
#         not file.filename.endswith('.ts'):
#         raise HTTPException(status_code=400, detail="Uploaded file is not a Python, C# or TypeScript file.")
    
#     #lang = Language.
    
#     file_income = file.file.read()

#     if file.filename.endswith('.py'):
#         answer = python_review(file_income)
#     elif file.filename.endswith('.cs'):
#         answer = csharp_review(file_income)
#     elif file.filename.endswith('.ts'):
#         answer = typescript_review(file_income)

#     answ_pdf = await CreatePDF.create(answer)

#     return answ_pdf