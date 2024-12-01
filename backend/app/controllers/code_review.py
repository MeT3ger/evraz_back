from fastapi import UploadFile
from backend.app.adapters.llm.exchange import LLM_Exchange

from backend.extensions.zip_file import ZipFile
from data.consts.instruct import Instructions
from data.consts.languague import Language

async def code_review_zip(zip: ZipFile, languague: Language):
    user_project_struct = await zip.project_struct()
    
    instructions = ""
    if languague == Language.python:
        instructions = Instructions.project_struct_py
    elif languague == Language.csharp:
        instructions = Instructions.project_struct_cs
    elif languague == Language.typescript:
        instructions = Instructions.project_struct_ts
 
    reviewed_result = await LLM_Exchange.mistral(
        user_project_struct, 
        instructions,
        "",
        is_this_project=True
    )
    
    return reviewed_result
    

async def code_review_file(file: UploadFile, languague: Language):
    user_project_struct = file.file.read()
    
    instructions = ""
    if languague == Language.python:
        instructions = Instructions.file_struct_py
    elif languague == Language.csharp:
        instructions = Instructions.file_struct_cs
    elif languague == Language.typescript:
        instructions = Instructions.file_struct_ts
    
    reviewed_result = await LLM_Exchange.mistral(
        user_project_struct, 
        instructions,
        "",
        is_this_project=False
    )
    
    return reviewed_result

