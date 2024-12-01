import asyncio

from fastapi import HTTPException
import httpx 
from backend.app.adapters.llm.params import LLM_Params
from data.consts.instruct import Instructions
from data.consts.languague import Language

class LLM_Exchange:

    async def mistral(file: str, instruction: Instructions, top_similarity_framgents: str, headers = {}, http_addr = '', is_this_project = True):
        if headers == {}:
            headers = LLM_Params.headers
        
        if http_addr == '':
            http_addr = LLM_Params.http_addr
            
        
        MAX_RETRIES = 1000
            
        for attempt in range(MAX_RETRIES):
            try:
                async with httpx.AsyncClient(timeout=httpx.Timeout(600)) as client:  # Use httpx.AsyncClient for async requests
                    response = await client.post(
                    http_addr, 
                    headers=headers, 
                    json=LLM_Params.body(file, instruction, top_similarity_framgents, is_this_project),
                )
                break  # Exit the loop if the request was successful
            except Exception as e:  # Log the exception if needed
                print(f"Attempt {attempt + 1} failed with error: {e}")
                if attempt < MAX_RETRIES - 1:  # If not the last attempt, you might want to wait before retrying
                    await asyncio.sleep(2)  # Optional: wait for a second before retrying
                else:
                    raise HTTPException(status_code=500, detail="Failed to process the ZIP file after multiple attempts.")  # Raise an error after the last attempt
            
        answer = response.json()

        return answer