from backend.app.adapters.faiss.helpers.create_db_for_code import FAISS_File_Search
from backend.app.adapters.faiss.helpers.create_db_for_structures import FAISS_Structure_Search

File_Search = FAISS_File_Search()
Project_Search = FAISS_Structure_Search()

class FAISS_Exchange:
    class Extract_Similar_Codes:
        async def file(query, k):
            results = await File_Search.similarity_search(query)

            if results:
                top_results = results[:k]
                combined_content = "\n\n".join(
                    [result.page_content for result in top_results]
                )  
                return combined_content
            else:
                return ""
            
        async def project(query, k):
            results = await Project_Search.similary_search(query, k)
            output = "\n".join(results)
            return output