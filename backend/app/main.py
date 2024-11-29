from fastapi import FastAPI, File, UploadFile, HTTPException
from backend.parsers.zip_preproc import ZipPreproc
from backend.parsers.pdf_parser import LoadPDF
from backend.app.llm_exchange import LLM_Connector

from io import BytesIO

app = FastAPI()
pdfLoader = LoadPDF()
instruct_pdf = pdfLoader.load_pdf()
projects_dataset = 'Тут должны быть проекты, но пока их нет'

@app.post("/zip")
async def zip(file: UploadFile = File(alias="some")):

    if file.content_type != "application/zip":
        raise HTTPException(status_code=400, detail="Uploaded file is not a ZIP archive.")
    
    file_content = await file.read()
    print('File read')

    zip_arc = ZipPreproc(BytesIO(file_content))
    archieve = await zip_arc.fill_dict()
    print('User data got')

    llm_preproc = LLM_Connector()
    await llm_preproc.create_prompt(user_content=archieve, 
                              database_content=projects_dataset,
                              instruct_content=instruct_pdf)
    print('LLM prompt created')
    
    llm_answer = llm_preproc.send_request_to_mistral()
    print('LLM answer got')

    return llm_answer