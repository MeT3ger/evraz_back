from backend.app.adapters.llm.exchange import LLM_Exchange
from backend.extensions.ZipFile import ZipFile
from data.consts.instruct import Instructions

async def code_review(file: ZipFile):
    # возможно стоит добавить функцию которая отвечает на вопрос это проект или файл (???)
    user_project_struct = file.project_struct()

    nearests_prompts = "some" # ! vladimir adapter !
    
    # надо понять на каком слое выбирать Instructions
    # заменить file на его структуру проекта
    reviewed_result = LLM_Exchange.mistral(
        user_project_struct, 
        Instructions.project_struct,
        nearests_prompts
    )
    
    return reviewed_result