from backend.app.adapters.faiss.create_db_for_code import FAISSManager
from backend.app.adapters.faiss.create_db_for_structures import FAISSManager_structure
import os

class FAISS_Exchange:

    async def extract_k_most_similar_codes(query, k):
    
        faiss_manager = FAISSManager()
        faiss_manager.load_index()
        results = await faiss_manager.similarity_search(query)

        if results:
            top_results = results[:k]
            combined_content = "\n\n".join(
             [result.page_content for result in top_results]
            )  
            return combined_content
        else:
            return "Результат не найден"
        
    async def extract_k_most_similar_structures(query, k):
        faiss_manager = FAISSManager_structure()
        faiss_manager.load_index()
        results = faiss_manager.search(query, k)
        output = "\n".join(results)
        return output
 
 
