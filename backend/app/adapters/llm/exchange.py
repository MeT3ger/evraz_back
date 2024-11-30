import requests
from backend.app.adapters.llm.params import LLM_Params
from data.consts.instruct import Instructions

class LLM_Exchange:

    async def mistral(file: str, file_type: Instructions, top_similarity_framgents: str, headers = {}, http_addr = ''):
        if headers == {}:
            headers = LLM_Params.headers
        
        if http_addr == '':
            http_addr = LLM_Params.http_addr

        response = requests.post(
            http_addr, 
            headers=headers, 
            json=LLM_Params.body(file, file_type, top_similarity_framgents)
        )
        answer = response.json()

        return answer