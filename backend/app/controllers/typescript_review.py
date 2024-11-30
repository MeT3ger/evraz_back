from backend.app.adapters.llm.exchange import LLM_Exchange
from data.consts.instruct_typescript import Instructions

async def typescript_review(user_file:str):

    nearests_prompts = 'some' # ! vladimir adapter !

    reviewed_result = await LLM_Exchange.mistral(
        user_file, 
        Instructions.project_struct,
        nearests_prompts
    )
    
    return reviewed_result