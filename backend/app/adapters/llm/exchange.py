import asyncio

from fastapi import HTTPException
import httpx 
from backend.app.adapters.llm.params import LLM_Params
from data.consts.instruct import Instructions

MAX_RETRIES = 100
TIMEOUT = 3000

class LLM_Exchange:

    async def mistral(
        file: str, 
        file_type: Instructions, 
        top_similarity_framgents: str, 
        is_this_project: bool, 
        headers = {}, 
        http_addr = ''
    ):
        if headers == {}:
            headers = LLM_Params.headers
        
        if http_addr == '':
            http_addr = LLM_Params.http_addr
            
        for attempt in range(MAX_RETRIES):
            try:
                async with httpx.AsyncClient(timeout=httpx.Timeout(TIMEOUT)) as client:
                    response = await client.post(
                    http_addr, 
                    headers=headers, 
                    json=LLM_Params.body(file, file_type, top_similarity_framgents, is_this_project),
                )
                break
            except Exception as e:
                print(f"Attempt {attempt + 1} failed with error: {e}")
                if attempt < MAX_RETRIES - 1:
                    await asyncio.sleep(2)
                else:
                    raise HTTPException(
                        status_code=500, 
                        detail="Failed to process the ZIP file after multiple attempts."
                    )
            
        answer = response.json()

        return answer