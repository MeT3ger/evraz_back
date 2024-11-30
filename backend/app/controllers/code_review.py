from backend.app.adapters.llm.exchange import LLM_Exchange
from backend.helpers.ZipFile import ZipFile
from data.consts.instruct import Instructions, instruct_pdf, projects_dataset

async def code_review(file: ZipFile):
    await file.display_json() # TODO: delete it

    nearests_prompts = "some" # ! vladimir adapter !
    
    # надо понять на каком слое выбирать Instructions
    reviewed_result = LLM_Exchange.mistral(file, Instructions.file_struct, nearests_prompts)
    
    return reviewed_result