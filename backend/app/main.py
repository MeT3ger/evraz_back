from fastapi import FastAPI, File, UploadFile, HTTPException
from backend.parsers.zip_preproc import ZipPreproc
from backend.app.llm_exchange import LLM_Connector
from backend.helpers.file_library import GetDataBase
from data.consts.instruct import Instructions

from io import BytesIO

app = FastAPI()
instruct_pdf = Instructions.project_struct
print('Instruct loaded')
projects_dataset = GetDataBase.get_db()
print('Datasets loaded')

@app.post("/zip")
async def zip(file: UploadFile = File(alias="some")):

    if file.content_type != "application/zip":
        raise HTTPException(status_code=400, detail="Uploaded file is not a ZIP archive.")
    
    file_content = await file.read()

    zip_arc = ZipPreproc(BytesIO(file_content))
    archieve = await zip_arc.fill_dict()
    await zip_arc.display_json()

    llm_preproc = LLM_Connector()
    global instruct_pdf, projects_dataset
    await llm_preproc.create_prompt(user_content=archieve, 
                              database_content=projects_dataset,
                              instruct_content=instruct_pdf)
    
    llm_answer = llm_preproc.send_request_to_mistral()

    return llm_answer