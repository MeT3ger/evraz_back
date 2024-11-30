from enum import Enum

from fastapi import UploadFile
from backend.app.adapters.llm.exchange import LLM_Exchange
from backend.app.adapters.faiss.exchange import FAISS_Exchange

from backend.extensions.ZipFile import ZipFile
from data.consts.instruct import Instructions

class LanguageType(Enum):
    python = "py"
    typescript = "ts"
    csharp = "cs"

async def code_review_zip(zip: ZipFile, languague: LanguageType):
    user_project_struct = await zip.project_struct()
    
    nearests_prompts = FAISS_Exchange.Extract_Similar_Codes.project(
        user_project_struct, 
        10
    )
 
    reviewed_result = await LLM_Exchange.mistral(
        user_project_struct, 
        Instructions.project_struct,
        nearests_prompts
    )
    
    return reviewed_result
    

async def code_review_file(file: UploadFile, languague: LanguageType):
    user_project_struct = await file.project_struct()

    nearests_prompts = FAISS_Exchange.Extract_Similar_Codes.file(
        user_project_struct, 
        10
    )
    
    reviewed_result = await LLM_Exchange.mistral(
        user_project_struct, 
        Instructions.project_struct,
        nearests_prompts
    )
    
    return reviewed_result

