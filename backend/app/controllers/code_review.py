from fastapi import UploadFile
from backend.app.adapters.llm.exchange import LLM_Exchange
from backend.app.adapters.faiss.exchange import FAISS_Exchange

from backend.extensions.ZipFile import ZipFile
from data.consts.instruct import Instructions
from data.consts.languague import Language

async def code_review_zip(zip: ZipFile, languague: Language):
    user_project_struct = await zip.project_struct()
    
    nearests_prompts = await FAISS_Exchange.Extract_Similar_Codes.project(
        user_project_struct, 
        10
    )
    
    #print(nearests_prompts)
 
    if languague == 'py':
        reviewed_result = await LLM_Exchange.mistral(
            user_project_struct, 
            Instructions.project_struct_py,
            nearests_prompts
        )
    elif languague == 'ts':
        reviewed_result = await LLM_Exchange.mistral(
            user_project_struct, 
            Instructions.file_struct_ts,
            nearests_prompts
        )
    else:
        print("Error type")
        return {'error': 'no such type'}
    
    return reviewed_result
    

async def code_review_file(file: UploadFile, languague: Language):
    user_project_struct = await file.file.read()

    nearests_prompts = FAISS_Exchange.Extract_Similar_Codes.file(
        user_project_struct, 
        10
    )

    if languague == 'py':
        reviewed_result = await LLM_Exchange.mistral(
            user_project_struct, 
            Instructions.file_struct_py,
            nearests_prompts
        )
    elif languague == 'ts':
        reviewed_result = await LLM_Exchange.mistral(
            user_project_struct, 
            Instructions.file_struct_ts,
            nearests_prompts
        )
    else:
        return {'error': 'no such type'}
    
    return reviewed_result

